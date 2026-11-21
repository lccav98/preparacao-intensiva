# Gabarito Comentado — Bloco `E06` (Interseções: Dois Planos, Reta-Plano e Eixos/Planos Coordenados)

> **Bloco de referência:** [E06_bloco.md](../blocos/E06_bloco.md)

---

## 1. Exercícios

### `E06-E01` *(Reta interseção de dois planos)*
- **Passo a passo:**
  - `\pi_1: x + y + z = 6`, `\pi_2: x - y + z = 2`.
  - Subtraindo: `2y = 4 → y = 2`.
  - Substituindo em `\pi_1`: `x + 2 + z = 6 → x + z = 4`.
  - Seja `z = t`: `x = 4 - t`, `y = 2`, `z = t`.
- **Resposta Final:** `x = 4 - t, y = 2, z = t`
- **Alerta pedagógico:** Duas equações, três incógnitas → um parâmetro livre. Escolha uma variável como `t`.

---

### `E06-E02` *(Ponto reta-plano)*
- **Passo a passo:**
  - Substitua: `2(2+t) + (1-t) - (3+2t) = 4`.
  - `4 + 2t + 1 - t - 3 - 2t = 4`.
  - `2 - t = 4 → t = -2`.
  - Ponto: `x = 2 + (-2) = 0`, `y = 1 - (-2) = 3`, `z = 3 + 2(-2) = -1`.
  - Ponto `(0, 3, -1)`.
- **Resposta Final:** `(0, 3, -1)`
- **Alerta pedagógico:** Após encontrar `t`, substitua de volta nas três equações paramétricas.

---

### `E06-E03` *(Interceptos nos eixos)*
- **Passo a passo:**
  - Eixo `x` (`y=0, z=0`): `2x = 12 → x = 6`. Intercepto `(6, 0, 0)`.
  - Eixo `y` (`x=0, z=0`): `3y = 12 → y = 4`. Intercepto `(0, 4, 0)`.
  - Eixo `z` (`x=0, y=0`): `6z = 12 → z = 2`. Intercepto `(0, 0, 2)`.
- **Resposta Final:** `(6, 4, 2)`
- **Alerta pedagógico:** Para interceptar um eixo, ponha as outras duas coordenadas como zero.

---

### `E06-E04` *(Volume do tetraedro nos interceptos)*
- **Passo a passo:**
  - Interceptos: `x: x = 6`, `y: 2y = 6 → y = 3`, `z: 3z = 6 → z = 2`.
  - `V = \frac{1}{6}|6 \cdot 3 \cdot 2| = \frac{36}{6} = 6`.
- **Resposta Final:** `6`
- **Alerta pedagogico:** `V = |abc|/6` onde `a, b, c` são os interceptos nos eixos `x, y, z`.

---

### `E10-E05` *(Área do triângulo nos interceptos)*
- **Passo a passo:**
  - Equação `20x + 15y + 12z = 60`.
  - Interceptos: `x = 60/20 = 3`, `y = 60/15 = 4`, `z = 60/12 = 5`.
  - Pontos: `A(3, 0, 0)`, `B(0, 4, 0)`, `C(0, 0, 5)`.
  - `\overrightarrow{AB} = (-3, 4, 0)`, `\overrightarrow{AC} = (-3, 0, 5)`.
  - `\overrightarrow{AB}\times\overrightarrow{AC} = (4\cdot5 - 0\cdot0,\; 0(-3) - (-3)\cdot5,\; (-3)\cdot0 - 4(-3)) = (20, 15, 12)`.
  - `|...| = \sqrt{400 + 225 + 144} = \sqrt{769}`.
  - Área = `\frac{1}{2}\sqrt{769}`.
- **Resposta Final:** `sqrt(769)/2`
- **Alerta pedagogico:** A área do triângulo é metade do módulo do produto vetorial de dois lados.

---

## 2. Checagem Independente

### `E06-C01` *(Reta interseção com frações)*
- **Passo a passo:**
  - `\pi_1: 2x - y + z = 3`, `\pi_2: x + y - z = 1`.
  - Somando: `3x = 4 → x = 4/3`.
  - Substituindo em `\pi_2`: `4/3 + y - z = 1 → y - z = -1/3`.
  - Seja `z = t`: `y = t - 1/3`.
  - Reta: `x = 4/3`, `y = t - 1/3`, `z = t`.
- **Resposta Final:** `x = 4/3, y = t - 1/3, z = t`
- **Alerta pedagógico:** Quando somando as equações uma variável some, fica uma equação com duas incógnitas; escolha uma como parâmetro.

---

### `E06-C02` *(Ponto reta-plano com parâmetro)*
- **Passo a passo:**
  - Substitua: `(1-t) + 2(2+2t) + 3(3t) = 12`.
  - `1 - t + 4 + 4t + 9t = 12`.
  - `5 + 12t = 12 → 12t = 7 → t = 7/12`.
  - Ponto: `x = 1 - 7/12 = 5/12`, `y = 2 + 2(7/12) = 2 + 7/6 = 19/6`, `z = 3(7/12) = 7/4`.
- **Resposta Final:** `(5/12, 19/6, 7/4)`
- **Alerta pedagógico:** Mantenha frações irredutíveis; não converta para decimal.

---

### `E06-C03` *(Volume tetraedro + interceptos)*
- **Passo a passo:**
  - Interceptos: `x: 3x = 12 → x = 4`, `y: 4y = 12 → y = 3`, `z: 12z = 12 → z = 1`.
  - `V = \frac{1}{6}|4 \cdot 3 \cdot 1| = \frac{12}{6} = 2`.
- **Resposta Final:** `2`
- **Alerta pedagogico:** `V = |abc|/6 = |4 \cdot 3 \cdot 1|/6 = 12/6 = 2`.
