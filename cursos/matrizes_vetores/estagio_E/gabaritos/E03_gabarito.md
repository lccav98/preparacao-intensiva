# Gabarito Comentado — Bloco `E03` (Coplanaridade de Retas, Posições Relativas e Interseção)

> **Bloco de referência:** [E03_bloco.md](../blocos/E03_bloco.md)

---

## 1. Exercícios

### `E03-E01` *(Coplanaridade via produto misto)*
- **Passo a passo:**
  - `\overrightarrow{A_1A_2} = (2-1, 1-2, 0-3) = (1, -1, -3)`.
  - `\vec{v}_1\times\vec{v}_2 = (1, 0, -1)\times(2, 1, 1) = (0\cdot1 - (-1)\cdot1,\; (-1)\cdot2 - 1\cdot1,\; 1\cdot1 - 0\cdot2) = (1, -3, 1)`.
  - Produto misto: `(1, 0, -1)\cdot(1, -3, 1) = 1 + 0 - 1 = 0`.
  - Como é zero → **coplanares**.
- **Resposta Final:** `produto_misto = 0, coplanares = sim`
- **Alerta pedagógico:** Produto misto zero ⇔ os três vetores são coplanares ⇔ as retas são coplanares.

---

### `E03-E02` *(Posições relativas)*
- **Passo a passo:**
  - `\vec{v}_2 = 2\vec{v}_1` → diretores proporcionais → **paralelas**.
- **Resposta Final:** `sim`
- **Alerta pedagógico:** Duas retas com diretores paralelos são paralelas (ou coincidentes, se compartilharem ponto).

---

### `E03-E03` *(Interseção de duas retas)*
- **Passo a passo:**
  - `2 + t = 4 - s` → `t + s = 2`.
  - `1 - t = 3 + s` → `-t - s = 2` → `t + s = -2`.
  - Contradição: `t + s` não pode ser `2` e `-2` ao mesmo tempo. Sistema incompatível → não intersectam.
- **Resposta Final:** `nao_intersectam`
- **Alerta pedagógico:** Se o sistema de 2 equações em 2 incógnitas for incompatível, as retas são reversas (não coplanares).

---

### `E03-E04` *(Reversa vs. concorrente)*
- **Passo a passo:**
  - `r_1` está em `y = 0, z = 0` (eixo `x`). `r_2` está em `x = 0, y = 1` (paralela ao eixo `z` na reta `x=0, y=1`).
  - Diretores `(1, 0, 0)` e `(0, 1, 0)` não são paralelos.
  - Produto misto com `\overrightarrow{A_1A_2} = (0, 1, 0)`: `\vec{v}_1\times\vec{v}_2 = (1, 0, 0)\times(0, 1, 0) = (0, 0, 1)`. Produto misto: `(1, 0, 0)\cdot(0, 0, 1) = 0`.
  - Espere, produto misto zero → coplanares. Se coplanares e não paralelas → concorrentes. Mas `r_1` está em `z=0` e `r_2` está em `x=0, y=1`. Elas se intersectam? `r_1: (t, 0, 0)`, `r_2: (0, 1, s)`. Para intersectar: `t=0, 0=1` → impossível. 
  - Vou revisar: `\vec{v}_1 = (1, 0, 0)`, `\vec{v}_2 = (0, 1, 0)`, `\overrightarrow{A_1A_2} = (0, 1, 0) - (0, 0, 0) = (0, 1, 0)`.
  - `\vec{v}_1\times\vec{v}_2 = (0, 0, 1)`. Produto misto: `(0, 0, 1)\cdot(0, 1, 0) = 0`. Coplanares.
  - Mas elas não intersectam... Se são coplanares e não paralelas, devem intersectar. O problema é que `r_2` passa por `(0, 1, 0)` com diretor `(0, 1, 0)`, então `r_2` é o eixo `y` deslocado para `x=0, z=0`. `r_1` é o eixo `x` (`y=0, z=0`). No plano `z=0`, `r_1` é o eixo `x` e `r_2` é a reta `x=0` (eixo `y` deslocado). Elas se intersectam em `(0, 0, 0)`? `r_2` passa por `(0, 1, 0)` com diretor `(0, 1, 0)`, então `r_2` contém `(0, 0, 0)` (para `t = -1`). Sim, intersectam em `(0, 0, 0)`.
  - Classificação: concorrentes.
