# Gabarito Comentado — Bloco `A09` (Revisão Cumulativa do Estágio A)

> **Bloco de referência:** [A09_bloco.md](../blocos/A09_bloco.md)

---

## 1. Exercícios

### `A09-E01` *(Lei de formação + igualdade com raízes `\pm`)*
- **Passo a passo:**
  - Construindo $A_{(2,2)}$ com $a_{ij} = 3i - 2j$:
    - $a_{11} = 3(1) - 2(1) = 1$, $\;a_{12} = 3(1) - 2(2) = -1$
    - $a_{21} = 3(2) - 2(1) = 4$, $\;a_{22} = 3(2) - 2(2) = 2$
    $$A = \begin{bmatrix} 1 & -1 \\ 4 & 2 \end{bmatrix}.$$
  - Igualando $A = B$:
    - **(a)** $x^2 - 8 = 1 \implies x^2 = 9 \implies x = \pm 3$.
    - **(b)** $y^2 - 14 = 2 \implies y^2 = 16 \implies y = \pm 4$.
    - Elementos fixos conferem: $-1 = -1$ e $4 = 4$.
- **Resposta Final:** `(a) x = +-3 (b) y = +-4`
- **Alerta pedagógico:** Não perca o sinal negativo em $x^2 = 9$ e $y^2 = 16$; revise sempre se $a_{12}$ e $a_{21}$ coincidem.

---

### `A09-E02` *(Combinação linear com transposta)*
- **Passo a passo:**
  - $2A - B = \begin{bmatrix} 2-(-1) & -4-3 & 6-2 \\ 0-2 & 8-(-1) & -2-5 \end{bmatrix} = \begin{bmatrix} 3 & -7 & 4 \\ -2 & 9 & -7 \end{bmatrix}$.
  - Transpondo: $(2A - B)^T = \begin{bmatrix} 3 & -2 \\ -7 & 9 \\ 4 & -7 \end{bmatrix}$.
  - Somando $3C = \begin{bmatrix} 6 & -3 \\ 0 & 9 \\ -6 & 3 \end{bmatrix}$:
    $$X = \begin{bmatrix} 9 & -5 \\ -7 & 18 \\ -2 & -4 \end{bmatrix}.$$
- **Resposta Final:** `[[9, -5], [-7, 18], [-2, -4]]`
- **Alerta pedagógico:** Só é possível somar após transpor $2A - B$ de $2 \times 3$ para $3 \times 2$, igualando à ordem de $C$.

---

### `A09-E03` *(Não-comutatividade e transposição do produto)*
- **Passo a passo:**
  - **(a)** $AB = \begin{bmatrix} 2(0)+(-1)(-2) & 2(4)+(-1)(1) \\ 1(0)+3(-2) & 1(4)+3(1) \end{bmatrix} = \begin{bmatrix} 2 & 7 \\ -6 & 7 \end{bmatrix} \implies (AB)^T = \begin{bmatrix} 2 & -6 \\ 7 & 7 \end{bmatrix}$.
  - **(b)** $BA = \begin{bmatrix} 0(2)+4(1) & 0(-1)+4(3) \\ (-2)(2)+1(1) & (-2)(-1)+1(3) \end{bmatrix} = \begin{bmatrix} 4 & 12 \\ -3 & 5 \end{bmatrix} \implies (BA)^T = \begin{bmatrix} 4 & -3 \\ 12 & 5 \end{bmatrix}$.
- **Resposta Final:** `(a) [[2, -6], [7, 7]] (b) [[4, -3], [12, 5]]`
- **Alerta pedagógico:** Note que $(AB)^T \neq (BA)^T$ porque $AB \neq BA$.

---

### `A09-E04` *(Decomposição simétrica/anti-simétrica e ortogonalidade)*
- **Passo a passo:**
  - **(a)** $M^T = \begin{bmatrix} 3 & -1 \\ 5 & 7 \end{bmatrix} \implies S = \frac{1}{2}\begin{bmatrix} 6 & 4 \\ 4 & 14 \end{bmatrix} = \begin{bmatrix} 3 & 2 \\ 2 & 7 \end{bmatrix}$.
  - **(b)** $K = \frac{1}{2}\begin{bmatrix} 0 & 6 \\ -6 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 3 \\ -3 & 0 \end{bmatrix}$.
  - **(c)** Calculando $Q \cdot Q^T$:
    $$Q \cdot Q^T = \begin{bmatrix} \frac{64}{289} + \frac{225}{289} & \frac{120 - 120}{289} \\ \frac{120 - 120}{289} & \frac{225}{289} + \frac{64}{289} \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I_2.$$
    Logo, $Q$ é **ortogonal** (pois $8^2 + 15^2 = 64 + 225 = 289 = 17^2$).
- **Resposta Final:** `(a) [[3, 2], [2, 7]] (b) [[0, 3], [-3, 0]] (c) ortogonal`
- **Alerta pedagógico:** Terna pitagórica $(8, 15, 17)$ gera matriz de rotação ortogonal exata sem radicais.

---

### `A09-E05` *(Potências e classificação especial)*
- **Passo a passo:**
  - **(a)** $H^2 = \begin{bmatrix} 2 & 4 \\ -1 & -2 \end{bmatrix} \begin{bmatrix} 2 & 4 \\ -1 & -2 \end{bmatrix} = \begin{bmatrix} 4-4 & 8-8 \\ -2+2 & -4+4 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} = [O]$.
  - **(b)** $J^2 = \begin{bmatrix} 4 & -6 \\ 2 & -3 \end{bmatrix} \begin{bmatrix} 4 & -6 \\ 2 & -3 \end{bmatrix} = \begin{bmatrix} 16-12 & -24+18 \\ 8-6 & -12+9 \end{bmatrix} = \begin{bmatrix} 4 & -6 \\ 2 & -3 \end{bmatrix} = J$.
  - **(c)** Como $H \neq [O]$ e $H^2 = [O]$, $H$ é **nilpotente** (índice $p = 2$). *(Já $J$ é idempotente.)*
