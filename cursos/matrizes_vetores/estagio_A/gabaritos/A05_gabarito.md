# Gabarito Comentado — Bloco `A05` (Propriedades do Produto, Não-Comutatividade e Associatividade)

> **Bloco de referência:** [A05_bloco.md](../blocos/A05_bloco.md)

---

## 1. Exercícios

### `A05-E01` *(Verificação de não-comutatividade)*
- **Passo a passo:**
  - **(a)** $AB = \begin{bmatrix} 2(1)+(-1)(-2) & 2(4)+(-1)(5) \\ 3(1)+0(-2) & 3(4)+0(5) \end{bmatrix} = \begin{bmatrix} 4 & 3 \\ 3 & 12 \end{bmatrix}$.
  - **(b)** $BA = \begin{bmatrix} 1(2)+4(3) & 1(-1)+4(0) \\ (-2)(2)+5(3) & (-2)(-1)+5(0) \end{bmatrix} = \begin{bmatrix} 14 & -1 \\ 11 & 2 \end{bmatrix}$.
- **Resposta Final:** `(a) [[4, 3], [3, 12]] (b) [[14, -1], [11, 2]]`
- **Alerta pedagógico:** $AB \neq BA$ confirma que o produto matricial não é comutativo.

---

### `A05-E02` *(Divisores de zero e assimetria de `AB` vs. `BA`)*
- **Passo a passo:**
  - **(a)** $AB = \begin{bmatrix} 1(2)+(-2)(1) & 1(6)+(-2)(3) \\ (-2)(2)+4(1) & (-2)(6)+4(3) \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} = [O]$.
  - **(b)** $BA = \begin{bmatrix} 2(1)+6(-2) & 2(-2)+6(4) \\ 1(1)+3(-2) & 1(-2)+3(4) \end{bmatrix} = \begin{bmatrix} -10 & 20 \\ -5 & 10 \end{bmatrix}$.
- **Resposta Final:** `(a) [[0, 0], [0, 0]] (b) [[-10, 20], [-5, 10]]`
- **Alerta pedagógico:** Um produto $AB = [O]$ não garante que $A = [O]$ ou $B = [O]$, e muito menos que $BA$ também será nulo!

---

### `A05-E03` *(Associatividade em produto de três matrizes)*
- **Passo a passo:**
  - **(a)** Calculando $J_{(3,2)} = A_{(3,2)} B_{(2,2)}$:
    - Linha 1: $[1(2)+(-1)(-1),\; 1(3)+(-1)(4)] = [3,\; -1]$.
    - Linha 2: $[2(2)+0(-1),\; 2(3)+0(4)] = [4,\; 6]$.
    - Linha 3: $[-3(2)+1(-1),\; -3(3)+1(4)] = [-7,\; -5]$.
    $$J = \begin{bmatrix} 3 & -1 \\ 4 & 6 \\ -7 & -5 \end{bmatrix}$$
  - **(b)** Calculando $JC = (AB)C$:
    - Linha 1: $[3(1)+(-1)(-2),\; 3(0)+(-1)(3)] = [5,\; -3]$.
    - Linha 2: $[4(1)+6(-2),\; 4(0)+6(3)] = [-8,\; 18]$.
    - Linha 3: $[-7(1)+(-5)(-2),\; -7(0)+(-5)(3)] = [3,\; -15]$.
    *(Conferência via $BC = \begin{bmatrix} -4 & 9 \\ -9 & 12 \end{bmatrix}$: $A(BC)$ fornece exatamente a mesma matriz $3 \times 2$.)*
- **Resposta Final:** `(a) [[3, -1], [4, 6], [-7, -5]] (b) [[5, -3], [-8, 18], [3, -15]]`
- **Alerta pedagógico:** Na associatividade $(AB)C = A(BC)$, pode-se escolher a ordem de agrupamento, mas jamais inverter a sequência dos fatores.

---

### `A05-E04` *(Parametrização de matrizes comutáveis)*
- **Passo a passo:**
  - Calculando os dois produtos:
    $$AB = \begin{bmatrix} 1 & 2 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} x & y \\ 1 & 2 \end{bmatrix} = \begin{bmatrix} x + 2 & y + 4 \\ x & y \end{bmatrix}$$
    $$BA = \begin{bmatrix} x & y \\ 1 & 2 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} x + y & 2x \\ 3 & 2 \end{bmatrix}$$
  - Igualando $AB = BA$:
    - Posição $(2,1)$: $x = 3$.
    - Posição $(2,2)$: $y = 2$.
    - Conferindo $(1,1)$ e $(1,2)$: $x + 2 = 3 + 2 = 5 = x + y$; e $y + 4 = 2 + 4 = 6 = 2(3) = 2x$. Todas as 4 posições concordam!
- **Resposta Final:** `(3, 2)`
- **Alerta pedagógico:** Sempre confira todas as 4 entradas da igualdade $AB = BA$: se uma única posição falhar, não existe par que faça as matrizes comutarem.

---

