# Bloco `C04` — Método da Matriz Inversa (`X = A^{-1}B`)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio C — Sistemas Lineares, Escalonamento, Posto (`C_A, C_V`) e Parâmetros / **`C04`** |
| **Micro-habilidade foco** | Resolver sistemas quadrados $AX = B$ determinando $A^{-1}$ por Gauss-Jordan na matriz ampliada `[A | I] -> [I | A^{-1}]`, calcular $X = A^{-1}B$ à esquerda e reaproveitar $A^{-1}$ para múltiplos vetores $B$. |
| **Pré-requisitos** | `B07` *(Inversão por Gauss-Jordan `[A | I]`)* e `C01` *(Forma matricial $AX = B$)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Prática (`C04-E01`–`C04-E05`, 22 min):** `14 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`C04-C01`–`C04-C03`, 16 min):** `11 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Proibido:** matriz adjunta (`adj(A)`), Regra de Cramer ou Regra de Sarrus. Calcule $A^{-1}$ exclusivamente por `[A | I] -> [I | A^{-1}]` com operações $L_{ij}$, $L_i(\alpha)$ e $L_j' = L_j + L_i(\alpha)$, mantendo frações irredutíveis exatas. |

### Registro da Sessão (Preenchido na Prática)
- **Protocolo:** `PREP-MV-C04-<VARIANTE>-T<TENTATIVA>-<HASH>`
- **Prática (`C04-E01`–`C04-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`C04-C01`–`C04-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Dedução da fórmula:** partindo do sistema quadrado $n \times n$ escrito como $A_{\text{coef}} X = B$ (ou simplesmente $AX = B$), se $A$ é inversível ($\det(A) \neq 0$), multiplicamos **pela esquerda** ambos os lados por $A^{-1}$:
   $$A^{-1} A X = A^{-1} B \Rightarrow I X = A^{-1} B \Rightarrow X = A^{-1} B.$$
   *(Cuidado: o produto de matrizes não é comutativo; $B A^{-1}$ sequer tem dimensões compatíveis para $B_{(n,1)}$ quando $n > 1$!)*
2. **Quando o método falha:** se durante a redução `[A | I]` surgir uma linha de zeros no bloco esquerdo, então $A$ é **singular** (não possui inversa) e o método não se aplica — sendo necessário escalonar `[A | B]` para distinguir entre `SPI` e `SI`.
3. **Grande vantagem prática:** quando se deseja resolver vários sistemas com **a mesma matriz de coeficientes $A$** e diferentes vetores de termos independentes $B^{(1)}, B^{(2)}, \dots$, calcula-se $A^{-1}$ **uma única vez** e obtém-se cada solução com uma simples multiplicação $X^{(k)} = A^{-1} B^{(k)}$.

---

## 2. Exemplos Guiados

### Exemplo 1 — Inversão `[A | I] -> [I | A^{-1}]` e solução `X = A^{-1}B`
Considere $A = \begin{bmatrix} 1 & 2 \\ 2 & 5 \end{bmatrix}$ e dois sistemas $AX = B^{(1)}$ com $B^{(1)} = \begin{bmatrix} 4 \\ 9 \end{bmatrix}$ e $AX = B^{(2)}$ com $B^{(2)} = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$:
1. **Obtendo $A^{-1}$ por Gauss-Jordan:**
   $$\left[\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 2 & 5 & 0 & 1 \end{array}\right] \xrightarrow{L_2' = L_2 + L_1(-2)} \left[\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 0 & 1 & -2 & 1 \end{array}\right] \xrightarrow{L_1' = L_1 + L_2(-2)} \left[\begin{array}{cc|cc} 1 & 0 & 5 & -2 \\ 0 & 1 & -2 & 1 \end{array}\right]$$
   Logo, $A^{-1} = \begin{bmatrix} 5 & -2 \\ -2 & 1 \end{bmatrix}$.
2. **Soluções por reutilização:**
   $$X^{(1)} = A^{-1} B^{(1)} = \begin{bmatrix} 5 & -2 \\ -2 & 1 \end{bmatrix}\begin{bmatrix} 4 \\ 9 \end{bmatrix} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}; \qquad X^{(2)} = A^{-1} B^{(2)} = \begin{bmatrix} 5 & -2 \\ -2 & 1 \end{bmatrix}\begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} 7 \\ -3 \end{bmatrix}.$$

