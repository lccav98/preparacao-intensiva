# Gabarito Comentado — Bloco `D02` (Vetores no $\mathbb{R}^2$ e $\mathbb{R}^3$, Base Canônica e $\overrightarrow{AB} = B - A$)

> **Bloco de referência:** [D02_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/blocos/D02_bloco.md)  
> **Nota para Caça ao Erro:** Em `D02-E03`, o estudante inverteu a subtração para $A-B$ e não substituiu $\overrightarrow{AP}=P-A$ nem $\overrightarrow{PB}=B-P$.

---

## 1. Gabarito dos Exercícios (`D02-E01` a `D02-E06`)

### `D02-E01` *(Extremidade menos origem)*
- **(a)** $\overrightarrow{AB} = B - A = (-1 - 2,\; 4 - (-3),\; 5 - 1) = \mathbf{(-3, 7, 4)} = -3\hat{\imath} + 7\hat{\jmath} + 4\hat{k}$.
- **(b)** $\overrightarrow{BA} = -\overrightarrow{AB} = A - B = \mathbf{(3, -7, -4)}$.

### `D02-E02` *(Equação vetorial linear)*
Isolando $\vec{w}$ algebricamente:
$$3\vec{u} - 3\vec{v} + \frac{1}{2}\vec{w} = 2\vec{u} - \vec{w} \implies \frac{3}{2}\vec{w} = 3\vec{v} - \vec{u} \implies \vec{w} = 2\vec{v} - \frac{2}{3}\vec{u}.$$
Substituindo $\vec{u} = (3, -1, 2)$ e $\vec{v} = (-1, 2, 1)$:
$$\vec{w} = (-2, 4, 2) - \left(2, -\frac{2}{3}, \frac{4}{3}\right) = \mathbf{\left(-4,\, \frac{14}{3},\, \frac{2}{3}\right)}.$$

### `D02-E03` *(Caça ao Erro — Subtração invertida e razão de segmento)*
- **Erros do estudante:** (1) calculou origem menos extremidade ($A - B$) em vez de extremidade menos origem ($B - A$); (2) ignorou a origem $A$ e o fator $(1+2)=3$ ao isolar $P$ em $P - A = 2(B - P)$.
- **(a)** $\overrightarrow{AB} = B - A = (4 - 1,\; 2 - (-2),\; -1 - 3) = \mathbf{(3, 4, -4)}$.
- **(b)** $P - A = 2(B - P) \implies 3P = A + 2B \implies P = \frac{1}{3}\big((1, -2, 3) + (8, 4, -2)\big) = \frac{1}{3}(9, 2, 1) = \mathbf{\left(3,\, \frac{2}{3},\, \frac{1}{3}\right)}$.

### `D02-E04` *(Combinação de segmentos e ordem fixa)*
- **(a)** $\overrightarrow{AB} = B - A = (3, 2, -3)$ e $\overrightarrow{BC} = C - B = (1, -6, 5)$. Logo:
  $$2\overrightarrow{AB} - \overrightarrow{BC} = (6, 4, -6) - (1, -6, 5) = \mathbf{(5, 10, -11)}.$$
- **(b)** $\overrightarrow{DC} = \overrightarrow{BA} \implies C - D = A - B \implies D = C + B - A = (3+2-(-1),\; -1+5-3,\; 4+(-1)-2) = \mathbf{(6, 1, 1)}$.

### `D02-E05` *(Os 3 possíveis vértices do paralelogramo)*
Com $P(1, -2, 3)$, $Q(3, 1, 0)$ e $R(-2, 4, 2)$:
1. $S_1 = P + Q - R = (1+3-(-2),\; -2+1-4,\; 3+0-2) = \mathbf{(6, -5, 1)}$.
2. $S_2 = P + R - Q = (1+(-2)-3,\; -2+4-1,\; 3+2-0) = \mathbf{(-4, 1, 5)}$.
3. $S_3 = Q + R - P = (3+(-2)-1,\; 1+4-(-2),\; 0+2-3) = \mathbf{(0, 7, -1)}$.

Resposta: **$(6, -5, 1),\; (-4, 1, 5),\; (0, 7, -1)$**.

### `D02-E06` *(Ponto médio e prolongamento)*
Com $A(-2, 1, 4)$ e $B(1, -3, 2)$:
- **(a)** $P - A = B - P \implies 2P = A + B \implies P = \left(\frac{-2+1}{2},\; \frac{1-3}{2},\; \frac{4+2}{2}\right) = \mathbf{\left(-\frac{1}{2},\, -1,\, 3\right)}$.
- **(b)** $\overrightarrow{AB} = (3, -4, -2)$, logo $P = A + 3\overrightarrow{AB} = (-2, 1, 4) + (9, -12, -6) = \mathbf{(7, -11, -2)}$.

---

## 2. Gabarito da Checagem Independente (`D02-C01` a `D02-C03`)

### `D02-C01`
$2\vec{x} + \vec{a} = 3\vec{b} - 3\vec{x} \implies 5\vec{x} = 3\vec{b} - \vec{a}$.
Com $\vec{a} = (2, -3, 1)$ e $\vec{b} = (-1, 4, -2)$:
$$5\vec{x} = (-3, 12, -6) - (2, -3, 1) = (-5, 15, -7) \implies \vec{x} = \mathbf{\left(-1,\, 3,\, -\frac{7}{5}\right)}.$$

### `D02-C02`
- **(a)** $\overrightarrow{BA} = A - B = (3, -6, 4)$ e $\overrightarrow{CB} = B - C = (-1, 3, -5)$. Então:
  $$3\overrightarrow{BA} - 2\overrightarrow{CB} = (9, -18, 12) - (-2, 6, -10) = \mathbf{(11, -24, 22)}.$$
- **(b)** $\overrightarrow{AB} = (-3, 6, -4)$, logo $M = A + \frac{1}{2}\overrightarrow{AB} = (3, -1, 2) + \left(-\frac{3}{2}, 3, -2\right) = \mathbf{\left(\frac{3}{2},\, 2,\, 0\right)}$.

### `D02-C03`
Com $P(0, 2, -1)$, $Q(2, -1, 3)$ e $R(4, 3, 1)$:
1. $S_1 = P + Q - R = (0+2-4,\; 2-1-3,\; -1+3-1) = \mathbf{(-2, -2, 1)}$.
2. $S_2 = P + R - Q = (0+4-2,\; 2+3-(-1),\; -1+1-3) = \mathbf{(2, 6, -3)}$.
3. $S_3 = Q + R - P = (2+4-0,\; -1+3-2,\; 3+1-(-1)) = \mathbf{(6, 0, 5)}$.

Resposta: **$(-2, -2, 1),\; (2, 6, -3),\; (6, 0, 5)$**.
