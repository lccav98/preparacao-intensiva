# Gabarito Comentado — Bloco `G04` (Simulado Integrador P3 — Parte 1: Retas, Planos e Distâncias)

> **Bloco de referência:** [G04_bloco.md](../blocos/G04_bloco.md)

---

## 1. Exercícios

### `G04-E01` *(Equações da reta e reta ortogonal a duas retas)*
- **Passo a passo:**
  - **(a)** Vetor diretor: $\overrightarrow{AB} = (3-1,\; 6-2,\; 3-(-1)) = (2, 4, 4) \parallel (1, 2, 2)$.
    Pelas simétricas usando $A(1, 2, -1)$:
    $$\frac{x - 1}{1} = \frac{y - 2}{2} = \frac{z + 1}{2} \implies \begin{cases} y - 2 = 2(x - 1) \implies y = 2x \\ z + 1 = 2(x - 1) \implies z = 2x - 3 \end{cases}.$$
  - **(b)** Vetor diretor ortogonal a $\vec{v}_1$ e $\vec{v}_2$ (desenvolvendo pela 1ª linha):
    $$\vec{v}_s = \vec{v}_1 \times \vec{v}_2 = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ 1 & -1 & 2 \\ 2 & 1 & -1 \end{vmatrix} = (1 - 2)\hat{\imath} - (-1 - 4)\hat{\jmath} + (1 + 2)\hat{k} = (-1, 5, 3).$$
    Passando por $O(0, 0, 0)$: $(x, y, z) = (0, 0, 0) + t(-1, 5, 3)$.
- **Resposta Final:** `(a) y = 2x, z = 2x - 3 (b) (x, y, z) = (0, 0, 0) + t(-1, 5, 3)`
- **Alerta pedagógico:** Na forma reduzida em $x$, confira substituindo os dois pontos $A$ e $B$ em $y = 2x$ e $z = 2x - 3$.

---

### `G04-E02` *(Posição relativa de duas retas e interseção)*
- **Passo a passo:**
  - **(a)** Diretores $\vec{v}_1 = (1, -1, 2)$ e $\vec{v}_2 = (-1, 2, -1)$ não são paralelos.
    Igualando as coordenadas para testar interseção:
    $$\begin{cases} 1 + t = 3 - s \implies t + s = 2 \\ 2 - t = -1 + 2s \implies t + 2s = 3 \\ 3 + 2t = 6 - s \implies 2t + s = 3 \end{cases}$$
    Subtraindo a 1ª da 2ª: $s = 1 \implies t = 1$. Conferindo na 3ª: $2(1) + 1 = 3$ (satisfeita!).
    Logo, as retas são **concorrentes**.
  - **(b)** Substituindo $t = 1$ em $r_1$ (ou $s = 1$ em $r_2$):
    $$P = (1 + 1,\; 2 - 1,\; 3 + 2(1)) = (2, 1, 5).$$
- **Resposta Final:** `(a) concorrentes (b) (2, 1, 5)`
- **Alerta pedagógico:** Em $\mathbb{R}^3$, é obrigatório conferir a 3ª equação ao encontrar $(t, s)$ nas duas primeiras; se falhar, as retas seriam reversas.

---

### `G04-E03` *(Equação geral do plano por 3 pontos e ângulo reta-plano)*
- **Passo a passo:**
  - **(a)** $\overrightarrow{AB} = (1, 1, 0)$ e $\overrightarrow{AC} = (-1, 1, 1)$.
    Vetor normal:
    $$\vec{n} = \overrightarrow{AB} \times \overrightarrow{AC} = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ 1 & 1 & 0 \\ -1 & 1 & 1 \end{vmatrix} = (1 - 0)\hat{\imath} - (1 - 0)\hat{\jmath} + (1 + 1)\hat{k} = (1, -1, 2).$$
    Substituindo $A(1, 0, 1)$ em $x - y + 2z + d = 0$: $1 - 0 + 2 + d = 0 \implies d = -3$.
    Logo, $\pi: x - y + 2z - 3 = 0$.
  - **(b)** Com $\vec{v} = (1, 2, 2)$ e $\vec{n} = (1, -1, 2)$:
    $$\sin\phi = \frac{|\vec{v}\cdot\vec{n}|}{|\vec{v}|\,|\vec{n}|} = \frac{|1(1) + 2(-1) + 2(2)|}{\sqrt{1+4+4}\sqrt{1+1+4}} = \frac{3}{3\sqrt{6}} = \frac{1}{\sqrt{6}} = \frac{\sqrt{6}}{6}.$$
