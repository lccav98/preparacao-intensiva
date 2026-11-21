# Gabarito Comentado — Bloco `E08` (Distância entre Duas Retas: Concorrentes, Paralelas e Reversas)

> **Bloco de referência:** [E08_bloco.md](../blocos/E08_bloco.md)

---

## 1. Exercícios

### `E08-E01` *(Verificar paralelismo primeiro)*
- **Passo a passo:**
  - `\vec{v}_1 = (2, 4, 6) = 2(1, 2, 3) = 2\vec{v}_2`. Proporcionais → **paralelas**.
- **Resposta Final:** `sim`
- **Alerta pedagógico:** Sempre teste paralelismo antes de escolher a fórmula de distância.

---

### `E08-E02` *(Distância entre retas paralelas)*
- **Passo a passo:**
  - `r_1: (0, 0, 0) + t(1, 0, 0)`, `r_2: (0, 1, 0) + s(1, 0, 0)`.
  - Ponto `P_0(0, 0, 0)` de `r_1`, reta `r_2` com `P_1(0, 1, 0)` e `\vec{v} = (1, 0, 0)`.
  - `\overrightarrow{P_1P_0} = (0, -1, 0)`.
  - `\vec{v}\times\overrightarrow{P_1P_0} = (1, 0, 0)\times(0, -1, 0) = (0, 0, -1)`. `|...| = 1`.
  - `|\vec{v}| = 1`.
  - `d = 1/1 = 1`.
- **Resposta Final:** `1`
- **Alerta pedagógico:** Para retas paralelas, a distância é a distância de um ponto de uma reta à outra reta.

---

### `E08-E03` *(Distância entre retas reversas — paralelepípedo)*
- **Passo a passo:**
  - `r_1: (0, 0, 0) + t(1, 0, 0)`, `r_2: (0, 1, 0) + s(0, 0, 1)`.
  - Diretores não proporcionais → não paralelas. Verificar coplanaridade: produto misto.
  - `\vec{u}\times\vec{v} = (1, 0, 0)\times(0, 0, 1) = (0, -1, 0)`. `|...| = 1`.
  - `\overrightarrow{P_1P_2} = (0, 1, 0)`.
  - Produto misto: `(1, 0, 0)\cdot((0, 0, 1)\times(0, 1, 0))`. `(0, 0, 1)\times(0, 1, 0) = (-1, 0, 0)`. `(1, 0, 0)\cdot(-1, 0, 0) = -1`. `|-1| = 1`.
  - `d = 1/1 = 1`.
- **Resposta Final:** `1`
- **Alerta pedagógico:** `d = |(\vec{u},\vec{v},\overrightarrow{P_1P_2})|/|\vec{u}\times\vec{v}|`. O valor absoluto remove o sinal.

---

### `E08-E04` *(Retas concorrentes → distância zero)*
- **Passo a passo:**
  - `r_1: (0, 0, 0) + t(1, 1, 0)`, `r_2: (2, 2, 0) + s(-1, -1, 0)`.
  - `r_2` passa por `(2, 2, 0)` com diretor `(-1, -1, 0) = -(1, 1, 0)` → paralelas a `r_1`. Mas `(2, 2, 0)` está em `r_1` (para `t = 2`) → coincidentes. Distância `0`.
  - Mesmo classificando como concorrentes (se intersectam), distância é `0`.
- **Resposta Final:** `0`
- **Alerta pedagógico:** Retas concorrentes (ou coincidentes) têm distância nula.

---

### `E10-E05` *(Integração: classificação + distância)*
- **Passo a passo:**
  - **(a)** `\vec{v}_1 = (0, 1, 0)`, `\vec{v}_2 = (0, 1, 0)` → iguais → **paralelas**.
  - **(b)** `r_1: (1, 0, 0) + t(0, 1, 0)`, `r_2: (0, 0, 1) + s(0, 1, 0)`.
  - Ponto `P_0(1, 0, 0)` de `r_1`, reta `r_2` com `P_1(0, 0, 1)` e `\vec{v} = (0, 1, 0)`.
  - `\overrightarrow{P_1P_0} = (1, 0, -1)`.
  - `\vec{v}\times\overrightarrow{P_1P_0} = (0, 1, 0)\times(1, 0, -1) = (-1, 0, -1)`. `|...| = \sqrt{2}`.
  - `|\vec{v}| = 1`.
  - `d = \sqrt{2}`.
