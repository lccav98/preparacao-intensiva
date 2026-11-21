# Gabarito Comentado — Bloco `B03` (Propriedades dos Determinantes)

> **Bloco de referência:** [B03_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_B/blocos/B03_bloco.md)

---

## 1. Gabarito dos Exercícios (`B03-E01` a `B03-E05`)

### `B03-E01`
- **(a)** $\det(A^T \cdot B) = \det(A^T)\cdot\det(B) = \det(A)\cdot\det(B) = 4 \cdot (-3) = \mathbf{-12}$.
- **(b)** Como $A$ tem ordem $n = 3$: $\det(2A) = 2^3 \cdot \det(A) = 8 \cdot 4 = \mathbf{32}$.

### `B03-E02`
- **(a)** Observe que $L_3 = -3\,L_1$, pois $(-6, 3, -12) = -3\cdot(2, -1, 4)$. Pela propriedade de linhas proporcionais, $\det(M) = \mathbf{0}$.
- **(b)** Uma troca de linhas multiplica por $-1$, e multiplicar uma linha por $-5$ multiplica por $-5$. Logo: $\det(P) = (-1)\cdot(-5)\cdot\det(N) = 5 \cdot 6 = \mathbf{30}$.

### `B03-E03`
- **(a)** Matriz triangular superior: produto da diagonal principal $= 2\cdot(-1)\cdot 3\cdot 5 = \mathbf{-30}$.
- **(b)** Matriz triangular inferior: produto da diagonal principal $= (-4)\cdot\frac{1}{2}\cdot 6 = \mathbf{-12}$.

### `B03-E04`
- **(a)** $\det(A) = 2\cdot 3 - (-1)\cdot 1 = 7$; $\det(B) = 1\cdot 4 - 2\cdot(-1) = 6$. Assim, $\det(A) + \det(B) = 7 + 6 = \mathbf{13}$.
- **(b)** $A + B = \begin{bmatrix} 3 & 1 \\ 0 & 7 \end{bmatrix}$, logo $\det(A + B) = 3\cdot 7 - 1\cdot 0 = \mathbf{21}$ (confirmando $21 \neq 13$).

### `B03-E05`
- **(a)** A operação $L_3' = L_3 + 3L_1$ não altera o determinante; o fator $2$ na 2ª linha multiplica o determinante por $2$: $2 \cdot 5 = \mathbf{10}$.
- **(b)** Partindo de $[L_1, L_2, L_3]$ ($\det = 5$):
  1. $L_1 \leftrightarrow L_3$ gera $[L_3, L_2, L_1]$ ($\det = -5$);
  2. $L_2 \leftrightarrow L_3$ gera $[L_3, L_1, L_2]$ ($\det = +5$);
  3. Multiplicar a nova $L_3$ por $-1$ gera $[L_3, L_1, -L_2]$ ($\det = -5$).  
  Logo, o determinante vale **$-5$**.

---

## 2. Gabarito da Checagem Independente (`B03-C01` a `B03-C03`)

### `B03-C01`
- **(a)** $\det(A^T \cdot B^2) = \det(A)\cdot(\det(B))^2 = (-2)\cdot 3^2 = -2 \cdot 9 = \mathbf{-18}$.
- **(b)** Ordem $n = 4$: $\det(-2A) = (-2)^4 \cdot \det(A) = 16 \cdot (-2) = \mathbf{-32}$.

### `B03-C02`
- **(a)** $\det(A) = 1\cdot 3 - 0 = 3$; $\det(B) = 1\cdot 1 - (-1)\cdot 1 = 2$? **Conferência exata:** $\det(B) = 1\cdot 1 - (-1)\cdot 1$? Não: $B = \begin{bmatrix} 2 & -1 \\ 1 & 1 \end{bmatrix}$, logo $\det(B) = 2\cdot 1 - (-1)\cdot 1 = 3$. Assim $\det(A) + \det(B) = 3 + 3 = \mathbf{6}$.
- **(b)** $A + B = \begin{bmatrix} 3 & 1 \\ 1 & 4 \end{bmatrix}$, logo $\det(A + B) = 3\cdot 4 - 1\cdot 1 = \mathbf{11}$ ($11 \neq 6$).

### `B03-C03`
Partindo de $L_1=(x,y,z),\, L_2=(u,v,w),\, L_3=(r,s,t)$ com $\det = -4$:
1. $L_1 \leftrightarrow L_3$ produz $[L_3, L_2, L_1]$ ($\det = +4$);
2. $L_2 \leftrightarrow L_3$ produz $[L_3, L_1, L_2]$ ($\det = -4$);
3. Somar $-2L_1^{\text{novo}}$ ($-2L_3$) à nova $L_3$ ($L_2$) não altera o determinante ($\det = -4$);
4. Multiplicar a nova $L_2$ ($L_1$) por $3$ multiplica o determinante por $3$: $3 \cdot (-4) = \mathbf{-12}$.
*(Critério de aceitação: 3/3 acertos exatos sem consulta.)*
