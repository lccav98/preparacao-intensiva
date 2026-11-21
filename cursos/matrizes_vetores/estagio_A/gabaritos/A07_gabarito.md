# Gabarito Comentado — Bloco `A07` (Matrizes Simétricas, Anti-Simétricas e Ortogonais)

> **Bloco de referência:** [A07_bloco.md](../blocos/A07_bloco.md)

---

## 1. Exercícios

### `A07-E01` *(Parametrização de simétrica e reconhecimento de anti-simétrica)*
- **Passo a passo:**
  - **(a)** Para $S$ ser simétrica ($S^T = S$), os pares simétricos coincidem:
    - $s_{12} = s_{21} \implies x + 1 = 5 \implies x = 4$.
    - $s_{23} = s_{32} \implies y - 2 = 4 \implies y = 6$.
    - Conferindo $s_{13} = s_{31} = -3$. Logo $(x, y) = (4, 6)$.
  - **(b)** Em $E$, a diagonal principal é $(0, 0, 0)$ e $E^T = \begin{bmatrix} 0 & 3 & -1 \\ -3 & 0 & 5 \\ 1 & -5 & 0 \end{bmatrix} = -E$. Logo $E$ é **anti-simétrica**.
- **Resposta Final:** `(a) (4, 6) (b) anti-simetrica`
- **Alerta pedagógico:** Não basta $s_{12}$ e $s_{21}$ terem o mesmo módulo: na simétrica têm o **mesmo sinal**; na anti-simétrica têm **sinais opostos** e diagonal nula.

---

### `A07-E02` *(Parametrização de anti-simétrica — armadilha da diagonal)*
- **Passo a passo:**
  - Pela condição $K^T = -K$:
    - Diagonal principal nula: $a - 2 = 0 \implies a = 2$, e $d + 1 = 0 \implies d = -1$.
    - Posições $(1,3)$ e $(3,1)$: $b = -5$.
    - Posições $(3,2)$ e $(2,3)$: $c = -3$.
  - Portanto, $(a, b, c, d) = (2, -5, -3, -1)$.
- **Resposta Final:** `(2, -5, -3, -1)`
- **Alerta pedagógico:** O erro mais comum é ignorar a diagonal principal e deixar $a$ ou $d$ sem igualar a zero.

---

### `A07-E03` *(Propriedades de `C + C^T` e `C * C^T`)*
- **Passo a passo:**
  - **(a)** $C^T = \begin{bmatrix} 1 & 5 & -4 \\ -3 & 0 & 2 \\ 2 & -1 & 3 \end{bmatrix}$. Somando:
    $$D = C + C^T = \begin{bmatrix} 2 & 2 & -2 \\ 2 & 0 & 1 \\ -2 & 1 & 6 \end{bmatrix}.$$
  - **(b)** Como $D^T = D$ ($d_{12}=d_{21}=2$, $d_{13}=d_{31}=-2$, $d_{23}=d_{32}=1$), $D$ é **simétrica**.
  - **(c)** Calculando $E = C \cdot C^T$:
    - Linha 1: $[1+9+4,\; 5+0-2,\; -4-6+6] = [14,\; 3,\; -4]$.
    - Linha 2: $[5+0-2,\; 25+0+1,\; -20+0-3] = [3,\; 26,\; -23]$.
    - Linha 3: $[-4-6+6,\; -20+0-3,\; 16+4+9] = [-4,\; -23,\; 29]$.
    $$E = \begin{bmatrix} 14 & 3 & -4 \\ 3 & 26 & -23 \\ -4 & -23 & 29 \end{bmatrix}.$$
    *(Note que $E$ também é simétrica, como previsto pela propriedade $(CC^T)^T = (C^T)^T C^T = CC^T$.)*
- **Resposta Final:** `(a) [[2, 2, -2], [2, 0, 1], [-2, 1, 6]] (b) simetrica (c) [[14, 3, -4], [3, 26, -23], [-4, -23, 29]]`
- **Alerta pedagógico:** Em produtos como $C \cdot C^T$, você pode verificar a simetria instantaneamente ($e_{ij} = e_{ji}$): se der diferente, houve erro aritmético.

---

### `A07-E04` *(Decomposição `M = S + K`)*
- **Passo a passo:**
  - $M^T = \begin{bmatrix} 4 & -1 \\ 3 & 6 \end{bmatrix}$.
  - **(a)** $S = \frac{1}{2}(M + M^T) = \frac{1}{2}\begin{bmatrix} 8 & 2 \\ 2 & 12 \end{bmatrix} = \begin{bmatrix} 4 & 1 \\ 1 & 6 \end{bmatrix}$.
  - **(b)** $K = \frac{1}{2}(M - M^T) = \frac{1}{2}\begin{bmatrix} 0 & 4 \\ -4 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 2 \\ -2 & 0 \end{bmatrix}$.
  - Conferência: $S + K = \begin{bmatrix} 4 & 3 \\ -1 & 6 \end{bmatrix} = M$.
