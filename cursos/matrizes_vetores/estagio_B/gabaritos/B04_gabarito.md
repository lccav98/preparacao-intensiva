# Gabarito Comentado — Bloco `B04` (Determinantes por Triangulação e Redução a `I`)

> **Bloco de referência:** [B04_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_B/blocos/B04_bloco.md)

---

## 1. Gabarito dos Exercícios (`B04-E01` a `B04-E05`)

### `B04-E01`
1. $L_2' = L_2 - 2L_1$ e $L_3' = L_3 + L_1$:
   $$\begin{vmatrix} 1 & 2 & -1 \\ 0 & 1 & 3 \\ 0 & 2 & 3 \end{vmatrix}$$
2. $L_3' = L_3 - 2L_2$:
   $$\begin{vmatrix} 1 & 2 & -1 \\ 0 & 1 & 3 \\ 0 & 0 & -3 \end{vmatrix} = 1\cdot 1\cdot(-3) = \mathbf{-3}$$

### `B04-E02`
1. Fatoramos $2$ da 2ª linha ($L_2 \to \frac{1}{2}L_2$):
   $$\det(B) = 2\begin{vmatrix} 0 & 2 & -1 \\ 1 & -2 & 3 \\ 1 & 3 & -2 \end{vmatrix}$$
2. Trocamos $L_1 \leftrightarrow L_2$ (multiplica por $-1$):
   $$\det(B) = -2\begin{vmatrix} 1 & -2 & 3 \\ 0 & 2 & -1 \\ 1 & 3 & -2 \end{vmatrix}$$
3. $L_3' = L_3 - L_1$:
   $$\det(B) = -2\begin{vmatrix} 1 & -2 & 3 \\ 0 & 2 & -1 \\ 0 & 5 & -5 \end{vmatrix}$$
4. $L_3' = L_3 - \frac{5}{2}L_2$:
   $$\det(B) = -2\begin{vmatrix} 1 & -2 & 3 \\ 0 & 2 & -1 \\ 0 & 0 & -5/2 \end{vmatrix} = -2\cdot\left(1\cdot 2\cdot\left(-\frac{5}{2}\right)\right) = -2\cdot(-5) = \mathbf{10}$$

### `B04-E03`
1. Fatoramos $2$ da 1ª linha:
   $$\det(C) = 2\begin{vmatrix} 1 & 2 & -1 & 3 \\ 1 & 3 & 0 & 2 \\ -1 & 2 & 3 & 1 \\ 0 & 1 & -2 & 4 \end{vmatrix}$$
2. $L_2' = L_2 - L_1$, $L_3' = L_3 + L_1$:
   $$\det(C) = 2\begin{vmatrix} 1 & 2 & -1 & 3 \\ 0 & 1 & 1 & -1 \\ 0 & 4 & 2 & 4 \\ 0 & 1 & -2 & 4 \end{vmatrix}$$
3. $L_3' = L_3 - 4L_2$, $L_4' = L_4 - L_2$:
   $$\det(C) = 2\begin{vmatrix} 1 & 2 & -1 & 3 \\ 0 & 1 & 1 & -1 \\ 0 & 0 & -2 & 8 \\ 0 & 0 & -3 & 5 \end{vmatrix}$$
4. $L_4' = L_4 - \frac{3}{2}L_3$:
   $$\det(C) = 2\begin{vmatrix} 1 & 2 & -1 & 3 \\ 0 & 1 & 1 & -1 \\ 0 & 0 & -2 & 8 \\ 0 & 0 & 0 & -7 \end{vmatrix} = 2\cdot(1\cdot 1\cdot(-2)\cdot(-7)) = 2\cdot 14 = \mathbf{28}$$

### `B04-E04`
1. $L_2' = L_2 - 2L_1$, $L_3' = L_3 + L_1$, $L_4' = L_4 - 3L_1$:
   $$\begin{vmatrix} 1 & -1 & 2 & 1 \\ 0 & 3 & -5 & 1 \\ 0 & 1 & 3 & -1 \\ 0 & 3 & -4 & -2 \end{vmatrix}$$
2. Trocando $L_2 \leftrightarrow L_3$ (sinal `-1`):
   $$-\begin{vmatrix} 1 & -1 & 2 & 1 \\ 0 & 1 & 3 & -1 \\ 0 & 3 & -5 & 1 \\ 0 & 3 & -4 & -2 \end{vmatrix}$$
3. $L_3' = L_3 - 3L_2$, $L_4' = L_4 - 3L_2$:
   $$-\begin{vmatrix} 1 & -1 & 2 & 1 \\ 0 & 1 & 3 & -1 \\ 0 & 0 & -14 & 4 \\ 0 & 0 & -13 & 1 \end{vmatrix}$$
4. $L_4' = L_4 - \frac{13}{14}L_3$:
   $a_{44}' = 1 - \frac{13}{14}(4) = 1 - \frac{26}{7} = -\frac{19}{7}$.
   $$\det(D) = -\left(1\cdot 1\cdot(-14)\cdot\left(-\frac{19}{7}\right)\right) = -(2\cdot 19) = \mathbf{-38}$$

