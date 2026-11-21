# Gabarito Comentado — Bloco `E09` (Distâncias Envolvendo Planos: Ponto-Plano, Planos Paralelos, Reta-Plano)

> **Bloco de referência:** [E09_bloco.md](../blocos/E09_bloco.md)

---

## 1. Exercícios

### `E09-E01` *(Distância ponto-plano)*
- **Passo a passo:**
  - `a=1, b=2, c=2, d=-3`. `P_0(2, 1, -1)`.
  - Numerador: `|1(2) + 2(1) + 2(-1) - 3| = |2 + 2 - 2 - 3| = |-1| = 1`.
  - Denominador: `\sqrt{1 + 4 + 4} = 3`.
  - `d = 1/3`.
- **Resposta Final:** `1/3`
- **Alerta pedagogico:** Valor absoluto no numerador; `1/3` já está irredutível.

---

### `E09-E02` *(Planos paralelos — normalização)*
- **Passo a passo:**
  - `\pi_1: 3x - 4y + 12z - 5 = 0`.
  - `\pi_2: 6x - 8y + 24z + 10 = 0`. Divida por 2: `3x - 4y + 12z + 5 = 0`.
  - Agora `d_1 = -5`, `d_2' = 5`.
  - `d = \frac{|-5 - 5|}{\sqrt{9 + 16 + 144}} = \frac{10}{13}`.
- **Resposta Final:** `10/13`
- **Alerta pedagogico:** NUNCA subtraia `d_1` e `d_2` sem normalizar os coeficientes de `x, y, z` primeiro.

---

### `E09-E03` *(Distância reta-plano, reta paralela)*
- **Passo a passo:**
  - `\vec{v} = (1, 1, 0)`, `\vec{n} = (1, 1, 0)` (do plano `x + y - 2 = 0`).
  - `\vec{v}\cdot\vec{n} = 1 + 1 + 0 = 2 \neq 0`.
  - Não é paralela ao plano.
- **Resposta Final:** `nao_paralela`
- **Alerta pedagogico:** Para distância reta-plano, primeiro verifique `\vec{v}\cdot\vec{n} = 0`.

---

### `E09-E04` *(Distância ponto-plano com frações)*
- **Passo a passo:**
  - `P_0(1/2, 1, -1/2)`, `\pi: 2x - y + 2z - 3 = 0`.
  - Numerador: `|2(1/2) - 1 + 2(-1/2) - 3| = |1 - 1 - 1 - 3| = |-4| = 4`.
  - Denominador: `\sqrt{4 + 1 + 4} = 3`.
  - `d = 4/3`.
- **Resposta Final:** `4/3`
- **Alerta pedagogico:** Mantenha frações até o final; `4/3` é irredutível.

---

### `E10-E05` *(Integração: ponto-plano e planos paralelos)*
- **Passo a passo:**
  - **(a)** `P_0(1, 2, 3)`, `\pi: 2x - y + 2z - 6 = 0`.
  - Numerador: `|2(1) - 2 + 2(3) - 6| = |2 - 2 + 6 - 6| = 0`.
  - `d = 0`. O ponto pertence ao plano!
  - **(b)** `\pi': 4x - 2y + 4z + 8 = 0`. Divida por 2: `2x - y + 2z + 4 = 0`.
  - `d_1 = -6`, `d_2' = 4`. `d = \frac{|-6 - 4|}{\sqrt{4 + 1 + 4}} = \frac{10}{3}`.
- **Resposta Final:** `(a) 0 (b) 10/3`
- **Alerta pedagógico:** Na parte (a), o ponto está no plano (distância zero). Na parte (b), normalize `\pi'` antes de subtrair.

---

## 2. Checagem Independente

### `E09-C01` *(Distância ponto-plano exata)*
- **Passo a passo:**
  - `P_0(1, 2, 3)`, `\pi: x - 2y + 2z - 4 = 0`.
  - Numerador: `|1 - 4 + 6 - 4| = |-1| = 1`.
  - Denominador: `\sqrt{1 + 4 + 4} = 3`.
  - `d = 1/3`.
- **Resposta Final:** `1/3`
- **Alerta pedagogico:** Confira os sinais: `1 - 4 + 6 - 4 = -1`, valor absoluto `1`.

---

### `E09-C02` *(Planos paralelos com normalização)*
- **Passo a passo:**
  - `\pi_1: x + y + z - 1 = 0`.
  - `\pi_2: 2x + 2y + 2z + 5 = 0`. Divida por 2: `x + y + z + 5/2 = 0`.
  - `d_1 = -1`, `d_2' = 5/2`.
  - `d = \frac{|-1 - 5/2|}{\sqrt{3}} = \frac{|-7/2|}{\sqrt{3}} = \frac{7}{2\sqrt{3}} = \frac{7\sqrt{3}}{6}`.
- **Resposta Final:** `7sqrt(3)/6`
- **Alerta pedagogico:** Normalize dividindo por 2, depois `d = |d_1 - d_2'|/|\vec{n}|`.

---

### `E09-C03` *(Distância reta-plano — ponto da reta ao plano)*
- **Passo a passo:**
  - `r: (2, 1, 0) + t(1, -1, 0)`, `\pi: x - y - 3 = 0`.
  - `\vec{v} = (1, -1, 0)`, `\vec{n} = (1, -1, 0)`.
  - `\vec{v}\cdot\vec{n} = 1 + 1 + 0 = 2 \neq 0`.
  - Não é paralela ao plano.
- **Resposta Final:** `nao_paralela`
- **Alerta pedagogico:** O diretor `(1, -1, 0)` é igual à normal `(1, -1, 0)`, então a reta é perpendicular ao plano, não paralela.
