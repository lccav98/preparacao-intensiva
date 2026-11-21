# Bloco `B04` — Determinantes por Triangulação e Redução a `I`

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio B — Determinantes, Inversão (`[A\|I]`) e Equações Matriciais / **`B04`** |
| **Micro-habilidade foco** | Calcular determinantes `3x3` e `4x4` reduzindo a matriz à forma triangular superior (ou à identidade `I`) com compensação exata de trocas de linhas (`-1`) e fatores multiplicativos (`k`). |
| **Pré-requisitos** | `B03` *(Propriedades dos determinantes e efeito das operações em filas)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`B04-E01`–`B04-E05`, 24 min):** `15 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`B04-C01`–`B04-C03`, 16 min):** `12 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Método obrigatório de triangulação / redução por operações elementares `L_{ij}`, `L_i(\alpha)` e `L_j' = L_j + L_i(\alpha)`.** Proibido usar Regra de Sarrus, Chió ou Vandermonde. Mantenha frações irredutíveis exatas. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`B04-E01`–`B04-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`B04-C01`–`B04-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Por que triangular?** Para matrizes `4x4` densas (sem zeros), expandir por cofatores exige dezenas de contas; reduzir a matriz à forma **triangular superior** $T$ torna $\det(T)$ imediato (produto da diagonal principal).
2. **Efeito das 3 operações elementares sobre $\det$:**
   - **Substituição ($L_j' = L_j + L_i(\alpha)$):** **não altera** o determinante ($\det(A') = \det(A)$).
   - **Permutação ($L_{ij}$ — troca de linhas):** **inverte o sinal** do determinante. Se você fez $t$ trocas, multiplique ao final por $(-1)^t$ *(ou mantenha um fator `(-1)` à esquerda da barra do determinante!)*.
   - **Escala ($L_i(\alpha)$ — multiplicar a linha $i$ por $\alpha \neq 0$):** se $A'$ foi obtida multiplicando $L_i$ por $\alpha$, então $\det(A') = \alpha\,\det(A)$, logo **$\det(A) = \frac{1}{\alpha}\,\det(A')$**. *(Dica prática: ao "fatorar" $k$ para fora do determinante `|...|`, escreva `k * |...|` mantendo a igualdade exata passo a passo!)*
3. **Redução até a identidade `I`:** Se reduzirmos $A$ até $I_n$ mantendo a igualdade com os fatores externos acumulados, como $\det(I_n) = 1$, o próprio produto dos fatores acumulados à frente de $|I_n|$ é o valor exato de $\det(A)$.
4. **Regra de ouro:** **Nunca** some um múltiplo da própria linha que está sendo substituída ($L_2' = 2L_2 - L_1$ multiplica o determinante por $2$!); escreva sempre $L_2' = L_2 + \alpha L_1$ para não alterar o determinante.

---

## 2. Exemplos Guiados

### Exemplo 1 — Triangulação `3x3` com troca de linhas e fator em evidência
Calcule $\det(A) = \begin{vmatrix} 0 & 3 & -6 \\ 2 & 4 & 2 \\ 1 & 5 & -1 \end{vmatrix}$ por triangulação.

1. Como $a_{11} = 0$, trocamos $L_1 \leftrightarrow L_3$ *(custa sinal `-`)*:
   $$\det(A) = -\begin{vmatrix} 1 & 5 & -1 \\ 2 & 4 & 2 \\ 0 & 3 & -6 \end{vmatrix}$$
2. Zeramos abaixo do pivô $1$ com $L_2' = L_2 - 2L_1$ *(não altera o determinante)*:
   $$\det(A) = -\begin{vmatrix} 1 & 5 & -1 \\ 0 & -6 & 4 \\ 0 & 3 & -6 \end{vmatrix}$$
3. Fatoramos $3$ da 3ª linha *(ou usamos direto $L_3' = L_3 + \frac{1}{2}L_2$)*:
   $$\xrightarrow{L_3' = L_3 + \frac{1}{2}L_2} \det(A) = -\begin{vmatrix} 1 & 5 & -1 \\ 0 & -6 & 4 \\ 0 & 0 & -4 \end{vmatrix}$$
4. Produto da diagonal principal com o sinal externo:
   $$\det(A) = -(1 \cdot (-6) \cdot (-4)) = -(24) = \mathbf{-24}$$

---

## 3. Exercícios (`B04-E01` a `B04-E05`)

### `B04-E01` *(Triangulação `3x3` apenas com substituições `L_j' = L_j + \alpha L_i`)*
Calcule $\det(A)$ por triangulação (sem expandir cofatores):
$$A = \begin{bmatrix} 1 & 2 & -1 \\ 2 & 5 & 1 \\ -1 & 0 & 4 \end{bmatrix}$$

---

### `B04-E02` *(Triangulação `3x3` com troca de linhas e fator em linha)*
Calcule $\det(B)$ por triangulação, registrando explicitamente a troca de linhas (pivô inicial nulo):
$$B = \begin{bmatrix} 0 & 2 & -1 \\ 2 & -4 & 6 \\ 1 & 3 & -2 \end{bmatrix}$$

---

### `B04-E03` *(Triangulação `4x4` com fatoração de linha)*
Calcule $\det(C)$ reduzindo à forma triangular superior:
$$C = \begin{bmatrix} 2 & 4 & -2 & 6 \\ 1 & 3 & 0 & 2 \\ -1 & 2 & 3 & 1 \\ 0 & 1 & -2 & 4 \end{bmatrix}$$

---

### `B04-E04` *(Triangulação `4x4` densa sem zeros)*
Calcule $\det(D)$ por triangulação (mantenha frações exatas nos passos intermediários, se necessário):
$$D = \begin{bmatrix} 1 & -1 & 2 & 1 \\ 2 & 1 & -1 & 3 \\ -1 & 2 & 1 & -2 \\ 3 & 0 & 2 & 1 \end{bmatrix}$$

---

### `B04-E05` *(Redução completa até `I_3`)*
Calcule $\det(E)$ reduzindo a matriz completamente até a matriz identidade $I_3$ e multiplicando os fatores retirados:
$$E = \begin{bmatrix} 2 & 1 & 3 \\ 4 & 5 & 7 \\ -2 & 2 & 1 \end{bmatrix}$$

---

## 4. Checagem Independente (`B04-C01` a `B04-C03`)
*(Sem consulta e sem calculadora. Critério de aprovação: **100% — 3/3**.)*

### `B04-C01` *(Triangulação `3x3` com troca de linhas)*
Calcule $\det(M)$ exclusivamente por triangulação:
$$M = \begin{bmatrix} 0 & 3 & -2 \\ 2 & 4 & 1 \\ -1 & 2 & 3 \end{bmatrix}$$

---

### `B04-C02` *(Triangulação `4x4`)*
Calcule $\det(N)$ por triangulação:
$$N = \begin{bmatrix} 1 & 2 & -1 & 3 \\ 0 & 2 & 4 & -2 \\ 2 & 5 & 1 & 4 \\ -1 & 1 & 3 & 0 \end{bmatrix}$$

---

### `B04-C03` *(Triangulação `4x4` com frações exatas)*
Calcule $\det(P)$ por triangulação:
$$P = \begin{bmatrix} 2 & -1 & 3 & 1 \\ 1 & 2 & -1 & 0 \\ 3 & 1 & 2 & 4 \\ -2 & 3 & 1 & -1 \end{bmatrix}$$

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `B05` (`Equações com Determinantes e Condição de Singularidade`):** somente após autocorreção de `B04-E01`–`B04-E05` e **100% (3/3)** na Checagem Independente `B04-C01`–`B04-C03`.
- **Recuperação direcionada (1ª falha):** verificar se houve alteração indevida da linha destino (como fazer $L_2' = 2L_2 - L_1$ sem compensar o fator $2$), esquecimento do sinal `-1` em uma troca $L_{ij}$ ou erro aritmético em frações. Refazer o Exemplo 1 escrevendo cada operação ao lado da seta e aplicar a variante `V2`.
- **Após 2 tentativas malsucedidas:** recuar ao pré-requisito **`B03`** para revisar os efeitos de $L_{ij}$, $L_i(\alpha)$ e $L_j' = L_j + \alpha L_i$ sobre o determinante.
