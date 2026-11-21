# Gabarito Comentado — Bloco `E02` (Ângulo, Paralelismo, Ortogonalidade e Reta Ortogonal a Duas)

> **Bloco de referência:** [E02_bloco.md](../blocos/E02_bloco.md)

---

## 1. Exercícios

### `E02-E01` *(Ângulo entre duas retas)*
- **Passo a passo:**
  - `\vec{v}_1\cdot\vec{v}_2 = 1(2) + 2(1) + 2(-2) = 2 + 2 - 4 = 0`.
  - `|\vec{v}_1| = \sqrt{1+4+4} = 3`, `|\vec{v}_2| = \sqrt{4+1+4} = 3`.
  - `\cos\theta = \frac{|0|}{3\cdot 3} = 0`.
- **Resposta Final:** `cos = 0`
- **Alerta pedagógico:** Produto escalar nulo → vetores ortogonais → ângulo de 90°. O ângulo entre retas é sempre agudo (ou reto).

---

### `E02-E02` *(Paralelismo de vetores diretores)*
- **Passo a passo:**
  - `\vec{u} = (2, 4, -6)`, `\vec{v} = (-1, -2, 3)`.
  - `2/(-1) = -2`, `4/(-2) = -2`, `-6/3 = -2`. Todas as razões são `-2`.
  - `\vec{u} = -2\vec{v}` → paralelas com `k = -2`.
- **Resposta Final:** `sim k = -2`
- **Alerta pedagógico:** O fator `k` pode ser negativo; o que importa é a proporcionalidade de todos os componentes.

---

### `E02-E03` *(Ortogonalidade)*
- **Passo a passo:**
  - `\vec{a}\cdot\vec{b} = 1(2) + 2(-1) + (-1)(0) = 2 - 2 + 0 = 0`.
  - Produto escalar nulo → ortogonais.
- **Resposta Final:** `sim`
- **Alerta pedagógico:** Um componente zero não impede a ortogonalidade; o que importa é a soma dos produtos ser zero.

---

### `E02-E04` *(Reta ortogonal a duas retas)*
- **Passo a passo:**
  - `\vec{v}_1\times\vec{v}_2 = (2\cdot1 - 3(-1),\; 3\cdot2 - 1\cdot1,\; 1(-1) - 2\cdot2) = (2+3,\; 6-1,\; -1-4) = (5, 5, -5)`.
  - Pode simplificar para `(1, 1, -1)`.
- **Resposta Final:** `(5, 5, -5)`
- **Alerta pedagógico:** Qualquer múltiplo escalar não nulo de `(5, 5, -5)` é um vetor diretor válido da reta ortogonal.

---

### `E02-E05` *(Integração: ângulo + ortogonalidade)*
- **Passo a passo:**
  - **(a)** `\vec{p}\cdot\vec{q} = 1(1) + 1(-1) + 1(2) = 1 - 1 + 2 = 2 \neq 0` → não ortogonais.
  - **(b)** `|\vec{p}| = \sqrt{3}`, `|\vec{q}| = \sqrt{1+1+4} = \sqrt{6}`. `\cos\theta = \frac{|2|}{\sqrt{3}\sqrt{6}} = \frac{2}{\sqrt{18}} = \frac{2}{3\sqrt{2}} = \frac{\sqrt{2}}{3}`.
- **Resposta Final:** `(a) nao (b) cos = sqrt(2)/3`
- **Alerta pedagógico:** Simplifique `\frac{2}{3\sqrt{2}}` multiplicando numerador e denominador por `\sqrt{2}` para obter `\frac{\sqrt{2}}{3}`.

---

## 2. Checagem Independente

### `E02-C01` *(Ângulo agudo com frações)*
- **Passo a passo:**
  - `\vec{r}\cdot\vec{s} = 3(1) + 4(0) + 0(2) = 3`.
  - `|\vec{r}| = \sqrt{9+16+0} = 5`, `|\vec{s}| = \sqrt{1+0+4} = \sqrt{5}`.
  - `\cos\theta = \frac{3}{5\sqrt{5}} = \frac{3\sqrt{5}}{25}`.
- **Resposta Final:** `cos = 3/(5sqrt(5))` ou `cos = 3sqrt(5)/25`
- **Alerta pedagógico:** Rationalize o denominador: `\frac{3}{5\sqrt{5}} = \frac{3\sqrt{5}}{25}`.

---

### `E02-C02` *(Reta ortogonal a duas retas coordenadas)*
- **Passo a passo:**
  - `\vec{v}_1\times\vec{v}_2 = (1, 0, 0)\times(0, 1, 0) = (0\cdot0 - 0\cdot1,\; 0\cdot0 - 1\cdot0,\; 1\cdot1 - 0\cdot0) = (0, 0, 1)`.
- **Resposta Final:** `(0, 0, 1)`
- **Alerta pedagógico:** A reta ortogonal ao plano `xy` é paralela ao eixo `z`.

---

### `E02-C03` *(Paralelismo com frações)*
- **Passo a passo:**
  - `\vec{m} = (1/2, 1, -3/2)`, `\vec{n} = (1, 2, -3)`.
  - `\vec{n} = 2\vec{m}` → `2(1/2) = 1`, `2(1) = 2`, `2(-3/2) = -3`. Sim, paralelas com `k = 2` (ou `\vec{m} = (1/2)\vec{n}` → `k = 1/2`).
- **Resposta Final:** `sim k = 2` (ou `sim k = 1/2` dependendo da ordem)
- **Alerta pedagógico:** Informe o fator `k` tal que `\vec{m} = k\vec{n}` (nesse caso `k = 1/2`) ou `\vec{n} = k\vec{m}` (`k = 2`). Aceite qualquer um com justificativa.
