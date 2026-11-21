# Gabarito Comentado — Bloco `D07` (Produto Vetorial $\vec{u}\times\vec{v}$, Propriedades e Ortogonalidade)

> **Bloco de referência:** [D07_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/blocos/D07_bloco.md)  
> **Nota para Caça ao Erro:** Em `D07-E03`, o estudante omitiu o sinal negativo do cofator de $\hat{\jmath}$.

---

## 1. Gabarito dos Exercícios (`D07-E01` a `D07-E06`)

### `D07-E01` *(Anti-comutatividade)*
- **(a)** Desenvolvendo pela 1ª linha:
  $$\vec{u}\times\vec{v} = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ 2 & -1 & 3 \\ 1 & 4 & -2 \end{vmatrix} = \begin{vmatrix} -1 & 3 \\ 4 & -2 \end{vmatrix}\hat{\imath} - \begin{vmatrix} 2 & 3 \\ 1 & -2 \end{vmatrix}\hat{\jmath} + \begin{vmatrix} 2 & -1 \\ 1 & 4 \end{vmatrix}\hat{k} = (2 - 12)\hat{\imath} - (-4 - 3)\hat{\jmath} + (8 - (-1))\hat{k} = \mathbf{(-10, 7, 9)}.$$
- **(b)** Pela anti-comutatividade: $\vec{v}\times\vec{u} = -(\vec{u}\times\vec{v}) = \mathbf{(10, -7, -9)}$.

### `D07-E02` *(Propriedades algébricas)*
Calculamos primeiro $\vec{a}\times\vec{b}$ para $\vec{a} = (1, 2, -1)$ e $\vec{b} = (2, 0, 1)$:
$$\vec{a}\times\vec{b} = \begin{vmatrix} 2 & -1 \\ 0 & 1 \end{vmatrix}\hat{\imath} - \begin{vmatrix} 1 & -1 \\ 2 & 1 \end{vmatrix}\hat{\jmath} + \begin{vmatrix} 1 & 2 \\ 2 & 0 \end{vmatrix}\hat{k} = (2, -3, -4).$$
- **(a)** $2\vec{a}\times(\vec{a} + \vec{b}) = 2(\vec{a}\times\vec{a}) + 2(\vec{a}\times\vec{b}) = \vec{0} + 2(2, -3, -4) = \mathbf{(4, -6, -8)}$.
- **(b)** $(\vec{a} + 2\vec{b})\times(\vec{a} - 2\vec{b}) = \vec{a}\times\vec{a} - 2(\vec{a}\times\vec{b}) + 2(\vec{b}\times\vec{a}) - 4(\vec{b}\times\vec{b}) = -4(\vec{a}\times\vec{b}) = \mathbf{(-8, 12, 16)}$.

### `D07-E03` *(Caça ao Erro — Sinal de $\hat{\jmath}$)*
- **Teste da resposta errada:** $(3, -1, 2)\cdot(0, -14, 7) = 0 + 14 + 14 = 28 \neq 0$, provando que não é ortogonal a $\vec{u}$.
- **(a)** $\vec{u}\times\vec{v} = ((-1)(-4)-2(2))\hat{\imath} - (3(-4)-2(1))\hat{\jmath} + (3(2)-(-1)(1))\hat{k} = (0)\hat{\imath} - (-14)\hat{\jmath} + (7)\hat{k} = \mathbf{(0, 14, 7)}$.
- **(b)** Conferência: $(3, -1, 2)\cdot(0, 14, 7) = 0 - 14 + 14 = \mathbf{0}$.

