# Bloco `B09` — Revisão Cumulativa do Estágio B (Simulado P1)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio B — Determinantes, Inversão (`[A\|I]`) e Equações Matriciais / **`B09`** |
| **Micro-habilidade foco** | Integrar sem consulta triangulação `4x4`, propriedades de determinantes, equações de singularidade (sem perder `r = 0`), inversão por `[A | I_n]` e equações matriciais no padrão P1. |
| **Pré-requisitos** | `B07`, `B08` *(Inversão por Gauss-Jordan e equações matriciais)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`B09-E01`–`B09-E05`, 25 min):** `16 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`B09-C01`–`B09-C03`, 18 min):** `14 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Simulado sem consulta e sem calculadora.** Proibido Sarrus, Chió, Vandermonde, matriz adjunta e Regra de Cramer. Exija frações irredutíveis exatas em todos os resultados. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`B09-E01`–`B09-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`B09-C01`–`B09-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Mapa mental de decisão no Estágio B:**
   - **Determinante `2x2` / `3x3` esparso:** expanda pela linha ou coluna com **mais zeros** usando a matriz xadrez `(-1)^{i+j}`.
   - **Determinante `4x4` denso:** reduza à forma triangular superior com $L_j' = L_j + \alpha L_i$ (invariante), $L_{ij}$ (`-1`) e fatoração explícita de linha.
   - **Propriedades:** $\det(A^T)=\det(A)$, $\det(AB)=\det(A)\det(B)$, $\det(kA)=k^n\det(A)$, $\det(A^{-1})=1/\det(A)$, e $\det(A+B)\neq\det(A)+\det(B)$.
   - **Singularidade:** $\det(A)=0 \iff$ não inversível. Fatore em evidência para **nunca perder $r=0$**.
   - **Inversão:** exclusivamente via `[A | I_n] -> [I_n | A^{-1}]`.
   - **Equação matricial:** isole $X$ multiplicando pelo mesmo lado (esquerdo ou direito) e aplique $(AB)^{-1}=B^{-1}A^{-1}$ e $(X^T)^T=X$.

---

## 2. Exemplos Guiados

### Exemplo 1 — Encadeamento completo: inversa `[A | I_2]` aplicada a equação matricial
Dadas $A = \begin{bmatrix} 1 & 2 \\ 1 & 3 \end{bmatrix}$ e $B = \begin{bmatrix} 2 & -1 \\ 3 & 4 \end{bmatrix}$, resolva $A X + B = 2I_2$.
1. Isolamos $AX = 2I_2 - B = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix} - \begin{bmatrix} 2 & -1 \\ 3 & 4 \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -3 & -2 \end{bmatrix}$.
2. Invertendo $A$ via `[A | I_2]`: $A^{-1} = \begin{bmatrix} 3 & -2 \\ -1 & 1 \end{bmatrix}$.
3. Multiplicando à esquerda: $X = A^{-1}(2I_2 - B) = \begin{bmatrix} 3 & -2 \\ -1 & 1 \end{bmatrix}\begin{bmatrix} 0 & 1 \\ -3 & -2 \end{bmatrix} = \begin{bmatrix} 6 & 7 \\ -3 & -3 \end{bmatrix}$.

---

## 3. Exercícios (`B09-E01` a `B09-E05`)

### `B09-E01` *(Determinante `4x4` por triangulação)*
Calcule $\det(M)$ reduzindo à forma triangular superior por operações elementares:
$$M = \begin{bmatrix} 1 & -2 & 0 & 1 \\ 2 & -3 & 1 & 4 \\ -1 & 4 & 2 & -1 \\ 0 & 2 & -1 & 3 \end{bmatrix}$$

---

### `B09-E02` *(Propriedades combinadas de determinantes)*
Sejam $A$ e $B$ matrizes inversíveis de **ordem 3** com $\det(A) = 3$ e $\det(B) = -2$. Calcule:  
**(a)** $\det\left(2\,A^T B^{-1}\right)$  
**(b)** $\det\left((AB)^T\right)$

---

### `B09-E03` *(Equação de singularidade com 3 raízes incluindo `k = 0`)*
Determine todos os valores reais de $k$ para os quais a matriz $P$ é **singular** ($\det(P) = 0$):
$$P = \begin{bmatrix} k & 0 & 2 \\ 3 & k & 1 \\ 4 & 0 & k - 2 \end{bmatrix}$$

---

### `B09-E04` *(Inversão `3x3` por Gauss-Jordan com frações)*
Usando exclusivamente `[A | I_3] -> [I_3 | A^{-1}]`, determine a inversa da matriz:
$$A = \begin{bmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2 \end{bmatrix}$$

---

### `B09-E05` *(Equação matricial integrando inversa e transposta)*
Dadas $A = \begin{bmatrix} 2 & 3 \\ 1 & 2 \end{bmatrix}$, $B = \begin{bmatrix} 1 & -2 \\ 0 & 4 \end{bmatrix}$ e $C = \begin{bmatrix} 5 & 0 \\ 2 & 6 \end{bmatrix}$, resolva $A X^T + B = C$ e informe a matriz $X$ exata.

---

## 4. Checagem Independente (`B09-C01` a `B09-C03`)
*(Simulado P1 sem consulta e sem calculadora. Critério de aprovação: **100% — 3/3**.)*

### `B09-C01` *(Determinante `4x4` com pivô inicial nulo)*
Calcule $\det(M)$ por triangulação ou desenvolvimento estratégico:
$$M = \begin{bmatrix} 0 & 2 & -1 & 1 \\ 1 & -1 & 3 & 2 \\ 2 & 0 & 1 & -1 \\ -1 & 3 & 2 & 0 \end{bmatrix}$$

---

### `B09-C02` *(Singularidade com fração e raiz nula)*
Determine todos os valores reais de $x$ para os quais a matriz $Q$ **não admite inversa**:
$$Q = \begin{bmatrix} x & 0 & 2 \\ 1 & x & 5 \\ 3 & 0 & 2x + 1 \end{bmatrix}$$

---

### `B09-C03` *(Inversão `[A | I_3]` seguida de resolução `AX = B`)*
Considere $A = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 2 & 1 \\ 1 & 0 & 2 \end{bmatrix}$ e $B = \begin{bmatrix} 3 & 1 \\ 1 & -2 \\ 2 & 4 \end{bmatrix}$.  
**(a)** Calcule $A^{-1}$ pelo método `[A | I_3] -> [I_3 | A^{-1}]`.  
**(b)** Usando $A^{-1}$, determine a matriz $X$ que satisfaz $AX = B$.

---

## 5. Critério de Domínio e Recuperação

- **Conclusão do Estágio B:** somente após autocorreção de `B09-E01`–`B09-E05` e **100% (3/3)** na Checagem Independente `B09-C01`–`B09-C03` (habilitando a entrada no Estágio C — Sistemas Lineares).
- **Recuperação direcionada (1ª falha):** diagnosticar exatamente qual dos 4 pilares falhou (triangulação `4x4`, propriedades `k^n` / `det(B^{-1})`, perda de raiz nula `0`, inversão `[A|I]` ou ordem em equação matricial) e aplicar a variante `V2` de `B09`.
- **Após 2 tentativas malsucedidas:** recuar diretamente para o pré-requisito específico da falha detectada — **`B07`** (se o erro foi em `[A|I]`), **`B08`** (se o erro foi na equação matricial) ou **`B04`/`B05`** (se o erro foi em triangulação ou singularidade).
