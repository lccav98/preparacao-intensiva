# Gabarito Comentado — Bloco `C06` (Grau de Liberdade `g = n - C` e Sistemas Homogêneos)

> **Bloco de referência:** [C06_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_C/blocos/C06_bloco.md)  
> **Nota para Caça ao Bug (`C06-E05`):** Ao resolver $k^2 - 4 = 0$, ambas as raízes ($k = 2$ e $k = -2$) anulam o determinante / último pivô.

---

## 1. Gabarito dos Exercícios (`C06-E01` a `C06-E05`)

### `C06-E01` *(Lista 5 Ex. 4)*
$$A = \left[\begin{array}{ccc|c} 1 & 1 & -1 & 0 \\ 2 & -3 & 1 & 0 \\ 4 & -4 & -2 & 0 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(-4)}} \left[\begin{array}{ccc|c} 1 & 1 & -1 & 0 \\ 0 & -5 & 3 & 0 \\ 0 & -8 & 2 & 0 \end{array}\right] \xrightarrow{L_2(-1/5)} \left[\begin{array}{ccc|c} 1 & 1 & -1 & 0 \\ 0 & 1 & -3/5 & 0 \\ 0 & -8 & 2 & 0 \end{array}\right]$$
$$\xrightarrow{\substack{L_1' = L_1 + L_2(-1) \\ L_3' = L_3 + L_2(8)}} \left[\begin{array}{ccc|c} 1 & 0 & -2/5 & 0 \\ 0 & 1 & -3/5 & 0 \\ 0 & 0 & -14/5 & 0 \end{array}\right] \xrightarrow{\substack{L_3(-5/14) \\ L_1' = L_1 + L_3(2/5),\; L_2' = L_2 + L_3(3/5)}} \left[\begin{array}{ccc|c} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{array}\right] = B$$
$C_A = 3$, $C_V = 3$, $C = 3 = n \Rightarrow g = 0$, **`SPD`**, apenas a **solução trivial** `(0, 0, 0)`.
- **Resposta final:** `ca: 3; cv: 3; g: 0; classificacao: SPD; solucao: (0, 0, 0)`.

### `C06-E02` *(Lista 5 Ex. 7)*
$$A = \left[\begin{array}{ccc|c} 6 & 2 & 4 & 0 \\ -9 & -3 & -6 & 0 \end{array}\right] \xrightarrow{L_1(1/6)} \left[\begin{array}{ccc|c} 1 & 1/3 & 2/3 & 0 \\ -9 & -3 & -6 & 0 \end{array}\right] \xrightarrow{L_2' = L_2 + L_1(9)} \left[\begin{array}{ccc|c} 1 & 1/3 & 2/3 & 0 \\ 0 & 0 & 0 & 0 \end{array}\right] = B$$
$C_A = 1$, $C_V = 1$, $C = 1 < n = 3 \Rightarrow g = 3 - 1 = 2$, **`SPI`**.
Equação reduzida: $x = -\frac{1}{3}y - \frac{2}{3}z = \frac{-y - 2z}{3}$. Para $y = 3, z = 0$: $x = -1 \Rightarrow (-1, 3, 0)$.
- **Resposta final:** `ca: 1; cv: 1; g: 2; classificacao: SPI; solucao: (-1, 3, 0)`.

### `C06-E03` *(Lista 5 Ex. 8)*
Multiplicando todas as linhas pelas constantes convenientes ($L_1(1/3)$ e anulando $L_2, L_3, L_4$ via combinações de $L_1$):
$$B = \left[\begin{array}{cc|c} 1 & 2 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array}\right]$$
$C_A = 1$, $C_V = 1$, $C = 1 < n = 2 \Rightarrow g = 2 - 1 = 1$, **`SPI`**.
Solução geral: $x = -2y$ ($y \in \mathbb{R}$ arbitrário). Para $y = 1$: `(-2, 1)` *(qualquer múltiplo não nulo $t(-2, 1)$ com $t \neq 0$ é uma solução própria válida)*.
- **Resposta final:** `ca: 1; cv: 1; g: 1; classificacao: SPI; solucao: (-2, 1)`.

