#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Suite de verificacao Ponta a Ponta (E2E) do sistema de automacao do curso:
1) Emissao A4 + envio por e-mail + devolucao via foto PNG por e-mail + Aprovacao 100% (B05 -> B06)
2) Falha na 1a tentativa de B06 (erro 1 <= x <= 10 + tempo excedido) -> Feedback + Variante V2
3) Falha na 2a tentativa de B06 (V2) -> Regra das 2 Tentativas -> Recuo automatico para B03
4) Sincronizacao com 00_acompanhamento.csv (12 colunas), metricas JEV lightShare >= 60%,
   endpoints HTTP do Dashboard e geracao de dashboard_evolucao.html.
"""

import base64
import csv
import json
import os
import shutil
import sys
import threading
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import banco_dados
import config
import extrator_ocr
import servidor_dashboard
import servico_email
from catalogo_curricular import CatalogoCurricular
from corretor_automatico import OrquestradorCurso


def _limpar_ambiente_teste():
    for path in [config.DB_PATH]:
        if os.path.isfile(path):
            os.remove(path)
    for folder in [
        config.FOLHAS_DIR,
        config.SPOOL_ENVIADOS_DIR,
        config.SPOOL_RECEBIDOS_DIR,
        config.UPLOADS_DIR,
    ]:
        if os.path.isdir(folder):
            shutil.rmtree(folder)
    config.garantir_diretorios()


def _assert(cond: bool, msg: str):
    if not cond:
        raise AssertionError(msg)


def main():
    print("=== INICIANDO VERIFICACAO PONTA A PONTA (E2E) DA AUTOMACAO DO CURSO ===")

    # Backup do 00_acompanhamento.csv oficial para nao poluir apos o teste
    with open(config.CSV_ACOMPANHAMENTO_PATH, "r", encoding="utf-8") as f:
        csv_original = f.read()

    try:
        _limpar_ambiente_teste()
        catalogo = CatalogoCurricular()
        todos = catalogo.carregar_todos()
        _assert(len(todos) == 73, f"Esperado 73 blocos, obtido {len(todos)}")
        print(f"[OK] Catalogo carregou {len(todos)}/73 blocos curriculares.")

        orq = OrquestradorCurso(catalogo)
        aluno = banco_dados.obter_ou_criar_aluno(
            nome="Ana Silva (Piloto E2E)",
            email="ana.silva@alunos.utfpr.edu.br",
            bloco_inicial="B05",
            modo_inicial="checagem",
        )

        # ------------------------------------------------------------------
        # CENARIO 1: Emissao B05, retorno por e-mail com foto PNG 100% -> B06
        # ------------------------------------------------------------------
        print("\n--- Cenario 1: B05 (Checagem V1 T1) -> Foto PNG via E-mail -> Aprovacao 100% -> B06 ---")
        emit1 = orq.emitir_e_enviar_prova(aluno["id"])
        prot1 = emit1["prova"]["protocolo"]
        _assert(os.path.isfile(emit1["folha"]["caminho_folha_html"]), "Folha A4 B05 nao gerada.")
        _assert(os.path.isfile(emit1["email"]["caminho_eml"]), "E-mail B05 nao gravado no spool.")

        # Simula aluno abrindo cronometro antes de escrever na folha
        banco_dados.iniciar_cronometro_prova(prot1)

        # Ler codigo de referencia real de B05-C03 do gabarito
        b05 = catalogo.obter("B05")
        q_b05_c03 = [q for q in b05.questoes_checagem if q.questao_id == "B05-C03"][0]

        respostas_b05 = {
            "B05-C01": (
                "nota = 2.9 -> avalia 1 condicao (2.9 < 3.0) -> Insuficiente; "
                "nota = 3.0 -> avalia 2 condicoes (3.0 < 6.0) -> Recuperacao; "
                "nota = 6.0 -> avalia 3 condicoes (6.0 < 9.0) -> Bom; "
                "nota = 9.0 -> avalia 3 condicoes -> else -> Excelente."
            ),
            "B05-C02": (
                '#include <stdio.h>\nint main(void) {\n    double mbps, preco;\n    scanf("%lf", &mbps);\n'
                '    if (mbps <= 20.0) { preco = 79.90; } else if (mbps <= 100.0) { preco = 109.90; }\n'
                '    else if (mbps <= 300.0) { preco = 149.90; } else { preco = 199.90; }\n'
                '    printf("Plano: R$ %.2f\\n", preco);\n    return 0;\n}'
            ),
            "B05-C03": q_b05_c03.codigo_referencia,
        }

        foto1 = os.path.join(config.AUTOMACAO_DIR, "dados", f"foto_{prot1}.png")
        extrator_ocr.gerar_foto_prova_manuscrita_simulada(
            caminho_saida_png=foto1,
            protocolo=prot1,
            bloco_id="B05",
            aluno_nome=aluno["nome"],
            tempo_min=16,
            respostas=respostas_b05,
        )

        # Simula resposta de e-mail do aluno com a foto anexada
        servico_email.simular_resposta_email_aluno(prot1, aluno["email"], foto1)
        resultados_c1 = orq.processar_caixa_email_e_corrigir()
        _assert(len(resultados_c1) == 1, f"Esperado 1 resposta coletada do e-mail, obtido {len(resultados_c1)}")

        r1 = resultados_c1[0]
        _assert(r1["acertos"] == 3 and r1["total"] == 3, f"Esperado 3/3 em B05, obtido {r1['acertos']}/{r1['total']}")
        _assert(r1["percentual"] == 100.0, "Percentual deve ser 100%")
        _assert(r1["fluencia_codigo"] == "dentro_meta", f"Fluencia inesperada: {r1['fluencia_codigo']}")
        _assert(r1["proxima_acao"] == "AVANCAR_B06", f"Esperado AVANCAR_B06, obtido {r1['proxima_acao']}")
        _assert(r1["proxima_folha"] is not None and r1["proxima_folha"]["protocolo"].startswith("PREP-B06-V1-T1"), "Folha B06 nao foi auto-emitida!")

        aluno_apos_1 = banco_dados.obter_aluno_por_id(aluno["id"])
        _assert(aluno_apos_1["bloco_atual"] == "B06", f"Aluno deveria estar em B06, mas esta em {aluno_apos_1['bloco_atual']}")
        print(f"[OK] Cenario 1 aprovado: {r1['acertos']}/{r1['total']} em {r1['tempo_declarado_min']} min -> {r1['proxima_acao']}")

        # ------------------------------------------------------------------
        # CENARIO 2: Falha em B06 T1 (bug 1 <= x <= 10 e tempo 24 min) -> V2
        # ------------------------------------------------------------------
        print("\n--- Cenario 2: B06 (V1 T1) com erro 'min <= x <= max' + tempo 24 min -> Variante V2 ---")
        prot2 = r1["proxima_folha"]["protocolo"]
        b06 = catalogo.obter("B06")
        respostas_b06_erro = {}
        for q in b06.obter_questoes("checagem"):
            if q.tipo in ("codigo", "bug") or q.codigo_referencia:
                # Injeta erro classico de comparacao encadeada 18 <= idade <= 35 em uma das questoes
                if q.questao_id == "B06-C02":
                    respostas_b06_erro[q.questao_id] = (
                        '#include <stdio.h>\nint main(void) {\n    double nota; int freq;\n'
                        '    scanf("%lf %d", &nota, &freq);\n'
                        '    if (6 <= nota <= 10 && freq >= 75) {\n        printf("Aprovado\\n");\n    }\n'
                        '    return 0;\n}'
                    )
                else:
                    respostas_b06_erro[q.questao_id] = q.codigo_referencia
            else:
                respostas_b06_erro[q.questao_id] = "0 e 1"

        foto2 = os.path.join(config.AUTOMACAO_DIR, "dados", f"foto_{prot2}.png")
        extrator_ocr.gerar_foto_prova_manuscrita_simulada(
            caminho_saida_png=foto2,
            protocolo=prot2,
            bloco_id="B06",
            aluno_nome=aluno["nome"],
            tempo_min=24,  # Meta e 18 -> excedido (> 22.5)
            respostas=respostas_b06_erro,
        )
        r2 = orq.processar_submissao_imagem(foto2)
        _assert(not r2["aprovado"], "B06 T1 deveria reprovar devido ao erro 6 <= nota <= 10!")
        _assert(r2["fluencia_codigo"] == "excedido_alerta", f"Esperado excedido_alerta, obtido {r2['fluencia_codigo']}")
        _assert(r2["proxima_acao"] == "RECUPERACAO_V2_B06", f"Esperado RECUPERACAO_V2_B06, obtido {r2['proxima_acao']}")
        _assert(any(it["categoria_erro"] == "comparacao_encadeada" for it in r2["itens"]), "Nao detectou categoria comparacao_encadeada!")

        aluno_apos_2 = banco_dados.obter_aluno_por_id(aluno["id"])
        _assert(aluno_apos_2["bloco_atual"] == "B06" and aluno_apos_2["variante_atual"] == "V2" and aluno_apos_2["tentativa_bloco"] == 2,
                f"Estado incorreto apos 1a falha: {aluno_apos_2}")
        print(f"[OK] Cenario 2 aprovado: Erro detectado (comparacao_encadeada) + alerta de tempo -> {r2['proxima_acao']}")

        # ------------------------------------------------------------------
        # CENARIO 3: 2a falha consecutiva em B06 (V2 T2) -> Recuo para B03
        # ------------------------------------------------------------------
        print("\n--- Cenario 3: B06 (V2 T2) com nova falha -> Regra 2 Tentativas -> Recuo para B03 ---")
        prot3 = r2["proxima_folha"]["protocolo"]
        _assert(prot3.startswith("PREP-B06-V2-T2"), f"Protocolo V2 invalido: {prot3}")

        respostas_b06_erro2 = {q.questao_id: "" for q in b06.obter_questoes("checagem")}
        respostas_b06_erro2["B06-C02"] = '#include <stdio.h>\nint main(void) {\n    int x;\n    if (x = 5) { printf("Ok\\n"); }\n    return 0;\n}'

        foto3 = os.path.join(config.AUTOMACAO_DIR, "dados", f"foto_{prot3}.png")
        extrator_ocr.gerar_foto_prova_manuscrita_simulada(
            caminho_saida_png=foto3,
            protocolo=prot3,
            bloco_id="B06",
            aluno_nome=aluno["nome"],
            tempo_min=20,
            respostas=respostas_b06_erro2,
        )
        r3 = orq.processar_submissao_imagem(foto3)
        _assert(r3["proxima_acao"] == "RECUO_PREREQUISITO_B03", f"Esperado RECUO_PREREQUISITO_B03, obtido {r3['proxima_acao']}")

        aluno_apos_3 = banco_dados.obter_aluno_por_id(aluno["id"])
        _assert(aluno_apos_3["bloco_atual"] == "B03" and aluno_apos_3["variante_atual"] == "V1" and aluno_apos_3["tentativa_bloco"] == 1,
                f"Deveria ter recuado para B03 V1 T1, obtido {aluno_apos_3}")
        print(f"[OK] Cenario 3 aprovado: Regra das 2 tentativas acionada -> {r3['proxima_acao']}")

        # ------------------------------------------------------------------
        # CENARIO 4: CSV 12 colunas + JEV lightShare + HTTP Server + Snapshot
        # ------------------------------------------------------------------
        print("\n--- Cenario 4: Verificando 00_acompanhamento.csv, JEV lightShare, HTTP API e Snapshot ---")
        linhas_csv = banco_dados.ler_acompanhamento_csv()
        _assert(len(linhas_csv) == 3, f"Esperado 3 linhas no CSV, obtido {len(linhas_csv)}")
        for lc in linhas_csv:
            _assert(len(lc.keys()) == 12, f"Colunas divergentes no CSV: {len(lc.keys())}")

        jev_resumo = banco_dados.obter_metricas_jev_resumo()
        print(f"    Metricas JEV: {jev_resumo}")
        _assert(jev_resumo["light_share_pct"] >= 60.0, f"lightShare abaixo da meta 60%: {jev_resumo['light_share_pct']}%")

        # Testar servidor HTTP real em porta efemera (0)
        srv = servidor_dashboard.criar_servidor(host="127.0.0.1", port=0)
        port = srv.server_address[1]
        t = threading.Thread(target=srv.serve_forever, daemon=True)
        t.start()
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{port}/api/estado", timeout=5) as resp:
                _assert(resp.status == 200, "GET /api/estado falhou")
                estado_http = json.loads(resp.read().decode("utf-8"))
                _assert(len(estado_http["mapa_blocos"]) == 73, "Mapa HTTP deve conter 73 blocos")
                _assert(estado_http["aluno_ativo"]["bloco_atual"] == "B03", "Estado HTTP deve refletir recuo para B03")

            with urllib.request.urlopen(f"http://127.0.0.1:{port}/folha/{prot1}", timeout=5) as resp_f:
                _assert(resp_f.status == 200, "GET /folha/ falhou")
                _assert(prot1 in resp_f.read().decode("utf-8"), "Folha servida nao contem o protocolo")

            # Teste POST upload base64 via API (emissao + submissao minima de verificacao)
            req_emit = urllib.request.Request(
                f"http://127.0.0.1:{port}/api/emitir-prova",
                data=json.dumps({"aluno_id": aluno["id"]}).encode("utf-8"),
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(req_emit, timeout=5) as resp_e:
                _assert(resp_e.status == 200, "POST /api/emitir-prova falhou")

            snap_path = servidor_dashboard.gerar_snapshot_dashboard(aluno["id"])
            _assert(os.path.isfile(snap_path) and os.path.getsize(snap_path) > 5000, "Snapshot dashboard_evolucao.html invalido")
        finally:
            srv.shutdown()
            srv.server_close()

        print(f"[OK] Cenario 4 aprovado: CSV sincronizado (12 colunas), JEV lightShare={jev_resumo['light_share_pct']}%, HTTP API e Snapshot OK.")
        print("\n=====================================================================")
        print(">>> VERIFICACAO PONTA A PONTA (E2E) CONCLUIDA COM 100% DE SUCESSO <<<")
        print("=====================================================================")
    finally:
        # Restaurar 00_acompanhamento.csv limpo para preservar estado oficial de entrega
        with open(config.CSV_ACOMPANHAMENTO_PATH, "w", encoding="utf-8", newline="") as f:
            f.write(csv_original)


if __name__ == "__main__":
    main()
