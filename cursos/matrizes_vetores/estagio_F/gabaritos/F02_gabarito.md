# Gabarito Comentado — Bloco `F02` (Parábola Transladada, Completamento de Quadrados e 3 Pontos)

> **Bloco de referência:** [F02_bloco.md](../blocos/F02_bloco.md)  
> **Nota para Caça ao Erro:** Em `F02-E03`, o estudante somou $9$ no membro esquerdo para formar $(y - 3)^2$, mas esqueceu de somar $+9$ no membro direito.

---

## 1. Gabarito dos Exercícios (`F02-E01` a `F02-E06`)

### `F02-E01` *(Leitura com vértice $V(h,k)$)*
De $(y - 1)^2 = 12(x + 2) = 12(x - (-2))$:
- **(a)** Vértice: $\mathbf{V(-2, 1)}$.
- **(b)** Como $2p = 12 \implies p = 6 > 0$ e o eixo é paralelo a $Ox$ (abertura à direita): $F\!\left(-2 + \frac{6}{2},\; 1\right) = \mathbf{(1, 1)}$.
- **(c)** Reta diretriz: $x = -2 - \frac{6}{2} \implies \mathbf{x = -5}$.

### `F02-E02` *(Completamento de quadrados)*
Partindo de $x^2 + 4x + 8y - 12 = 0$:
$$x^2 + 4x + 4 = -8y + 12 + 4 \implies (x + 2)^2 = -8y + 16 \implies (x + 2)^2 = -8(y - 2).$$
- **(a)** Vértice: $\mathbf{V(-2, 2)}$.
- **(b)** Aqui $2p = -8 \implies p = -4 < 0$ (eixo paralelo a $Oy$, concavidade para baixo): $F\!\left(-2,\; 2 + (-2)\right) = \mathbf{(-2, 0)}$.
- **(c)** Reta diretriz: $y = 2 - (-2) \implies \mathbf{y = 4}$.

### `F02-E03` *(Caça ao Erro — Compensação do quadrado)*
- **Erro:** ao trocar $y^2 - 6y$ por $(y - 3)^2 = y^2 - 6y + 9$, acrescentou-se $+9$ à esquerda; é obrigatório somar $+9$ também à direita:
  $$y^2 - 6y + 9 = 4x - 13 + 9 \implies (y - 3)^2 = 4x - 4 \implies (y - 3)^2 = 4(x - 1).$$
- **(a)** $\mathbf{(y - 3)^2 = 4(x - 1)}$.
- **(b)** $\mathbf{V(1, 3)}$.
- **(c)** $2p = 4 \implies p = 2 \implies F(1 + 1,\; 3) = \mathbf{(2, 3)}$.

### `F02-E04` *(Foco e diretriz fora da origem)*
Com $F(4, -1)$ e diretriz $y = 5$, o eixo de simetria é vertical ($x = 4$) e a parábola abre para baixo (o foco está abaixo da diretriz):
- Vértice (ponto médio): $V = \left(4,\; \frac{-1 + 5}{2}\right) = (4, 2)$.
- Meio-parâmetro orientado: $\frac{p}{2} = -1 - 2 = -3 \implies p = -6 \implies 2p = -12$.
- Equação reduzida: $\mathbf{(x - 4)^2 = -12(y - 2)}$.

### `F02-E05` *(Parábola vertical por 3 pontos)*
Substituindo em $y = ax^2 + bx + c$:
- $B(0, 1) \implies c = 1$.
- $A(-1, 6) \implies a - b + 1 = 6 \implies a - b = 5$.
- $C(2, 3) \implies 4a + 2b + 1 = 3 \implies 2a + b = 1$.
Somando as duas últimas equações: $3a = 6 \implies a = 2$, donde $b = 2 - 5 = -3$.
Equação: $\mathbf{y = 2x^2 - 3x + 1}$.

### `F02-E06` *(Parábola horizontal por 3 pontos)*
Substituindo em $x = ay^2 + by + c$:
- $P(3, 0) \implies c = 3$.
- $Q(2, 1) \implies a + b + 3 = 2 \implies a + b = -1$.
- $R(11, -2) \implies 4a - 2b + 3 = 11 \implies 2a - b = 4$.
Somando $a + b = -1$ com $2a - b = 4$: $3a = 3 \implies a = 1$ e $b = -2$.
Equação: $\mathbf{x = y^2 - 2y + 3}$ (ou $(y - 1)^2 = x - 2$).

---

## 2. Gabarito da Checagem Independente (`F02-C01` a `F02-C03`)

### `F02-C01`
Completando o quadrado em $y^2 + 4y - 12x + 28 = 0$:
$$y^2 + 4y + 4 = 12x - 28 + 4 \implies (y + 2)^2 = 12x - 24 \implies (y + 2)^2 = 12(x - 2).$$
- **(a)** $\mathbf{V(2, -2)}$.
- **(b)** $2p = 12 \implies p = 6 \implies F(2 + 3, -2) = \mathbf{(5, -2)}$.
- **(c)** Reta diretriz: $x = 2 - 3 \implies \mathbf{x = -1}$.

### `F02-C02`
Com foco $F(-1, 3)$ e diretriz $x = 3$, o eixo é horizontal ($y = 3$), $V = \left(\frac{-1 + 3}{2},\; 3\right) = (1, 3)$ e $\frac{p}{2} = -1 - 1 = -2 \implies 2p = -8$:
$$\mathbf{(y - 3)^2 = -8(x - 1)}.$$

### `F02-C03`
Em $y = ax^2 + bx + c$:
- $(0, 2) \implies c = 2$.
- $(1, 3) \implies a + b = 1$.
- $(-1, 5) \implies a - b = 3$.
Somando: $2a = 4 \implies a = 2$, $b = -1$. Logo: $\mathbf{y = 2x^2 - x + 2}$.
