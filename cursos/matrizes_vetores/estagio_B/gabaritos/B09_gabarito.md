# Gabarito Comentado — Bloco `B09` (Revisão Cumulativa do Estágio B — Simulado P1)

> **Bloco de referência:** [B09_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_B/blocos/B09_bloco.md)

---

## 1. Gabarito dos Exercícios (`B09-E01` a `B09-E05`)

### `B09-E01`
1. $L_2' = L_2 - 2L_1$, $L_3' = L_3 + L_1$:
   $$\begin{vmatrix} 1 & -2 & 0 & 1 \\ 0 & 1 & 1 & 2 \\ 0 & 2 & 2 & 0 \\ 0 & 2 & -1 & 3 \end{vmatrix}$$
2. $L_3' = L_3 - 2L_2$, $L_4' = L_4 - 2L_2$:
   $$\begin{vmatrix} 1 & -2 & 0 & 1 \\ 0 & 1 & 1 & 2 \\ 0 & 0 & 0 & -4 \\ 0 & 0 & -3 & -1 \end{vmatrix}$$
3. Trocando $L_3 \leftrightarrow L_4$ (sinal `-1`):
   $$-\begin{vmatrix} 1 & -2 & 0 & 1 \\ 0 & 1 & 1 & 2 \\ 0 & 0 & -3 & -1 \\ 0 & 0 & 0 & -4 \end{vmatrix} = -\left(1\cdot 1\cdot(-3)\cdot(-4)\right) = \mathbf{-12}$$

### `B09-E02`
- **(a)** Ordem $n = 3$: $\det(2 A^T B^{-1}) = 2^3 \cdot \det(A^T) \cdot \det(B^{-1}) = 8 \cdot 3 \cdot \left(-\frac{1}{2}\right) = \mathbf{-12}$.
- **(b)** $\det((AB)^T) = \det(AB) = \det(A)\cdot\det(B) = 3\cdot(-2) = \mathbf{-6}$.

### `B09-E03`
Expandindo pela **2ª coluna** (dois zeros; sinal de $(2,2)$ é `+`):
$$\det(P) = +k\begin{vmatrix} k & 2 \\ 4 & k - 2 \end{vmatrix} = k\left(k(k - 2) - 8\right) = k(k^2 - 2k - 8) = k(k - 4)(k + 2) = 0$$
Sem dividir por $k$: $\mathbf{k \in \{-2,\; 0,\; 4\}}$.

