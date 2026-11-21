# Bloco `B03` — Propriedades dos Determinantes e Desigualdade da Soma

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio B — Determinantes, Inversão (`[A\|I]`) e Equações Matriciais / **`B03`** |
| **Micro-habilidade foco** | Aplicar as 8 propriedades dos determinantes, a multiplicatividade `\det(AB) = \det(A)\det(B)`, o fator `\det(kA) = k^n\det(A)` e a desigualdade `\det(A+B) \neq \det(A)+\det(B)`. |
| **Pré-requisitos** | `B02`, `A06` *(Expansão por linha/coluna e matriz transposta)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`B03-E01`–`B03-E05`, 22 min):** `14 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`B03-C01`–`B03-C03`, 14 min):** `10 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | Resolva utilizando as propriedades estruturais sem expandir determinantes desnecessariamente. Não use Sarrus, Chió ou Vandermonde. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`B03-E01`–`B03-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`B03-C01`–`B03-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

As **8 propriedades fundamentais** para matrizes quadradas de ordem $n$ são:

1. **Transposta:** $\det(A^T) = \det(A)$. *(Tudo o que vale para linhas vale também para colunas.)*
2. **Fila nula:** Se uma linha (ou coluna) for toda nula, então $\det(A) = 0$.
3. **Filas iguais:** Se duas linhas (ou colunas) paralelas forem iguais, então $\det(A) = 0$.
4. **Filas proporcionais:** Se uma linha (ou coluna) for múltipla de outra paralela ($L_i = k L_j$), então $\det(A) = 0$.
5. **Troca de filas paralelas:** Trocar duas linhas (ou colunas) entre si **inverte o sinal** do determinante ($L_{ij} \Rightarrow -\det(A)$).
6. **Escalar em uma fila vs. matriz inteira:**
   - Multiplicar **uma única linha** (ou coluna) por $k$ multiplica o determinante por $k$.
   - Multiplicar **toda a matriz** $A_{(n,n)}$ por $k$ multiplica cada uma das $n$ linhas por $k$: **$\det(kA) = k^n \det(A)$**. *(Erro clássico: escrever $k\det(A)$ sem o expoente $n$!)*
7. **Matriz triangular (ou diagonal):** Se todos os elementos acima (ou abaixo) da diagonal principal forem nulos, $\det(A) = a_{11}\cdot a_{22}\cdots a_{nn}$ *(produto da diagonal principal)*.
8. **Combinação linear de filas paralelas (Jacobi):** Somar a uma linha (ou coluna) um múltiplo de outra paralela ($L_j' = L_j + \alpha L_i$) **não altera** o determinante.

**Regras adicionais essenciais:**
- **Produto:** $\det(AB) = \det(A)\cdot\det(B)$ *(para matrizes quadradas de mesma ordem)*.
- **Desigualdade da soma:** O determinante **não é linear** — em geral, **$\det(A + B) \neq \det(A) + \det(B)$**.

---

## 2. Exemplos Guiados

### Exemplo 1 — Escalar em matriz inteira vs. produto e transposta
Se $A$ e $B$ são matrizes $3\times 3$ com $\det(A) = 5$ e $\det(B) = -2$:
- $\det(B \cdot A^T) = \det(B)\cdot\det(A^T) = \det(B)\cdot\det(A) = (-2)\cdot 5 = \mathbf{-10}$.
- $\det(3A) = 3^3 \cdot \det(A) = 27 \cdot 5 = \mathbf{135}$ *(expoente $3$ porque $A$ tem $3$ linhas!)*.

### Exemplo 2 — Transformações em linhas de um determinante conhecido
Sabe-se que $\det\begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix} = 4$. Calcule $\det\begin{bmatrix} d & e & f \\ a & b & c \\ -2g & -2h & -2i \end{bmatrix}$.

1. Partimos da matriz original com $\det = 4$.
2. Trocando $L_1 \leftrightarrow L_2$, o determinante muda de sinal: fica $-4$.
3. Multiplicando $L_3$ por $-2$, multiplicamos o determinante por $-2$: $(-2)\cdot(-4) = \mathbf{8}$.

---

## 3. Exercícios (`B03-E01` a `B03-E05`)