- **Resposta Final:** `(a) sim (b) sqrt(2)`
- **Alerta pedagógico:** Mesmo sendo paralelas, as retas são distintas (diferentes pontos de apoio), então a distância não é zero.

---

## 2. Checagem Independente

### `E08-C01` *(Retas reverses com produto misto)*
- **Passo a passo:**
  - `r_1: (1, 2, 3) + t(1, 0, 0)`, `r_2: (4, 5, 6) + s(0, 1, 0)`.
  - `\vec{u}\times\vec{v} = (1, 0, 0)\times(0, 1, 0) = (0, 0, 1)`. `|...| = 1`.
  - `\overrightarrow{P_1P_2} = (3, 3, 3)`.
  - Produto misto: `(1, 0, 0)\cdot((0, 1, 0)\times(3, 3, 3))`. `(0, 1, 0)\times(3, 3, 3) = (3, 0, -3)`. `(1, 0, 0)\cdot(3, 0, -3) = 3`. `|3| = 3`.
  - `d = 3/1 = 3`.
- **Resposta Final:** `3`
- **Alerta pedagógico:** Verifique primeiro se são paralelas (não são) antes de usar a fórmula do paralelepípedo.

---

### `E08-C02` *(Retas paralelas com frações)*
- **Passo a passo:**
  - `r_1: (0, 0, 0) + t(2, 2, 0)`, `r_2: (1, 1, 1) + s(1, 1, 0)`.
  - `\vec{v} = (1, 1, 0)` (simplificado de `(2, 2, 0)`).
  - Ponto `P_0(0, 0, 0)` de `r_1`, `r_2` com `P_1(1, 1, 1)`.
  - `\overrightarrow{P_1P_0} = (-1, -1, -1)`.
  - `\vec{v}\times\overrightarrow{P_1P_0} = (1, 1, 0)\times(-1, -1, -1) = (-1, 1, 0)`. `|...| = \sqrt{2}`.
  - `|\vec{v}| = \sqrt{2}`.
  - `d = \sqrt{2}/\sqrt{2} = 1`.
- **Resposta Final:** `1`
- **Alerta pedagógico:** Simplifique o diretor antes de calcular; o resultado deve ser o mesmo.

---

### `E08-C03` *(Classificação e distância)*
- **Passo a passo:**
  - **(a)** `\vec{v}_2 = (-1, -2, -3) = -(1, 2, 3) = -\vec{v}_1` → paralelas.
  - **(b)** `r_1: (0, 0, 0) + t(1, 2, 3)`, `r_2: (3, 2, 1) + s(-1, -2, -3)`.
  - Ponto `P_0(0, 0, 0)` de `r_1`, `r_2` com `P_1(3, 2, 1)` e `\vec{v} = (1, 2, 3)`.
  - `\overrightarrow{P_1P_0} = (-3, -2, -1)`.
  - `(1, 2, 3)\times(-3, -2, -1) = (2(-1) - 3(-2),\; 3(-3) - 1(-1),\; 1(-2) - 2(-3)) = (-2+6,\; -9+1,\; -2+6) = (4, -8, 4)`.
  - `|...| = \sqrt{16 + 64 + 16} = \sqrt{96} = 4\sqrt{6}`.
  - `|\vec{v}| = \sqrt{1 + 4 + 9} = \sqrt{14}`.
  - `d = 4\sqrt{6}/\sqrt{14} = 4\sqrt{6}/\sqrt{14} = 4\sqrt{3/7} = 4\sqrt{21}/7`.
- **Resposta Final:** `(a) sim (b) 4sqrt(21)/7`
- **Alerta pedagógico:** Simplifique o radical: `4\sqrt{6}/\sqrt{14} = 4\sqrt{6/14} = 4\sqrt{3/7} = 4\sqrt{21}/7`.
