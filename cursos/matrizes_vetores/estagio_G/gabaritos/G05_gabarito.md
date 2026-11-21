# Gabarito Comentado — Bloco `G05` (Simulado Integrador P3 — Parte 2: Cônicas e Quádricas)

> **Bloco de referência:** [G05_bloco.md](../blocos/G05_bloco.md)

---

## 1. Exercícios

### `G05-E01` *(Parábola transladada por completamento de quadrados)*
- **Passo a passo:**
  - Completando o quadrado em $y$:
    $$y^2 - 6y = 8x - 17 \implies (y - 3)^2 - 9 = 8x - 17 \implies (y - 3)^2 = 8x - 8 = 8(x - 1).$$
  - Comparando com $(y - k)^2 = 2p(x - h)$:
    - **(a)** Vértice $V(1, 3)$, $2p = 8 \implies p = 4 \implies \frac{p}{2} = 2$ (concavidade para a direita, eixo paralelo a $x$).
    - **(b)** Foco: $F\left(h + \frac{p}{2},\; k\right) = (1 + 2,\; 3) = (3, 3)$.
    - **(c)** Reta diretriz: $x = h - \frac{p}{2} = 1 - 2 \implies x = -1$ (ou $x + 1 = 0$).
- **Resposta Final:** `(a) (1, 3) (b) (3, 3) (c) x = -1`
- **Alerta pedagógico:** A distância entre vértice e foco é $p/2 = 2$, não $p = 4$ nem $2p = 8$.

---

### `G05-E02` *(Elipse transladada — centro, excentricidade e focos)*
- **Passo a passo:**
  - Agrupando por variável e fatorando os coeficientes quadráticos:
    $$9(x^2 - 4x) + 25(y^2 + 6y) = -36$$
    $$9\big[(x - 2)^2 - 4\big] + 25\big[(y + 3)^2 - 9\big] = -36$$
    $$9(x - 2)^2 - 36 + 25(y + 3)^2 - 225 = -36 \implies 9(x - 2)^2 + 25(y + 3)^2 = 225.$$
  - Dividindo por $225$:
    $$\frac{(x - 2)^2}{25} + \frac{(y + 3)^2}{9} = 1.$$
  - **(a)** Centro: $C(2, -3)$.
  - **(b)** Como $a^2 = 25 \implies a = 5$ e $b^2 = 9 \implies b = 3$, temos $c = \sqrt{a^2 - b^2} = \sqrt{25 - 9} = 4$. Logo, $e = \frac{c}{a} = \frac{4}{5}$.
  - **(c)** Eixo maior paralelo a $x$: focos $F(2 \pm 4, -3)$, isto é, $(-2, -3)$ e $(6, -3)$.
- **Resposta Final:** `(a) (2, -3) (b) 4/5 (c) [(-2, -3), (6, -3)]`
- **Alerta pedagógico:** Ao completar o quadrado dentro de $25(y^2 + 6y)$, lembre de multiplicar o termo compensatório $-9$ por $25$ ($-225$).

---

### `G05-E03` *(Hipérbole transladada com lado direito negativo)*
- **Passo a passo:**
  - Completando quadrados:
    $$9(x^2 - 6x) - 4(y^2 - 2y) = -113$$
    $$9\big[(x - 3)^2 - 9\big] - 4\big[(y - 1)^2 - 1\big] = -113$$
    $$9(x - 3)^2 - 81 - 4(y - 1)^2 + 4 = -113 \implies 9(x - 3)^2 - 4(y - 1)^2 = -36.$$
  - Dividindo ambos os membros por $-36$:
    $$\frac{(y - 1)^2}{9} - \frac{(x - 3)^2}{4} = 1.$$
  - **(a)** Equação reduzida: $\frac{(y - 1)^2}{9} - \frac{(x - 3)^2}{4} = 1$.
  - **(b)** Centro $(3, 1)$, eixo real paralelo a $y$, $a = 3$, $b = 2$. Vértices reais: $(3, 1 \pm 3)$, ou seja, $(3, 4)$ e $(3, -2)$.
  - **(c)** $c = \sqrt{a^2 + b^2} = \sqrt{9 + 4} = \sqrt{13} \implies e = \frac{\sqrt{13}}{3}$.
- **Resposta Final:** `(a) (y-1)^2/9 - (x-3)^2/4 = 1 (b) [(3, 4), (3, -2)] (c) sqrt(13)/3`
- **Alerta pedagógico:** Dois erros fatais aqui seriam esquecer o sinal negativo de $-4(-1) = +4$ e não inverter o eixo real ao dividir por $-36$.

---

### `G05-E04` *(Classificação de superfícies quádricas por sinais e traços `[INF/AUS]`)*
- **Passo a passo:**
  - **(a)** $\frac{x^2}{4} + \frac{y^2}{9} - \frac{z^2}{16} = 1$: dois termos quadráticos positivos e um negativo igual a $1$; traços $z=k$ são elipses para todo $k \in \mathbb{R}$, e traços em $x=0$ e $y=0$ são hipérboles $\Rightarrow$ **hiperboloide de uma folha**.
  - **(b)** $\frac{x^2}{9} - \frac{y^2}{4} - \frac{z^2}{16} = 1$: um termo quadrático positivo e dois negativos igual a $1$; cortes $x=k$ só existem para $|k| \ge 3$ (superfície desconexa em duas folhas) $\Rightarrow$ **hiperboloide de duas folhas**.
  - **(c)** $z = \frac{x^2}{4} - \frac{y^2}{9}$: uma variável linear e duas quadráticas com sinais opostos; cortes $z=k \neq 0$ são hipérboles e cortes $x=k, y=k$ são parábolas de concavidades opostas $\Rightarrow$ **paraboloide hiperbólico**.
