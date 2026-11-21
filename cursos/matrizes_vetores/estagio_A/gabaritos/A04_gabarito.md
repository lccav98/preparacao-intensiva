# Gabarito Comentado — Bloco `A04` (Produto de Matrizes e Forma Matricial `AX = B`)

> **Bloco de referência:** [A04_bloco.md](../blocos/A04_bloco.md)

---

## 1. Exercícios

### `A04-E01` *(Compatibilidade dimensional e ordem resultante)*
- **Passo a passo:**
  - **(a)** $A_{(3,4)} \times B_{(4,2)}$: os meios coincidem ($4 = 4$), resultando nos extremos $(3, 2)$.
  - **(b)** $B_{(4,2)} \times C_{(2,3)}$: os meios coincidem ($2 = 2$), resultando nos extremos $(4, 3)$.
  - **(c)** Em $C_{(2,3)} \times A_{(3,4)} \times B_{(4,2)}$: primeiro $(C \cdot A)$ tem ordem $(2, 4)$; depois $(CA)_{(2,4)} \times B_{(4,2)}$ tem ordem $(2, 2)$.
- **Resposta Final:** `(a) (3, 2) (b) (4, 3) (c) (2, 2)`
- **Alerta pedagógico:** Sempre verifique se o número de colunas da matriz à esquerda coincide com o número de linhas da matriz à direita.

---

### `A04-E02` *(Produto `2x2` por `2x3`)*
- **Passo a passo:**
  - Ordem $(2,2) \times (2,3) \to (2,3)$:
    - $c_{11} = 2(1) + (-1)(5) = 2 - 5 = -3$
    - $c_{12} = 2(0) + (-1)(-3) = 0 + 3 = 3$
    - $c_{13} = 2(-2) + (-1)(1) = -4 - 1 = -5$
    - $c_{21} = 3(1) + 4(5) = 3 + 20 = 23$
    - $c_{22} = 3(0) + 4(-3) = 0 - 12 = -12$
    - $c_{23} = 3(-2) + 4(1) = -6 + 4 = -2$
  $$AB = \begin{bmatrix} -3 & 3 & -5 \\ 23 & -12 & -2 \end{bmatrix}$$
- **Resposta Final:** `[[-3, 3, -5], [23, -12, -2]]`
- **Alerta pedagógico:** Note que $B \cdot A$ nem sequer existiria aqui, pois $(2,3) \times (2,2)$ é incompatível ($3 \neq 2$).

---

### `A04-E03` *(Produto `3x2` por `2x2` com frações)*
- **Passo a passo:**
  - Ordem $(3,2) \times (2,2) \to (3,2)$:
    - Linha 1: $c_{11} = \frac{1}{2}(4) + (-1)(3) = 2 - 3 = -1$; $\;c_{12} = \frac{1}{2}(-2) + (-1)(6) = -1 - 6 = -7$.
    - Linha 2: $c_{21} = 2(4) + \frac{1}{3}(3) = 8 + 1 = 9$; $\;c_{22} = 2(-2) + \frac{1}{3}(6) = -4 + 2 = -2$.
    - Linha 3: $c_{31} = (-3)(4) + 2(3) = -12 + 6 = -6$; $\;c_{32} = (-3)(-2) + 2(6) = 6 + 12 = 18$.
  $$AB = \begin{bmatrix} -1 & -7 \\ 9 & -2 \\ -6 & 18 \end{bmatrix}$$
- **Resposta Final:** `[[-1, -7], [9, -2], [-6, 18]]`
- **Alerta pedagógico:** Simplifique produtos de frações antes de somar (ex.: $\frac{1}{3} \cdot 6 = 2$).

---

### `A04-E04` *(Multiplicação `AX` por matriz coluna)*
- **Passo a passo:**
  - Ordem $(3,3) \times (3,1) \to (3,1)$:
    - Linha 1: $2(2) + (-1)(-4) + \frac{1}{2}(6) = 4 + 4 + 3 = 11$.
    - Linha 2: $0(2) + 3(-4) + (-2)(6) = 0 - 12 - 12 = -24$.
    - Linha 3: $1(2) + \frac{1}{2}(-4) + 4(6) = 2 - 2 + 24 = 24$.
  $$AX = \begin{bmatrix} 11 \\ -24 \\ 24 \end{bmatrix}$$
- **Resposta Final:** `[[11], [-24], [24]]`
- **Alerta pedagógico:** O produto de uma matriz $3 \times 3$ por uma matriz coluna $3 \times 1$ resulta sempre em uma nova matriz coluna $3 \times 1$ (e não em uma linha $1 \times 3$).

---

