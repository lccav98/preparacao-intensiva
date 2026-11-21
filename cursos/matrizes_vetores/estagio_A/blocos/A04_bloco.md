# Bloco `A04` — Produto de Matrizes e Forma Matricial `AX = B`

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio A — Matrizes: Definição, Operações, Transposta e Especiais / **`A04`** |
| **Micro-habilidade foco** | Verificar compatibilidade dimensional ($A_{(m,n)} \times B_{(n,\ell)} = C_{(m,\ell)}$), executar multiplicação linha-por-coluna e converter sistemas lineares para a forma matricial $AX = B$. |
| **Pré-requisitos** | `A03` |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`A04-E01`–`A04-E05`, 20 min):** `12 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`A04-C01`–`A04-C03`, 14 min):** `10 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** condição de existência do produto, ordem resultante, somatório $c_{ij} = \sum_{k=1}^n a_{ik}b_{kj}$, produto $AX$ com coluna e escrita de sistemas em $AX = B$. **Proibido:** propriedades avançadas e divisores de zero (`A05`), transposição (`A06`), determinantes (`B01`) e resolução por escalonamento (`C01`). |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`A04-E01`–`A04-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`A04-C01`–`A04-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Condição de existência do produto:** o produto $A_{(m,n)} \times B_{(p,\ell)}$ só existe quando o número de **colunas da primeira** é igual ao número de **linhas da segunda** ($n = p$). A matriz resultante $C = A \cdot B$ possui ordem $(m, \ell)$ (as dimensões externas).
2. **Regra linha por coluna:** cada elemento $c_{ij}$ de $C = AB$ é o produto escalar da **linha $i$ de $A$** pela **coluna $j$ de $B$**:
   $$c_{ij} = \sum_{k=1}^{n} a_{ik}\,b_{kj} = a_{i1}b_{1j} + a_{i2}b_{2j} + \dots + a_{in}b_{nj}.$$
3. **Nunca multiplique elemento a elemento!** A multiplicação matricial não multiplica $a_{ij}$ por $b_{ij}$ diretamente.
4. **Forma matricial de sistemas lineares (`AX = B`):** um sistema de $m$ equações e $n$ incógnitas escreve-se como $A_{(m,n)} X_{(n,1)} = B_{(m,1)}$, onde $A$ contém os coeficientes das incógnitas ordenadas, $X$ é o vetor coluna das incógnitas e $B$ é a matriz coluna dos termos independentes.
5. **Conferência dimensional prévia:** sempre escreva as ordens lado a lado — ex.: $(3, 2) \times (2, 4) \to (3, 4)$ — antes de iniciar qualquer conta.

---

## 2. Exemplos Guiados

### Exemplo 1 — Compatibilidade e produto retangular
Dadas $A_{(2,3)} = \begin{bmatrix} 1 & -2 & 0 \\ 3 & 1 & -1 \end{bmatrix}$ e $B_{(3,2)} = \begin{bmatrix} 2 & 1 \\ 0 & -3 \\ 4 & 2 \end{bmatrix}$:
- Ordem: $(2,3) \times (3,2) \to C_{(2,2)}$ (colunas de $A = 3 =$ linhas de $B$).
- Cálculo de $C = A \cdot B$:
  - $c_{11} = 1(2) + (-2)(0) + 0(4) = 2$
  - $c_{12} = 1(1) + (-2)(-3) + 0(2) = 1 + 6 = 7$
  - $c_{21} = 3(2) + 1(0) + (-1)(4) = 6 - 4 = 2$
  - $c_{22} = 3(1) + 1(-3) + (-1)(2) = 3 - 3 - 2 = -2$
$$C = \begin{bmatrix} 2 & 7 \\ 2 & -2 \end{bmatrix}$$

### Exemplo 2 — Sistema linear na forma `AX = B` (`L1` Ex. 6)
O sistema $\begin{cases} x + 2y + 3z = 4 \\ -2x - 5y + 7z = -1 \\ 3x + 9y - 8z = 0 \end{cases}$ equivale a:
$$\begin{bmatrix} 1 & 2 & 3 \\ -2 & -5 & 7 \\ 3 & 9 & -8 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 4 \\ -1 \\ 0 \end{bmatrix}$$
*(Se alguma incógnita estiver ausente em uma equação, seu coeficiente na matriz $A$ é `0`.)*

---

## 3. Exercícios (`A04-E01` a `A04-E05`)

### `A04-E01` *(Compatibilidade dimensional e ordem resultante)*
Considere as matrizes $A_{(3,4)}$, $B_{(4,2)}$ e $C_{(2,3)}$. Informe a ordem `(m, n)` de cada produto abaixo:  
**(a)** $A \cdot B$  
**(b)** $B \cdot C$  
**(c)** $C \cdot A \cdot B$

**Formato de resposta:** `(a) (m, n) (b) (m, n) (c) (m, n)`.

---

