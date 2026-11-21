# Bloco `D08` — Áreas via Produto Vetorial (Paralelogramo e Triângulo)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio D — Vetores em $\mathbb{R}^2/\mathbb{R}^3$, Produtos, Áreas e Volumes / **`D08`** |
| **Micro-habilidade foco** | Calcular áreas de paralelogramos ($|\vec{u}\times\vec{v}|$) e de triângulos ($\frac{1}{2}|\overrightarrow{AB}\times\overrightarrow{AC}|$), determinar alturas relativas à base, e resolver equações de área com parâmetros mantendo radicais e frações exatas. |
| **Pré-requisitos** | `D07` *(Produto vetorial $\vec{u}\times\vec{v}$ por desenvolvimento na 1ª linha)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Prática (`D08-E01`–`D08-E06`, 20 min):** `13 min` resol. \| `4 min` corr. \| `3 min` recup.; **Checagem (`D08-C01`–`D08-C03`, 14 min):** `10 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Áreas de polígonos via produto vetorial no $\mathbb{R}^3$.** Utilize desenvolvimento pela 1ª linha para $\vec{u}\times\vec{v}$ e expresse toda raiz quadrada não exata simplificada na forma exata (`5*sqrt(2)/2`, `sqrt(83)`). |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`D08-E01`–`D08-E06`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Protocolo:** `PREP-MV-D08-V__-T__` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 6` | **Após autocorreção:** `___ / 6`
- **Checagem independente (sem gabarito) (`D08-C01`–`D08-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Área do paralelogramo:** o módulo $|\vec{u}\times\vec{v}| = |\vec{u}|\,|\vec{v}|\sin\theta$ é numericamente igual à área do paralelogramo determinado pelos vetores adjacentes $\vec{u}$ e $\vec{v}$:
   $$A_{\text{paral}} = |\vec{u}\times\vec{v}|.$$
   Se o paralelogramo for dado pelos vértices consecutivos $A, B, C, D$, tome dois lados adjacentes partindo do mesmo vértice: $A_{\text{paral}} = |\overrightarrow{AB}\times\overrightarrow{AD}|$.
2. **Área do triângulo ($\frac{1}{2}$!):** um triângulo $ABC$ tem exatamente a **metade** da área do paralelogramo formado pelos vetores $\overrightarrow{AB}$ e $\overrightarrow{AC}$ partindo de um vértice comum:
   $$A_{\triangle ABC} = \frac{1}{2}\left|\overrightarrow{AB}\times\overrightarrow{AC}\right|.$$
   **Armadilha clássica:** nunca esqueça o fator $\frac{1}{2}$ na área do triângulo!
3. **Altura relativa a uma base:** sabendo que $A_{\text{paral}} = \text{base} \times \text{altura}$, a altura do paralelogramo (ou do triângulo) em relação ao lado $AB$ é:
   $$h = \frac{|\overrightarrow{AB}\times\overrightarrow{AC}|}{|\overrightarrow{AB}|} = \frac{2\,A_{\triangle ABC}}{|\overrightarrow{AB}|}.$$

---

## 2. Exemplos Guiados

### Exemplo 1 — Área do paralelogramo e altura relativa à base
Determine a área do paralelogramo gerado por $\vec{u} = (2, 1, -1)$ e $\vec{v} = (1, -1, 2)$, e a altura relativa à base $\vec{u}$:
1. $\vec{u}\times\vec{v} = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ 2 & 1 & -1 \\ 1 & -1 & 2 \end{vmatrix} = (2-1)\hat{\imath} - (4+1)\hat{\jmath} + (-2-1)\hat{k} = (1, -5, -3)$.
2. $A_{\text{paral}} = |\vec{u}\times\vec{v}| = \sqrt{1^2 + (-5)^2 + (-3)^2} = \mathbf{\sqrt{35}}$.
3. Como $|\vec{u}| = \sqrt{4 + 1 + 1} = \sqrt{6}$, a altura sobre $\vec{u}$ é $h = \frac{\sqrt{35}}{\sqrt{6}} = \mathbf{\frac{\sqrt{210}}{6}}$.

### Exemplo 2 — Área do triângulo por 3 vértices
Calcule a área do triângulo de vértices $A(0, 1, 1)$, $B(2, 1, 2)$ e $C(1, 3, 1)$:
1. Vetores saindo de $A$: $\overrightarrow{AB} = (2, 0, 1)$ e $\overrightarrow{AC} = (1, 2, 0)$.
2. $\overrightarrow{AB}\times\overrightarrow{AC} = (0-2)\hat{\imath} - (0-1)\hat{\jmath} + (4-0)\hat{k} = (-2, 1, 4)$.
3. $A_{\triangle} = \frac{1}{2}|(-2, 1, 4)| = \frac{1}{2}\sqrt{4 + 1 + 16} = \mathbf{\frac{\sqrt{21}}{2}}$.

---

## 3. Exercícios (`D08-E01` a `D08-E06`)

### `D08-E01` *(Reprodução do modelo — Área do paralelogramo)*
Calcule a área exata do paralelogramo definido pelos vetores $\vec{u} = (2, -1, 3)$ e $\vec{v} = (1, 2, -1)$.

---

### `D08-E02` *(Técnica central — Área do triângulo $ABC$)*
Calcule a área exata do triângulo de vértices $A(1, 0, 2)$, $B(3, 1, 0)$ e $C(0, 2, 1)$.

---

### `D08-E03` *(Caça ao Erro — Esquecimento do fator $\frac{1}{2}$)*
Um estudante calculou $|\overrightarrow{AB}\times\overrightarrow{AC}|$ para os pontos $A(0, 1, 1)$, $B(2, 3, 2)$ e $C(1, 0, 3)$ e entregou esse valor diretamente como a área do triângulo $ABC$.  
Corrija o procedimento e informe os valores exatos de:  
**(a)** A área do triângulo $ABC$  
**(b)** A área do paralelogramo que tem $\overrightarrow{AB}$ e $\overrightarrow{AC}$ como lados adjacentes

---

### `D08-E04` *(Variação controlada com pistas — Área e altura sobre a base)*
Um paralelogramo $ABCD$ possui vértices consecutivos $A(1, 1, 0)$, $B(3, 2, 2)$ e $D(2, -1, 1)$. Determine os valores exatos de:  
**(a)** A área do paralelogramo $ABCD$  
**(b)** A altura do paralelogramo relativa à base $AB$

*Pistas:* Como $A, B, C, D$ estão em ordem consecutiva, os lados adjacentes que saem de $A$ são $\overrightarrow{AB}$ e $\overrightarrow{AD}$.

---

### `D08-E05` *(Variação controlada com pistas — Parâmetro para área de triângulo)*
Determine todos os valores reais de $m$ para que o triângulo de vértices $A(1, 0, 0)$, $B(3, 0, 0)$ e $C(0, m, 2)$ tenha área igual a $\frac{5}{2}$.

*Pistas:* Monte $\overrightarrow{AB}$ e $\overrightarrow{AC}$, calcule $\overrightarrow{AB}\times\overrightarrow{AC}$ em função de $m$ e resolva $\frac{1}{2}|\overrightarrow{AB}\times\overrightarrow{AC}| = \frac{5}{2}$. Atenção às duas raízes ($\pm$)!

---

### `D08-E06` *(Resolução independente — Área via propriedades do produto vetorial)*
Dois vetores $\vec{a}$ e $\vec{b}$ satisfazem $|\vec{a}| = 3$, $|\vec{b}| = 4$ e formam entre si um ângulo de $30^\circ$. Calcule a área exata do paralelogramo determinado pelos vetores $\vec{u} = 2\vec{a} + \vec{b}$ e $\vec{v} = \vec{a} - \vec{b}$.

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `D08-C01` *(Área do paralelogramo)*
Calcule a área exata do paralelogramo gerado pelos vetores $\vec{u} = (3, -2, 1)$ e $\vec{v} = (1, 1, -2)$.

### `D08-C02` *(Área do triângulo por vértices)*
Calcule a área exata do triângulo de vértices $P(2, -1, 1)$, $Q(4, 1, 0)$ e $R(1, 2, 3)$.

### `D08-C03` *(Parâmetro para área do paralelogramo)*
Determine todos os valores reais de $k$ para que a área do paralelogramo definido pelos vetores $\vec{u} = (1, k, 0)$ e $\vec{v} = (2, 0, 1)$ seja igual a $\sqrt{21}$.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `D09` (`Produto Misto, Coplanaridade e Volumes`):** somente após autocorreção de `D08-E01..E06` **e** **100% (3/3)** na Checagem Independente `D08-C01..C03` sem consulta.
- **Recuperação direcionada (1ª falha):** identificar se a falha foi omissão do $\frac{1}{2}$ no triângulo, erro de sinal no produto vetorial, erro na simplificação do radical ($\sqrt{75} = 5\sqrt{3}$), ou perda de raiz negativa em equação de área; revisar os Exemplos 1 e 2 e aplicar a variante `V2`.
- **Após 2 tentativas malsucedidas:** recuar ao pré-requisito **`D07`** para treinar cálculo seguro do produto vetorial e de seu módulo antes de retomar áreas.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Vetores.pdf` p. 69 (interpretação geométrica de $|\vec{u}\times\vec{v}|$ como área do paralelogramo).
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 119–120 (Cap. 3 — exemplos de área do paralelogramo e do triângulo).
- `[DOC]` `Mat_Vet_L7.pdf` p. 2 (Ex. 17 e Ex. 18 — área do paralelogramo por vetores e área do triângulo por 3 vértices).
- Gabarito e especificação de validação: [D08_gabarito.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/gabaritos/D08_gabarito.md) e [casos_D08.json](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/testes/casos_D08.json).
