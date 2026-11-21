# Gabarito Comentado — Bloco `A06` (Matriz Transposta e Propriedade Reversa `(AB)^T = B^T A^T`)

> **Bloco de referência:** [A06_bloco.md](../blocos/A06_bloco.md)

---

## 1. Exercícios

### `A06-E01` *(Transposta e linearidade `(2A - B)^T`)*
- **Passo a passo:**
  - **(a)** Trocando linhas de $A_{(2,3)}$ por colunas:
    $$A^T = \begin{bmatrix} 2 & 0 \\ -1 & 3 \\ 4 & -5 \end{bmatrix}.$$
  - **(b)** Calculando $2A - B$:
    $$2A - B = \begin{bmatrix} 4-1 & -2-2 & 8-(-3) \\ 0-(-4) & 6-1 & -10-2 \end{bmatrix} = \begin{bmatrix} 3 & -4 & 11 \\ 4 & 5 & -12 \end{bmatrix}.$$
    Transpondo:
    $$(2A - B)^T = \begin{bmatrix} 3 & 4 \\ -4 & 5 \\ 11 & -12 \end{bmatrix}.$$
- **Resposta Final:** `(a) [[2, 0], [-1, 3], [4, -5]] (b) [[3, 4], [-4, 5], [11, -12]]`
- **Alerta pedagógico:** A ordem $2 \times 3$ passa obrigatoriamente a $3 \times 2$ ao transpor.

---

### `A06-E02` *(Combinação linear envolvendo `A^T`)*
- **Passo a passo:**
  - $A^T = \begin{bmatrix} 1 & 3 & -1 \\ -2 & 0 & 4 \end{bmatrix} \implies 3A^T = \begin{bmatrix} 3 & 9 & -3 \\ -6 & 0 & 12 \end{bmatrix}$.
  - $-2B = \begin{bmatrix} -4 & -2 & 6 \\ 0 & 2 & -4 \end{bmatrix}$.
  - Somando:
    $$X = \begin{bmatrix} 3-4 & 9-2 & -3+6 \\ -6+0 & 0+2 & 12-4 \end{bmatrix} = \begin{bmatrix} -1 & 7 & 3 \\ -6 & 2 & 8 \end{bmatrix}.$$
- **Resposta Final:** `[[-1, 7, 3], [-6, 2, 8]]`
- **Alerta pedagógico:** Só é possível somar $3A^T$ e $-2B$ após transpor $A_{(3,2)}$ para $(2,3)$, igualando à ordem de $B_{(2,3)}$.

---

### `A06-E03` *(Produto transposto `(AB)^T`)*
- **Passo a passo:**
  - **(a)** Ordem $(3,2)\times(2,2) \to (3,2)$:
    - Linha 1: $[1(2)+(-2)(3),\; 1(-1)+(-2)(4)] = [-4,\; -9]$.
    - Linha 2: $[3(2)+0(3),\; 3(-1)+0(4)] = [6,\; -3]$.
    - Linha 3: $[-1(2)+4(3),\; -1(-1)+4(4)] = [10,\; 17]$.
    $$AB = \begin{bmatrix} -4 & -9 \\ 6 & -3 \\ 10 & 17 \end{bmatrix}$$
  - **(b)** Transpondo $AB$:
    $$(AB)^T = \begin{bmatrix} -4 & 6 & 10 \\ -9 & -3 & 17 \end{bmatrix}.$$
    *(Conferência via $B^T A^T = \begin{bmatrix} 2 & 3 \\ -1 & 4 \end{bmatrix}\begin{bmatrix} 1 & 3 & -1 \\ -2 & 0 & 4 \end{bmatrix} = \begin{bmatrix} -4 & 6 & 10 \\ -9 & -3 & 17 \end{bmatrix}$.)*
- **Resposta Final:** `(a) [[-4, -9], [6, -3], [10, 17]] (b) [[-4, 6, 10], [-9, -3, 17]]`
- **Alerta pedagógico:** Observe que $(AB)^T = B^T A^T$, nunca $A^T B^T$.

---

### `A06-E04` *(Uso direto de `B^T A^T` e equação com `X^T`)*
- **Passo a passo:**
  - **(a)** $B^T = \begin{bmatrix} 2 & 1 & -1 \\ -3 & 4 & 0 \end{bmatrix}$ e $A^T = \begin{bmatrix} 1 & 3 \\ 0 & -1 \\ -2 & 2 \end{bmatrix}$.
    $$B^T A^T = \begin{bmatrix} 2(1)+1(0)+(-1)(-2) & 2(3)+1(-1)+(-1)(2) \\ (-3)(1)+4(0)+0(-2) & (-3)(3)+4(-1)+0(2) \end{bmatrix} = \begin{bmatrix} 4 & 3 \\ -3 & -13 \end{bmatrix}.$$
  - **(b)** Isolando $X^T$: $X^T = N^T - 2M$.
    $$N^T = \begin{bmatrix} 5 & -1 \\ 0 & 2 \end{bmatrix}, \quad 2M = \begin{bmatrix} 2 & -4 \\ 6 & 8 \end{bmatrix} \implies X^T = \begin{bmatrix} 3 & 3 \\ -6 & -6 \end{bmatrix}.$$
    Transpondo ambos os lados:
    $$X = (X^T)^T = \begin{bmatrix} 3 & -6 \\ 3 & -6 \end{bmatrix}.$$
