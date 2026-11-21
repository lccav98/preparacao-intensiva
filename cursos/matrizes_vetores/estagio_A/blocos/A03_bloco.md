# Bloco `A03` — Adição, Subtração e Multiplicação por Escalar

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio A — Matrizes: Definição, Operações, Transposta e Especiais / **`A03`** |
| **Micro-habilidade foco** | Executar adição $A + B$, subtração $A - B$ e multiplicação por escalar $\lambda A$, calcular combinações lineares e isolar incógnitas em equações matriciais lineares. |
| **Pré-requisitos** | `A02` |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`A03-E01`–`A03-E05`, 20 min):** `12 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`A03-C01`–`A03-C03`, 14 min):** `10 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** soma/subtração de matrizes de mesma ordem, produto por escalar real ou fracionário, propriedades algébricas, matriz nula `[O]`, identidade `I_n` e sistemas matriciais lineares sem produto entre matrizes. **Proibido:** multiplicação entre duas matrizes (`A04`), transposição (`A06`) e determinantes (`B01`). |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`A03-E01`–`A03-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`A03-C01`–`A03-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Condição para somar ou subtrair:** $A + B$ e $A - B$ só existem quando $A$ e $B$ têm exatamente a **mesma ordem** $(m, n)$. A operação é feita elemento a elemento: $(A \pm B)_{ij} = a_{ij} \pm b_{ij}$.
2. **Multiplicação por escalar $\lambda \in \mathbb{R}$:** multiplica **todos** os elementos da matriz por $\lambda$: $(\lambda A)_{ij} = \lambda a_{ij}$.
3. **Propriedades algébricas:**
   - Comutativa e associativa na soma: $A + B = B + A$ e $(A + B) + C = A + (B + C)$.
   - Elemento neutro da soma: $A + [O] = A$; matriz oposta: $A + (-A) = [O]$.
   - Distributividade com escalares: $\lambda(A + B) = \lambda A + \lambda B$ e $(\alpha + \beta)A = \alpha A + \beta A$.
4. **Isolamento de matriz incógnita $X$:** antes de substituir números, isole $X$ algebricamente (ex.: $3X + 2A = 5B \implies X = \frac{1}{3}(5B - 2A)$). Isso evita erro de sinal acumulado e economiza contas.
5. **Atenção aos sinais e frações:** em $-kB$, distribua o sinal negativo por toda a matriz $B$ e preserve resultados em frações irredutíveis (`7/3`, `-13/3`).

---

## 2. Exemplos Guiados

### Exemplo 1 — Combinação linear de matrizes (`L1` Ex. 5)
Dadas $P = \begin{bmatrix} 1 & -2 \\ 3 & 0 \end{bmatrix}$ e $Q = \begin{bmatrix} -1 & 4 \\ 2 & 5 \end{bmatrix}$, calcule $X = 3P - 2Q$:
$$3P = \begin{bmatrix} 3 & -6 \\ 9 & 0 \end{bmatrix}, \quad -2Q = \begin{bmatrix} 2 & -8 \\ -4 & -10 \end{bmatrix}$$
$$X = 3P + (-2Q) = \begin{bmatrix} 3+2 & -6-8 \\ 9-4 & 0-10 \end{bmatrix} = \begin{bmatrix} 5 & -14 \\ 5 & -10 \end{bmatrix}$$

### Exemplo 2 — Equação matricial linear
Resolva $2X - A = B + I_2$ com $A = \begin{bmatrix} 3 & -1 \\ 2 & 4 \end{bmatrix}$ e $B = \begin{bmatrix} 0 & 5 \\ -2 & 1 \end{bmatrix}$.
- Primeiro isole $X$: $2X = A + B + I_2 \implies X = \frac{1}{2}(A + B + I_2)$.
- Some as matrizes: $A + B + I_2 = \begin{bmatrix} 3+0+1 & -1+5+0 \\ 2-2+0 & 4+1+1 \end{bmatrix} = \begin{bmatrix} 4 & 4 \\ 0 & 6 \end{bmatrix}$.
- Divida por $2$: $X = \begin{bmatrix} 2 & 2 \\ 0 & 3 \end{bmatrix}$.

---

## 3. Exercícios (`A03-E01` a `A03-E05`)

### `A03-E01` *(Adição e subtração direta)*
Dadas as matrizes $A = \begin{bmatrix} 2 & -3 & 5 \\ 1 & 4 & -2 \end{bmatrix}$ e $B = \begin{bmatrix} -1 & 6 & -4 \\ 3 & -2 & 7 \end{bmatrix}$, calcule:  
**(a)** $A + B$  
**(b)** $A - B$

**Formato de resposta:** `(a) [[...], [...]] (b) [[...], [...]]`.

---