- **Resposta Final:** `(a) x - y + 2z - 3 = 0 (b) sqrt(6)/6`
- **Alerta pedagógico:** Ângulo entre reta e plano usa **seno** ($\sin\phi$), nunca cosseno.

---

### `G04-E04` *(Interseção de dois planos e volume pelos interceptos)*
- **Passo a passo:**
  - **(a)** Somando $\pi_1$ e $\pi_2$:
    $$(x + y - z) + (2x - y + z) = 2 + 4 \implies 3x = 6 \implies x = 2.$$
    Substituindo $x = 2$ em $\pi_1$: $2 + y - z = 2 \implies y = z$. Fazendo $z = t$:
    $$r: \begin{cases} x = 2 \\ y = t \\ z = t \end{cases}.$$
  - **(b)** Interceptos de $\alpha: 2x + 3y + 6z = 12$ nos eixos coordenados:
    - Eixo $x$ ($y=z=0$): $2x = 12 \implies x = 6$.
    - Eixo $y$ ($x=z=0$): $3y = 12 \implies y = 4$.
    - Eixo $z$ ($x=y=0$): $6z = 12 \implies z = 2$.
    Volume do tetraedro retângulo na origem:
    $$V = \frac{1}{6}(6 \cdot 4 \cdot 2) = 8.$$
- **Resposta Final:** `(a) x = 2, y = t, z = t (b) 8`
- **Alerta pedagógico:** Na interseção de planos, quando uma variável fica constante ($x = 2$), sua coordenada no vetor diretor é $0$: $\vec{v} = (0, 1, 1)$.

---

### `G04-E05` *(Distância entre retas reversas e entre planos paralelos)*
- **Passo a passo:**
  - **(a)** Temos $P_1(1, 0, 1)$, $\vec{u} = (1, 1, 0)$, $P_2(0, 1, 2)$, $\vec{v} = (0, 1, 1)$, $\overrightarrow{P_1P_2} = (-1, 1, 1)$.
    $$\vec{u}\times\vec{v} = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{vmatrix} = (1, -1, 1) \implies |\vec{u}\times\vec{v}| = \sqrt{3}.$$
    Produto misto: $(\vec{u}, \vec{v}, \overrightarrow{P_1P_2}) = \overrightarrow{P_1P_2}\cdot(\vec{u}\times\vec{v}) = (-1)(1) + 1(-1) + 1(1) = -1$.
    Logo:
    $$d(r_1, r_2) = \frac{|-1|}{\sqrt{3}} = \frac{\sqrt{3}}{3}.$$
  - **(b)** Dividindo $\pi_2$ por $2$: $\pi_2: 2x - y + 2z + 6 = 0$.
    Comparando com $\pi_1: 2x - y + 2z - 3 = 0$ (mesmo vetor normal $(2, -1, 2)$):
    $$d(\pi_1, \pi_2) = \frac{|6 - (-3)|}{\sqrt{2^2 + (-1)^2 + 2^2}} = \frac{9}{3} = 3.$$
- **Resposta Final:** `(a) sqrt(3)/3 (b) 3`
- **Alerta pedagógico:** Se esquecer de dividir $\pi_2$ por $2$, obtém-se $|12 - (-3)|/3 = 5$ (errado!).

---

## 2. Checagem Independente

