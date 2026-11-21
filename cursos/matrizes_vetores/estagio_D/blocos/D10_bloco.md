# Bloco `D10` — Revisão Cumulativa do Estágio D (Simulado P2)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio D — Vetores em $\mathbb{R}^2/\mathbb{R}^3$, Produtos, Áreas e Volumes / **`D10`** |
| **Micro-habilidade foco** | Integrar combinação linear por escalonamento, 3 soluções do paralelogramo, colinearidade, produto escalar, ângulo interno, projeção ortogonal, produto vetorial, áreas ($\frac{1}{2}$) e volumes ($\frac{1}{6}$ e $|\det|=V$) no padrão de avaliação P2. |
| **Pré-requisitos** | `D06` *(Projeção ortogonal)*; `D08` *(Áreas)*; `D09` *(Produto misto e volumes)*; `C08` *(Revisão de escalonamento e sistemas)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Prática (`D10-E01`–`D10-E06`, 25 min):** `16 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`D10-C01`–`D10-C03`, 18 min):** `14 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Simulado cumulativo sem consulta do Estágio D.** Sistemas por escalonamento, determinantes $3\times 3$ pela 1ª linha (matriz $+ - +$) e respostas exatas com frações irredutíveis e radicais simplificados. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`D10-E01`–`D10-E06`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Protocolo:** `PREP-MV-D10-V__-T__` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 6` | **Após autocorreção:** `___ / 6`
- **Checagem independente (sem gabarito) (`D10-C01`–`D10-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas (Checklist Rápido do Estágio D)

1. **Pontos e paralelogramo:** $\overrightarrow{AB} = B - A$; 3 possíveis vértices $S$ para $P, Q, R$ são $P+Q-R$, $P+R-Q$, $Q+R-P$.
2. **Combinação linear e colinearidade:** sistema resolvido por **escalonamento**; 3 pontos colineares $\iff \overrightarrow{AC} = k\,\overrightarrow{AB}$.
3. **Escalar, ângulo e projeção:**
   $$\cos\theta = \frac{\vec{u}\cdot\vec{v}}{|\vec{u}|\,|\vec{v}|} \quad (\text{vértice comum em triângulos!}), \qquad \operatorname{proj}_{\vec{v}}\vec{u} = \left(\frac{\vec{u}\cdot\vec{v}}{|\vec{v}|^2}\right)\vec{v}, \qquad \cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1.$$
4. **Vetorial e Áreas:** desenvolvimento pela 1ª linha com sinais $+ - +$; $A_{\text{paral}} = |\vec{u}\times\vec{v}|$ e $A_{\triangle} = \frac{1}{2}|\overrightarrow{AB}\times\overrightarrow{AC}|$.
5. **Produto misto, Coplanaridade e Volumes:** $(\vec{u},\vec{v},\vec{w}) = 0 \iff$ coplanares; $V_{\text{paral}} = |(\vec{u},\vec{v},\vec{w})|$; $V_{\text{tetra}} = \frac{1}{6}|(\overrightarrow{AB},\overrightarrow{AC},\overrightarrow{AD})|$; equações $|E(m)| = V$ sempre geram **2 equações** ($E(m) = \pm V$).

---

## 2. Exemplos Guiados

### Exemplo 1 — Síntese métrica: versor, produto escalar e projeção
Dados $A(1, 1, 0)$, $B(2, 3, 2)$ e $C(3, 1, 2)$:
1. $\overrightarrow{AB} = (1, 2, 2)$ tem $|\overrightarrow{AB}| = 3$, logo $\widehat{AB} = \left(\frac{1}{3}, \frac{2}{3}, \frac{2}{3}\right)$.
2. $\overrightarrow{AC} = (2, 0, 2)$ tem $\overrightarrow{AB}\cdot\overrightarrow{AC} = 1(2) + 2(0) + 2(2) = 6$.
3. $\operatorname{proj}_{\overrightarrow{AB}}\overrightarrow{AC} = \frac{6}{3^2}(1, 2, 2) = \frac{2}{3}(1, 2, 2) = \mathbf{\left(\frac{2}{3},\, \frac{4}{3},\, \frac{4}{3}\right)}$.

### Exemplo 2 — Síntese espacial: paralelepípedo com parâmetro ($|\det| = V$)
Para que $\vec{a} = (1, 0, 2)$, $\vec{b} = (2, 1, 0)$ e $\vec{c} = (0, k, 1)$ determinem um paralelepípedo de volume $10$:
$$(\vec{a},\vec{b},\vec{c}) = \begin{vmatrix} 1 & 0 & 2 \\ 2 & 1 & 0 \\ 0 & k & 1 \end{vmatrix} = 1(1 - 0) - 0 + 2(2k - 0) = 4k + 1.$$
$$|4k + 1| = 10 \implies 4k + 1 = 10 \text{ ou } 4k + 1 = -10 \implies \mathbf{k = \frac{9}{4} \text{ ou } k = -\frac{11}{4}}.$$

