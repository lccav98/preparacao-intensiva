# Bloco `B07` — Inversão pelo Método de Gauss-Jordan (`[A | I] -> [I | A^{-1}]`)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio B — Determinantes, Inversão (`[A\|I]`) e Equações Matriciais / **`B07`** |
| **Micro-habilidade foco** | Inverter matrizes `2x2`, `3x3` e `4x4` (ou detectar singularidade) aplicando operações elementares simultâneas na matriz ampliada `[A | I_n] -> [I_n | A^{-1}]`. |
| **Pré-requisitos** | `B04`, `B06` *(Operações elementares em linhas e definição/existência da inversa)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`B07-E01`–`B07-E05`, 25 min):** `16 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`B07-C01`–`B07-C03`, 18 min):** `14 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Método obrigatório de Gauss-Jordan (`[A | I] -> [I | A^{-1}]`).** É estritamente proibido ensinar ou usar matriz adjunta (`A^{-1} = \operatorname{adj}(A)/\det(A)`). Mantenha frações irredutíveis exatas. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`B07-E01`–`B07-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`B07-C01`–`B07-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Estrutura da matriz ampliada `[A | I_n]`:** Escreva a matriz $A$ à esquerda de uma barra vertical e a matriz identidade $I_n$ à direita.
2. **Algoritmo de Gauss-Jordan (coluna por coluna, da esquerda para a direita):**
   - Na coluna $j$, obtenha o pivô igual a `1` na posição $(j, j)$ *(trocando linhas `L_{jk}` se $a_{jj} = 0$ ou escalando `L_j(1/a_{jj})`)*.
   - Zere **todos** os elementos **abaixo e acima** do pivô usando `L_i' = L_i - \alpha L_j` — aplicando **exatamente a mesma operação em toda a linha** (tanto no bloco esquerdo quanto no direito!).
3. **Critério automático de singularidade:** Se, durante o escalonamento, surgir uma **linha inteira de zeros** no bloco da esquerda, a matriz $A$ é **singular** e **não possui inversa** (encerre imediatamente).
4. **Conferência rápida à prova de erro:** Sempre verifique mentalmente ao menos uma linha por coluna de $A \cdot A^{-1} = I_n$ para garantir que nenhuma fração foi corrompida.

---

## 2. Exemplos Guiados