- **Resposta Final:** `(a) [[0, 0], [0, 0]] (b) [[4, -6], [2, -3]] (c) nilpotente`
- **Alerta pedagógico:** Não confunda as classificações: $A^2 = [O] \implies$ nilpotente; $A^2 = A \implies$ idempotente.

---

## 2. Checagem Independente

### `A09-C01` *(Equação matricial com `X^T` e frações)*
- **Passo a passo:**
  - Isolando $X^T$: $2X^T = A + B = \begin{bmatrix} 3+1 & -1+4 \\ 2-2 & 5+0 \end{bmatrix} = \begin{bmatrix} 4 & 3 \\ 0 & 5 \end{bmatrix}$.
  - Dividindo por $2$: $X^T = \begin{bmatrix} 2 & 3/2 \\ 0 & 5/2 \end{bmatrix}$.
  - Transpondo para obter $X$:
    $$X = \begin{bmatrix} 2 & 0 \\ 3/2 & 5/2 \end{bmatrix}.$$
- **Resposta Final:** `[[2, 0], [3/2, 5/2]]`
- **Alerta pedagógico:** Se esquecer a transposição final, as posições $(1,2)$ e $(2,1)$ ficam invertidas!

---

### `A09-C02` *(Comutatividade + regra reversa `(AB)^T = B^T A^T`)*
- **Passo a passo:**
  - **(a)** Calculando $AB$ e $BA$:
    $$AB = \begin{bmatrix} 1 & 3 \\ 0 & 2 \end{bmatrix}\begin{bmatrix} x & 6 \\ y & 4 \end{bmatrix} = \begin{bmatrix} x + 3y & 18 \\ 2y & 8 \end{bmatrix}$$
    $$BA = \begin{bmatrix} x & 6 \\ y & 4 \end{bmatrix}\begin{bmatrix} 1 & 3 \\ 0 & 2 \end{bmatrix} = \begin{bmatrix} x & 3x + 12 \\ y & 3y + 8 \end{bmatrix}$$
    Igualando $AB = BA$:
    - Posição $(2,1)$: $2y = y \implies y = 0$.
    - Posição $(1,2)$: $3x + 12 = 18 \implies 3x = 6 \implies x = 2$.
    - Conferência em $(1,1)$ e $(2,2)$: $2 + 0 = 2$ e $8 = 0 + 8$. Logo $(x, y) = (2, 0)$.
  - **(b)** Para $B = \begin{bmatrix} 2 & 6 \\ 0 & 4 \end{bmatrix}$, temos $B^T = \begin{bmatrix} 2 & 0 \\ 6 & 4 \end{bmatrix}$ e $A^T = \begin{bmatrix} 1 & 0 \\ 3 & 2 \end{bmatrix}$:
    $$B^T A^T = \begin{bmatrix} 2(1)+0(3) & 2(0)+0(2) \\ 6(1)+4(3) & 6(0)+4(2) \end{bmatrix} = \begin{bmatrix} 2 & 0 \\ 18 & 8 \end{bmatrix}.$$
    *(Conferência pela propriedade reversa: $B^T A^T = (AB)^T = \begin{bmatrix} 2 & 18 \\ 0 & 8 \end{bmatrix}^T = \begin{bmatrix} 2 & 0 \\ 18 & 8 \end{bmatrix}$.)*
- **Resposta Final:** `(a) (2, 0) (b) [[2, 0], [18, 8]]`
- **Alerta pedagógico:** Usar $(AB)^T = B^T A^T$ serve como dupla conferência instantânea para o cálculo do item (b).

---

### `A09-C03` *(Integração: potência especial + decomposição anti-simétrica)*
- **Passo a passo:**
  - **(a)** $P^2 = \begin{bmatrix} -3 & -6 \\ 2 & 4 \end{bmatrix}\begin{bmatrix} -3 & -6 \\ 2 & 4 \end{bmatrix} = \begin{bmatrix} 9-12 & 18-24 \\ -6+8 & -12+16 \end{bmatrix} = \begin{bmatrix} -3 & -6 \\ 2 & 4 \end{bmatrix} = P$.
  - **(b)** Como $P^2 = P$, $P$ é **idempotente**.
  - **(c)** Com $P^T = \begin{bmatrix} -3 & 2 \\ -6 & 4 \end{bmatrix}$, a parcela anti-simétrica é:
    $$K = \frac{1}{2}(P - P^T) = \frac{1}{2}\begin{bmatrix} -3-(-3) & -6-2 \\ 2-(-6) & 4-4 \end{bmatrix} = \frac{1}{2}\begin{bmatrix} 0 & -8 \\ 8 & 0 \end{bmatrix} = \begin{bmatrix} 0 & -4 \\ 4 & 0 \end{bmatrix}.$$
- **Resposta Final:** `(a) [[-3, -6], [2, 4]] (b) idempotente (c) [[0, -4], [4, 0]]`
- **Alerta pedagógico:** Uma matriz pode simultaneamente ser idempotente ($P^2 = P$) e **não** ser simétrica ($P^T \neq P$), possuindo parte anti-simétrica não nula $K \neq [O]$.
