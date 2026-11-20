# Guia do Orientador — Curso de Algoritmos e Programação em C (UTFPR-PG)

> **Identidade Pedagógica:** Este manual orienta a condução de um curso de prática independente, micro-passos graduados e aprendizagem por domínio, **estruturado** como um programa de **Preparação Intensiva** (aprendizagem por domínio, micro-passos graduados e prática independente).  
> **Alinhamento Curricular:** Escopo integralmente baseado nos materiais auditados de `CC61A - Algoritmos` da UTFPR – Campus Ponta Grossa ([00_inventario_fontes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/00_inventario_fontes.md) e [00_mapa_curricular.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/00_mapa_curricular.md)).

---

## 1. Papel do Orientador e Regras Invioláveis de Escopo

- **Não antecipar conteúdo:** Cada bloco isola uma única micro-habilidade nova e proíbe recursos de blocos futuros (ex.: não usar `&&`/`||` em `B05`; não passar vetores como parâmetros antes de `F06`; não usar laços em recursividade).
- **Respeitar o escopo negativo da disciplina:** Não exigir nem ensinar `struct`, alocação dinâmica (`malloc`/`free`), VLAs, aritmética de ponteiros, ordenação própria (fornecida no Trabalho) ou construção do zero de parser `FILE*` para PGM.
- **Rigor terminológico em C:** Descrever sempre a passagem de parâmetros em C como **passagem por valor** (cópia). Quando a função recebe ponteiro, explicar como **passagem de endereço por valor** (evitando o termo impreciso "passagem por referência").
- **Autonomia progressiva:** Seguir em cada bloco a curva de retirada de apoio:  
  `1. Exemplo resolvido → 2. Completar lacunas → 3. Resolver com pistas → 4. Resolver sozinho`.

---

## 2. Aplicação do Diagnóstico e Posicionamento

1. Aplique [00_teste_diagnostico.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/00_teste_diagnostico.md) **sem consulta e sem compilador**.
2. Aplique rigorosamente as **Regras de Interrupção (`I1`–`I5`)**:
   - **Nunca** exponha o estudante a itens muito além do seu nível após 2 falhas seguidas (`I1`), falha em `T1` (`I2`) ou falha no item-âncora de uma sondagem (`I4`).
   - Limite a sessão diagnóstica a no máximo 2 sondagens (`I5`).
3. Corrija com [00_gabarito_diagnostico.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/00_gabarito_diagnostico.md) e posicione **pelo menor pré-requisito não demonstrado**, nunca pela soma bruta de acertos.
4. **Confirmação de Posicionamento Provisório:** Sempre que o posicionamento for marcado como `PROVISÓRIO`, observe atentamente as **2 primeiras sessões**:
   - Se o estudante resolver com fluência e passar na checagem independente de 1ª, confirme `DEFINITIVO` (e, em perfil "dente de serra", após sanar o pré-requisito pontual, permita avançar os blocos intermediários via checagem independente direta).
   - Se falhar no bloco de entrada provisório, recue imediatamente para os pré-requisitos indicados na Matriz de Decisão do diagnóstico.

---

## 3. Condução da Sessão Diária (15 a 25 Minutos)

> **Aviso sobre Tempos:** Todos os tempos-alvo especificados nos blocos são **estimativas iniciais sujeitas à calibração** empírica. Use o cronômetro para registrar `tempo_resolucao`, nunca como punição ou substituto de compreensão.

| Momento da Sessão | Duração Típica | O que o Aluno Faz | O que o Orientador Faz |
|---|---:|---|---|
| **A. Leitura e Exemplos** | 2–3 min | Lê as instruções curtas e acompanha os 1–2 exemplos resolvidos. | Garante que o aluno não pule o exemplo antes de iniciar os exercícios. |
| **B. Resolução Independente** | 10–15 min | Resolve os exercícios no papel (teste de mesa) e/ou no código sem consultar o gabarito. | Cronometra o tempo líquido (`tempo_resolucao`). Não dá a resposta pronta; redireciona ao exemplo se travar. |
| **C. Correção (Autocorreção + Conferência)** | 4–6 min | Confere com o gabarito/casos de teste, anota **acertos de 1ª tentativa** e realiza autocorreção dos erros. | Registra separadamente `acertos_iniciais` e `acertos_apos_correcao`. Confere se a correção foi real, não apenas cópia mecânica. |
| **D. Checagem ou Recuperação** | 3–5 min *(ou sessão extra)* | Se completou a bateria, realiza a **Checagem Independente** (sem gabarito). | Aplica critério de **100% na checagem** para liberar avanço ou define recuperação direcionada. |

