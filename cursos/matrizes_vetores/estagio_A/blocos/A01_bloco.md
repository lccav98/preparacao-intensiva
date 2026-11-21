# Bloco `A01` — Definição de Matriz, Ordem e Tipos Básicos

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio A — Matrizes: Definição, Operações, Transposta e Especiais / **`A01`** |
| **Micro-habilidade foco** | Identificar a ordem `A_{(m,n)}`, localizar elementos `a_{ij}`, construir matrizes a partir de leis de formação, extrair diagonais principal/secundária e classificar tipos básicos. |
| **Pré-requisitos** | `—` *(Bloco inicial do curso)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`A01-E01`–`A01-E05`, 20 min):** `12 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`A01-C01`–`A01-C03`, 14 min):** `10 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** definição de matriz `A_{(m,n)} = [a_{ij}]`, lei de formação, diagonais principal e secundária, matriz nula `[O]`, linha, coluna, quadrada, diagonal, escalar, identidade `I` e triangulares. **Proibido:** igualdade paramétrica (`A02`), adição/escalar (`A03`), multiplicação (`A04`), transposta (`A06`) e determinantes (`B01`). |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`A01-E01`–`A01-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`A01-C01`–`A01-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Definição e ordem (notação Steinbruch):** uma matriz $A$ de $m$ linhas e $n$ colunas é representada por $A_{(m,n)} = [a_{ij}]$, sempre delimitada por **colchetes** `[ ... ]`. O primeiro índice $i \in \{1, \dots, m\}$ indica a **linha**; o segundo índice $j \in \{1, \dots, n\}$ indica a **coluna**.
2. **Retangular vs. Quadrada:** se $m \neq n$, $A$ é **retangular** (casos particulares: **matriz linha** $1 \times n$ e **matriz coluna** $m \times 1$). Se $m = n$, $A$ é **quadrada de ordem $n$**.
3. **Diagonais de uma matriz quadrada $A_{(n,n)}$:**
   - **Diagonal principal:** elementos em que $i = j$ ($a_{11}, a_{22}, \dots, a_{nn}$).
   - **Diagonal secundária:** elementos em que $i + j = n + 1$ ($a_{1n}, a_{2,n-1}, \dots, a_{n1}$).
4. **Matrizes especiais básicas:**
   - **Nula (`[O]` ou `O`):** todos os elementos são zero ($a_{ij} = 0$).
   - **Diagonal:** quadrada com $a_{ij} = 0$ para todo $i \neq j$.
   - **Escalar:** matriz diagonal cujos elementos da diagonal principal são todos iguais a um mesmo valor $k$ ($a_{ii} = k$).
   - **Identidade (`I` ou `I_n`):** matriz escalar com $a_{ii} = 1$ na diagonal principal e $0$ fora dela.
   - **Triangular superior:** quadrada com todos os elementos **abaixo** da diagonal principal nulos ($a_{ij} = 0$ para $i > j$).
   - **Triangular inferior:** quadrada com todos os elementos **acima** da diagonal principal nulos ($a_{ij} = 0$ para $i < j$).
5. **Aritmética exata:** mantenha eventuais resultados fracionários na forma irredutível (`-1/2`, nunca `-0.5`).

---

## 2. Exemplos Guiados

### Exemplo 1 — Ordem e construção por lei de formação
Construa a matriz $A_{(2,3)} = [a_{ij}]$ definida por $a_{ij} = i - 3j$ se $i \neq j$ e $a_{ij} = i + j$ se $i = j$.

**Passo a passo:**
- Linha 1 ($i = 1$):
  - $a_{11}$ ($i = j$): $1 + 1 = 2$
  - $a_{12}$ ($i \neq j$): $1 - 3(2) = -5$
  - $a_{13}$ ($i \neq j$): $1 - 3(3) = -8$
- Linha 2 ($i = 2$):
  - $a_{21}$ ($i \neq j$): $2 - 3(1) = -1$
  - $a_{22}$ ($i = j$): $2 + 2 = 4$
  - $a_{23}$ ($i \neq j$): $2 - 3(3) = -7$

$$A = \begin{bmatrix} 2 & -5 & -8 \\ -1 & 4 & -7 \end{bmatrix}$$

### Exemplo 2 — Diagonais e classificação específica
Considere $M = \begin{bmatrix} 3 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 3 \end{bmatrix}$ e $U = \begin{bmatrix} 1 & 4 & -2 \\ 0 & 5 & 7 \\ 0 & 0 & -3 \end{bmatrix}$.
- Em $M$, a diagonal principal é $(3, 3, 3)$ (soma $9$), a diagonal secundária é $(0, 3, 0)$ (soma $3$). Embora $M$ seja quadrada e diagonal, seu tipo **mais específico** é **matriz escalar** (pois toda diagonal principal é igual a $3$).
- Em $U$, todos os elementos abaixo da diagonal principal ($u_{21}, u_{31}, u_{32}$) são iguais a $0$; logo, $U$ é **triangular superior**.

---

## 3. Exercícios (`A01-E01` a `A01-E05`)

### `A01-E01` *(Leitura de ordem e indexação `a_{ij}`)*
Considere a matriz:
$$A = \begin{bmatrix} 2 & -1 & 4 & 0 \\ 5 & 3 & -2 & 7 \\ -4 & 1 & 6 & 8 \end{bmatrix}$$
**(a)** Informe a ordem `(m, n)` de $A$.  
**(b)** Calcule o valor exato de $a_{23} - 2a_{31}$.

