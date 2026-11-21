# Gabarito Comentado — Bloco `D06` (Projeção Ortogonal $\operatorname{proj}_{\vec{v}}\vec{u}$)

> **Bloco de referência:** [D06_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/blocos/D06_bloco.md)  
> **Nota para Caça ao Erro:** Em `D06-E03`, o estudante dividiu por $|\vec{u}|^2$ em vez de $|\vec{v}|^2$ ao projetar sobre $\vec{v}$.

---

## 1. Gabarito dos Exercícios (`D06-E01` a `D06-E06`)

### `D06-E01` *(Projeção direta)*
$\vec{u}\cdot\vec{v} = 3(2) + (-2)(1) + 5(-2) = 6 - 2 - 10 = -6$; $|\vec{v}|^2 = 4 + 1 + 4 = 9$.
$$\operatorname{proj}_{\vec{v}}\vec{u} = \frac{-6}{9}(2, 1, -2) = -\frac{2}{3}(2, 1, -2) = \mathbf{\left(-\frac{4}{3},\, -\frac{2}{3},\, \frac{4}{3}\right)}.$$

### `D06-E02` *(Decomposição paralela e ortogonal)*
$\vec{u}\cdot\vec{v} = 4(1) + (-1)(2) + 3(2) = 8$; $|\vec{v}|^2 = 1 + 4 + 4 = 9$.
- **(a)** $\vec{u}_{\parallel} = \operatorname{proj}_{\vec{v}}\vec{u} = \frac{8}{9}(1, 2, 2) = \mathbf{\left(\frac{8}{9},\, \frac{16}{9},\, \frac{16}{9}\right)}$.
- **(b)** $\vec{u}_{\perp} = (4, -1, 3) - \left(\frac{8}{9}, \frac{16}{9}, \frac{16}{9}\right) = \mathbf{\left(\frac{28}{9},\, -\frac{25}{9},\, \frac{11}{9}\right)}$.
  *(Conferência: $\vec{u}_{\perp}\cdot\vec{v} = \frac{28 - 50 + 22}{9} = 0$.)*

### `D06-E03` *(Caça ao Erro — Denominador $|\vec{v}|^2$)*
- **Erro do estudante:** usou $|\vec{u}|^2 = 30$ no denominador em lugar de $|\vec{v}|^2 = 3$. Ao projetar $\vec{u}$ na direção de $\vec{v}$, o denominador pertence sempre ao vetor base $\vec{v}$.
- **(a)** $\vec{u}\cdot\vec{v} = 5(1) + 1(1) + (-2)(-1) = 8$ e $|\vec{v}|^2 = 1 + 1 + 1 = 3$. Logo:
  $$\operatorname{proj}_{\vec{v}}\vec{u} = \frac{8}{3}(1, 1, -1) = \mathbf{\left(\frac{8}{3},\, \frac{8}{3},\, -\frac{8}{3}\right)}.$$
- **(b)** $\left|\operatorname{proj}_{\vec{v}}\vec{u}\right| = \frac{8}{\sqrt{3}} = \mathbf{\frac{8\sqrt{3}}{3}}$.

### `D06-E04` *(Projeção sobre $\overrightarrow{AB}$)*
$\overrightarrow{AB} = B - A = (2, 2, -1)$, $|\overrightarrow{AB}|^2 = 4 + 4 + 1 = 9$, e $\vec{u}\cdot\overrightarrow{AB} = 4(2) + (-1)(2) + 2(-1) = 4$.
$$\operatorname{proj}_{\overrightarrow{AB}}\vec{u} = \frac{4}{9}(2, 2, -1) = \mathbf{\left(\frac{8}{9},\, \frac{8}{9},\, -\frac{4}{9}\right)}.$$

### `D06-E05` *(Parâmetro na projeção)*
$|\vec{v}|^2 = 4 + 1 + 4 = 9$ e $\vec{u}\cdot\vec{v} = 2m - 3 - 2 = 2m - 5$.  
Para $\operatorname{proj}_{\vec{v}}\vec{u} = \frac{2m - 5}{9}\vec{v} = \vec{v}$:
$$\frac{2m - 5}{9} = 1 \implies 2m - 5 = 9 \implies 2m = 14 \implies \mathbf{m = 7}.$$

### `D06-E06` *(Decomposição $\vec{a} = \vec{p} + \vec{q}$)*
$\vec{a}\cdot\vec{b} = 5(2) + 2(-2) + (-4)(1) = 2$ e $|\vec{b}|^2 = 4 + 4 + 1 = 9$.
- **(a)** $\vec{p} = \operatorname{proj}_{\vec{b}}\vec{a} = \frac{2}{9}(2, -2, 1) = \mathbf{\left(\frac{4}{9},\, -\frac{4}{9},\, \frac{2}{9}\right)}$.
- **(b)** $\vec{q} = \vec{a} - \vec{p} = (5, 2, -4) - \left(\frac{4}{9}, -\frac{4}{9}, \frac{2}{9}\right) = \mathbf{\left(\frac{41}{9},\, \frac{22}{9},\, -\frac{38}{9}\right)}$.
  *(Conferência: $\vec{q}\cdot\vec{b} = \frac{82 - 44 - 38}{9} = 0$.)*

---

## 2. Gabarito da Checagem Independente (`D06-C01` a `D06-C03`)

### `D06-C01`
$\vec{u}\cdot\vec{v} = 2(1) + (-5)(-2) + 4(2) = 20$ e $|\vec{v}|^2 = 1 + 4 + 4 = 9$.
$$\operatorname{proj}_{\vec{v}}\vec{u} = \frac{20}{9}(1, -2, 2) = \mathbf{\left(\frac{20}{9},\, -\frac{40}{9},\, \frac{40}{9}\right)}.$$

### `D06-C02`
$\vec{u}\cdot\vec{v} = 14 + 4 + 6 = 24$ e $|\vec{v}|^2 = 4 + 1 + 4 = 9$, logo $\frac{24}{9} = \frac{8}{3}$.
- **(a)** $\vec{u}_{\parallel} = \frac{8}{3}(2, -1, 2) = \mathbf{\left(\frac{16}{3},\, -\frac{8}{3},\, \frac{16}{3}\right)}$.
- **(b)** $\vec{u}_{\perp} = (7, -4, 3) - \left(\frac{16}{3}, -\frac{8}{3}, \frac{16}{3}\right) = \mathbf{\left(\frac{5}{3},\, -\frac{4}{3},\, -\frac{7}{3}\right)}$.

### `D06-C03`
$\vec{u}\cdot\vec{v} = 1(3) + 2(0) + 2(4) = 11$, $|\vec{u}| = 3$ ($|\vec{u}|^2 = 9$), $|\vec{v}| = 5$.
- **(a)** $\left|\operatorname{proj}_{\vec{v}}\vec{u}\right| = \frac{|\vec{u}\cdot\vec{v}|}{|\vec{v}|} = \mathbf{\frac{11}{5}}$.
- **(b)** $\operatorname{proj}_{\vec{u}}\vec{v} = \frac{\vec{v}\cdot\vec{u}}{|\vec{u}|^2}\vec{u} = \frac{11}{9}(1, 2, 2) = \mathbf{\left(\frac{11}{9},\, \frac{22}{9},\, \frac{22}{9}\right)}$.
