# Gabarito Comentado — Bloco `G01` (Simulado Integrador P1 — Matrizes, Determinantes e Inversa)

> **Bloco de referência:** [G01_bloco.md](../blocos/G01_bloco.md)

---

## 1. Exercícios

### `G01-E01` *(Lei de formação, igualdade paramétrica $\pm$ e transposição do produto)*
- **Passo a passo:**
  - Construindo $A_{(2,2)}$ com $a_{ij} = 2i - j$:
    $$a_{11} = 2(1)-1 = 1,\quad a_{12} = 2(1)-2 = 0,\quad a_{21} = 2(2)-1 = 3,\quad a_{22} = 2(2)-2 = 2 \implies A = \begin{bmatrix} 1 & 0 \\ 3 & 2 \end{bmatrix}.$$
  - Igualando $A = B$:
    - **(a)** $x^2 - 3 = 1 \implies x^2 = 4 \implies x = \pm 2$.
    - **(b)** $y^2 - 7 = 2 \implies y^2 = 9 \implies y = \pm 3$.
    - As entradas fixas conferem ($0=0$ e $3=3$).
  - **(c)** Calculando $AC$ e transpondo (ou usando $C^T A^T$):
    $$AC = \begin{bmatrix} 1 & 0 \\ 3 & 2 \end{bmatrix}\begin{bmatrix} 1 & -1 \\ 2 & 3 \end{bmatrix} = \begin{bmatrix} 1 & -1 \\ 7 & 3 \end{bmatrix} \implies (AC)^T = \begin{bmatrix} 1 & 7 \\ -1 & 3 \end{bmatrix}.$$
- **Resposta Final:** `(a) x = +-2 (b) y = +-3 (c) [[1, 7], [-1, 3]]`
- **Alerta pedagógico:** Não omita as raízes negativas em $x^2=4$ e $y^2=9$; lembre-se de que $(AC)^T = C^T A^T \neq A^T C^T$.

---

### `G01-E02` *(Decomposição anti-simétrica e classificação de potência)*
- **Passo a passo:**
  - **(a)** Com $M^T = \begin{bmatrix} 1 & -2 \\ 4 & 5 \end{bmatrix}$:
    $$K = \frac{1}{2}(M - M^T) = \frac{1}{2}\begin{bmatrix} 0 & 6 \\ -6 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 3 \\ -3 & 0 \end{bmatrix}.$$
  - **(b)** Calculando $N^2$:
    $$N^2 = \begin{bmatrix} 3 & -6 \\ 1 & -2 \end{bmatrix}\begin{bmatrix} 3 & -6 \\ 1 & -2 \end{bmatrix} = \begin{bmatrix} 9-6 & -18+12 \\ 3-2 & -6+4 \end{bmatrix} = \begin{bmatrix} 3 & -6 \\ 1 & -2 \end{bmatrix} = N.$$
  - **(c)** Como $N^2 = N$, $N$ é **idempotente**.
- **Resposta Final:** `(a) [[0, 3], [-3, 0]] (b) [[3, -6], [1, -2]] (c) idempotente`
- **Alerta pedagógico:** Toda matriz anti-simétrica tem diagonal principal nula e elementos simétricos opostos ($k_{21} = -k_{12}$).

---

