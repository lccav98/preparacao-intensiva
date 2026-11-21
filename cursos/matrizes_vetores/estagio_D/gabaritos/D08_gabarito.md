# Gabarito Comentado — Bloco `D08` (Áreas via Produto Vetorial — Paralelogramo e Triângulo)

> **Bloco de referência:** [D08_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/blocos/D08_bloco.md)  
> **Nota para Caça ao Erro:** Em `D08-E03`, o estudante omitiu o fator $\frac{1}{2}$ na área do triângulo.

---

## 1. Gabarito dos Exercícios (`D08-E01` a `D08-E06`)

### `D08-E01` *(Área do paralelogramo)*
$$\vec{u}\times\vec{v} = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ 2 & -1 & 3 \\ 1 & 2 & -1 \end{vmatrix} = (1 - 6)\hat{\imath} - (-2 - 3)\hat{\jmath} + (4 - (-1))\hat{k} = (-5, 5, 5).$$
$$A_{\text{paral}} = |\vec{u}\times\vec{v}| = \sqrt{(-5)^2 + 5^2 + 5^2} = \sqrt{75} = \mathbf{5\sqrt{3}}.$$

### `D08-E02` *(Área do triângulo $ABC$)*
$\overrightarrow{AB} = B - A = (2, 1, -2)$ e $\overrightarrow{AC} = C - A = (-1, 2, -1)$.
$$\overrightarrow{AB}\times\overrightarrow{AC} = (-1 - (-4))\hat{\imath} - (-2 - 2)\hat{\jmath} + (4 - (-1))\hat{k} = (3, 4, 5).$$
$$A_{\triangle ABC} = \frac{1}{2}\sqrt{3^2 + 4^2 + 5^2} = \frac{1}{2}\sqrt{50} = \mathbf{\frac{5\sqrt{2}}{2}}.$$

### `D08-E03` *(Caça ao Erro — Fator $\frac{1}{2}$)*
$\overrightarrow{AB} = (2, 2, 1)$ e $\overrightarrow{AC} = (1, -1, 2)$, logo:
$$\overrightarrow{AB}\times\overrightarrow{AC} = (4 - (-1))\hat{\imath} - (4 - 1)\hat{\jmath} + (-2 - 2)\hat{k} = (5, -3, -4).$$
Como $|\overrightarrow{AB}\times\overrightarrow{AC}| = \sqrt{25 + 9 + 16} = \sqrt{50} = 5\sqrt{2}$:
- **(a)** Área do triângulo $ABC$: $\frac{1}{2}|\overrightarrow{AB}\times\overrightarrow{AC}| = \mathbf{\frac{5\sqrt{2}}{2}}$.
- **(b)** Área do paralelogramo: $|\overrightarrow{AB}\times\overrightarrow{AC}| = \mathbf{5\sqrt{2}}$.

### `D08-E04` *(Área e altura do paralelogramo)*
$\overrightarrow{AB} = B - A = (2, 1, 2)$ e $\overrightarrow{AD} = D - A = (1, -2, 1)$.
$$\overrightarrow{AB}\times\overrightarrow{AD} = (1 - (-4))\hat{\imath} - (2 - 2)\hat{\jmath} + (-4 - 1)\hat{k} = (5, 0, -5).$$
- **(a)** $A_{\text{paral}} = \sqrt{25 + 0 + 25} = \sqrt{50} = \mathbf{5\sqrt{2}}$.
- **(b)** Como $|\overrightarrow{AB}| = \sqrt{4 + 1 + 4} = 3$, a altura relativa a $AB$ é $h = \frac{A_{\text{paral}}}{|\overrightarrow{AB}|} = \mathbf{\frac{5\sqrt{2}}{3}}$.

### `D08-E05` *(Parâmetro para área de triângulo)*
$\overrightarrow{AB} = (2, 0, 0)$ e $\overrightarrow{AC} = (-1, m, 2)$, donde:
$$\overrightarrow{AB}\times\overrightarrow{AC} = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ 2 & 0 & 0 \\ -1 & m & 2 \end{vmatrix} = (0, -4, 2m).$$
Impondo $A_{\triangle} = \frac{5}{2}$:
$$\frac{1}{2}\sqrt{0^2 + (-4)^2 + (2m)^2} = \frac{5}{2} \implies \sqrt{16 + 4m^2} = 5 \implies 16 + 4m^2 = 25 \implies m^2 = \frac{9}{4} \implies \mathbf{m = -\frac{3}{2} \text{ ou } m = \frac{3}{2}}.$$

### `D08-E06` *(Área via propriedades do produto vetorial)*
Expandindo $\vec{u}\times\vec{v} = (2\vec{a} + \vec{b})\times(\vec{a} - \vec{b})$:
$$\vec{u}\times\vec{v} = 2(\vec{a}\times\vec{a}) - 2(\vec{a}\times\vec{b}) + (\vec{b}\times\vec{a}) - (\vec{b}\times\vec{b}) = -3(\vec{a}\times\vec{b}).$$
Portanto:
$$A_{\text{paral}} = |\vec{u}\times\vec{v}| = 3|\vec{a}\times\vec{b}| = 3\cdot|\vec{a}|\,|\vec{b}|\sin 30^\circ = 3 \cdot 3 \cdot 4 \cdot \frac{1}{2} = \mathbf{18}.$$

---

## 2. Gabarito da Checagem Independente (`D08-C01` a `D08-C03`)

### `D08-C01`
$$\vec{u}\times\vec{v} = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ 3 & -2 & 1 \\ 1 & 1 & -2 \end{vmatrix} = (4 - 1)\hat{\imath} - (-6 - 1)\hat{\jmath} + (3 - (-2))\hat{k} = (3, 7, 5).$$
$$A_{\text{paral}} = \sqrt{3^2 + 7^2 + 5^2} = \sqrt{9 + 49 + 25} = \mathbf{\sqrt{83}}.$$

### `D08-C02`
$\overrightarrow{PQ} = Q - P = (2, 2, -1)$ e $\overrightarrow{PR} = R - P = (-1, 3, 2)$.
$$\overrightarrow{PQ}\times\overrightarrow{PR} = (4 - (-3))\hat{\imath} - (4 - 1)\hat{\jmath} + (6 - (-2))\hat{k} = (7, -3, 8).$$
$$A_{\triangle PQR} = \frac{1}{2}\sqrt{7^2 + (-3)^2 + 8^2} = \frac{1}{2}\sqrt{49 + 9 + 64} = \mathbf{\frac{\sqrt{122}}{2}}.$$

### `D08-C03`
$$\vec{u}\times\vec{v} = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ 1 & k & 0 \\ 2 & 0 & 1 \end{vmatrix} = (k, -1, -2k).$$
Impondo $|\vec{u}\times\vec{v}| = \sqrt{21}$:
$$\sqrt{k^2 + (-1)^2 + (-2k)^2} = \sqrt{21} \implies 5k^2 + 1 = 21 \implies k^2 = 4 \implies \mathbf{k = -2 \text{ ou } k = 2}.$$