- **Resposta Final:** `(a) [[4, 3], [-3, -13]] (b) [[3, -6], [3, -6]]`
- **Alerta pedagógico:** No item (b), o enunciado pede $X$, e não $X^T$; não pare no passo intermediário!

---

### `A06-E05` *(Expressão mista com produto e transposição)*
- **Passo a passo:**
  - Primeiro $A^T = \begin{bmatrix} 1 & 0 \\ -2 & 3 \end{bmatrix}$.
  - Produto $A^T B = \begin{bmatrix} 1 & 0 \\ -2 & 3 \end{bmatrix} \begin{bmatrix} 2 & 1 \\ -1 & 4 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ -7 & 10 \end{bmatrix}$.
  - Subtraindo $C$: $A^T B - C = \begin{bmatrix} 2-3 & 1-(-2) \\ -7-1 & 10-5 \end{bmatrix} = \begin{bmatrix} -1 & 3 \\ -8 & 5 \end{bmatrix}$.
  - Transpondo o resultado:
    $$(A^T B - C)^T = \begin{bmatrix} -1 & -8 \\ 3 & 5 \end{bmatrix}.$$
- **Resposta Final:** `[[-1, -8], [3, 5]]`
- **Alerta pedagógico:** Respeite a ordem dos parênteses: primeiro calcule o interior ($A^T B - C$) e só no fim transponha.

---

## 2. Checagem Independente

### `A06-C01` *(Linearidade e produto transposto)*
- **Passo a passo:**
  - **(a)** $A^T = \begin{bmatrix} 1 & 3 \\ -2 & 4 \\ 0 & -1 \end{bmatrix}$ e $2B = \begin{bmatrix} 4 & 2 \\ -2 & 6 \\ 8 & -4 \end{bmatrix}$.
    $$A^T + 2B = \begin{bmatrix} 5 & 5 \\ -4 & 10 \\ 8 & -5 \end{bmatrix}.$$
  - **(b)** $AB = \begin{bmatrix} 1(2)+(-2)(-1)+0(4) & 1(1)+(-2)(3)+0(-2) \\ 3(2)+4(-1)+(-1)(4) & 3(1)+4(3)+(-1)(-2) \end{bmatrix} = \begin{bmatrix} 4 & -5 \\ -2 & 17 \end{bmatrix}$.
    Logo:
    $$(AB)^T = \begin{bmatrix} 4 & -2 \\ -5 & 17 \end{bmatrix}.$$
- **Resposta Final:** `(a) [[5, 5], [-4, 10], [8, -5]] (b) [[4, -2], [-5, 17]]`
- **Alerta pedagógico:** Em $(AB)_{22}$, $3(1) + 4(3) + (-1)(-2) = 3 + 12 + 2 = 17$.

---

### `A06-C02` *(Aplicação direta da regra reversa)*
- **Passo a passo:**
  - $Q^T = \begin{bmatrix} 2 & 0 \\ -1 & 3 \\ 4 & 1 \end{bmatrix}$ ($3 \times 2$) e $P^T = \begin{bmatrix} 1 & -1 & 3 \\ 2 & 0 & -2 \end{bmatrix}$ ($2 \times 3$).
  - Multiplicando $Q^T \cdot P^T$ ($3 \times 3$):
    - Linha 1: $[2(1)+0(2),\; 2(-1)+0(0),\; 2(3)+0(-2)] = [2,\; -2,\; 6]$.
    - Linha 2: $[-1(1)+3(2),\; -1(-1)+3(0),\; -1(3)+3(-2)] = [5,\; 1,\; -9]$.
    - Linha 3: $[4(1)+1(2),\; 4(-1)+1(0),\; 4(3)+1(-2)] = [6,\; -4,\; 10]$.
  $$Q^T P^T = \begin{bmatrix} 2 & -2 & 6 \\ 5 & 1 & -9 \\ 6 & -4 & 10 \end{bmatrix}$$
- **Resposta Final:** `[[2, -2, 6], [5, 1, -9], [6, -4, 10]]`
- **Alerta pedagógico:** Note que $Q^T P^T$ coincide com $(PQ)^T$.

---

### `A06-C03` *(Equação matricial sob transposta)*
- **Passo a passo:**
  - Aplicando transposição nos dois lados de $(2X - A)^T = 3B$:
    $$2X - A = 3B^T \implies 2X = 3B^T + A.$$
  - $B^T = \begin{bmatrix} 2 & 0 \\ -1 & 5 \end{bmatrix} \implies 3B^T = \begin{bmatrix} 6 & 0 \\ -3 & 15 \end{bmatrix}$.
  - $3B^T + A = \begin{bmatrix} 6+1 & 0+4 \\ -3-2 & 15+3 \end{bmatrix} = \begin{bmatrix} 7 & 4 \\ -5 & 18 \end{bmatrix}$.
  - Dividindo por $2$:
    $$X = \begin{bmatrix} 7/2 & 2 \\ -5/2 & 9 \end{bmatrix}.$$
- **Resposta Final:** `[[7/2, 2], [-5/2, 9]]`
- **Alerta pedagógico:** Transpor a equação inteira logo no início evita carregar $X^T$ até o final e simplifica o isolamento de $X$.
