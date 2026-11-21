# Gabarito Comentado — Bloco `E10` (Revisão Cumulativa do Estágio E)

> **Bloco de referência:** [E10_bloco.md](../blocos/E10_bloco.md)

---

## 1. Exercícios — Sessão 1

### `E10-E01` *(E01 — Reta reduzida)*
- **Passo a passo:**
  - `\vec{v} = \overrightarrow{AB} = (3, -2, 2)`.
  - `t = (x-1)/3`. `y = 2 - 2t = 2 - 2(x-1)/3 = (-2/3)x + 8/3`. `z = 3 + 2t = 3 + 2(x-1)/3 = (2/3)x + 7/3`.
- **Resposta Final:** `y = -2/3 x + 8/3, z = 2/3 x + 7/3`
- **Alerta pedagógico:** Mantenha frações irredutíveis.

---

### `E10-E02` *(E04 — Plano por 3 pontos)*
- **Passo a passo:**
  - `\overrightarrow{AB} = (-1, 1, 0)`, `\overrightarrow{AC} = (-1, 0, 1)`.
  - `\vec{n} = (1, 1, 1)`.
  - Plano: `x + y + z - 1 = 0`.
- **Resposta Final:** `x + y + z - 1 = 0`
- **Alerta pedagógico:** Plano da primeira octante passando pelos interceptos unitários.

---

### `E10-E03` *(E07 — Distância ponto-reta)*
- **Passo a passo:**
  - `P_1(0, 0, 0)`, `\vec{v} = (1, 1, 1)`, `\overrightarrow{P_1P_0} = (1, 2, 3)`.
  - `(1, 1, 1)\times(1, 2, 3) = (1\cdot3 - 1\cdot2,\; 1\cdot1 - 1\cdot3,\; 1\cdot2 - 1\cdot1) = (1, -2, 1)`.
  - `|...| = \sqrt{6}`, `|\vec{v}| = \sqrt{3}`.
  - `d = \sqrt{6}/\sqrt{3} = \sqrt{2}`.
- **Resposta Final:** `sqrt(2)`
- **Alerta pedagógico:** `\sqrt{6}/\sqrt{3} = \sqrt{2}`.

---

## 1. Exercícios — Sessão 2 (continuação)

### `E10-E04` *(E09 — Planos paralelos)*
- **Passo a passo:**
  - `\pi_1: 2x - y + 2z - 3 = 0`.
  - `\pi_2: 4x - 2y + 4z + 6 = 0`. Divida por 2: `2x - y + 2z + 3 = 0`.
  - `d_1 = -3`, `d_2' = 3`. `d = \frac{|-3 - 3|}{3} = 2`.
- **Resposta Final:** `2`
- **Alerta pedagógico:** Normalize `\pi_2` dividindo por 2 antes de subtrair.

---

### `E10-E05` *(E05 — Ângulo reta-plano)*
- **Passo a passo:**
  - `\vec{v} = (1, 2, 2)`, `\vec{n} = (2, -1, 2)`.
  - `\vec{v}\cdot\vec{n} = 2 - 2 + 4 = 4`.
  - `|\vec{v}| = 3`, `|\vec{n}| = 3`.
  - `\sin\phi = 4/9`.
- **Resposta Final:** `sen = 4/9`
- **Alerta pedagógico:** Seno do ângulo reta-plano, não cosseno.

---

### `E10-E06` *(E03 — Coplanaridade de retas)*
- **Passo a passo:**
  - `\overrightarrow{A_1A_2} = (-1, 1, 0)`.
  - `\vec{v}_1\times\vec{v}_2 = (1, 1, 0)\times(0, 1, 1) = (1, -1, 1)`.
  - Produto misto: `(1, 1, 0)\cdot(1, -1, 1) = 1 - 1 + 0 = 0`.
  - Coplanares → sim.
- **Resposta Final:** `sim`
- **Alerta pedagógico:** Produto misto zero ⇔ coplanares.

---

## 2. Checagem Independente

### `E10-C01` *(E02 — Ângulo entre retas)*
- **Passo a passo:**
  - `\vec{v}_1\cdot\vec{v}_2 = 2 + 2 - 4 = 0`. `\cos\theta = 0`.
- **Resposta Final:** `cos = 0`
- **Alerta pedagógico:** Vetores ortogonais → ângulo 90° entre as retas.

---

### `E10-C02` *(E06 — Interseção reta-plano)*
- **Passo a passo:**
  - `(1+t) + (2-t) + 3t = 6 → 3 + 3t = 6 → t = 1`.
  - Ponto: `(2, 1, 3)`.
- **Resposta Final:** `(2, 1, 3)`
- **Alerta pedagógico:** Confirme: `2 + 1 + 3 = 6`. Pertence ao plano.

---

### `E10-C03` *(E08 — Distância entre retas reverses)*
- **Passo a passo:**
  - `r_1: (0, 0, 0) + t(1, 0, 0)`, `r_2: (0, 1, 0) + s(0, 0, 1)`.
  - `\vec{u}\times\vec{v} = (0, -1, 0)`, `|...| = 1`.
  - `\overrightarrow{P_1P_2} = (0, 1, 0)`.
  - Produto misto: `(1, 0, 0)\cdot((0, 0, 1)\times(0, 1, 0))`. `(0, 0, 1)\times(0, 1, 0) = (-1, 0, 0)`. `(1, 0, 0)\cdot(-1, 0, 0) = -1`. `|-1| = 1`.
  - `d = 1/1 = 1`.
- **Resposta Final:** `1`
- **Alerta pedagógico:** Retas reverses (não coplanares, não paralelas) usam a fórmula do paralelepípedo.

---

## 3. Critério de Domínio e Recuperação

- **Avançar para `F01` (Estágio F):** somente após autocorreção de `E10-E01`–`E10-E06` e **100% (3/3)** na Checagem Independente `E10-C01`–`E10-C03` sem consulta.
- **Recuperação direcionada (1ª falha):** retorne ao bloco específico do Estágio E (`E01` a `E09`) onde ocorreu o erro.
- **Após 2 tentativas malsucedidas:** interrompa e revise todo o Estágio E com o orientador antes de avançar para `F01`.

## 6. Referências do Orientador
- `[DOC]` `MAT121_Parte_4.pdf` p. 1–61.
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 124–164.
- Gabarito e casos: [E10_gabarito.md](../gabaritos/E10_gabarito.md) e [casos_E10.json](../testes/casos_E10.json).