- Blocos com maior carga de escrita de código (ex.: os pilotos `B05`, `D02` e `F05`) dividem a bateria em **2 sessões de prática** (`Sessão 1`: Leitura, Teste de Mesa, Lacunas e Caça ao Bug; `Sessão 2`: Variações Controladas e Resolução Independente, mantendo `15–25 min` por sessão) e reservam uma **Checagem Independente dedicada (`15–18 min`)** para que nenhuma sessão ultrapasse o teto de 25 minutos. *(Na Fase 3, blocos densos também podem optar por 5 exercícios em 1–2 sessões para preservar a janela-alvo.)*

---

## 4. Critério de Domínio e Fluência

Para autorizar o avanço do bloco `X` para o bloco seguinte:
1. **Registro separado obrigatório:** Preencha `acertos_iniciais` (quantos exercícios da bateria o aluno acertou integralmente na 1ª tentativa) e `acertos_apos_correcao` (quantos passaram a estar corretos após autocorreção guiada).
2. **Autocorreção não basta:** Mesmo com `acertos_apos_correcao == total_questoes`, o aluno **não avança** sem cumprir a Checagem Independente.
3. **Checagem Independente (100% sem consulta):** O aluno deve acertar **100%** das questões inéditas equivalentes da checagem sem consultar o gabarito do bloco nem notas anteriores.
4. **Tempo como indicador complementar:**
   - Tempo dentro do alvo + 100% na checagem → **fluência sólida (`avancar`)**.
   - Tempo muito acima do estimado + 100% na checagem → **domínio alcançado com fluência baixa**: avançar normalmente ou recomendar revisão extra apenas se o aluno demonstrar insegurança evidente, evitando estagnação desnecessária.

---

## 5. Recuperação Direcionada e Regra das 2 Tentativas

### 5.1 Fluxo após Erro na Bateria ou na Checagem
- **Falha na 1ª tentativa (`tentativa = 1`):**
  1. Classifique o erro exato (`dificuldade_observada` no CSV: ex. *ordem invertida no else if*, *off-by-one*, *desempate > vs <=*, *uso de & incorreto*).
  2. Realize **recuperação direcionada** (2–5 min): refaça apenas o ponto conceitual que gerou o erro usando teste de mesa no papel.
  3. Aplique uma **variante equivalente (`variante = V2`, `tentativa = 2`)** do bloco (mesma micro-habilidade, novos valores e contextos, sem repetir mecanicamente os mesmos enunciados).

### 5.2 Regra das 2 Tentativas Malsucedidas (`tentativa >= 2`)
> **Proibição:** Nunca repita o mesmo bloco pela 3ª vez consecutiva sem investigar pré-requisitos.

Se o estudante reprovar na Checagem Independente pela **2ª vez** no mesmo bloco (`tentativa = 2`, `resultado_checagem = reprovado`):
1. Registre `proxima_acao = investigar_prerequisito` na ficha CSV.
2. Consulte os **pré-requisitos** declarados no cabeçalho do bloco e no grafo de [00_mapa_curricular.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/00_mapa_curricular.md).
3. Aplique 1–2 itens rápidos do(s) bloco(s) pré-requisito(s) usando a tabela diagnóstica abaixo antes de retomar o bloco original:

| Sintoma Observado no Bloco Atual | Pré-Requisito Provável em Falta | Ação de Recuperação na Base |
|---|---|---|
| Erra precedência de expressão ou divisão truncada em condicionais/médias (`B05`, `D02`) | `B01` / `B02` | Revisar divisão inteira, `(double)` *cast* e precedência. |
| Confunde `=` com `==` ou esquece chaves `{ }` (`B05`, `C01`+) | `B03` | Refazer caça ao bug de atribuição em `if` e delimitação de blocos. |
| Erra intervalo contínuo com lacuna (`<= 199.99` vs `< 200.0`) (`B05`) | `A09` / `B03` | Revisar representação real e comparações estritas/inclusivas. |
| Erra limites do `for` (`i <= n` acessa `v[n]`) (`D02`+) | `C05` / `D01` | Refazer contagem de iterações `0 .. n-1` e índices base 0. |
| Inicializa máximo/mínimo em `0` ou usa `else if` para extremos (`D02`) | `B04` / `D02` | Retomar dois `if`s independentes (`B04`) e candidato `v[0]`. |
| Confunde `p` com `*p` ou passa `&p` errado em funções (`F05`) | `F03` / `F04` | Refazer tabela de memória `a`, `&a`, `p`, `*p` no papel antes de programar. |
| Usa `for`/`while` dentro de função recursiva ou causa *stack overflow* (`G03`–`G08`) | `G01` / `G02` | Retomar rastreamento de pilha e caso base obrigatório. |

---

## 6. Uso da Ficha de Acompanhamento (`00_acompanhamento.csv`)

O arquivo [00_acompanhamento.csv](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/00_acompanhamento.csv) contém as **12 colunas obrigatórias** para controle longitudinal:

