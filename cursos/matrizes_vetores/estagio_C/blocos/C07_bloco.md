# Bloco `C07` — Discussão de Sistemas com Parâmetros (`k, a, b, c, d`)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio C — Sistemas Lineares, Escalonamento, Posto (`C_A, C_V`) e Parâmetros / **`C07`** |
| **Micro-habilidade foco** | Carregar termos simbólicos (`a, b, c, d, k`) durante o escalonamento de `[A | B]` até a forma de escada $B$, impor $C_A = C_V$ para extrair condições exatas de compatibilidade, resolver incógnitas em função de parâmetros e discutir `SPD`, `SPI` e `SI` sem dividir por expressões que possam se anular. |
| **Pré-requisitos** | `C05` *(Forma de escada $B$ e posto $C_A, C_V$)* e `C06` *(Grau de liberdade e parâmetros em homogêneos)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Prática (`C07-E01`–`C07-E05`, 25 min):** `16 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C07-C01`–`C07-C03`, 18 min):** `12 min` resol. \| `6 min` conf. |
| **Restrição de escopo** | **Proibido:** Regra de Cramer, Regra de Sarrus ou matriz adjunta. Execute todas as operações $L_{ij}$, $L_i(\alpha)$ e $L_j' = L_j + L_i(\alpha)$ diretamente na matriz ampliada carregando os símbolos no lado direito; **nunca** divida por uma expressão contendo $k$ sem abrir o caso em que ela vale zero. |

