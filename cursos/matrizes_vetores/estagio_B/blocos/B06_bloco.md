# Bloco `B06` — Matriz Inversa por Definição (`AB = BA = I`) e Singularidade

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio B — Determinantes, Inversão (`[A\|I]`) e Equações Matriciais / **`B06`** |
| **Micro-habilidade foco** | Verificar e determinar matrizes inversas `2x2` exclusivamente pela definição `AB = BA = I` e decidir sobre invertibilidade (singular vs. não-singular) via `\det(A) \neq 0`. |
| **Pré-requisitos** | `A05`, `B05` *(Produto de matrizes e equações de singularidade)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`B06-E01`–`B06-E05`, 20 min):** `12 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`B06-C01`–`B06-C03`, 14 min):** `10 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Inversão exclusivamente pela definição `AB = I`.** É estritamente proibido ensinar ou usar matriz adjunta (`A^{-1} = \operatorname{adj}(A)/\det(A)`). Mantenha frações irredutíveis exatas. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`B06-E01`–`B06-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`B06-C01`–`B06-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Definição de matriz inversa:** Seja $A$ uma matriz quadrada de ordem $n$. Se existe uma matriz $B$ de mesma ordem tal que:
   $$A\cdot B = B\cdot A = I_n$$
   dizemos que $A$ é **inversível** (ou **não-singular**) e que $B$ é a **inversa** de $A$, denotada por **$A^{-1}$**.
2. **Unicidade e critério de existência:**
   - Quando $A^{-1}$ existe, ela é **única**.
   - $A$ possui inversa **se e somente se $\det(A) \neq 0$**.
   - Se $\det(A) = 0$, $A$ é **singular** e **não admite inversa**.
3. **Cálculo pela definição (`AB = I_2`):** Para encontrar $B = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ tal que $AB = I_2$, efetuamos o produto $AB$ e igualamos elemento a elemento a $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$, resolvendo os dois sistemas lineares `2x2` resultantes (um para a 1ª coluna $(a, c)$ e outro para a 2ª coluna $(b, d)$).

---

## 2. Exemplos Guiados

### Exemplo 1 — Determinando $A^{-1}$ pela definição $AB = I_2$
Determine a inversa de $A = \begin{bmatrix} 3 & 5 \\ 1 & 2 \end{bmatrix}$ usando apenas a definição.

1. Conferimos existência: $\det(A) = 3\cdot 2 - 5\cdot 1 = 1 \neq 0$ *(é inversível)*.
2. Escrevemos $B = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ e impomos $AB = I_2$:
   $$\begin{bmatrix} 3 & 5 \\ 1 & 2 \end{bmatrix} \begin{bmatrix} a & b \\ c & d \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \implies \begin{bmatrix} 3a + 5c & 3b + 5d \\ a + 2c & b + 2d \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$$
3. Resolvemos os dois sistemas:
   - **1ª coluna:** $\begin{cases} 3a + 5c = 1 \\ a + 2c = 0 \implies a = -2c \end{cases}$ $\implies 3(-2c) + 5c = 1 \implies -c = 1 \implies c = -1,\; a = 2$.
   - **2ª coluna:** $\begin{cases} 3b + 5d = 0 \\ b + 2d = 1 \implies b = 1 - 2d \end{cases}$ $\implies 3(1 - 2d) + 5d = 0 \implies 3 - d = 0 \implies d = 3,\; b = -5$.
4. Logo, $A^{-1} = \begin{bmatrix} 2 & -5 \\ -1 & 3 \end{bmatrix}$. *(Conferência: $BA = I_2$.)*

---

## 3. Exercícios (`B06-E01` a `B06-E05`)

### `B06-E01` *(Verificação direta pela definição)*
Dadas $A = \begin{bmatrix} 2 & 1 \\ 5 & 3 \end{bmatrix}$ e $B = \begin{bmatrix} 3 & -1 \\ -5 & 2 \end{bmatrix}$:  
**(a)** Calcule o produto matricial $A \cdot B$.  
**(b)** Responda `"sim"` ou `"nao"`: $B$ é a matriz inversa de $A$?

---

### `B06-E02` *(Inversa `2x2` via `AB = I_2`)*
Utilizando exclusivamente a definição $A \cdot A^{-1} = I_2$, encontre a matriz inversa de:
$$A = \begin{bmatrix} 2 & 5 \\ 1 & 3 \end{bmatrix}$$

---

### `B06-E03` *(Parâmetros desconhecidos em $AB = I_2$)*
Determine os valores reais de $m$ e $n$ para que a matriz $B = \begin{bmatrix} 2 & m \\ -1 & n \end{bmatrix}$ seja a inversa de $A = \begin{bmatrix} 3 & 5 \\ 1 & 2 \end{bmatrix}$:  
**(a)** Valor de $m$  
**(b)** Valor de $n$

---

### `B06-E04` *(Singularidade e invertibilidade com parâmetro)*
Considere a matriz $M = \begin{bmatrix} 1 & 2 & -1 \\ 0 & k & 2 \\ 2 & 1 & 1 \end{bmatrix}$.  
**(a)** Calcule $\det(M)$ para $k = 2$.  
**(b)** Determine o valor real de $k$ para o qual $M$ é **singular** (não admite inversa).

---

### `B06-E05` *(Inversa `2x2` com frações pela definição)*
Utilizando exclusivamente a definição $AB = I_2$, calcule $A^{-1}$ para:
$$A = \begin{bmatrix} 1/2 & 1 \\ 1 & 4 \end{bmatrix}$$

---

## 4. Checagem Independente (`B06-C01` a `B06-C03`)
*(Sem consulta e sem calculadora. Critério de aprovação: **100% — 3/3**.)*

### `B06-C01` *(Determinação de parâmetros via `AB = I_2`)*
Determine os valores reais de $x$ e $y$ para que $B = \begin{bmatrix} x & -2 \\ y & 3 \end{bmatrix}$ seja a matriz inversa de $A = \begin{bmatrix} 3 & 2 \\ 1 & 1 \end{bmatrix}$:  
**(a)** Valor de $x$  
**(b)** Valor de $y$

---

### `B06-C02` *(Inversa `2x2` com entradas fracionárias via `AB = I_2`)*
Usando exclusivamente a definição $A \cdot A^{-1} = I_2$, determine $A^{-1}$ (em frações irredutíveis) para:
$$A = \begin{bmatrix} 2 & -1 \\ 4 & 3 \end{bmatrix}$$

---

### `B06-C03` *(Todos os valores singulares em `3x3`)*
Determine **todos** os valores reais de $k$ para os quais a matriz abaixo **não possui inversa**:
$$A = \begin{bmatrix} k & 1 & 0 \\ 4 & k & 0 \\ 2 & -3 & k - 1 \end{bmatrix}$$

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `B07` (`Inversão pelo Método de Gauss-Jordan`):** somente após autocorreção de `B06-E01`–`B06-E05` e **100% (3/3)** na Checagem Independente `B06-C01`–`B06-C03`.
- **Recuperação direcionada (1ª falha):** verificar se o erro ocorreu na multiplicação linha-por-coluna de $AB$, na montagem dos sistemas para igualar a $I_2$ ou na perda de raiz em $\det(A) = 0$. Refazer o Exemplo 1 verificando ao final que $A\cdot A^{-1} = I_2$ e aplicar a variante `V2`.
- **Após 2 tentativas malsucedidas:** recuar para **`A05`** se houver falhas no produto matricial, ou para **`B05`** se o erro estiver na equação de singularidade $\det(A) = 0$.
