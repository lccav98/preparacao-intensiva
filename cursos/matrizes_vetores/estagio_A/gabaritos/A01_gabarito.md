# Gabarito Comentado — Bloco `A01` (Definição de Matriz, Ordem e Tipos Básicos)

> **Bloco de referência:** [A01_bloco.md](../blocos/A01_bloco.md)

---

## 1. Exercícios

### `A01-E01` *(Leitura de ordem e indexação `a_{ij}`)*
- **Passo a passo:**
  - **(a)** Contando linhas e colunas de $A$: há $m = 3$ linhas horizontais e $n = 4$ colunas verticais. Portanto, $A_{(3,4)}$.
  - **(b)** O elemento $a_{23}$ está na 2ª linha, 3ª coluna: $a_{23} = -2$. O elemento $a_{31}$ está na 3ª linha, 1ª coluna: $a_{31} = -4$. Assim:
    $$a_{23} - 2a_{31} = -2 - 2(-4) = -2 + 8 = 6.$$
- **Resposta Final:** `(a) (3, 4) (b) 6`
- **Alerta pedagógico:** Erro clássico: inverter a ordem para `(4, 3)` ou trocar $a_{31}$ por $a_{13}$. Lembre sempre: **primeiro linha, depois coluna**.

---

### `A01-E02` *(Construção por lei de formação)*
- **Passo a passo:**
  - Linha 1 ($i = 1$):
    - $b_{11}$ ($i = j$): $1^2 + 1 = 2$
    - $b_{12}$ ($i \neq j$): $2(1) - 2 = 0$
    - $b_{13}$ ($i \neq j$): $2(1) - 3 = -1$
  - Linha 2 ($i = 2$):
    - $b_{21}$ ($i \neq j$): $2(2) - 1 = 3$
    - $b_{22}$ ($i = j$): $2^2 + 2 = 6$
    - $b_{23}$ ($i \neq j$): $2(2) - 3 = 1$
  - Montando a matriz $2 \times 3$:
    $$B = \begin{bmatrix} 2 & 0 & -1 \\ 3 & 6 & 1 \end{bmatrix}$$
- **Resposta Final:** `[[2, 0, -1], [3, 6, 1]]`
- **Alerta pedagógico:** Verifique o sinal em $2i - j$ e aplique a regra $i^2 + j$ apenas nos elementos com $i = j$ ($b_{11}$ e $b_{22}$).

---

### `A01-E03` *(Lei de formação condicional com frações e diagonal secundária)*
- **Passo a passo:**
  - **(a)** Calculando elemento a elemento em $C_{(3,3)}$:
    - $i = j$: $c_{11} = c_{22} = c_{33} = 0$.
    - $i < j$ (acima da diagonal principal):
      - $c_{12} = (1 - 2)/2 = -1/2$
      - $c_{13} = (1 - 3)/2 = -1$
      - $c_{23} = (2 - 3)/2 = -1/2$
    - $i > j$ (abaixo da diagonal principal):
      - $c_{21} = 3(2) + 1 = 7$
      - $c_{31} = 3(3) + 1 = 10$
      - $c_{32} = 3(3) + 2 = 11$
    $$C = \begin{bmatrix} 0 & -1/2 & -1 \\ 7 & 0 & -1/2 \\ 10 & 11 & 0 \end{bmatrix}$$
  - **(b)** Na diagonal secundária ($i + j = 4$), temos $c_{13} = -1$, $c_{22} = 0$ e $c_{31} = 10$:
    $$c_{13} + c_{22} + c_{31} = -1 + 0 + 10 = 9.$$
- **Resposta Final:** `(a) [[0, -1/2, -1], [7, 0, -1/2], [10, 11, 0]] (b) 9`
- **Alerta pedagógico:** Não converta `-1/2` para decimal (`-0.5`). Além disso, lembre que $i < j$ significa elementos **acima** da diagonal principal, pois o número da coluna supera o da linha.

---

### `A01-E04` *(Diagonais principal e secundária)*
- **Passo a passo:**
  - **(a)** Diagonal principal ($i = j$): $m_{11} = 3$, $m_{22} = 4$, $m_{33} = -2$.
    $$\text{Soma} = 3 + 4 + (-2) = 5.$$
  - **(b)** Diagonal secundária ($i + j = 4$): $m_{13} = 5$, $m_{22} = 4$, $m_{31} = 7$.
    $$\text{Soma} = 5 + 4 + 7 = 16.$$
- **Resposta Final:** `(a) 5 (b) 16`
- **Alerta pedagógico:** Em ordem $3\times 3$, $m_{22}$ pertence tanto à diagonal principal quanto à diagonal secundária.

