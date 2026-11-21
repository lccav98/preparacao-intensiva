# Bloco `B01` — Determinante de 2ª e 3ª Ordem (1ª Linha)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio B — Determinantes, Inversão (`[A\|I]`) e Equações Matriciais / **`B01`** |
| **Micro-habilidade foco** | Calcular determinantes de matrizes quadradas de ordem `2` e de ordem `3` exclusivamente pela regra da diagonal principal menos secundária (`2x2`) e pelo desenvolvimento pela 1ª linha com sinais alternados (`3x3`). |
| **Pré-requisitos** | `A01` *(Definição de matriz quadrada, ordem e elementos `a_{ij}`)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`B01-E01`–`B01-E05`, 20 min):** `12 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`B01-C01`–`B01-C03`, 13 min):** `9 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Desenvolvimento exclusivo pela 1ª linha:** proibido utilizar Regra de Sarrus, Regra de Chió ou Determinante de Vandermonde. Mantenha todas as respostas em inteiros ou frações irredutíveis exatas. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`B01-E01`–`B01-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`B01-C01`–`B01-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Notação de determinante:** O determinante de uma matriz quadrada $A = [a_{ij}]$ é um número real associado a $A$, denotado por $\det(A)$ ou por **barras verticais** $|A| = |a_{ij}|$ (nunca confunda colchetes `[...]` de matriz com barras `|...|` de determinante).
2. **Determinante de 2ª ordem (`2x2`):**
   $$\det \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix} = a_{11}a_{22} - a_{12}a_{21}$$
   *(Produto da diagonal principal menos o produto da diagonal secundária. Atenção dupla a sinais negativos na diagonal secundária!)*
