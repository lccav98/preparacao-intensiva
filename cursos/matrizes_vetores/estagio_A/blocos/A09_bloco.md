# Bloco `A09` — Revisão Cumulativa do Estágio A

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio A — Matrizes: Definição, Operações, Transposta e Especiais / **`A09`** |
| **Micro-habilidade foco** | Integrar, sem consulta, lei de formação, igualdade paramétrica ($\pm$), combinações lineares, produto não comutativo, propriedade reversa $(AB)^T = B^T A^T$, decomposição simétrica/anti-simétrica, ortogonalidade e potências especiais. |
| **Pré-requisitos** | `A05`, `A07`, `A08` |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`A09-E01`–`A09-E05`, 20 min):** `12 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`A09-C01`–`A09-C03`, 14 min):** `10 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** todo o repertório de `A01`–`A08` com aritmética exata em frações irredutíveis. **Proibido:** determinantes (`B01`–`B05`), matriz inversa por definição ou por `[A|I]` (`B06`–`B07`), escalonamento de sistemas (`C01`) e vetores (`D01`). |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`A09-E01`–`A09-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`A09-C01`–`A09-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Checklist rápido do Estágio A antes de resolver:**
   - **Igualdade (`A02`):** mesma ordem e $a_{ij} = b_{ij}$; em $x^2 = c > 0$, lembre sempre do sinal **$\pm$**.
   - **Produto (`A04`–`A05`):** $A_{(m,n)} B_{(n,\ell)} = C_{(m,\ell)}$; em geral $AB \neq BA$ e $AB = [O]$ não implica $A=[O]$ ou $B=[O]$.
   - **Transposição (`A06`):** $(A+B)^T = A^T + B^T$ e **$(AB)^T = B^T A^T$** (ordem invertida!).
   - **Simetria e Ortogonalidade (`A07`):** simétrica $S^T = S$; anti-simétrica $K^T = -K$ (diagonal nula!); decomposição $M = \frac{1}{2}(M+M^T) + \frac{1}{2}(M-M^T)$; ortogonal $G \cdot G^T = I$.
   - **Potências especiais (`A08`):** idempotente ($A^2 = A$), nilpotente ($A^p = [O]$, índice $p$), periódica ($A^{k+1} = A$, período $k$).
2. **Estratégia de prova:** isole incógnitas matriciais simbolicamente antes de substituir números e verifique suas contas por uma segunda propriedade (ex.: confira se $S^T = S$ e $S + K = M$).

---

## 2. Exemplos Guiados

### Exemplo 1 — Encadeamento lei de formação + transposta + simetria
Se $A_{(2,2)}$ tem $a_{ij} = i - 2j$, então $A = \begin{bmatrix} -1 & -3 \\ 0 & -2 \end{bmatrix}$ e $A^T = \begin{bmatrix} -1 & 0 \\ -3 & -2 \end{bmatrix}$. A soma $A + A^T = \begin{bmatrix} -2 & -3 \\ -3 & -4 \end{bmatrix}$ é sempre **simétrica**, enquanto $A - A^T = \begin{bmatrix} 0 & -3 \\ 3 & 0 \end{bmatrix}$ é sempre **anti-simétrica**.

### Exemplo 2 — Propriedade reversa + verificação de potência
Se $P = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$, então $P^2 = I_2 \neq P$ e $P^3 = P$ (periódica de período $k = 2$). Além disso, $P \cdot P^T = P^2 = I_2$, mostrando que $P$ também é **ortogonal** (e simétrica!).

---

## 3. Exercícios (`A09-E01` a `A09-E05`)

### `A09-E01` *(Lei de formação + igualdade com raízes `\pm`)*
Construa a matriz $A_{(2,2)} = [a_{ij}]$ definida por $a_{ij} = 3i - 2j$ e iguale-a à matriz $B = \begin{bmatrix} x^2 - 8 & -1 \\ 4 & y^2 - 14 \end{bmatrix}$. Determine todos os valores reais possíveis de:  
**(a)** $x$  
**(b)** $y$

**Formato de resposta:** `(a) x = +-... (b) y = +-...`.

---

### `A09-E02` *(Combinação linear com transposta)*
Dadas $A = \begin{bmatrix} 1 & -2 & 3 \\ 0 & 4 & -1 \end{bmatrix}$, $B = \begin{bmatrix} -1 & 3 & 2 \\ 2 & -1 & 5 \end{bmatrix}$ e $C = \begin{bmatrix} 2 & -1 \\ 0 & 3 \\ -2 & 1 \end{bmatrix}$, calcule:
$$X = (2A - B)^T + 3C$$

**Formato de resposta:** matriz `[[...], [...], [...]]`.

---

