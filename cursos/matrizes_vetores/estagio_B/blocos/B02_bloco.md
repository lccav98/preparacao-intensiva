# Bloco `B02` — Desenvolvimento por Qualquer Linha ou Coluna (`3x3` e `4x4`)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio B — Determinantes, Inversão (`[A\|I]`) e Equações Matriciais / **`B02`** |
| **Micro-habilidade foco** | Aplicar a matriz de sinais xadrez `(-1)^{i+j}` para expandir determinantes `3x3` e `4x4` escolhendo estrategicamente a linha ou coluna com maior quantidade de zeros. |
| **Pré-requisitos** | `B01` *(Determinante `2x2` e expansão `3x3` pela 1ª linha)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`B02-E01`–`B02-E05`, 24 min):** `15 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`B02-C01`–`B02-C03`, 16 min):** `12 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Desenvolvimento exclusivo por linha ou coluna (cofatores):** proibido utilizar Regra de Sarrus, Regra de Chió ou Determinante de Vandermonde. Mantenha frações irredutíveis exatas. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`B02-E01`–`B02-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`B02-C01`–`B02-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Teorema de Laplace (expansão por qualquer fila):** O determinante de uma matriz quadrada $A$ de ordem $n$ é igual à soma dos produtos dos elementos de **qualquer linha ou coluna** pelos seus respectivos cofatores:
   $$\det(A) = \sum_{j=1}^n a_{ij}\,(-1)^{i+j}\,M_{ij} \quad (\text{linha } i) \qquad\text{ou}\qquad \det(A) = \sum_{i=1}^n a_{ij}\,(-1)^{i+j}\,M_{ij} \quad (\text{coluna } j)$$
   onde $M_{ij}$ é o determinante obtido ao eliminar a linha $i$ e a coluna $j$.
2. **Matriz de sinais xadrez `(-1)^{i+j}`:** Sempre começa com **`+`** no canto superior esquerdo $(1,1)$ e alterna **`+`** e **`-`** em cada passo horizontal ou vertical:
   $$\text{Ordem } 3:\; \begin{bmatrix} + & - & + \\ - & + & - \\ + & - & + \end{bmatrix} \qquad\qquad \text{Ordem } 4:\; \begin{bmatrix} + & - & + & - \\ - & + & - & + \\ + & - & + & - \\ - & + & - & + \end{bmatrix}$$
3. **Estratégia da fila mais esparsa:** Antes de calcular, conte os zeros de cada linha e de cada coluna. Escolha sempre a **linha ou coluna com mais zeros** — cada elemento zero elimina um determinante inteiro!
4. **Ordem `4x4` → `3x3` → `2x2`:** Ao expandir um determinante `4x4` por uma fila, cada termo não nulo gera um determinante `3x3`, que por sua vez é desenvolvido pela sua fila com mais zeros até chegar a determinantes `2x2`.

---

## 2. Exemplos Guiados

### Exemplo 1 — Escolha estratégica em matriz `3x3`
Calcule $\det(A)$ onde $A = \begin{bmatrix} 5 & -2 & 3 \\ 0 & 4 & 0 \\ -1 & 7 & 2 \end{bmatrix}$.

- A **2ª linha** possui **dois zeros**! Os sinais da 2ª linha na matriz xadrez são **`-  +  -`**.
- Expandindo pela 2ª linha:
  $$\det(A) = -0\cdot M_{21} + 4\cdot\begin{vmatrix} 5 & 3 \\ -1 & 2 \end{vmatrix} - 0\cdot M_{23} = 4\cdot(10 - (-3)) = 4\cdot 13 = \mathbf{52}$$

### Exemplo 2 — Determinante `4x4` expandido pela coluna mais esparsa
Calcule $\det(B)$ para $B = \begin{bmatrix} 1 & 0 & 2 & -1 \\ 3 & 0 & 0 & 4 \\ -2 & 5 & 1 & 0 \\ 4 & 0 & 3 & 2 \end{bmatrix}$.

1. A **2ª coluna** tem três zeros e um único elemento não nulo $b_{32} = 5$.
2. Na matriz de sinais `4x4`, a posição $(3, 2)$ tem sinal $(-1)^{3+2} = -1$ (**`-`**).
3. Riscamos a 3ª linha e a 2ª coluna:
   $$\det(B) = -5 \cdot \begin{vmatrix} 1 & 2 & -1 \\ 3 & 0 & 4 \\ 4 & 3 & 2 \end{vmatrix}$$
