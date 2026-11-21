# Bloco `A05` — Propriedades do Produto, Não-Comutatividade e Associatividade

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio A — Matrizes: Definição, Operações, Transposta e Especiais / **`A05`** |
| **Micro-habilidade foco** | Comprovar a não-comutatividade ($AB \neq BA$), parametrizar matrizes comutáveis, aplicar associatividade $(AB)C = A(BC)$ e distributividade, e reconhecer divisores de zero ($AB = [O]$ com $A, B \neq [O]$). |
| **Pré-requisitos** | `A04` |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`A05-E01`–`A05-E05`, 20 min):** `12 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`A05-C01`–`A05-C03`, 14 min):** `10 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** multiplicação de matrizes, associatividade, distributividade, identidade como elemento neutro ($AI = IA = A$), potência $A^2 = A \cdot A$ e divisores de zero. **Proibido:** transposta (`A06`), determinantes (`B01`) e matriz inversa (`B06`–`B07`). |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`A05-E01`–`A05-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`A05-C01`–`A05-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Não-comutatividade ($AB \neq BA$):** em geral, a ordem dos fatores altera o produto (mesmo quando $A$ e $B$ são quadradas de mesma ordem). Só afirmamos que $A$ e $B$ **comutam** quando $AB = BA$ é verificado.
2. **Consequência nos produtos notáveis:** como $AB \neq BA$, temos:
   $$(A + B)^2 = (A + B)(A + B) = A^2 + AB + BA + B^2 \neq A^2 + 2AB + B^2.$$
3. **Associatividade e Distributividade (válidas quando as ordens são compatíveis):**
   - $(AB)C = A(BC)$ *(muda o agrupamento, nunca a ordem da esquerda para a direita!)*
   - $A(B + C) = AB + AC$ e $(A + B)C = AC + BC$.
   - Elemento neutro: $A_{(m,n)} I_n = I_m A_{(m,n)} = A_{(m,n)}$.
4. **Divisores de zero em matrizes:** diferentemente dos números reais, podemos ter $A \cdot B = [O]$ com $A \neq [O]$ e $B \neq [O]$. Além disso, $AB = [O]$ **não** implica $BA = [O]$, nem permite cancelar $A$ em $AB = AC$ para concluir $B = C$.

---

## 2. Exemplos Guiados

### Exemplo 1 — Não-comutatividade e divisores de zero
Considere $A = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ e $B = \begin{bmatrix} 0 & 2 \\ 0 & 3 \end{bmatrix}$:
- $AB = \begin{bmatrix} 1(0)+0(0) & 1(2)+0(3) \\ 0(0)+0(0) & 0(2)+0(3) \end{bmatrix} = \begin{bmatrix} 0 & 2 \\ 0 & 0 \end{bmatrix}$
- $BA = \begin{bmatrix} 0(1)+2(0) & 0(0)+2(0) \\ 0(1)+3(0) & 0(0)+3(0) \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} = [O]$
Logo $AB \neq BA$, e $BA = [O]$ mesmo com $B \neq [O]$ e $A \neq [O]$.

### Exemplo 2 — Associatividade `(AB)C = A(BC)` (`L1` Ex. 8–9)
Para calcular $A_{(3,2)} B_{(2,2)} C_{(2,2)}$, você pode agrupar $(AB)C$ ou $A(BC)$: o resultado final tem sempre ordem $(3,2)$ e é idêntico nos dois caminhos, desde que não se troque a ordem relativa dos fatores.

---

## 3. Exercícios (`A05-E01` a `A05-E05`)

### `A05-E01` *(Verificação de não-comutatividade)*
Dadas $A = \begin{bmatrix} 2 & -1 \\ 3 & 0 \end{bmatrix}$ e $B = \begin{bmatrix} 1 & 4 \\ -2 & 5 \end{bmatrix}$, calcule:  
**(a)** $AB$  
**(b)** $BA$

**Formato de resposta:** `(a) [[...], [...]] (b) [[...], [...]]`.

---

### `A05-E02` *(Divisores de zero e assimetria de `AB` vs. `BA`)*
Considere as matrizes não nulas $A = \begin{bmatrix} 1 & -2 \\ -2 & 4 \end{bmatrix}$ e $B = \begin{bmatrix} 2 & 6 \\ 1 & 3 \end{bmatrix}$. Calcule:  
**(a)** $AB$  
**(b)** $BA$