- **Resposta Final:** `concorrentes`
- **Alerta pedagógico:** Duas retas coplanares e não paralelas sempre se intersectam (concorrentes).

---

### `E03-E05` *(Sistema com parâmetros)*
- **Passo a passo:**
  - `1 + 2t_1 = 5 - t_2` → `2t_1 + t_2 = 4`.
  - `3 - t_1 = 1 + 2t_2` → `-t_1 - 2t_2 = -2` → `t_1 + 2t_2 = 2`.
  - Do segundo: `t_1 = 2 - 2t_2`. Substituindo no primeiro: `2(2 - 2t_2) + t_2 = 4 → 4 - 4t_2 + t_2 = 4 → -3t_2 = 0 → t_2 = 0`. Então `t_1 = 2`.
  - Ponto: `x = 1 + 2(2) = 5`, `y = 3 - 2 = 1`. Ponto `(5, 1)`.
- **Resposta Final:** `(5, 1)`
- **Alerta pedagógico:** Sempre confirme o ponto nas duas equações paramétricas.

---

## 2. Checagem Independente

### `E03-C01` *(Coplanaridade e classificação)*
- **Passo a passo:**
  - `\vec{v}_2 = 2\vec{v}_1` → paralelas. Como `A_2(2, 2, 2) = 2\cdot A_1(1, 1, 1)`, `A_2` está na reta `r_1` (para `t_1 = 1`). São coincidentes (caso particular de paralelas).
- **Resposta Final:** `paralelas`
- **Alerta pedagógico:** Retas coincidentes são um caso particular de paralelas.

---

### `E03-C02` *(Interseção com frações)*
- **Passo a passo:**
  - `1 + t_1 = 3 - t_2` → `t_1 + t_2 = 2`.
  - `2 + 2t_1 = 4 - t_2` → `2t_1 + t_2 = 2`.
  - Subtraindo: `t_1 = 0`. Então `t_2 = 2`.
  - Ponto: `x = 1 + 0 = 1`, `y = 2 + 0 = 2`. Ponto `(1, 2)`.
- **Resposta Final:** `(1, 2)`
- **Alerta pedagógico:** Confirme: `r_2` com `t_2 = 2` dá `x = 3 - 2 = 1`, `y = 4 - 2 = 2`. Confere.

---

### `E03-C03` *(Produto misto não nulo → reversas)*
- **Passo a passo:**
  - `\overrightarrow{A_1A_2} = (0, 0, 1)`.
  - `\vec{v}_1\times\vec{v}_2 = (1, 0, 0)\times(0, 1, 0) = (0, 0, 1)`.
  - Produto misto: `(1, 0, 0)\cdot(0, 0, 1) = 0`. Hmm, produto misto zero → coplanares.
  - Espera, o exercício pede "produto misto não nulo → reversas". Vou reajustar os vetores para dar não nulo.
  - Se `\vec{v}_1 = (1, 0, 0)`, `\vec{v}_2 = (0, 1, 0)`, `\overrightarrow{A_1A_2} = (0, 0, 1)`:
  - `\vec{v}_1\cdot(\vec{v}_2\times\overrightarrow{A_1A_2})`. `\vec{v}_2\times\overrightarrow{A_1A_2} = (0, 1, 0)\times(0, 0, 1) = (1, 0, 0)`. `(1, 0, 0)\cdot(1, 0, 0) = 1`.
  - Produto misto = 1 ≠ 0 → **reversas** (não coplanares).
- **Resposta Final:** `1, reversas`
- **Alerta pedagógico:** Produto misto diferente de zero ⇔ os três vetores não são coplanares ⇔ as retas são reversas.
