# Bloco `A02` — Igualdade de Matrizes e Equações por Elementos

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio A — Matrizes: Definição, Operações, Transposta e Especiais / **`A02`** |
| **Micro-habilidade foco** | Aplicar a condição de igualdade entre matrizes ($m = p$, $n = q$ e $a_{ij} = b_{ij}$) para resolver equações lineares, sistemas acoplados e equações quadráticas nos elementos sem perder raízes ($\pm$). |
| **Pré-requisitos** | `A01` |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`A02-E01`–`A02-E05`, 20 min):** `12 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`A02-C01`–`A02-C03`, 14 min):** `10 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** igualdade de matrizes de mesma ordem, equações do 1º e 2º graus por posição, sistemas simples de duas incógnitas, matriz identidade `I_2` e lei de formação. **Proibido:** adição/subtração matricial como álgebra de blocos (`A03`), multiplicação de matrizes (`A04`), transposta (`A06`) e determinantes (`B01`). |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`A02-E01`–`A02-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`A02-C01`–`A02-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Definição de igualdade:** duas matrizes $A_{(m,n)} = [a_{ij}]$ e $B_{(p,q)} = [b_{ij}]$ são iguais ($A = B$) **se, e somente se**:
   - possuem a **mesma ordem** ($m = p$ e $n = q$); e
   - seus **elementos correspondentes são iguais**: $a_{ij} = b_{ij}$ para todo $1 \le i \le m$ e $1 \le j \le n$.
2. **Armadilha clássica nas equações quadráticas:** quando aparece $x^2 = c$ ($c > 0$), **ambas** as raízes $x = +\sqrt{c}$ e $x = -\sqrt{c}$ são soluções válidas (escreva $x = \pm\sqrt{c}$). Nunca descarte a raiz negativa sem restrição explícita no enunciado.
3. **Equação completa do 2º grau:** iguale todos os termos a zero ($k^2 - 12k + 36 = 0$) antes de fatorar ou aplicar Bhaskara; verifique se há raiz dupla (1 valor) ou duas raízes distintas.
4. **Sistemas acoplados:** quando duas posições envolvem o mesmo par de variáveis (ex.: $x + y = 5$ e $2x - y = 7$), resolva o sistema linear $2 \times 2$ antes de concluir os valores individuais.
5. **Consistência em elementos fixos:** sempre confira os demais elementos numéricos da matriz (ex.: $6 = 6$); se houver qualquer posição numérica desigual, não existe solução para $A = B$.

---

## 2. Exemplos Guiados

### Exemplo 1 — Igualdade com termos quadráticos (`L1` Ex. 1)
Determine $m$ e $n$ para que $A = B$, sendo:
$$A = \begin{bmatrix} m^2 - 40 & n^2 + 4 \\ 6 & 3 \end{bmatrix}, \quad B = \begin{bmatrix} 41 & 13 \\ 6 & 3 \end{bmatrix}$$
**Resolução:**
- Ordem: ambas são $2 \times 2$, e os elementos fixos conferem ($a_{21}=6=b_{21}$ e $a_{22}=3=b_{22}$).
- Posição $(1,1)$: $m^2 - 40 = 41 \implies m^2 = 81 \implies \mathbf{m = \pm 9}$.
- Posição $(1,2)$: $n^2 + 4 = 13 \implies n^2 = 9 \implies \mathbf{n = \pm 3}$.

### Exemplo 2 — Igualdade acoplada e conferência de consistência
Encontre $(x, y)$ tais que:
$$\begin{bmatrix} x + 2y & -3 \\ 3x - y & 4 \end{bmatrix} = \begin{bmatrix} 7 & -3 \\ 0 & 4 \end{bmatrix}$$
**Resolução:**
- Sistema por posições $(1,1)$ e $(2,1)$:
  - $x + 2y = 7 \implies x = 7 - 2y$
  - $3(7 - 2y) - y = 0 \implies 21 - 7y = 0 \implies y = 3 \implies x = 1$.
- Conferência: $1 + 2(3) = 7$ e $3(1) - 3 = 0$; posições fixas $-3 = -3$ e $4 = 4$. Resposta: $(x, y) = (1, 3)$.

---

## 3. Exercícios (`A02-E01` a `A02-E05`)

### `A02-E01` *(Igualdade linear direta)*
Dadas as matrizes $A$ e $B$ abaixo, sabendo que $A = B$, determine o par ordenado $(x, y)$:
$$A = \begin{bmatrix} 2x - 1 & 5 \\ 3 & y + 4 \end{bmatrix}, \quad B = \begin{bmatrix} 7 & 5 \\ 3 & -2 \end{bmatrix}$$

**Formato de resposta:** vetor `(x, y)`.

---

