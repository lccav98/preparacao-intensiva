# Bloco `G02` — Simulado Integrador P2 (Parte 1) — Sistemas Lineares e Parâmetros

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio G — Integração Geral e Simulados por Avaliação / **`G02`** |
| **Micro-habilidade foco** | Integrar, no padrão P2 sem consulta, escalonamento de sistemas $m \times n$ até a forma de escada $B$, determinação de postos ($C_A, C_V, C$) e grau de liberdade ($g = n - C$), discussão de sistemas homogêneos e não-homogêneos com parâmetros, e resolução via matriz inversa ($X = A^{-1}B$). |
| **Pré-requisitos** | `C08` *(Revisão cumulativa do Estágio C)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`G02-E01`–`G02-E05`, 25 min):** `16 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`G02-C01`–`G02-C03`, 18 min):** `14 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Simulado P2 (Parte 1) sem consulta.** **Proibido:** Regra de Cramer, Regra de Sarrus, Regra de Chió, Vandermonde e matriz adjunta. Empregue apenas operações elementares $L$, classificação por $C_A$ e $C_V$, grau de liberdade $g = n - C$ e inversão `[A \| I_n] -> [I_n \| A^{-1}]`. |

### Registro da Sessão (Preenchido na Prática)
- **Protocolo:** `PREP-MV-G02-<VARIANTE>-T<TENTATIVA>-<HASH>`
- **Sessão única (`G02-E01`–`G02-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`G02-C01`–`G02-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Critério de Classificação por Posto (`C_A, C_V, C`):**
   - Escalone a matriz ampliada $A$ até a forma de escada $B$; seja $V$ a submatriz dos coeficientes de $B$.
   - **$C_A > C_V$:** sistema **incompatível (`SI`)** (linha do tipo $[0 \dots 0 \mid c]$ com $c \neq 0$).
   - **$C_A = C_V = C = n$:** sistema **compatível e determinado (`SPD`)**, grau de liberdade $g = n - C = 0$ (solução única).
   - **$C_A = C_V = C < n$:** sistema **compatível e indeterminado (`SPI`)**, grau de liberdade $g = n - C \ge 1$ ($g$ variáveis livres com valores arbitrários).
2. **Sistemas Homogêneos ($AX = O$):**
   - Sempre compatíveis ($C_A = C_V = C$). Admitem **soluções próprias (não-triviais)** se e somente se $C < n$ (ou, quando $m = n$, $\det(A) = 0$).
3. **Discussão Paramétrica e Inversa:**
   - Em parâmetros na coluna dos termos independentes, **carregue a expressão simbólica** em todas as operações $L$ e iguale a zero a entrada do termo independente na linha zerada de $V$.
   - Quando $A_{(n,n)}$ é inversível, $AX = B \implies X = A^{-1}B$ (nunca use Cramer).

---

## 2. Exemplos Guiados

### Exemplo 1 — Compatibilidade com Parâmetro e Contagem de Posto
Dado um sistema $3\times 3$ em que a 3ª linha escalonada resulta em $[0 \;\; 0 \;\; 0 \mid k - 7]$:
- Para $k \neq 7$: $C_V = 2$ e $C_A = 3 \Rightarrow C_A > C_V$ (`SI`).
- Para $k = 7$: $C_V = C_A = C = 2 < 3 \Rightarrow g = 3 - 2 = 1$ (`SPI`), atribuindo valor arbitrário a 1 variável livre.

---

## 3. Exercícios (`G02-E01` a `G02-E05`)

### `G02-E01` *(Sistema sobredeterminado $4 \times 3$, forma de escada e posto)*
Escalone até a forma de escada $B$ o sistema $4 \times 3$ abaixo, informe $C_A$, $C_V$, $g$, a classificação (`SPD`, `SPI` ou `SI`) e a solução $(x, y, z)$:
$$\begin{cases} x + y + z = 4 \\ 2x - y + z = 8 \\ x + 2y - z = -3 \\ 3x + 2z = 12 \end{cases}$$

*Formato de resposta:* `ca: <int>; cv: <int>; g: <int>; classificacao: <SPD/SPI/SI>; solucao: (x, y, z)`.

---

### `G02-E02` *(Sistema subdeterminado $3 \times 4$ com $g = 2$ e valores arbitrários)*
Para o sistema nas incógnitas $(x, y, z, w)$:
$$\begin{cases} x + 2y - z + w = 3 \\ 2x + 5y + z - w = 8 \\ 3x + 7y = 11 \end{cases}$$
Obtenha a forma de escada $B$, informe $C_A$, $C_V$, $g$, a classificação e a solução particular $(x, y, z, w)$ obtida atribuindo os valores arbitrários **$z = 2$** e **$w = -1$**.

*Formato de resposta:* `ca: <int>; cv: <int>; g: <int>; classificacao: <SPD/SPI/SI>; solucao: (x, y, 2, -1)`.

---

### `G02-E03` *(Sistema homogêneo com parâmetro quadrático — sem perder raízes)*
Determine **todos** os valores reais de $k$ para os quais o sistema homogêneo abaixo admite **soluções próprias (não-triviais)** (resolva por escalonamento ou $\det(A) = 0$ via cofatores pela 1ª linha, **sem Sarrus**):
$$\begin{cases} x + y - z = 0 \\ 2x + ky + z = 0 \\ kx + 2y + z = 0 \end{cases}$$

*Formato de resposta:* lista de valores separados por vírgula (ex.: `k1, k2`).

---

### `G02-E04` *(Discussão paramétrica e solução particular compatível)*
Considere o sistema com parâmetro real $a$:
$$\begin{cases} x + 2y - z = 2 \\ 2x + 5y + z = a \\ x + 3y + 2z = 5 \end{cases}$$
**(a)** Determine o único valor real de $a$ para o qual o sistema é compatível (`SPI`).  
**(b)** Para esse valor de $a$, informe a solução particular $(x, y, z)$ obtida ao escolher **$z = 1$**.

*Formato de resposta:* `(a) valor_a (b) (x, y, 1)`.

---

### `G02-E05` *(Resolução pelo Método da Matriz Inversa $X = A^{-1}B$)*
Considere o sistema $AX = B$ dado por:
$$A = \begin{bmatrix} 1 & 1 & 1 \\ 0 & 2 & 1 \\ 1 & 0 & 2 \end{bmatrix}, \qquad X = \begin{bmatrix} x \\ y \\ z \end{bmatrix}, \qquad B = \begin{bmatrix} 4 \\ 3 \\ 5 \end{bmatrix}$$
**(a)** Calcule $A^{-1}$ via `[A | I_3] -> [I_3 | A^{-1}]`.  
**(b)** Usando $X = A^{-1}B$ (proibido Cramer), informe a solução $(x, y, z)$ em frações irredutíveis.

*Formato de resposta:* `(a) [[...], [...], [...]] (b) (x, y, z)`.

---

## 4. Checagem Independente (`G02-C01` a `G02-C03`)
*(Simulado P2 Parte 1 sem consulta. Critério de aprovação: **100% — 3/3**.)*

### `G02-C01` *(Classificação por posto $C_A > C_V$)*
Escalone o sistema abaixo até a forma de escada $B$ e informe $C_A$, $C_V$ e a classificação (`SPD`, `SPI` ou `SI`):
$$\begin{cases} x - y + 2z = 1 \\ 2x + y - z = 3 \\ 3x + z = 7 \end{cases}$$

*Formato de resposta:* `ca: <int>; cv: <int>; classificacao: <SPD/SPI/SI>`.

---

### `G02-C02` *(Homogêneo com parâmetro sem consulta)*
Determine **todos** os valores reais de $k$ para que o sistema homogêneo abaixo admita **soluções não-triviais**:
$$\begin{cases} x + y + z = 0 \\ 2x + ky + 2z = 0 \\ x + 2y + kz = 0 \end{cases}$$

*Formato de resposta:* lista de valores exatos (ex.: `k1, k2`).

---

### `G02-C03` *(Método da matriz inversa $X = A^{-1}B$ sem consulta)*
Dadas $A = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 2 & 1 \\ 1 & 0 & 1 \end{bmatrix}$ e $B = \begin{bmatrix} 3 \\ 5 \\ 4 \end{bmatrix}$:  
**(a)** Determine $A^{-1}$ via `[A | I_3] -> [I_3 | A^{-1}]`.  
**(b)** Resolva $AX = B$ por $X = A^{-1}B$ e informe $(x, y, z)$ em frações irredutíveis.

*Formato de resposta:* `(a) [[...], [...], [...]] (b) (x, y, z)`.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `G03` (`Simulado Integrador P2 — Parte 2`):** somente após autocorreção de `G02-E01`–`G02-E05` e **100% (3/3)** na Checagem Independente `G02-C01`–`G02-C03`.
- **Recuperação direcionada (1ª falha):** identifique o foco do erro (contagem de $C_A, C_V, g$ → `C05`; homogêneos e raízes de $k$ → `C06`; parâmetro no termo independente → `C07`; inversa $X = A^{-1}B$ → `C04`) e aplique a variante `V2` de `G02`.
- **Após 2 tentativas malsucedidas:** recuar no DAG para **`C08`** (ou diretamente ao pré-requisito específico **`C04`**, **`C05`**, **`C06`** ou **`C07`**).

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_RE42B_Planejamento.pdf` (Semanas 5–6 — 1ª metade da Avaliação P2).
- `[DOC]` `MAT121_Sistemas.pdf` p. 1–60; `Matrizes_Vetores_P2.pdf` p. 49–77; `Mat_Vet_L5.pdf` Ex. 1–23.
- Gabarito comentado e casos de teste: [G02_gabarito.md](../gabaritos/G02_gabarito.md) e [casos_G02.json](../testes/casos_G02.json).
