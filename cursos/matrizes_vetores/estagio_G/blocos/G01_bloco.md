# Bloco `G01` — Simulado Integrador P1 — Matrizes, Determinantes e Inversa

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio G — Integração Geral e Simulados por Avaliação / **`G01`** |
| **Micro-habilidade foco** | Integrar, em formato de simulado P1 sem consulta, lei de formação, igualdade com raízes ($\pm$), propriedade reversa $(AB)^T = B^T A^T$, decomposição simétrica/anti-simétrica, potências especiais, determinantes por triangulação $4\times 4$ e cofatores, equações de singularidade (sem perder $k=0$), inversão por `[A \| I_n]` e equações matriciais. |
| **Pré-requisitos** | `A09`, `B09` *(Revisões cumulativas dos Estágios A e B)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`G01-E01`–`G01-E05`, 25 min):** `16 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`G01-C01`–`G01-C03`, 18 min):** `14 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Simulado P1 sem consulta e sem calculadora.** **Proibido:** Regra de Sarrus, Regra de Chió, Determinante de Vandermonde, matriz adjunta para inversão e Regra de Cramer. Use exclusivamente desenvolvimento por linha/coluna (matriz xadrez de sinais), triangulação via operações $L$ e Gauss-Jordan `[A \| I_n] -> [I_n \| A^{-1}]`, mantendo frações irredutíveis exatas. |