---

### `A01-E05` *(Construção de triangular e classificação específica)*
- **Passo a passo:**
  - **(a)** Como $T$ é triangular inferior, todo elemento com $i < j$ vale $0$ ($t_{12} = t_{13} = t_{23} = 0$). Para $i \ge j$, calculamos $t_{ij} = i + 2j$:
    - $t_{11} = 1 + 2(1) = 3$
    - $t_{21} = 2 + 2(1) = 4$, $t_{22} = 2 + 2(2) = 6$
    - $t_{31} = 3 + 2(1) = 5$, $t_{32} = 3 + 2(2) = 7$, $t_{33} = 3 + 2(3) = 9$
    $$T = \begin{bmatrix} 3 & 0 & 0 \\ 4 & 6 & 0 \\ 5 & 7 & 9 \end{bmatrix}$$
  - **(b)** Na matriz $E$, todos os elementos fora da diagonal principal são nulos (matriz diagonal) e os elementos da diagonal principal são todos iguais a $4$ ($k = 4 \neq 1$). Logo, a classificação mais específica é **escalar**.
- **Resposta Final:** `(a) [[3, 0, 0], [4, 6, 0], [5, 7, 9]] (b) escalar`
- **Alerta pedagógico:** Toda matriz escalar é também diagonal e triangular, mas a classificação **escalar** é a mais específica. Só seria `identidade` se a diagonal fosse composta por `1`.

---

## 2. Checagem Independente

### `A01-C01` *(Construção com sinal alternado)*
- **Passo a passo:**
  - Para $P_{(3,2)}$ com $p_{ij} = (-1)^{i+j}(2i - j)$:
    - $p_{11} = (-1)^2(2 - 1) = +1 \cdot 1 = 1$
    - $p_{12} = (-1)^3(2 - 2) = -1 \cdot 0 = 0$
    - $p_{21} = (-1)^3(4 - 1) = -1 \cdot 3 = -3$
    - $p_{22} = (-1)^4(4 - 2) = +1 \cdot 2 = 2$
    - $p_{31} = (-1)^4(6 - 1) = +1 \cdot 5 = 5$
    - $p_{32} = (-1)^5(6 - 2) = -1 \cdot 4 = -4$
    $$P = \begin{bmatrix} 1 & 0 \\ -3 & 2 \\ 5 & -4 \end{bmatrix}$$
- **Resposta Final:** `[[1, 0], [-3, 2], [5, -4]]`
- **Alerta pedagógico:** Cuidado com o expoente $i + j$: se $i+j$ é par, $(-1)^{i+j} = +1$; se $i+j$ é ímpar, $(-1)^{i+j} = -1$.

---

### `A01-C02` *(Indexação e diagonal secundária em ordem 4)*
- **Passo a passo:**
  - **(a)** $q_{24}$ (2ª linha, 4ª coluna) $= -3$; $q_{42}$ (4ª linha, 2ª coluna) $= 2$. Logo:
    $$q_{24} + q_{42} = -3 + 2 = -1.$$
  - **(b)** Na matriz de ordem $n = 4$, a diagonal secundária satisfaz $i + j = 5$: $q_{14} = 5$, $q_{23} = 4$, $q_{32} = 6$, $q_{41} = -4$.
    $$\text{Soma} = 5 + 4 + 6 + (-4) = 11.$$
- **Resposta Final:** `(a) -1 (b) 11`
- **Alerta pedagógico:** Em ordem par ($n = 4$), as diagonais principal e secundária **não** compartilham nenhum elemento em comum.

---

### `A01-C03` *(Classificação precisa de tipos especiais)*
- **Passo a passo:**
  - **(a)** Em $U_{(3,3)}$, todos os elementos abaixo da diagonal principal são nulos ($u_{21} = u_{31} = u_{32} = 0$) e há elementos não nulos acima da diagonal principal ($u_{12}=-3, u_{13}=2, u_{23}=5$). Trata-se de uma matriz **triangular superior** (observe que $u_{22} = 0$ na diagonal principal não impede que seja triangular superior).
  - **(b)** Em $N_{(3,2)}$, todos os elementos são iguais a zero, independentemente de ser retangular; logo, é uma **matriz nula** (`[O]`).
- **Resposta Final:** `(a) triangular superior (b) nula`
- **Alerta pedagógico:** Um zero na diagonal principal ($u_{22} = 0$) não altera a definição de triangular superior, pois a exigência é exclusivamente $a_{ij} = 0$ para $i > j$.