### `A09-E03` *(Não-comutatividade e transposição do produto)*
Dadas $A = \begin{bmatrix} 2 & -1 \\ 1 & 3 \end{bmatrix}$ e $B = \begin{bmatrix} 0 & 4 \\ -2 & 1 \end{bmatrix}$, calcule:  
**(a)** $(AB)^T$  
**(b)** $(BA)^T$

**Formato de resposta:** `(a) [[...], [...]] (b) [[...], [...]]`.

---

### `A09-E04` *(Decomposição simétrica/anti-simétrica e ortogonalidade)*
Considere as matrizes $M = \begin{bmatrix} 3 & 5 \\ -1 & 7 \end{bmatrix}$ e $Q = \begin{bmatrix} 8/17 & -15/17 \\ 15/17 & 8/17 \end{bmatrix}$:  
**(a)** Calcule a parte simétrica $S = \frac{1}{2}(M + M^T)$.  
**(b)** Calcule a parte anti-simétrica $K = \frac{1}{2}(M - M^T)$.  
**(c)** Verifique $Q \cdot Q^T$ e classifique $Q$ (`ortogonal`, `simetrica` ou `nilpotente`).

**Formato de resposta:** `(a) [[...], [...]] (b) [[...], [...]] (c) classificacao`.

---

### `A09-E05` *(Potências e classificação especial)*
Dadas $H = \begin{bmatrix} 2 & 4 \\ -1 & -2 \end{bmatrix}$ e $J = \begin{bmatrix} 4 & -6 \\ 2 & -3 \end{bmatrix}$:  
**(a)** Calcule $H^2$.  
**(b)** Calcule $J^2$.  
**(c)** Classifique a matriz $H$ (`idempotente`, `nilpotente` ou `ortogonal`).

**Formato de resposta:** `(a) [[...], [...]] (b) [[...], [...]] (c) classificacao`.

---

## 4. Checagem Independente (`A09-C01` a `A09-C03`)

### `A09-C01` *(Equação matricial com `X^T` e frações)*
Dadas $A = \begin{bmatrix} 3 & -1 \\ 2 & 5 \end{bmatrix}$ e $B = \begin{bmatrix} 1 & 4 \\ -2 & 0 \end{bmatrix}$, determine a matriz $X$ que satisfaz:
$$2X^T - A = B$$

**Formato de resposta:** matriz `[[...], [...]]` com frações irredutíveis.

---

### `A09-C02` *(Comutatividade + regra reversa `(AB)^T = B^T A^T`)*
Considere $A = \begin{bmatrix} 1 & 3 \\ 0 & 2 \end{bmatrix}$ e $B = \begin{bmatrix} x & 6 \\ y & 4 \end{bmatrix}$.  
**(a)** Determine o par $(x, y)$ para que $A$ e $B$ comutem ($AB = BA$).  
**(b)** Para esse par $(x, y)$ encontrado, calcule $B^T \cdot A^T$.

**Formato de resposta:** `(a) (x, y) (b) [[...], [...]]`.

---

### `A09-C03` *(Integração: potência especial + decomposição anti-simétrica)*
Considere a matriz $P = \begin{bmatrix} -3 & -6 \\ 2 & 4 \end{bmatrix}$.  
**(a)** Calcule $P^2$.  
**(b)** Classifique $P$ quanto à sua potência (`idempotente`, `nilpotente` ou `periodica de periodo 2`).  
**(c)** Calcule a parcela anti-simétrica $K = \frac{1}{2}(P - P^T)$ da decomposição de $P$.

**Formato de resposta:** `(a) [[...], [...]] (b) classificacao (c) [[...], [...]]`.

---

## 5. Critério de Domínio e Recuperação

- **Avançar para o Estágio B (`B01` — Determinante de 2ª e 3ª Ordem):** somente após autocorreção de `A09-E01`–`A09-E05` e **100% (3/3)** na Checagem Independente `A09-C01`–`A09-C03` sem consulta.
- **Recuperação direcionada (1ª falha):** identifique exatamente em qual micro-habilidade ocorreu o deslize (igualdade $\pm$ → `A02`; produto/comutatividade → `A04`/`A05`; transposta → `A06`; simetria/ortogonalidade → `A07`; potências → `A08`) e refaça 1 exercício daquele bloco antes da variante `V2`.
- **Após 2 tentativas malsucedidas:** interrompa `A09` e retorne ao pré-requisito específico responsável pela falha (`A05`, `A07` ou `A08`) conforme o DAG curricular.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Matrizes.pdf` p. 1–22 (síntese completa de matrizes até classificações especiais).
- `[DOC]` `Matrizes_Vetores_P1.pdf` p. 1–24 (caderno manuscrito da Parte 1 — Matrizes).
- `[DOC]` `Mat_Vet_L1.pdf` e `Mat_Vet_L2.pdf` (listas oficiais integrais do Estágio A).
- Gabarito comentado e casos de teste: [A09_gabarito.md](../gabaritos/A09_gabarito.md) e [casos_A09.json](../testes/casos_A09.json).