### `A04-E02` *(Produto `2x2` por `2x3`)*
Calcule o produto $A \cdot B$, sendo:
$$A = \begin{bmatrix} 2 & -1 \\ 3 & 4 \end{bmatrix}, \quad B = \begin{bmatrix} 1 & 0 & -2 \\ 5 & -3 & 1 \end{bmatrix}$$

**Formato de resposta:** matriz `[[...], [...]]`.

---

### `A04-E03` *(Produto `3x2` por `2x2` com frações)*
Calcule o produto $A \cdot B$, onde:
$$A = \begin{bmatrix} 1/2 & -1 \\ 2 & 1/3 \\ -3 & 2 \end{bmatrix}, \quad B = \begin{bmatrix} 4 & -2 \\ 3 & 6 \end{bmatrix}$$

**Formato de resposta:** matriz `[[...], [...], [...]]`.

---

### `A04-E04` *(Multiplicação `AX` por matriz coluna)*
Calcule a matriz coluna resultante de $A \cdot X$, sendo:
$$A = \begin{bmatrix} 2 & -1 & 1/2 \\ 0 & 3 & -2 \\ 1 & 1/2 & 4 \end{bmatrix}, \quad X = \begin{bmatrix} 2 \\ -4 \\ 6 \end{bmatrix}$$

**Formato de resposta:** matriz coluna `[[...], [...], [...]]`.

---

### `A04-E05` *(Forma matricial `AX = B` e verificação de solução)*
Considere o sistema linear:
$$\begin{cases} 2x - y + 3z = 13 \\ x + 4y - 2z = -13 \\ -3x + 2y + z = -4 \end{cases}$$
**(a)** Escreva a matriz dos coeficientes $A$.  
**(b)** Escreva a matriz coluna dos termos independentes $B$.  
**(c)** Calcule $A \cdot X_0$ para $X_0 = \begin{bmatrix} 1 \\ -2 \\ 3 \end{bmatrix}$ e verifique se coincide com $B$.

**Formato de resposta:** `(a) [[...], [...], [...]] (b) [[...], [...], [...]] (c) [[...], [...], [...]]`.

---

## 4. Checagem Independente (`A04-C01` a `A04-C03`)

### `A04-C01` *(Produto `2x3` por `3x2`)*
Dadas $A = \begin{bmatrix} 1 & -2 & 3 \\ 4 & 0 & -1 \end{bmatrix}$ e $B = \begin{bmatrix} 2 & 1 \\ -3 & 5 \\ 0 & 2 \end{bmatrix}$, calcule $A \cdot B$.

**Formato de resposta:** matriz `[[...], [...]]`.

---

### `A04-C02` *(Ordem inversa `3x2` por `2x3`)*
Utilizando as mesmas matrizes $B_{(3,2)}$ e $A_{(2,3)}$ de `A04-C01`, calcule agora o produto $B \cdot A$.

**Formato de resposta:** matriz `[[...], [...], [...]]`.

---

### `A04-C03` *(Sistema com coeficiente nulo na forma `AX = B`)*
Dado o sistema linear:
$$\begin{cases} x + 2y - z = 3 \\ 3x - y + 2z = 4 \\ 4y + z = -1 \end{cases}$$
**(a)** Escreva a matriz dos coeficientes $A$.  
**(b)** Escreva a matriz coluna $B$.  
**(c)** Calcule $A \cdot X_0$ para $X_0 = \begin{bmatrix} 2 \\ 0 \\ -1 \end{bmatrix}$.

**Formato de resposta:** `(a) [[...], [...], [...]] (b) [[...], [...], [...]] (c) [[...], [...], [...]]`.

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `A05` (`Propriedades do Produto, Não-Comutatividade e Associatividade`) e `A06` (`Matriz Transposta`):** somente após autocorreção de `A04-E01`–`A04-E05` e **100% (3/3)** na Checagem Independente `A04-C01`–`A04-C03` sem consulta.
- **Recuperação direcionada (1ª falha):**
  - Se multiplicou posição a posição → trace setas horizontais nas linhas da 1ª matriz e setas verticais nas colunas da 2ª antes de calcular cada $c_{ij}$.
  - Se errou a ordem em `A04-C01` vs. `A04-C02` → escreva a regra $(m,n)\times(n,\ell)=(m,\ell)$ acima do cálculo.
- **Após 2 tentativas malsucedidas:** recue para **`A03`** para eliminar falhas de soma/sinais nas combinações elementares antes de retomar o produto matricial.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Matrizes.pdf` p. 12–13, 16 (definição de produto e escrita $AX = B$).
- `[DOC]` `Mat_Vet_L1.pdf` Ex. 6–7 (produto $AX$ e produto de matrizes retangulares $BA$).
- Gabarito comentado e casos de teste: [A04_gabarito.md](../gabaritos/A04_gabarito.md) e [casos_A04.json](../testes/casos_A04.json).