### Registro da Sessão (Preenchido na Prática)
- **Protocolo:** `PREP-MV-C07-<VARIANTE>-T<TENTATIVA>-<HASH>`
- **Prática (`C07-E01`–`C07-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`C07-C01`–`C07-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Condição de compatibilidade sobre termos independentes ($a, b, c, d$):**
   - Monte a matriz ampliada colocando os símbolos na coluna à direita do traço vertical.
   - Escalone a submatriz à esquerda até zerar todas as linhas linearmente dependentes.
   - Para cada linha em que os coeficientes das variáveis zeraram (`[0  0  ...  0 | E(a,b,c,...)]`), o sistema só será compatível ($C_A = C_V$) se **$E(a, b, c, \dots) = 0$**.
2. **Discussão completa de um parâmetro $k$:**
   - Reduza até isolar o pivô ou expressão em $k$ na última linha não trivial: `[0  ...  0  p(k) | q(k)]`.
   - Resolva primeiro $p(k) = 0$:
     - Para uma raiz $k_0$ tal que $p(k_0) = 0$ **e** $q(k_0) = 0$ $\Rightarrow$ linha toda nula ($C_A = C_V < n$ se não houver outra linha absurda) $\Rightarrow$ **`SPI`**.
     - Para uma raiz $k_0$ tal que $p(k_0) = 0$ **e** $q(k_0) \neq 0$ $\Rightarrow$ $0 = q(k_0) \neq 0$ ($C_A > C_V$) $\Rightarrow$ **`SI`**.
   - Para $p(k) \neq 0$ (e pivôs anteriores não nulos) $\Rightarrow$ $C_A = C_V = n$ $\Rightarrow$ **`SPD`**.
3. **Regra de ouro:** **nunca** simplifique $\frac{q(k)}{p(k)}$ cancelando um fator $(k - k_0)$ antes de testar $k = k_0$ no sistema original.

---

## 2. Exemplos Guiados

### Exemplo 1 — Condição sobre $a, b, c$ para compatibilidade (`Sondagem SC-03`)
$$\begin{cases} x - 2y = a \\ 2x + y = b \\ 3x - y = c \end{cases}$$
$$\left[\begin{array}{cc|c} 1 & -2 & a \\ 2 & 1 & b \\ 3 & -1 & c \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(-3)}} \left[\begin{array}{cc|c} 1 & -2 & a \\ 0 & 5 & b - 2a \\ 0 & 5 & c - 3a \end{array}\right] \xrightarrow{L_3' = L_3 + L_2(-1)} \left[\begin{array}{cc|c} 1 & -2 & a \\ 0 & 5 & b - 2a \\ 0 & 0 & c - a - b \end{array}\right]$$
Para que $C_A = C_V = 2$ (sistema compatível), a 3ª linha deve anular o termo independente:
$$c - a - b = 0 \quad (\text{ou } c = a + b).$$

### Exemplo 2 — Discussão do parâmetro $k$ sem cancelar fator nulo
Considere $\begin{cases} x + y = 3 \\ kx + 2y = 6 \end{cases}$:
$$\left[\begin{array}{cc|c} 1 & 1 & 3 \\ k & 2 & 6 \end{array}\right] \xrightarrow{L_2' = L_2 + L_1(-k)} \left[\begin{array}{cc|c} 1 & 1 & 3 \\ 0 & 2 - k & 6 - 3k \end{array}\right]$$
Note que $2 - k = 0 \iff k = 2$, caso em que $6 - 3(2) = 0$ (`[0 0 | 0]` $\Rightarrow$ `SPI`). Para $k \neq 2$, $2 - k \neq 0$ $\Rightarrow$ `SPD` com $y = \frac{3(2-k)}{2-k} = 3$ e $x = 0$.

---

## 3. Exercícios (`C07-E01` a `C07-E05`)

### `C07-E01` *(Condição de compatibilidade $3 \times 2$ — Lista 5 Ex. 12)*
Estabeleça a equação algébrica que deve ser satisfeita pelos termos independentes $a, b, c$ para que o sistema abaixo seja compatível:
$$\begin{cases} x + 2y = a \\ -3x + 4y = b \\ 2x - y = c \end{cases}$$
*Formato na caixa de resposta:* equação em `a, b, c` (ex.: `a - b - 2c = 0` ou `a = b + 2c`).

---

### `C07-E02` *(Condição de compatibilidade $3 \times 3$ — Lista 5 Ex. 18)*
Estabeleça a relação que deve ser satisfeita por $a, b, c$ para que o sistema seja compatível:
$$\begin{cases} x - 2y - z = a \\ 2x + y + 3z = b \\ 4x - 3y + z = c \end{cases}$$
*Formato na caixa de resposta:* equação em `a, b, c` (ex.: `... = 0`).

---

### `C07-E03` *(Caça ao Bug — Cancelamento indevido de parâmetro nulo)*
Para o sistema $\begin{cases} x + ky = 2 \\ kx + y = 2 \end{cases}$, um estudante escalonou até $(1 - k^2)y = 2(1 - k)$, dividiu ambos os lados por $(1 - k)$ e escreveu $y = \frac{2}{1 + k}$, concluindo erroneamente que só não há solução única em $k = -1$ (esquecendo o caso $k = 1$).
Escalone corretamente sem cancelar $(1 - k)$ e informe:  
**(a)** o valor de $k$ para o qual o sistema é **`SPI`**;  
**(b)** o valor de $k$ para o qual o sistema é **`SI`**.  
*Formato na caixa de resposta:* `spi: <valor de k>; si: <valor de k>`.

---

### `C07-E04` *(Duas condições simultâneas em sistema $4 \times 2$ — Lista 5 Ex. 14)*
Estabeleça as duas condições sobre $a, b, c, d$ para que o sistema seja compatível:
$$\begin{cases} -x + 3y = a \\ 2x - y = b \\ -2x + y = c \\ 3x + y = d \end{cases}$$
Escreva **uma** equação relacionando apenas `b` e `c`, e **outra** relacionando apenas `a, c` e `d`.  
*Formato na caixa de resposta:* `cond1: <equacao em b, c>; cond2: <equacao em a, c, d>`.

---

### `C07-E05` *(Resolução simbólica em função de $a, b$ — Lista 5 Ex. 16)*
Resolva o sistema por escalonamento expressando $x$ e $y$ em função de $a$ e $b$:
$$\begin{cases} 3x + 5y = a \\ x + 2y = b \end{cases}$$
*Formato na caixa de resposta:* `x: x = <expressao em a, b>; y: y = <expressao em a, b>`.

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `C07-C01` *(Condição sobre $a, b, c$ — Lista 5 Ex. 13)*
Determine a condição algébrica sobre $a, b, c$ para que o sistema abaixo seja compatível:
$$\begin{cases} x + 2y = a \\ -2x + y = b \\ -x + y = c \end{cases}$$
*Formato na caixa de resposta:* equação em `a, b, c` (ex.: `... = 0`).

---

### `C07-C02` *(Parâmetro $k$ de compatibilidade — Lista 5 Ex. 15)*
Calcule o valor real de $k$ para que o sistema abaixo seja compatível:
$$\begin{cases} x + 2y = -1 \\ -3x + 4y = k \\ 2x - y = -7 \end{cases}$$
*Formato na caixa de resposta:* `k = <valor>`.

---

### `C07-C03` *(Discussão completa $3 \times 3$ em $k$)*
Considere o sistema:
$$\begin{cases} x + y + z = 2 \\ 2x + 3y + 2z = 5 \\ x + y + (k^2 - 3)z = k \end{cases}$$
Escalone carregando $k$ e informe:  
**(a)** o valor de $k$ que torna o sistema **`SPI`**;  
**(b)** o valor de $k$ que torna o sistema **`SI`**.  
*Formato na caixa de resposta:* `spi: <valor de k>; si: <valor de k>`.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `C08` (`Revisão Cumulativa do Estágio C`):** somente após autocorreção de `C07-E01..E05` **e** **100% (3/3)** na Checagem Independente `C07-C01..C03`.
- **Recuperação direcionada (1ª falha):** verifique se não houve divisão por expressão contendo $k$ antes da análise de raízes e confira cada sinal ao combinar $a, b, c$ na última linha da matriz escalonada; aplique a variante `V2` de `C07`.
- **Após 2 tentativas malsucedidas:** recuar no DAG para **`C05`** *(redução de sistemas $m \times n$ à forma de escada $B$)* ou **`C06`** *(análise de parâmetro $k$ em homogêneos)*.

---

## 6. Referências do Orientador
- `[DOC]` `Mat_Vet_L5.pdf` p. 2–3 (Ex. 12–19: condições de compatibilidade e resolução paramétrica).
- `[DOC]` `Matrizes_Vetores_P2.pdf` p. 64–77 (discussão de sistemas com parâmetros simbólicos e numéricos).
- Gabarito comentado e casos de verificação: [C07_gabarito.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_C/gabaritos/C07_gabarito.md) e [casos_C07.json](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_C/testes/casos_C07.json).
