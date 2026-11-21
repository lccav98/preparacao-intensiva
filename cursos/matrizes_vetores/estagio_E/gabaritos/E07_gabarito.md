# Gabarito Comentado — Bloco `E07` (Distâncias Ponto-Ponto e Ponto-Reta)

> **Bloco de referência:** [E07_bloco.md](../blocos/E07_bloco.md)

---

## 1. Exercícios

### `E07-E01` *(Distância ponto-ponto)*
- **Passo a passo:**
  - `\overrightarrow{P_1P_2} = (4-1, 5-1, 9-1) = (3, 4, 8)`.
  - `d = \sqrt{9 + 16 + 64} = \sqrt{89}`.
- **Resposta Final:** `sqrt(89)`
- **Alerta pedagógico:** `89` é primo; não simplifica.

---

### `E07-E02` *(Distância ponto-reta)*
- **Passo a passo:**
  - `P_1 = (0, 0, 0)`, `\vec{v} = (2, 1, 2)`, `\overrightarrow{P_1P_0} = (1, 2, 3)`.
  - `\vec{v}\times\overrightarrow{P_1P_0} = (1\cdot3 - 2\cdot2,\; 2\cdot1 - 2\cdot3,\; 2\cdot2 - 1\cdot1) = (3-4,\; 2-6,\; 4-1) = (-1, -4, 3)`.
  - `|...| = \sqrt{1 + 16 + 9} = \sqrt{26}`.
  - `|\vec{v}| = \sqrt{4 + 1 + 4} = 3`.
  - `d = \sqrt{26}/3`.
- **Resposta Final:** `sqrt(26)/3`
- **Alerta pedagógico:** `d = |\vec{v}\times\overrightarrow{P_1P_0}|/|\vec{v}|`, não esqueça de dividir pelo módulo do diretor.

---

### `E07-E03` *(Distância a um eixo coordenado)*
- **Passo a passo:**
  - Distância ao eixo `z`: `d = \sqrt{x^2 + y^2} = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = 5`.
- **Resposta Final:** `5`
- **Alerta pedagogico:** Ao eixo `z`, só importam as coordenadas `x` e `y` (a distância ao eixo é a distância ao ponto `(0, 0, z)`).

---

### `E07-E04` *(Distância ponto-reta com frações)*
- **Passo a passo:**
  - `P_1 = (1, 0, 0)`, `\vec{v} = (0, 1, 1)`, `\overrightarrow{P_1P_0} = (0, 1, 1)`.
  - `\vec{v}\times\overrightarrow{P_1P_0} = (0, 1, 1)\times(0, 1, 1) = (0, 0, 0)`.
  - `d = 0`. O ponto pertence à reta!
- **Resposta Final:** `0`
- **Alerta pedagógico:** Se o produto vetorial é zero, o ponto está na reta (distância nula).

---

### `E07-E05` *(Integração: ponto-reta + ponto-ponto)*
- **Passo a passo:**
  - **(a)** `d(P_1, P_2) = \sqrt{(3-0)^2 + (4-0)^2 + (0-0)^2} = \sqrt{9 + 16} = 5`.
  - **(b)** `P_0 = P_1 = (0, 0, 0)`, `P_1(reta) = (1, 1, 0)`, `\vec{v} = (1, -1, 0)`.
  - `\overrightarrow{P_1P_0} = (-1, -1, 0)`.
  - `(1, -1, 0)\times(-1, -1, 0) = (0, 0, -1-1) = (0, 0, -2)`. `|...| = 2`.
  - `|\vec{v}| = \sqrt{2}`.
  - `d = 2/\sqrt{2} = \sqrt{2}`.
- **Resposta Final:** `(a) 5 (b) sqrt(2)`
- **Alerta pedagógico:** Na parte (b), o ponto `P_1` é a origem `(0,0,0)`; cuidado para não confundir com o ponto de apoio da reta `(1,1,0)`.

---

## 2. Checagem Independente

### `E07-C01` *(Distância ponto-ponto com radical)*
- **Passo a passo:**
  - `\overrightarrow{P_1P_2} = (2-(-1), -1-2, -1-3) = (3, -3, -4)`.
  - `d = \sqrt{9 + 9 + 16} = \sqrt{34}`.
- **Resposta Final:** `sqrt(34)`
- **Alerta pedagógico:** `34` não tem fator quadrado; não simplifica.

---

### `E07-C02` *(Distância ponto-reta)*
- **Passo a passo:**
  - `P_1 = (0, 1, 0)`, `\vec{v} = (1, 0, 1)`, `\overrightarrow{P_1P_0} = (2, 0, -1)`.
  - `(1, 0, 1)\times(2, 0, -1) = (0(-1) - 1\cdot0,\; 1\cdot2 - 1(-1),\; 1\cdot0 - 0\cdot2) = (0, 3, 0)`.
  - `|...| = 3`, `|\vec{v}| = \sqrt{2}`.
  - `d = 3/\sqrt{2} = 3\sqrt{2}/2`.
- **Resposta Final:** `3sqrt(2)/2`
- **Alerta pedagógico:** Rationalize: `3/\sqrt{2} = 3\sqrt{2}/2`.

---

### `E07-C03` *(Distância ao eixo y)*
- **Passo a passo:**
  - Distância ao eixo `y`: `d = \sqrt{x^2 + z^2} = \sqrt{5^2 + 12^2} = \sqrt{25 + 144} = \sqrt{169} = 13`.
- **Resposta Final:** `13`
- **Alerta pedagogico:** Ao eixo `y`, só importam `x` e `z` (distância ao ponto `(0, y, 0)`).