3. **Determinante de 3ª ordem (`3x3`) pelo desenvolvimento pela 1ª linha:**
   Para $A = \begin{bmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{bmatrix}$, expandimos pela 1ª linha alternando os sinais **`+  -  +`**:
   $$\det(A) = +\,a_{11}\begin{vmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{vmatrix} - a_{12}\begin{vmatrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{vmatrix} + a_{13}\begin{vmatrix} a_{21} & a_{22} \\ a_{31} & a_{32} \end{vmatrix}$$
4. **Regra do menor complementar:** Para o elemento $a_{1j}$ da 1ª linha, risca-se mentalmente a **1ª linha** e a **$j$-ésima coluna**; o determinante `2x2` restante é o seu menor complementar.
5. **Armadilha clássica:** Quando $a_{12}$ é negativo (ex.: $a_{12} = -3$), o sinal **`-`** da fórmula combina com o sinal do elemento: $-(-3) = +3$.

---

## 2. Exemplos Guiados

### Exemplo 1 — Determinante `2x2` com negativos e fração
Calcule $\det(M)$ para $M = \begin{bmatrix} -2 & 3/2 \\ -4 & 5 \end{bmatrix}$.

- **Diagonal principal:** $(-2)\cdot 5 = -10$.
- **Diagonal secundária:** $(3/2)\cdot(-4) = -6$.
- **Diferença:** $\det(M) = -10 - (-6) = -10 + 6 = \mathbf{-4}$.

### Exemplo 2 — Determinante `3x3` pelo desenvolvimento pela 1ª linha
Calcule $\det(A)$ para $A = \begin{bmatrix} 2 & -3 & 1 \\ 4 & 0 & -2 \\ -1 & 5 & 3 \end{bmatrix}$.

1. Aplicamos os sinais **`+  -  +`** aos elementos da 1ª linha (`2`, `-3`, `1`):
   $$\det(A) = +2\begin{vmatrix} 0 & -2 \\ 5 & 3 \end{vmatrix} - (-3)\begin{vmatrix} 4 & -2 \\ -1 & 3 \end{vmatrix} + 1\begin{vmatrix} 4 & 0 \\ -1 & 5 \end{vmatrix}$$
2. Calculamos cada determinante `2x2`:
   - $\begin{vmatrix} 0 & -2 \\ 5 & 3 \end{vmatrix} = 0\cdot 3 - (-2)\cdot 5 = 0 + 10 = 10$
   - $\begin{vmatrix} 4 & -2 \\ -1 & 3 \end{vmatrix} = 4\cdot 3 - (-2)\cdot(-1) = 12 - 2 = 10$
   - $\begin{vmatrix} 4 & 0 \\ -1 & 5 \end{vmatrix} = 4\cdot 5 - 0\cdot(-1) = 20$
3. Substituindo na expansão:
   $$\det(A) = 2(10) + 3(10) + 1(20) = 20 + 30 + 20 = \mathbf{70}$$

---

## 3. Exercícios (`B01-E01` a `B01-E05`)

### `B01-E01` *(Determinantes de 2ª ordem com negativos e frações)*
Calcule os determinantes de 2ª ordem abaixo:  
**(a)** $\begin{vmatrix} 3 & -2 \\ 5 & 4 \end{vmatrix}$  
**(b)** $\begin{vmatrix} 1/2 & -3 \\ 2 & 6 \end{vmatrix}$

---

### `B01-E02` *(Desenvolvimento pela 1ª linha — Matriz `3x3` completa)*
Calcule $\det(A)$ desenvolvendo exclusivamente pela 1ª linha (sem Regra de Sarrus):
$$A = \begin{bmatrix} 1 & -2 & 3 \\ 4 & 0 & -1 \\ 2 & 5 & 1 \end{bmatrix}$$

---

### `B01-E03` *(Desenvolvimento pela 1ª linha com entrada nula)*
Calcule $\det(B)$ desenvolvendo pela 1ª linha:
$$B = \begin{bmatrix} 3 & 0 & -2 \\ 1 & 4 & 5 \\ -2 & 1 & 2 \end{bmatrix}$$

---

### `B01-E04` *(Desenvolvimento pela 1ª linha com fração)*
Calcule $\det(C)$ mantendo aritmética exata em frações:
$$C = \begin{bmatrix} 1/2 & -1 & 2 \\ 4 & 3 & -2 \\ 2 & 1 & 0 \end{bmatrix}$$

---

### `B01-E05` *(Combinação de determinantes de 3ª ordem)*
Dadas as matrizes $A = \begin{bmatrix} 2 & 1 & -1 \\ 3 & -2 & 4 \\ 1 & 0 & 2 \end{bmatrix}$ e $B = \begin{bmatrix} -1 & 3 & 2 \\ 0 & 1 & -1 \\ 2 & 4 & 1 \end{bmatrix}$, desenvolva cada uma pela 1ª linha e determine:  
**(a)** $\det(A)$  
**(b)** $\det(A) - 2\det(B)$

---

## 4. Checagem Independente (`B01-C01` a `B01-C03`)
*(Resolva no papel, sem consulta ao gabarito e sem calculadora. Critério de aprovação: **100% — 3/3**.)*

### `B01-C01` *(Determinante `2x2` fracionário)*
Calcule o determinante exato:
$$\begin{vmatrix} -3/2 & 4 \\ 1/4 & -2 \end{vmatrix}$$

---

### `B01-C02` *(Determinante `3x3` pela 1ª linha)*
Calcule $\det(P)$ desenvolvendo pela 1ª linha:
$$P = \begin{bmatrix} 2 & -3 & 1 \\ -1 & 4 & 2 \\ 3 & 0 & -2 \end{bmatrix}$$

---

### `B01-C03` *(Armadilha de sinais na 1ª linha)*
Calcule $\det(Q)$ desenvolvendo pela 1ª linha:
$$Q = \begin{bmatrix} -2 & -4 & 3 \\ 1 & 2 & -1 \\ 3 & -1 & 4 \end{bmatrix}$$

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `B02` (`Desenvolvimento por Qualquer Linha ou Coluna`):** somente após autocorreção de `B01-E01`–`B01-E05` e **100% (3/3)** na Checagem Independente `B01-C01`–`B01-C03`.
- **Recuperação direcionada (1ª falha):** identificar se o erro ocorreu na subtração da diagonal secundária (`2x2`), no sinal `-a_{12}` do 2º termo ou ao riscar linha/coluna errada na montagem do menor `2x2`. Refazer o Exemplo 2 marcando os sinais `+ - +` acima da 1ª linha e aplicar a variante `V2`.
- **Após 2 tentativas malsucedidas:** retornar ao pré-requisito **`A01`** para revisar leitura de índices `a_{ij}`, linha vs. coluna e diagonais principal/secundária antes de tentar `B01` novamente.
