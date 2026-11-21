# Gabarito Comentado — Bloco `E01` (Equações da Reta no R³ e Pertinência)

> **Bloco de referência:** [E01_bloco.md](../blocos/E01_bloco.md)

---

## 1. Exercícios

### `E01-E01` *(Vetorial e paramétricas por dois pontos)*
- **Passo a passo:**
  - `\vec{v} = \overrightarrow{AB} = B - A = (2 - (-1), -1 - 3, 5 - 2) = (3, -4, 3)`.
  - **(a)** Vetorial: `r: (-1, 3, 2) + t(3, -4, 3)`.
  - **(b)** Paramétricas: `x = -1 + 3t`, `y = 3 - 4t`, `z = 2 + 3t`.
- **Resposta Final:** `(a) (-1, 3, 2) + t(3, -4, 3) (b) x = -1 + 3t, y = 3 - 4t, z = 2 + 3t`
- **Alerta pedagógico:** Sempre `\vec{v} = B - A` (extremidade menos origem), nunca `A - B`.

---

### `E01-E02` *(Simétricas e reduzidas em `x`)*
- **Passo a passo:**
  - **(a)** Simétricas: `\frac{x-1}{2} = \frac{y-(-2)}{3} = \frac{z-4}{-1}` → `\frac{x-1}{2} = \frac{y+2}{3} = \frac{z-4}{-1}`.
  - **(b)** Do `\frac{x-1}{2} = t`: `t = \frac{x-1}{2}`. Então `y = -2 + 3t = -2 + 3(\frac{x-1}{2}) = \frac{3}{2}x - \frac{7}{2}`. E `z = 4 - t = 4 - \frac{x-1}{2} = -\frac{1}{2}x + \frac{9}{2}`.
- **Resposta Final:** `(a) (x-1)/2 = (y+2)/3 = (z-4)/(-1) (b) y = 3/2 x - 7/2, z = -1/2 x + 9/2`
- **Alerta pedagógico:** As reduzidas devem estar sempre isoladas em `x`: `y = mx + n`, `z = px + q`.

---

### `E01-E03` *(Vetor diretor de coordenadas constantes)*
- **Passo a passo:**
  - **(a)** Paralela ao eixo `y` → vetor diretor `(0, 1, 0)`.
  - **(b)** Como `x` e `z` são constantes: `x = 3`, `z = -2`. A equação de `y` varia livremente.
- **Resposta Final:** `(a) (0, 1, 0) (b) x = 3, z = -2`
- **Alerta pedagógico:** Uma reta paralela a um eixo coordenado tem vetor diretor com 1 nesse eixo e 0 nos outros.

---

### `E01-E04` *(Pertinência de ponto)*
- **Passo a passo:**
  - `x: 1 = 3 - 2t → t = 1`.
  - `y: 3 = 1 + t → t = 2`.
  - `z: 6 = -2 + 4t → t = 2`.
  - Como `t` não é único (1, 2, 2), **não pertence**.
- **Resposta Final:** `nao`
- **Alerta pedagógico:** O mesmo `t` deve satisfazer as três equações simultaneamente.

---

### `E01-E05` *(Conversão simétricas → paramétricas)*
- **Passo a passo:**
  - Seja cada fração igual a `t`.
  - `x = 2 - t`, `y = -3 + 2t`, `z = 5 + 3t`.
  - Para `t = 0`: ponto `(2, -3, 5)`.
- **Resposta Final:** `(a) x = 2 - t, y = -3 + 2t, z = 5 + 3t (b) (2, -3, 5)`
- **Alerta pedagógico:** O ponto de `t = 0` é justamente o ponto `(x_0, y_0, z_0)` das simétricas.

---

## 2. Checagem Independente

### `E01-C01` *(Reta completa por dois pontos)*
- **Passo a passo:**
  - `\vec{v} = \overrightarrow{MN} = N - M = (4 - 0, 0 - 4, 1 - (-3)) = (4, -4, 4)`.
  - **(a)** Vetorial: `r: (0, 4, -3) + t(4, -4, 4)`.
  - **(b)** `t = x/4`. `y = 4 - 4t = 4 - x`. `z = -3 + 4t = -3 + x`.
- **Resposta Final:** `(a) (0, 4, -3) + t(4, -4, 4) (b) y = 4 - x, z = x - 3`
- **Alerta pedagógico:** `\vec{v} = (4, -4, 4)` pode ser simplificado para `(1, -1, 1)` mas mantenha os valores originais para não confundir o aluno.

---

### `E01-C02` *(Pertinência com frações)*
- **Passo a passo:**
  - `x: 7 = 1 + 3t → t = 2`.
  - `y: -5 = -2 - t → t = 3`.
  - `z: 10 = 4 + 2t → t = 3`.
  - `t` não é único (2, 3, 3) → **não pertence**.
- **Resposta Final:** `nao`
- **Alerta pedagógico:** Mesmo que duas coordenadas deem o mesmo `t`, a terceira invalida a pertinência.

---

### `E01-C03` *(Reduzidas a partir de simétricas)*
- **Passo a passo:**
  - `t = \frac{x-5}{3}`.
  - `y = 1 - 2t = 1 - 2(\frac{x-5}{3}) = -\frac{2}{3}x + \frac{13}{3}`.
  - `z = -2 + 4t = -2 + 4(\frac{x-5}{3}) = \frac{4}{3}x - \frac{26}{3}`.
- **Resposta Final:** `y = -2/3 x + 13/3, z = 4/3 x - 26/3`
- **Alerta pedagógico:** Mantenha frações irredutíveis; não converta para decimal.
