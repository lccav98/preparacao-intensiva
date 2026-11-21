# Gabarito Comentado — Bloco `F04` (Elipse Transladada e Completamento de Quadrados)

> **Bloco de referência:** [F04_bloco.md](../blocos/F04_bloco.md)

---

## 1. Exercícios

### `F04-E01` *(Completamento de quadrados simples)*
- **Passo a passo:**
  - `x² - 4x + 4y² + 8y + 4 = 0`.
  - `(x² - 4x) + 4(y² + 2y) = -4`.
  - `(x² - 4x + 4) + 4(y² + 2y + 1) = -4 + 4 + 4 = 4`.
  - `(x-2)² + 4(y+1)² = 4`.
  - `(x-2)²/4 + (y+1)²/1 = 1`.
  - Centro `C(2, -1)`. `a² = 4 → a = 2`, `b² = 1 → b = 1`.
- **Resposta Final:** `(x-2)²/4 + (y+1)²/1 = 1, centro (2, -1)`
- **Alerta pedagógico:** Ao completar o quadrado de `4(y² + 2y)`, adicione `4·1 = 4` ao lado direito, não `1`.

---

### `F04-E02` *(Elipse transladada com coeficientes)*
- **Passo a passo:**
  - `9x² - 54x + 4y² - 16y = -61`.
  - `9(x² - 6x) + 4(y² - 4y) = -61`.
  - `9(x² - 6x + 9) + 4(y² - 4y + 4) = -61 + 81 + 16 = 36`.
  - `9(x-3)² + 4(y-2)² = 36`.
  - `(x-3)²/4 + (y-2)²/9 = 1`.
  - Centro `C(3, 2)`. `a² = 9 → a = 3` (sob `y²`, eixo vertical), `b² = 4 → b = 2`.
- **Resposta Final:** `(a) (x-3)²/4 + (y-2)²/9 = 1 (b) C(3, 2)`
- **Alerta pedagógico:** O termo maior (`9`) está sob `(y-2)²`, então o eixo maior é vertical e `a = 3`.

---

### `F04-E03` *(Vértices e focos de elipse transladada)*
- **Passo a passo:**
  - `(x-3)²/25 + (y+2)²/9 = 1`. Centro `C(3, -2)`.
  - `a² = 25 → a = 5` (sob `x²`, eixo horizontal). `b² = 9 → b = 3`.
  - **(a)** Vértices: `(3 ± 5, -2)` → `(8, -2)` e `(-2, -2)`.
  - `c = √(25 - 9) = 4`. **(b)** Focos: `(3 ± 4, -2)` → `(7, -2)` e `(-1, -2)`.
- **Resposta Final:** `(a) (8, -2) e (-2, -2) (b) (7, -2) e (-1, -2)`
- **Alerta pedagógico:** Vértices ficam no eixo maior (aqui horizontal, `x`). Focos também no eixo maior.

---

### `F04-E04` *(Excentricidade de elipse transladada)*
- **Passo a passo:**
  - `(x+1)²/16 + (y-4)²/7 = 1`. `a² = 16 → a = 4`, `b² = 7 → b = √7`.
  - `c = √(16 - 7) = √9 = 3`.
  - `e = c/a = 3/4`.
- **Resposta Final:** `c = 3, e = 3/4`
- **Alerta pedagógico:** `c = 3` é inteiro aqui; `e = 3/4` é fração irredutível.

---

### `F04-E05` *(Reconhecer elipse vs. circunferência transladada)*
- **Passo a passo:**
  - `(x-2)² + (y+3)² = 16`. Coeficientes de `(x-2)²` e `(y+3)²` são iguais (1).
  - É circunferência. Centro `C(2, -3)`, raio `r = 4`.
- **Resposta Final:** `(a) circunferencia (b) centro=(2, -3), r=4`
- **Alerta pedagógico:** Coeficientes iguais nos quadrados → circunferência, não elipse geral.

---

## 2. Checagem Independente

### `F04-C01` *(Completamento de quadrados)*
- **Passo a passo:**
  - `x² - 6x + y² + 4y = 12`.
  - `(x² - 6x + 9) + (y² + 4y + 4) = 12 + 9 + 4 = 25`.
  - `(x-3)² + (y+2)² = 25`.
  - É circunferência. Centro `(3, -2)`, raio `r = 5`.
- **Resposta Final:** `(a) sim (b) centro=(3, -2), r=5`
- **Alerta pedagógico:** Coeficientes iguais em `x²` e `y²` (ambos 1) → circunferência.

---

### `F04-C02` *(Elipse transladada, eixo vertical)*
- **Passo a passo:**
  - `4(x-1)² + 9(y+2)² = 36`.
  - `(x-1)²/9 + (y+2)²/4 = 1`.
  - Centro `C(1, -2)`. `a² = 9 → a = 3` (sob `y+2`, eixo vertical), `b² = 4 → b = 2`.
  - `c = √(9 - 4) = √5`.
- **Resposta Final:** `(a) (x-1)²/9 + (y+2)²/4 = 1 (b) a=3, b=2, c=√5`
- **Alerta pedagógico:** O denominador maior (`9`) está sob `(y+2)²`, então `a = 3` e o eixo é vertical.

---

### `F04-C03` *(Focos de elipse transladada)*
- **Passo a passo:**
  - `(x+2)²/49 + (y-3)²/36 = 1`. Centro `C(-2, 3)`.
  - `a² = 49 → a = 7` (sob `x+2`, eixo horizontal). `b² = 36 → b = 6`.
  - `c = √(49 - 36) = √13`.
  - Focos: `(-2 ± √13, 3)`.
- **Resposta Final:** `(-2+-√13, 3)`
- **Alerta pedagógico:** `c = √13` é radical exato; não converta para decimal.