### `A02-E02` *(Equações quadráticas puras — atenção ao sinal `\pm`)*
Determine todos os valores reais possíveis de $m$ e $n$ para que $A = B$:
$$A = \begin{bmatrix} m^2 - 15 & n^2 + 3 \\ -2 & 8 \end{bmatrix}, \quad B = \begin{bmatrix} 10 & 19 \\ -2 & 8 \end{bmatrix}$$

**Formato de resposta:** `(a) m = +-... (b) n = +-...` (ou liste os valores separados por vírgula).

---

### `A02-E03` *(Equação do 2º grau completa e raiz dupla vs. raízes distintas)*
Calcule todos os valores reais de $k$ e de $p$ tais que:
$$\begin{bmatrix} 7 & k^2 \\ 4 & p^2 - 6p \end{bmatrix} = \begin{bmatrix} 7 & 12k - 36 \\ 4 & -5 \end{bmatrix}$$

**Formato de resposta:** `(a) k = ... (b) p = ..., ...` (em `(a)` e `(b)`, informe todas as raízes reais distintas).

---

### `A02-E04` *(Posições acopladas em sistema `2x2`)*
Determine o par $(x, y)$ para que as matrizes abaixo sejam iguais:
$$\begin{bmatrix} x + y & 3 \\ 2x - y & 4 \end{bmatrix} = \begin{bmatrix} 5 & 3 \\ 7 & 4 \end{bmatrix}$$

**Formato de resposta:** vetor `(x, y)`.

---

### `A02-E05` *(Integração com lei de formação e frações exatas)*
Seja $M_{(2,2)} = [m_{ij}]$ definida por $m_{ij} = \dfrac{2i - j}{3}$ e $N = \begin{bmatrix} a & 0 \\ b + \frac{1}{3} & 3c \end{bmatrix}$. Sabendo que $M = N$, determine a terna ordenada $(a, b, c)$ em frações irredutíveis.

**Formato de resposta:** vetor `(a, b, c)` (ex.: `(1/2, 1/3, 1/4)`).

---

## 4. Checagem Independente (`A02-C01` a `A02-C03`)

### `A02-C01` *(Quadráticas puras inéditas)*
Determine todos os valores reais de $p$ e de $q$ para que $A = B$:
$$A = \begin{bmatrix} p^2 - 20 & 4 \\ -1 & q^2 + 7 \end{bmatrix}, \quad B = \begin{bmatrix} 29 & 4 \\ -1 & 16 \end{bmatrix}$$

**Formato de resposta:** `(a) p = +-... (b) q = +-...`.

---

### `A02-C02` *(Acoplamento e raiz dupla)*
Determine o par $(a, b)$ e o valor real de $r$ para que:
$$\begin{bmatrix} 2a - b & 9 \\ a + 3b & r^2 \end{bmatrix} = \begin{bmatrix} 1 & 9 \\ 11 & 8r - 16 \end{bmatrix}$$

**Formato de resposta:** `(a) (a, b) (b) r`.

---

### `A02-C03` *(Igualdade com matriz identidade `I_2` e frações)*
Sabendo que a matriz $M = \begin{bmatrix} 3x - \frac{1}{2} & y^2 - \frac{9}{4} \\ 0 & \frac{z}{3} + 1 \end{bmatrix}$ é igual à matriz identidade $I_2$, determine:  
**(a)** o valor de $x$;  
**(b)** todos os valores reais de $y$;  
**(c)** o valor de $z$.

**Formato de resposta:** `(a) x (b) y = +-... (c) z`.

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `A03` (`Adição, Subtração e Multiplicação por Escalar`):** somente após autocorreção de `A02-E01`–`A02-E05` e **100% (3/3)** na Checagem Independente `A02-C01`–`A02-C03` sem consulta.
- **Recuperação direcionada (1ª falha):**
  - Se esqueceu a raiz negativa em $m^2 = c$ → refaça `A02-E02` e `A02-E03` escrevendo sempre a verificação das duas raízes na matriz original.
  - Se errou o sistema em `A02-E04` ou `A02-C02` → substitua a solução encontrada de volta nas duas equações antes de finalizar.
- **Após 2 tentativas malsucedidas:** volte ao pré-requisito **`A01`** para consolidar a indexação exata $a_{ij}$ e a construção de $I_2$ e leis de formação antes de tentar nova variante de `A02`.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Matrizes.pdf` p. 9 (definição de igualdade de matrizes).
- `[DOC]` `Mat_Vet_L1.pdf` Ex. 1–2 (equações quadráticas em elementos com raízes $\pm$ e raiz dupla).
- Gabarito comentado e casos de teste: [A02_gabarito.md](../gabaritos/A02_gabarito.md) e [casos_A02.json](../testes/casos_A02.json).