---

## 3. Exercícios (`D10-E01` a `D10-E06`)

### `D10-E01` *(Combinação linear via escalonamento e colinearidade)*
**(a)** Determine o par $(c_1, c_2)$ tal que $(1, -8, 11) = c_1(1, -2, 3) + c_2(1, 1, -1)$ escalonando a matriz ampliada.  
**(b)** Determine o par $(a, b)$ de modo que os pontos $A(1, 2, -1)$, $B(3, 0, 2)$ e $C(a, b, 5)$ sejam colineares.

---

### `D10-E02` *(3 vértices do paralelogramo e versor)*
Dados os pontos $P(1, 0, -1)$, $Q(3, 1, 1)$ e $R(-1, 2, 2)$, determine:  
**(a)** O conjunto dos **3 possíveis pontos $S$** que formam um paralelogramo com $P, Q, R$  
**(b)** O versor $\widehat{PQ}$

---

### `D10-E03` *(Ângulo interno em triângulo e projeção ortogonal)*
Dados os vértices $A(1, 1, 1)$, $B(3, 1, 3)$ e $C(3, 3, 1)$, calcule:  
**(a)** O ângulo interno $\hat{A}$ do triângulo $ABC$ (em graus)  
**(b)** O vetor projeção $\operatorname{proj}_{\overrightarrow{AB}}\overrightarrow{AC}$

---

### `D10-E04` *(Produto vetorial e área do triângulo)*
Para os pontos $A(0, 1, 2)$, $B(2, -1, 3)$ e $C(1, 2, 0)$, determine:  
**(a)** O produto vetorial $\overrightarrow{AB}\times\overrightarrow{AC}$  
**(b)** A área exata do triângulo $ABC$

---

### `D10-E05` *(Volume do tetraedro e coplanaridade de 4 pontos)*
Dados $A(1, -1, 0)$, $B(2, 1, 1)$, $C(0, 2, -1)$ e $D(3, 0, 4)$, determine:  
**(a)** O volume exato do tetraedro $ABCD$  
**(b)** Se os quatro pontos são coplanares (`Sao coplanares` ou `Nao sao coplanares`)

---

### `D10-E06` *(Volume do paralelepípedo com parâmetro — 2 soluções)*
Determine todos os valores reais de $m$ para que os vetores $\vec{u} = (1, 2, -1)$, $\vec{v} = (2, -1, 1)$ e $\vec{w} = (m, 1, m - 2)$ determinem um paralelepípedo de volume igual a $15$.

---

## 4. Checagem Independente de Domínio *(Simulado P2 sem Consulta — Exige 100%)*

### `D10-C01` *(Ângulo interno e área do triângulo)*
Dados os pontos $A(2, 0, -1)$, $B(4, 2, -1)$ e $C(4, 0, 1)$, determine:  
**(a)** O ângulo interno do triângulo $ABC$ no vértice $A$ (em graus)  
**(b)** A área exata do triângulo $ABC$

### `D10-C02` *(Decomposição ortogonal)*
Dados $\vec{u} = (2, -1, 2)$ e $\vec{v} = (1, 3, -1)$, determine:  
**(a)** $\operatorname{proj}_{\vec{u}}\vec{v}$  
**(b)** A componente ortogonal $\vec{v}_{\perp} = \vec{v} - \operatorname{proj}_{\vec{u}}\vec{v}$

### `D10-C03` *(Volume do tetraedro com parâmetro — 2 soluções)*
Determine todos os valores reais de $t$ para que o tetraedro de vértices $A(1, 0, 1)$, $B(2, 2, 1)$, $C(1, 1, 3)$ e $D(t, 1, 2)$ tenha volume igual a $\frac{2}{3}$.

---

## 5. Orientação de Avanço ou Recuperação

- **Estágio D concluído (avançar para `E01` — `Equações da Reta no R^3`):** somente após **100% (3/3)** na Checagem Independente `D10-C01..C03` sem consulta.
- **Recuperação direcionada (1ª falha):** identificar o bloco específico da falha na checagem (`D10-C01` → `D05`/`D08`; `D10-C02` → `D06`; `D10-C03` → `D09`), revisar o tópico pontual e aplicar a variante `V2` de `D10`.
- **Após 2 tentativas malsucedidas:** parar a repetição de `D10` e recuar diretamente ao bloco de origem da falha no DAG (`D06`, `D08`, `D09` ou `C08`).

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Vetores.pdf` p. 1–75 (síntese integral de vetores no $\mathbb{R}^2/\mathbb{R}^3$, produtos escalar, vetorial e misto, áreas e volumes).
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 78–123 (Capítulos 1 a 3 do caderno manuscrito).
- `[DOC]` `Mat_Vet_L6.pdf` e `Mat_Vet_L7.pdf` (42 exercícios completos das Listas 6 e 7).
- Gabarito e especificação de validação: [D10_gabarito.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/gabaritos/D10_gabarito.md) e [casos_D10.json](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/testes/casos_D10.json).
