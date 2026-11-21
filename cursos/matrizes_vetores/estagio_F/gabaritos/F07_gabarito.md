# Gabarito Comentado — Bloco `F07` (Superfícies Quádricas Canônicas e Traços) `[INF/AUS]`

> **Bloco de referência:** [F07_bloco.md](../blocos/F07_bloco.md)
> **Nota:** Este bloco é marcado `[INF/AUS]` pois superfícies quádricas não constam nos 19 PDFs auditados (apenas no Planejamento, Semanas 13–14). O conteúdo é uma inferência apoiada nas cônicas de `L11`.

---

## 1. Exercícios

### `F07-E01` *(Elipsoide)*
- **Passo a passo:**
  - `x²/4 + y²/9 + z²/16 = 1`. Todos os coeficientes positivos, lado direito `1`.
  - Traços em `x = k`, `y = k`, `z = k` são elipses.
  - **Elipsoide**.
- **Resposta Final:** `elipsoide`
- **Alerta pedagógico:** Todos os sinais iguais (positivos) e `= 1` ⇔ elipsoide.

---

### `F07-E02` *(Hiperboloide de 1 folha)*
- **Passo a passo:**
  - `x² + y² - z² = 1`. Sinais `+ + -`, lado direito `1`.
  - Traço em `z = 0`: `x² + y² = 1` (elipse). Traços verticais: hipérboles.
  - **Hiperboloide de 1 folha**, eixo `z` (eixo do termo com sinal diferente).
- **Resposta Final:** `hiperboloide de 1 folha, eixo z`
- **Alerta pedagógico:** O eixo de simetria é o da variável com sinal diferente dos outros dois.

---

### `F07-E03` *(Hiperboloide de 2 folhas)*
- **Passo a passo:**
  - `x² + y² - z² = -1`. Sinais `+ + -`, lado direito `-1`.
  - **Hiperboloide de 2 folhas**, eixo `z`.
- **Resposta Final:** `hiperboloide de 2 folhas`
- **Alerta pedagógico:** Mesmos sinais de `F07-E02` mas lado direito `-1` ⇔ 2 folhas.

---

### `F07-E04` *(Paraboloide elíptico vs. hiperbólico)*
- **Passo a passo:**
  - `z = x² + y²`. Só há soma de quadrados, um termo linear (`z`).
  - Traços horizontais `z = k`: `x² + y² = k` (elipse para `k > 0`).
  - **Paraboloide elíptico**.
- **Resposta Final:** `paraboloide eliptico`
- **Alerta pedagógico:** Soma de quadrados igual a variável linear ⇔ paraboloide elíptico.

---

### `F07-E05` *(Cone e cilindro)*
- **Passo a passo:**
  - `x² + y² - z² = 0`. Lado direito `0`, sinais `+ + -`.
  - Traços horizontais `z = k`: `x² + y² = k²` (elipse/círculo para `k ≠ 0`, ponto para `k = 0`).
  - **Cone**, eixo `z`.
- **Resposta Final:** `cone`
- **Alerta pedagógico:** Lado direito `0` com sinais mistos ⇔ cone.

---

## 2. Checagem Independente

### `F07-C01` *(Traços coordenados)*
- **Passo a passo:**
  - `x²/4 + y²/9 - z² = 1`. Em `z = 0`: `x²/4 + y²/9 = 1` → elipse.
- **Resposta Final:** `elipse`
- **Alerta pedagógico:** Traço horizontal de hiperboloide de 1 folha é elipse.

---

### `F07-C02` *(Paraboloide hiperbólico)*
- **Passo a passo:**
  - `z = x²/4 - y²/9`. Subtração de quadrados igual a variável linear.
  - Traços horizontais: hipérboles. Traços verticais: parábolas.
  - **Paraboloide hiperbólico**.
- **Resposta Final:** `paraboloide hiperbolico`
- **Alerta pedagógico:** Subtração de quadrados (sinais opostos) ⇔ paraboloide hiperbólico (selim).

---

### `F07-C03` *(Cilindro)*
- **Passo a passo:**
  - `x²/4 + y²/9 = 1`. Apenas `x` e `y` aparecem; `z` está ausente.
  - É um cilindro elíptico cujos elementos são paralelos ao eixo `z`.
- **Resposta Final:** `cilindro eliptico sobre o eixo z`
- **Alerta pedagógico:** Variável ausente (`z`) ⇔ cilindro sobre o eixo da variável ausente.
