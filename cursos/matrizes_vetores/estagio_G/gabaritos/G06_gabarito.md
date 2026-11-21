# Gabarito Comentado — Bloco `G06` (Simulado Geral Completo `MAT121` — Preparação Reavaliação)

> **Bloco de referência:** [G06_bloco.md](../blocos/G06_bloco.md)

---

## 1. Exercícios

### `G06-E01` *(P1 — Singularidade por cofatores e equação matricial `AX^T = B`)*
- **Passo a passo:**
  - **(a)** Desenvolvendo $\det(M)$ pela **2ª coluna** (dois zeros):
    $$\det(M) = (-1)^{2+2}(k - 1)\begin{vmatrix} k & 1 \\ 4 & k \end{vmatrix} = (k - 1)(k^2 - 4) = (k - 1)(k - 2)(k + 2) = 0.$$
    Logo, $k \in \{-2,\; 1,\; 2\}$.
  - **(b)** Invertendo $A$ via $[A \mid I_2]$:
    $$\left[\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 3 & 4 & 0 & 1 \end{array}\right] \xrightarrow{L_2' = L_2 - 3L_1} \left[\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 0 & -2 & -3 & 1 \end{array}\right] \xrightarrow{L_2(-1/2)} \left[\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 0 & 1 & 3/2 & -1/2 \end{array}\right]$$
    $$\xrightarrow{L_1' = L_1 - 2L_2} \left[\begin{array}{cc|cc} 1 & 0 & -2 & 1 \\ 0 & 1 & 3/2 & -1/2 \end{array}\right] \implies A^{-1} = \begin{bmatrix} -2 & 1 \\ 3/2 & -1/2 \end{bmatrix}.$$
    Calculando $X^T = A^{-1}B$:
    $$X^T = \begin{bmatrix} -2 & 1 \\ 3/2 & -1/2 \end{bmatrix}\begin{bmatrix} 2 & 0 \\ -1 & 4 \end{bmatrix} = \begin{bmatrix} -5 & 4 \\ 7/2 & -2 \end{bmatrix}.$$
    Transpondo para obter $X$:
    $$X = \begin{bmatrix} -5 & 7/2 \\ 4 & -2 \end{bmatrix}.$$
- **Resposta Final:** `(a) -2, 1, 2 (b) [[-5, 7/2], [4, -2]]`
- **Alerta pedagógico:** Lembre-se de transpor $X^T$ no último passo; caso contrário, $7/2$ e $4$ ficam trocados de posição.

---

### `G06-E02` *(P2 Parte 1 — Homogêneo com parâmetro e sistema escalonado)*
- **Passo a passo:**
  - **(a)** Escalonando a matriz dos coeficientes:
    $$\begin{bmatrix} 1 & 1 & 2 \\ 2 & 3 & 5 \\ 1 & 2 & k \end{bmatrix} \xrightarrow{\substack{L_2' = L_2 - 2L_1 \\ L_3' = L_3 - L_1}} \begin{bmatrix} 1 & 1 & 2 \\ 0 & 1 & 1 \\ 0 & 1 & k - 2 \end{bmatrix} \xrightarrow{L_3' = L_3 - L_2} \begin{bmatrix} 1 & 1 & 2 \\ 0 & 1 & 1 \\ 0 & 0 & k - 3 \end{bmatrix}.$$
    Para admitir soluções próprias ($C < 3$), é necessário $k - 3 = 0 \implies k = 3$.
  - **(b)** Escalonando o segundo sistema:
    $$\left[\begin{array}{ccc|c} 1 & 1 & -1 & 1 \\ 2 & 3 & 1 & 7 \\ 1 & 1 & 1 & 5 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 - 2L_1 \\ L_3' = L_3 - L_1}} \left[\begin{array}{ccc|c} 1 & 1 & -1 & 1 \\ 0 & 1 & 3 & 5 \\ 0 & 0 & 2 & 4 \end{array}\right] \xrightarrow{L_3(1/2)} \left[\begin{array}{ccc|c} 1 & 1 & -1 & 1 \\ 0 & 1 & 3 & 5 \\ 0 & 0 & 1 & 2 \end{array}\right].$$
    Logo, $C_A = 3$, $C_V = 3$, $g = 3 - 3 = 0$ (`SPD`).
    Por substituição regressiva: $z = 2$; $y = 5 - 3(2) = -1$; $x = 1 - (-1) + 2 = 4$.
- **Resposta Final:** `(a) 3 (b) ca: 3; cv: 3; g: 0; classificacao: SPD; solucao: (4, -1, 2)`
- **Alerta pedagógico:** Conferência rápida no item (b): $4 + (-1) + 2 = 5$ e $2(4) + 3(-1) + 2 = 7$.

---

### `G06-E03` *(P2 Parte 2 — Área do triângulo `1/2` e volume do tetraedro `1/6`)*
- **Passo a passo:**
  - Vetores partindo de $A(1, 0, 1)$:
    $$\overrightarrow{AB} = (2, 2, 0), \qquad \overrightarrow{AC} = (0, 2, 2), \qquad \overrightarrow{AD} = (1, 1, 3).$$
  - **(a)** Produto vetorial pela 1ª linha:
    $$\overrightarrow{AB}\times\overrightarrow{AC} = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ 2 & 2 & 0 \\ 0 & 2 & 2 \end{vmatrix} = (4 - 0)\hat{\imath} - (4 - 0)\hat{\jmath} + (4 - 0)\hat{k} = (4, -4, 4).$$
    Módulo: $|\overrightarrow{AB}\times\overrightarrow{AC}| = \sqrt{16 + 16 + 16} = \sqrt{48} = 4\sqrt{3}$.
    Área do triângulo $ABC$:
    $$A_{\triangle} = \frac{1}{2}(4\sqrt{3}) = 2\sqrt{3}.$$
  - **(b)** Produto misto:
    $$(\overrightarrow{AB}, \overrightarrow{AC}, \overrightarrow{AD}) = \overrightarrow{AD}\cdot(\overrightarrow{AB}\times\overrightarrow{AC}) = 1(4) + 1(-4) + 3(4) = 12.$$
    Volume do tetraedro $ABCD$:
    $$V_{\text{tetra}} = \frac{1}{6}|12| = 2.$$
- **Resposta Final:** `(a) 2*sqrt(3) (b) 2`
- **Alerta pedagógico:** Aproveite $\overrightarrow{AB}\times\overrightarrow{AC}$ do item (a) para calcular $(\overrightarrow{AB}, \overrightarrow{AC}, \overrightarrow{AD}) = \overrightarrow{AD}\cdot(\overrightarrow{AB}\times\overrightarrow{AC})$ diretamente no item (b), sem esquecer o fator $\frac{1}{6}$.

---

### `G06-E04` *(P3 Parte 1 — Plano paralelo e distância entre planos paralelos)*
- **Passo a passo:**
  - **(a)** Como $\pi \parallel \alpha$, podemos usar o mesmo vetor normal $\vec{n} = (2, -1, 2)$:
    $$2x - y + 2z + d = 0.$$
    Substituindo $P(1, -1, 2)$: $2(1) - (-1) + 2(2) + d = 0 \implies 7 + d = 0 \implies d = -7$.
    Logo, $\pi: 2x - y + 2z - 7 = 0$.
  - **(b)** Com o mesmo vetor normal $(2, -1, 2)$ em $\pi$ e $\alpha: 2x - y + 2z - 5 = 0$:
    $$d(\pi, \alpha) = \frac{|-7 - (-5)|}{\sqrt{2^2 + (-1)^2 + 2^2}} = \frac{2}{3}.$$
- **Resposta Final:** `(a) 2x - y + 2z - 7 = 0 (b) 2/3`
- **Alerta pedagógico:** Conferência alternativa de (b): calcule diretamente $d(P, \alpha) = \frac{|2(1) - (-1) + 2(2) - 5|}{3} = \frac{2}{3}$.

---

### `G06-E05` *(P3 Parte 2 — Cônica transladada e quádrica canônica `[INF/AUS]`)*
- **Passo a passo:**
  - **(a)** Completando quadrados em $x^2 + 4y^2 - 6x + 16y + 21 = 0$:
    $$(x^2 - 6x) + 4(y^2 + 4y) = -21$$
    $$\big[(x - 3)^2 - 9\big] + 4\big[(y + 2)^2 - 4\big] = -21$$
    $$(x - 3)^2 - 9 + 4(y + 2)^2 - 16 = -21 \implies (x - 3)^2 + 4(y + 2)^2 = 4.$$
    Dividindo por $4$:
    $$\frac{(x - 3)^2}{4} + (y + 2)^2 = 1 \quad (\text{elipse de centro } (3, -2)).$$
  - **(b)** Em $\frac{x^2}{4} - \frac{y^2}{9} + \frac{z^2}{16} = 1$, há dois sinais positivos e um negativo igualados a $1$; os cortes $y = k$ são elipses para qualquer $k \in \mathbb{R}$, logo trata-se de um **hiperboloide de uma folha**.
- **Resposta Final:** `(a) (x-3)^2/4 + (y+2)^2 = 1 (b) hiperboloide de uma folha`
- **Alerta pedagógico:** Mesmo que o termo negativo esteja em $y$ (e não em $z$), o critério de 1 sinal negativo com lado direito $+1$ continua identificando o **hiperboloide de uma folha** (agora ao longo do eixo $y$).

---

## 2. Checagem Independente

### `G06-C01` *(Integração P1 + P2 — Inversa `[A | I_3]` aplicada a `AX = B`)*
- **Passo a passo:**
  - **(a)** Escalonamento de $[A \mid I_3]$:
    $$\left[\begin{array}{ccc|ccc} 1 & 0 & 2 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 1 & 1 & 4 & 0 & 0 & 1 \end{array}\right] \xrightarrow{L_3' = L_3 - L_1} \left[\begin{array}{ccc|ccc} 1 & 0 & 2 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & 1 & 2 & -1 & 0 & 1 \end{array}\right]$$
    $$\xrightarrow{L_3' = L_3 - L_2} \left[\begin{array}{ccc|ccc} 1 & 0 & 2 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & 0 & 1 & -1 & -1 & 1 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 - L_3 \\ L_1' = L_1 - 2L_3}} \left[\begin{array}{ccc|ccc} 1 & 0 & 0 & 3 & 2 & -2 \\ 0 & 1 & 0 & 1 & 2 & -1 \\ 0 & 0 & 1 & -1 & -1 & 1 \end{array}\right].$$
    Logo, $A^{-1} = \begin{bmatrix} 3 & 2 & -2 \\ 1 & 2 & -1 \\ -1 & -1 & 1 \end{bmatrix}$.
  - **(b)** Calculando $X = A^{-1}B$:
    $$X = \begin{bmatrix} 3 & 2 & -2 \\ 1 & 2 & -1 \\ -1 & -1 & 1 \end{bmatrix}\begin{bmatrix} 5 \\ 2 \\ 9 \end{bmatrix} = \begin{bmatrix} 15 + 4 - 18 \\ 5 + 4 - 9 \\ -5 - 2 + 9 \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix}.$$
- **Resposta Final:** `(a) [[3, 2, -2], [1, 2, -1], [-1, -1, 1]] (b) (1, 0, 2)`
- **Alerta pedagógico:** Conferência: $1 + 2(2) = 5$, $0 + 2 = 2$ e $1 + 0 + 4(2) = 9$.

---

### `G06-C02` *(Integração P2 + P3 Parte 1 — Plano por 3 pontos e distância ponto-plano)*
- **Passo a passo:**
  - **(a)** $\overrightarrow{AB} = (2, 0, 2)$ e $\overrightarrow{AC} = (0, 2, 2)$.
    Vetor normal pela 1ª linha:
    $$\vec{n} = \overrightarrow{AB} \times \overrightarrow{AC} = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ 2 & 0 & 2 \\ 0 & 2 & 2 \end{vmatrix} = (0 - 4)\hat{\imath} - (4 - 0)\hat{\jmath} + (4 - 0)\hat{k} = (-4, -4, 4).$$
    Simplificando por $-4$, podemos usar $\vec{n}_0 = (1, 1, -1)$: $x + y - z + d = 0$.
    Substituindo $A(1, 1, 0)$: $1 + 1 - 0 + d = 0 \implies d = -2$.
    Logo, $\pi: x + y - z - 2 = 0$.
  - **(b)** Distância de $P(4, 2, 3)$ ao plano $\pi$:
    $$d(P, \pi) = \frac{|4 + 2 - 3 - 2|}{\sqrt{1^2 + 1^2 + (-1)^2}} = \frac{1}{\sqrt{3}} = \frac{\sqrt{3}}{3}.$$
- **Resposta Final:** `(a) x + y - z - 2 = 0 (b) sqrt(3)/3`
- **Alerta pedagógico:** Se mantiver $\vec{n} = (-4, -4, 4)$, a equação $-4x - 4y + 4z + 8 = 0$ é equivalente e dá a mesma distância $\frac{4}{\sqrt{48}} = \frac{4}{4\sqrt{3}} = \frac{\sqrt{3}}{3}$.

---

### `G06-C03` *(Integração P3 Parte 2 — Cônica por completamento de quadrados e quádrica)*
- **Passo a passo:**
  - **(a)** Completando os quadrados em $4y^2 - x^2 - 8y - 4x - 4 = 0$:
    $$4(y^2 - 2y) - (x^2 + 4x) = 4$$
    $$4\big[(y - 1)^2 - 1\big] - \big[(x + 2)^2 - 4\big] = 4$$
    $$4(y - 1)^2 - 4 - (x + 2)^2 + 4 = 4 \implies 4(y - 1)^2 - (x + 2)^2 = 4.$$
    Dividindo por $4$:
    $$(y - 1)^2 - \frac{(x + 2)^2}{4} = 1.$$
    O centro é $(h, k) = (-2, 1)$ *(atenção à ordem $(x, y)$: $h = -2$ e $k = 1$!)*.
  - **(b)** Sinais opostos nos quadrados: **hipérbole**.
  - **(c)** Em $y = \frac{x^2}{4} - \frac{z^2}{9}$, temos uma variável linear ($y$) e duas quadráticas com sinais opostos $\Rightarrow$ **paraboloide hiperbólico**.
- **Resposta Final:** `(a) (-2, 1) (b) hiperbole (c) paraboloide hiperbolico`
- **Alerta pedagógico:** Cuidado para não inverter $(h, k)$ como $(1, -2)$ só porque $(y - 1)^2$ apareceu antes de $(x + 2)^2$ na equação.
