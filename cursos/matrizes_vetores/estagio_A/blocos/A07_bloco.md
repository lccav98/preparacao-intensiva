# Bloco `A07` — Matrizes Simétricas, Anti-Simétricas e Ortogonais

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio A — Matrizes: Definição, Operações, Transposta e Especiais / **`A07`** |
| **Micro-habilidade foco** | Classificar e parametrizar matrizes simétricas ($S^T = S$), anti-simétricas ($K^T = -K$, com diagonal nula) e ortogonais ($G \cdot G^T = I$), além de decompor qualquer matriz quadrada na soma $M = S + K$. |
| **Pré-requisitos** | `A06` |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`A07-E01`–`A07-E05`, 20 min):** `12 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`A07-C01`–`A07-C03`, 14 min):** `10 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** definição de matriz simétrica, anti-simétrica e ortogonal via transposição, simetria de $C + C^T$ e $C \cdot C^T$, anti-simetria de $C - C^T$ e decomposição $\frac{1}{2}(M + M^T) + \frac{1}{2}(M - M^T)$. **Proibido:** determinantes (`B01`), cálculo de inversa pelo algoritmo `[A|I]` (`B07`) e tópicos dos Estágios B–F. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`A07-E01`–`A07-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`A07-C01`–`A07-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Matriz simétrica (`S^T = S`):** uma matriz quadrada $S$ é simétrica quando $s_{ij} = s_{ji}$ para todos $i, j$ (espelhamento idêntico em relação à diagonal principal; a diagonal principal pode conter quaisquer valores).
2. **Matriz anti-simétrica (`K^T = -K`):** uma matriz quadrada $K$ é anti-simétrica quando $k_{ij} = -k_{ji}$ para todos $i, j$.
   - **Consequência obrigatória na diagonal principal ($i = j$):** $k_{ii} = -k_{ii} \implies 2k_{ii} = 0 \implies \mathbf{k_{ii} = 0}$. Toda matriz anti-simétrica tem **todos os elementos da diagonal principal nulos**!
3. **Construção imediata de simétricas e anti-simétricas:** para qualquer matriz $C$ quadrada:
   - $C + C^T$ e $C \cdot C^T$ são sempre **simétricas**;
   - $C - C^T$ é sempre **anti-simétrica**.
4. **Decomposição única `M = S + K`:** toda matriz quadrada $M$ se escreve de maneira única como soma de uma parcela simétrica $S$ e uma parcela anti-simétrica $K$:
   $$S = \frac{1}{2}(M + M^T), \qquad K = \frac{1}{2}(M - M^T).$$
5. **Matriz ortogonal (`G \cdot G^T = I`):** uma matriz quadrada $G$ é ortogonal quando o produto pela sua transposta resulta na identidade ($G \cdot G^T = G^T \cdot G = I$), como ocorre na matriz de rotação $G = \begin{bmatrix} \cos\theta & -\operatorname{sen}\theta \\ \operatorname{sen}\theta & \cos\theta \end{bmatrix}$.

---

## 2. Exemplos Guiados

### Exemplo 1 — Parametrização de anti-simétrica e decomposição `M = S + K`
Considere $A = \begin{bmatrix} p & -3 \\ q & r - 2 \end{bmatrix}$ anti-simétrica.
- Pela diagonal nula: $p = 0$ e $r - 2 = 0 \implies r = 2$.
- Pelos termos simétricos com sinal trocado: $q = -(-3) = 3$.

Para decompor $M = \begin{bmatrix} 2 & 5 \\ -1 & 4 \end{bmatrix}$:
- $S = \frac{1}{2}\left(\begin{bmatrix} 2 & 5 \\ -1 & 4 \end{bmatrix} + \begin{bmatrix} 2 & -1 \\ 5 & 4 \end{bmatrix}\right) = \begin{bmatrix} 2 & 2 \\ 2 & 4 \end{bmatrix}$ *(simétrica)*
- $K = \frac{1}{2}\left(\begin{bmatrix} 2 & 5 \\ -1 & 4 \end{bmatrix} - \begin{bmatrix} 2 & -1 \\ 5 & 4 \end{bmatrix}\right) = \begin{bmatrix} 0 & 3 \\ -3 & 0 \end{bmatrix}$ *(anti-simétrica)*
- Conferência: $S + K = \begin{bmatrix} 2 & 5 \\ -1 & 4 \end{bmatrix} = M$.

### Exemplo 2 — Verificação de ortogonalidade (`L2` Ex. 6)
Para $G = \begin{bmatrix} \cos\theta & -\operatorname{sen}\theta \\ \operatorname{sen}\theta & \cos\theta \end{bmatrix}$:
$$G \cdot G^T = \begin{bmatrix} \cos\theta & -\operatorname{sen}\theta \\ \operatorname{sen}\theta & \cos\theta \end{bmatrix} \begin{bmatrix} \cos\theta & \operatorname{sen}\theta \\ -\operatorname{sen}\theta & \cos\theta \end{bmatrix} = \begin{bmatrix} \cos^2\theta + \operatorname{sen}^2\theta & 0 \\ 0 & \operatorname{sen}^2\theta + \cos^2\theta \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I_2.$$
Logo, $G$ é **ortogonal**.

---

## 3. Exercícios (`A07-E01` a `A07-E05`)