- **Resposta Final:** `(a) hiperboloide de uma folha (b) hiperboloide de duas folhas (c) paraboloide hiperbolico`
- **Alerta pedagógico:** Conte os sinais negativos quando o termo constante do lado direito for $+1$: $0$ negativos $\to$ elipsoide; $1$ negativo $\to$ hiperboloide de 1 folha; $2$ negativos $\to$ hiperboloide de 2 folhas.

---

### `G05-E05` *(Quádricas mistas e parábola por 3 pontos)*
- **Passo a passo:**
  - **(a)** Dividindo por $36$: $\frac{x^2}{36} + \frac{y^2}{9} + \frac{z^2}{4} = 1$ (todos os sinais positivos) $\Rightarrow$ **elipsoide**.
  - **(b)** $z^2 = \frac{x^2}{4} + \frac{y^2}{9} \iff \frac{x^2}{4} + \frac{y^2}{9} - z^2 = 0$ (homogênea de grau 2 com dois sinais positivos e um negativo) $\Rightarrow$ **cone elíptico**.
  - **(c)** Substituindo os pontos em $y = ax^2 + bx + c$:
    - $(0, 1) \implies c = 1$.
    - $(1, 0) \implies a + b + 1 = 0 \implies a + b = -1$.
    - $(2, 3) \implies 4a + 2b + 1 = 3 \implies 2a + b = 1$.
    Subtraindo as duas últimas: $a = 2$, e logo $b = -1 - 2 = -3$.
    Equação: $y = 2x^2 - 3x + 1$.
- **Resposta Final:** `(a) elipsoide (b) cone eliptico (c) y = 2*x^2 - 3*x + 1`
- **Alerta pedagógico:** Não confunda $z^2 = \frac{x^2}{4} + \frac{y^2}{9}$ (cone elíptico) com $z = \frac{x^2}{4} + \frac{y^2}{9}$ (paraboloide elíptico).

---

## 2. Checagem Independente

### `G05-C01` *(Elipse transladada sem consulta)*
- **Passo a passo:**
  - Completando quadrados:
    $$4(x^2 + 4x) + (y^2 - 6y) = -9 \implies 4\big[(x + 2)^2 - 4\big] + \big[(y - 3)^2 - 9\big] = -9$$
    $$4(x + 2)^2 - 16 + (y - 3)^2 - 9 = -9 \implies 4(x + 2)^2 + (y - 3)^2 = 16.$$
    Dividindo por $16$:
    $$\frac{(x + 2)^2}{4} + \frac{(y - 3)^2}{16} = 1.$$
  - **(a)** Centro: $C(-2, 3)$.
  - **(b)** Como $a^2 = 16 \implies a = 4$ e $b^2 = 4 \implies b = 2$, temos $c = \sqrt{16 - 4} = \sqrt{12} = 2\sqrt{3}$.
    Excentricidade: $e = \frac{2\sqrt{3}}{4} = \frac{\sqrt{3}}{2}$.
- **Resposta Final:** `(a) (-2, 3) (b) sqrt(3)/2`
- **Alerta pedagógico:** O maior denominador ($16 > 4$) está sob $(y - 3)^2$, logo $a = 4$ (eixo maior vertical).

---

### `G05-C02` *(Hipérbole transladada com inversão de sinal sem consulta)*
- **Passo a passo:**
  - Completando quadrados:
    $$4(x^2 - 2x) - 9(y^2 - 4y) = -4 \implies 4\big[(x - 1)^2 - 1\big] - 9\big[(y - 2)^2 - 4\big] = -4$$
    $$4(x - 1)^2 - 4 - 9(y - 2)^2 + 36 = -4 \implies 4(x - 1)^2 - 9(y - 2)^2 = -36.$$
  - **(a)** Dividindo por $-36$:
    $$\frac{(y - 2)^2}{4} - \frac{(x - 1)^2}{9} = 1.$$
  - **(b)** Eixo real paralelo a $y$: $a^2 = 4 \implies a = 2$, $b^2 = 9 \implies b = 3$, $c = \sqrt{4 + 9} = \sqrt{13}$.
    Excentricidade: $e = \frac{\sqrt{13}}{2}$.
- **Resposta Final:** `(a) (y-2)^2/4 - (x-1)^2/9 = 1 (b) sqrt(13)/2`
- **Alerta pedagógico:** Mesmo que $9 > 4$, na hipérbole $a^2$ é o denominador do termo **positivo** ($a^2 = 4$), nunca o maior denominador!

---

### `G05-C03` *(Classificação de quádricas por traços `[INF/AUS]` sem consulta)*
- **Passo a passo:**
  - **(a)** $z = \frac{x^2}{9} + \frac{y^2}{4}$: traços $z = k > 0$ são elipses, traços $x = 0$ e $y = 0$ são parábolas voltadas para $+z$ $\Rightarrow$ **paraboloide elíptico**.
  - **(b)** $\frac{x^2}{4} + \frac{y^2}{9} = 1$ no $\mathbb{R}^3$: a variável $z$ está ausente (livre para todo $z \in \mathbb{R}$) e a seção transversal é uma elipse $\Rightarrow$ **cilindro elíptico**.
  - **(c)** $x^2 - y^2 - z^2 = 1$: um quadrado positivo e dois negativos igualados a $+1$ $\Rightarrow$ **hiperboloide de duas folhas**.
- **Resposta Final:** `(a) paraboloide eliptico (b) cilindro eliptico (c) hiperboloide de duas folhas`
- **Alerta pedagógico:** No $\mathbb{R}^3$, uma equação de cônica em apenas duas variáveis (como $\frac{x^2}{4} + \frac{y^2}{9} = 1$) representa uma superfície cilíndrica estendida ao longo do eixo da variável ausente ($z$).
