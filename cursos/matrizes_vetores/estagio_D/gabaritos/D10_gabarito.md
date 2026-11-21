# Gabarito Comentado — Bloco `D10` (Revisão Cumulativa do Estágio D — Simulado P2)

> **Bloco de referência:** [D10_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/blocos/D10_bloco.md)

---

## 1. Gabarito dos Exercícios (`D10-E01` a `D10-E06`)

### `D10-E01` *(Combinação linear e colinearidade)*
- **(a)** $\begin{bmatrix} 1 & 1 & \mid & 1 \\ -2 & 1 & \mid & -8 \\ 3 & -1 & \mid & 11 \end{bmatrix} \xrightarrow{L_2'=L_2+2L_1,\; L_3'=L_3-3L_1} \begin{bmatrix} 1 & 1 & \mid & 1 \\ 0 & 3 & \mid & -6 \\ 0 & -4 & \mid & 8 \end{bmatrix} \xrightarrow{L_2(1/3),\; L_3'=L_3+4L_2} \begin{bmatrix} 1 & 1 & \mid & 1 \\ 0 & 1 & \mid & -2 \\ 0 & 0 & \mid & 0 \end{bmatrix}$.  
  Logo $c_2 = -2$ e $c_1 = 1 - (-2) = 3 \implies \mathbf{(3, -2)}$.
- **(b)** $\overrightarrow{AB} = (2, -2, 3)$ e $\overrightarrow{AC} = (a - 1,\; b - 2,\; 6)$. Pela 3ª coordenada, $6 = 3k \implies k = 2$, donde $a - 1 = 4 \implies a = 5$ e $b - 2 = -4 \implies b = -2$. Resposta: **$(5, -2)$**.

### `D10-E02` *(3 vértices do paralelogramo e versor)*
- **(a)** Com $P(1, 0, -1)$, $Q(3, 1, 1)$ e $R(-1, 2, 2)$:
  1. $S_1 = P + Q - R = (1+3-(-1),\; 0+1-2,\; -1+1-2) = \mathbf{(5, -1, -2)}$.
  2. $S_2 = P + R - Q = (1-1-3,\; 0+2-1,\; -1+2-1) = \mathbf{(-3, 1, 0)}$.
  3. $S_3 = Q + R - P = (3-1-1,\; 1+2-0,\; 1+2-(-1)) = \mathbf{(1, 3, 4)}$.
- **(b)** $\overrightarrow{PQ} = Q - P = (2, 1, 2)$, $|\overrightarrow{PQ}| = \sqrt{4 + 1 + 4} = 3 \implies \widehat{PQ} = \mathbf{\left(\frac{2}{3},\, \frac{1}{3},\, \frac{2}{3}\right)}$.

### `D10-E03` *(Ângulo interno e projeção)*
Vetores partindo de $A$: $\overrightarrow{AB} = (2, 0, 2)$ e $\overrightarrow{AC} = (2, 2, 0)$.
- **(a)** $\overrightarrow{AB}\cdot\overrightarrow{AC} = 4$, $|\overrightarrow{AB}| = \sqrt{8} = 2\sqrt{2}$, $|\overrightarrow{AC}| = 2\sqrt{2}$, logo $\cos\hat{A} = \frac{4}{8} = \frac{1}{2} \implies \hat{A} = \mathbf{60^\circ}$.
- **(b)** $\operatorname{proj}_{\overrightarrow{AB}}\overrightarrow{AC} = \frac{\overrightarrow{AC}\cdot\overrightarrow{AB}}{|\overrightarrow{AB}|^2}\overrightarrow{AB} = \frac{4}{8}(2, 0, 2) = \mathbf{(1, 0, 1)}$.

### `D10-E04` *(Produto vetorial e área do triângulo)*
$\overrightarrow{AB} = (2, -2, 1)$ e $\overrightarrow{AC} = (1, 1, -2)$.
- **(a)** $\overrightarrow{AB}\times\overrightarrow{AC} = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ 2 & -2 & 1 \\ 1 & 1 & -2 \end{vmatrix} = (4 - 1)\hat{\imath} - (-4 - 1)\hat{\jmath} + (2 + 2)\hat{k} = \mathbf{(3, 5, 4)}$.
- **(b)** $A_{\triangle ABC} = \frac{1}{2}\sqrt{3^2 + 5^2 + 4^2} = \frac{1}{2}\sqrt{50} = \mathbf{\frac{5\sqrt{2}}{2}}$.

### `D10-E05` *(Volume do tetraedro e coplanaridade)*
$\overrightarrow{AB} = (1, 2, 1)$, $\overrightarrow{AC} = (-1, 3, -1)$ e $\overrightarrow{AD} = (2, 1, 4)$.
$$(\overrightarrow{AB},\overrightarrow{AC},\overrightarrow{AD}) = \begin{vmatrix} 1 & 2 & 1 \\ -1 & 3 & -1 \\ 2 & 1 & 4 \end{vmatrix} = 1(12 + 1) - 2(-4 + 2) + 1(-1 - 6) = 13 + 4 - 7 = 10.$$
- **(a)** $V_{\text{tetra}} = \frac{|10|}{6} = \mathbf{\frac{5}{3}}$.
- **(b)** Como $10 \neq 0$, os pontos **Não são coplanares**.

### `D10-E06` *(Volume do paralelepípedo com parâmetro)*
$$(\vec{u},\vec{v},\vec{w}) = \begin{vmatrix} 1 & 2 & -1 \\ 2 & -1 & 1 \\ m & 1 & m-2 \end{vmatrix} = 1(-m+2-1) - 2(2m-4-m) - 1(2+m) = (-m+1) - 2(m-4) - (m+2) = 7 - 4m.$$
Impondo $|7 - 4m| = 15$:
1. $7 - 4m = 15 \implies -4m = 8 \implies \mathbf{m = -2}$.
2. $7 - 4m = -15 \implies -4m = -22 \implies \mathbf{m = \frac{11}{2}}$.
Resposta: **$\mathbf{m = -2 \text{ ou } m = \frac{11}{2}}$**.

---

## 2. Gabarito da Checagem Independente (`D10-C01` a `D10-C03`)

### `D10-C01`
$\overrightarrow{AB} = (2, 2, 0)$ e $\overrightarrow{AC} = (2, 0, 2)$.
- **(a)** $\overrightarrow{AB}\cdot\overrightarrow{AC} = 4$, $|\overrightarrow{AB}| = 2\sqrt{2}$, $|\overrightarrow{AC}| = 2\sqrt{2} \implies \cos\hat{A} = \frac{4}{8} = \frac{1}{2} \implies \hat{A} = \mathbf{60^\circ}$.
- **(b)** $\overrightarrow{AB}\times\overrightarrow{AC} = (4 - 0)\hat{\imath} - (4 - 0)\hat{\jmath} + (0 - 4)\hat{k} = (4, -4, -4)$, cujo módulo é $\sqrt{16+16+16} = 4\sqrt{3}$. Logo:
  $$A_{\triangle ABC} = \frac{1}{2}\cdot 4\sqrt{3} = \mathbf{2\sqrt{3}}.$$

### `D10-C02`
$\vec{v}\cdot\vec{u} = 1(2) + 3(-1) + (-1)(2) = -3$ e $|\vec{u}|^2 = 4 + 1 + 4 = 9$.
- **(a)** $\operatorname{proj}_{\vec{u}}\vec{v} = \frac{-3}{9}(2, -1, 2) = -\frac{1}{3}(2, -1, 2) = \mathbf{\left(-\frac{2}{3},\, \frac{1}{3},\, -\frac{2}{3}\right)}$.
- **(b)** $\vec{v}_{\perp} = (1, 3, -1) - \left(-\frac{2}{3}, \frac{1}{3}, -\frac{2}{3}\right) = \mathbf{\left(\frac{5}{3},\, \frac{8}{3},\, -\frac{1}{3}\right)}$.
  *(Conferência: $\vec{v}_{\perp}\cdot\vec{u} = \frac{10 - 8 - 2}{3} = 0$.)*

### `D10-C03`
$\overrightarrow{AB} = (1, 2, 0)$, $\overrightarrow{AC} = (0, 1, 2)$ e $\overrightarrow{AD} = (t - 1, 1, 1)$.
$$(\overrightarrow{AB},\overrightarrow{AC},\overrightarrow{AD}) = \begin{vmatrix} 1 & 2 & 0 \\ 0 & 1 & 2 \\ t-1 & 1 & 1 \end{vmatrix} = 1(1 - 2) - 2(0 - 2(t-1)) + 0 = -1 + 4t - 4 = 4t - 5.$$
Impondo $V_{\text{tetra}} = \frac{1}{6}|4t - 5| = \frac{2}{3} \implies |4t - 5| = 4$:
1. $4t - 5 = 4 \implies \mathbf{t = \frac{9}{4}}$.
2. $4t - 5 = -4 \implies \mathbf{t = \frac{1}{4}}$.
Resposta: **$\mathbf{t = \frac{1}{4} \text{ ou } t = \frac{9}{4}}$**.