### `A07-E01` *(Parametrização de simétrica e reconhecimento de anti-simétrica)*
**(a)** Determine o par $(x, y)$ para que a matriz $S = \begin{bmatrix} 2 & x + 1 & -3 \\ 5 & 0 & y - 2 \\ -3 & 4 & 7 \end{bmatrix}$ seja **simétrica**.  
**(b)** Classifique a matriz $E = \begin{bmatrix} 0 & -3 & 1 \\ 3 & 0 & -5 \\ -1 & 5 & 0 \end{bmatrix}$ quanto à simetria (`simetrica`, `anti-simetrica` ou `ortogonal`).

**Formato de resposta:** `(a) (x, y) (b) classificacao`.

---

### `A07-E02` *(Parametrização de anti-simétrica — armadilha da diagonal)*
Determine a quádrupla $(a, b, c, d)$ para que a matriz abaixo seja **anti-simétrica**:
$$K = \begin{bmatrix} a - 2 & -4 & b \\ 4 & 0 & 3 \\ 5 & c & d + 1 \end{bmatrix}$$

**Formato de resposta:** vetor `(a, b, c, d)`.

---

### `A07-E03` *(Propriedades de `C + C^T` e `C * C^T`)*
Dada a matriz $C = \begin{bmatrix} 1 & -3 & 2 \\ 5 & 0 & -1 \\ -4 & 2 & 3 \end{bmatrix}$:  
**(a)** Calcule $D = C + C^T$.  
**(b)** Classifique $D$ quanto à simetria (`simetrica` ou `anti-simetrica`).  
**(c)** Calcule $E = C \cdot C^T$.

**Formato de resposta:** `(a) [[...], [...], [...]] (b) classificacao (c) [[...], [...], [...]]`.

---

### `A07-E04` *(Decomposição `M = S + K`)*
Decomponha a matriz $M = \begin{bmatrix} 4 & 3 \\ -1 & 6 \end{bmatrix}$ na soma $M = S + K$, calculando:  
**(a)** a parcela simétrica $S = \frac{1}{2}(M + M^T)$;  
**(b)** a parcela anti-simétrica $K = \frac{1}{2}(M - M^T)$.

**Formato de resposta:** `(a) [[...], [...]] (b) [[...], [...]]`.

---

### `A07-E05` *(Verificação de matriz ortogonal)*
Considere a matriz $G = \begin{bmatrix} 3/5 & -4/5 \\ 4/5 & 3/5 \end{bmatrix}$.  
**(a)** Calcule o produto $G \cdot G^T$.  
**(b)** Classifique $G$ quanto à propriedade verificada (`simetrica`, `anti-simetrica` ou `ortogonal`).

**Formato de resposta:** `(a) [[...], [...]] (b) classificacao`.

---

## 4. Checagem Independente (`A07-C01` a `A07-C03`)

### `A07-C01` *(Parametrização anti-simétrica inédita)*
Determine a terna $(x, y, z)$ para que a matriz abaixo seja **anti-simétrica**:
$$A = \begin{bmatrix} x - 3 & 2 & y \\ -2 & z & -7 \\ 4 & 7 & 0 \end{bmatrix}$$

**Formato de resposta:** vetor `(x, y, z)`.

---

### `A07-C02` *(Decomposição `3x3` em parte simétrica e anti-simétrica)*
Para $M = \begin{bmatrix} 2 & 5 & -1 \\ 1 & 4 & 3 \\ 5 & -1 & 0 \end{bmatrix}$, calcule:  
**(a)** a parte simétrica $S = \frac{1}{2}(M + M^T)$;  
**(b)** a parte anti-simétrica $K = \frac{1}{2}(M - M^T)$.

**Formato de resposta:** `(a) [[...], [...], [...]] (b) [[...], [...], [...]]`.

---

### `A07-C03` *(Parâmetro de ortogonalidade com sinal `\pm`)*
Considere a matriz $Q = \begin{bmatrix} a & 12/13 \\ -12/13 & a \end{bmatrix}$.  
**(a)** Determine todos os valores reais de $a$ para os quais $Q$ é **ortogonal** ($Q \cdot Q^T = I_2$).  
**(b)** Para $a = 5/13$, calcule explicitamente $Q \cdot Q^T$.

**Formato de resposta:** `(a) a = +-... (b) [[...], [...]]`.

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `A09` (`Revisão Cumulativa do Estágio A`):** após autocorreção de `A07-E01`–`A07-E05` e **100% (3/3)** na Checagem Independente `A07-C01`–`A07-C03` sem consulta *(desde que também tenha concluído `A05` e `A08`)*.
- **Recuperação direcionada (1ª falha):**
  - Se esqueceu que a diagonal de uma matriz anti-simétrica é zero → releia o item 2 das Instruções Curtas e confira $k_{ii} = -k_{ii} \implies k_{ii} = 0$.
  - Se perdeu a raiz negativa em `A07-C03(a)` → confira os dois valores em $a^2 + 144/169 = 1$.
- **Após 2 tentativas malsucedidas:** recue para **`A06`** para revisar a construção de $A^T$ e multiplicação envolvendo transpostas antes de retornar a `A07`.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Matrizes.pdf` p. 18–20 (matrizes simétrica, anti-simétrica, decomposição $S+K$ e ortogonal).
- `[DOC]` `Mat_Vet_L2.pdf` Ex. 3–6 (classificação de $C+C^T$, $C\cdot C^T$, $C-C^T$ e $G \cdot G^T$).
- Gabarito comentado e casos de teste: [A07_gabarito.md](../gabaritos/A07_gabarito.md) e [casos_A07.json](../testes/casos_A07.json).