**Formato de resposta:** `(a) (m, n) (b) numero` (ex.: `(a) (2, 2) (b) 10`).

---

### `A01-E02` *(Construção por lei de formação)*
Construa a matriz $B_{(2,3)} = [b_{ij}]$ definida pela lei:
$$b_{ij} = \begin{cases} i^2 + j, & \text{se } i = j \\ 2i - j, & \text{se } i \neq j \end{cases}$$

**Formato de resposta:** matriz `[[b11, b12, b13], [b21, b22, b23]]`.

---

### `A01-E03` *(Lei de formação condicional com frações e diagonal secundária)*
Seja a matriz $C_{(3,3)} = [c_{ij}]$ definida por:
$$c_{ij} = \begin{cases} \dfrac{i - j}{2}, & \text{se } i < j \\ 0, & \text{se } i = j \\ 3i + j, & \text{se } i > j \end{cases}$$
**(a)** Escreva explicitamente a matriz $C$ mantendo frações irredutíveis.  
**(b)** Calcule a soma dos elementos da **diagonal secundária** de $C$.

**Formato de resposta:** `(a) [[...], [...], [...]] (b) numero`.

---

### `A01-E04` *(Diagonais principal e secundária)*
Dada a matriz quadrada de ordem 3:
$$M = \begin{bmatrix} 3 & -2 & 5 \\ 1 & 4 & -6 \\ 7 & 0 & -2 \end{bmatrix}$$
**(a)** Calcule a soma dos elementos da **diagonal principal** de $M$.  
**(b)** Calcule a soma dos elementos da **diagonal secundária** de $M$.

**Formato de resposta:** `(a) numero (b) numero`.

---

### `A01-E05` *(Construção de triangular e classificação específica)*
**(a)** Construa a matriz triangular inferior $T_{(3,3)} = [t_{ij}]$ em que $t_{ij} = i + 2j$ para $i \ge j$ e $t_{ij} = 0$ para $i < j$.  
**(b)** Classifique a matriz $E = \begin{bmatrix} 4 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 4 \end{bmatrix}$ pelo seu tipo **mais específico** dentre: `identidade`, `escalar`, `diagonal`, `nula`, `triangular superior`.

**Formato de resposta:** `(a) [[...], [...], [...]] (b) classificacao`.

---

## 4. Checagem Independente (`A01-C01` a `A01-C03`)

### `A01-C01` *(Construção com sinal alternado)*
Construa a matriz $P_{(3,2)} = [p_{ij}]$ tal que $p_{ij} = (-1)^{i+j}(2i - j)$.

**Formato de resposta:** matriz `[[p11, p12], [p21, p22], [p31, p32]]`.

---

### `A01-C02` *(Indexação e diagonal secundária em ordem 4)*
Considere a matriz:
$$Q = \begin{bmatrix} 1 & 0 & -2 & 5 \\ 3 & -1 & 4 & -3 \\ 2 & 6 & 0 & 1 \\ -4 & 2 & 7 & 8 \end{bmatrix}$$
**(a)** Calcule $q_{24} + q_{42}$.  
**(b)** Calcule a soma dos elementos da **diagonal secundária** de $Q$.

**Formato de resposta:** `(a) numero (b) numero`.

---

### `A01-C03` *(Classificação precisa de tipos especiais)*
Classifique cada matriz abaixo pelo tipo **mais específico**:  
**(a)** $U = \begin{bmatrix} 1 & -3 & 2 \\ 0 & 0 & 5 \\ 0 & 0 & 4 \end{bmatrix}$  
**(b)** $N = \begin{bmatrix} 0 & 0 \\ 0 & 0 \\ 0 & 0 \end{bmatrix}$

**Formato de resposta:** `(a) classificacao (b) classificacao` (ex.: `triangular superior`, `triangular inferior`, `nula`, `identidade`, `escalar`).

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `A02` (`Igualdade de Matrizes e Equações por Elementos`):** somente após autocorreção de `A01-E01`–`A01-E05` e **100% (3/3)** na Checagem Independente `A01-C01`–`A01-C03` sem consulta.
- **Recuperação direcionada (1ª falha):**
  - Se trocou linha com coluna ($a_{ij}$ por $a_{ji}$) → refaça `A01-E01` marcando $(i, j)$ = `(linha, coluna)` em voz alta.
  - Se confundiu diagonal secundária ou triangular superior/inferior → escreva os pares de índices $(i,j)$ da matriz $3\times 3$ antes de testar a condição ($i<j$ acima da diagonal principal; $i>j$ abaixo; $i+j=n+1$ na secundária).
- **Após 2 tentativas malsucedidas:** interrompa a repetição do bloco e revise a leitura matricial básica (`MAT121_Matrizes.pdf` p. 3–8) com o orientador antes de gerar nova variante.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Matrizes.pdf` p. 3–8 (definição, ordem `A_{(m,n)}`, diagonais e tipos especiais).
- `[DOC]` `Matrizes_Vetores_P1.pdf` p. 1–6 (exemplos manuscritos de construção por lei de formação).
- Gabarito comentado e casos de teste: [A01_gabarito.md](../gabaritos/A01_gabarito.md) e [casos_A01.json](../testes/casos_A01.json).
