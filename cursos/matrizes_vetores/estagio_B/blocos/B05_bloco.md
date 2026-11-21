# Bloco `B05` — Equações com Determinantes e Condição de Singularidade

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio B — Determinantes, Inversão (`[A\|I]`) e Equações Matriciais / **`B05`** |
| **Micro-habilidade foco** | Resolver equações algébricas oriundas de `\det(A) = c` e da condição de singularidade `\det(A) = 0` encontrando **todas** as raízes reais (sem perder `r = 0` ao simplificar). |
| **Pré-requisitos** | `B02`, `B03` *(Expansão por linha/coluna e propriedades dos determinantes)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`B05-E01`–`B05-E05`, 22 min):** `14 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`B05-C01`–`B05-C03`, 14 min):** `10 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | Expanda determinantes por linha/coluna ou propriedades (sem Sarrus, Chió ou Vandermonde). Proibido dividir uma equação pela incógnita (fatore em evidência!). |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`B05-E01`–`B05-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`B05-C01`–`B05-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Condição de singularidade:** Uma matriz quadrada $A$ é **singular** (não admite inversa) se e somente se **$\det(A) = 0$**.
2. **Equação com determinante:** Transforme $\det(A(x)) = c$ em uma equação polinomial desenvolvendo pela linha ou coluna mais conveniente (aproveitando zeros e termos que contêm $x$).
3. **Regra crítica anti-perda de raiz (`r = 0`):**
   - **NUNCA** faça: $2r^2 = 6r \implies 2r = 6 \implies r = 3$ *(erro grave: você dividiu por $r$ e apagou a raiz $r = 0$!)*.
   - **FAÇA SEMPRE** por fatoração: $2r^2 - 6r = 0 \implies 2r(r - 3) = 0 \implies \mathbf{r = 0 \text{ ou } r = 3}$.
4. **Raízes quadráticas e cúbicas:** Em equações do tipo $x^2 = 9$, registre ambos os sinais ($x = \pm 3$). Em equações cúbicas fatoradas como $x(x-2)(x+3) = 0$, liste **todas** as raízes reais distintas.

---

## 2. Exemplos Guiados

### Exemplo 1 — Singularidade sem perder a raiz `r = 0`
Determine todos os valores reais de $r$ que tornam singular a matriz $M = \begin{bmatrix} r & 2 & 0 \\ 1 & r & 4 \\ 0 & 0 & r - 5 \end{bmatrix}$? *(Melhor: veja um caso que gera $r$ em evidência!)* Considere $M = \begin{bmatrix} r & 0 & 1 \\ 3 & r & 2 \\ 4 & 0 & 2 \end{bmatrix}$.

1. Expandimos pela **2ª coluna** (dois zeros; sinal de $(2,2)$ é `+`):
   $$\det(M) = +r\begin{vmatrix} r & 1 \\ 4 & 2 \end{vmatrix} = r(2r - 4) = 2r^2 - 4r$$
2. Igualamos a zero:
   $$r(2r - 4) = 0 \implies r = 0 \quad \text{ou} \quad 2r - 4 = 0 \implies \mathbf{r \in \{0,\; 2\}}$$
   *(Se tivéssemos "cortado" $r$ de $2r^2 = 4r$, teríamos perdido $r = 0$!)*

---

## 3. Exercícios (`B05-E01` a `B05-E05`)

### `B05-E01` *(Equação linear de singularidade em matriz `3x3`)*
Determine o valor real exato de $k$ (em fração irredutível) para que a matriz abaixo seja **singular** ($\det(A) = 0$):
$$A = \begin{bmatrix} 1 & 2 & -1 \\ 3 & k & 2 \\ 2 & -1 & 1 \end{bmatrix}$$

---

### `B05-E02` *(Singularidade com fatoração — Atenção a `r = 0`)*
Encontre **todos** os valores reais de $r$ para os quais a matriz $B$ tem determinante nulo:
$$B = \begin{bmatrix} r & 0 & 2 \\ 1 & r & -1 \\ 3 & 0 & 2 \end{bmatrix}$$

---

### `B05-E03` *(Equação quadrática completa vinda de `\det = c`)*
Determine todas as raízes reais da equação $\det(C) = -6$, onde:
$$C = \begin{bmatrix} x & 1 & 2 \\ 3 & x & 0 \\ 1 & -1 & 1 \end{bmatrix}$$

---

### `B05-E04` *(Equação cúbica fatorável — Todas as raízes reais)*
Determine o conjunto de todos os valores reais de $x$ tais que $\det(D) = 0$, onde:
$$D = \begin{bmatrix} x & 3 & 0 \\ 2 & x + 1 & 0 \\ 4 & -1 & x \end{bmatrix}$$

---

### `B05-E05` *(Igualdade de determinantes `2x2` e `3x3`)*
Resolva em $\mathbb{R}$ a equação:
$$\begin{vmatrix} x & 2 \\ 1 & x \end{vmatrix} = \begin{vmatrix} 1 & 0 & 1 \\ 0 & x & 2 \\ 1 & 1 & 2 \end{vmatrix}$$

---

## 4. Checagem Independente (`B05-C01` a `B05-C03`)
*(Sem consulta e sem calculadora. Critério de aprovação: **100% — 3/3**.)*

### `B05-C01` *(Singularidade com fração e raiz `r = 0`)*
Determine todos os valores reais de $r$ para que a matriz $M$ seja singular ($\det(M) = 0$):
$$M = \begin{bmatrix} r & 0 & 1 \\ 2 & r & 3 \\ 5 & 0 & 2 \end{bmatrix}$$

---

### `B05-C02` *(Equação quadrática `\det(P) = 2`)*
Encontre todas as soluções reais da equação $\det(P) = 2$, onde:
$$P = \begin{bmatrix} x & 1 & -1 \\ 0 & x - 2 & 2 \\ 1 & 0 & 3 \end{bmatrix}$$

---

### `B05-C03` *(Equação cúbica com 3 raízes reais distintas)*
Determine todas as raízes reais de $\det(Q) = 0$, onde:
$$Q = \begin{bmatrix} x - 1 & 6 & 0 \\ 1 & x & 0 \\ 3 & 5 & x \end{bmatrix}$$

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `B06` (`Matriz Inversa por Definição e Singularidade`):** somente após autocorreção de `B05-E01`–`B05-E05` e **100% (3/3)** na Checagem Independente `B05-C01`–`B05-C03`.
- **Recuperação direcionada (1ª falha):** se o aluno perdeu `r = 0` ao simplificar a equação ou errou sinais ao expandir o determinante simbólico, revisar o Exemplo 1 enfatizando *"fatorar em evidência antes de resolver"* e aplicar a variante `V2`.
- **Após 2 tentativas malsucedidas:** recuar para **`B02`** se o erro foi na expansão por linha/coluna com parâmetros, ou para **`B03`** se ignorou propriedades de filas proporcionais/nulas.
