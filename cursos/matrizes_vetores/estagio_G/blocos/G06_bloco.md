# Bloco `G06` — Simulado Geral Completo `MAT121` (Preparação Reavaliação)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio G — Integração Geral e Simulados por Avaliação / **`G06`** |
| **Micro-habilidade foco** | Sintetizar, em simulado integral sem consulta no padrão da Reavaliação de `MAT121`, todos os 6 estágios da disciplina: determinantes por cofatores/triangulação, inversão `[A \| I]` e equações matriciais; sistemas lineares com parâmetros; vetores, áreas ($\frac{1}{2}$) e volumes ($\frac{1}{6}$); planos, retas e distâncias no $\mathbb{R}^3$; cônicas transladadas (sem `xy`) e quádricas canônicas (`[INF/AUS]`). |
| **Pré-requisitos** | `G01`, `G02`, `G03`, `G04`, `G05` *(Todos os simulados integradores P1–P3)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`G06-E01`–`G06-E05`, 25 min):** `16 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`G06-C01`–`G06-C03`, 18 min):** `14 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Simulado Geral Final sem consulta e sem calculadora.** **Proibido:** Sarrus, Chió, Vandermonde, matriz adjunta, Regra de Cramer, autovalores/autovetores, Gram-Schmidt e rotação de cônicas com termo $xy$. Expresse todos os resultados em frações irredutíveis e radicais exatos. |

