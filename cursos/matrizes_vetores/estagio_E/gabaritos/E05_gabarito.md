# Gabarito Comentado — Bloco `E05` (Ângulos e Posições Relativas Plano-Plano e Reta-Plano)

> **Bloco de referência:** [E05_bloco.md](../blocos/E05_bloco.md)

---

## 1. Exercícios

### `E05-E01` *(Ângulo entre dois planos)*
- **Passo a passo:**
  - `\vec{n}_1 = (1, 1, 1)`, `\vec{n}_2 = (1, -1, 1)`.
  - `\vec{n}_1\cdot\vec{n}_2 = 1 - 1 + 1 = 1`.
  - `|\vec{n}_1| = \sqrt{3}`, `|\vec{n}_2| = \sqrt{3}`.
  - `\cos\theta = \frac{|1|}{\sqrt{3}\sqrt{3}} = \frac{1}{3}`.
- **Resposta Final:** `cos = 1/3`
- **Alerta pedagógico:** O ângulo entre planos é sempre o agudo; use valor absoluto no produto escalar das normais.

---

### `E05-E02` *(Ângulo reta-plano)*
- **Passo a passo:**
  - `\vec{v} = (1, 1, 1)`, `\vec{n} = (1, 1, 1)`.
  - `\vec{v}\cdot\vec{n} = 3`.
  - `|\vec{v}| = \sqrt{3}`, `|\vec{n}| = \sqrt{3}`.
  - `\sin\phi = \frac{|3|}{\sqrt{3}\sqrt{3}} = \frac{3}{3} = 1`.
- **Resposta Final:** `sen = 1`
- **Alerta pedagógico:** Seno = 1 → ângulo reta-plano de 90° → a reta é perpendicular ao plano (seu diretor é paralelo à normal).

---

### `E05-E03` *(Paralelismo estrito reta-plano)*
- **Passo a passo:**
  - `\vec{v}\cdot\vec{n} = 1(1) + (-1)(-1) + 0(2) = 1 + 1 + 0 = 2 \neq 0`.
  - Não é ortogonal à normal → não é paralela ao plano.
- **Resposta Final:** `nao`
- **Alerta pedagógico:** Para reta paralela ao plano, o diretor deve ser ortogonal à normal (`\vec{v}\cdot\vec{n} = 0`). Aqui `2 ≠ 0`.

---

### `E05-E04` *(Planos paralelos)*
- **Passo a passo:**
  - `\vec{n}_1 = (2, -4, 4)`, `\vec{n}_2 = (1, -2, 2)`.
  - `\vec{n}_1 = 2\vec{n}_2` → proporcionais → planos paralelos.
- **Resposta Final:** `sim`
- **Alerta pedagógico:** Normais proporcionais ⇔ planos paralelos (ou coincidentes).

---

### `E05-E05` *(Cosseno vs. Seno — não confundir)*
- **Passo a passo:**
  - **(a)** `\vec{n}_1\cdot\vec{n}_2 = 0`, `|\vec{n}_1| = 1`, `|\vec{n}_2| = 1`. `\cos\theta = 0` → ângulo de 90° (planos perpendiculares).
  - **(b)** `\vec{v} = (1, 0, 0)`, `\vec{n} = (0, 1, 0)`. `\vec{v}\cdot\vec{n} = 0`. `|\vec{v}| = 1`, `|\vec{n}| = 1`. `\sin\phi = 0` → ângulo reta-plano de 0° (reta contida ou paralela ao plano).
- **Resposta Final:** `(a) cos = 0 (b) sen = 0`
- **Alerta pedagógico:** Plano-plano usa cosseno das normais; reta-plano usa seno do diretor com a normal. Não confunda.

---

## 2. Checagem Independente

### `E05-C01` *(Ângulo entre planos com frações)*
- **Passo a passo:**
  - `\vec{n}_1 = (2, -1, 2)`, `\vec{n}_2 = (1, 2, -2)`.
  - `\vec{n}_1\cdot\vec{n}_2 = 2 - 2 - 4 = -4`. Valor absoluto: `4`.
  - `|\vec{n}_1| = \sqrt{4+1+4} = 3`, `|\vec{n}_2| = \sqrt{1+4+4} = 3`.
  - `\cos\theta = 4/9`.
- **Resposta Final:** `cos = 4/9`
- **Alerta pedagógico:** Valor absoluto de `-4` é `4`; o ângulo é agudo.

---

### `E05-C02` *(Ângulo reta-plano com seno)*
- **Passo a passo:**
  - `\vec{v} = (3, 4, 0)`, `\vec{n} = (3, 4, 0)`.
  - `\vec{v}\cdot\vec{n} = 9 + 16 + 0 = 25`.
  - `|\vec{v}| = 5`, `|\vec{n}| = 5`.
  - `\sin\phi = 25/25 = 1`.
- **Resposta Final:** `sen = 1`
- **Alerta pedagógico:** Quando o diretor é igual à normal, a reta é perpendicular ao plano (ângulo 90°).

---

### `E05-C03` *(Paralelismo estrito reta-plano — ponto fora)*
- **Passo a passo:**
  - `\vec{v}\cdot\vec{n} = 1(1) + 1(1) + 0(-2) = 2 \neq 0`. Não é ortogonal à normal → não é paralela.
  - Mesmo que fosse, verifique ponto fora: `P(0, 0, 1)` no plano `x + y - 2 = 0`: `0 + 0 - 2 = -2 \neq 0` → ponto fora.
  - Mas como `\vec{v}\cdot\vec{n} \neq 0`, não é paralela.
- **Resposta Final:** `nao`
- **Alerta pedagógico:** Ambas as condições devem ser satisfeitas: `\vec{v}\cdot\vec{n} = 0` E ponto fora do plano.
