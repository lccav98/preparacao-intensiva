# Gabarito Comentado — Bloco `C02` (Eliminação de Gauss e Substituição Regressiva)

> **Bloco de referência:** [C02_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_C/blocos/C02_bloco.md)  
> **Nota para Caça ao Bug (`C02-E03`):** O erro intencional está no sinal durante a substituição regressiva (`-6z` trocado para `+6z`).

---

## 1. Gabarito dos Exercícios (`C02-E01` a `C02-E05`)

### `C02-E01`
$$A = \left[\begin{array}{ccc|c} 2 & 4 & -6 & 4 \\ 4 & 2 & 2 & 10 \\ 2 & 8 & -4 & 14 \end{array}\right] \xrightarrow{L_{23},\; L_1(1/2)} \left[\begin{array}{ccc|c} 1 & 2 & -3 & 2 \\ 2 & 8 & -4 & 14 \\ 4 & 2 & 2 & 10 \end{array}\right]$$
$$\xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(-4)}} \left[\begin{array}{ccc|c} 1 & 2 & -3 & 2 \\ 0 & 4 & 2 & 10 \\ 0 & -6 & 14 & 2 \end{array}\right] \xrightarrow{L_3' = L_3 + L_2(3/2)} \left[\begin{array}{ccc|c} 1 & 2 & -3 & 2 \\ 0 & 4 & 2 & 10 \\ 0 & 0 & 17 & 17 \end{array}\right]$$
Substituição regressiva: $17z = 17 \Rightarrow z = 1$; $4y + 2(1) = 10 \Rightarrow y = 2$; $x + 2(2) - 3(1) = 2 \Rightarrow x = 1$.
- **Resposta final:** `(1, 2, 1)`.

### `C02-E02`
$$A = \left[\begin{array}{ccc|c} 2 & -1 & 3 & 9 \\ 1 & 2 & -1 & 0 \\ 3 & 1 & 1 & 9 \end{array}\right] \xrightarrow{L_{12}} \left[\begin{array}{ccc|c} 1 & 2 & -1 & 0 \\ 2 & -1 & 3 & 9 \\ 3 & 1 & 1 & 9 \end{array}\right]$$
$$\xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(-3)}} \left[\begin{array}{ccc|c} 1 & 2 & -1 & 0 \\ 0 & -5 & 5 & 9 \\ 0 & -5 & 4 & 9 \end{array}\right] \xrightarrow{L_3' = L_3 + L_2(-1)} \left[\begin{array}{ccc|c} 1 & 2 & -1 & 0 \\ 0 & -5 & 5 & 9 \\ 0 & 0 & -1 & 0 \end{array}\right]$$
Substituição regressiva: $-z = 0 \Rightarrow z = 0$; $-5y + 5(0) = 9 \Rightarrow y = -9/5$; $x + 2(-9/5) - 0 = 0 \Rightarrow x = 18/5$.
- **Resposta final:** `(18/5, -9/5, 0)`.

### `C02-E03` *(Caça ao Bug)*
- **Diagnóstico da falha:** O sinal de $-6z$ foi invertido para $+6z$ ao substituir $z = 2$.
- **Substituição regressiva correta:**
  - $4z = 8 \Rightarrow z = 2$
  - $3y - 6(2) = -9 \Rightarrow 3y - 12 = -9 \Rightarrow 3y = 3 \Rightarrow y = 1$
  - $x - 2(1) + 2 = 3 \Rightarrow x = 3$
- **Resposta final:** `(3, 1, 2)`.

### `C02-E04`
$$A = \left[\begin{array}{ccc|c} 0 & 2 & 3 & 7 \\ 3 & -6 & 3 & 3 \\ 2 & 4 & -1 & 5 \end{array}\right] \xrightarrow{L_{12},\; L_1(1/3)} \left[\begin{array}{ccc|c} 1 & -2 & 1 & 1 \\ 0 & 2 & 3 & 7 \\ 2 & 4 & -1 & 5 \end{array}\right]$$
$$\xrightarrow{L_3' = L_3 + L_1(-2)} \left[\begin{array}{ccc|c} 1 & -2 & 1 & 1 \\ 0 & 2 & 3 & 7 \\ 0 & 8 & -3 & 3 \end{array}\right] \xrightarrow{L_3' = L_3 + L_2(-4)} \left[\begin{array}{ccc|c} 1 & -2 & 1 & 1 \\ 0 & 2 & 3 & 7 \\ 0 & 0 & -15 & -25 \end{array}\right]$$
Substituição regressiva:
- $z = \frac{-25}{-15} = \frac{5}{3}$
- $2y + 3\left(\frac{5}{3}\right) = 7 \Rightarrow 2y + 5 = 7 \Rightarrow y = 1$
- $x - 2(1) + \frac{5}{3} = 1 \Rightarrow x = 3 - \frac{5}{3} = \frac{4}{3}$
- **Resposta final:** `(4/3, 1, 5/3)`.

### `C02-E05`
$$A = \left[\begin{array}{cccc|c} 1 & 1 & 1 & 1 & 3 \\ 2 & -1 & 1 & 2 & 1 \\ 1 & 2 & -2 & 1 & 8 \\ 3 & 1 & 2 & -1 & 2 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(-1) \\ L_4' = L_4 + L_1(-3)}} \left[\begin{array}{cccc|c} 1 & 1 & 1 & 1 & 3 \\ 0 & -3 & -1 & 0 & -5 \\ 0 & 1 & -3 & 0 & 5 \\ 0 & -2 & -1 & -4 & -7 \end{array}\right]$$
$$\xrightarrow{L_{23}} \left[\begin{array}{cccc|c} 1 & 1 & 1 & 1 & 3 \\ 0 & 1 & -3 & 0 & 5 \\ 0 & -3 & -1 & 0 & -5 \\ 0 & -2 & -1 & -4 & -7 \end{array}\right] \xrightarrow{\substack{L_3' = L_3 + L_2(3) \\ L_4' = L_4 + L_2(2)}} \left[\begin{array}{cccc|c} 1 & 1 & 1 & 1 & 3 \\ 0 & 1 & -3 & 0 & 5 \\ 0 & 0 & -10 & 0 & 10 \\ 0 & 0 & -7 & -4 & 3 \end{array}\right]$$
$$\xrightarrow{L_4' = L_4 + L_3(-7/10)} \left[\begin{array}{cccc|c} 1 & 1 & 1 & 1 & 3 \\ 0 & 1 & -3 & 0 & 5 \\ 0 & 0 & -10 & 0 & 10 \\ 0 & 0 & 0 & -4 & -4 \end{array}\right]$$
Substituição regressiva: $w = 1$; $z = -1$; $y - 3(-1) = 5 \Rightarrow y = 2$; $x + 2 - 1 + 1 = 3 \Rightarrow x = 1$.
- **Resposta final:** `(1, 2, -1, 1)`.

---

## 2. Gabarito da Checagem Independente (`C02-C01` a `C02-C03`)

### `C02-C01`
$$A = \left[\begin{array}{ccc|c} 0 & 3 & -1 & 5 \\ 2 & -1 & 4 & 7 \\ 1 & 2 & -3 & -4 \end{array}\right] \xrightarrow{L_{13}} \left[\begin{array}{ccc|c} 1 & 2 & -3 & -4 \\ 2 & -1 & 4 & 7 \\ 0 & 3 & -1 & 5 \end{array}\right] \xrightarrow{L_2' = L_2 + L_1(-2)} \left[\begin{array}{ccc|c} 1 & 2 & -3 & -4 \\ 0 & -5 & 10 & 15 \\ 0 & 3 & -1 & 5 \end{array}\right]$$
$$\xrightarrow{L_2(-1/5)} \left[\begin{array}{ccc|c} 1 & 2 & -3 & -4 \\ 0 & 1 & -2 & -3 \\ 0 & 3 & -1 & 5 \end{array}\right] \xrightarrow{L_3' = L_3 + L_2(-3)} \left[\begin{array}{ccc|c} 1 & 2 & -3 & -4 \\ 0 & 1 & -2 & -3 \\ 0 & 0 & 5 & 14 \end{array}\right]$$
Substituição regressiva: $z = 14/5$; $y = -3 + 2(14/5) = 13/5$; $x = -4 - 2(13/5) + 3(14/5) = -4/5$.
- **Resposta final:** `(-4/5, 13/5, 14/5)`.

### `C02-C02`
$$A = \left[\begin{array}{ccc|c} 2 & 3 & -1 & 2 \\ 4 & -1 & 2 & 3 \\ 1 & 2 & 1 & 3 \end{array}\right] \xrightarrow{L_{13}} \left[\begin{array}{ccc|c} 1 & 2 & 1 & 3 \\ 4 & -1 & 2 & 3 \\ 2 & 3 & -1 & 2 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-4) \\ L_3' = L_3 + L_1(-2)}} \left[\begin{array}{ccc|c} 1 & 2 & 1 & 3 \\ 0 & -9 & -2 & -9 \\ 0 & -1 & -3 & -4 \end{array}\right]$$
$$\xrightarrow{L_{23},\; L_2(-1)} \left[\begin{array}{ccc|c} 1 & 2 & 1 & 3 \\ 0 & 1 & 3 & 4 \\ 0 & -9 & -2 & -9 \end{array}\right] \xrightarrow{L_3' = L_3 + L_2(9)} \left[\begin{array}{ccc|c} 1 & 2 & 1 & 3 \\ 0 & 1 & 3 & 4 \\ 0 & 0 & 25 & 27 \end{array}\right]$$
Substituição regressiva: $z = 27/25$; $y = 4 - 3(27/25) = 19/25$; $x = 3 - 2(19/25) - 27/25 = 10/25 = 2/5$.
- **Resposta final:** `(2/5, 19/25, 27/25)`.

### `C02-C03`
$$A = \left[\begin{array}{ccc|c} 1 & -2 & 3 & 11 \\ 2 & 1 & -1 & 1 \\ 3 & -1 & 1 & 8 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(-3)}} \left[\begin{array}{ccc|c} 1 & -2 & 3 & 11 \\ 0 & 5 & -7 & -21 \\ 0 & 5 & -8 & -25 \end{array}\right] \xrightarrow{L_3' = L_3 + L_2(-1)} \left[\begin{array}{ccc|c} 1 & -2 & 3 & 11 \\ 0 & 5 & -7 & -21 \\ 0 & 0 & -1 & -4 \end{array}\right]$$
Substituição regressiva: $z = 4$; $5y - 7(4) = -21 \Rightarrow 5y = 7 \Rightarrow y = 7/5$; $x - 2(7/5) + 3(4) = 11 \Rightarrow x = 14/5 - 1 = 9/5$.
- **Resposta final:** `(9/5, 7/5, 4)`.
