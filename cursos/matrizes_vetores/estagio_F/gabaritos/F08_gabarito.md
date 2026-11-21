# Gabarito Comentado — Bloco `F08` (Revisão Cumulativa do Estágio F)

> **Bloco de referência:** [F08_bloco.md](../blocos/F08_bloco.md)

---

## 1. Exercícios — Sessão 1

### `F08-E01` *(F01 — Parábola na origem)*
- **Passo a passo:**
  - `y² = 8x`. `2p = 8 → p = 4`. `p/2 = 2`.
  - Vértice `V(0, 0)`. Foco `F(p/2, 0) = (2, 0)`. Diretriz `x = -p/2 = -2`.
- **Resposta Final:** `(a) V=(0,0) (b) F=(2, 0) (c) x = -2`
- **Alerta pedagógico:** `2p = 8` → `p = 4`. Foco em `(p/2, 0) = (2, 0)`.

---

### `F08-E02` *(F04 — Elipse transladada)*
- **Passo a passo:**
  - `4(x-1)² + 9(y+2)² = 36` → `(x-1)²/9 + (y+2)²/4 = 1`.
  - Centro `(1, -2)`. `a² = 9 → a = 3`, `b² = 4 → b = 2`.
- **Resposta Final:** `(a) (1, -2) (b) a=3, b=2`
- **Alerta pedagógico:** Centro vem de `(x-1)` e `(y+2)`: `h = 1`, `k = -2`.

---

### `F08-E03` *(F05 — Hipérbole na origem)*
- **Passo a passo:**
  - `x²/16 - y²/9 = 1`. `a = 4`, `b = 3`.
  - Assíntotas: `y = ±(b/a)x = ±(3/4)x`.
  - `c = √(16 + 9) = 5`. `e = c/a = 5/4`.
- **Resposta Final:** `(a) y = +-3/4 x (b) e = 5/4`
- **Alerta pedagógico:** Eixo horizontal → assíntotas `y = ±(b/a)x`.

---

## 1. Exercícios — Sessão 2 (continuação)

### `F08-E04` *(F06 — Armadilha do sinal)*
- **Passo a passo:**
  - `x² - 4y² + 4x - 8y - 4 = 0`.
  - `(x² + 4x) - 4(y² + 2y) = 4`.
  - `(x² + 4x + 4) - 4(y² + 2y + 4) = 4 + 4 - 16 = -8`.
  - `(x+2)² - 4(y+2)² = -8`.
  - Multiplique por `-1`: `4(y+2)² - (x+2)² = 8`.
  - Divida por 8: `(y+2)²/2 - (x+2)²/8 = 1`.
  - Hipérbole com eixo vertical. Centro `(-2, -2)`.
- **Resposta Final:** `(y+2)²/2 - (x+2)²/8 = 1, hiperbole`
- **Alerta pedagógico:** Lado direito `-8` → multiplique por `-1` antes de dividir.

---

### `F08-E05` *(F07 — Quádrica)*
- **Passo a passo:**
  - `x²/4 + y²/9 - z²/16 = 1`. Sinais `+ + -`, lado direito `1`.
  - Hiperboloide de 1 folha.
- **Resposta Final:** `hiperboloide de 1 folha`
- **Alerta pedagógico:** Dois sinais positivos, um negativo, lado direito positivo ⇔ hiperboloide de 1 folha.

---

### `F08-E06` *(F03 — Circunferência)*
- **Passo a passo:**
  - `x² + y² = 25`. `r² = 25 → r = 5`. `e = 0` (circunferência).
- **Resposta Final:** `r=5, e=0`
- **Alerta pedagógico:** Circunferência de raio 5, excentricidade zero.

---

## 2. Checagem Independente

### `F08-C01` *(Parábola transladada)*
- **Passo a passo:**
  - `(y+3)² = 8(x-1)`. `2p = 8 → p = 4`. `p/2 = 2`.
  - Vértice `V(1, -3)`. Foco `F(1 + 2, -3) = (3, -3)`.
- **Resposta Final:** `V=(1, -3), F=(3, -3)`
- **Alerta pedagógico:** Vértice `(h, k) = (1, -3)`. Foco desloca `p/2 = 2` no eixo da variável não ao quadrado (`x`).

---

### `F08-C02` *(Classificação de cônica)*
- **Passo a passo:**
  - `9x² - 4y² + ... = 0`. `A = 9`, `C = -4`. Sinais opostos.
  - **Hipérbole**.
- **Resposta Final:** `hiperbole`
- **Alerta pedagógico:** `A` e `C` de sinais opostos ⇔ hipérbole.

---

### `F08-C03` *(Quádrica por traços)*
- **Passo a passo:**
  - `x²/4 + y²/9 - z²/16 = 1`. Em `z = 0`: `x²/4 + y²/9 = 1` → elipse.
- **Resposta Final:** `elipse`
- **Alerta pedagógico:** Traço horizontal do hiperboloide de 1 folha é elipse.

---

## 3. Critério de Domínio e Recuperação

- **Avançar para `G01` (Estágio G):** somente após autocorreção de `F08-E01`–`F08-E06` e **100% (3/3)** na Checagem Independente `F08-C01`–`F08-C03` sem consulta.
- **Recuperação direcionada (1ª falha):** retorne ao bloco específico do Estágio F (`F01` a `F07`) onde ocorreu o erro.
- **Após 2 tentativas malsucedidas:** interrompa e revise todo o Estágio F com o orientador antes de avançar para `G01`.

## 6. Referências do Orientador
- `[DOC]` `P3` p. 165–184; `L11` Ex. 1–15.
- `[INF/AUS]` `Planejamento` Sem. 13–14 (quádricas em `F07`).
- Gabarito e casos: [F08_gabarito.md](../gabaritos/F08_gabarito.md) e [casos_F08.json](../testes/casos_F08.json).
