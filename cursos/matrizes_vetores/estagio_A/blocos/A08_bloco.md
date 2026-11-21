# Bloco `A08` — Potências de Matrizes e Classificação Especial

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio A — Matrizes: Definição, Operações, Transposta e Especiais / **`A08`** |
| **Micro-habilidade foco** | Calcular potências sucessivas $A^2, A^3, \dots$ por multiplicação matricial e classificar matrizes **periódicas** (com período $k$), **idempotentes** ($A^2 = A$), **nilpotentes** (com índice $p$) e produtos de matrizes triangulares. |
| **Pré-requisitos** | `A05` |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`A08-E01`–`A08-E05`, 20 min):** `12 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`A08-C01`–`A08-C03`, 14 min):** `10 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** potências inteiras positivas $A^2 = A \cdot A$, $A^3 = A^2 \cdot A$, definições de periódica, idempotente, nilpotente e preservação da forma triangular no produto. **Proibido:** determinantes (`B01`), matriz inversa (`B06`) e tópicos avançados fora do escopo de `MAT121`. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`A08-E01`–`A08-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`A08-C01`–`A08-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Potência de matriz quadrada (`A^n`):** só existe para matrizes quadradas e é obtida por multiplicações sucessivas ($A^2 = A \cdot A$, $A^3 = A^2 \cdot A$, ...). **Nunca eleve os elementos individualmente!**
2. **Matriz periódica (notação Steinbruch):** uma matriz quadrada $A$ é **periódica** se existe um menor inteiro positivo $k \ge 1$ tal que:
   $$A^{k+1} = A.$$
   O menor $k$ que satisfaz $A^{k+1} = A$ é chamado de **período** de $A$.
3. **Matriz idempotente:** caso particular de matriz periódica de período $k = 1$, isto é:
   $$A^2 = A.$$
4. **Matriz nilpotente:** uma matriz quadrada $A$ é **nilpotente** se existe um menor inteiro positivo $p \ge 1$ tal que:
   $$A^p = [O].$$
   O menor $p$ para o qual a potência anula é chamado de **índice de nilpotência** de $A$.
5. **Produto de triangulares:** o produto de duas matrizes **triangulares superiores** (ou duas **triangulares inferiores**) de mesma ordem resulta sempre em outra matriz triangular do mesmo tipo.

---

## 2. Exemplos Guiados

### Exemplo 1 — Nilpotente vs. Idempotente (`L2` Ex. 7–8)
- Se $H = \begin{bmatrix} 6 & 9 \\ -4 & -6 \end{bmatrix}$, então $H^2 = \begin{bmatrix} 36-36 & 54-54 \\ -24+24 & -36+36 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} = [O]$. Como $H \neq [O]$ e $H^2 = [O]$, $H$ é **nilpotente** de índice $p = 2$.
- Se $J = \begin{bmatrix} 5 & 10 \\ -2 & -4 \end{bmatrix}$, então $J^2 = \begin{bmatrix} 25-20 & 50-40 \\ -10+8 & -20+16 \end{bmatrix} = \begin{bmatrix} 5 & 10 \\ -2 & -4 \end{bmatrix} = J$. Logo $J$ é **idempotente** (período $k = 1$).

### Exemplo 2 — Periódica de período $k = 2$
Se $M = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$, temos $M^2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \neq M$ e $M^3 = M^2 \cdot M = M$. Como $M^{2+1} = M$, $M$ é **periódica** de período $k = 2$.

---

## 3. Exercícios (`A08-E01` a `A08-E05`)

### `A08-E01` *(Identificação de matriz idempotente)*
Dada $J = \begin{bmatrix} 3 & -6 \\ 1 & -2 \end{bmatrix}$:  
**(a)** Calcule $J^2$.  
**(b)** Classifique $J$ entre: `idempotente`, `nilpotente` ou `identidade`.

**Formato de resposta:** `(a) [[...], [...]] (b) classificacao`.

---

### `A08-E02` *(Identificação de matriz nilpotente `2x2`)*
Dada $H = \begin{bmatrix} 4 & 8 \\ -2 & -4 \end{bmatrix}$:  
**(a)** Calcule $H^2$.  
**(b)** Classifique $H$ entre: `idempotente`, `nilpotente` ou `triangular superior`.

**Formato de resposta:** `(a) [[...], [...]] (b) classificacao`.

---

