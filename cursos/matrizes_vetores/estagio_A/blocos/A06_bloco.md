# Bloco `A06` — Matriz Transposta e Propriedade Reversa `(AB)^T = B^T A^T`

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio A — Matrizes: Definição, Operações, Transposta e Especiais / **`A06`** |
| **Micro-habilidade foco** | Construir a matriz transposta $A^T_{(n,m)}$ trocando linhas por colunas, operar expressões lineares com transposição e aplicar a propriedade reversa $(AB)^T = B^T A^T$. |
| **Pré-requisitos** | `A04` |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`A06-E01`–`A06-E05`, 20 min):** `12 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`A06-C01`–`A06-C03`, 14 min):** `10 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** definição de $A^T$, linearidade da transposição, involução $(A^T)^T = A$, propriedade reversa $(AB)^T = B^T A^T$ e isolamento de $X$ em equações com $X^T$. **Proibido:** classificação simétrica/anti-simétrica/ortogonal (`A07`), potências (`A08`), determinantes (`B01`) e inversas (`B06`). |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`A06-E01`–`A06-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`A06-C01`–`A06-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Definição de transposta (`A^T`):** dada $A_{(m,n)} = [a_{ij}]$, sua transposta é a matriz $A^T_{(n,m)} = [a'_{ji}]$ obtida trocando ordenadamente linhas por colunas ($a'_{ij} = a_{ji}$). A 1ª linha de $A$ vira a 1ª coluna de $A^T$, a 2ª linha vira a 2ª coluna, e assim por diante.
2. **Propriedades fundamentais:**
   - **Dupla transposição:** $(A^T)^T = A$.
   - **Linearidade:** $(A + B)^T = A^T + B^T$ e $(\lambda A)^T = \lambda A^T$.
   - **Propriedade reversa do produto (inverte a ordem!):**
     $$(A \cdot B)^T = B^T \cdot A^T$$
     Para três matrizes compatíveis: $(A \cdot B \cdot C)^T = C^T \cdot B^T \cdot A^T$.
3. **Armadilha clássica:** $(AB)^T \neq A^T B^T$! Inclusive, se $A$ é $3 \times 2$ e $B$ é $2 \times 2$, $A^T_{(2,3)} B^T_{(2,2)}$ nem sequer existe, enquanto $B^T_{(2,2)} A^T_{(2,3)}$ existe e tem ordem $(2, 3)$.
4. **Equações com `X^T`:** se $X^T = M$, basta transpor ambos os lados para obter $X = (X^T)^T = M^T$.

---

## 2. Exemplos Guiados

### Exemplo 1 — Transposição e linearidade
Dada $A = \begin{bmatrix} 1 & -3 & 2 \\ 0 & 4 & -5 \end{bmatrix}$ ($2 \times 3$), então:
$$A^T = \begin{bmatrix} 1 & 0 \\ -3 & 4 \\ 2 & -5 \end{bmatrix} \quad (3 \times 2)$$
Se $B_{(3,2)} = \begin{bmatrix} 2 & 1 \\ -1 & 0 \\ 3 & 2 \end{bmatrix}$, podemos somar $A^T + B = \begin{bmatrix} 3 & 1 \\ -4 & 4 \\ 5 & -3 \end{bmatrix}$ pois ambas têm ordem $3 \times 2$.

### Exemplo 2 — Propriedade reversa `(AB)^T = B^T A^T` (`L2` Ex. 1–2)
Para $P = \begin{bmatrix} 1 & 2 \\ 0 & -1 \end{bmatrix}$ e $Q = \begin{bmatrix} 3 & 1 \\ 2 & 4 \end{bmatrix}$:
- Caminho 1: $PQ = \begin{bmatrix} 7 & 9 \\ -2 & -4 \end{bmatrix} \implies (PQ)^T = \begin{bmatrix} 7 & -2 \\ 9 & -4 \end{bmatrix}$.
- Caminho 2 (ordem invertida): $Q^T P^T = \begin{bmatrix} 3 & 2 \\ 1 & 4 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 2 & -1 \end{bmatrix} = \begin{bmatrix} 7 & -2 \\ 9 & -4 \end{bmatrix}$. Resultados idênticos!

---

## 3. Exercícios (`A06-E01` a `A06-E05`)

### `A06-E01` *(Transposta e linearidade `(2A - B)^T`)*
Dadas $A = \begin{bmatrix} 2 & -1 & 4 \\ 0 & 3 & -5 \end{bmatrix}$ e $B = \begin{bmatrix} 1 & 2 & -3 \\ -4 & 1 & 2 \end{bmatrix}$, calcule:  
**(a)** $A^T$  
**(b)** $(2A - B)^T$

**Formato de resposta:** `(a) [[...], [...], [...]] (b) [[...], [...], [...]]`.

---

### `A06-E02` *(Combinação linear envolvendo `A^T`)*
Dadas $A = \begin{bmatrix} 1 & -2 \\ 3 & 0 \\ -1 & 4 \end{bmatrix}$ e $B = \begin{bmatrix} 2 & 1 & -3 \\ 0 & -1 & 2 \end{bmatrix}$, calcule:
$$X = 3A^T - 2B$$

