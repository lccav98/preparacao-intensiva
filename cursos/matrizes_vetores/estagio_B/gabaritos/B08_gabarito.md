# Gabarito Comentado — Bloco `B08` (Propriedades da Inversa e Equações Matriciais)

> **Bloco de referência:** [B08_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_B/blocos/B08_bloco.md)

---

## 1. Gabarito dos Exercícios (`B08-E01` a `B08-E05`)

### `B08-E01`
1. Multiplicamos ambos os lados por $A^{-1}$ **à esquerda**:
   $$A^{-1}(ADX) = A^{-1}(ABC) \implies DX = BC$$
2. Multiplicamos ambos os lados por $D^{-1}$ **à esquerda**:
   $$D^{-1}(DX) = D^{-1}(BC) \implies \mathbf{X = D^{-1}BC}$$

### `B08-E02`
Primeiro calculamos $A^{-1}$ de $A = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix}$ (via `[A | I_2]`): $A^{-1} = \begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix}$.
- **(a)** $X = A^{-1}B = \begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix}\begin{bmatrix} 4 & -2 \\ 0 & 3 \end{bmatrix} = \begin{bmatrix} 4 & -5 \\ -4 & 8 \end{bmatrix}$.
- **(b)** $Y = BA^{-1} = \begin{bmatrix} 4 & -2 \\ 0 & 3 \end{bmatrix}\begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix} = \begin{bmatrix} 6 & -8 \\ -3 & 6 \end{bmatrix}$.

### `B08-E03`
Transpondo ambos os membros de $(AX)^T = B$:
$$AX = B^T \implies X = A^{-1}B^T$$
Como $B^T = \begin{bmatrix} 3 & -2 \\ 1 & 4 \end{bmatrix}$:
$$X = \begin{bmatrix} 1 & -1 \\ 2 & 0 \end{bmatrix}\begin{bmatrix} 3 & -2 \\ 1 & 4 \end{bmatrix} = \begin{bmatrix} 2 & -6 \\ 6 & -4 \end{bmatrix}$$

### `B08-E04`
Isolando $X$ em $D^{-1}XD = A$: multiplicamos por $D$ **à esquerda** e por $D^{-1}$ **à direita**:
$$X = D A D^{-1}$$
Calculando $D^{-1}$ de $D = \begin{bmatrix} 3 & 1 \\ 2 & 1 \end{bmatrix}$: $D^{-1} = \begin{bmatrix} 1 & -1 \\ -2 & 3 \end{bmatrix}$.
1. $DA = \begin{bmatrix} 3 & 1 \\ 2 & 1 \end{bmatrix}\begin{bmatrix} 1 & -2 \\ 0 & 4 \end{bmatrix} = \begin{bmatrix} 3 & -2 \\ 2 & 0 \end{bmatrix}$.
2. $X = (DA)D^{-1} = \begin{bmatrix} 3 & -2 \\ 2 & 0 \end{bmatrix}\begin{bmatrix} 1 & -1 \\ -2 & 3 \end{bmatrix} = \begin{bmatrix} 7 & -9 \\ 2 & -2 \end{bmatrix}$.

### `B08-E05`
Fatorando $X$ à direita: $(A + B)X = C$, com $M = A + B = \begin{bmatrix} 2 & 2 \\ 1 & 3 \end{bmatrix}$.
1. Invertendo $M$ via `[M | I_2]`: $M^{-1} = \begin{bmatrix} 3/4 & -1/2 \\ -1/4 & 1/2 \end{bmatrix}$.
2. Multiplicando à esquerda:
   $$X = M^{-1}C = \begin{bmatrix} 3/4 & -1/2 \\ -1/4 & 1/2 \end{bmatrix}\begin{bmatrix} 4 & 2 \\ 1 & 5 \end{bmatrix} = \begin{bmatrix} 5/2 & -1 \\ -1/2 & 2 \end{bmatrix}$$

---

## 2. Gabarito da Checagem Independente (`B08-C01` a `B08-C03`)

### `B08-C01`
Multiplicamos por $D$ **à esquerda** e por $D^{-1}$ **à direita** em ambos os membros:
$$D(D^{-1}XD)D^{-1} = D(AC)D^{-1} \implies \mathbf{X = DACD^{-1}}$$

### `B08-C02`
Fatorando com $I_2$: $(A - 2I_2)X = B$, onde $M = A - 2I_2 = \begin{bmatrix} 3 & 1 \\ 2 & 2 \end{bmatrix}$.
1. Por `[M | I_2]`: $M^{-1} = \begin{bmatrix} 1/2 & -1/4 \\ -1/2 & 3/4 \end{bmatrix}$.
2. $X = M^{-1}B = \begin{bmatrix} 1/2 & -1/4 \\ -1/2 & 3/4 \end{bmatrix}\begin{bmatrix} 3 & -1 \\ 4 & 2 \end{bmatrix} = \begin{bmatrix} 1/2 & -1 \\ 3/2 & 2 \end{bmatrix}$.

### `B08-C03`
Transpondo ambos os lados: $AX = B^T \implies X = A^{-1}B^T$.
Como $B^T = \begin{bmatrix} 1 & -2 \\ 4 & 0 \end{bmatrix}$:
$$X = \begin{bmatrix} 2 & -1 \\ 1 & 3 \end{bmatrix}\begin{bmatrix} 1 & -2 \\ 4 & 0 \end{bmatrix} = \begin{bmatrix} -2 & -4 \\ 13 & -2 \end{bmatrix}$$
*(Critério de aceitação: 3/3 acertos exatos sem consulta.)*