### `G01-E03` *(Determinante `4x4` por triangulação e propriedades)*
- **Passo a passo:**
  - **(a)** Redução à forma triangular superior:
    $$D = \begin{bmatrix} 1 & 2 & -1 & 0 \\ 2 & 5 & 0 & 1 \\ -1 & 0 & 3 & 2 \\ 0 & 2 & 2 & 5 \end{bmatrix} \xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(1)}} \begin{bmatrix} 1 & 2 & -1 & 0 \\ 0 & 1 & 2 & 1 \\ 0 & 2 & 2 & 2 \\ 0 & 2 & 2 & 5 \end{bmatrix}$$
    $$\xrightarrow{\substack{L_3' = L_3 + L_2(-2) \\ L_4' = L_4 + L_2(-2)}} \begin{bmatrix} 1 & 2 & -1 & 0 \\ 0 & 1 & 2 & 1 \\ 0 & 0 & -2 & 0 \\ 0 & 0 & -2 & 3 \end{bmatrix} \xrightarrow{L_4' = L_4 + L_3(-1)} \begin{bmatrix} 1 & 2 & -1 & 0 \\ 0 & 1 & 2 & 1 \\ 0 & 0 & -2 & 0 \\ 0 & 0 & 0 & 3 \end{bmatrix}.$$
    Como foram usadas apenas substituições $L_j' = L_j + L_i(\alpha)$ (que preservam o determinante):
    $$\det(D) = 1 \cdot 1 \cdot (-2) \cdot 3 = -6.$$
  - **(b)** Pelas propriedades ($\text{ordem } n = 3$):
    $$\det(2\,P^T Q^{-1}) = 2^3 \cdot \det(P^T) \cdot \det(Q^{-1}) = 8 \cdot \det(P) \cdot \frac{1}{\det(Q)} = 8 \cdot (-2) \cdot \frac{1}{3} = -\frac{16}{3}.$$
- **Resposta Final:** `(a) -6 (b) -16/3`
- **Alerta pedagógico:** Em $\det(2\,P^T Q^{-1})$, o escalar $2$ sai elevado à ordem $n=3$ ($2^3 = 8$), nunca como fator $2$ simples.

---

### `G01-E04` *(Equação de singularidade por cofatores — sem perder `k = 0`)*
- **Passo a passo:**
  - Desenvolvendo $\det(S)$ pela **2ª coluna** (dois zeros):
    $$\det(S) = (-1)^{2+2}\,k\,\begin{vmatrix} k & 3 \\ 1 & k - 2 \end{vmatrix} = k\big(k(k-2) - 3\big) = k(k^2 - 2k - 3) = k(k - 3)(k + 1).$$
  - Igualando $\det(S) = 0$: obtemos $k = 0$, $k = 3$ ou $k = -1$.
- **Resposta Final:** `-1, 0, 3`
- **Alerta pedagógico:** Nunca divida a equação $k(k^2 - 2k - 3) = 0$ por $k$: isso eliminaria a raiz $k = 0$.

---

### `G01-E05` *(Inversão `[A | I_3]` aplicada a equação matricial com transposta)*
- **Passo a passo:**
  - **(a)** Escalonamento de $[A \mid I_3]$:
    $$\left[\begin{array}{ccc|ccc} 1 & 0 & 1 & 1 & 0 & 0 \\ 0 & 2 & 1 & 0 & 1 & 0 \\ 1 & 1 & 2 & 0 & 0 & 1 \end{array}\right] \xrightarrow{L_3' = L_3 - L_1} \left[\begin{array}{ccc|ccc} 1 & 0 & 1 & 1 & 0 & 0 \\ 0 & 2 & 1 & 0 & 1 & 0 \\ 0 & 1 & 1 & -1 & 0 & 1 \end{array}\right]$$
    $$\xrightarrow{L_2 \leftrightarrow L_3} \left[\begin{array}{ccc|ccc} 1 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & -1 & 0 & 1 \\ 0 & 2 & 1 & 0 & 1 & 0 \end{array}\right] \xrightarrow{L_3' = L_3 - 2L_2} \left[\begin{array}{ccc|ccc} 1 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & -1 & 0 & 1 \\ 0 & 0 & -1 & 2 & 1 & -2 \end{array}\right]$$
    $$\xrightarrow{L_3(-1)} \left[\begin{array}{ccc|ccc} 1 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & -1 & 0 & 1 \\ 0 & 0 & 1 & -2 & -1 & 2 \end{array}\right] \xrightarrow{\substack{L_1' = L_1 - L_3 \\ L_2' = L_2 - L_3}} \left[\begin{array}{ccc|ccc} 1 & 0 & 0 & 3 & 1 & -2 \\ 0 & 1 & 0 & 1 & 1 & -1 \\ 0 & 0 & 1 & -2 & -1 & 2 \end{array}\right].$$
    Logo, $A^{-1} = \begin{bmatrix} 3 & 1 & -2 \\ 1 & 1 & -1 \\ -2 & -1 & 2 \end{bmatrix}$.
  - **(b)** Isolando $X^T$:
    $$A X^T = C - B = \begin{bmatrix} 4-2 & 1-(-1) & 2-0 \\ 3-1 & 5-3 & 0-(-2) \\ 3-0 & 4-1 & 5-1 \end{bmatrix} = \begin{bmatrix} 2 & 2 & 2 \\ 2 & 2 & 2 \\ 3 & 3 & 4 \end{bmatrix}.$$
    Multiplicando à esquerda por $A^{-1}$:
    $$X^T = A^{-1}(C - B) = \begin{bmatrix} 3 & 1 & -2 \\ 1 & 1 & -1 \\ -2 & -1 & 2 \end{bmatrix}\begin{bmatrix} 2 & 2 & 2 \\ 2 & 2 & 2 \\ 3 & 3 & 4 \end{bmatrix} = \begin{bmatrix} 2 & 2 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 2 \end{bmatrix}.$$
    Transpondo para obter $X$:
    $$X = \begin{bmatrix} 2 & 1 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 2 \end{bmatrix}.$$
- **Resposta Final:** `(a) [[3, 1, -2], [1, 1, -1], [-2, -1, 2]] (b) [[2, 1, 0], [2, 1, 0], [0, 0, 2]]`
- **Alerta pedagógico:** A equação fornece primeiro $X^T$; não entregue $X^T$ sem aplicar a transposição final.

---

## 2. Checagem Independente

### `G01-C01` *(Determinante `4x4` com pivô inicial nulo)*
- **Passo a passo:**
  - Trocando $L_1 \leftrightarrow L_2$ (fator $-1$ no determinante):
    $$\det(M) = -\begin{vmatrix} 1 & -1 & 1 & 2 \\ 0 & 1 & -2 & 1 \\ 2 & 0 & 1 & -1 \\ -1 & 2 & 0 & 3 \end{vmatrix} \xrightarrow{\substack{L_3' = L_3 - 2L_1 \\ L_4' = L_4 + L_1}} -\begin{vmatrix} 1 & -1 & 1 & 2 \\ 0 & 1 & -2 & 1 \\ 0 & 2 & -1 & -5 \\ 0 & 1 & 1 & 5 \end{vmatrix}$$
    $$\xrightarrow{\substack{L_3' = L_3 - 2L_2 \\ L_4' = L_4 - L_2}} -\begin{vmatrix} 1 & -1 & 1 & 2 \\ 0 & 1 & -2 & 1 \\ 0 & 0 & 3 & -7 \\ 0 & 0 & 3 & 4 \end{vmatrix} \xrightarrow{L_4' = L_4 - L_3} -\begin{vmatrix} 1 & -1 & 1 & 2 \\ 0 & 1 & -2 & 1 \\ 0 & 0 & 3 & -7 \\ 0 & 0 & 0 & 11 \end{vmatrix}.$$
  - Logo, $\det(M) = -(1 \cdot 1 \cdot 3 \cdot 11) = -33$.
- **Resposta Final:** `-33`
- **Alerta pedagógico:** A permutação inicial $L_1 \leftrightarrow L_2$ introduz obrigatoriamente o sinal negativo ($-1$).

---

### `G01-C02` *(Singularidade com raiz nula e fração)*
- **Passo a passo:**
  - $T$ não admite inversa quando $\det(T) = 0$. Desenvolvendo pela **3ª coluna**:
    $$\det(T) = (-1)^{3+3}\,m\,\begin{vmatrix} m & 1 \\ 3 & 2m - 1 \end{vmatrix} = m\big(m(2m - 1) - 3\big) = m(2m^2 - m - 3) = m(2m - 3)(m + 1).$$
  - Igualando a zero: $m = 0$, $m = \frac{3}{2}$ ou $m = -1$.
- **Resposta Final:** `-1, 0, 3/2`
- **Alerta pedagógico:** Verifique as três raízes substituindo em $2m^2 - m - 3 = 0$ e mantendo a raiz $m = 0$ em evidência.

---

### `G01-C03` *(Inversão `[A | I_3]` e equação matricial `XA = B`)*
- **Passo a passo:**
  - **(a)** Reduzindo $[A \mid I_3]$:
    $$\left[\begin{array}{ccc|ccc} 1 & 2 & 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 2 & 3 & 2 & 0 & 0 & 1 \end{array}\right] \xrightarrow{L_3' = L_3 - 2L_1} \left[\begin{array}{ccc|ccc} 1 & 2 & 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & -1 & 2 & -2 & 0 & 1 \end{array}\right]$$
    $$\xrightarrow{L_3' = L_3 + L_2} \left[\begin{array}{ccc|ccc} 1 & 2 & 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & 0 & 3 & -2 & 1 & 1 \end{array}\right] \xrightarrow{L_3(1/3)} \left[\begin{array}{ccc|ccc} 1 & 2 & 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & 0 & 1 & -2/3 & 1/3 & 1/3 \end{array}\right]$$
    $$\xrightarrow{L_2' = L_2 - L_3} \left[\begin{array}{ccc|ccc} 1 & 2 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 2/3 & 2/3 & -1/3 \\ 0 & 0 & 1 & -2/3 & 1/3 & 1/3 \end{array}\right] \xrightarrow{L_1' = L_1 - 2L_2} \left[\begin{array}{ccc|ccc} 1 & 0 & 0 & -1/3 & -4/3 & 2/3 \\ 0 & 1 & 0 & 2/3 & 2/3 & -1/3 \\ 0 & 0 & 1 & -2/3 & 1/3 & 1/3 \end{array}\right].$$
    Portanto, $A^{-1} = \begin{bmatrix} -1/3 & -4/3 & 2/3 \\ 2/3 & 2/3 & -1/3 \\ -2/3 & 1/3 & 1/3 \end{bmatrix}$.
  - **(b)** Como $X A = B$, multiplicamos por $A^{-1}$ **à direita**:
    $$X = B A^{-1} = \begin{bmatrix} 3 & 5 & 1 \\ -1 & 0 & 2 \end{bmatrix}\begin{bmatrix} -1/3 & -4/3 & 2/3 \\ 2/3 & 2/3 & -1/3 \\ -2/3 & 1/3 & 1/3 \end{bmatrix} = \begin{bmatrix} 5/3 & -1/3 & 2/3 \\ -1 & 2 & 0 \end{bmatrix}.$$
- **Resposta Final:** `(a) [[-1/3, -4/3, 2/3], [2/3, 2/3, -1/3], [-2/3, 1/3, 1/3]] (b) [[5/3, -1/3, 2/3], [-1, 2, 0]]`
- **Alerta pedagógico:** Em $XA = B$, o produto $A^{-1} B$ nem sequer está definido porque $A^{-1}$ é $3\times 3$ e $B$ é $2\times 3$; o lado correto é $X = B A^{-1}$.
