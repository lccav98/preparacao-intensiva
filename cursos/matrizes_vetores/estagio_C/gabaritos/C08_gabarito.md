# Gabarito Comentado — Bloco `C08` (Revisão Cumulativa do Estágio C)

> **Bloco de referência:** [C08_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_C/blocos/C08_bloco.md)

---

## 1. Gabarito dos Exercícios (`C08-E01` a `C08-E05`)

### `C08-E01`
$$A = \left[\begin{array}{ccc|c} 2 & -2 & 4 & 5 \\ 1 & 3 & -1 & 2 \\ 3 & 1 & 2 & 4 \end{array}\right] \xrightarrow{L_{12}} \left[\begin{array}{ccc|c} 1 & 3 & -1 & 2 \\ 2 & -2 & 4 & 5 \\ 3 & 1 & 2 & 4 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(-3)}} \left[\begin{array}{ccc|c} 1 & 3 & -1 & 2 \\ 0 & -8 & 6 & 1 \\ 0 & -8 & 5 & -2 \end{array}\right]$$
$$\xrightarrow{L_3' = L_3 + L_2(-1)} \left[\begin{array}{ccc|c} 1 & 3 & -1 & 2 \\ 0 & -8 & 6 & 1 \\ 0 & 0 & -1 & -3 \end{array}\right] \xrightarrow{\substack{L_3(-1) \\ L_2' = L_2 + L_3(-6) \\ L_1' = L_1 + L_3(1)}} \left[\begin{array}{ccc|c} 1 & 3 & 0 & 5 \\ 0 & -8 & 0 & -17 \\ 0 & 0 & 1 & 3 \end{array}\right]$$
$$\xrightarrow{\substack{L_2(-1/8) \\ L_1' = L_1 + L_2(-3)}} \left[\begin{array}{ccc|c} 1 & 0 & 0 & -11/8 \\ 0 & 1 & 0 & 17/8 \\ 0 & 0 & 1 & 3 \end{array}\right]$$
- **Resposta final:** `(-11/8, 17/8, 3)`.

### `C08-E02`
$$\left[\begin{array}{ccc|ccc} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 1 & 0 & 2 & 0 & 0 & 1 \end{array}\right] \xrightarrow{L_3' = L_3 + L_1(-1)} \left[\begin{array}{ccc|ccc} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & -1 & 2 & -1 & 0 & 1 \end{array}\right] \xrightarrow{\substack{L_1' = L_1 + L_2(-1) \\ L_3' = L_3 + L_2(1)}} \left[\begin{array}{ccc|ccc} 1 & 0 & -1 & 1 & -1 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & 0 & 3 & -1 & 1 & 1 \end{array}\right]$$
$$\xrightarrow{\substack{L_3(1/3) \\ L_1' = L_1 + L_3(1),\; L_2' = L_2 + L_3(-1)}} \left[\begin{array}{ccc|ccc} 1 & 0 & 0 & 2/3 & -2/3 & 1/3 \\ 0 & 1 & 0 & 1/3 & 2/3 & -1/3 \\ 0 & 0 & 1 & -1/3 & 1/3 & 1/3 \end{array}\right]$$
- $X^{(1)} = A^{-1}\begin{bmatrix} 3 \\ 5 \\ 7 \end{bmatrix} = \begin{bmatrix} 2 - 10/3 + 7/3 \\ 1 + 10/3 - 7/3 \\ -1 + 5/3 + 7/3 \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$.
- $X^{(2)} = A^{-1}\begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix} = \begin{bmatrix} 2/3 + 0 + 2/3 \\ 1/3 + 0 - 2/3 \\ -1/3 + 0 + 2/3 \end{bmatrix} = \begin{bmatrix} 4/3 \\ -1/3 \\ 1/3 \end{bmatrix}$.
- **Resposta final:** `inversa: [[2/3, -2/3, 1/3], [1/3, 2/3, -1/3], [-1/3, 1/3, 1/3]]; solucao1: (1, 2, 3); solucao2: (4/3, -1/3, 1/3)`.

### `C08-E03`
$$A = \left[\begin{array}{ccc|c} 1 & 2 & -1 & 3 \\ 2 & 5 & 1 & 8 \\ 1 & 3 & 2 & 5 \\ 3 & 8 & 0 & 11 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(-1) \\ L_4' = L_4 + L_1(-3)}} \left[\begin{array}{ccc|c} 1 & 2 & -1 & 3 \\ 0 & 1 & 3 & 2 \\ 0 & 1 & 3 & 2 \\ 0 & 2 & 3 & 2 \end{array}\right] \xrightarrow{\substack{L_1' = L_1 + L_2(-2) \\ L_3' = L_3 + L_2(-1) \\ L_4' = L_4 + L_2(-2)}} \left[\begin{array}{ccc|c} 1 & 0 & -7 & -1 \\ 0 & 1 & 3 & 2 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & -3 & -2 \end{array}\right]$$
$$\xrightarrow{\substack{L_{34},\; L_3(-1/3) \\ L_1' = L_1 + L_3(7),\; L_2' = L_2 + L_3(-3)}} \left[\begin{array}{ccc|c} 1 & 0 & 0 & 11/3 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 2/3 \\ 0 & 0 & 0 & 0 \end{array}\right] = B$$
$C_A = 3$, $C_V = 3$, $C = 3 = n \Rightarrow g = 0$, **`SPD`**, solução `(11/3, 0, 2/3)`.
- **Resposta final:** `ca: 3; cv: 3; g: 0; classificacao: SPD; solucao: (11/3, 0, 2/3)`.

### `C08-E04`
Desenvolvendo $\det(A)$ pela 1ª linha (sem Sarrus):
$$\det\begin{bmatrix} k & 1 & 1 \\ 1 & k & 1 \\ 1 & 1 & k \end{bmatrix} = k(k^2 - 1) - 1(k - 1) + 1(1 - k) = k(k-1)(k+1) - 2(k-1) = (k-1)(k^2 + k - 2) = (k-1)^2(k+2).$$
Igualando a zero: $(k-1)^2(k+2) = 0 \Rightarrow \mathbf{k = 1\text{ ou }k = -2}$.
*(Verificação via forma de escada: para $k = 1$, $B$ tem $C = 1, g = 2$; para $k = -2$, $B$ tem $C = 2, g = 1$.)*
- **Resposta final:** `k = -2 ou k = 1`.

### `C08-E05`
$$\left[\begin{array}{ccc|c} 1 & 1 & -2 & a \\ 2 & -1 & 1 & b \\ 4 & 1 & -3 & c \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(-4)}} \left[\begin{array}{ccc|c} 1 & 1 & -2 & a \\ 0 & -3 & 5 & b - 2a \\ 0 & -3 & 5 & c - 4a \end{array}\right] \xrightarrow{L_3' = L_3 + L_2(-1)} \left[\begin{array}{ccc|c} 1 & 1 & -2 & a \\ 0 & -3 & 5 & b - 2a \\ 0 & 0 & 0 & c - 2a - b \end{array}\right]$$
Compatível $\iff C_A = C_V \iff c - 2a - b = 0 \iff \mathbf{2a + b - c = 0}$.
- **Resposta final:** `2a + b - c = 0`.

---

## 2. Gabarito da Checagem Independente (`C08-C01` a `C08-C03`)

### `C08-C01`
$$\left[\begin{array}{ccc|c} 1 & -1 & 2 & 4 \\ 2 & -2 & 4 & 8 \\ 3 & -1 & 1 & 7 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(-3)}} \left[\begin{array}{ccc|c} 1 & -1 & 2 & 4 \\ 0 & 0 & 0 & 0 \\ 0 & 2 & -5 & -5 \end{array}\right] \xrightarrow{\substack{L_{23},\; L_2(1/2) \\ L_1' = L_1 + L_2(1)}} \left[\begin{array}{ccc|c} 1 & 0 & -1/2 & 3/2 \\ 0 & 1 & -5/2 & -5/2 \\ 0 & 0 & 0 & 0 \end{array}\right] = B$$
$C_A = 2$, $C_V = 2$, $C = 2 < n = 3 \Rightarrow g = 1$, **`SPI`**.
Logo $x = \frac{3 + z}{2}$ e $y = \frac{-5 + 5z}{2}$. Para $z = 1$: $x = 2$, $y = 0 \Rightarrow (2, 0, 1)$.
- **Resposta final:** `ca: 2; cv: 2; g: 1; classificacao: SPI; solucao: (2, 0, 1)`.

### `C08-C02`
$$\left[\begin{array}{ccc|ccc} 2 & 1 & 0 & 1 & 0 & 0 \\ 1 & 1 & 1 & 0 & 1 & 0 \\ 0 & 1 & 3 & 0 & 0 & 1 \end{array}\right] \xrightarrow{L_{12}} \left[\begin{array}{ccc|ccc} 1 & 1 & 1 & 0 & 1 & 0 \\ 2 & 1 & 0 & 1 & 0 & 0 \\ 0 & 1 & 3 & 0 & 0 & 1 \end{array}\right] \xrightarrow{L_2' = L_2 + L_1(-2)} \left[\begin{array}{ccc|ccc} 1 & 1 & 1 & 0 & 1 & 0 \\ 0 & -1 & -2 & 1 & -2 & 0 \\ 0 & 1 & 3 & 0 & 0 & 1 \end{array}\right]$$
$$\xrightarrow{\substack{L_2(-1) \\ L_1' = L_1 + L_2(-1) \\ L_3' = L_3 + L_2(-1)}} \left[\begin{array}{ccc|ccc} 1 & 0 & -1 & 1 & -1 & 0 \\ 0 & 1 & 2 & -1 & 2 & 0 \\ 0 & 0 & 1 & 1 & -2 & 1 \end{array}\right] \xrightarrow{\substack{L_1' = L_1 + L_3(1) \\ L_2' = L_2 + L_3(-2)}} \left[\begin{array}{ccc|ccc} 1 & 0 & 0 & 2 & -3 & 1 \\ 0 & 1 & 0 & -3 & 6 & -2 \\ 0 & 0 & 1 & 1 & -2 & 1 \end{array}\right]$$
Logo $X = A^{-1}\begin{bmatrix} 4 \\ 3 \\ 2 \end{bmatrix} = \begin{bmatrix} 8 - 9 + 2 \\ -12 + 18 - 4 \\ 4 - 6 + 2 \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \\ 0 \end{bmatrix}$.
- **Resposta final:** `inversa: [[2, -3, 1], [-3, 6, -2], [1, -2, 1]]; solucao: (1, 2, 0)`.

### `C08-C03`
$$\left[\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 1 & 2 & k & 2 \\ 2 & 3 & k^2 - 1 & k + 1 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-1) \\ L_3' = L_3 + L_1(-2)}} \left[\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 0 & 1 & k - 1 & 1 \\ 0 & 1 & k^2 - 3 & k - 1 \end{array}\right] \xrightarrow{L_3' = L_3 + L_2(-1)} \left[\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 0 & 1 & k - 1 & 1 \\ 0 & 0 & k^2 - k - 2 & k - 2 \end{array}\right]$$
Fatorando $k^2 - k - 2 = (k - 2)(k + 1)$:
- **(a)** Para **$k = 2$**, a 3ª linha torna-se `[0  0  0 | 0]` $\Rightarrow$ **`SPI`**.
- **(b)** Para **$k = -1$**, a 3ª linha torna-se `[0  0  0 | -3]` $\Rightarrow$ **`SI`**.
- **Resposta final:** `spi: 2; si: -1`.