### Registro da Sessão (Preenchido na Prática)
- **Protocolo:** `PREP-MV-G01-<VARIANTE>-T<TENTATIVA>-<HASH>`
- **Sessão única (`G01-E01`–`G01-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`G01-C01`–`G01-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Checklist Integrador P1 (Estágios A + B):**
   - **Igualdade e Lei de Formação (`A01`–`A02`):** construa $A_{(m,n)} = [a_{ij}]$ respeitando linha $i$ e coluna $j$; em $x^2 = c > 0$, registre sempre as **duas raízes** ($\pm$).
   - **Transposição e Especiais (`A06`–`A08`):** $(AB)^T = B^T A^T$ (ordem invertida); decomposição $M = S + K$ com $S = \frac{1}{2}(M + M^T)$ e $K = \frac{1}{2}(M - M^T)$; idempotente ($N^2 = N$), nilpotente ($N^p = [O]$), ortogonal ($Q Q^T = I$).
   - **Determinantes (`B01`–`B05`):** desenvolva pela linha ou coluna com mais zeros usando os sinais xadrez $(-1)^{i+j}$ ou triangularize por $L_j' = L_j + L_i(\alpha)$ (invariante), lembrando de multiplicar por $-1$ a cada troca $L_{ij}$ e compensar fatores escalares $L_i(\alpha)$. Em $\det(A) = 0$, **fatore sem cancelar incógnitas** para não perder $k = 0$.
   - **Propriedades:** $\det(kA) = k^n \det(A)$, $\det(A^T) = \det(A)$, $\det(AB) = \det(A)\det(B)$, $\det(A^{-1}) = 1/\det(A)$ e $\det(A+B) \neq \det(A)+\det(B)$.
   - **Inversa e Equações Matriciais (`B07`–`B08`):** obtenha $A^{-1}$ exclusivamente por $[A \mid I_n] \sim \dots \sim [I_n \mid A^{-1}]$. Isole $X$ respeitando o lado da multiplicação ($AX = B \Rightarrow X = A^{-1}B$; $XA = B \Rightarrow X = BA^{-1}$).

---

## 2. Exemplos Guiados

### Exemplo 1 — Triangulação `4x4` e Propriedade Reversa na Equação Matricial
1. **Triangulação com troca de linhas:** se uma matriz $M_{(4,4)}$ tem pivô nulo na posição $(1,1)$, aplique $L_{12}$ (multiplicando o determinante acumulado por $-1$) antes de zerar a 1ª coluna com $L_j' = L_j + L_1(\alpha)$. Ao final, $\det(M) = (-1)^{\text{trocas}} \cdot \text{produto da diagonal principal}$.
2. **Ordem na equação matricial:** para resolver $X A + B = C$ (com $A$ inversível), primeiro subtraia $B$ ($X A = C - B$) e depois multiplique por $A^{-1}$ **à direita**: $X = (C - B) A^{-1}$. Se houver $X^T$, aplique a transposição somente após isolar $X^T$.

---

## 3. Exercícios (`G01-E01` a `G01-E05`)

### `G01-E01` *(Lei de formação, igualdade paramétrica $\pm$ e transposição do produto)*
Construa $A_{(2,2)} = [a_{ij}]$ definida por $a_{ij} = 2i - j$, e considere as matrizes:
$$B = \begin{bmatrix} x^2 - 3 & 0 \\ 3 & y^2 - 7 \end{bmatrix}, \qquad C = \begin{bmatrix} 1 & -1 \\ 2 & 3 \end{bmatrix}$$
Sabendo que $A = B$, determine:  
**(a)** Todos os valores reais possíveis de $x$  
**(b)** Todos os valores reais possíveis de $y$  
**(c)** A matriz $(AC)^T$

*Formato de resposta:* `(a) x = +-... (b) y = +-... (c) [[...], [...]]`.

---

### `G01-E02` *(Decomposição anti-simétrica e classificação de potência)*
Considere as matrizes $M = \begin{bmatrix} 1 & 4 \\ -2 & 5 \end{bmatrix}$ e $N = \begin{bmatrix} 3 & -6 \\ 1 & -2 \end{bmatrix}$:  
**(a)** Calcule a parcela anti-simétrica $K = \frac{1}{2}(M - M^T)$ da decomposição de $M$.  
**(b)** Calcule $N^2$.  
**(c)** Classifique $N$ quanto à sua potência (`idempotente`, `nilpotente` ou `ortogonal`).

*Formato de resposta:* `(a) [[...], [...]] (b) [[...], [...]] (c) classificacao`.

---

### `G01-E03` *(Determinante `4x4` por triangulação e propriedades)*
**(a)** Calcule $\det(D)$ reduzindo $D$ à forma triangular superior por operações elementares:
$$D = \begin{bmatrix} 1 & 2 & -1 & 0 \\ 2 & 5 & 0 & 1 \\ -1 & 0 & 3 & 2 \\ 0 & 2 & 2 & 5 \end{bmatrix}$$
**(b)** Sejam $P$ e $Q$ matrizes inversíveis de ordem $3$ com $\det(P) = -2$ e $\det(Q) = 3$. Calcule $\det\left(2\,P^T Q^{-1}\right)$ na forma de fração irredutível.

*Formato de resposta:* `(a) valor (b) fracao`.

---

### `G01-E04` *(Equação de singularidade por cofatores — sem perder `k = 0`)*
Desenvolvendo por uma linha ou coluna estratégica (sem Sarrus), determine **todos** os valores reais de $k$ para que a matriz $S$ seja singular ($\det(S) = 0$):
$$S = \begin{bmatrix} k & 0 & 3 \\ 2 & k & -1 \\ 1 & 0 & k - 2 \end{bmatrix}$$

*Formato de resposta:* lista de valores separados por vírgula (ex.: `k1, k2, k3`).

---

### `G01-E05` *(Inversão `[A | I_3]` aplicada a equação matricial com transposta)*
Dadas as matrizes:
$$A = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 2 & 1 \\ 1 & 1 & 2 \end{bmatrix}, \qquad B = \begin{bmatrix} 2 & -1 & 0 \\ 1 & 3 & -2 \\ 0 & 1 & 1 \end{bmatrix}, \qquad C = \begin{bmatrix} 4 & 1 & 2 \\ 3 & 5 & 0 \\ 3 & 4 & 5 \end{bmatrix}$$
**(a)** Calcule $A^{-1}$ exclusivamente pelo método `[A | I_3] -> [I_3 | A^{-1}]`.  
**(b)** Resolva a equação matricial $A X^T + B = C$ e informe a matriz $X$.

*Formato de resposta:* `(a) [[...], [...], [...]] (b) [[...], [...], [...]]`.

---

## 4. Checagem Independente (`G01-C01` a `G01-C03`)
*(Simulado P1 sem consulta e sem calculadora. Critério de aprovação: **100% — 3/3**.)*

### `G01-C01` *(Determinante `4x4` com pivô inicial nulo)*
Calcule $\det(M)$ por triangulação via operações elementares:
$$M = \begin{bmatrix} 0 & 1 & -2 & 1 \\ 1 & -1 & 1 & 2 \\ 2 & 0 & 1 & -1 \\ -1 & 2 & 0 & 3 \end{bmatrix}$$

*Formato de resposta:* número inteiro exato.

---

### `G01-C02` *(Singularidade com raiz nula e fração)*
Determine **todos** os valores reais de $m$ para os quais a matriz $T$ **não admite inversa**:
$$T = \begin{bmatrix} m & 1 & 0 \\ 3 & 2m - 1 & 0 \\ 5 & 2 & m \end{bmatrix}$$

*Formato de resposta:* lista com todos os valores exatos (ex.: `m1, m2, m3`).

---

### `G01-C03` *(Inversão `[A | I_3]` e equação matricial `XA = B`)*
Considere as matrizes $A = \begin{bmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \\ 2 & 3 & 2 \end{bmatrix}$ e $B = \begin{bmatrix} 3 & 5 & 1 \\ -1 & 0 & 2 \end{bmatrix}$.  
**(a)** Calcule $A^{-1}$ pelo método `[A | I_3] -> [I_3 | A^{-1}]`.  
**(b)** Usando $A^{-1}$, determine a matriz $X$ de ordem $2 \times 3$ que satisfaz $X A = B$.

*Formato de resposta:* `(a) [[...], [...], [...]] (b) [[...], [...]]` com frações irredutíveis.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `G02` (`Simulado Integrador P2 — Parte 1`):** somente após autocorreção de `G01-E01`–`G01-E05` e **100% (3/3)** na Checagem Independente `G01-C01`–`G01-C03`.
- **Recuperação direcionada (1ª falha):** identifique qual habilidade falhou (raízes $\pm$ ou transposta → `A02`/`A06`; decomposição/potências → `A07`/`A08`; triangulação $4\times 4$ → `B04`; singularidade $k=0$ → `B05`; inversão `[A | I]` ou lado da multiplicação → `B07`/`B08`) e aplique a variante `V2` de `G01`.
- **Após 2 tentativas malsucedidas:** recuar no DAG para **`A09`** (se a falha ocorreu em matrizes/transposta/potências) ou **`B09`** (se a falha ocorreu em determinantes/inversa/equações matriciais).

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_RE42B_Planejamento.pdf` (Semanas 1–4 — Avaliação P1).
- `[DOC]` `MAT121_Matrizes.pdf` p. 1–36; `Matrizes_Vetores_P1.pdf` p. 1–48; `Mat_Vet_L1.pdf` a `Mat_Vet_L4.pdf`.
- Gabarito comentado e casos de teste: [G01_gabarito.md](../gabaritos/G01_gabarito.md) e [casos_G01.json](../testes/casos_G01.json).
