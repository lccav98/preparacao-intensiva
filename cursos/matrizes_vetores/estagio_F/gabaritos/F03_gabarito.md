# Gabarito Comentado — Bloco `F03` (Elipse na Origem e Circunferência)

> **Bloco de referência:** [F03_bloco.md](../blocos/F03_bloco.md)

---

## 1. Exercícios

### `F03-E01` *(Elipse na origem, eixo horizontal)*
- **Passo a passo:**
  - `x²/16 + y²/9 = 1`. `a² = 16 → a = 4`, `b² = 9 → b = 3`. Eixo maior horizontal (`a` sob `x²`).
  - **(b)** `c = √(a² - b²) = √(16 - 9) = √7`. Focos `(±√7, 0)`.
  - **(c)** `e = c/a = √7/4`.
- **Resposta Final:** `(a) a=4, b=3 (b) (+-√7, 0) (c) e = √7/4`
- **Alerta pedagógico:** `a` é sempre o semi-eixo maior (sob o termo do eixo maior). Aqui `a=4 > b=3`.

---

### `F03-E02` *(Elipse na origem, eixo vertical)*
- **Passo a passo:**
  - `x²/9 + y²/25 = 1`. `a² = 25 → a = 5` (sob `y²`, eixo vertical), `b² = 9 → b = 3`.
  - `c = √(25 - 9) = 4`. Focos `(0, ±4)`.
  - `e = c/a = 4/5`.
- **Resposta Final:** `(a) a=5, b=3 (b) (0, +-4) (c) e = 4/5`
- **Alerta pedagógico:** Quando o denominador maior está sob `y²`, o eixo real é vertical e os focos estão em `(0, ±c)`.

---

### `F03-E03` *(Dados a e c, encontrar b e equação)*
- **Passo a passo:**
  - `a = 5`, `c = 3`. `a² = b² + c² → 25 = b² + 9 → b² = 16 → b = 4`.
  - Equação: `x²/25 + y²/16 = 1`.
- **Resposta Final:** `(a) b=4 (b) x²/25 + y²/16 = 1`
- **Alerta pedagógico:** Lembre da relação `a² = b² + c²` para elipse (diferente da hipérbole, que é `c² = a² + b²`).

---

### `F03-E04` *(Circunferência como caso particular)*
- **Passo a passo:**
  - `x² + y² = 16` → `x²/16 + y²/16 = 1`. `a = b = 4`. É circunferência.
  - Raio `r = 4`, centro `(0, 0)`, `c = 0`, `e = 0`.
- **Resposta Final:** `(a) sim (b) r=4, centro=(0,0), e=0`
- **Alerta pedagógico:** Circunferência é elipse com `a = b`, logo `c = 0` e `e = 0`.

---

### `F03-E05` *(Integração: elipse com dados mistos)*
- **Passo a passo:**
  - Vértice `(4, 0)` → `a = 4`. Foco `(2, 0)` → `c = 2`.
  - `a² = b² + c² → 16 = b² + 4 → b² = 12 → b = √12 = 2√3`.
  - Equação: `x²/16 + y²/12 = 1`.
  - `e = c/a = 2/4 = 1/2`.
- **Resposta Final:** `(a) x²/16 + y²/12 = 1 (b) e = 1/2`
- **Alerta pedagógico:** `c = 2` vem do foco `(2, 0)`. `b² = 12`, não `b = 12`.

---

## 2. Checagem Independente

### `F03-C01` *(Elipse, eixo horizontal)*
- **Passo a passo:**
  - `x²/36 + y²/20 = 1`. `a² = 36 → a = 6`, `b² = 20`.
  - `c = √(36 - 20) = √16 = 4`.
  - `e = c/a = 4/6 = 2/3`.
- **Resposta Final:** `(a) c=4 (b) e = 2/3`
- **Alerta pedagógico:** Simplifique `4/6` para `2/3`.

---

### `F03-C02` *(Elipse, eixo vertical)*
- **Passo a passo:**
  - `x²/4 + y²/9 = 1`. `a² = 9 → a = 3` (sob `y²`), `b² = 4 → b = 2`.
  - `c = √(9 - 4) = √5`. Focos `(0, ±√5)`.
- **Resposta Final:** `(a) a=3 (b) (0, +-√5)`
- **Alerta pedagógico:** O semi-eixo maior `a = 3` está sob `y²`, então os focos estão no eixo `y`.

---

### `F03-C03` *(Circunferência)*
- **Passo a passo:**
  - `x² + y² = 25` → `x²/25 + y²/25 = 1`. `a = b = 5`. Circunferência.
  - Raio `r = 5`. `e = 0`.
- **Resposta Final:** `r=5, e=0`
- **Alerta pedagógico:** Circunferência de raio 5, centro na origem, excentricidade zero.
