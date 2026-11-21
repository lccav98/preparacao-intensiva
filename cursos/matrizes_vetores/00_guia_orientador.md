# Guia do Orientador — Matrizes e Vetores (`MAT121` — UTFPR-PG)

> **Identidade Pedagógica:** Este manual orienta a condução do programa de **Preparação Intensiva** para a disciplina `MAT121 - Matrizes e Vetores` da UTFPR – Campus Ponta Grossa, alinhado a [00_inventario_fontes.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/00_inventario_fontes.md) e [00_mapa_curricular.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/00_mapa_curricular.md).

---

## 1. Regras Invioláveis de Escopo e Rigor Matemático

- **Respeitar o escopo negativo da disciplina:** É estritamente **proibido** introduzir ou cobrar:
  - Regra de Sarrus, Regra de Chió ou Determinante de Vandermonde;
  - Matriz Adjunta para inversão (sempre usar definição `AB=I` ou Gauss-Jordan `[A|I] -> [I|A^{-1}]`);
  - Regra de Cramer para sistemas lineares;
  - Autovalores, autovetores, diagonalização ou Gram-Schmidt;
  - Rotação de cônicas/quádricas com termo misto `xy`.
- **Respeitar a notação do professor:** Colchetes `[...]`, `A^T`, `A^{-1}`, operações `L_{ij}`, `L_i(\alpha)`, `L_j' = L_j + L_i(\alpha)`, características `C_A, C_V, C`, grau de liberdade `g = n - C`, barras simples `|\vec{v}|`, versor `\hat{v}`, produto misto `(\vec{u},\vec{v},\vec{w})`, e reta reduzida sempre em função de `x`.
- **Frações e radicais exatos:** Nunca arredondar intermediários para decimais (`0.333`, `3.605`). Exigir sempre `1/3`, `\sqrt{13}`, `16/\sqrt{21}`.

---

## 2. Aplicação do Diagnóstico e Sessão Diária (15–25 min)

1. Aplique [00_teste_diagnostico.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/00_teste_diagnostico.md) **sem consulta e sem calculadora**.
2. Observe as regras de interrupção `I1`–`I5` e posicione pelo menor pré-requisito faltante.
3. Condução da sessão diária (`15–25 min`):
   - **Leitura & Exemplos (`2–3 min`):** Garantir que o estudante acompanhe o passo a passo resolvido antes de começar.
   - **Prática Independente (`10–15 min`):** Resolução a caneta no papel (ou na folha A4 impressa com protocolo `PREP-MV-...`), registrando horário de início e término.
   - **Autocorreção (`4–6 min`):** Conferência com o gabarito comentado; registrar `acertos_iniciais` e `acertos_apos_correcao` separados no CSV.
   - **Checagem Independente (`10–18 min`):** Folha sem consulta exigindo **100% de acerto** para liberar o próximo bloco.

---

## 3. Regra das 2 Tentativas e Diagnóstico de Pré-Requisitos (`MAT121`)

Após **2 tentativas malsucedidas** na checagem do mesmo bloco (`V1` e `V2`), é proibido repetir o bloco pela 3ª vez: o orientador investiga os **pré-requisitos** declarados no bloco usando a tabela abaixo:

| Sintoma Observado no Bloco Atual | Pré-requisito em Falta | Ação de Recuperação |
|---|---|---|
| Erra sinal `\pm` em raízes quadráticas ou ignora ordem compatível `A \times B` (`B06`, `D03`) | `A02` / `A04` | Refazer igualdade com equações quadráticas e compatibilidade `(m,n) \times (k,\ell)`. |
| Troca sinais da matriz de cofatores (`+ - +`) ou erra compensação na triangulação (`B04`, `B07`) | `B01` / `B02` | Retomar matriz xadrez de sinais e efeito das 3 operações elementares em `\det`. |
| Esquece a linha do termo independente ao multiplicar linha ou perde solução `r=0` (`C03`, `C07`) | `B05` / `C01` | Refazer escrita de `[A\|B]` com barra vertical e fatoração sem cancelar variáveis nulas. |
| Calcula vetor ao contrário (`A - B` em vez de `B - A`) ou ângulo suplementar em triângulo (`D05`, `E03`) | `D02` / `D04` | Refazer regra "extremidade menos origem" e garantir vetores com mesma origem no vértice. |
| Aplica fórmula de retas reversas quando `\vec{v}_1 \parallel \vec{v}_2` (`0/0`) ou erra `\sin\phi` reta-plano (`E05`, `E08`) | `E02` / `E03` / `D07` | Testar paralelismo antes da distância e distinguir cosseno (plano-plano) de seno (reta-plano). |
| Troca `a^2 = b^2 + c^2` (elipse) por `c^2 = a^2 + b^2` (hipérbole) ou erra fatoração com sinal negativo (`F04`, `F06`) | `F03` / `F05` | Retomar esquema gráfico de `a, b, c` em cada cônica e conferência por expansão do quadrado. |

---

## 4. Uso da Ficha de Acompanhamento (`00_acompanhamento.csv`)

O arquivo [00_acompanhamento.csv](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/00_acompanhamento.csv) usa exatamente as **12 colunas padrão** (`data, aluno, bloco, variante, tentativa, tempo_resolucao, acertos_iniciais, total_questoes, acertos_apos_correcao, resultado_checagem, dificuldade_observada, proxima_acao`) sincronizadas automaticamente pelo sistema de correção e dashboard.