| Coluna | Tipo / Formato | Valores Permitidos e Significado |
|---|---|---|
| `data` | `AAAA-MM-DD` | Data da sessão. |
| `aluno` | Texto (ID/nome) | Identificação do estudante. |
| `bloco` | `A01`..`H06` ou `DIAG` | Código do bloco trabalhado (ou `DIAG` para sessão diagnóstica). |
| `variante` | `V1`, `V2`, `DIAG` | `V1` (bateria padrão), `V2` (variante equivalente de recuperação). |
| `tentativa` | Inteiro (`1`, `2`, ...) | Número da tentativa no bloco. |
| `tempo_resolucao` | Inteiro (minutos) | Tempo líquido de resolução da bateria (sem contar correção). |
| `acertos_iniciais` | Inteiro (`0..N`) | Exercícios da bateria totalmente corretos na **1ª tentativa**. |
| `total_questoes` | Inteiro (`N`) | Quantidade de exercícios praticados na sessão registrada (ex.: `3` por sessão em blocos de 2 sessões ou `5`–`6` em sessão única). |
| `acertos_apos_correcao` | Inteiro (`0..N`) | Total correto **após autocorreção** (sempre `>= acertos_iniciais`). |
| `resultado_checagem` | `aprovado` / `reprovado` / `pendente` | `aprovado` exige **100%** na checagem independente; `pendente` se bloco de 2 sessões na Sessão 1 (ou antes da checagem dedicada). |
| `dificuldade_observada` | Texto curto (sem vírgula) | Descrição objetiva do erro predominante ou `nenhuma`. |
| `proxima_acao` | Código padronizado | `avancar`, `continuar_sessao2`, `recuperar_variante`, `investigar_prerequisito`, `confirmar_posicionamento`. |

> **Exemplos puramente ilustrativos (FICTÍCIOS — não constam no CSV em branco):**  
> `2026-11-19,Aluno_Exemplo_01,B05,V1,1,12,2,3,3,pendente,ordem_inicial_invertida_corrigida,continuar_sessao2`  
> `2026-11-20,Aluno_Exemplo_01,B05,V1,1,13,3,3,3,aprovado,nenhuma,avancar`  
> `2026-11-21,Aluno_Exemplo_02,F05,V1,2,15,1,3,2,reprovado,confunde_p_e_asterisco_p,investigar_prerequisito`

---

## 7. Correção Técnica de Código C e Uso dos Casos de Teste

1. **Ambiente e Comando Padrão (UTFPR-PG):**  
   Sempre compile programas completos no terminal Linux com:
   ```bash
   gcc -std=c99 -Wall -Wextra programa.c -o programa
   ```
   *(Adicione `-lm` quando o programa incluir `<math.h>`, e liste todos os `.c` em blocos multi-arquivo a partir de `F08`.)*
2. **Warnings contam na correção:** Código com aviso relevante (`unused`, conversão incompatível de ponteiro, falta de `return` ou uso de variável não inicializada) deve ser corrigido durante a etapa de **Correção**.
3. **Trechos ilustrativos vs. Programas completos:**
   - **Trecho ilustrativo** serve apenas para leitura/teste de mesa ou exercício de lacuna (`E02`); nos gabaritos e testes, qualquer verificação compilável recebe um `main` de contexto completo.
   - **Programa completo** (`E03_corrigido`, `E04`–`E06`, `C02_corrigido`, `C03`) deve compilar isoladamente com `int main(void)` e `return 0;`.
4. **Cuidado pedagógico na Caça ao Bug:** Nunca entregue o arquivo bugado sem marcação visual. Ao corrigir, peça que o estudante **explique por que** o código original falhava (como exigido em `Lista10` Ex. 3) antes de validar a versão corrigida.
5. **Comparação de saídas e tolerância numérica:**
   - Valores inteiros e strings exigem correspondência exata.
   - Valores em ponto flutuante formatados com `%.2f` devem conferir exatamente a string esperada ou dentro de tolerância numérica de **`1e-2`** (`0,01`), verificando sempre entradas de **fronteira exata** (ex.: `10.0`, `20.0`, `30.0`, `n = 1`, vetores negativos).

---

## 8. Política de Desafios Opcionais e Calibração

- **Desafios `[OPCIONAIS]`:** Presentes apenas quando explicitados no mapa (ex.: `H06`), permanecem 100% dentro da ementa da UTFPR-PG (sem `struct` ou `malloc`) e **jamais bloqueiam o avanço** nem compõem o critério de 100% da Checagem Independente.
- **Calibração contínua:** Ao acumular registros no `00_acompanhamento.csv`, revise se a mediana de `tempo_resolucao` nos blocos ultrapassa 18 minutos (sinal para dividir ou enxugar carga antes de expandir novos grupos de estudantes).