### Exemplo 2 — Matriz $3 \times 3$ com frações (`MAT121_Sistemas` p. 24–31)
Para $\begin{cases} 2x + y + 3z = b_1 \\ 4x + 2y + 2z = b_2 \\ 2x + 5y + 3z = b_3 \end{cases}$, a redução `[A | I] -> [I | A^{-1}]` produz:
$$A^{-1} = \begin{bmatrix} -1/8 & 3/8 & -1/8 \\ -1/4 & 0 & 1/4 \\ 1/2 & -1/4 & 0 \end{bmatrix}$$
Para $B = \begin{bmatrix} 8 \\ 4 \\ -12 \end{bmatrix}$, $X = A^{-1} B = \begin{bmatrix} -1 + 12/8 + 12/8 \\ -2 + 0 - 3 \\ 4 - 1 + 0 \end{bmatrix} = \begin{bmatrix} 2 \\ -5 \\ 3 \end{bmatrix}$.

---

## 3. Exercícios (`C04-E01` a `C04-E05`)

### `C04-E01` *(Sistema $2 \times 2$ pelo método da matriz inversa)*
Considere o sistema $\begin{cases} 3x + 5y = 7 \\ x + 2y = 2 \end{cases}$:
**(a)** Calcule $A^{-1}$ via `[A | I] -> [I | A^{-1}]`.  
**(b)** Determine a solução $(x, y)$ calculando $X = A^{-1}B$.  
*Formato na caixa de resposta:* `inversa: [[..., ...], [..., ...]]; solucao: (x, y)`.

---

### `C04-E02` *(Matriz $3 \times 3$ e múltiplos termos independentes — Lista 5 Ex. 20 e 22)*
Para o sistema parametrizado nos termos independentes:
$$\begin{cases} x + 2y - 2z = b_1 \\ 2x + 5y - 4z = b_2 \\ 3x + 7y - 5z = b_3 \end{cases}$$
**(a)** Obtenha $A^{-1}$ por Gauss-Jordan em `[A | I]`.  
**(b)** Resolva $X^{(1)} = A^{-1}B^{(1)}$ para $(b_1, b_2, b_3) = (0, 3, 7)$.  
**(c)** Reaproveite $A^{-1}$ para resolver $X^{(2)} = A^{-1}B^{(2)}$ para $(b_1, b_2, b_3) = (1, 7, 6)$.  
*Formato na caixa de resposta:* `inversa: [[...], [...], [...]]; solucao1: (x1, y1, z1); solucao2: (x2, y2, z2)`.

---

### `C04-E03` *(Caça ao Bug — Matriz singular e ordem da multiplicação)*
Um estudante tentou resolver o sistema $\begin{cases} x + 2y + 3z = 1 \\ 2x + 4y + 6z = 3 \\ x + y + z = 0 \end{cases}$ pelo método da matriz inversa, mas não conseguiu chegar a $I_3$ no lado esquerdo de `[A | I]`. Além disso, em outro exercício, multiplicou `B * A^{-1}` em vez de `A^{-1} * B`.
Explique no papel por que os dois erros ocorrem e responda:  
**(a)** A matriz dos coeficientes $A$ é inversível (`sim` ou `nao`)?  
**(b)** Escalonando `[A | B]`, qual é a classificação do sistema (`SPD`, `SPI` ou `SI`)?  
*Formato na caixa de resposta:* `inversivel: nao (ou sim); classificacao: <SPD/SPI/SI>`.

---

### `C04-E04` *(Inversa com frações e reuso — Baseado em `MAT121_Sistemas` p. 30–31)*
Considere $A = \begin{bmatrix} 2 & 1 & 3 \\ 4 & 2 & 2 \\ 2 & 5 & 3 \end{bmatrix}$:  
**(a)** Verifique por escalonamento `[A | I]` a matriz inversa $A^{-1}$ (mantenha frações exatas).  
**(b)** Resolva o sistema $AX = \begin{bmatrix} 17 \\ 18 \\ 21 \end{bmatrix}$ usando $X = A^{-1}B$.  
*Formato na caixa de resposta:* `inversa: [[...], [...], [...]]; solucao: (x, y, z)`.

