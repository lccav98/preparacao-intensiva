# Gabarito Comentado — Bloco `C04` (Método da Matriz Inversa `X = A^{-1}B`)

> **Bloco de referência:** [C04_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_C/blocos/C04_bloco.md)  
> **Nota para Caça ao Bug (`C04-E03`):** Matriz singular ($\det(A) = 0$) não possui inversa; além disso, $X = A^{-1}B$ exige multiplicação à esquerda.

---

## 1. Gabarito dos Exercícios (`C04-E01` a `C04-E05`)

### `C04-E01`
$$\left[\begin{array}{cc|cc} 3 & 5 & 1 & 0 \\ 1 & 2 & 0 & 1 \end{array}\right] \xrightarrow{L_{12}} \left[\begin{array}{cc|cc} 1 & 2 & 0 & 1 \\ 3 & 5 & 1 & 0 \end{array}\right] \xrightarrow{L_2' = L_2 + L_1(-3)} \left[\begin{array}{cc|cc} 1 & 2 & 0 & 1 \\ 0 & -1 & 1 & -3 \end{array}\right]$$
$$\xrightarrow{L_2(-1)} \left[\begin{array}{cc|cc} 1 & 2 & 0 & 1 \\ 0 & 1 & -1 & 3 \end{array}\right] \xrightarrow{L_1' = L_1 + L_2(-2)} \left[\begin{array}{cc|cc} 1 & 0 & 2 & -5 \\ 0 & 1 & -1 & 3 \end{array}\right]$$
Logo $A^{-1} = \begin{bmatrix} 2 & -5 \\ -1 & 3 \end{bmatrix}$ e $X = A^{-1}B = \begin{bmatrix} 2 & -5 \\ -1 & 3 \end{bmatrix}\begin{bmatrix} 7 \\ 2 \end{bmatrix} = \begin{bmatrix} 4 \\ -1 \end{bmatrix}$.
- **Resposta final:** `inversa: [[2, -5], [-1, 3]]; solucao: (4, -1)`.

### `C04-E02` *(Lista 5 Ex. 20 e 22)*
$$\left[\begin{array}{ccc|ccc} 1 & 2 & -2 & 1 & 0 & 0 \\ 2 & 5 & -4 & 0 & 1 & 0 \\ 3 & 7 & -5 & 0 & 0 & 1 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(-3)}} \left[\begin{array}{ccc|ccc} 1 & 2 & -2 & 1 & 0 & 0 \\ 0 & 1 & 0 & -2 & 1 & 0 \\ 0 & 1 & 1 & -3 & 0 & 1 \end{array}\right]$$
$$\xrightarrow{\substack{L_1' = L_1 + L_2(-2) \\ L_3' = L_3 + L_2(-1)}} \left[\begin{array}{ccc|ccc} 1 & 0 & -2 & 5 & -2 & 0 \\ 0 & 1 & 0 & -2 & 1 & 0 \\ 0 & 0 & 1 & -1 & -1 & 1 \end{array}\right] \xrightarrow{L_1' = L_1 + L_3(2)} \left[\begin{array}{ccc|ccc} 1 & 0 & 0 & 3 & -4 & 2 \\ 0 & 1 & 0 & -2 & 1 & 0 \\ 0 & 0 & 1 & -1 & -1 & 1 \end{array}\right]$$
- **(a)** $A^{-1} = \begin{bmatrix} 3 & -4 & 2 \\ -2 & 1 & 0 \\ -1 & -1 & 1 \end{bmatrix}$.
- **(b)** $X^{(1)} = A^{-1}\begin{bmatrix} 0 \\ 3 \\ 7 \end{bmatrix} = \begin{bmatrix} 0 - 12 + 14 \\ 0 + 3 + 0 \\ 0 - 3 + 7 \end{bmatrix} = \begin{bmatrix} 2 \\ 3 \\ 4 \end{bmatrix}$.
- **(c)** $X^{(2)} = A^{-1}\begin{bmatrix} 1 \\ 7 \\ 6 \end{bmatrix} = \begin{bmatrix} 3 - 28 + 12 \\ -2 + 7 + 0 \\ -1 - 7 + 6 \end{bmatrix} = \begin{bmatrix} -13 \\ 5 \\ -2 \end{bmatrix}$.
- **Resposta final:** `inversa: [[3, -4, 2], [-2, 1, 0], [-1, -1, 1]]; solucao1: (2, 3, 4); solucao2: (-13, 5, -2)`.

### `C04-E03` *(Caça ao Bug)*
- **Diagnóstico:** Na matriz $A$, $L_2 = 2L_1$; ao aplicar $L_2' = L_2 + L_1(-2)$ em `[A | I]`, toda a 2ª linha do lado esquerdo zera (`[0 0 0 | -2 1 0]`), provando que $A$ é singular (não inversível). Além disso, o produto $B A^{-1}$ não está definido porque $B$ é $3 \times 1$ e $A^{-1}$ seria $3 \times 3$.
- Escalonando `[A | B]`, a 2ª linha resulta `[0 0 0 | 1]`, indicando $0 = 1$, logo o sistema é **incompatível (`SI`)**.
- **Resposta final:** `inversivel: nao; classificacao: SI`.

### `C04-E04` *(Apostila p. 25–31)*
$$\left[\begin{array}{ccc|ccc} 2 & 1 & 3 & 1 & 0 & 0 \\ 4 & 2 & 2 & 0 & 1 & 0 \\ 2 & 5 & 3 & 0 & 0 & 1 \end{array}\right] \xrightarrow{L_1(1/2)} \left[\begin{array}{ccc|ccc} 1 & 1/2 & 3/2 & 1/2 & 0 & 0 \\ 4 & 2 & 2 & 0 & 1 & 0 \\ 2 & 5 & 3 & 0 & 0 & 1 \end{array}\right]$$
$$\xrightarrow{\substack{L_2' = L_2 + L_1(-4) \\ L_3' = L_3 + L_1(-2)}} \left[\begin{array}{ccc|ccc} 1 & 1/2 & 3/2 & 1/2 & 0 & 0 \\ 0 & 0 & -4 & -2 & 1 & 0 \\ 0 & 4 & 0 & -1 & 0 & 1 \end{array}\right] \xrightarrow{\substack{L_{23} \\ L_2(1/4),\; L_3(-1/4)}} \left[\begin{array}{ccc|ccc} 1 & 1/2 & 3/2 & 1/2 & 0 & 0 \\ 0 & 1 & 0 & -1/4 & 0 & 1/4 \\ 0 & 0 & 1 & 1/2 & -1/4 & 0 \end{array}\right]$$
$$\xrightarrow{L_1' = L_1 + L_2(-1/2)} \left[\begin{array}{ccc|ccc} 1 & 0 & 3/2 & 5/8 & 0 & -1/8 \\ 0 & 1 & 0 & -1/4 & 0 & 1/4 \\ 0 & 0 & 1 & 1/2 & -1/4 & 0 \end{array}\right] \xrightarrow{L_1' = L_1 + L_3(-3/2)} \left[\begin{array}{ccc|ccc} 1 & 0 & 0 & -1/8 & 3/8 & -1/8 \\ 0 & 1 & 0 & -1/4 & 0 & 1/4 \\ 0 & 0 & 1 & 1/2 & -1/4 & 0 \end{array}\right]$$
Logo $X = A^{-1}\begin{bmatrix} 17 \\ 18 \\ 21 \end{bmatrix} = \begin{bmatrix} -17/8 + 54/8 - 21/8 \\ -17/4 + 0 + 21/4 \\ 17/2 - 18/4 + 0 \end{bmatrix} = \begin{bmatrix} 16/8 \\ 4/4 \\ 16/4 \end{bmatrix} = \begin{bmatrix} 2 \\ 1 \\ 4 \end{bmatrix}$.
- **Resposta final:** `inversa: [[-1/8, 3/8, -1/8], [-1/4, 0, 1/4], [1/2, -1/4, 0]]; solucao: (2, 1, 4)`.

### `C04-E05`
$$\left[\begin{array}{ccc|ccc} 1 & 1 & 1 & 1 & 0 & 0 \\ 0 & 2 & 1 & 0 & 1 & 0 \\ 1 & 3 & 3 & 0 & 0 & 1 \end{array}\right] \xrightarrow{L_3' = L_3 + L_1(-1)} \left[\begin{array}{ccc|ccc} 1 & 1 & 1 & 1 & 0 & 0 \\ 0 & 2 & 1 & 0 & 1 & 0 \\ 0 & 2 & 2 & -1 & 0 & 1 \end{array}\right] \xrightarrow{\substack{L_3' = L_3 + L_2(-1) \\ L_2(1/2)}} \left[\begin{array}{ccc|ccc} 1 & 1 & 1 & 1 & 0 & 0 \\ 0 & 1 & 1/2 & 0 & 1/2 & 0 \\ 0 & 0 & 1 & -1 & -1 & 1 \end{array}\right]$$
$$\xrightarrow{\substack{L_1' = L_1 + L_2(-1) \\ L_2' = L_2 + L_3(-1/2)}} \left[\begin{array}{ccc|ccc} 1 & 0 & 1/2 & 1 & -1/2 & 0 \\ 0 & 1 & 0 & 1/2 & 1 & -1/2 \\ 0 & 0 & 1 & -1 & -1 & 1 \end{array}\right] \xrightarrow{L_1' = L_1 + L_3(-1/2)} \left[\begin{array}{ccc|ccc} 1 & 0 & 0 & 3/2 & 0 & -1/2 \\ 0 & 1 & 0 & 1/2 & 1 & -1/2 \\ 0 & 0 & 1 & -1 & -1 & 1 \end{array}\right]$$
- $X^{(1)} = A^{-1}\begin{bmatrix} 3 \\ 1 \\ 4 \end{bmatrix} = \begin{bmatrix} 9/2 + 0 - 2 \\ 3/2 + 1 - 2 \\ -3 - 1 + 4 \end{bmatrix} = \begin{bmatrix} 5/2 \\ 1/2 \\ 0 \end{bmatrix}$.
- $X^{(2)} = A^{-1}\begin{bmatrix} 1 \\ 2 \\ 5 \end{bmatrix} = \begin{bmatrix} 3/2 + 0 - 5/2 \\ 1/2 + 2 - 5/2 \\ -1 - 2 + 5 \end{bmatrix} = \begin{bmatrix} -1 \\ 0 \\ 2 \end{bmatrix}$.
- **Resposta final:** `inversa: [[3/2, 0, -1/2], [1/2, 1, -1/2], [-1, -1, 1]]; solucao1: (5/2, 1/2, 0); solucao2: (-1, 0, 2)`.

---

## 2. Gabarito da Checagem Independente (`C04-C01` a `C04-C03`)

### `C04-C01`
$$\left[\begin{array}{cc|cc} 4 & 3 & 1 & 0 \\ 3 & 2 & 0 & 1 \end{array}\right] \xrightarrow{L_1' = L_1 + L_2(-1)} \left[\begin{array}{cc|cc} 1 & 1 & 1 & -1 \\ 3 & 2 & 0 & 1 \end{array}\right] \xrightarrow{L_2' = L_2 + L_1(-3)} \left[\begin{array}{cc|cc} 1 & 1 & 1 & -1 \\ 0 & -1 & -3 & 4 \end{array}\right]$$
$$\xrightarrow{L_2(-1),\; L_1' = L_1 + L_2(-1)} \left[\begin{array}{cc|cc} 1 & 0 & -2 & 3 \\ 0 & 1 & 3 & -4 \end{array}\right]$$
Logo $A^{-1} = \begin{bmatrix} -2 & 3 \\ 3 & -4 \end{bmatrix}$; $X^{(1)} = A^{-1}\begin{bmatrix} 5 \\ 4 \end{bmatrix} = \begin{bmatrix} 2 \\ -1 \end{bmatrix}$; $X^{(2)} = A^{-1}\begin{bmatrix} 1 \\ -2 \end{bmatrix} = \begin{bmatrix} -8 \\ 11 \end{bmatrix}$.
- **Resposta final:** `inversa: [[-2, 3], [3, -4]]; solucao1: (2, -1); solucao2: (-8, 11)`.

### `C04-C02`
$$\left[\begin{array}{ccc|ccc} 1 & 0 & 2 & 1 & 0 & 0 \\ 2 & -1 & 3 & 0 & 1 & 0 \\ 4 & 1 & 8 & 0 & 0 & 1 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(-4)}} \left[\begin{array}{ccc|ccc} 1 & 0 & 2 & 1 & 0 & 0 \\ 0 & -1 & -1 & -2 & 1 & 0 \\ 0 & 1 & 0 & -4 & 0 & 1 \end{array}\right]$$
$$\xrightarrow{L_{23},\; L_3' = L_3 + L_2(1)} \left[\begin{array}{ccc|ccc} 1 & 0 & 2 & 1 & 0 & 0 \\ 0 & 1 & 0 & -4 & 0 & 1 \\ 0 & 0 & -1 & -6 & 1 & 1 \end{array}\right] \xrightarrow{\substack{L_3(-1) \\ L_1' = L_1 + L_3(-2)}} \left[\begin{array}{ccc|ccc} 1 & 0 & 0 & -11 & 2 & 2 \\ 0 & 1 & 0 & -4 & 0 & 1 \\ 0 & 0 & 1 & 6 & -1 & -1 \end{array}\right]$$
$X = A^{-1}\begin{bmatrix} 3 \\ 1 \\ 7 \end{bmatrix} = \begin{bmatrix} -33 + 2 + 14 \\ -12 + 0 + 7 \\ 18 - 1 - 7 \end{bmatrix} = \begin{bmatrix} -17 \\ -5 \\ 10 \end{bmatrix}$.
- **Resposta final:** `inversa: [[-11, 2, 2], [-4, 0, 1], [6, -1, -1]]; solucao: (-17, -5, 10)`.

### `C04-C03` *(Lista 5 Ex. 23 + vetor extra)*
- **(a)** $X^{(1)} = \begin{bmatrix} 3 & -4 & 2 \\ -2 & 1 & 0 \\ -1 & -1 & 1 \end{bmatrix}\begin{bmatrix} 3 \\ 2 \\ 5 \end{bmatrix} = \begin{bmatrix} 9 - 8 + 10 \\ -6 + 2 + 0 \\ -3 - 2 + 5 \end{bmatrix} = \begin{bmatrix} 11 \\ -4 \\ 0 \end{bmatrix}$.
- **(b)** $X^{(2)} = \begin{bmatrix} 3 & -4 & 2 \\ -2 & 1 & 0 \\ -1 & -1 & 1 \end{bmatrix}\begin{bmatrix} -1 \\ 0 \\ 2 \end{bmatrix} = \begin{bmatrix} -3 + 0 + 4 \\ 2 + 0 + 0 \\ 1 + 0 + 2 \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$.
- **Resposta final:** `solucao1: (11, -4, 0); solucao2: (1, 2, 3)`.