### `A08-E03` *(Nilpotência de índice `p = 3`)*
Considere $N = \begin{bmatrix} 0 & 2 & -1 \\ 0 & 0 & 3 \\ 0 & 0 & 0 \end{bmatrix}$.  
**(a)** Calcule $N^2$.  
**(b)** Calcule $N^3$.  
**(c)** Informe o **índice de nilpotência** $p$ de $N$.

**Formato de resposta:** `(a) [[...], [...], [...]] (b) [[...], [...], [...]] (c) numero`.

---

### `A08-E04` *(Matriz periódica e determinação do período `k`)*
Considere a matriz $L = \begin{bmatrix} 0 & 1 & -1 \\ 1 & 0 & -1 \\ 0 & 0 & 0 \end{bmatrix}$.  
**(a)** Calcule $L^2$.  
**(b)** Calcule $L^3 = L^2 \cdot L$.  
**(c)** Informe o **período** $k$ de $L$ na definição $L^{k+1} = L$.

**Formato de resposta:** `(a) [[...], [...], [...]] (b) [[...], [...], [...]] (c) numero`.

---

### `A08-E05` *(Produto de matrizes triangulares)*
Dadas $R = \begin{bmatrix} 2 & 0 & 0 \\ -1 & 3 & 0 \\ 4 & -2 & 1 \end{bmatrix}$ e $S = \begin{bmatrix} 1 & 0 & 0 \\ 2 & -2 & 0 \\ -3 & 1 & 5 \end{bmatrix}$:  
**(a)** Calcule $T = R \cdot S$.  
**(b)** Classifique a matriz $T$ (`triangular superior`, `triangular inferior`, `diagonal` ou `simetrica`).

**Formato de resposta:** `(a) [[...], [...], [...]] (b) classificacao`.

---

## 4. Checagem Independente (`A08-C01` a `A08-C03`)

### `A08-C01` *(Idempotência inédita)*
Dada $A = \begin{bmatrix} 2 & -2 \\ 1 & -1 \end{bmatrix}$:  
**(a)** Calcule $A^2$.  
**(b)** Classifique $A$ (`idempotente`, `nilpotente` ou `periodica de periodo 2`).

**Formato de resposta:** `(a) [[...], [...]] (b) classificacao`.

---

### `A08-C02` *(Nilpotência `3x3` inédita)*
Dada $B = \begin{bmatrix} 0 & 1 & 2 \\ 0 & 0 & -3 \\ 0 & 0 & 0 \end{bmatrix}$:  
**(a)** Calcule $B^2$.  
**(b)** Calcule $B^3$.  
**(c)** Classifique $B$ (`idempotente`, `nilpotente` ou `periodica`).

**Formato de resposta:** `(a) [[...], [...], [...]] (b) [[...], [...], [...]] (c) classificacao`.

---

### `A08-C03` *(Periodicidade inédita)*
Dada $M = \begin{bmatrix} 2 & 3 \\ -1 & -2 \end{bmatrix}$:  
**(a)** Calcule $M^2$.  
**(b)** Calcule $M^3$.  
**(c)** Classifique $M$ (`idempotente`, `nilpotente` ou `periodica`).

**Formato de resposta:** `(a) [[...], [...]] (b) [[...], [...]] (c) classificacao`.

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `A09` (`Revisão Cumulativa do Estágio A`):** após autocorreção de `A08-E01`–`A08-E05` e **100% (3/3)** na Checagem Independente `A08-C01`–`A08-C03` sem consulta *(desde que também tenha concluído `A07`)*.
- **Recuperação direcionada (1ª falha):**
  - Se elevou cada elemento ao quadrado em vez de multiplicar $A \cdot A$ → refaça `A08-E01` e `A08-C01` escrevendo $A \cdot A$ lado a lado.
  - Se confundiu período $k$ com o expoente $k+1$ em $L^{k+1} = L$ → verifique que $L^3 = L \implies k + 1 = 3 \implies k = 2$.
- **Após 2 tentativas malsucedidas:** recue para **`A05`** para revisar multiplicação sequencial de matrizes antes de retornar a `A08`.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Matrizes.pdf` p. 21–22 (definições de matriz periódica, idempotente e nilpotente).
- `[DOC]` `Mat_Vet_L2.pdf` Ex. 7–11 (nilpotente, idempotente, periódica e produto de triangulares).
- Gabarito comentado e casos de teste: [A08_gabarito.md](../gabaritos/A08_gabarito.md) e [casos_A08.json](../testes/casos_A08.json).
