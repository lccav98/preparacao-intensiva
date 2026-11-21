# Gabarito Comentado — Bloco `C05` (Forma de Escada, Posto `C_A, C_V, C` e Sistemas `m × n`)

> **Bloco de referência:** [C05_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_C/blocos/C05_bloco.md)

---

## 1. Gabarito dos Exercícios (`C05-E01` a `C05-E05`)

### `C05-E01` *(Lista 5 Ex. 1)*
$$A = \left[\begin{array}{cc|c} 2 & -3 & 4 \\ 6 & -9 & 15 \end{array}\right] \xrightarrow{L_1(1/2)} \left[\begin{array}{cc|c} 1 & -3/2 & 2 \\ 6 & -9 & 15 \end{array}\right] \xrightarrow{L_2' = L_2 + L_1(-6)} \left[\begin{array}{cc|c} 1 & -3/2 & 2 \\ 0 & 0 & 3 \end{array}\right] = B$$
Submatriz $V = \begin{bmatrix} 1 & -3/2 \\ 0 & 0 \end{bmatrix}$. Logo $C_A = 2$, $C_V = 1$. Como $C_A > C_V$, o sistema é **incompatível (`SI`)**.
- **Resposta final:** `ca: 2; cv: 1; classificacao: SI`.

### `C05-E02` *(Lista 5 Ex. 10)*
$$A = \left[\begin{array}{cc|c} 1 & 2 & -4 \\ -3 & 4 & -18 \\ 2 & -1 & 7 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(3) \\ L_3' = L_3 + L_1(-2)}} \left[\begin{array}{cc|c} 1 & 2 & -4 \\ 0 & 10 & -30 \\ 0 & -5 & 15 \end{array}\right] \xrightarrow{\substack{L_2(1/10) \\ L_1' = L_1 + L_2(-2) \\ L_3' = L_3 + L_2(5)}} \left[\begin{array}{cc|c} 1 & 0 & 2 \\ 0 & 1 & -3 \\ 0 & 0 & 0 \end{array}\right] = B$$
$V = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{bmatrix}$. Temos $C_A = 2$, $C_V = 2 \Rightarrow C = 2$. Como $n = 2 = C$, $g = 2 - 2 = 0$, **Compatível e Determinado (`SPD`)**, solução `(2, -3)`.
- **Resposta final:** `ca: 2; cv: 2; g: 0; classificacao: SPD; solucao: (2, -3)`.

### `C05-E03` *(Lista 5 Ex. 11)*
$$A = \left[\begin{array}{cc|c} 1 & 2 & 4 \\ -3 & 4 & 3 \\ 2 & -1 & -6 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(3) \\ L_3' = L_3 + L_1(-2)}} \left[\begin{array}{cc|c} 1 & 2 & 4 \\ 0 & 10 & 15 \\ 0 & -5 & -14 \end{array}\right] \xrightarrow{L_2(1/10)} \left[\begin{array}{cc|c} 1 & 2 & 4 \\ 0 & 1 & 3/2 \\ 0 & -5 & -14 \end{array}\right] \xrightarrow{\substack{L_1' = L_1 + L_2(-2) \\ L_3' = L_3 + L_2(5)}} \left[\begin{array}{cc|c} 1 & 0 & 1 \\ 0 & 1 & 3/2 \\ 0 & 0 & -13/2 \end{array}\right] = B$$
$C_A = 3$, $C_V = 2$. Como $C_A > C_V$, é **incompatível (`SI`)**.
- **Resposta final:** `ca: 3; cv: 2; classificacao: SI`.

### `C05-E04` *(Lista 5 Ex. 9)*
$$A = \left[\begin{array}{ccc|c} 1 & -1 & 0 & 0 \\ 0 & 2 & 4 & 6 \\ 1 & 1 & 4 & 6 \end{array}\right] \xrightarrow{L_3' = L_3 + L_1(-1)} \left[\begin{array}{ccc|c} 1 & -1 & 0 & 0 \\ 0 & 2 & 4 & 6 \\ 0 & 2 & 4 & 6 \end{array}\right] \xrightarrow{\substack{L_2(1/2) \\ L_1' = L_1 + L_2(1) \\ L_3' = L_3 + L_2(-2)}} \left[\begin{array}{ccc|c} 1 & 0 & 2 & 3 \\ 0 & 1 & 2 & 3 \\ 0 & 0 & 0 & 0 \end{array}\right] = B$$
$C_A = 2$, $C_V = 2 \Rightarrow C = 2$. Com $n = 3$, $g = 3 - 2 = 1$, **`SPI`**.
Solução geral: $x = 3 - 2z$, $y = 3 - 2z$. Para $z = 1$: $(1, 1, 1)$.
- **Resposta final:** `ca: 2; cv: 2; g: 1; classificacao: SPI; solucao: (1, 1, 1)`.

### `C05-E05`
$$A = \left[\begin{array}{cccc|c} 1 & -2 & 3 & -1 & 5 \\ 2 & -3 & 7 & 1 & 13 \end{array}\right] \xrightarrow{L_2' = L_2 + L_1(-2)} \left[\begin{array}{cccc|c} 1 & -2 & 3 & -1 & 5 \\ 0 & 1 & 1 & 3 & 3 \end{array}\right] \xrightarrow{L_1' = L_1 + L_2(2)} \left[\begin{array}{cccc|c} 1 & 0 & 5 & 5 & 11 \\ 0 & 1 & 1 & 3 & 3 \end{array}\right] = B$$
$C_A = C_V = C = 2$; $n = 4 \Rightarrow g = 4 - 2 = 2$, **`SPI`**.
$x = 11 - 5z - 5w$, $y = 3 - z - 3w$. Para $z = 1, w = 0$: $(6, 2, 1, 0)$.
- **Resposta final:** `ca: 2; cv: 2; g: 2; classificacao: SPI; solucao: (6, 2, 1, 0)`.

---

## 2. Gabarito da Checagem Independente (`C05-C01` a `C05-C03`)

### `C05-C01` *(Apostila p. 37–39)*
$$A = \left[\begin{array}{cc|c} 2 & 4 & 16 \\ 5 & -2 & 4 \\ 3 & 1 & 9 \\ 4 & -5 & -7 \end{array}\right] \xrightarrow{L_1(1/2)} \left[\begin{array}{cc|c} 1 & 2 & 8 \\ 5 & -2 & 4 \\ 3 & 1 & 9 \\ 4 & -5 & -7 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-5) \\ L_3' = L_3 + L_1(-3) \\ L_4' = L_4 + L_1(-4)}} \left[\begin{array}{cc|c} 1 & 2 & 8 \\ 0 & -12 & -36 \\ 0 & -5 & -15 \\ 0 & -13 & -39 \end{array}\right]$$
$$\xrightarrow{\substack{L_2(-1/12) \\ L_1' = L_1 + L_2(-2) \\ L_3' = L_3 + L_2(5),\; L_4' = L_4 + L_2(13)}} \left[\begin{array}{cc|c} 1 & 0 & 2 \\ 0 & 1 & 3 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array}\right] = B$$
$C_A = 2, C_V = 2, C = 2 = n \Rightarrow g = 0$, **`SPD`**, solução `(2, 3)`.
- **Resposta final:** `ca: 2; cv: 2; g: 0; classificacao: SPD; solucao: (2, 3)`.

### `C05-C02`
$$A = \left[\begin{array}{cccc|c} 1 & -1 & 2 & 1 & 3 \\ 2 & -2 & 5 & 4 & 8 \\ 3 & -3 & 6 & 3 & 9 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(-3)}} \left[\begin{array}{cccc|c} 1 & -1 & 2 & 1 & 3 \\ 0 & 0 & 1 & 2 & 2 \\ 0 & 0 & 0 & 0 & 0 \end{array}\right] \xrightarrow{L_1' = L_1 + L_2(-2)} \left[\begin{array}{cccc|c} 1 & -1 & 0 & -3 & -1 \\ 0 & 0 & 1 & 2 & 2 \\ 0 & 0 & 0 & 0 & 0 \end{array}\right] = B$$
$C_A = C_V = C = 2 < n = 4 \Rightarrow g = 2$, **`SPI`**.
$x = -1 + y + 3w$, $z = 2 - 2w$. Para $y = 0, w = 1$: $x = 2, z = 0 \Rightarrow (2, 0, 0, 1)$.
- **Resposta final:** `ca: 2; cv: 2; g: 2; classificacao: SPI; solucao: (2, 0, 0, 1)`.

### `C05-C03`
$$A = \left[\begin{array}{cc|c} 2 & 1 & 4 \\ 4 & -2 & 2 \\ 6 & 1 & 9 \end{array}\right] \xrightarrow{L_1(1/2)} \left[\begin{array}{cc|c} 1 & 1/2 & 2 \\ 4 & -2 & 2 \\ 6 & 1 & 9 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-4) \\ L_3' = L_3 + L_1(-6)}} \left[\begin{array}{cc|c} 1 & 1/2 & 2 \\ 0 & -4 & -6 \\ 0 & -2 & -3 \end{array}\right]$$
$$\xrightarrow{\substack{L_2(-1/4) \\ L_1' = L_1 + L_2(-1/2) \\ L_3' = L_3 + L_2(2)}} \left[\begin{array}{cc|c} 1 & 0 & 5/4 \\ 0 & 1 & 3/2 \\ 0 & 0 & 0 \end{array}\right] = B$$
$C_A = 2, C_V = 2, C = 2 = n \Rightarrow g = 0$, **`SPD`**, solução `(5/4, 3/2)`.
- **Resposta final:** `ca: 2; cv: 2; g: 0; classificacao: SPD; solucao: (5/4, 3/2)`.