### `D07-E04` *(Expressão com pontos)*
$\overrightarrow{CB} = B - C = (2, -3, 2)$, $\overrightarrow{BC} = (-2, 3, -2)$ e $\overrightarrow{CA} = A - C = (1, -2, 1)$.  
Logo $\overrightarrow{BC} - 2\overrightarrow{CA} = (-2, 3, -2) - (2, -4, 2) = (-4, 7, -4)$.  
Calculando $\overrightarrow{CB}\times(-4, 7, -4)$ pela 1ª linha:
$$\begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ 2 & -3 & 2 \\ -4 & 7 & -4 \end{vmatrix} = (12 - 14)\hat{\imath} - (-8 - (-8))\hat{\jmath} + (14 - 12)\hat{k} = \mathbf{(-2, 0, 2)}.$$
*(Alternativamente, como $\overrightarrow{CB}\times\overrightarrow{BC} = \vec{0}$, basta calcular $-2(\overrightarrow{CB}\times\overrightarrow{CA}) = -2(1, 0, -1) = (-2, 0, 2)$.)*

### `D07-E05` *(Vetor e versor ortogonais)*
- **(a)** $\vec{u}\times\vec{v} = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ 1 & 2 & 0 \\ 0 & -2 & 1 \end{vmatrix} = (2 - 0)\hat{\imath} - (1 - 0)\hat{\jmath} + (-2 - 0)\hat{k} = \mathbf{(2, -1, -2)}$ *(qualquer múltiplo $k(2, -1, -2)$ com $k\neq 0$ é válido)*.
- **(b)** $|\vec{u}\times\vec{v}| = \sqrt{4 + 1 + 4} = 3 \implies$ versor $\mathbf{\left(\frac{2}{3},\, -\frac{1}{3},\, -\frac{2}{3}\right)}$ *(ou seu oposto $\left(-\frac{2}{3}, \frac{1}{3}, \frac{2}{3}\right)$)*.

### `D07-E06` *(Norma pelo ângulo)*
- **(a)** $|\vec{a}\times\vec{b}| = |\vec{a}|\,|\vec{b}|\sin 60^\circ = 4\cdot\sqrt{3}\cdot\frac{\sqrt{3}}{2} = \mathbf{6}$.
- **(b)** $|\vec{a}\cdot\vec{b}| = |\vec{a}|\,|\vec{b}|\cos 60^\circ = 4\cdot\sqrt{3}\cdot\frac{1}{2} = \mathbf{2\sqrt{3}}$.

---

## 2. Gabarito da Checagem Independente (`D07-C01` a `D07-C03`)

### `D07-C01`
$(\vec{u} + \vec{v})\times(\vec{u} - \vec{v}) = -2(\vec{u}\times\vec{v})$.  
Com $\vec{u} = (2, 1, -1)$ e $\vec{v} = (1, -2, 3)$, temos $\vec{u}\times\vec{v} = (3-2,\; -(6+1),\; -4-1) = (1, -7, -5)$.  
Logo $(\vec{u} + \vec{v})\times(\vec{u} - \vec{v}) = -2(1, -7, -5) = \mathbf{(-2, 14, 10)}$. *(Ou calculando $\vec{u}+\vec{v}=(3,-1,2)$ e $\vec{u}-\vec{v}=(1,3,-4)$ diretamente: $(-2, 14, 10)$.)*

### `D07-C02`
$$\vec{p}\times\vec{q} = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ 1 & 0 & 2 \\ 1 & 2 & -2 \end{vmatrix} = (0 - 4)\hat{\imath} - (-2 - 2)\hat{\jmath} + (2 - 0)\hat{k} = (-4, 4, 2).$$
Como $|\vec{p}\times\vec{q}| = \sqrt{16 + 16 + 4} = 6$, um versor ortogonal a ambos é $\mathbf{\left(-\frac{2}{3},\, \frac{2}{3},\, \frac{1}{3}\right)}$ *(ou seu oposto $\left(\frac{2}{3}, -\frac{2}{3}, -\frac{1}{3}\right)$)*.

### `D07-C03`
Pela Identidade de Lagrange:
$$|\vec{u}\times\vec{v}|^2 = |\vec{u}|^2|\vec{v}|^2 - (\vec{u}\cdot\vec{v})^2 = 5^2\cdot 4^2 - 12^2 = 400 - 144 = 256 \implies |\vec{u}\times\vec{v}| = \mathbf{16}.$$