### `A03-E02` *(Combinação linear com três matrizes)*
Considerando $A$ e $B$ de `A03-E01` e $C = \begin{bmatrix} 1 & -2 & 0 \\ -4 & 5 & 3 \end{bmatrix}$, calcule:
$$X = 2A - 3B + 4C$$

**Formato de resposta:** matriz `[[...], [...]]`.

---

### `A03-E03` *(Escalares fracionários e matriz identidade)*
Dadas $A = \begin{bmatrix} 4 & -6 \\ 2 & 8 \end{bmatrix}$ e $B = \begin{bmatrix} 3 & -9 \\ 6 & 1 \end{bmatrix}$, calcule a matriz:
$$X = \frac{1}{2}A - \frac{2}{3}B + I_2$$

**Formato de resposta:** matriz `[[...], [...]]` com frações irredutíveis.

---

### `A03-E04` *(Equação matricial linear com `X` isolado)*
Dadas $A = \begin{bmatrix} 1 & -2 \\ 4 & 0 \end{bmatrix}$ e $B = \begin{bmatrix} 2 & 1 \\ -1 & 3 \end{bmatrix}$, determine a matriz $X$ que satisfaz:
$$3X + 2A = 5B - I_2$$

**Formato de resposta:** matriz `[[...], [...]]` com frações irredutíveis.

---

### `A03-E05` *(Sistema linear matricial `2x2`)*
Encontre as matrizes $X$ e $Y$ de ordem $2 \times 2$ tais que:
$$\begin{cases} 2X + Y = A \\ X - Y = B \end{cases}, \quad \text{sendo } A = \begin{bmatrix} 5 & -1 \\ 4 & 7 \end{bmatrix} \text{ e } B = \begin{bmatrix} 1 & 4 \\ -1 & 2 \end{bmatrix}$$

**Formato de resposta:** `(a) [[...], [...]] (b) [[...], [...]]`, sendo `(a)` a matriz $X$ e `(b)` a matriz $Y$.

---

## 4. Checagem Independente (`A03-C01` a `A03-C03`)

### `A03-C01` *(Combinação linear inédita `2x3`)*
Dadas $A = \begin{bmatrix} 1 & -3 & 2 \\ 0 & 4 & -1 \end{bmatrix}$, $B = \begin{bmatrix} -2 & 1 & 5 \\ 3 & -1 & 2 \end{bmatrix}$ e $C = \begin{bmatrix} 4 & 0 & -3 \\ -2 & 5 & 1 \end{bmatrix}$, calcule:
$$M = 3A - 2B + C$$

**Formato de resposta:** matriz `[[...], [...]]`.

---

### `A03-C02` *(Equação matricial com divisão por escalar)*
Determine a matriz $X$ que satisfaz $2X - 3A = B + 4I_2$, sendo:
$$A = \begin{bmatrix} 1 & -2 \\ 3 & 0 \end{bmatrix}, \quad B = \begin{bmatrix} -1 & 4 \\ 2 & 5 \end{bmatrix}$$

**Formato de resposta:** matriz `[[...], [...]]` com frações irredutíveis.

---

### `A03-C03` *(Sistema matricial inédito)*
Determine as matrizes $X$ e $Y$ que satisfazem o sistema:
$$\begin{cases} X + 2Y = A \\ 2X - Y = B \end{cases}, \quad \text{com } A = \begin{bmatrix} 3 & -4 \\ 1 & 5 \end{bmatrix} \text{ e } B = \begin{bmatrix} 1 & 7 \\ 2 & 0 \end{bmatrix}$$

**Formato de resposta:** `(a) [[...], [...]] (b) [[...], [...]]`, onde `(a)` é $X$ e `(b)` é $Y$.

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `A04` (`Produto de Matrizes e Forma Matricial AX = B`):** somente após autocorreção de `A03-E01`–`A03-E05` e **100% (3/3)** na Checagem Independente `A03-C01`–`A03-C03` sem consulta.
- **Recuperação direcionada (1ª falha):**
  - Se errou sinal em $-3B$ ou $-2B$ → passe a calcular primeiro a matriz com o sinal negativo já multiplicado (`(-3)B`) e depois **some** todas as parcelas.
  - Se esqueceu um elemento de $I_2$ → escreva $4I_2 = \begin{bmatrix} 4 & 0 \\ 0 & 4 \end{bmatrix}$ explicitamente antes de somar.
- **Após 2 tentativas malsucedidas:** recue para **`A02`** para revisar equações lineares e igualdade elemento a elemento antes de nova tentativa em `A03`.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Matrizes.pdf` p. 10–11 (adição, subtração, multiplicação por escalar e propriedades).
- `[DOC]` `Mat_Vet_L1.pdf` Ex. 3–5 (combinações lineares do tipo $X = 2A - 6B + 4C$).
- Gabarito comentado e casos de teste: [A03_gabarito.md](../gabaritos/A03_gabarito.md) e [casos_A03.json](../testes/casos_A03.json).