**Formato de resposta:** `(a) [[...], [...]] (b) [[...], [...]]`.

---

### `A05-E03` *(Associatividade em produto de três matrizes)*
Dadas $A = \begin{bmatrix} 1 & -1 \\ 2 & 0 \\ -3 & 1 \end{bmatrix}$, $B = \begin{bmatrix} 2 & 3 \\ -1 & 4 \end{bmatrix}$ e $C = \begin{bmatrix} 1 & 0 \\ -2 & 3 \end{bmatrix}$:  
**(a)** Calcule a matriz intermediária $J = AB$.  
**(b)** Calcule $(AB)C = JC$ e confira que coincide com $A(BC)$.

**Formato de resposta:** `(a) [[...], [...], [...]] (b) [[...], [...], [...]]`.

---

### `A05-E04` *(Parametrização de matrizes comutáveis)*
Determine o par $(x, y)$ para que as matrizes $A = \begin{bmatrix} 1 & 2 \\ 1 & 0 \end{bmatrix}$ e $B = \begin{bmatrix} x & y \\ 1 & 2 \end{bmatrix}$ **comutem**, isto é, satisfaçam $AB = BA$.

**Formato de resposta:** vetor `(x, y)`.

---

### `A05-E05` *(Armadilha do produto notável em matrizes)*
Para $A = \begin{bmatrix} 1 & 2 \\ 0 & -1 \end{bmatrix}$ e $B = \begin{bmatrix} 2 & -1 \\ 3 & 1 \end{bmatrix}$, calcule:  
**(a)** $(A + B)^2 = (A + B)(A + B)$  
**(b)** $A^2 + 2AB + B^2$

**Formato de resposta:** `(a) [[...], [...]] (b) [[...], [...]]`.

---

## 4. Checagem Independente (`A05-C01` a `A05-C03`)

### `A05-C01` *(Não-comutatividade inédita)*
Dadas $A = \begin{bmatrix} 1 & 3 \\ -2 & 4 \end{bmatrix}$ e $B = \begin{bmatrix} 0 & -1 \\ 2 & 5 \end{bmatrix}$, calcule:  
**(a)** $AB$  
**(b)** $BA$

**Formato de resposta:** `(a) [[...], [...]] (b) [[...], [...]]`.

---

### `A05-C02` *(Parâmetros para comutatividade)*
Encontre o par $(x, y)$ tal que $A = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix}$ e $B = \begin{bmatrix} x & 2 \\ y & 3 \end{bmatrix}$ satisfaçam $AB = BA$.

**Formato de resposta:** vetor `(x, y)`.

---

### `A05-C03` *(Divisores de zero combinados com distributividade)*
Dadas $A = \begin{bmatrix} 2 & -1 \\ -4 & 2 \end{bmatrix}$, $B = \begin{bmatrix} 1 & 3 \\ 2 & 6 \end{bmatrix}$ e $C = \begin{bmatrix} 1 & 0 \\ -1 & 2 \end{bmatrix}$, calcule:  
**(a)** $AB$  
**(b)** $A(B + C)$

**Formato de resposta:** `(a) [[...], [...]] (b) [[...], [...]]`.

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `A08` (`Potências de Matrizes e Classificação Especial`):** após autocorreção de `A05-E01`–`A05-E05` e **100% (3/3)** na Checagem Independente `A05-C01`–`A05-C03` sem consulta *(observação: `A06` depende apenas de `A04`)*.
- **Recuperação direcionada (1ª falha):**
  - Se trocou $AB$ por $BA$ ou aplicou $(A+B)^2 = A^2 + 2AB + B^2$ → refaça `A05-E05` expandindo $(A+B)(A+B) = A^2 + AB + BA + B^2$.
  - Se errou o sistema em `A05-E04` ou `A05-C02` → compare as 4 posições de $AB = BA$ e confira se sua resposta satisfaz todas simultaneamente.
- **Após 2 tentativas malsucedidas:** recue para **`A04`** para consolidar a mecânica linha-por-coluna do produto de matrizes.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Matrizes.pdf` p. 14–15 (propriedades do produto, não-comutatividade e divisores de zero).
- `[DOC]` `Mat_Vet_L1.pdf` Ex. 8–9 (verificação de associatividade $(BA)C = B(AC)$).
- Gabarito comentado e casos de teste: [A05_gabarito.md](../gabaritos/A05_gabarito.md) e [casos_A05.json](../testes/casos_A05.json).
