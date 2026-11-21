# Bloco `B08` — Propriedades da Inversa e Equações Matriciais Simbólicas

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio B — Determinantes, Inversão (`[A\|I]`) e Equações Matriciais / **`B08`** |
| **Micro-habilidade foco** | Aplicar as propriedades da matriz inversa (`(AB)^{-1}=B^{-1}A^{-1}`, `(A^T)^{-1}=(A^{-1})^T`) e resolver equações matriciais simbólicas e numéricas respeitando a ordem **à esquerda vs. à direita**. |
| **Pré-requisitos** | `B06`, `A06` *(Definição da inversa e propriedades da transposta)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`B08-E01`–`B08-E05`, 22 min):** `14 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`B08-C01`–`B08-C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | Proibido usar matriz adjunta ou dividir matrizes (`B/A` não existe!). Sempre multiplique pela inversa do lado correto (esquerdo ou direito) em ambos os membros da equação. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`B08-E01`–`B08-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`B08-C01`–`B08-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Propriedades algébricas da inversa** *(supondo $A, B$ inversíveis de mesma ordem)*:
   - $(A^{-1})^{-1} = A$
   - **Inversa do produto (ordem reversa!):** $(AB)^{-1} = B^{-1}A^{-1}$ *(e $(ABC)^{-1} = C^{-1}B^{-1}A^{-1}$)*
   - **Inversa da transposta:** $(A^T)^{-1} = (A^{-1})^T$
   - **Escalar não nulo ($k \neq 0$):** $(kA)^{-1} = \frac{1}{k}A^{-1}$
2. **Ordem de multiplicação — Esquerda vs. Direita:** Como o produto de matrizes **não é comutativo**, para cancelar uma matriz inversível devemos multiplicar pelo **mesmo lado** em ambos os membros:
   - Se **$AX = B$**, multiplicamos por $A^{-1}$ **à esquerda**: $A^{-1}(AX) = A^{-1}B \implies \mathbf{X = A^{-1}B}$.
   - Se **$XA = B$**, multiplicamos por $A^{-1}$ **à direita**: $(XA)A^{-1} = BA^{-1} \implies \mathbf{X = BA^{-1}}$.
   - Se **$ADX = ABC$**, multiplicamos primeiro por $A^{-1}$ à esquerda ($DX = BC$) e depois por $D^{-1}$ à esquerda ($\mathbf{X = D^{-1}BC}$).
3. **Fatoração com a matriz identidade $I$:** Em equações como $AX - 2X = B$, **nunca** escreva $(A - 2)X$ *(não se subtrai escalar de matriz!)*. Use $X = IX$:
   $$AX - 2IX = B \implies (A - 2I)X = B \implies X = (A - 2I)^{-1}B$$

---

## 2. Exemplos Guiados

### Exemplo 1 — Isolamento simbólico com inversa e transposta
Supondo $D$ inversível, isole $X$ na equação $DX^T = DC$.
1. Multiplicamos ambos os membros por $D^{-1}$ **à esquerda**:
   $$D^{-1}(DX^T) = D^{-1}(DC) \implies I X^T = I C \implies X^T = C$$
2. Aplicamos a transposta em ambos os lados ($(X^T)^T = X$):
   $$\mathbf{X = C^T}$$

### Exemplo 2 — Equação numérica com fatoração `AX + 2X = B`
Dadas $A = \begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix}$ e $B = \begin{bmatrix} 3 & -2 \\ 6 & 4 \end{bmatrix}$, encontre $X$ tal que $AX + 2X = B$.
1. Fatoramos $X$ à direita usando $2X = 2IX$: $(A + 2I)X = B$.
2. Calculamos $M = A + 2I = \begin{bmatrix} 3 & 2 \\ 0 & 3 \end{bmatrix}$.
3. Por `[M | I_2] -> [I_2 | M^{-1}]`, obtemos $M^{-1} = \begin{bmatrix} 1/3 & -2/9 \\ 0 & 1/3 \end{bmatrix}$.
4. Multiplicando à esquerda: $X = M^{-1}B = \begin{bmatrix} 1/3 & -2/9 \\ 0 & 1/3 \end{bmatrix}\begin{bmatrix} 3 & -2 \\ 6 & 4 \end{bmatrix} = \begin{bmatrix} -1/3 & -14/9 \\ 2 & 4/3 \end{bmatrix}$.