**Formato de resposta:** matriz `[[...], [...]]`.

---

### `A06-E03` *(Produto transposto `(AB)^T`)*
Utilizando a matriz $A_{(3,2)} = \begin{bmatrix} 1 & -2 \\ 3 & 0 \\ -1 & 4 \end{bmatrix}$ e $B_{(2,2)} = \begin{bmatrix} 2 & -1 \\ 3 & 4 \end{bmatrix}$:  
**(a)** Calcule $AB$.  
**(b)** Calcule $(AB)^T$ (e confira que coincide com $B^T A^T$).

**Formato de resposta:** `(a) [[...], [...], [...]] (b) [[...], [...]]`.

---

### `A06-E04` *(Uso direto de `B^T A^T` e equação com `X^T`)*
**(a)** Dadas $A = \begin{bmatrix} 1 & 0 & -2 \\ 3 & -1 & 2 \end{bmatrix}$ e $B = \begin{bmatrix} 2 & -3 \\ 1 & 4 \\ -1 & 0 \end{bmatrix}$, calcule diretamente $B^T \cdot A^T$.  
**(b)** Dadas $M = \begin{bmatrix} 1 & -2 \\ 3 & 4 \end{bmatrix}$ e $N = \begin{bmatrix} 5 & 0 \\ -1 & 2 \end{bmatrix}$, encontre a matriz $X$ que satisfaz $X^T + 2M = N^T$.

**Formato de resposta:** `(a) [[...], [...]] (b) [[...], [...]]`.

---

### `A06-E05` *(Expressão mista com produto e transposição)*
Dadas $A = \begin{bmatrix} 1 & -2 \\ 0 & 3 \end{bmatrix}$, $B = \begin{bmatrix} 2 & 1 \\ -1 & 4 \end{bmatrix}$ e $C = \begin{bmatrix} 3 & -2 \\ 1 & 5 \end{bmatrix}$, calcule:
$$(A^T B - C)^T$$

**Formato de resposta:** matriz `[[...], [...]]`.

---

## 4. Checagem Independente (`A06-C01` a `A06-C03`)

### `A06-C01` *(Linearidade e produto transposto)*
Dadas $A = \begin{bmatrix} 1 & -2 & 0 \\ 3 & 4 & -1 \end{bmatrix}$ e $B = \begin{bmatrix} 2 & 1 \\ -1 & 3 \\ 4 & -2 \end{bmatrix}$, calcule:  
**(a)** $A^T + 2B$  
**(b)** $(AB)^T$

**Formato de resposta:** `(a) [[...], [...], [...]] (b) [[...], [...]]`.

---

### `A06-C02` *(Aplicação direta da regra reversa)*
Dadas $P = \begin{bmatrix} 1 & 2 \\ -1 & 0 \\ 3 & -2 \end{bmatrix}$ e $Q = \begin{bmatrix} 2 & -1 & 4 \\ 0 & 3 & 1 \end{bmatrix}$, calcule $Q^T \cdot P^T$.

**Formato de resposta:** matriz `[[...], [...], [...]]`.

---

### `A06-C03` *(Equação matricial sob transposta)*
Determine a matriz $X$ que satisfaz $(2X - A)^T = 3B$, sendo:
$$A = \begin{bmatrix} 1 & 4 \\ -2 & 3 \end{bmatrix}, \quad B = \begin{bmatrix} 2 & -1 \\ 0 & 5 \end{bmatrix}$$

**Formato de resposta:** matriz `[[...], [...]]` com frações irredutíveis.

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `A07` (`Matrizes Simétricas, Anti-Simétricas e Ortogonais`):** somente após autocorreção de `A06-E01`–`A06-E05` e **100% (3/3)** na Checagem Independente `A06-C01`–`A06-C03` sem consulta.
- **Recuperação direcionada (1ª falha):**
  - Se calculou $A^T B^T$ em vez de $B^T A^T$ → reescreva a identidade $(AB)^T = B^T A^T$ circulando a inversão dos fatores.
  - Se esqueceu a última transposição em `A06-E04(b)` ou `A06-C03` → aplique $(\cdot)^T$ nos dois lados da igualdade logo no primeiro passo (`(2X - A) = 3B^T`).
- **Após 2 tentativas malsucedidas:** recue para **`A04`** para revisar compatibilidade dimensional e produto linha-por-coluna antes de retornar a `A06`.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Matrizes.pdf` p. 17 (definição de transposta e propriedades $(AB)^T = B^T A^T$).
- `[DOC]` `Mat_Vet_L2.pdf` Ex. 1–2 (cálculo e comparação entre $(AB)^T$ e $B^T A^T$).
- Gabarito comentado e casos de teste: [A06_gabarito.md](../gabaritos/A06_gabarito.md) e [casos_A06.json](../testes/casos_A06.json).
