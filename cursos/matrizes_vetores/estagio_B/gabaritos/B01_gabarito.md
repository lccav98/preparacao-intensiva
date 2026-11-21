# Gabarito Comentado — Bloco `B01` (Determinante de 2ª e 3ª Ordem — 1ª Linha)

> **Bloco de referência:** [B01_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_B/blocos/B01_bloco.md)  
> **Método obrigatório:** `2x2` via diagonal principal menos secundária; `3x3` exclusivamente via desenvolvimento pela 1ª linha com sinais `+ - +` (sem Regra de Sarrus).

---

## 1. Gabarito dos Exercícios (`B01-E01` a `B01-E05`)

### `B01-E01`
- **(a)** $3\cdot 4 - (-2)\cdot 5 = 12 - (-10) = 12 + 10 = \mathbf{22}$.
- **(b)** $\left(\frac{1}{2}\right)\cdot 6 - (-3)\cdot 2 = 3 - (-6) = 3 + 6 = \mathbf{9}$.

### `B01-E02`
Desenvolvendo pela 1ª linha com sinais **`+  -  +`**:
$$\det(A) = +1\begin{vmatrix} 0 & -1 \\ 5 & 1 \end{vmatrix} - (-2)\begin{vmatrix} 4 & -1 \\ 2 & 1 \end{vmatrix} + 3\begin{vmatrix} 4 & 0 \\ 2 & 5 \end{vmatrix}$$
- $1\cdot(0\cdot 1 - (-1)\cdot 5) = 1\cdot 5 = 5$
- $+2\cdot(4\cdot 1 - (-1)\cdot 2) = 2\cdot(4 + 2) = 12$
- $+3\cdot(4\cdot 5 - 0\cdot 2) = 3\cdot 20 = 60$

Logo: $\det(A) = 5 + 12 + 60 = \mathbf{77}$.

### `B01-E03`
Desenvolvendo pela 1ª linha com sinais **`+  -  +`**:
$$\det(B) = +3\begin{vmatrix} 4 & 5 \\ 1 & 2 \end{vmatrix} - 0\begin{vmatrix} 1 & 5 \\ -2 & 2 \end{vmatrix} + (-2)\begin{vmatrix} 1 & 4 \\ -2 & 1 \end{vmatrix}$$
- $3\cdot(8 - 5) = 3\cdot 3 = 9$
- $-0 = 0$
- $-2\cdot(1 - (-8)) = -2\cdot 9 = -18$

Logo: $\det(B) = 9 + 0 - 18 = \mathbf{-9}$.

### `B01-E04`
Desenvolvendo pela 1ª linha:
$$\det(C) = +\frac{1}{2}\begin{vmatrix} 3 & -2 \\ 1 & 0 \end{vmatrix} - (-1)\begin{vmatrix} 4 & -2 \\ 2 & 0 \end{vmatrix} + 2\begin{vmatrix} 4 & 3 \\ 2 & 1 \end{vmatrix}$$
- $\frac{1}{2}(0 - (-2)) = \frac{1}{2}(2) = 1$
- $+1(0 - (-4)) = 4$
- $+2(4 - 6) = 2(-2) = -4$

Logo: $\det(C) = 1 + 4 - 4 = \mathbf{1}$.

### `B01-E05`
- **(a)** Para $A$:
  $$\det(A) = +2\begin{vmatrix} -2 & 4 \\ 0 & 2 \end{vmatrix} - 1\begin{vmatrix} 3 & 4 \\ 1 & 2 \end{vmatrix} + (-1)\begin{vmatrix} 3 & -2 \\ 1 & 0 \end{vmatrix}$$
  $$\det(A) = 2(-4 - 0) - 1(6 - 4) - 1(0 - (-2)) = -8 - 2 - 2 = \mathbf{-12}$$
- **(b)** Para $B$:
  $$\det(B) = +(-1)\begin{vmatrix} 1 & -1 \\ 4 & 1 \end{vmatrix} - 3\begin{vmatrix} 0 & -1 \\ 2 & 1 \end{vmatrix} + 2\begin{vmatrix} 0 & 1 \\ 2 & 4 \end{vmatrix}$$
  $$\det(B) = -1(1 - (-4)) - 3(0 - (-2)) + 2(0 - 2) = -5 - 6 - 4 = -15$$
  Portanto: $\det(A) - 2\det(B) = -12 - 2(-15) = -12 + 30 = \mathbf{18}$.

---

## 2. Gabarito da Checagem Independente (`B01-C01` a `B01-C03`)

### `B01-C01`
$$\left(-\frac{3}{2}\right)(-2) - 4\left(\frac{1}{4}\right) = 3 - 1 = \mathbf{2}$$

### `B01-C02`
Desenvolvendo pela 1ª linha:
$$\det(P) = +2\begin{vmatrix} 4 & 2 \\ 0 & -2 \end{vmatrix} - (-3)\begin{vmatrix} -1 & 2 \\ 3 & -2 \end{vmatrix} + 1\begin{vmatrix} -1 & 4 \\ 3 & 0 \end{vmatrix}$$
$$\det(P) = 2(-8 - 0) + 3(2 - 6) + 1(0 - 12) = -16 - 12 - 12 = \mathbf{-40}$$

### `B01-C03`
Desenvolvendo pela 1ª linha:
$$\det(Q) = +(-2)\begin{vmatrix} 2 & -1 \\ -1 & 4 \end{vmatrix} - (-4)\begin{vmatrix} 1 & -1 \\ 3 & 4 \end{vmatrix} + 3\begin{vmatrix} 1 & 2 \\ 3 & -1 \end{vmatrix}$$
$$\det(Q) = -2(8 - 1) + 4(4 - (-3)) + 3(-1 - 6) = -14 + 28 - 21 = \mathbf{-7}$$
*(Critério de aceitação: 3/3 acertos exatos sem consulta e sem uso de Sarrus.)*