---

### `C04-E05` *(Inversa fracionária e múltiplas soluções)*
Seja $A = \begin{bmatrix} 1 & 1 & 1 \\ 0 & 2 & 1 \\ 1 & 3 & 3 \end{bmatrix}$:  
**(a)** Determine $A^{-1}$ pelo método `[A | I] -> [I | A^{-1}]`.  
**(b)** Resolva $AX = B^{(1)}$ para $B^{(1)} = \begin{bmatrix} 3 \\ 1 \\ 4 \end{bmatrix}$ e $AX = B^{(2)}$ para $B^{(2)} = \begin{bmatrix} 1 \\ 2 \\ 5 \end{bmatrix}$.  
*Formato na caixa de resposta:* `inversa: [[...], [...], [...]]; solucao1: (x1, y1, z1); solucao2: (x2, y2, z2)`.

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `C04-C01` *(Inversa $2 \times 2$ e dois vetores $B$)*
Dada $A = \begin{bmatrix} 4 & 3 \\ 3 & 2 \end{bmatrix}$:  
**(a)** Calcule $A^{-1}$ por `[A | I] -> [I | A^{-1}]`.  
**(b)** Resolva $AX = B^{(1)}$ para $B^{(1)} = \begin{bmatrix} 5 \\ 4 \end{bmatrix}$.  
**(c)** Resolva $AX = B^{(2)}$ para $B^{(2)} = \begin{bmatrix} 1 \\ -2 \end{bmatrix}$.  
*Formato na caixa de resposta:* `inversa: [[...], [...]]; solucao1: (x1, y1); solucao2: (x2, y2)`.

---

### `C04-C02` *(Inversa $3 \times 3$ completa sem consulta)*
Para o sistema $\begin{cases} x + 2z = 3 \\ 2x - y + 3z = 1 \\ 4x + y + 8z = 7 \end{cases}$:  
**(a)** Encontre $A^{-1}$ via `[A | I] -> [I | A^{-1}]`.  
**(b)** Calcule a solução $X = A^{-1}B$.  
*Formato na caixa de resposta:* `inversa: [[...], [...], [...]]; solucao: (x, y, z)`.

---

### `C04-C03` *(Reutilização da inversa — Lista 5 Ex. 23 e novo vetor)*
Sabendo que para $A = \begin{bmatrix} 1 & 2 & -2 \\ 2 & 5 & -4 \\ 3 & 7 & -5 \end{bmatrix}$ a inversa é $A^{-1} = \begin{bmatrix} 3 & -4 & 2 \\ -2 & 1 & 0 \\ -1 & -1 & 1 \end{bmatrix}$:  
**(a)** Resolva $AX = B^{(1)}$ para $B^{(1)} = \begin{bmatrix} 3 \\ 2 \\ 5 \end{bmatrix}$ *(Lista 5 Ex. 23)*.  
**(b)** Resolva $AX = B^{(2)}$ para $B^{(2)} = \begin{bmatrix} -1 \\ 0 \\ 2 \end{bmatrix}$.  
*Formato na caixa de resposta:* `solucao1: (x1, y1, z1); solucao2: (x2, y2, z2)`.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `C08` *(quando `C07` também estiver concluído)*:** somente após autocorreção de `C04-E01..E05` **e** **100% (3/3)** na Checagem Independente `C04-C01..C03`.
- **Recuperação direcionada (1ª falha):** verifique a multiplicação linha-por-coluna em $A^{-1}B$ e confira $A \cdot A^{-1} = I$ antes de multiplicar por $B$; aplique a variante `V2` de `C04`.
- **Após 2 tentativas malsucedidas:** recuar no DAG para **`B07`** *(inversão por Gauss-Jordan `[A | I] -> [I | A^{-1}]`)* ou **`C01`** *(forma matricial $AX=B$)*.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Sistemas.pdf` p. 22–32 (Método da Matriz Inversa $X = A^{-1}B$ e vantagem de reaproveitamento para múltiplos vetores $B$).
- `[DOC]` `Mat_Vet_L5.pdf` p. 3 (Ex. 20–23).
- Gabarito comentado e casos de verificação: [C04_gabarito.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_C/gabaritos/C04_gabarito.md) e [casos_C04.json](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_C/testes/casos_C04.json).