### `B03-E01` *(Produto, transposta e fator `k^n`)*
Sejam $A$ e $B$ matrizes quadradas de **ordem 3** tais que $\det(A) = 4$ e $\det(B) = -3$. Calcule:  
**(a)** $\det(A^T \cdot B)$  
**(b)** $\det(2A)$

---

### `B03-E02` *(Inspeção de propriedades: fila proporcional e operações em filas)*
**(a)** Sem expandir cofatores, determine por propriedade o valor de $\det(M)$ para $M = \begin{bmatrix} 2 & -1 & 4 \\ 5 & 0 & -3 \\ -6 & 3 & -12 \end{bmatrix}$.  
**(b)** Se $N$ é uma matriz $3\times 3$ com $\det(N) = 6$, e $P$ é obtida a partir de $N$ trocando $L_1$ com $L_3$ e multiplicando a nova $L_2$ por $-5$, qual é $\det(P)$?

---

### `B03-E03` *(Determinante de matrizes triangulares)*
Utilizando a propriedade das matrizes triangulares, calcule:  
**(a)** $\det\begin{bmatrix} 2 & -3 & 1 & 5 \\ 0 & -1 & 4 & 2 \\ 0 & 0 & 3 & -7 \\ 0 & 0 & 0 & 5 \end{bmatrix}$  
**(b)** $\det\begin{bmatrix} -4 & 0 & 0 \\ 7 & 1/2 & 0 \\ -2 & 9 & 6 \end{bmatrix}$

---

### `B03-E04` *(Desigualdade da soma: `\det(A+B) \neq \det(A)+\det(B)`)*
Dadas $A = \begin{bmatrix} 2 & -1 \\ 1 & 3 \end{bmatrix}$ e $B = \begin{bmatrix} 1 & 2 \\ -1 & 4 \end{bmatrix}$, calcule separadamente para verificar que os valores diferem:  
**(a)** $\det(A) + \det(B)$  
**(b)** $\det(A + B)$

---

### `B03-E05` *(Combinação linear de linhas e permutações)*
Sabendo que $\det\begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix} = 5$, use exclusivamente as propriedades dos determinantes para calcular:  
**(a)** $\det\begin{bmatrix} a & b & c \\ 2d & 2e & 2f \\ g+3a & h+3b & i+3c \end{bmatrix}$  
**(b)** $\det\begin{bmatrix} g & h & i \\ a & b & c \\ -d & -e & -f \end{bmatrix}$

---

## 4. Checagem Independente (`B03-C01` a `B03-C03`)
*(Sem consulta e sem calculadora. Critério de aprovação: **100% — 3/3**.)*

### `B03-C01` *(Ordem `4`: transposta, potência e escalar)*
Sejam $A$ e $B$ matrizes quadradas de **ordem 4** com $\det(A) = -2$ e $\det(B) = 3$. Calcule:  
**(a)** $\det(A^T \cdot B^2)$  
**(b)** $\det(-2A)$

---

### `B03-C02` *(Verificação da desigualdade da soma)*
Dadas $A = \begin{bmatrix} 1 & 2 \\ 0 & 3 \end{bmatrix}$ e $B = \begin{bmatrix} 2 & -1 \\ 1 & 1 \end{bmatrix}$, calcule:  
**(a)** $\det(A) + \det(B)$  
**(b)** $\det(A + B)$

---

### `B03-C03` *(Operações combinadas em matriz simbólica `3x3`)*
Sabendo que $\det\begin{bmatrix} x & y & z \\ u & v & w \\ r & s & t \end{bmatrix} = -4$, calcule:
$$\det\begin{bmatrix} r & s & t \\ 3x & 3y & 3z \\ u - 2r & v - 2s & w - 2t \end{bmatrix}$$

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `B04` (`Determinantes por Triangulação e Redução a I`):** somente após autocorreção de `B03-E01`–`B03-E05` e **100% (3/3)** na Checagem Independente `B03-C01`–`B03-C03`.
- **Recuperação direcionada (1ª falha):** revisar a diferença entre multiplicar **uma fila** por $k$ ($\times k$) e multiplicar **a matriz inteira** por $k$ ($\times k^n$), além da contagem exata do número de trocas de linhas na sequência de transformações. Aplicar a variante `V2` de `B03`.
- **Após 2 tentativas malsucedidas:** recuar para **`A06`** se o erro envolveu transposta, ou para **`B02`** se houve falha no cálculo dos determinantes de apoio.