### `C06-E04` *(Lista 5 Ex. 19)*
Escalonando a matriz dos coeficientes:
$$\left[\begin{array}{ccc|c} 1 & -1 & -1 & 0 \\ 1 & -2 & -2 & 0 \\ 2 & k & 1 & 0 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-1) \\ L_3' = L_3 + L_1(-2)}} \left[\begin{array}{ccc|c} 1 & -1 & -1 & 0 \\ 0 & -1 & -1 & 0 \\ 0 & k+2 & 3 & 0 \end{array}\right] \xrightarrow{L_2(-1)} \left[\begin{array}{ccc|c} 1 & -1 & -1 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & k+2 & 3 & 0 \end{array}\right]$$
$$\xrightarrow{L_3' = L_3 + L_2(-(k+2))} \left[\begin{array}{ccc|c} 1 & -1 & -1 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 3 - (k+2) & 0 \end{array}\right] = \left[\begin{array}{ccc|c} 1 & -1 & -1 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 1 - k & 0 \end{array}\right]$$
Para admitir solução não-trivial ($C < 3$), o último pivô deve se anular: $1 - k = 0 \Rightarrow \mathbf{k = 1}$.  
*(Conferência alternativa via $\det(A) = 0$ pela 1ª linha: $1(-2 + 2k) - (-1)(1 + 4) - 1(k + 4) = 2k - 2 + 5 - k - 4 = k - 1 = 0 \Rightarrow k = 1$.)*
- **Resposta final:** `k = 1`.

### `C06-E05` *(Caça ao Bug)*
Pelo desenvolvimento de $\det(A)$ pela 1ª linha (sem Sarrus):
$$\det\begin{bmatrix} 1 & 0 & 2 \\ 0 & k & 2 \\ 0 & 2 & k \end{bmatrix} = 1\cdot(k^2 - 4) = 0 \Rightarrow k^2 = 4 \Rightarrow \mathbf{k = -2\text{ ou }k = 2}.$$
*(Conferência por escalonamento: se $k = 0$, as duas últimas equações ficam $2z = 0$ e $2y = 0$, dando $C = 3$ e apenas solução trivial. Se $k \neq 0$, aplicando $L_3' = L_3 + L_2(-2/k)$ resulta no pivô $k - 4/k = (k^2 - 4)/k$, que zera para $k = 2$ e $k = -2$.)*
- **Resposta final:** `k = -2 ou k = 2`.

---

## 2. Gabarito da Checagem Independente (`C06-C01` a `C06-C03`)

### `C06-C01` *(Lista 5 Ex. 6)*
$$A = \left[\begin{array}{ccc|c} 1 & 0 & -1 & 0 \\ 3 & 1 & 2 & 0 \\ 4 & 2 & 2 & 0 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-3) \\ L_3' = L_3 + L_1(-4)}} \left[\begin{array}{ccc|c} 1 & 0 & -1 & 0 \\ 0 & 1 & 5 & 0 \\ 0 & 2 & 6 & 0 \end{array}\right] \xrightarrow{L_3' = L_3 + L_2(-2)} \left[\begin{array}{ccc|c} 1 & 0 & -1 & 0 \\ 0 & 1 & 5 & 0 \\ 0 & 0 & -4 & 0 \end{array}\right] \sim \left[\begin{array}{ccc|c} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{array}\right]$$
$C_A = 3, C_V = 3, g = 0$, **`SPD`**, apenas a solução trivial `(0, 0, 0)`.
- **Resposta final:** `ca: 3; cv: 3; g: 0; classificacao: SPD; solucao: (0, 0, 0)`.

### `C06-C02`
$$A = \left[\begin{array}{ccc|c} 1 & -2 & 1 & 0 \\ 2 & -1 & 5 & 0 \\ 3 & -3 & 6 & 0 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(-3)}} \left[\begin{array}{ccc|c} 1 & -2 & 1 & 0 \\ 0 & 3 & 3 & 0 \\ 0 & 3 & 3 & 0 \end{array}\right] \xrightarrow{\substack{L_2(1/3) \\ L_1' = L_1 + L_2(2) \\ L_3' = L_3 + L_2(-3)}} \left[\begin{array}{ccc|c} 1 & 0 & 3 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{array}\right] = B$$
$C_A = 2, C_V = 2, C = 2 < n = 3 \Rightarrow g = 1$, **`SPI`**.
Logo $x = -3z$ e $y = -z$. Para $z = 1$: `(-3, -1, 1)` *(aceita-se qualquer múltiplo não nulo)*.
- **Resposta final:** `ca: 2; cv: 2; g: 1; classificacao: SPI; solucao: (-3, -1, 1)`.

### `C06-C03`
$$\left[\begin{array}{ccc|c} 1 & 2 & -1 & 0 \\ 2 & 1 & 1 & 0 \\ 3 & k & 0 & 0 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(-3)}} \left[\begin{array}{ccc|c} 1 & 2 & -1 & 0 \\ 0 & -3 & 3 & 0 \\ 0 & k-6 & 3 & 0 \end{array}\right] \xrightarrow{L_2(-1/3)} \left[\begin{array}{ccc|c} 1 & 2 & -1 & 0 \\ 0 & 1 & -1 & 0 \\ 0 & k-6 & 3 & 0 \end{array}\right]$$
$$\xrightarrow{L_3' = L_3 + L_2(-(k-6))} \left[\begin{array}{ccc|c} 1 & 2 & -1 & 0 \\ 0 & 1 & -1 & 0 \\ 0 & 0 & 3 + k - 6 & 0 \end{array}\right] = \left[\begin{array}{ccc|c} 1 & 2 & -1 & 0 \\ 0 & 1 & -1 & 0 \\ 0 & 0 & k - 3 & 0 \end{array}\right]$$
Anula o último pivô quando $k - 3 = 0 \Rightarrow \mathbf{k = 3}$.
- **Resposta final:** `k = 3`.
