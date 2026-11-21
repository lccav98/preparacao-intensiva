# Bloco `C05` — Forma de Escada (Escalonada), Posto (`C_A, C_V, C`) e Sistemas `m × n`

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio C — Sistemas Lineares, Escalonamento, Posto (`C_A, C_V`) e Parâmetros / **`C05`** |
| **Micro-habilidade foco** | Reduzir qualquer matriz ampliada $A$ ($m \times n$, retangular ou quadrada) à forma de escada (escalonada) $B$, extrair a submatriz $V$ dos coeficientes, contar as características $C_A$ e $C_V$ e classificar o sistema em `SI`, `SPD` ou `SPI`. |
| **Pré-requisitos** | `C03` *(Método de Gauss-Jordan na matriz ampliada)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Prática (`C05-E01`–`C05-E05`, 24 min):** `15 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C05-C01`–`C05-C03`, 16 min):** `11 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Proibido:** Regra de Cramer, Regra de Sarrus ou matriz adjunta. Empregue exatamente a notação da disciplina: $A$ (matriz ampliada), $B$ (forma de escada / escalonada), $V$ (submatriz dos coeficientes em $B$), $C_A$, $C_V$, $C$ e $g = n - C$. |

### Registro da Sessão (Preenchido na Prática)
- **Protocolo:** `PREP-MV-C05-<VARIANTE>-T<TENTATIVA>-<HASH>`
- **Prática (`C05-E01`–`C05-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`C05-C01`–`C05-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Quando $m \neq n$ (sistemas retangulares):** a matriz dos coeficientes não é quadrada e não pode virar $I$. Reduzimos $A$ por operações $L$ até a **forma de escada (matriz escalonada) $B$**, onde cada pivô vale $1$ (com $0$ acima e abaixo na sua coluna à esquerda do traço vertical) e linhas inteiramente nulas ficam abaixo das demais.
2. **Definições oficiais (`MAT121_Sistemas` p. 43–51 e `Lista 5`):**
   - **$B$:** matriz ampliada reduzida à forma de escada (escalonada).
   - **$V$:** submatriz dos coeficientes das variáveis contida em $B$ *(tudo à esquerda do traço vertical)*.
   - **$C_A$:** característica (posto / rank) da matriz ampliada — número de linhas de **$B$** com elementos **não todos nulos** *(olhando a linha inteira, inclusive a coluna dos termos independentes)*.
   - **$C_V$:** característica (posto / rank) de $V$ — número de linhas de **$V$** com elementos **não todos nulos**.
   - **$m$** = número de equações; **$n$** = número de variáveis.
3. **Teorema de Classificação (sempre $C_A \ge C_V$):**
   - Se **$C_A > C_V$** $\Rightarrow$ sistema **Incompatível (`SI`)** *(existe linha `[0 ... 0 | c]` com $c \neq 0$)*.
   - Se **$C_A = C_V = C$** $\Rightarrow$ sistema **Compatível**, onde $C \le n$:
     - Se **$C = n$** $\Rightarrow$ **Compatível e Determinado (`SPD`)** *(solução única)*.
     - Se **$C < n$** $\Rightarrow$ **Compatível e Indeterminado (`SPI`)** *(infinitas soluções, com grau de liberdade $g = n - C$)*.

---

## 2. Exemplos Guiados

### Exemplo 1 — Sistema $3 \times 2$ incompatível (`MAT121_Sistemas` p. 34–36, 44–47)
$$\begin{cases} 2x + 4y = 16 \\ 5x - 2y = 4 \\ 10x - 4y = 3 \end{cases} \Rightarrow A = \left[\begin{array}{cc|c} 2 & 4 & 16 \\ 5 & -2 & 4 \\ 10 & -4 & 3 \end{array}\right]$$
Aplicando $L_1(1/2)$, $L_2'=L_2+L_1(-5)$, $L_2(-1/12)$, $L_1'=L_1+L_2(-2)$, $L_3'=L_3+L_1(-10)$ e $L_3''=L_3'+L_2(4)$:
$$B = \left[\begin{array}{cc|c} 1 & 0 & 2 \\ 0 & 1 & 3 \\ 0 & 0 & -5 \end{array}\right], \qquad V = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{bmatrix}.$$
- **Contagem:** $B$ possui $3$ linhas não nulas $\Rightarrow C_A = 3$; $V$ possui $2$ linhas não nulas $\Rightarrow C_V = 2$.
- **Classificação:** Como $C_A > C_V$ ($3 > 2$), o sistema é **incompatível (`SI`)**.

### Exemplo 2 — Sistema $2 \times 4$ compatível e indeterminado (`MAT121_Sistemas` p. 40–42, 45–49)
$$\begin{cases} 2x - 8y + 24z + 18w = 84 \\ 4x - 14y + 52z + 42w = 190 \end{cases} \Rightarrow B = \left[\begin{array}{cccc|c} 1 & 0 & 20 & 21 & 86 \\ 0 & 1 & 2 & 3 & 11 \end{array}\right], \qquad V = \begin{bmatrix} 1 & 0 & 20 & 21 \\ 0 & 1 & 2 & 3 \end{bmatrix}.$$
- **Contagem:** $C_A = 2$, $C_V = 2 \Rightarrow C = 2$. Como $n = 4$ e $C < n$ ($2 < 4$), é **`SPI`** com $g = 4 - 2 = 2$.
- **Solução geral:** $x = 86 - 20z - 21w$, $y = 11 - 2z - 3w$ ($z, w \in \mathbb{R}$ arbitrários).

---

## 3. Exercícios (`C05-E01` a `C05-E05`)

### `C05-E01` *(Posto e incompatibilidade em $2 \times 2$ — Lista 5 Ex. 1)*
Reduza à forma de escada $B$, identifique $V$, determine $C_A$, $C_V$ e classifique o sistema:
$$\begin{cases} 2x - 3y = 4 \\ 6x - 9y = 15 \end{cases}$$
*Formato na caixa de resposta:* `ca: <int>; cv: <int>; classificacao: <SPD/SPI/SI>`.

---

### `C05-E02` *(Sistema sobredeterminado $3 \times 2$ compatível — Lista 5 Ex. 10)*
Escalone até a forma de escada $B$, obtenha $C_A$, $C_V$, $g$, a classificação e a solução $(x, y)$ de:
$$\begin{cases} x + 2y = -4 \\ -3x + 4y = -18 \\ 2x - y = 7 \end{cases}$$
*Formato na caixa de resposta:* `ca: <int>; cv: <int>; g: <int>; classificacao: <SPD/SPI/SI>; solucao: (x, y)`.

---

### `C05-E03` *(Sistema sobredeterminado $3 \times 2$ incompatível — Lista 5 Ex. 11)*
Reduza à forma de escada $B$, conte $C_A$ e $C_V$ e classifique:
$$\begin{cases} x + 2y = 4 \\ -3x + 4y = 3 \\ 2x - y = -6 \end{cases}$$
*Formato na caixa de resposta:* `ca: <int>; cv: <int>; classificacao: <SPD/SPI/SI>`.

---

### `C05-E04` *(Sistema $3 \times 3$ com posto $C = 2 < n$ — Lista 5 Ex. 9)*
Reduza à forma de escada $B$ o sistema $\begin{cases} x - y = 0 \\ 2y + 4z = 6 \\ x + y + 4z = 6 \end{cases}$.
Informe $C_A$, $C_V$, $g = n - C$, a classificação e a solução particular obtida ao atribuir $z = 1$.  
*Formato na caixa de resposta:* `ca: <int>; cv: <int>; g: <int>; classificacao: <SPD/SPI/SI>; solucao: (x, y, 1)`.

---

### `C05-E05` *(Sistema subdeterminado $2 \times 4$)*
Reduza à forma de escada $B$ o sistema $\begin{cases} x - 2y + 3z - w = 5 \\ 2x - 3y + 7z + w = 13 \end{cases}$.
Informe $C_A$, $C_V$, $g = n - C$, a classificação e a solução particular $(x, y, z, w)$ quando $z = 1$ e $w = 0$.  
*Formato na caixa de resposta:* `ca: <int>; cv: <int>; g: <int>; classificacao: <SPD/SPI/SI>; solucao: (x, y, 1, 0)`.

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `C05-C01` *(Sobredeterminado $4 \times 2$ — `MAT121_Sistemas` p. 37–39)*
Escalone o sistema abaixo até a forma de escada $B$, determine $C_A$, $C_V$, $g$, classifique e resolva:
$$\begin{cases} 2x + 4y = 16 \\ 5x - 2y = 4 \\ 3x + y = 9 \\ 4x - 5y = -7 \end{cases}$$
*Formato na caixa de resposta:* `ca: <int>; cv: <int>; g: <int>; classificacao: <SPD/SPI/SI>; solucao: (x, y)`.

---

### `C05-C02` *(Subdeterminado $3 \times 4$ com linha nula)*
Para o sistema $\begin{cases} x - y + 2z + w = 3 \\ 2x - 2y + 5z + 4w = 8 \\ 3x - 3y + 6z + 3w = 9 \end{cases}$, reduza à forma de escada $B$, informe $C_A$, $C_V$, $g$, a classificação e a solução particular para as variáveis arbitrárias $y = 0$ e $w = 1$.  
*Formato na caixa de resposta:* `ca: <int>; cv: <int>; g: <int>; classificacao: <SPD/SPI/SI>; solucao: (x, 0, z, 1)`.

---

### `C05-C03` *(Sobredeterminado $3 \times 2$ com frações exatas)*
Escalone até $B$, informe $C_A$, $C_V$, $g$, a classificação e a solução exata $(x, y)$ de:
$$\begin{cases} 2x + y = 4 \\ 4x - 2y = 2 \\ 6x + y = 9 \end{cases}$$
*Formato na caixa de resposta:* `ca: <int>; cv: <int>; g: <int>; classificacao: <SPD/SPI/SI>; solucao: (x, y)`.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `C06` (`Grau de Liberdade g = n - C e Sistemas Homogêneos`) e `C07` (`Discussão com Parâmetros`):** somente após autocorreção de `C05-E01..E05` **e** **100% (3/3)** na Checagem Independente `C05-C01..C03`.
- **Recuperação direcionada (1ª falha):** verifique se você contou $C_A$ em **$B$ inteira** (incluindo o termo independente) e $C_V$ apenas em **$V$** (à esquerda do traço), e se comparou $C$ com o número de variáveis $n$ (e não com $m$); aplique a variante `V2` de `C05`.
- **Após 2 tentativas malsucedidas:** recuar no DAG para **`C03`** *(redução completa por Gauss-Jordan)*.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Sistemas.pdf` p. 33–51 (`A.45.2`: sistemas $m \times n$, forma de escada $B$, submatriz $V$, características $C_A, C_V, C$ e posto/rank).
- `[DOC]` `Mat_Vet_L5.pdf` p. 1–3 (critérios oficiais e Ex. 1, 9, 10, 11).
- Gabarito comentado e casos de verificação: [C05_gabarito.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_C/gabaritos/C05_gabarito.md) e [casos_C05.json](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_C/testes/casos_C05.json).
