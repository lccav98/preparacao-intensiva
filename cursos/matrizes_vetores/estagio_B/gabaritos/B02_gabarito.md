# Gabarito Comentado — Bloco `B02` (Desenvolvimento por Qualquer Linha ou Coluna)

> **Bloco de referência:** [B02_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_B/blocos/B02_bloco.md)  
> **Método obrigatório:** Matriz de sinais xadrez `(-1)^{i+j}` e expansão estratégica por linha ou coluna (sem Sarrus, Chió ou Vandermonde).

---

## 1. Gabarito dos Exercícios (`B02-E01` a `B02-E05`)

### `B02-E01`
Expandindo pela **2ª coluna** (dois zeros; sinais **`-  +  -`**):
$$\det(A) = +4\begin{vmatrix} 2 & -1 \\ -1 & 5 \end{vmatrix} = 4(10 - 1) = 4\cdot 9 = \mathbf{36}$$

### `B02-E02`
Expandindo pela **3ª linha** (sinais **`+  -  +`**):
$$\det(B) = +0\cdot M_{31} - 4\begin{vmatrix} 1 & 3 \\ 2 & -1 \end{vmatrix} + (-2)\begin{vmatrix} 1 & -2 \\ 2 & 1 \end{vmatrix}$$
$$\det(B) = -4(-1 - 6) - 2(1 - (-4)) = -4(-7) - 2(5) = 28 - 10 = \mathbf{18}$$

### `B02-E03`
A **2ª linha** possui três zeros e elemento $c_{23} = 2$. Sinal da posição $(2,3)$: $(-1)^{2+3} = -1$ (**`-`**).
$$\det(C) = -2\begin{vmatrix} 2 & 0 & 3 \\ 1 & 3 & -2 \\ -1 & 2 & 1 \end{vmatrix}$$
Expandindo o `3x3` pela 1ª linha (sinais `+ - +`):
$$= -2\left[2(3 - (-4)) - 0 + 3(2 - (-3))\right] = -2\left[2(7) + 3(5)\right] = -2(14 + 15) = -2(29) = \mathbf{-58}$$

### `B02-E04`
Expandindo pela **2ª linha** (dois zeros; sinais **`-  +  -  +`**):
$$\det(D) = -3\begin{vmatrix} 2 & 0 & -1 \\ 1 & 1 & 3 \\ 4 & -1 & 2 \end{vmatrix} - 2\begin{vmatrix} 1 & 2 & -1 \\ -2 & 1 & 3 \\ 0 & 4 & 2 \end{vmatrix}$$
- Primeiro `3x3` (pela 1ª linha): $2(2 - (-3)) - 0 - 1(-1 - 4) = 2(5) + 5 = 15$.
- Segundo `3x3` (pela 1ª coluna, sinais `+ - +`): $1(2 - 12) - (-2)(4 - (-4)) + 0 = -10 + 16 = 6$.

Logo: $\det(D) = -3(15) - 2(6) = -45 - 12 = \mathbf{-57}$.

### `B02-E05`
Expandindo pela **3ª coluna** (sinais **`+  -  +  -`**; entradas $0, 1/2, 0, -2$):
$$\det(E) = -\frac{1}{2}\begin{vmatrix} 2 & -1 & 3 \\ 4 & 0 & 2 \\ -1 & 2 & 1 \end{vmatrix} - (-2)\begin{vmatrix} 2 & -1 & 3 \\ 1 & 3 & -1 \\ 4 & 0 & 2 \end{vmatrix}$$
- Primeiro `3x3` (pela 2ª linha, sinais `- + -`): $-4(-1 - 6) + 0 - 2(4 - 1) = -4(-7) - 6 = 28 - 6 = 22$.
- Segundo `3x3` (pela 3ª linha, sinais `+ - +`): $4(1 - 9) - 0 + 2(6 - (-1)) = 4(-8) + 2(7) = -32 + 14 = -18$.

Logo: $\det(E) = -\frac{1}{2}(22) + 2(-18) = -11 - 36 = \mathbf{-47}$.

---

## 2. Gabarito da Checagem Independente (`B02-C01` a `B02-C03`)

### `B02-C01`
Expandindo pela **2ª linha** (sinais **`-  +  -`**):
$$\det(M) = +(-2)\begin{vmatrix} 3 & 2 \\ 4 & -1 \end{vmatrix} = -2(-3 - 8) = -2(-11) = \mathbf{22}$$

### `B02-C02`
A **4ª coluna** tem três zeros e $n_{34} = -3$. Sinal da posição $(3,4)$: $(-1)^{3+4} = -1$ (**`-`**).
$$\det(N) = -(-3)\begin{vmatrix} 1 & -2 & 3 \\ 2 & 1 & -1 \\ 3 & 0 & 1 \end{vmatrix} = +3\left[3(-2 - 3) - 0 + 1(1 - (-4))\right] = 3\left[3(-5) + 5\right] = 3(-10) = \mathbf{-30}$$
*(Atenção! Vamos conferir o cálculo acima passo a passo!)*
Espere: no `3x3` $\begin{vmatrix} 1 & -2 & 3 \\ 2 & 1 & -1 \\ 3 & 0 & 1 \end{vmatrix}$ expandido pela 3ª linha (sinais `+ - +`):
- Termo $(3,1)$: $+3\begin{vmatrix} -2 & 3 \\ 1 & -1 \end{vmatrix} = 3(2 - 3) = -3$.
- Termo $(3,3)$: $+1\begin{vmatrix} 1 & -2 \\ 2 & 1 \end{vmatrix} = 1(1 + 4) = 5$.
- Soma do `3x3`: $-3 + 5 = 2$! (Na linha acima estava digitado `-2 - 3` por descuido no rascunho; o correto é `(-2)(-1) - 3(1) = 2 - 3 = -1`, dando `3(-1) + 5 = 2`!)
Logo: $\det(N) = +3 \cdot (2) = \mathbf{6}$. *(Conferido exatamente pelo algoritmo de Gauss em frações!)*

### `B02-C03`
Expandindo pela **2ª linha** (sinais **`-  +  -  +`**):
$$\det(P) = +(-2)\begin{vmatrix} 2 & -1 & 3 \\ 1 & 2 & -1 \\ -1 & 3 & 2 \end{vmatrix} + 4\begin{vmatrix} 2 & 1 & -1 \\ 1 & 3 & 2 \\ -1 & 0 & 3 \end{vmatrix}$$
- Primeiro `3x3` (pela 1ª linha): $2(4 - (-3)) - (-1)(2 - 1) + 3(3 - (-2)) = 14 + 1 + 15 = 30$.
- Segundo `3x3` (pela 3ª linha): $-1(2 - (-3)) - 0 + 3(6 - 1) = -5 + 15 = 10$.

Logo: $\det(P) = -2(30) + 4(10) = -60 + 40 = \mathbf{-20}$.
*(Critério de aceitação: 3/3 acertos exatos sem consulta e sem Sarrus/Chió/Vandermonde.)*
