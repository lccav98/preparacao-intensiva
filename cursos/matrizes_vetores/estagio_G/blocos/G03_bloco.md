# Bloco `G03` — Simulado Integrador P2 (Parte 2) — Vetores e Produtos

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio G — Integração Geral e Simulados por Avaliação / **`G03`** |
| **Micro-habilidade foco** | Integrar, no padrão P2 sem consulta, vetores em $\mathbb{R}^2/\mathbb{R}^3$, combinação linear via sistema escalonado, colinearidade, produto escalar, ângulo interno de triângulo, projeção ortogonal, produto vetorial ($\vec{u}\times\vec{v}$), área de triângulo ($\frac{1}{2}$), produto misto, coplanaridade de 4 pontos e volume de tetraedro ($\frac{1}{6}$) com parâmetro (2 raízes). |
| **Pré-requisitos** | `D10` *(Revisão cumulativa do Estágio D)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`G03-E01`–`G03-E05`, 25 min):** `16 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`G03-C01`–`G03-C03`, 18 min):** `14 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Simulado P2 (Parte 2) sem consulta.** **Proibido:** Processo de Gram-Schmidt, Regra de Sarrus, Regra de Cramer, autovalores/autovetores e espaços vetoriais abstratos. Desenvolva produtos vetoriais e mistos pela 1ª linha e expresse todos os resultados em frações irredutíveis e radicais exatos. |