### Registro da Sessão (Preenchido na Prática)
- **Protocolo:** `PREP-MV-G06-<VARIANTE>-T<TENTATIVA>-<HASH>`
- **Sessão única (`G06-E01`–`G06-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`G06-C01`–`G06-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Roteiro de Decisão Rápida na Prova Geral (`MAT121`):**
   - **P1 (Matrizes e Determinantes):** use desenvolvimento por linha/coluna mais esparsa ou triangulação por operações $L$; para $A^{-1}$, aplique $[A \mid I_n] \to [I_n \mid A^{-1}]$; em $AX^T = B$, isole $X^T = A^{-1}B$ e transponha no fim.
   - **P2 (Sistemas e Vetores):** classifique com $C_A, C_V$ e $g = n - C$; em sistemas homogêneos quadrados, solução própria $\iff \det(A) = 0$; em geometria vetorial, área de triângulo leva $\frac{1}{2}$ e volume de tetraedro leva $\frac{1}{6}$.
   - **P3 (Retas, Planos, Cônicas e Quádricas):** plano paralelo preserva $\vec{n} = (a,b,c)$ e ajusta $d$; distância entre planos paralelos exige igualar $(a,b,c)$ antes de $|d_1 - d_2|$; cônicas sem $xy$ reduzem por completamento de quadrados; quádricas classificam-se por sinais e traços coordenados.

---

## 2. Exemplos Guiados

### Exemplo 1 — Ponte Completa Entre Estágios (P1 $\leftrightarrow$ P2 $\leftrightarrow$ P3)
Em uma prova de Reavaliação, o mesmo mecanismo de escalonamento $[A \mid I_3]$ resolve $AX = B$ (via $X = A^{-1}B$), o produto vetorial $\overrightarrow{AB}\times\overrightarrow{AC}$ fornece tanto a área do triângulo $\frac{1}{2}|\vec{n}|$ quanto o vetor normal do plano $ax+by+cz+d=0$, e a comparação de sinais nos quadrados identifica imediatamente elipses, hipérboles e superfícies quádricas.

---

## 3. Exercícios (`G06-E01` a `G06-E05`)

### `G06-E01` *(P1 — Singularidade por cofatores e equação matricial `AX^T = B`)*
**(a)** Desenvolvendo pela linha ou coluna mais favorável (sem Sarrus), determine **todos** os valores reais de $k$ que tornam singular a matriz:
$$M = \begin{bmatrix} k & 0 & 1 \\ 2 & k - 1 & 3 \\ 4 & 0 & k \end{bmatrix}$$
**(b)** Dadas $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ e $B = \begin{bmatrix} 2 & 0 \\ -1 & 4 \end{bmatrix}$, calcule $A^{-1}$ via `[A | I_2]` e determine a matriz $X$ tal que $A X^T = B$.

*Formato de resposta:* `(a) k1, k2, k3 (b) [[...], [...]]`.

---

### `G06-E02` *(P2 Parte 1 — Homogêneo com parâmetro e sistema escalonado)*
**(a)** Determine o valor real de $k$ para que o sistema homogêneo $\begin{cases} x + y + 2z = 0 \\ 2x + 3y + 5z = 0 \\ x + 2y + kz = 0 \end{cases}$ admita soluções próprias (não-triviais).  
**(b)** Escalone o sistema $\begin{cases} x + y - z = 1 \\ 2x + 3y + z = 7 \\ x + y + z = 5 \end{cases}$ e informe $C_A$, $C_V$, $g$, a classificação (`SPD`, `SPI` ou `SI`) e a solução $(x, y, z)$.

*Formato de resposta:* `(a) valor_k (b) ca: <int>; cv: <int>; g: <int>; classificacao: <SPD/SPI/SI>; solucao: (x, y, z)`.

---

### `G06-E03` *(P2 Parte 2 — Área do triângulo `1/2` e volume do tetraedro `1/6`)*
Considere os pontos $A(1, 0, 1)$, $B(3, 2, 1)$, $C(1, 2, 3)$ e $D(2, 1, 4)$:  
**(a)** Calcule a área exata do triângulo $ABC$.  
**(b)** Calcule o volume exato do tetraedro $ABCD$.

*Formato de resposta:* `(a) valor_exato (b) valor`.

---

### `G06-E04` *(P3 Parte 1 — Plano paralelo e distância entre planos paralelos)*
Considere o ponto $P(1, -1, 2)$ e o plano $\alpha: 2x - y + 2z - 5 = 0$:  
**(a)** Determine a equação geral do plano $\pi$ que passa por $P$ e é paralelo a $\alpha$.  
**(b)** Calcule a distância exata entre os planos $\pi$ e $\alpha$.

*Formato de resposta:* `(a) ax + by + cz + d = 0 (b) fracao`.

---

### `G06-E05` *(P3 Parte 2 — Cônica transladada e quádrica canônica `[INF/AUS]`)*
**(a)** Complete os quadrados da equação $x^2 + 4y^2 - 6x + 16y + 21 = 0$ e escreva sua equação reduzida.  
**(b)** Classifique a superfície quádrica $\dfrac{x^2}{4} - \dfrac{y^2}{9} + \dfrac{z^2}{16} = 1$.

*Formato de resposta:* `(a) (x-...)^2/... + (y+...)^2/... = 1 (b) nome_quadrica`.

---

## 4. Checagem Independente (`G06-C01` a `G06-C03`)
*(Simulado Final sem consulta e sem calculadora. Critério de aprovação: **100% — 3/3**.)*

### `G06-C01` *(Integração P1 + P2 — Inversa `[A | I_3]` aplicada a `AX = B`)*
Considere $A = \begin{bmatrix} 1 & 0 & 2 \\ 0 & 1 & 1 \\ 1 & 1 & 4 \end{bmatrix}$ e $B = \begin{bmatrix} 5 \\ 2 \\ 9 \end{bmatrix}$.  
**(a)** Calcule $A^{-1}$ exclusivamente pelo método `[A | I_3] -> [I_3 | A^{-1}]`.  
**(b)** Usando $X = A^{-1}B$ (proibido Cramer), informe a solução $(x, y, z)$.

*Formato de resposta:* `(a) [[...], [...], [...]] (b) (x, y, z)`.

---

### `G06-C02` *(Integração P2 + P3 Parte 1 — Plano por 3 pontos e distância ponto-plano)*
Dados os pontos $A(1, 1, 0)$, $B(3, 1, 2)$, $C(1, 3, 2)$ e $P(4, 2, 3)$:  
**(a)** Determine a equação geral do plano $\pi$ que passa por $A$, $B$ e $C$.  
**(b)** Calcule a distância exata do ponto $P$ ao plano $\pi$.

*Formato de resposta:* `(a) ax + by + cz + d = 0 (b) valor_exato`.

---

### `G06-C03` *(Integração P3 Parte 2 — Cônica por completamento de quadrados e quádrica)*
**(a)** Complete os quadrados em $4y^2 - x^2 - 8y - 4x - 4 = 0$ e informe o centro $(h, k)$ da cônica.  
**(b)** Classifique a cônica obtida no item (a) (`elipse`, `hiperbole` ou `parabola`).  
**(c)** Classifique a superfície quádrica $y = \dfrac{x^2}{4} - \dfrac{z^2}{9}$ (`[INF/AUS]`).

*Formato de resposta:* `(a) (h, k) (b) classificacao (c) nome_quadrica`.

---

## 5. Orientação de Avanço ou Recuperação

- **Conclusão integral do curso `MAT121`:** atingida com autocorreção de `G06-E01`–`G06-E05` e **100% (3/3)** na Checagem Independente `G06-C01`–`G06-C03` sem consulta.
- **Recuperação direcionada (1ª falha):** identifique exatamente em qual frente ocorreu o erro e retome o simulado correspondente: P1 → **`G01`**, Sistemas → **`G02`**, Vetores/Produtos → **`G03`**, Retas/Planos/Distâncias → **`G04`**, Cônicas/Quádricas → **`G05`**, aplicando a variante `V2` de `G06`.
- **Após 2 tentativas malsucedidas:** recuar no DAG para o bloco simulador da avaliação correspondente (**`G01`**, **`G02`**, **`G03`**, **`G04`** ou **`G05`**) antes de nova tentativa em `G06`.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_RE42B_Planejamento.pdf` (Semanas 1–16 — Ementa integral e Reavaliação).
- `[DOC]` Todas as apostilas (`MAT121_Matrizes.pdf`, `MAT121_Sistemas.pdf`, `MAT121_Vetores.pdf`, `MAT121_Parte_4.pdf`), caderno manuscrito (`P1`–`P3`) e listas oficiais (`L1`–`L11`).
- Gabarito comentado e casos de teste: [G06_gabarito.md](../gabaritos/G06_gabarito.md) e [casos_G06.json](../testes/casos_G06.json).
