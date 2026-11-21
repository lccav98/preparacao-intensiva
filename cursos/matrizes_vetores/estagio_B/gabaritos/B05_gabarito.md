# Gabarito Comentado — Bloco `B05` (Equações com Determinantes e Singularidade)

> **Bloco de referência:** [B05_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_B/blocos/B05_bloco.md)

---

## 1. Gabarito dos Exercícios (`B05-E01` a `B05-E05`)

### `B05-E01`
Expandindo pela 1ª linha (sinais `+ - +`):
$$\det(A) = 1(k - (-2)) - 2(3 - 4) + (-1)(-3 - 2k) = (k + 2) + 2 + (3 + 2k) = 3k + 7$$
Igualando a zero:
$$3k + 7 = 0 \implies \mathbf{k = -\frac{7}{3}}$$

### `B05-E02`
Expandindo pela **2ª coluna** (dois zeros; sinal de $(2,2)$ é `+`):
$$\det(B) = +r\begin{vmatrix} r & 2 \\ 3 & 2 \end{vmatrix} = r(2r - 6) = 2r(r - 3)$$
Igualando a zero **sem dividir por $r$**:
$$2r(r - 3) = 0 \implies \mathbf{r = 0 \;\text{ ou }\; r = 3} \quad (\{0,\; 3\})$$

### `B05-E03`
Expandindo pela **3ª coluna** (sinais `+ - +`):
$$\det(C) = +2\begin{vmatrix} 3 & x \\ 1 & -1 \end{vmatrix} - 0 + 1\begin{vmatrix} x & 1 \\ 3 & x \end{vmatrix} = 2(-3 - x) + (x^2 - 3) = x^2 - 2x - 9$$
Igualando a $-6$:
$$x^2 - 2x - 9 = -6 \implies x^2 - 2x - 3 = 0 \implies (x - 3)(x + 1) = 0$$
Logo, $\mathbf{x = -1 \;\text{ ou }\; x = 3}$ (`{-1, 3}`).

### `B05-E04`
Expandindo pela **3ª coluna** (dois zeros; sinal de $(3,3)$ é `+`):
$$\det(D) = +x\begin{vmatrix} x & 3 \\ 2 & x + 1 \end{vmatrix} = x\left[x(x + 1) - 6\right] = x(x^2 + x - 6) = x(x + 3)(x - 2)$$
Igualando a zero (sem cortar $x$!):
$$x(x + 3)(x - 2) = 0 \implies \mathbf{x \in \{-3,\; 0,\; 2\}}$$

### `B05-E05`
- Lado esquerdo: $x^2 - 2$.
- Lado direito (pela 1ª linha): $1(2x - 2) - 0 + 1(0 - x) = 2x - 2 - x = x - 2$.
- Igualando:
  $$x^2 - 2 = x - 2 \implies x^2 - x = 0 \implies x(x - 1) = 0 \implies \mathbf{x \in \{0,\; 1\}}$$

---

## 2. Gabarito da Checagem Independente (`B05-C01` a `B05-C03`)

### `B05-C01`
Expandindo pela **2ª coluna** (sinais `- + -`):
$$\det(M) = +r\begin{vmatrix} r & 1 \\ 5 & 2 \end{vmatrix} = r(2r - 5) = 0$$
Sem cancelar $r$: $\mathbf{r = 0 \;\text{ ou }\; r = \frac{5}{2}}$ (`{0, 5/2}`).

### `B05-C02`
Expandindo pela **1ª coluna** (sinais `+ - +`):
$$\det(P) = +x\begin{vmatrix} x - 2 & 2 \\ 0 & 3 \end{vmatrix} - 0 + 1\begin{vmatrix} 1 & -1 \\ x - 2 & 2 \end{vmatrix} = 3x(x - 2) + \left[2 - (-(x - 2))\right] = 3x^2 - 6x + x = 3x^2 - 5x$$
Igualando a $2$:
$$3x^2 - 5x - 2 = 0 \implies (3x + 1)(x - 2) = 0 \implies \mathbf{x \in \{-1/3,\; 2\}}$$

### `B05-C03`
Expandindo pela **3ª coluna** (sinais `+ - +`):
$$\det(Q) = +x\begin{vmatrix} x - 1 & 6 \\ 1 & x \end{vmatrix} = x(x^2 - x - 6) = x(x - 3)(x + 2) = 0$$
Logo, $\mathbf{x \in \{-2,\; 0,\; 3\}}$.
*(Critério de aceitação: 3/3 acertos exatos com todas as raízes reais, incluindo `0`.)*