### `B04-E05`
1. $L_2' = L_2 - 2L_1$, $L_3' = L_3 + L_1$:
   $$\begin{vmatrix} 2 & 1 & 3 \\ 0 & 3 & 1 \\ 0 & 3 & 4 \end{vmatrix}$$
2. $L_3' = L_3 - L_2$:
   $$\begin{vmatrix} 2 & 1 & 3 \\ 0 & 3 & 1 \\ 0 & 0 & 3 \end{vmatrix}$$
3. Fatorando os pivôs ($2$ de $L_1$, $3$ de $L_2$, $3$ de $L_3$):
   $$\det(E) = 2\cdot 3\cdot 3 \begin{vmatrix} 1 & 1/2 & 3/2 \\ 0 & 1 & 1/3 \\ 0 & 0 & 1 \end{vmatrix}$$
4. Reduzindo acima da diagonal ($L_2' = L_2 - \frac{1}{3}L_3$, $L_1' = L_1 - \frac{3}{2}L_3$, depois $L_1'' = L_1' - \frac{1}{2}L_2'$):
   $$\det(E) = 18 \cdot |I_3| = 18 \cdot 1 = \mathbf{18}$$

---

## 2. Gabarito da Checagem Independente (`B04-C01` a `B04-C03`)

### `B04-C01`
1. $L_1 \leftrightarrow L_3$ (sinal `-1`):
   $$-\begin{vmatrix} -1 & 2 & 3 \\ 2 & 4 & 1 \\ 0 & 3 & -2 \end{vmatrix}$$
2. $L_2' = L_2 + 2L_1$:
   $$-\begin{vmatrix} -1 & 2 & 3 \\ 0 & 8 & 7 \\ 0 & 3 & -2 \end{vmatrix}$$
3. $L_3' = L_3 - \frac{3}{8}L_2$: $a_{33}' = -2 - \frac{21}{8} = -\frac{37}{8}$.
   $$\det(M) = -\left((-1)\cdot 8\cdot\left(-\frac{37}{8}\right)\right) = -(37) = \mathbf{-37}$$

### `B04-C02`
1. $L_3' = L_3 - 2L_1$, $L_4' = L_4 + L_1$:
   $$\begin{vmatrix} 1 & 2 & -1 & 3 \\ 0 & 2 & 4 & -2 \\ 0 & 1 & 3 & -2 \\ 0 & 3 & 2 & 3 \end{vmatrix}$$
2. Fatorando $2$ de $L_2$ (ou $L_2 \leftrightarrow L_3$ com sinal `-1`): trocando $L_2 \leftrightarrow L_3$:
   $$-\begin{vmatrix} 1 & 2 & -1 & 3 \\ 0 & 1 & 3 & -2 \\ 0 & 2 & 4 & -2 \\ 0 & 3 & 2 & 3 \end{vmatrix}$$
3. $L_3' = L_3 - 2L_2$, $L_4' = L_4 - 3L_2$:
   $$-\begin{vmatrix} 1 & 2 & -1 & 3 \\ 0 & 1 & 3 & -2 \\ 0 & 0 & -2 & 2 \\ 0 & 0 & -7 & 9 \end{vmatrix}$$
4. $L_4' = L_4 - \frac{7}{2}L_3$: $a_{44}' = 9 - 7 = 2$.
   $$\det(N) = -(1\cdot 1\cdot(-2)\cdot 2) = -(-4) = \mathbf{4}$$

### `B04-C03`
1. $L_1 \leftrightarrow L_2$ (sinal `-1`):
   $$-\begin{vmatrix} 1 & 2 & -1 & 0 \\ 2 & -1 & 3 & 1 \\ 3 & 1 & 2 & 4 \\ -2 & 3 & 1 & -1 \end{vmatrix}$$
2. $L_2' = L_2 - 2L_1$, $L_3' = L_3 - 3L_1$, $L_4' = L_4 + 2L_1$:
   $$-\begin{vmatrix} 1 & 2 & -1 & 0 \\ 0 & -5 & 5 & 1 \\ 0 & -5 & 5 & 4 \\ 0 & 7 & -1 & -1 \end{vmatrix}$$
3. $L_3' = L_3 - L_2$:
   $$-\begin{vmatrix} 1 & 2 & -1 & 0 \\ 0 & -5 & 5 & 1 \\ 0 & 0 & 0 & 3 \\ 0 & 7 & -1 & -1 \end{vmatrix}$$
4. $L_4' = L_4 + \frac{7}{5}L_2$: $a_{43}' = -1 + 7 = 6$, $a_{44}' = -1 + \frac{7}{5} = \frac{2}{5}$.
   Trocando $L_3 \leftrightarrow L_4$ (novo sinal `-1`, cancelando o `-1` externo → `+1`):
   $$+\begin{vmatrix} 1 & 2 & -1 & 0 \\ 0 & -5 & 5 & 1 \\ 0 & 0 & 6 & 2/5 \\ 0 & 0 & 0 & 3 \end{vmatrix} = 1\cdot(-5)\cdot 6\cdot 3 = \mathbf{-90}$$
*(Critério de aceitação: 3/3 acertos exatos sem consulta e sem Sarrus/Chió/Vandermonde.)*