### `A05-E05` *(Armadilha do produto notável em matrizes)*
- **Passo a passo:**
  - **(a)** Somando primeiro: $A + B = \begin{bmatrix} 3 & 1 \\ 3 & 0 \end{bmatrix}$. Então:
    $$(A + B)^2 = \begin{bmatrix} 3 & 1 \\ 3 & 0 \end{bmatrix} \begin{bmatrix} 3 & 1 \\ 3 & 0 \end{bmatrix} = \begin{bmatrix} 9+3 & 3+0 \\ 9+0 & 3+0 \end{bmatrix} = \begin{bmatrix} 12 & 3 \\ 9 & 3 \end{bmatrix}.$$
  - **(b)** Calculando termo a termo:
    - $A^2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$, $\;B^2 = \begin{bmatrix} 1 & -3 \\ 9 & -2 \end{bmatrix}$, $\;AB = \begin{bmatrix} 8 & 1 \\ -3 & -1 \end{bmatrix}$.
    - $A^2 + 2AB + B^2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} + \begin{bmatrix} 16 & 2 \\ -6 & -2 \end{bmatrix} + \begin{bmatrix} 1 & -3 \\ 9 & -2 \end{bmatrix} = \begin{bmatrix} 18 & -1 \\ 3 & -3 \end{bmatrix}$.
- **Resposta Final:** `(a) [[12, 3], [9, 3]] (b) [[18, -1], [3, -3]]`
- **Alerta pedagógico:** A diferença entre os itens (a) e (b) ocorre porque $(A + B)^2 = A^2 + AB + BA + B^2$, e aqui $BA = \begin{bmatrix} 2 & 5 \\ 3 & 5 \end{bmatrix} \neq AB$.

---

## 2. Checagem Independente

### `A05-C01` *(Não-comutatividade inédita)*
- **Passo a passo:**
  - **(a)** $AB = \begin{bmatrix} 1(0)+3(2) & 1(-1)+3(5) \\ (-2)(0)+4(2) & (-2)(-1)+4(5) \end{bmatrix} = \begin{bmatrix} 6 & 14 \\ 8 & 22 \end{bmatrix}$.
  - **(b)** $BA = \begin{bmatrix} 0(1)+(-1)(-2) & 0(3)+(-1)(4) \\ 2(1)+5(-2) & 2(3)+5(4) \end{bmatrix} = \begin{bmatrix} 2 & -4 \\ -8 & 26 \end{bmatrix}$.
- **Resposta Final:** `(a) [[6, 14], [8, 22]] (b) [[2, -4], [-8, 26]]`
- **Alerta pedagógico:** Cuidado com o sinal de $(-2)(-1) = +2$ em $(AB)_{22}$ e com $0(1)+(-1)(-2) = +2$ em $(BA)_{11}$.

---

### `A05-C02` *(Parâmetros para comutatividade)*
- **Passo a passo:**
  - Calculando os produtos:
    $$AB = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} x & 2 \\ y & 3 \end{bmatrix} = \begin{bmatrix} 2x + y & 7 \\ x + y & 5 \end{bmatrix}$$
    $$BA = \begin{bmatrix} x & 2 \\ y & 3 \end{bmatrix} \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix} = \begin{bmatrix} 2x + 2 & x + 2 \\ 2y + 3 & y + 3 \end{bmatrix}$$
  - Igualando $AB = BA$:
    - Posição $(1,1)$: $2x + y = 2x + 2 \implies y = 2$.
    - Posição $(1,2)$: $7 = x + 2 \implies x = 5$.
    - Conferindo $(2,1)$ e $(2,2)$: $x + y = 7 = 2(2)+3$ e $5 = 2+3$. Consistente!
- **Resposta Final:** `(5, 2)`
- **Alerta pedagógico:** Não basta igualar apenas a diagonal principal; verifique também as posições fora da diagonal.

---

### `A05-C03` *(Divisores de zero combinados com distributividade)*
- **Passo a passo:**
  - **(a)** $AB = \begin{bmatrix} 2(1)+(-1)(2) & 2(3)+(-1)(6) \\ (-4)(1)+2(2) & (-4)(3)+2(6) \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$.
  - **(b)** Pela distributividade, $A(B + C) = AB + AC = [O] + AC = AC$:
    $$AC = \begin{bmatrix} 2 & -1 \\ -4 & 2 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ -1 & 2 \end{bmatrix} = \begin{bmatrix} 2+1 & 0-2 \\ -4-2 & 0+4 \end{bmatrix} = \begin{bmatrix} 3 & -2 \\ -6 & 4 \end{bmatrix}.$$
    *(Mesmo resultado somando primeiro $B+C = \begin{bmatrix} 2 & 3 \\ 1 & 8 \end{bmatrix}$ e multiplicando por $A$.)*
- **Resposta Final:** `(a) [[0, 0], [0, 0]] (b) [[3, -2], [-6, 4]]`
- **Alerta pedagógico:** Aproveitar $AB = [O]$ na propriedade distributiva $A(B+C) = AB + AC$ poupa cálculos e reduz chance de erro.
