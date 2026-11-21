# Gabarito Comentado — Bloco `A08` (Potências de Matrizes e Classificação Especial)

> **Bloco de referência:** [A08_bloco.md](../blocos/A08_bloco.md)

---

## 1. Exercícios

### `A08-E01` *(Identificação de matriz idempotente)*
- **Passo a passo:**
  - **(a)** $J^2 = \begin{bmatrix} 3 & -6 \\ 1 & -2 \end{bmatrix} \begin{bmatrix} 3 & -6 \\ 1 & -2 \end{bmatrix} = \begin{bmatrix} 9-6 & -18+12 \\ 3-2 & -6+4 \end{bmatrix} = \begin{bmatrix} 3 & -6 \\ 1 & -2 \end{bmatrix}$.
  - **(b)** Como $J^2 = J$, $J$ é **idempotente**.
- **Resposta Final:** `(a) [[3, -6], [1, -2]] (b) idempotente`
- **Alerta pedagógico:** Não eleve os elementos ao quadrado ($3^2 = 9$); execute sempre o produto linha por coluna $J \cdot J$.

---

### `A08-E02` *(Identificação de matriz nilpotente `2x2`)*
- **Passo a passo:**
  - **(a)** $H^2 = \begin{bmatrix} 4 & 8 \\ -2 & -4 \end{bmatrix} \begin{bmatrix} 4 & 8 \\ -2 & -4 \end{bmatrix} = \begin{bmatrix} 16-16 & 32-32 \\ -8+8 & -16+16 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} = [O]$.
  - **(b)** Como $H \neq [O]$ e $H^2 = [O]$, $H$ é **nilpotente** (de índice $p = 2$).
- **Resposta Final:** `(a) [[0, 0], [0, 0]] (b) nilpotente`
- **Alerta pedagógico:** Toda matriz nilpotente de ordem 2 com $H^2 = [O]$ também satisfaz $H^3 = [O]$, mas o índice é o **menor** expoente positivo ($p = 2$).

---

### `A08-E03` *(Nilpotência de índice `p = 3`)*
- **Passo a passo:**
  - **(a)** $N^2 = \begin{bmatrix} 0 & 2 & -1 \\ 0 & 0 & 3 \\ 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} 0 & 2 & -1 \\ 0 & 0 & 3 \\ 0 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 6 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$.
  - **(b)** $N^3 = N^2 \cdot N = \begin{bmatrix} 0 & 0 & 6 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} 0 & 2 & -1 \\ 0 & 0 & 3 \\ 0 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$.
  - **(c)** Como $N^2 \neq [O]$ e $N^3 = [O]$, o índice de nilpotência é $p = 3$.
- **Resposta Final:** `(a) [[0, 0, 6], [0, 0, 0], [0, 0, 0]] (b) [[0, 0, 0], [0, 0, 0], [0, 0, 0]] (c) 3`
- **Alerta pedagógico:** Em matrizes triangulares superiores com diagonal nula, cada potência desloca os termos não nulos uma diagonal acima até anular tudo na potência $n$.

---

### `A08-E04` *(Matriz periódica e determinação do período `k`)*
- **Passo a passo:**
  - **(a)** $L^2 = \begin{bmatrix} 0 & 1 & -1 \\ 1 & 0 & -1 \\ 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} 0 & 1 & -1 \\ 1 & 0 & -1 \\ 0 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 1 & 0 & -1 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{bmatrix} \neq L$.
  - **(b)** $L^3 = L^2 \cdot L = \begin{bmatrix} 1 & 0 & -1 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} 0 & 1 & -1 \\ 1 & 0 & -1 \\ 0 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 1 & -1 \\ 1 & 0 & -1 \\ 0 & 0 & 0 \end{bmatrix} = L$.
  - **(c)** Como $L^3 = L$ (isto é, $L^{k+1} = L$ com $k + 1 = 3$) e $L^2 \neq L$, o período é $k = 2$.
- **Resposta Final:** `(a) [[1, 0, -1], [0, 1, -1], [0, 0, 0]] (b) [[0, 1, -1], [1, 0, -1], [0, 0, 0]] (c) 2`
- **Alerta pedagógico:** Cuidado clássico: pela definição $A^{k+1} = A$, se $L^3 = L$, o período é $k = 3 - 1 = 2$ (não $3$!).

