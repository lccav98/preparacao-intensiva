# Gabarito Comentado — Bloco `A03` (Adição, Subtração e Multiplicação por Escalar)

> **Bloco de referência:** [A03_bloco.md](../blocos/A03_bloco.md)

---

## 1. Exercícios

### `A03-E01` *(Adição e subtração direta)*
- **Passo a passo:**
  - **(a)** $A + B = \begin{bmatrix} 2+(-1) & -3+6 & 5+(-4) \\ 1+3 & 4+(-2) & -2+7 \end{bmatrix} = \begin{bmatrix} 1 & 3 & 1 \\ 4 & 2 & 5 \end{bmatrix}$.
  - **(b)** $A - B = \begin{bmatrix} 2-(-1) & -3-6 & 5-(-4) \\ 1-3 & 4-(-2) & -2-7 \end{bmatrix} = \begin{bmatrix} 3 & -9 & 9 \\ -2 & 6 & -9 \end{bmatrix}$.
- **Resposta Final:** `(a) [[1, 3, 1], [4, 2, 5]] (b) [[3, -9, 9], [-2, 6, -9]]`
- **Alerta pedagógico:** Em $A - B$, subtrair um número negativo equivale a somar ($5 - (-4) = 9$ e $4 - (-2) = 6$).

---

### `A03-E02` *(Combinação linear com três matrizes)*
- **Passo a passo:**
  - $2A = \begin{bmatrix} 4 & -6 & 10 \\ 2 & 8 & -4 \end{bmatrix}$
  - $-3B = \begin{bmatrix} 3 & -18 & 12 \\ -9 & 6 & -21 \end{bmatrix}$
  - $4C = \begin{bmatrix} 4 & -8 & 0 \\ -16 & 20 & 12 \end{bmatrix}$
  - Somando posição a posição:
    - Linha 1: $(4+3+4,\; -6-18-8,\; 10+12+0) = (11,\; -32,\; 22)$.
    - Linha 2: $(2-9-16,\; 8+6+20,\; -4-21+12) = (-23,\; 34,\; -13)$.
- **Resposta Final:** `[[11, -32, 22], [-23, 34, -13]]`
- **Alerta pedagógico:** Calcular explicitamente $-3B$ e somar as três matrizes reduz drasticamente erros de troca de sinal.

---

### `A03-E03` *(Escalares fracionários e matriz identidade)*
- **Passo a passo:**
  - $\frac{1}{2}A = \begin{bmatrix} 2 & -3 \\ 1 & 4 \end{bmatrix}$
  - $-\frac{2}{3}B = \begin{bmatrix} -2 & 6 \\ -4 & -2/3 \end{bmatrix}$
  - $I_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$
  - Somando:
    $$X = \begin{bmatrix} 2-2+1 & -3+6+0 \\ 1-4+0 & 4 - \frac{2}{3} + 1 \end{bmatrix} = \begin{bmatrix} 1 & 3 \\ -3 & \frac{13}{3} \end{bmatrix}$$
    *(Nota: $5 - \frac{2}{3} = \frac{15 - 2}{3} = \frac{13}{3}$.)*
- **Resposta Final:** `[[1, 3], [-3, 13/3]]`
- **Alerta pedagógico:** Não deixe `13/3` como `4.333`; mantenha sempre a fração imprópria irredutível.

---

### `A03-E04` *(Equação matricial linear com `X` isolado)*
- **Passo a passo:**
  - Isolando $X$: $3X = 5B - I_2 - 2A \implies X = \frac{1}{3}(5B - I_2 - 2A)$.
  - $5B = \begin{bmatrix} 10 & 5 \\ -5 & 15 \end{bmatrix}$, $-I_2 = \begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix}$, $-2A = \begin{bmatrix} -2 & 4 \\ -8 & 0 \end{bmatrix}$.
  - $5B - I_2 - 2A = \begin{bmatrix} 10-1-2 & 5+0+4 \\ -5+0-8 & 15-1+0 \end{bmatrix} = \begin{bmatrix} 7 & 9 \\ -13 & 14 \end{bmatrix}$.
  - Dividindo todos os elementos por $3$:
    $$X = \begin{bmatrix} 7/3 & 3 \\ -13/3 & 14/3 \end{bmatrix}$$
- **Resposta Final:** `[[7/3, 3], [-13/3, 14/3]]`
- **Alerta pedagógico:** Ao multiplicar por $1/3$, não esqueça de dividir **todos** os quatro elementos (inclusive $9/3 = 3$).

---