### `B09-E04`
Aplicando `[A | I_3] -> [I_3 | A^{-1}]`:
1. $L_{12}$: $\left[\begin{array}{ccc|ccc} 1 & 2 & 1 & 0 & 1 & 0 \\ 2 & 1 & 0 & 1 & 0 & 0 \\ 0 & 1 & 2 & 0 & 0 & 1 \end{array}\right] \xrightarrow{L_2' = L_2 - 2L_1} \left[\begin{array}{ccc|ccc} 1 & 2 & 1 & 0 & 1 & 0 \\ 0 & -3 & -2 & 1 & -2 & 0 \\ 0 & 1 & 2 & 0 & 0 & 1 \end{array}\right]$
2. $L_{23}$: $\left[\begin{array}{ccc|ccc} 1 & 2 & 1 & 0 & 1 & 0 \\ 0 & 1 & 2 & 0 & 0 & 1 \\ 0 & -3 & -2 & 1 & -2 & 0 \end{array}\right] \xrightarrow{L_1'=L_1-2L_2,\; L_3'=L_3+3L_2} \left[\begin{array}{ccc|ccc} 1 & 0 & -3 & 0 & 1 & -2 \\ 0 & 1 & 2 & 0 & 0 & 1 \\ 0 & 0 & 4 & 1 & -2 & 3 \end{array}\right]$
3. $L_3(1/4)$, depois $L_1' = L_1 + 3L_3$ e $L_2' = L_2 - 2L_3$:
   $$A^{-1} = \begin{bmatrix} 3/4 & -1/2 & 1/4 \\ -1/2 & 1 & -1/2 \\ 1/4 & -1/2 & 3/4 \end{bmatrix}$$

### `B09-E05`
1. $A X^T = C - B = \begin{bmatrix} 4 & 2 \\ 2 & 2 \end{bmatrix}$.
2. Invertendo $A = \begin{bmatrix} 2 & 3 \\ 1 & 2 \end{bmatrix}$ via `[A | I_2]`: $A^{-1} = \begin{bmatrix} 2 & -3 \\ -1 & 2 \end{bmatrix}$.
3. $X^T = A^{-1}(C - B) = \begin{bmatrix} 2 & -3 \\ -1 & 2 \end{bmatrix}\begin{bmatrix} 4 & 2 \\ 2 & 2 \end{bmatrix} = \begin{bmatrix} 2 & -2 \\ 0 & 2 \end{bmatrix}$.
4. Transpondo $X^T$:
   $$X = \begin{bmatrix} 2 & 0 \\ -2 & 2 \end{bmatrix}$$

---

## 2. Gabarito da Checagem Independente (`B09-C01` a `B09-C03`)

### `B09-C01`
1. $L_{12}$ (sinal `-1`): $-\begin{vmatrix} 1 & -1 & 3 & 2 \\ 0 & 2 & -1 & 1 \\ 2 & 0 & 1 & -1 \\ -1 & 3 & 2 & 0 \end{vmatrix}$
2. $L_3' = L_3 - 2L_1$, $L_4' = L_4 + L_1$:
   $$-\begin{vmatrix} 1 & -1 & 3 & 2 \\ 0 & 2 & -1 & 1 \\ 0 & 2 & -5 & -5 \\ 0 & 2 & 5 & 2 \end{vmatrix}$$
3. $L_3' = L_3 - L_2$, $L_4' = L_4 - L_2$:
   $$-\begin{vmatrix} 1 & -1 & 3 & 2 \\ 0 & 2 & -1 & 1 \\ 0 & 0 & -4 & -6 \\ 0 & 0 & 6 & 1 \end{vmatrix}$$
4. $L_4' = L_4 + \frac{3}{2}L_3$: $a_{44}' = 1 + \frac{3}{2}(-6) = -8$.
   $$\det(M) = -\left(1\cdot 2\cdot(-4)\cdot(-8)\right) = -(64) = \mathbf{-64}$$

### `B09-C02`
Expandindo pela **2ª coluna** (sinais `- + -`):
$$\det(Q) = +x\begin{vmatrix} x & 2 \\ 3 & 2x + 1 \end{vmatrix} = x\left(2x^2 + x - 6\right) = x(2x - 3)(x + 2) = 0$$
Logo, $\mathbf{x \in \{-2,\; 0,\; 3/2\}}$.

### `B09-C03`
- **(a)** Escalonando `[A | I_3]`:
  1. $L_3' = L_3 - L_1$: $\left[\begin{array}{ccc|ccc} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 2 & 1 & 0 & 1 & 0 \\ 0 & -1 & 2 & -1 & 0 & 1 \end{array}\right] \xrightarrow{L_2 \leftrightarrow L_3,\, L_2(-1)} \left[\begin{array}{ccc|ccc} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 1 & -2 & 1 & 0 & -1 \\ 0 & 2 & 1 & 0 & 1 & 0 \end{array}\right]$
  2. $L_1' = L_1 - L_2$, $L_3' = L_3 - 2L_2$: $\left[\begin{array}{ccc|ccc} 1 & 0 & 2 & 0 & 0 & 1 \\ 0 & 1 & -2 & 1 & 0 & -1 \\ 0 & 0 & 5 & -2 & 1 & 2 \end{array}\right]$
  3. $L_3(1/5)$, depois $L_1' = L_1 - 2L_3$ e $L_2' = L_2 + 2L_3$:
     $$A^{-1} = \begin{bmatrix} 4/5 & -2/5 & 1/5 \\ 1/5 & 2/5 & -1/5 \\ -2/5 & 1/5 & 2/5 \end{bmatrix}$$
- **(b)** $X = A^{-1}B = \begin{bmatrix} 4/5 & -2/5 & 1/5 \\ 1/5 & 2/5 & -1/5 \\ -2/5 & 1/5 & 2/5 \end{bmatrix}\begin{bmatrix} 3 & 1 \\ 1 & -2 \\ 2 & 4 \end{bmatrix} = \begin{bmatrix} 12/5 & 12/5 \\ 3/5 & -7/5 \\ -1/5 & 4/5 \end{bmatrix}$.
*(Critério de aceitação: 3/3 acertos exatos sem consulta.)*
