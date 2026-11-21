# Gabarito Comentado — Bloco `D03` (Combinação Linear, Paralelismo e Colinearidade de Pontos)

> **Bloco de referência:** [D03_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/blocos/D03_bloco.md)  
> **Nota para Caça ao Erro:** Em `D03-E03`, o estudante não verificou a 3ª coordenada na condição de proporcionalidade.

---

## 1. Gabarito dos Exercícios (`D03-E01` a `D03-E06`)

### `D03-E01` *(Combinação linear no $\mathbb{R}^2$)*
$k_1(2, -3) + k_2(-1, 4) = (7, -13) \implies \begin{cases} 2k_1 - k_2 = 7 \\ -3k_1 + 4k_2 = -13 \end{cases}$.
Escalonando (trocando linhas ou multiplicando $L_1$ por $1/2$):
$$\begin{bmatrix} 2 & -1 & \mid & 7 \\ -3 & 4 & \mid & -13 \end{bmatrix} \xrightarrow{L_1(1/2)} \begin{bmatrix} 1 & -1/2 & \mid & 7/2 \\ -3 & 4 & \mid & -13 \end{bmatrix} \xrightarrow{L_2' = L_2 + 3L_1} \begin{bmatrix} 1 & -1/2 & \mid & 7/2 \\ 0 & 5/2 & \mid & -5/2 \end{bmatrix}.$$
Logo $k_2 = -1$ e $k_1 - \frac{1}{2}(-1) = \frac{7}{2} \implies k_1 = 3$.  
Resposta: **(a) $k_1 = 3$**; **(b) $k_2 = -1$**.

### `D03-E02` *(Sistema $3\times 2$ por escalonamento)*
$a_1(1, -2, 1) + a_2(2, 1, -3) = (-1, -8, 9)$ gera:
$$\begin{bmatrix} 1 & 2 & \mid & -1 \\ -2 & 1 & \mid & -8 \\ 1 & -3 & \mid & 9 \end{bmatrix} \xrightarrow{L_2' = L_2 + 2L_1,\; L_3' = L_3 - L_1} \begin{bmatrix} 1 & 2 & \mid & -1 \\ 0 & 5 & \mid & -10 \\ 0 & -5 & \mid & 10 \end{bmatrix} \xrightarrow{L_2(1/5),\; L_3' = L_3 + 5L_2} \begin{bmatrix} 1 & 2 & \mid & -1 \\ 0 & 1 & \mid & -2 \\ 0 & 0 & \mid & 0 \end{bmatrix}.$$
Sistema compatível determinado: $a_2 = -2$ e $a_1 = -1 - 2(-2) = 3$.  
Resposta: **(a) $a_1 = 3$**; **(b) $a_2 = -2$**.

### `D03-E03` *(Caça ao Erro — Verificação incompleta de paralelismo)*
- **(a)** Como $\frac{4}{6} = \frac{-2}{-3} = \frac{2}{3}$, mas $\frac{6}{8} = \frac{3}{4} \neq \frac{2}{3}$, as três razões não são iguais. Logo $\vec{u}$ e $\vec{v}$ são **Não paralelos**.
- **(b) e (c)** Para $\vec{w} = (6, a, b) \parallel (4, -2, 6)$, o fator de escala é $m = \frac{6}{4} = \frac{3}{2}$:
  $$a = -2 \cdot \frac{3}{2} = \mathbf{-3}, \qquad b = 6 \cdot \frac{3}{2} = \mathbf{9}.$$

### `D03-E04` *(Colinearidade de 3 pontos)*
- **(a)** $\overrightarrow{AB} = (3, 6, 3)$ e $\overrightarrow{AC} = (-1, -2, -1)$. Como $\overrightarrow{AB} = -3\,\overrightarrow{AC}$ em todas as coordenadas, os pontos **São colineares**.
- **(b)** $\overrightarrow{PQ} = (1, -2, 1)$ e $\overrightarrow{PR} = (-1, -1, 5)$. Como $\frac{1}{-1} = -1 \neq \frac{-2}{-1} = 2$, $\overrightarrow{PQ}$ e $\overrightarrow{PR}$ não são proporcionais; portanto os pontos **Não são colineares**.

### `D03-E05` *(Parâmetros de colinearidade)*
$\overrightarrow{AB} = B - A = (2, 4, -4)$ e $\overrightarrow{AC} = C - A = (a - 2,\; b + 1,\; -10)$.  
Impondo $\overrightarrow{AC} = k\,\overrightarrow{AB}$:
$$-10 = -4k \implies k = \frac{5}{2}.$$
Logo:
- **(a)** $a - 2 = 2\cdot\frac{5}{2} = 5 \implies \mathbf{a = 7}$.
- **(b)** $b + 1 = 4\cdot\frac{5}{2} = 10 \implies \mathbf{b = 9}$.

### `D03-E06` *(Combinação linear de 3 vetores)*
$c_1(1, 0, 1) + c_2(0, 1, 2) + c_3(1, -1, 0) = (1, 4, 8)$:
$$\begin{bmatrix} 1 & 0 & 1 & \mid & 1 \\ 0 & 1 & -1 & \mid & 4 \\ 1 & 2 & 0 & \mid & 8 \end{bmatrix} \xrightarrow{L_3' = L_3 - L_1} \begin{bmatrix} 1 & 0 & 1 & \mid & 1 \\ 0 & 1 & -1 & \mid & 4 \\ 0 & 2 & -1 & \mid & 7 \end{bmatrix} \xrightarrow{L_3' = L_3 - 2L_2} \begin{bmatrix} 1 & 0 & 1 & \mid & 1 \\ 0 & 1 & -1 & \mid & 4 \\ 0 & 0 & 1 & \mid & -1 \end{bmatrix}.$$
Por substituição regressiva: $c_3 = -1$, $c_2 = 4 + c_3 = 3$ e $c_1 = 1 - c_3 = 2$.  
Resposta: **$(2, 3, -1)$**.

---

## 2. Gabarito da Checagem Independente (`D03-C01` a `D03-C03`)

### `D03-C01`
$$\begin{bmatrix} 1 & 2 & \mid & 5 \\ -2 & 1 & \mid & -5 \\ 1 & -1 & \mid & 2 \end{bmatrix} \xrightarrow{L_2'=L_2+2L_1,\; L_3'=L_3-L_1} \begin{bmatrix} 1 & 2 & \mid & 5 \\ 0 & 5 & \mid & 5 \\ 0 & -3 & \mid & -3 \end{bmatrix} \xrightarrow{L_2(1/5),\; L_3'=L_3+3L_2} \begin{bmatrix} 1 & 2 & \mid & 5 \\ 0 & 1 & \mid & 1 \\ 0 & 0 & \mid & 0 \end{bmatrix}.$$
Logo $a_2 = 1$ e $a_1 = 5 - 2(1) = 3$. Resposta: **(a) $a_1 = 3$**; **(b) $a_2 = 1$**.

### `D03-C02`
Para $\vec{v} = k\vec{u}$, $k = \frac{9}{6} = \frac{3}{2}$. Assim:
- **(a)** $m = -4 \cdot \frac{3}{2} = \mathbf{-6}$.
- **(b)** $n = 10 \cdot \frac{3}{2} = \mathbf{15}$.

### `D03-C03`
$\overrightarrow{AB} = (2, -4, 4)$ e $\overrightarrow{AC} = (x - 1,\; y - 3,\; 10)$.  
Pela 3ª coordenada: $10 = 4k \implies k = \frac{5}{2}$.
- **(a)** $x - 1 = 2 \cdot \frac{5}{2} = 5 \implies \mathbf{x = 6}$.
- **(b)** $y - 3 = -4 \cdot \frac{5}{2} = -10 \implies \mathbf{y = -7}$.