4. Agora desenvolvemos o `3x3` restante pela sua **2ª linha** (sinais **`-  +  -`**, aproveitando o zero central):
   $$\begin{vmatrix} 1 & 2 & -1 \\ 3 & 0 & 4 \\ 4 & 3 & 2 \end{vmatrix} = -3\begin{vmatrix} 2 & -1 \\ 3 & 2 \end{vmatrix} + 0 - 4\begin{vmatrix} 1 & 2 \\ 4 & 3 \end{vmatrix} = -3(4 - (-3)) - 4(3 - 8) = -3(7) - 4(-5) = -21 + 20 = -1$$
5. Logo: $\det(B) = -5\cdot(-1) = \mathbf{5}$.

---

## 3. Exercícios (`B02-E01` a `B02-E05`)

### `B02-E01` *(Escolha da coluna mais esparsa em `3x3`)*
Calcule $\det(A)$ escolhendo a linha ou coluna com maior número de zeros:
$$A = \begin{bmatrix} 2 & 0 & -1 \\ 3 & 4 & 2 \\ -1 & 0 & 5 \end{bmatrix}$$

---

### `B02-E02` *(Desenvolvimento pela 3ª linha em `3x3`)*
Calcule $\det(B)$ desenvolvendo diretamente pela **3ª linha** (com os sinais **`+  -  +`**):
$$B = \begin{bmatrix} 1 & -2 & 3 \\ 2 & 1 & -1 \\ 0 & 4 & -2 \end{bmatrix}$$

---

### `B02-E03` *(Determinante `4x4` com 3 zeros em uma linha)*
Calcule $\det(C)$ escolhendo a linha com mais zeros (atenção ao sinal da posição na matriz `4x4`):
$$C = \begin{bmatrix} 2 & 0 & -1 & 3 \\ 0 & 0 & 2 & 0 \\ 1 & 3 & 4 & -2 \\ -1 & 2 & 0 & 1 \end{bmatrix}$$

---

### `B02-E04` *(Determinante `4x4` reduzido a dois determinantes `3x3`)*
Calcule $\det(D)$ expandindo pela fila mais conveniente:
$$D = \begin{bmatrix} 1 & 2 & 0 & -1 \\ 3 & 0 & 2 & 0 \\ -2 & 1 & 1 & 3 \\ 0 & 4 & -1 & 2 \end{bmatrix}$$

---

### `B02-E05` *(Determinante `4x4` com fração e zeros na 3ª coluna)*
Calcule $\det(E)$ expandindo pela 3ª coluna:
$$E = \begin{bmatrix} 2 & -1 & 0 & 3 \\ 1 & 3 & 1/2 & -1 \\ 4 & 0 & 0 & 2 \\ -1 & 2 & -2 & 1 \end{bmatrix}$$

---

## 4. Checagem Independente (`B02-C01` a `B02-C03`)
*(Sem consulta e sem calculadora. Critério de aprovação: **100% — 3/3**.)*

### `B02-C01` *(Sinais da 2ª linha em `3x3`)*
Calcule $\det(M)$ escolhendo a linha mais esparsa:
$$M = \begin{bmatrix} 3 & -1 & 2 \\ 0 & -2 & 0 \\ 4 & 5 & -1 \end{bmatrix}$$

---

### `B02-C02` *(Determinante `4x4` pela 4ª coluna)*
Calcule $\det(N)$ desenvolvendo pela 4ª coluna:
$$N = \begin{bmatrix} 1 & -2 & 3 & 0 \\ 2 & 1 & -1 & 0 \\ -1 & 4 & 2 & -3 \\ 3 & 0 & 1 & 0 \end{bmatrix}$$

---

### `B02-C03` *(Determinante `4x4` com 2 zeros na 2ª linha)*
Calcule $\det(P)$ desenvolvendo pela 2ª linha:
$$P = \begin{bmatrix} 2 & 1 & -1 & 3 \\ 0 & -2 & 0 & 4 \\ 1 & 3 & 2 & -1 \\ -1 & 0 & 3 & 2 \end{bmatrix}$$

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `B03` (`Propriedades dos Determinantes e Desigualdade da Soma`):** somente após autocorreção de `B02-E01`–`B02-E05` e **100% (3/3)** na Checagem Independente `B02-C01`–`B02-C03`.
- **Recuperação direcionada (1ª falha):** verificar se o erro ocorreu na matriz de sinais `(-1)^{i+j}` (especialmente posições `(2,1)`, `(2,3)`, `(3,2)`, `(3,4)` e `(2,4)`!) ou na eliminação correta da linha/coluna do cofator `4x4`. Refazer o Exemplo 2 desenhando a grade `4x4` de sinais `+`/`-` ao lado da matriz e aplicar a variante `V2`.
- **Após 2 tentativas malsucedidas:** recuar ao pré-requisito **`B01`** para consolidar cálculo exato de determinantes `2x2` e expansão `3x3` sem erros de sinal antes de retomar `B02`.
