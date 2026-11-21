# Gabarito Comentado — Bloco `B07` (Inversão pelo Método de Gauss-Jordan)

> **Bloco de referência:** [B07_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_B/blocos/B07_bloco.md)  
> **Método obrigatório:** Gauss-Jordan `[A | I] -> [I | A^{-1}]` (sem matriz adjunta).

---

## 1. Gabarito dos Exercícios (`B07-E01` a `B07-E05`)

### `B07-E01`
1. $\left[\begin{array}{cc|cc} 4 & -2 & 1 & 0 \\ 1 & 3 & 0 & 1 \end{array}\right] \xrightarrow{L_{12}} \left[\begin{array}{cc|cc} 1 & 3 & 0 & 1 \\ 4 & -2 & 1 & 0 \end{array}\right] \xrightarrow{L_2' = L_2 - 4L_1} \left[\begin{array}{cc|cc} 1 & 3 & 0 & 1 \\ 0 & -14 & 1 & -4 \end{array}\right]$
2. $\xrightarrow{L_2(-1/14)} \left[\begin{array}{cc|cc} 1 & 3 & 0 & 1 \\ 0 & 1 & -1/14 & 2/7 \end{array}\right] \xrightarrow{L_1' = L_1 - 3L_2} \left[\begin{array}{cc|cc} 1 & 0 & 3/14 & 1/7 \\ 0 & 1 & -1/14 & 2/7 \end{array}\right]$

Logo: $A^{-1} = \begin{bmatrix} 3/14 & 1/7 \\ -1/14 & 2/7 \end{bmatrix}$.

### `B07-E02`
1. $\left[\begin{array}{ccc|ccc} 1 & 2 & 1 & 1 & 0 & 0 \\ 0 & 1 & 2 & 0 & 1 & 0 \\ 2 & 5 & 3 & 0 & 0 & 1 \end{array}\right] \xrightarrow{L_3' = L_3 - 2L_1} \left[\begin{array}{ccc|ccc} 1 & 2 & 1 & 1 & 0 & 0 \\ 0 & 1 & 2 & 0 & 1 & 0 \\ 0 & 1 & 1 & -2 & 0 & 1 \end{array}\right]$
2. $\xrightarrow{L_1' = L_1 - 2L_2,\; L_3' = L_3 - L_2} \left[\begin{array}{ccc|ccc} 1 & 0 & -3 & 1 & -2 & 0 \\ 0 & 1 & 2 & 0 & 1 & 0 \\ 0 & 0 & -1 & -2 & -1 & 1 \end{array}\right] \xrightarrow{L_3(-1)} \left[\begin{array}{ccc|ccc} 1 & 0 & -3 & 1 & -2 & 0 \\ 0 & 1 & 2 & 0 & 1 & 0 \\ 0 & 0 & 1 & 2 & 1 & -1 \end{array}\right]$
3. $\xrightarrow{L_1' = L_1 + 3L_3,\; L_2' = L_2 - 2L_3} \left[\begin{array}{ccc|ccc} 1 & 0 & 0 & 7 & 1 & -3 \\ 0 & 1 & 0 & -4 & -1 & 2 \\ 0 & 0 & 1 & 2 & 1 & -1 \end{array}\right]$

Logo: $B^{-1} = \begin{bmatrix} 7 & 1 & -3 \\ -4 & -1 & 2 \\ 2 & 1 & -1 \end{bmatrix}$.

### `B07-E03`
1. $\left[\begin{array}{ccc|ccc} 1 & 2 & -1 & 1 & 0 & 0 \\ 2 & 5 & 0 & 0 & 1 & 0 \\ 0 & -1 & 3 & 0 & 0 & 1 \end{array}\right] \xrightarrow{L_2' = L_2 - 2L_1} \left[\begin{array}{ccc|ccc} 1 & 2 & -1 & 1 & 0 & 0 \\ 0 & 1 & 2 & -2 & 1 & 0 \\ 0 & -1 & 3 & 0 & 0 & 1 \end{array}\right]$
2. $\xrightarrow{L_1' = L_1 - 2L_2,\; L_3' = L_3 + L_2} \left[\begin{array}{ccc|ccc} 1 & 0 & -5 & 5 & -2 & 0 \\ 0 & 1 & 2 & -2 & 1 & 0 \\ 0 & 0 & 5 & -2 & 1 & 1 \end{array}\right] \xrightarrow{L_3(1/5)} \left[\begin{array}{ccc|ccc} 1 & 0 & -5 & 5 & -2 & 0 \\ 0 & 1 & 2 & -2 & 1 & 0 \\ 0 & 0 & 1 & -2/5 & 1/5 & 1/5 \end{array}\right]$
3. $\xrightarrow{L_1' = L_1 + 5L_3,\; L_2' = L_2 - 2L_3} \left[\begin{array}{ccc|ccc} 1 & 0 & 0 & 3 & -1 & 1 \\ 0 & 1 & 0 & -6/5 & 3/5 & -2/5 \\ 0 & 0 & 1 & -2/5 & 1/5 & 1/5 \end{array}\right]$

Logo: $C^{-1} = \begin{bmatrix} 3 & -1 & 1 \\ -6/5 & 3/5 & -2/5 \\ -2/5 & 1/5 & 1/5 \end{bmatrix}$.

### `B07-E04`
Aplicando $L_2' = L_2 - 2L_1$ na matriz ampliada $[D \mid I_3]$:
$$\left[\begin{array}{ccc|ccc} 1 & -2 & 3 & 1 & 0 & 0 \\ 2 & -4 & 6 & 0 & 1 & 0 \\ -1 & 3 & 1 & 0 & 0 & 1 \end{array}\right] \xrightarrow{L_2' = L_2 - 2L_1} \left[\begin{array}{ccc|ccc} 1 & -2 & 3 & 1 & 0 & 0 \\ 0 & 0 & 0 & -2 & 1 & 0 \\ -1 & 3 & 1 & 0 & 0 & 1 \end{array}\right]$$
Surgiu uma linha toda nula no bloco esquerdo (`L_2`), logo $D$ é **`singular`** (não possui inversa).

### `B07-E05`
1. $L_3' = L_3 - L_1$ e $L_2 \leftrightarrow L_4$:
   $$\left[\begin{array}{cccc|cccc} 1 & 0 & 2 & 0 & 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 1 & 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 & -1 & 0 & 1 & 0 \\ 0 & 2 & 0 & 1 & 0 & 1 & 0 & 0 \end{array}\right]$$
2. $L_4' = L_4 - 2L_2$ gera $[0, 0, 0, -1 \mid 0, 1, 0, -2] \xrightarrow{L_4(-1)} [0, 0, 0, 1 \mid 0, -1, 0, 2]$.
3. $L_1' = L_1 - 2L_3$ e $L_2' = L_2 - L_4$:
   $$E^{-1} = \begin{bmatrix} 3 & 0 & -2 & 0 \\ 0 & 1 & 0 & -1 \\ -1 & 0 & 1 & 0 \\ 0 & -1 & 0 & 2 \end{bmatrix}$$

---

## 2. Gabarito da Checagem Independente (`B07-C01` a `B07-C03`)

### `B07-C01`
$\left[\begin{array}{cc|cc} 3 & 2 & 1 & 0 \\ -1 & 4 & 0 & 1 \end{array}\right] \xrightarrow{L_{12},\, L_1(-1)} \left[\begin{array}{cc|cc} 1 & -4 & 0 & -1 \\ 3 & 2 & 1 & 0 \end{array}\right] \xrightarrow{L_2' = L_2 - 3L_1} \left[\begin{array}{cc|cc} 1 & -4 & 0 & -1 \\ 0 & 14 & 1 & 3 \end{array}\right] \xrightarrow{L_2(1/14),\, L_1'=L_1+4L_2}$
$$M^{-1} = \begin{bmatrix} 2/7 & -1/7 \\ 1/14 & 3/14 \end{bmatrix}$$

### `B07-C02`
1. $L_{12}$: $\left[\begin{array}{ccc|ccc} 1 & 2 & 3 & 0 & 1 & 0 \\ 0 & 1 & 2 & 1 & 0 & 0 \\ 2 & 1 & 1 & 0 & 0 & 1 \end{array}\right] \xrightarrow{L_3' = L_3 - 2L_1} \left[\begin{array}{ccc|ccc} 1 & 2 & 3 & 0 & 1 & 0 \\ 0 & 1 & 2 & 1 & 0 & 0 \\ 0 & -3 & -5 & 0 & -2 & 1 \end{array}\right]$
2. $L_1' = L_1 - 2L_2$, $L_3' = L_3 + 3L_2$: $\left[\begin{array}{ccc|ccc} 1 & 0 & -1 & -2 & 1 & 0 \\ 0 & 1 & 2 & 1 & 0 & 0 \\ 0 & 0 & 1 & 3 & -2 & 1 \end{array}\right]$
3. $L_1' = L_1 + L_3$, $L_2' = L_2 - 2L_3$:
   $$N^{-1} = \begin{bmatrix} 1 & -1 & 1 \\ -5 & 4 & -2 \\ 3 & -2 & 1 \end{bmatrix}$$

### `B07-C03`
Escalonando independentemente os dois blocos $2\times 2$ na diagonal:
- Bloco superior ($L_2' = L_2 - L_1$, depois $L_1' = L_1 - 2L_2'$): $\begin{bmatrix} 3 & -2 \\ -1 & 1 \end{bmatrix}$.
- Bloco inferior ($L_3 \leftrightarrow L_4$, depois $L_4' = L_4 - 2L_3$ e $L_4(-1)$, $L_3' = L_3 - L_4'$): $\begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix}$.
$$P^{-1} = \begin{bmatrix} 3 & -2 & 0 & 0 \\ -1 & 1 & 0 & 0 \\ 0 & 0 & 1 & -1 \\ 0 & 0 & -1 & 2 \end{bmatrix}$$
*(Critério de aceitação: 3/3 acertos exatos sem consulta e sem uso de matriz adjunta.)*
