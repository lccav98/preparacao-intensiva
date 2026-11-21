# Bloco `C01` — Equação Linear, Forma Matricial, Matriz Ampliada e Operações Elementares `L`

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio C — Sistemas Lineares, Escalonamento, Posto (`C_A, C_V`) e Parâmetros / **`C01`** |
| **Micro-habilidade foco** | Reconhecer equações lineares e suas raízes, converter sistemas na forma matricial $AX = B$ e na matriz ampliada $A$, e executar exatamente as três operações elementares $L_{ij}$, $L_i(\alpha)$ e $L_j' = L_j + L_i(\alpha)$. |
| **Pré-requisitos** | `A04` *(Produto de matrizes e $AX = B$)* e `B04` *(Operações elementares em matrizes)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Prática (`C01-E01`–`C01-E05`, 18 min):** `11 min` resol. \| `4 min` corr. \| `3 min` recup.; **Checagem (`C01-C01`–`C01-C03`, 12 min):** `8 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Proibido:** Regra de Cramer, Regra de Sarrus ou matriz adjunta. Use estritamente a notação $L_{ij}$, $L_i(\alpha)$ ($\alpha \neq 0$) e $L_j' = L_j + L_i(\alpha)$ sobre a matriz ampliada com traço vertical separador. Mantenha frações irredutíveis exatas (sem arredondamento decimal). |

### Registro da Sessão (Preenchido na Prática)
- **Protocolo:** `PREP-MV-C01-<VARIANTE>-T<TENTATIVA>-<HASH>`
- **Prática (`C01-E01`–`C01-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`C01-C01`–`C01-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Equação linear:** toda equação da forma
   $$a_1 x_1 + a_2 x_2 + \dots + a_n x_n = b$$
   em que $x_1, \dots, x_n$ são as variáveis (todas no **1º grau**, sem produtos entre variáveis, potências $\neq 1$, raízes ou funções trigonométricas), $a_1, \dots, a_n \in \mathbb{R}$ são os **coeficientes** e $b \in \mathbb{R}$ é o **termo independente**.
2. **Solução (raízes):** uma $n$-upla $(r_1, r_2, \dots, r_n)$ é solução de um sistema se satisfaz **todas** as equações simultaneamente.
3. **Forma matricial $AX = B$ e matriz ampliada:** dado um sistema com $m$ equações e $n$ variáveis alinhadas na mesma ordem (preenchendo com `0` variáveis ausentes):
   - Escrevemos $A_{\text{coef}} X = B_{\text{ind}}$ (na notação de sistema, $AX=B$ ou matriz ampliada $A = [A_{\text{coef}} \mid B_{\text{ind}}]$ separada por barra vertical).
   - **Atenção:** a coluna mais à direita da matriz ampliada contém os termos independentes $b_i$; qualquer operação de linha aplicada à matriz ampliada deve afetar **toda a linha**, inclusive o termo independente.
4. **Sistemas equivalentes e as 3 operações elementares (`A.42`–`A.43`):** dois sistemas são **equivalentes** ($A \sim B$) quando possuem exatamente o mesmo conjunto solução. Um sistema se transforma em outro equivalente ao aplicar:
   - **I) Permutação de duas equações (linhas):** $L_{ij}$ *(troca a linha $i$ com a linha $j$)*.
   - **II) Multiplicação de uma linha por escalar $\alpha \neq 0$:** $L_i(\alpha)$ *(multiplica todos os elementos da linha $i$ por $\alpha \neq 0$)*.
   - **III) Substituição de uma linha pela soma com outra multiplicada por $\alpha \neq 0$:** $L_j' = L_j + L_i(\alpha)$ *(altera apenas a linha $j$; a linha pivô $i$ permanece inalterada)*.

---

## 2. Exemplos Guiados

### Exemplo 1 — Forma matricial e matriz ampliada com variável ausente e desalinhada
Considere o sistema nas variáveis $(x, y, z)$:
$$\begin{cases} 3x - 2z = 5 \\ 2y + x - z = -4 \\ 4y + 7z = 1 \end{cases}$$
1. **Alinhe as variáveis na ordem $(x, y, z)$** e complete coeficientes ausentes com `0`:
   $$\begin{cases} 3x + 0y - 2z = 5 \\ 1x + 2y - 1z = -4 \\ 0x + 4y + 7z = 1 \end{cases}$$
2. **Forma matricial:**
   $$\begin{bmatrix} 3 & 0 & -2 \\ 1 & 2 & -1 \\ 0 & 4 & 7 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 5 \\ -4 \\ 1 \end{bmatrix}$$
3. **Matriz ampliada $A$:**
   $$A = \left[\begin{array}{ccc|c} 3 & 0 & -2 & 5 \\ 1 & 2 & -1 & -4 \\ 0 & 4 & 7 & 1 \end{array}\right]$$

### Exemplo 2 — Aplicação sequencial de $L_{12}$, $L_2(\alpha)$ e $L_j' = L_j + L_i(\alpha)$
Partindo de $A = \left[\begin{array}{ccc|c} 0 & 2 & -4 & 6 \\ 2 & 4 & -2 & 8 \\ 4 & -2 & 2 & 10 \end{array}\right]$, aplicamos:
1. $L_{12}$ *(para colocar elemento não nulo na posição $(1,1)$)*:
   $$\left[\begin{array}{ccc|c} 2 & 4 & -2 & 8 \\ 0 & 2 & -4 & 6 \\ 4 & -2 & 2 & 10 \end{array}\right]$$
2. $L_1(1/2)$ *(pivô $1$ na 1ª linha)*:
   $$\left[\begin{array}{ccc|c} 1 & 2 & -1 & 4 \\ 0 & 2 & -4 & 6 \\ 4 & -2 & 2 & 10 \end{array}\right]$$
3. $L_3' = L_3 + L_1(-4)$ *(zera a posição $(3,1)$ mantendo $L_1$ intacta)*:
   $$\left[\begin{array}{ccc|c} 1 & 2 & -1 & 4 \\ 0 & 2 & -4 & 6 \\ 0 & -10 & 6 & -6 \end{array}\right]$$

---

## 3. Exercícios (`C01-E01` a `C01-E05`)

### `C01-E01` *(Classificação de Equação Linear e Verificação de Raiz — Reprodução do modelo)*
**(a)** Classifique a equação $3x - 2xy + z = 7$ como `linear` ou `nao linear`.  
**(b)** Determine o valor real de $k$ para que a terna $(2, -1, k)$ seja solução da equação linear $3x - 2y + 4z = 20$.  
*Formato na caixa de resposta:* `a: linear (ou nao linear); b: <valor de k>`.

---

### `C01-E02` *(Construção da Matriz Ampliada — Variável ausente)*
Escreva a matriz ampliada $A$ (ordem $3 \times 4$, com variáveis ordenadas em $x, y, z$) correspondente ao sistema:
$$\begin{cases} 2x - y + 3z = 7 \\ 4x + 5z = -2 \\ -x + 3y - 2z = 9 \end{cases}$$
*Formato na caixa de resposta:* matriz $3 \times 4$ sem a barra vertical, ex.: `[[a11, a12, a13, b1], [a21, a22, a23, b2], [a31, a32, a33, b3]]`.

---

### `C01-E03` *(Caça ao Bug em Operações Elementares)*
Ao escalonar a matriz ampliada do sistema $\begin{cases} 2x + 4y = 10 \\ 4x - 2y = 6 \end{cases}$, um estudante aplicou $L_1(1/2)$ e em seguida $L_2' = L_2 + L_1(-4)$, obtendo incorretamente $\left[\begin{array}{cc|c} 1 & 2 & 10 \\ 0 & -10 & -34 \end{array}\right]$.
Identifique no papel qual falha foi cometida na coluna dos termos independentes e escreva a matriz ampliada $2 \times 3$ **correta** após essas duas operações.  
*Formato na caixa de resposta:* matriz $2 \times 3$, ex.: `[[..., ..., ...], [..., ..., ...]]`.

---

### `C01-E04` *(Aplicação Sequencial de Operações $L_{ij}$, $L_i(\alpha)$ e $L_j' = L_j + L_i(\alpha)$)*
Dada a matriz ampliada
$$A = \left[\begin{array}{ccc|c} 0 & 3 & -6 & 9 \\ 2 & -4 & 6 & 8 \\ -2 & 1 & 5 & -3 \end{array}\right]$$
aplique, **estritamente nesta ordem**, as operações:
1. $L_{12}$
2. $L_1(1/2)$
3. $L_3' = L_3 + L_1(2)$

Escreva a matriz ampliada resultante (ordem $3 \times 4$).  
*Formato na caixa de resposta:* `[[..., ..., ..., ...], [..., ..., ..., ...], [..., ..., ..., ...]]`.

---

### `C01-E05` *(Operações Elementares com Frações Irredutíveis)*
Considere a matriz ampliada $A = \left[\begin{array}{ccc|c} 1 & -2 & 3 & 4 \\ 2 & 1 & -1 & 3 \end{array}\right]$.
Aplique em sequência:
1. $L_2' = L_2 + L_1(-2)$
2. $L_2(1/5)$

Escreva a matriz ampliada resultante (ordem $2 \times 4$) mantendo frações irredutíveis exatas.  
*Formato na caixa de resposta:* `[[..., ..., ..., ...], [..., ..., ..., ...]]`.

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `C01-C01` *(Alinhamento de Variáveis e Matriz Ampliada)*
Escreva a matriz ampliada $A$ ($3 \times 4$) na ordem de variáveis $(x, y, z)$ para o sistema:
$$\begin{cases} 3y - x + 2z = 4 \\ 2x + z = -5 \\ y - 4z = 1 \end{cases}$$
*Formato na caixa de resposta:* `[[..., ..., ..., ...], [..., ..., ..., ...], [..., ..., ..., ...]]`.

---

### `C01-C02` *(Sequência de Operações Elementares)*
Partindo de $A = \left[\begin{array}{ccc|c} 3 & -6 & 9 & 12 \\ 6 & -10 & 15 & 20 \\ -3 & 8 & -5 & -7 \end{array}\right]$, aplique em sequência:
1. $L_1(1/3)$
2. $L_2' = L_2 + L_1(-6)$
3. $L_3' = L_3 + L_1(3)$

Informe a matriz ampliada resultante ($3 \times 4$).  
*Formato na caixa de resposta:* `[[..., ..., ..., ...], [..., ..., ..., ...], [..., ..., ..., ...]]`.

---

### `C01-C03` *(Verificação de Raiz e Coeficiente)*
Considere o sistema $\begin{cases} mx + 4y - z = 5 \\ x - 2y + z = 7 \end{cases}$ e a terna $(x, y, z) = (2, -1, 3)$:  
**(a)** Determine o valor de $m$ que torna $(2, -1, 3)$ solução da 1ª equação.  
**(b)** A terna $(2, -1, 3)$ satisfaz também a 2ª equação? Responda `sim` ou `nao`.  
*Formato na caixa de resposta:* `a: <valor de m>; b: sim (ou nao)`.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `C02` (`Eliminação de Gauss e Substituição Regressiva`):** somente após autocorreção de `C01-E01..E05` **e** **100% (3/3)** na Checagem Independente `C01-C01..C03`.
- **Recuperação direcionada (1ª falha):** revise se algum termo independente deixou de ser transformado pelas operações $L$, se alguma variável foi lida fora da ordem $(x, y, z)$ ou se $0$ foi omitido na matriz ampliada; aplique a variante `V2` de `C01`.
- **Após 2 tentativas malsucedidas:** recuar no DAG para **`A04`** *(escrita de $AX=B$)* ou **`B04`** *(aplicação controlada de $L_{ij}$, $L_i(\alpha)$ e $L_j' = L_j + L_i(\alpha)$ sem erros de sinal)*.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Sistemas.pdf` p. 2–8 (`A.38`–`A.43`: equação linear, sistemas equivalentes e notação das operações elementares $L_{ij}$, $L_i(\alpha)$, $L_j' = L_j + L_i(\alpha)$).
- `[DOC]` `Matrizes_Vetores_P2.pdf` p. 49–53 (construção da matriz ampliada e primeiras reduções equivalentes).
- Gabarito comentado e casos de verificação: [C01_gabarito.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_C/gabaritos/C01_gabarito.md) e [casos_C01.json](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_C/testes/casos_C01.json).