---

### `A08-E05` *(Produto de matrizes triangulares)*
- **Passo a passo:**
  - **(a)** Calculando $T = R \cdot S$:
    - Linha 1: $[2(1)+0+0,\; 0,\; 0] = [2,\; 0,\; 0]$.
    - Linha 2: $[-1(1)+3(2)+0,\; -1(0)+3(-2)+0,\; 0] = [5,\; -6,\; 0]$.
    - Linha 3: $[4(1)+(-2)(2)+1(-3),\; 4(0)+(-2)(-2)+1(1),\; 1(5)] = [-3,\; 5,\; 5]$.
    $$T = \begin{bmatrix} 2 & 0 & 0 \\ 5 & -6 & 0 \\ -3 & 5 & 5 \end{bmatrix}.$$
  - **(b)** Todos os elementos acima da diagonal principal são nulos ($t_{12}=t_{13}=t_{23}=0$), logo $T$ é **triangular inferior**.
- **Resposta Final:** `(a) [[2, 0, 0], [5, -6, 0], [-3, 5, 5]] (b) triangular inferior`
- **Alerta pedagógico:** Observe que na diagonal principal de $T$, cada elemento é exatamente o produto das diagonais de $R$ e $S$ ($2\cdot 1 = 2$, $3(-2) = -6$, $1\cdot 5 = 5$).

---

## 2. Checagem Independente

### `A08-C01` *(Idempotência inédita)*
- **Passo a passo:**
  - **(a)** $A^2 = \begin{bmatrix} 2 & -2 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} 2 & -2 \\ 1 & -1 \end{bmatrix} = \begin{bmatrix} 4-2 & -4+2 \\ 2-1 & -2+1 \end{bmatrix} = \begin{bmatrix} 2 & -2 \\ 1 & -1 \end{bmatrix}$.
  - **(b)** Como $A^2 = A$, $A$ é **idempotente**.
- **Resposta Final:** `(a) [[2, -2], [1, -1]] (b) idempotente`
- **Alerta pedagógico:** A idempotência aparece quando $A^2 = A$, independentemente de $A$ ser diferente de $I_2$ e de $[O]$.

---

### `A08-C02` *(Nilpotência `3x3` inédita)*
- **Passo a passo:**
  - **(a)** $B^2 = \begin{bmatrix} 0 & 1 & 2 \\ 0 & 0 & -3 \\ 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} 0 & 1 & 2 \\ 0 & 0 & -3 \\ 0 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 0 & -3 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$.
  - **(b)** $B^3 = B^2 \cdot B = \begin{bmatrix} 0 & 0 & -3 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} 0 & 1 & 2 \\ 0 & 0 & -3 \\ 0 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$.
  - **(c)** Como $B^3 = [O]$, $B$ é **nilpotente** (de índice $p = 3$).
- **Resposta Final:** `(a) [[0, 0, -3], [0, 0, 0], [0, 0, 0]] (b) [[0, 0, 0], [0, 0, 0], [0, 0, 0]] (c) nilpotente`
- **Alerta pedagógico:** Não conclua que $B$ não é nilpotente apenas porque $B^2 \neq [O]$; teste até a ordem $n = 3$.

---

### `A08-C03` *(Periodicidade inédita)*
- **Passo a passo:**
  - **(a)** $M^2 = \begin{bmatrix} 2 & 3 \\ -1 & -2 \end{bmatrix} \begin{bmatrix} 2 & 3 \\ -1 & -2 \end{bmatrix} = \begin{bmatrix} 4-3 & 6-6 \\ -2+2 & -3+4 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I_2$.
  - **(b)** $M^3 = M^2 \cdot M = I_2 \cdot M = \begin{bmatrix} 2 & 3 \\ -1 & -2 \end{bmatrix} = M$.
  - **(c)** Como $M^2 \neq M$ e $M^3 = M$, $M$ é **periódica** (de período $k = 2$).
- **Resposta Final:** `(a) [[1, 0], [0, 1]] (b) [[2, 3], [-1, -2]] (c) periodica`
- **Alerta pedagógico:** Quando $M^2 = I$, imediatamente $M^3 = I \cdot M = M$, caracterizando uma matriz periódica de período $2$.