### Exemplo 1 — Inversão `3x3` pelo método `[A | I_3] -> [I_3 | A^{-1}]`
Calcule $A^{-1}$ para $A = \begin{bmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \\ 2 & 3 & 1 \end{bmatrix}$.

$$\left[\begin{array}{ccc|ccc} 1 & 2 & 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 2 & 3 & 1 & 0 & 0 & 1 \end{array}\right] \xrightarrow{L_3' = L_3 - 2L_1} \left[\begin{array}{ccc|ccc} 1 & 2 & 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & -1 & 1 & -2 & 0 & 1 \end{array}\right]$$
$$\xrightarrow{L_1' = L_1 - 2L_2,\; L_3' = L_3 + L_2} \left[\begin{array}{ccc|ccc} 1 & 0 & -2 & 1 & -2 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & 0 & 2 & -2 & 1 & 1 \end{array}\right] \xrightarrow{L_3\left(\frac{1}{2}\right)} \left[\begin{array}{ccc|ccc} 1 & 0 & -2 & 1 & -2 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & 0 & 1 & -1 & 1/2 & 1/2 \end{array}\right]$$
$$\xrightarrow{L_1' = L_1 + 2L_3,\; L_2' = L_2 - L_3} \left[\begin{array}{ccc|ccc} 1 & 0 & 0 & -1 & -1 & 1 \\ 0 & 1 & 0 & 1 & 1/2 & -1/2 \\ 0 & 0 & 1 & -1 & 1/2 & 1/2 \end{array}\right]$$
Logo, $A^{-1} = \begin{bmatrix} -1 & -1 & 1 \\ 1 & 1/2 & -1/2 \\ -1 & 1/2 & 1/2 \end{bmatrix}$.

---

## 3. Exercícios (`B07-E01` a `B07-E05`)

### `B07-E01` *(Inversão `2x2` via `[A | I_2]` com frações)*
Usando o método de Gauss-Jordan `[A | I_2] -> [I_2 | A^{-1}]`, calcule $A^{-1}$ para:
$$A = \begin{bmatrix} 4 & -2 \\ 1 & 3 \end{bmatrix}$$

---

### `B07-E02` *(Inversão `3x3` inteira via `[A | I_3]`)*
Determine $B^{-1}$ pelo método `[B | I_3] -> [I_3 | B^{-1}]`:
$$B = \begin{bmatrix} 1 & 2 & 1 \\ 0 & 1 & 2 \\ 2 & 5 & 3 \end{bmatrix}$$

---

### `B07-E03` *(Inversão `3x3` com frações irredutíveis)*
Determine $C^{-1}$ pelo método `[C | I_3] -> [I_3 | C^{-1}]` mantendo todas as entradas em frações irredutíveis exatas:
$$C = \begin{bmatrix} 1 & 2 & -1 \\ 2 & 5 & 0 \\ 0 & -1 & 3 \end{bmatrix}$$

---

### `B07-E04` *(Detecção de singularidade durante `[A | I_3]`)*
Aplique o escalonamento em `[D | I_3]` para verificar se a matriz abaixo admite inversa e classifique-a como `"inversivel"` ou `"singular"`:
$$D = \begin{bmatrix} 1 & -2 & 3 \\ 2 & -4 & 6 \\ -1 & 3 & 1 \end{bmatrix}$$

---

### `B07-E05` *(Inversão `4x4` via `[A | I_4]`)*
Calcule a matriz inversa $E^{-1}$ pelo método de Gauss-Jordan `[E | I_4] -> [I_4 | E^{-1}]`:
$$E = \begin{bmatrix} 1 & 0 & 2 & 0 \\ 0 & 2 & 0 & 1 \\ 1 & 0 & 3 & 0 \\ 0 & 1 & 0 & 1 \end{bmatrix}$$

---

## 4. Checagem Independente (`B07-C01` a `B07-C03`)
*(Sem consulta e sem calculadora. Critério de aprovação: **100% — 3/3**.)*

### `B07-C01` *(Inversão `2x2` fracionária via `[A | I_2]`)*
Calcule $M^{-1}$ pelo método de Gauss-Jordan `[M | I_2]`:
$$M = \begin{bmatrix} 3 & 2 \\ -1 & 4 \end{bmatrix}$$

---

### `B07-C02` *(Inversão `3x3` exigindo troca de linhas)*
Calcule $N^{-1}$ pelo método de Gauss-Jordan `[N | I_3]`:
$$N = \begin{bmatrix} 0 & 1 & 2 \\ 1 & 2 & 3 \\ 2 & 1 & 1 \end{bmatrix}$$

---

### `B07-C03` *(Inversão `4x4` via `[P | I_4]`)*
Calcule $P^{-1}$ pelo método de Gauss-Jordan `[P | I_4]`:
$$P = \begin{bmatrix} 1 & 2 & 0 & 0 \\ 1 & 3 & 0 & 0 \\ 0 & 0 & 2 & 1 \\ 0 & 0 & 1 & 1 \end{bmatrix}$$

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `B08` (`Propriedades da Inversa e Equações Matriciais`):** somente após autocorreção de `B07-E01`–`B07-E05` e **100% (3/3)** na Checagem Independente `B07-C01`–`B07-C03`.
- **Recuperação direcionada (1ª falha):** conferir se a operação elementar foi esquecida no bloco direito de `I_n` ou se houve erro de sinal ao zerar elementos **acima** do pivô. Exigir verificação de pelo menos 1 linha de $A\cdot A^{-1} = I$ antes de finalizar e aplicar a variante `V2`.
- **Após 2 tentativas malsucedidas:** recuar para **`B04`** para treinar operações elementares em linhas sem erro aritmético, ou para **`B06`** se o aluno não reconhecer singularidade ou o significado de $A\cdot A^{-1} = I$.