### `A04-E05` *(Forma matricial `AX = B` e verificação de solução)*
- **Passo a passo:**
  - **(a)** Lendo os coeficientes na ordem $(x, y, z)$:
    $$A = \begin{bmatrix} 2 & -1 & 3 \\ 1 & 4 & -2 \\ -3 & 2 & 1 \end{bmatrix}$$
  - **(b)** Termos independentes à direita do sinal `=`:
    $$B = \begin{bmatrix} 13 \\ -13 \\ -4 \end{bmatrix}$$
  - **(c)** Calculando $A \cdot X_0$:
    - Linha 1: $2(1) - 1(-2) + 3(3) = 2 + 2 + 9 = 13$.
    - Linha 2: $1(1) + 4(-2) - 2(3) = 1 - 8 - 6 = -13$.
    - Linha 3: $-3(1) + 2(-2) + 1(3) = -3 - 4 + 3 = -4$.
    Como $A \cdot X_0 = B$, $X_0$ é solução do sistema.
- **Resposta Final:** `(a) [[2, -1, 3], [1, 4, -2], [-3, 2, 1]] (b) [[13], [-13], [-4]] (c) [[13], [-13], [-4]]`
- **Alerta pedagógico:** Mantenha as colunas de $A$ rigorosamente alinhadas com as variáveis $(x, y, z)$ e lembre que `[[13], [-13], [-4]]` é coluna $3\times 1$.

---

## 2. Checagem Independente

### `A04-C01` *(Produto `2x3` por `3x2`)*
- **Passo a passo:**
  - Ordem $(2,3) \times (3,2) \to (2,2)$:
    - $c_{11} = 1(2) + (-2)(-3) + 3(0) = 2 + 6 + 0 = 8$
    - $c_{12} = 1(1) + (-2)(5) + 3(2) = 1 - 10 + 6 = -3$
    - $c_{21} = 4(2) + 0(-3) + (-1)(0) = 8$
    - $c_{22} = 4(1) + 0(5) + (-1)(2) = 4 - 2 = 2$
  $$AB = \begin{bmatrix} 8 & -3 \\ 8 & 2 \end{bmatrix}$$
- **Resposta Final:** `[[8, -3], [8, 2]]`
- **Alerta pedagógico:** O produto $(2,3)\times(3,2)$ gera uma matriz quadrada $2 \times 2$.

---

### `A04-C02` *(Ordem inversa `3x2` por `2x3`)*
- **Passo a passo:**
  - Ordem $(3,2) \times (2,3) \to (3,3)$:
    - Linha 1 de $B$: $[2, 1]$
      - $(1,1) = 2(1) + 1(4) = 6$; $\;(1,2) = 2(-2) + 1(0) = -4$; $\;(1,3) = 2(3) + 1(-1) = 5$.
    - Linha 2 de $B$: $[-3, 5]$
      - $(2,1) = -3(1) + 5(4) = 17$; $\;(2,2) = -3(-2) + 5(0) = 6$; $\;(2,3) = -3(3) + 5(-1) = -14$.
    - Linha 3 de $B$: $[0, 2]$
      - $(3,1) = 0(1) + 2(4) = 8$; $\;(3,2) = 0(-2) + 2(0) = 0$; $\;(3,3) = 0(3) + 2(-1) = -2$.
  $$BA = \begin{bmatrix} 6 & -4 & 5 \\ 17 & 6 & -14 \\ 8 & 0 & -2 \end{bmatrix}$$
- **Resposta Final:** `[[6, -4, 5], [17, 6, -14], [8, 0, -2]]`
- **Alerta pedagógico:** Compare `A04-C01` ($2\times 2$) com `A04-C02` ($3\times 3$): além de não serem comutativas, $AB$ e $BA$ podem ter ordens completamente diferentes!

---

### `A04-C03` *(Sistema com coeficiente nulo na forma `AX = B`)*
- **Passo a passo:**
  - **(a)** Na 3ª equação, $x$ não aparece, logo seu coeficiente é $0$:
    $$A = \begin{bmatrix} 1 & 2 & -1 \\ 3 & -1 & 2 \\ 0 & 4 & 1 \end{bmatrix}$$
  - **(b)** Vetor coluna dos termos independentes:
    $$B = \begin{bmatrix} 3 \\ 4 \\ -1 \end{bmatrix}$$
  - **(c)** Calculando $A \cdot X_0$:
    - Linha 1: $1(2) + 2(0) - 1(-1) = 2 + 0 + 1 = 3$.
    - Linha 2: $3(2) - 1(0) + 2(-1) = 6 - 0 - 2 = 4$.
    - Linha 3: $0(2) + 4(0) + 1(-1) = -1$.
- **Resposta Final:** `(a) [[1, 2, -1], [3, -1, 2], [0, 4, 1]] (b) [[3], [4], [-1]] (c) [[3], [4], [-1]]`
- **Alerta pedagógico:** Erro clássico em sistemas com variáveis ausentes: deslocar `4` para a 1ª coluna em vez de preencher `0` na coluna de $x$.
