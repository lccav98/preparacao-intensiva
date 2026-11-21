# Gabarito Comentado — Bloco `D09` (Produto Misto, Coplanaridade e Volumes)

> **Bloco de referência:** [D09_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/blocos/D09_bloco.md)  
> **Nota para Caça ao Erro:** Em `D09-E03`, o estudante esqueceu que $|13 - m| = 18$ gera também a equação $13 - m = -18$.

---

## 1. Gabarito dos Exercícios (`D09-E01` a `D09-E06`)

### `D09-E01` *(Produto misto e volume do paralelepípedo)*
Desenvolvendo pela 1ª linha:
$$(\vec{u},\vec{v},\vec{w}) = \begin{vmatrix} 2 & -1 & 1 \\ 1 & 2 & -1 \\ -1 & 3 & 2 \end{vmatrix} = 2(4 - (-3)) - (-1)(2 - 1) + 1(3 - (-2)) = 2(7) + 1(1) + 1(5) = 14 + 1 + 5 = \mathbf{20}.$$
- **(a)** $(\vec{u},\vec{v},\vec{w}) = \mathbf{20}$.
- **(b)** $V_{\text{paral}} = |20| = \mathbf{20}$.

### `D09-E02` *(Coplanaridade de 3 vetores)*
- **(a)** $\begin{vmatrix} 2 & -1 & 3 \\ 1 & 2 & -1 \\ 4 & 3 & 1 \end{vmatrix} = 2(2 - (-3)) - (-1)(1 - (-4)) + 3(3 - 8) = 10 + 5 - 15 = \mathbf{0} \implies$ **São coplanares**.
- **(b)** $\begin{vmatrix} 1 & 2 & -1 \\ 0 & 1 & 3 \\ 2 & -1 & 1 \end{vmatrix} = 1(1 - (-3)) - 2(0 - 6) + (-1)(0 - 2) = 4 + 12 + 2 = \mathbf{18} \neq 0 \implies$ **Não são coplanares**.

### `D09-E03` *(Caça ao Erro — As 2 soluções de $|\det| = V$)*
- **Erro do estudante:** omitiu o módulo em $V = |(\vec{a},\vec{b},\vec{c})| = |13 - m| = 18$.
- **Resolução correta:**
  $$(\vec{a},\vec{b},\vec{c}) = \begin{vmatrix} 1 & -1 & 2 \\ 2 & 1 & -1 \\ m & 2 & 1 \end{vmatrix} = 1(1 + 2) - (-1)(2 + m) + 2(4 - m) = 3 + 2 + m + 8 - 2m = 13 - m.$$
  Impondo $|13 - m| = 18$:
  1. $13 - m = 18 \implies \mathbf{m = -5}$.
  2. $13 - m = -18 \implies \mathbf{m = 31}$.
  Resposta: **$\mathbf{m = -5 \text{ ou } m = 31}$**.

### `D09-E04` *(Coplanaridade de 4 pontos)*
$\overrightarrow{AB} = (1, 1, -2)$, $\overrightarrow{AC} = (-1, 2, 1)$ e $\overrightarrow{AD} = (2, 1, -3)$.
$$(\overrightarrow{AB},\overrightarrow{AC},\overrightarrow{AD}) = \begin{vmatrix} 1 & 1 & -2 \\ -1 & 2 & 1 \\ 2 & 1 & -3 \end{vmatrix} = 1(-6 - 1) - 1(3 - 2) + (-2)(-1 - 4) = -7 - 1 + 10 = 2.$$
- **(a)** $\left|(\overrightarrow{AB},\overrightarrow{AC},\overrightarrow{AD})\right| = \mathbf{2}$.
- **(b)** Como o produto misto é diferente de zero, os pontos **Não são coplanares**.

### `D09-E05` *(Volume do tetraedro)*
$\overrightarrow{AB} = (-1, 2, 0)$, $\overrightarrow{AC} = (-1, 0, 3)$ e $\overrightarrow{AD} = (1, 2, 3)$.
$$(\overrightarrow{AB},\overrightarrow{AC},\overrightarrow{AD}) = \begin{vmatrix} -1 & 2 & 0 \\ -1 & 0 & 3 \\ 1 & 2 & 3 \end{vmatrix} = -1(0 - 6) - 2(-3 - 3) + 0 = 6 + 12 = 18.$$
$$V_{\text{tetra}} = \frac{|18|}{6} = \mathbf{3}.$$

