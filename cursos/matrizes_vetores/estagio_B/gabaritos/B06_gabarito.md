# Gabarito Comentado — Bloco `B06` (Matriz Inversa por Definição e Singularidade)

> **Bloco de referência:** [B06_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_B/blocos/B06_bloco.md)  
> **Método obrigatório:** Definição $AB = I$ (sem matriz adjunta).

---

## 1. Gabarito dos Exercícios (`B06-E01` a `B06-E05`)

### `B06-E01`
- **(a)** $A\cdot B = \begin{bmatrix} 2\cdot 3 + 1(-5) & 2(-1) + 1\cdot 2 \\ 5\cdot 3 + 3(-5) & 5(-1) + 3\cdot 2 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$.
- **(b)** **`sim`** *(também $BA = I_2$, logo $B = A^{-1}$)*.

### `B06-E02`
Fazendo $A\begin{bmatrix} a & b \\ c & d \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$:
- 1ª coluna: $\begin{cases} 2a + 5c = 1 \\ a + 3c = 0 \implies a = -3c \end{cases}$ $\implies 2(-3c) + 5c = 1 \implies -c = 1 \implies c = -1,\; a = 3$.
- 2ª coluna: $\begin{cases} 2b + 5d = 0 \\ b + 3d = 1 \implies b = 1 - 3d \end{cases}$ $\implies 2(1 - 3d) + 5d = 0 \implies 2 - d = 0 \implies d = 2,\; b = -5$.

Logo: $A^{-1} = \begin{bmatrix} 3 & -5 \\ -1 & 2 \end{bmatrix}$.

### `B06-E03`
Efetuando $A\cdot B = \begin{bmatrix} 3 & 5 \\ 1 & 2 \end{bmatrix} \begin{bmatrix} 2 & m \\ -1 & n \end{bmatrix} = \begin{bmatrix} 1 & 3m + 5n \\ 0 & m + 2n \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$:
- Da posição $(2,2)$: $m = 1 - 2n$.
- Na posição $(1,2)$: $3(1 - 2n) + 5n = 0 \implies 3 - n = 0 \implies \mathbf{n = 3}$, e $\mathbf{m = 1 - 6 = -5}$.

### `B06-E04`
Desenvolvendo $\det(M)$ pela 1ª coluna (sinais `+ - +`):
$$\det(M) = +1(k - 2) - 0 + 2(4 - (-k)) = k - 2 + 8 + 2k = 3k + 6$$
- **(a)** Para $k = 2$: $\det(M) = 3(2) + 6 = \mathbf{12}$.
- **(b)** Singular $\Leftrightarrow 3k + 6 = 0 \implies \mathbf{k = -2}$.

### `B06-E05`
Fazendo $\begin{bmatrix} 1/2 & 1 \\ 1 & 4 \end{bmatrix} \begin{bmatrix} a & b \\ c & d \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$:
- 1ª coluna: $\begin{cases} \frac{1}{2}a + c = 1 \\ a + 4c = 0 \implies a = -4c \end{cases}$ $\implies -2c + c = 1 \implies c = -1,\; a = 4$.
- 2ª coluna: $\begin{cases} \frac{1}{2}b + d = 0 \\ b + 4d = 1 \implies b = 1 - 4d \end{cases}$ $\implies \frac{1}{2} - 2d + d = 0 \implies d = \frac{1}{2},\; b = -1$.

Logo: $A^{-1} = \begin{bmatrix} 4 & -1 \\ -1 & 1/2 \end{bmatrix}$.

---

## 2. Gabarito da Checagem Independente (`B06-C01` a `B06-C03`)

### `B06-C01`
$A\cdot B = \begin{bmatrix} 3x + 2y & -6 + 6 \\ x + y & -2 + 3 \end{bmatrix} = \begin{bmatrix} 3x + 2y & 0 \\ x + y & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$.
- $x + y = 0 \implies y = -x$.
- $3x + 2(-x) = 1 \implies \mathbf{x = 1}$ e $\mathbf{y = -1}$.

### `B06-C02`
$\begin{bmatrix} 2 & -1 \\ 4 & 3 \end{bmatrix}\begin{bmatrix} a & b \\ c & d \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$:
- 1ª coluna: $c = 2a - 1 \implies 4a + 3(2a - 1) = 0 \implies 10a = 3 \implies a = \frac{3}{10},\; c = \frac{6}{10} - 1 = -\frac{2}{5}$.
- 2ª coluna: $d = 2b \implies 4b + 3(2b) = 1 \implies 10b = 1 \implies b = \frac{1}{10},\; d = \frac{1}{5}$.

Logo: $A^{-1} = \begin{bmatrix} 3/10 & 1/10 \\ -2/5 & 1/5 \end{bmatrix}$.

### `B06-C03`
$A$ não possui inversa $\Leftrightarrow \det(A) = 0$. Expandindo pela **3ª coluna** (sinais `+ - +`):
$$\det(A) = +(k - 1)\begin{vmatrix} k & 1 \\ 4 & k \end{vmatrix} = (k - 1)(k^2 - 4) = (k - 1)(k - 2)(k + 2) = 0$$
Logo, $\mathbf{k \in \{-2,\; 1,\; 2\}}$.
*(Critério de aceitação: 3/3 acertos exatos sem consulta e sem matriz adjunta.)*