- **Resposta Final:** `(a) [[4, 1], [1, 6]] (b) [[0, 2], [-2, 0]]`
- **Alerta pedagógico:** Lembre de multiplicar por $\frac{1}{2}$ após somar ou subtrair $M^T$; caso contrário, $S + K$ daria $2M$ em vez de $M$.

---

### `A07-E05` *(Verificação de matriz ortogonal)*
- **Passo a passo:**
  - **(a)** $G^T = \begin{bmatrix} 3/5 & 4/5 \\ -4/5 & 3/5 \end{bmatrix}$. Multiplicando $G \cdot G^T$:
    $$G \cdot G^T = \begin{bmatrix} \frac{9}{25}+\frac{16}{25} & \frac{12}{25}-\frac{12}{25} \\ \frac{12}{25}-\frac{12}{25} & \frac{16}{25}+\frac{9}{25} \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I_2.$$
  - **(b)** Como $G \cdot G^T = I_2$, $G$ é **ortogonal** (observe que $G^T \neq G$ e $G^T \neq -G$).
- **Resposta Final:** `(a) [[1, 0], [0, 1]] (b) ortogonal`
- **Alerta pedagógico:** Não confunda ortogonal com simétrica: aqui $g_{12} = -4/5 \neq 4/5 = g_{21}$, mas as linhas são unitárias e ortogonais entre si ($G \cdot G^T = I_2$).

---

## 2. Checagem Independente

### `A07-C01` *(Parametrização anti-simétrica inédita)*
- **Passo a passo:**
  - Diagonal principal nula: $x - 3 = 0 \implies x = 3$, e $z = 0$.
  - Simétricos opostos: $a_{13} = -a_{31} \implies y = -4$.
  - Conferência: $a_{12} = 2 = -(-2)$ e $a_{23} = -7 = -(7)$.
- **Resposta Final:** `(3, -4, 0)`
- **Alerta pedagógico:** Toda anti-simétrica exige diagonal principal inteiramente igual a zero ($a_{11}=a_{22}=a_{33}=0$).

---

### `A07-C02` *(Decomposição `3x3` em parte simétrica e anti-simétrica)*
- **Passo a passo:**
  - $M^T = \begin{bmatrix} 2 & 1 & 5 \\ 5 & 4 & -1 \\ -1 & 3 & 0 \end{bmatrix}$.
  - **(a)** $S = \frac{1}{2}(M + M^T) = \frac{1}{2}\begin{bmatrix} 4 & 6 & 4 \\ 6 & 8 & 2 \\ 4 & 2 & 0 \end{bmatrix} = \begin{bmatrix} 2 & 3 & 2 \\ 3 & 4 & 1 \\ 2 & 1 & 0 \end{bmatrix}$.
  - **(b)** $K = \frac{1}{2}(M - M^T) = \frac{1}{2}\begin{bmatrix} 0 & 4 & -6 \\ -4 & 0 & 4 \\ 6 & -4 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 2 & -3 \\ -2 & 0 & 2 \\ 3 & -2 & 0 \end{bmatrix}$.
- **Resposta Final:** `(a) [[2, 3, 2], [3, 4, 1], [2, 1, 0]] (b) [[0, 2, -3], [-2, 0, 2], [3, -2, 0]]`
- **Alerta pedagógico:** Confira a soma $S + K$ posição a posição antes de encerrar: $2+0=2$, $3+2=5$, $2+(-3)=-1$, etc.

---

### `A07-C03` *(Parâmetro de ortogonalidade com sinal `\pm`)*
- **Passo a passo:**
  - **(a)** Calculando $Q \cdot Q^T$:
    $$Q \cdot Q^T = \begin{bmatrix} a & 12/13 \\ -12/13 & a \end{bmatrix} \begin{bmatrix} a & -12/13 \\ 12/13 & a \end{bmatrix} = \begin{bmatrix} a^2 + \frac{144}{169} & 0 \\ 0 & \frac{144}{169} + a^2 \end{bmatrix}.$$
    Igualando a $I_2$:
    $$a^2 + \frac{144}{169} = 1 \implies a^2 = \frac{25}{169} \implies a = \pm\frac{5}{13}.$$
  - **(b)** Para $a = 5/13$:
    $$Q \cdot Q^T = \begin{bmatrix} \frac{25}{169} + \frac{144}{169} & 0 \\ 0 & \frac{144}{169} + \frac{25}{169} \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}.$$
- **Resposta Final:** `(a) a = +-5/13 (b) [[1, 0], [0, 1]]`
- **Alerta pedagógico:** Não descarte $a = -5/13$: o quadrado negativo também satisfaz $(-5/13)^2 + (12/13)^2 = 1$.