### `D09-E06` *(Tetraedro com parâmetro)*
$\overrightarrow{AB} = (2, 1, 0)$, $\overrightarrow{AC} = (1, 3, 1)$ e $\overrightarrow{AD} = (0, 1, k)$.
$$(\overrightarrow{AB},\overrightarrow{AC},\overrightarrow{AD}) = \begin{vmatrix} 2 & 1 & 0 \\ 1 & 3 & 1 \\ 0 & 1 & k \end{vmatrix} = 2(3k - 1) - 1(k - 0) + 0 = 5k - 2.$$
Impondo $V_{\text{tetra}} = \frac{1}{6}|5k - 2| = \frac{5}{3} \implies |5k - 2| = 10$:
1. $5k - 2 = 10 \implies 5k = 12 \implies \mathbf{k = \frac{12}{5}}$.
2. $5k - 2 = -10 \implies 5k = -8 \implies \mathbf{k = -\frac{8}{5}}$.
Resposta: **$\mathbf{k = -\frac{8}{5} \text{ ou } k = \frac{12}{5}}$**.

---

## 2. Gabarito da Checagem Independente (`D09-C01` a `D09-C03`)

### `D09-C01`
$\overrightarrow{PQ} = (1, -2, 2)$, $\overrightarrow{PR} = (-1, -1, 3)$ e $\overrightarrow{PS} = (2, -3, 3)$.
$$(\overrightarrow{PQ},\overrightarrow{PR},\overrightarrow{PS}) = \begin{vmatrix} 1 & -2 & 2 \\ -1 & -1 & 3 \\ 2 & -3 & 3 \end{vmatrix} = 1(-3 + 9) - (-2)(-3 - 6) + 2(3 + 2) = 6 - 18 + 10 = -2.$$
- **(a)** $V_{\text{tetra}} = \frac{|-2|}{6} = \mathbf{\frac{1}{3}}$.
- **(b)** Como $V_{\text{tetra}} \neq 0$, os pontos **Não são coplanares**.

### `D09-C02`
$$(\vec{u},\vec{v},\vec{w}) = \begin{vmatrix} 2 & -1 & 1 \\ 1 & 3 & -2 \\ m & 1 & m+1 \end{vmatrix} = 2(3m + 3 + 2) - (-1)(m + 1 + 2m) + 1(1 - 3m) = 6m + 10 + 3m + 1 + 1 - 3m = 6m + 12.$$
Impondo $|6m + 12| = 20$:
1. $6m + 12 = 20 \implies 6m = 8 \implies \mathbf{m = \frac{4}{3}}$.
2. $6m + 12 = -20 \implies 6m = -32 \implies \mathbf{m = -\frac{16}{3}}$.
Resposta: **$\mathbf{m = -\frac{16}{3} \text{ ou } m = \frac{4}{3}}$**.

### `D09-C03`
$\overrightarrow{AB} = (1, 2, 1)$, $\overrightarrow{AC} = (-1, 1, 2)$ e $\overrightarrow{AD} = (2, 0, 3)$.
1. $\overrightarrow{AB}\times\overrightarrow{AC} = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ 1 & 2 & 1 \\ -1 & 1 & 2 \end{vmatrix} = (4-1)\hat{\imath} - (2+1)\hat{\jmath} + (1+2)\hat{k} = (3, -3, 3)$, logo $|\overrightarrow{AB}\times\overrightarrow{AC}| = \sqrt{9+9+9} = 3\sqrt{3}$.
2. $(\overrightarrow{AB},\overrightarrow{AC},\overrightarrow{AD}) = \overrightarrow{AD}\cdot(\overrightarrow{AB}\times\overrightarrow{AC}) = 2(3) + 0(-3) + 3(3) = 15$.
3. $h = \frac{|15|}{3\sqrt{3}} = \frac{5}{\sqrt{3}} = \mathbf{\frac{5\sqrt{3}}{3}}$.