### `G04-C01` *(Plano por ponto e reta + interseção reta-plano)*
- **Passo a passo:**
  - **(a)** Da reta $r$, extraímos o ponto $P_0(1, 0, -1)$ e o vetor diretor $\vec{v} = (2, 1, 1)$.
    Vetor $\overrightarrow{PP_0} = (0, -2, -1)$.
    Normal do plano:
    $$\vec{n} = \overrightarrow{PP_0} \times \vec{v} = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ 0 & -2 & -1 \\ 2 & 1 & 1 \end{vmatrix} = (-2 + 1)\hat{\imath} - (0 + 2)\hat{\jmath} + (0 + 4)\hat{k} = (-1, -2, 4).$$
    Usando $P(1, 2, 0)$ em $-x - 2y + 4z + d = 0$: $-1 - 4 + 0 + d = 0 \implies d = 5$.
    Logo, $-x - 2y + 4z + 5 = 0$ (equivalente a $x + 2y - 4z - 5 = 0$).
  - **(b)** Substituindo $s$ em $\beta: 2x + y - z = 10$:
    $$2(2 + t) + (1 - t) - (-1 + 2t) = 10 \implies 4 + 2t + 1 - t + 1 - 2t = 10 \implies 6 - t = 10 \implies t = -4.$$
    Logo, o ponto é $I = (2 - 4,\; 1 - (-4),\; -1 + 2(-4)) = (-2, 5, -9)$.
- **Resposta Final:** `(a) x + 2y - 4z - 5 = 0 (b) (-2, 5, -9)`
- **Alerta pedagógico:** Confira o ponto de interseção em $\beta$: $2(-2) + 5 - (-9) = -4 + 5 + 9 = 10$.

---

### `G04-C02` *(Distância entre retas reversas sem consulta)*
- **Passo a passo:**
  - $P_1(1, 0, -1)$, $\vec{u} = (1, 2, 1)$; $P_2(2, 1, 0)$, $\vec{v} = (-1, 1, 2)$; $\overrightarrow{P_1P_2} = (1, 1, 1)$.
  - $\vec{u}\times\vec{v} = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ 1 & 2 & 1 \\ -1 & 1 & 2 \end{vmatrix} = (4 - 1)\hat{\imath} - (2 + 1)\hat{\jmath} + (1 + 2)\hat{k} = (3, -3, 3)$.
  - $|\vec{u}\times\vec{v}| = \sqrt{9 + 9 + 9} = 3\sqrt{3}$.
  - Produto misto: $\overrightarrow{P_1P_2}\cdot(\vec{u}\times\vec{v}) = 1(3) + 1(-3) + 1(3) = 3$.
  - Distância:
    $$d(r_1, r_2) = \frac{|3|}{3\sqrt{3}} = \frac{1}{\sqrt{3}} = \frac{\sqrt{3}}{3}.$$
- **Resposta Final:** `sqrt(3)/3`
- **Alerta pedagógico:** Como $\vec{u}\times\vec{v} = (3, -3, 3) \neq \vec{0}$ e $(\vec{u},\vec{v},\overrightarrow{P_1P_2}) = 3 \neq 0$, confirma-se que são reversas.

---

### `G04-C03` *(Distância entre planos paralelos e distância ponto-reta)*
- **Passo a passo:**
  - **(a)** Dividindo $\pi_2: -3x - 6y + 6z + 15 = 0$ por $-3$:
    $$\pi_2: x + 2y - 2z - 5 = 0.$$
    Com $\pi_1: x + 2y - 2z + 4 = 0$:
    $$d(\pi_1, \pi_2) = \frac{|4 - (-5)|}{\sqrt{1^2 + 2^2 + (-2)^2}} = \frac{9}{3} = 3.$$
  - **(b)** Com $P_0(1, 0, 1)$, $Q(3, 1, -2)$ e $\vec{v} = (2, 1, -2)$, temos $\overrightarrow{P_0Q} = (2, 1, -3)$.
    $$\vec{v} \times \overrightarrow{P_0Q} = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ 2 & 1 & -2 \\ 2 & 1 & -3 \end{vmatrix} = (-3 + 2)\hat{\imath} - (-6 + 4)\hat{\jmath} + (2 - 2)\hat{k} = (-1, 2, 0).$$
    Como $|\vec{v}\times\overrightarrow{P_0Q}| = \sqrt{1 + 4 + 0} = \sqrt{5}$ e $|\vec{v}| = \sqrt{4 + 1 + 4} = 3$:
    $$d(Q, r) = \frac{\sqrt{5}}{3}.$$
- **Resposta Final:** `(a) 3 (b) sqrt(5)/3`
- **Alerta pedagógico:** Na distância entre planos paralelos, o sinal negativo na multiplicação de $\pi_2$ exigiu divisão por $-3$ (não apenas por $3$) para igualar $(1, 2, -2)$.