---

## 3. Exercícios (`B08-E01` a `B08-E05`)

### `B08-E01` *(Isolamento simbólico respeitando multiplicação à esquerda)*
Supondo que $A$ e $D$ sejam matrizes quadradas inversíveis de mesma ordem, isole $X$ na equação matricial abaixo (escreva no formato `X = ...`):
$$ADX = ABC$$

---

### `B08-E02` *(Não-comutatividade: `AX = B` vs. `YA = B`)*
Dadas $A = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix}$ e $B = \begin{bmatrix} 4 & -2 \\ 0 & 3 \end{bmatrix}$:  
**(a)** Resolva $AX = B$ (isolando $X = A^{-1}B$).  
**(b)** Resolva $YA = B$ (isolando $Y = BA^{-1}$).

---

### `B08-E03` *(Transposta combinada com inversa conhecida)*
Sabendo que $A^{-1} = \begin{bmatrix} 1 & -1 \\ 2 & 0 \end{bmatrix}$ e $B = \begin{bmatrix} 3 & 1 \\ -2 & 4 \end{bmatrix}$, isole $X$ e calcule a matriz resultante para a equação:
$$(AX)^T = B$$

---

### `B08-E04` *(Conjugação por matriz inversível: `D^{-1}XD = A`)*
Dadas $D = \begin{bmatrix} 3 & 1 \\ 2 & 1 \end{bmatrix}$ e $A = \begin{bmatrix} 1 & -2 \\ 0 & 4 \end{bmatrix}$, isole $X$ na equação $D^{-1}XD = A$ e calcule exatamente a matriz $X$.

---

### `B08-E05` *(Fatoração à esquerda e inversão: `AX + BX = C`)*
Dadas $A = \begin{bmatrix} 1 & 3 \\ -1 & 2 \end{bmatrix}$, $B = \begin{bmatrix} 1 & -1 \\ 2 & 1 \end{bmatrix}$ e $C = \begin{bmatrix} 4 & 2 \\ 1 & 5 \end{bmatrix}$, isole $X$ em $AX + BX = C$ e calcule a matriz $X$ exata.

---

## 4. Checagem Independente (`B08-C01` a `B08-C03`)
*(Sem consulta e sem calculadora. Critério de aprovação: **100% — 3/3**.)*

### `B08-C01` *(Isolamento simbólico bilateral)*
Supondo $D$ inversível, isole $X$ na equação matricial (escreva no formato `X = ...`):
$$D^{-1} X D = A C$$

---

### `B08-C02` *(Fatoração com matriz identidade: `AX - 2X = B`)*
Dadas $A = \begin{bmatrix} 5 & 1 \\ 2 & 4 \end{bmatrix}$ e $B = \begin{bmatrix} 3 & -1 \\ 4 & 2 \end{bmatrix}$, resolva $AX - 2X = B$ determinando exatamente a matriz $X$.

---

### `B08-C03` *(Equação com transposta e inversa fornecida)*
Sabendo que $A^{-1} = \begin{bmatrix} 2 & -1 \\ 1 & 3 \end{bmatrix}$ e $B = \begin{bmatrix} 1 & 4 \\ -2 & 0 \end{bmatrix}$, calcule a matriz $X$ que satisfaz:
$$(AX)^T = B$$

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `B09` (`Revisão Cumulativa do Estágio B — Simulado P1`):** somente após autocorreção de `B08-E01`–`B08-E05` e **100% (3/3)** na Checagem Independente `B08-C01`–`B08-C03`.
- **Recuperação direcionada (1ª falha):** identificar se houve troca entre multiplicação à esquerda ($A^{-1}B$) e à direita ($BA^{-1}$), erro na inversão da ordem em $(AB)^{-1} = B^{-1}A^{-1}$ ou esquecimento de $I$ ao fatorar $AX - 2IX$. Refazer o Exemplo 1 e o Exemplo 2 e aplicar a variante `V2`.
- **Após 2 tentativas malsucedidas:** recuar para **`A06`** se o erro envolveu propriedades da transposta ($(AX)^T = X^T A^T$), ou para **`B06`** se houve erro na inversão `2x2` ou no produto $A\cdot A^{-1} = I$.