### Registro da Sessão (Preenchido na Prática)
- **Protocolo:** `PREP-MV-G03-<VARIANTE>-T<TENTATIVA>-<HASH>`
- **Sessão única (`G03-E01`–`G03-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`G03-C01`–`G03-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Vetores por Dois Pontos e Combinação Linear (`D02`–`D03`):** $\overrightarrow{AB} = B - A$ (*extremidade menos origem*). Três pontos $A, B, C$ são colineares se e somente se $\overrightarrow{AB} \parallel \overrightarrow{AC}$ ($\overrightarrow{AC} = k\,\overrightarrow{AB}$).
2. **Ângulo Interno e Projeção (`D05`–`D06`):**
   - Para o ângulo interno no vértice $A$ do triângulo $ABC$, utilize **sempre os dois vetores saindo de $A$** ($\overrightarrow{AB}$ e $\overrightarrow{AC}$): $\cos\hat{A} = \frac{\overrightarrow{AB}\cdot\overrightarrow{AC}}{|\overrightarrow{AB}|\,|\overrightarrow{AC}|}$.
   - Projeção ortogonal: $\operatorname{proj}_{\vec{v}}\vec{u} = \left(\frac{\vec{u}\cdot\vec{v}}{|\vec{v}|^2}\right)\vec{v}$; parcela ortogonal: $\vec{u}_\perp = \vec{u} - \operatorname{proj}_{\vec{v}}\vec{u}$.
3. **Áreas e Volumes (`D08`–`D09`):**
   - **Área do triângulo $ABC$:** $A_{\triangle} = \frac{1}{2}\left|\overrightarrow{AB}\times\overrightarrow{AC}\right|$; altura relativa a $AB$: $h = \frac{|\overrightarrow{AB}\times\overrightarrow{AC}|}{|\overrightarrow{AB}|}$.
   - **Coplanaridade e Volume do Tetraedro:** $4$ pontos $A, B, C, D$ são coplanares se $(\overrightarrow{AB}, \overrightarrow{AC}, \overrightarrow{AD}) = 0$. Caso contrário, $V_{\text{tetra}} = \frac{1}{6}\left|(\overrightarrow{AB}, \overrightarrow{AC}, \overrightarrow{AD})\right|$. Em equações com parâmetro, o módulo gera **duas equações** ($\pm$).

---

## 2. Exemplos Guiados

### Exemplo 1 — Armadilha do Vértice Comum e do Módulo no Volume
- **Ângulo interno:** se um estudante usar $\overrightarrow{BA}$ e $\overrightarrow{AC}$ para o ângulo em $A$, obterá o **ângulo suplementar** ($180^\circ - \hat{A}$). Sempre posicione ambos os vetores com **origem no vértice** do ângulo pedido.
- **Parâmetro em volume:** $\frac{1}{6}|5k - 3| = 2 \iff |5k - 3| = 12 \iff 5k - 3 = 12$ **ou** $5k - 3 = -12$, produzindo **duas soluções reais**.

---

## 3. Exercícios (`G03-E01` a `G03-E05`)

### `G03-E01` *(Combinação linear e colinearidade de três pontos)*
**(a)** Escreva $\vec{w} = (5, -1, 7)$ como combinação linear $\vec{w} = a_1\vec{v}_1 + a_2\vec{v}_2 + a_3\vec{v}_3$, sendo $\vec{v}_1 = (1, 0, 1)$, $\vec{v}_2 = (0, 1, 1)$ e $\vec{v}_3 = (1, -1, 1)$, informando a terna $(a_1, a_2, a_3)$.  
**(b)** Determine o par $(m, n)$ para que os pontos $A(1, 2, -1)$, $B(3, 0, 1)$ e $C(5, m, n)$ sejam colineares.

*Formato de resposta:* `(a) (a1, a2, a3) (b) (m, n)`.

---

### `G03-E02` *(Ângulo interno de triângulo e projeção ortogonal)*
Considere o triângulo de vértices $A(1, 1, 0)$, $B(3, 1, 2)$ e $C(3, 3, 0)$:  
**(a)** Calcule a medida exata (em graus) do ângulo interno no vértice $A$.  
**(b)** Calcule o vetor projeção ortogonal $\operatorname{proj}_{\overrightarrow{AC}}\overrightarrow{AB}$.

*Formato de resposta:* `(a) valor_em_graus (b) (x, y, z)`.

---

### `G03-E03` *(Área do triângulo `1/2` e altura relativa à base)*
Para o triângulo de vértices $P(1, 0, 1)$, $Q(3, 2, 0)$ e $R(2, -1, 3)$:  
**(a)** Calcule a área exata do triângulo $PQR$.  
**(b)** Calcule a altura exata do triângulo relativa à base $PQ$.

*Formato de resposta:* `(a) valor_exato (b) valor_exato` (use radicais exatos, ex.: `5*sqrt(2)/2`).

---

### `G03-E04` *(Volume do tetraedro `1/6` e teste de coplanaridade de 4 pontos)*
Dados os pontos $A(1, 0, 1)$, $B(2, 1, 0)$, $C(0, 2, 1)$ e $D(3, 3, 2)$:  
**(a)** Calcule o volume exato do tetraedro $ABCD$ (fração irredutível).  
**(b)** Classifique os 4 pontos como `coplanares` ou `nao coplanares`.

*Formato de resposta:* `(a) fracao (b) classificacao`.

---

### `G03-E05` *(Parâmetro em volume de tetraedro — duas soluções)*
Determine **todos** os valores reais de $k$ para que o tetraedro de vértices $A(0, 0, 0)$, $B(2, 1, 0)$, $C(1, 3, 1)$ e $D(1, 2, k)$ tenha volume igual a $2$.

*Formato de resposta:* lista com todos os valores exatos (ex.: `k1, k2`).

---

## 4. Checagem Independente (`G03-C01` a `G03-C03`)
*(Simulado P2 Parte 2 sem consulta. Critério de aprovação: **100% — 3/3**.)*

### `G03-C01` *(Projeção ortogonal e parcela ortogonal)*
Dados $\vec{u} = (1, -2, 2)$ e $\vec{v} = (2, 1, -2)$:  
**(a)** Calcule $\operatorname{proj}_{\vec{u}}\vec{v}$.  
**(b)** Calcule a componente de $\vec{v}$ ortogonal a $\vec{u}$ ($\vec{v}_\perp = \vec{v} - \operatorname{proj}_{\vec{u}}\vec{v}$).

*Formato de resposta:* `(a) (x, y, z) (b) (x, y, z)` com frações irredutíveis.

---

### `G03-C02` *(Área de triângulo e versor ortogonal)*
Considere os pontos $A(0, 1, 2)$, $B(2, 1, 0)$ e $C(1, 3, 2)$:  
**(a)** Calcule a área exata do triângulo $ABC$.  
**(b)** Determine o versor (vetor unitário) do produto vetorial $\overrightarrow{AB} \times \overrightarrow{AC}$.

*Formato de resposta:* `(a) valor (b) (x, y, z)`.

---

### `G03-C03` *(Parâmetro em volume de tetraedro sem consulta)*
Determine **todos** os valores reais de $m$ para que o tetraedro gerado pelos vetores $\vec{u} = (1, 1, 0)$, $\vec{v} = (0, 2, 1)$ e $\vec{w} = (m, 1, 3)$ tenha volume igual a $\frac{5}{3}$.

*Formato de resposta:* lista com todos os valores exatos (ex.: `m1, m2`).

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `G04` (`Simulado Integrador P3 — Parte 1`):** somente após autocorreção de `G03-E01`–`G03-E05` e **100% (3/3)** na Checagem Independente `G03-C01`–`G03-C03`.
- **Recuperação direcionada (1ª falha):** identifique o erro específico (combinação linear/colinearidade → `D03`; ângulo interno/projeção → `D05`/`D06`; fator $\frac{1}{2}$ na área → `D08`; fator $\frac{1}{6}$ ou raiz negativa do módulo no volume → `D09`) e aplique a variante `V2` de `G03`.
- **Após 2 tentativas malsucedidas:** recuar no DAG para **`D10`** (ou diretamente para **`D06`**, **`D08`** ou **`D09`** conforme a falha).

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_RE42B_Planejamento.pdf` (Semanas 7–10 — 2ª metade da Avaliação P2).
- `[DOC]` `MAT121_Vetores.pdf` p. 1–75; `Matrizes_Vetores_P3.pdf` p. 78–123; `Mat_Vet_L6.pdf` e `Mat_Vet_L7.pdf`.
- Gabarito comentado e casos de teste: [G03_gabarito.md](../gabaritos/G03_gabarito.md) e [casos_G03.json](../testes/casos_G03.json).