### `A03-E05` *(Sistema linear matricial `2x2`)*
- **Passo a passo:**
  - Somando as duas equações $(2X + Y) + (X - Y) = A + B$:
    $$3X = A + B = \begin{bmatrix} 5+1 & -1+4 \\ 4-1 & 7+2 \end{bmatrix} = \begin{bmatrix} 6 & 3 \\ 3 & 9 \end{bmatrix} \implies X = \frac{1}{3}\begin{bmatrix} 6 & 3 \\ 3 & 9 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix}.$$
  - Da segunda equação, $Y = X - B$:
    $$Y = \begin{bmatrix} 2-1 & 1-4 \\ 1-(-1) & 3-2 \end{bmatrix} = \begin{bmatrix} 1 & -3 \\ 2 & 1 \end{bmatrix}.$$
  - Conferência: $2X + Y = \begin{bmatrix} 4+1 & 2-3 \\ 2+2 & 6+1 \end{bmatrix} = \begin{bmatrix} 5 & -1 \\ 4 & 7 \end{bmatrix} = A$.
- **Resposta Final:** `(a) [[2, 1], [1, 3]] (b) [[1, -3], [2, 1]]`
- **Alerta pedagógico:** Sistemas lineares de matrizes podem ser resolvidos por eliminação (somando/subtraindo equações) exatamente como sistemas numéricos comuns.

---

## 2. Checagem Independente

### `A03-C01` *(Combinação linear inédita `2x3`)*
- **Passo a passo:**
  - $3A = \begin{bmatrix} 3 & -9 & 6 \\ 0 & 12 & -3 \end{bmatrix}$
  - $-2B = \begin{bmatrix} 4 & -2 & -10 \\ -6 & 2 & -4 \end{bmatrix}$
  - $C = \begin{bmatrix} 4 & 0 & -3 \\ -2 & 5 & 1 \end{bmatrix}$
  - Somando:
    $$M = \begin{bmatrix} 3+4+4 & -9-2+0 & 6-10-3 \\ 0-6-2 & 12+2+5 & -3-4+1 \end{bmatrix} = \begin{bmatrix} 11 & -11 & -7 \\ -8 & 19 & -6 \end{bmatrix}.$$
- **Resposta Final:** `[[11, -11, -7], [-8, 19, -6]]`
- **Alerta pedagógico:** Atenção redobrada ao multiplicar $B$ por $-2$, especialmente nos termos positivos que se tornam negativos.

---

### `A03-C02` *(Equação matricial com divisão por escalar)*
- **Passo a passo:**
  - Isolando $X$: $2X = 3A + B + 4I_2 \implies X = \frac{1}{2}(3A + B + 4I_2)$.
  - $3A = \begin{bmatrix} 3 & -6 \\ 9 & 0 \end{bmatrix}$, $B = \begin{bmatrix} -1 & 4 \\ 2 & 5 \end{bmatrix}$, $4I_2 = \begin{bmatrix} 4 & 0 \\ 0 & 4 \end{bmatrix}$.
  - $3A + B + 4I_2 = \begin{bmatrix} 3-1+4 & -6+4+0 \\ 9+2+0 & 0+5+4 \end{bmatrix} = \begin{bmatrix} 6 & -2 \\ 11 & 9 \end{bmatrix}$.
  - Dividindo por $2$:
    $$X = \begin{bmatrix} 3 & -1 \\ 11/2 & 9/2 \end{bmatrix}.$$
- **Resposta Final:** `[[3, -1], [11/2, 9/2]]`
- **Alerta pedagógico:** Em $4I_2$, apenas a diagonal principal recebe $+4$; os elementos $(1,2)$ e $(2,1)$ recebem $0$.

---

### `A03-C03` *(Sistema matricial inédito)*
- **Passo a passo:**
  - Multiplicando a 2ª equação por $2$: $4X - 2Y = 2B$. Somando com a 1ª ($X + 2Y = A$):
    $$5X = A + 2B = \begin{bmatrix} 3+2 & -4+14 \\ 1+4 & 5+0 \end{bmatrix} = \begin{bmatrix} 5 & 10 \\ 5 & 5 \end{bmatrix} \implies X = \begin{bmatrix} 1 & 2 \\ 1 & 1 \end{bmatrix}.$$
  - Substituindo em $Y = 2X - B$:
    $$Y = \begin{bmatrix} 2-1 & 4-7 \\ 2-2 & 2-0 \end{bmatrix} = \begin{bmatrix} 1 & -3 \\ 0 & 2 \end{bmatrix}.$$
  - Conferência em $X + 2Y$: $\begin{bmatrix} 1+2 & 2-6 \\ 1+0 & 1+4 \end{bmatrix} = \begin{bmatrix} 3 & -4 \\ 1 & 5 \end{bmatrix} = A$.
- **Resposta Final:** `(a) [[1, 2], [1, 1]] (b) [[1, -3], [0, 2]]`
- **Alerta pedagógico:** Sempre confira o par $(X, Y)$ encontrado na equação que não foi usada no último passo.
