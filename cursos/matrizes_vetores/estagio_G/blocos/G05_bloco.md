# Bloco `G05` — Simulado Integrador P3 (Parte 2) — Cônicas e Quádricas

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio G — Integração Geral e Simulados por Avaliação / **`G05`** |
| **Micro-habilidade foco** | Integrar, no padrão P3 sem consulta, redução de equações de cônicas em $\mathbb{R}^2$ (parábola, elipse e hipérbole, **sem termo `xy`**) por completamento de quadrados, determinação de vértices, focos, diretriz e excentricidade, ajuste de parábola por 3 pontos e classificação de quádricas canônicas por traços coordenados (`[INF/AUS]`). |
| **Pré-requisitos** | `F08` *(Revisão cumulativa do Estágio F)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`G05-E01`–`G05-E05`, 25 min):** `16 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`G05-C01`–`G05-C03`, 18 min):** `14 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Simulado P3 (Parte 2) sem consulta.** **Proibido:** rotação de cônicas ou quádricas com eliminação de termo misto $xy$, diagonalização ou autovalores. Mantenha todas as coordenadas, excentricidades e equações em frações e radicais exatos. |

### Registro da Sessão (Preenchido na Prática)
- **Protocolo:** `PREP-MV-G05-<VARIANTE>-T<TENTATIVA>-<HASH>`
- **Sessão única (`G05-E01`–`G05-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`G05-C01`–`G05-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Relações Fundamentais das Cônicas (sem `xy`):**
   - **Parábola:** $(y - k)^2 = 2p(x - h)$ *(eixo horizontal)* ou $(x - h)^2 = 2p(y - k)$ *(eixo vertical)*; distância foco-vértice $= |p|/2$.
   - **Elipse:** $\frac{(x-h)^2}{a^2} + \frac{(y-k)^2}{b^2} = 1$ (ou com $a^2$ sob $y$); $a > b$, **$a^2 = b^2 + c^2$**, excentricidade $e = \frac{c}{a} < 1$.
   - **Hipérbole:** **o sinal positivo define o eixo real ($a^2$)**; **$c^2 = a^2 + b^2$**, excentricidade $e = \frac{c}{a} > 1$. Se após completar quadrados o lado direito for negativo, divida tudo por ele e **inverta a ordem dos sinais**.
2. **Superfícies Quádricas Canônicas por Traços `[INF/AUS]`:**
   - **Elipsoide:** $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$ *(todos positivos; traços são elipses)*.
   - **Hiperboloide de uma folha:** dois quadrados positivos, um negativo $= 1$ *(traços paralelos a um plano coordenado são elipses; nos outros dois, hipérboles)*.
   - **Hiperboloide de duas folhas:** um quadrado positivo, dois negativos $= 1$ *(seções perpendiculares ao eixo principal existem apenas para $|var| \ge a$)*.
   - **Paraboloide elíptico:** $z = \frac{x^2}{a^2} + \frac{y^2}{b^2}$ *(elipses + parábolas)*.
   - **Paraboloide hiperbólico:** $z = \frac{x^2}{a^2} - \frac{y^2}{b^2}$ *(hipérboles + parábolas opostas — sela)*.
   - **Cone elíptico:** $z^2 = \frac{x^2}{a^2} + \frac{y^2}{b^2}$ *(igualado a zero passando todos ao mesmo lado)*.
   - **Cilindro elíptico:** ausência de uma das variáveis (ex.: $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ no $\mathbb{R}^3$).

---

## 2. Exemplos Guiados

### Exemplo 1 — Armadilha do Sinal Negativo no Lado Direito
Ao completar quadrados em $9x^2 - 4y^2 - 54x + 8y + 113 = 0$, obtém-se $9(x-3)^2 - 4(y-1)^2 = -36$. Dividindo por $-36$ (e não por $+36$!), os sinais se invertem:
$$\frac{(y-1)^2}{9} - \frac{(x-3)^2}{4} = 1,$$
revelando eixo real paralelo ao eixo **$y$** ($a = 3$, $b = 2$), e não paralelo a $x$.

---

## 3. Exercícios (`G05-E01` a `G05-E05`)

### `G05-E01` *(Parábola transladada por completamento de quadrados)*
Considere a parábola de equação $y^2 - 6y - 8x + 17 = 0$. Complete os quadrados e determine:  
**(a)** As coordenadas do vértice $V(h, k)$  
**(b)** As coordenadas do foco $F$  
**(c)** A equação da reta diretriz

*Formato de resposta:* `(a) (h, k) (b) (xf, yf) (c) x = ...` (ou `x + 1 = 0`).

---

### `G05-E02` *(Elipse transladada — centro, excentricidade e focos)*
Complete os quadrados na equação $9x^2 + 25y^2 - 36x + 150y + 36 = 0$ e determine:  
**(a)** As coordenadas do centro $C(h, k)$  
**(b)** A excentricidade $e$ (fração irredutível)  
**(c)** Os dois focos $F_1$ e $F_2$

*Formato de resposta:* `(a) (h, k) (b) e (c) [(x1, y1), (x2, y2)]`.

---

### `G05-E03` *(Hipérbole transladada com lado direito negativo)*
Reduza a equação $9x^2 - 4y^2 - 54x + 8y + 113 = 0$ à forma canônica e informe:  
**(a)** A equação reduzida da hipérbole  
**(b)** Os dois vértices reais $A_1$ e $A_2$  
**(c)** A excentricidade exata $e$

*Formato de resposta:* `(a) (y-1)^2/... - (x-3)^2/... = 1 (b) [(x1, y1), (x2, y2)] (c) valor_exato`.

---

### `G05-E04` *(Classificação de superfícies quádricas por sinais e traços `[INF/AUS]`)*
Classifique cada superfície quádrica no $\mathbb{R}^3$ segundo sua equação canônica e seus traços nos planos coordenados:  
**(a)** $\dfrac{x^2}{4} + \dfrac{y^2}{9} - \dfrac{z^2}{16} = 1$  
**(b)** $\dfrac{x^2}{9} - \dfrac{y^2}{4} - \dfrac{z^2}{16} = 1$  
**(c)** $z = \dfrac{x^2}{4} - \dfrac{y^2}{9}$

*Formato de resposta:* `(a) nome_quadrica (b) nome_quadrica (c) nome_quadrica`.

---

### `G05-E05` *(Quádricas mistas e parábola por 3 pontos)*
**(a)** Classifique a superfície $x^2 + 4y^2 + 9z^2 = 36$.  
**(b)** Classifique a superfície $z^2 = \dfrac{x^2}{4} + \dfrac{y^2}{9}$.  
**(c)** Determine a equação da parábola de eixo paralelo ao eixo $y$ ($y = ax^2 + bx + c$) que passa pelos pontos $(0, 1)$, $(1, 0)$ e $(2, 3)$.

*Formato de resposta:* `(a) nome_quadrica (b) nome_quadrica (c) y = ...`.

---

## 4. Checagem Independente (`G05-C01` a `G05-C03`)
*(Simulado P3 Parte 2 sem consulta. Critério de aprovação: **100% — 3/3**.)*

### `G05-C01` *(Elipse transladada sem consulta)*
Para a cônica $4x^2 + y^2 + 16x - 6y + 9 = 0$, complete os quadrados e determine:  
**(a)** O centro $C(h, k)$  
**(b)** A excentricidade exata $e$

*Formato de resposta:* `(a) (h, k) (b) valor_exato`.

---

### `G05-C02` *(Hipérbole transladada com inversão de sinal sem consulta)*
Reduza a equação $4x^2 - 9y^2 - 8x + 36y + 4 = 0$ à forma padrão e informe:  
**(a)** A equação reduzida da hipérbole  
**(b)** A excentricidade exata $e$

*Formato de resposta:* `(a) (y-...)^2/... - (x-...)^2/... = 1 (b) valor_exato`.

---

### `G05-C03` *(Classificação de quádricas por traços `[INF/AUS]` sem consulta)*
Classifique as três superfícies no $\mathbb{R}^3$:  
**(a)** $z = \dfrac{x^2}{9} + \dfrac{y^2}{4}$  
**(b)** $\dfrac{x^2}{4} + \dfrac{y^2}{9} = 1$  
**(c)** $x^2 - y^2 - z^2 = 1$

*Formato de resposta:* `(a) nome_quadrica (b) nome_quadrica (c) nome_quadrica`.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `G06` (`Simulado Geral Completo MAT121 — Preparação Reavaliação`):** somente após autocorreção de `G05-E01`–`G05-E05` e **100% (3/3)** na Checagem Independente `G05-C01`–`G05-C03`.
- **Recuperação direcionada (1ª falha):** identifique a falha (parábola/3 pontos → `F01`/`F02`; relação $a^2=b^2+c^2$ na elipse → `F03`/`F04`; relação $c^2=a^2+b^2$ e divisão por constante negativa na hipérbole → `F05`/`F06`; traços de quádricas → `F07`) e aplique a variante `V2` de `G05`.
- **Após 2 tentativas malsucedidas:** recuar no DAG para **`F08`** (ou diretamente ao bloco específico **`F02`**, **`F04`**, **`F06`** ou **`F07`**).

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_RE42B_Planejamento.pdf` (Semanas 13–15 — *Estudo de cônicas e quádricas*).
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 165–184 (Cap. 7 — Seções Cônicas); `Mat_Vet_L11.pdf` Ex. 1–15.
- `[INF/AUS]` Quádricas canônicas por traços conforme `F07` (lacuna documentada em `00_inventario_fontes.md`).
- Gabarito comentado e casos de teste: [G05_gabarito.md](../gabaritos/G05_gabarito.md) e [casos_G05.json](../testes/casos_G05.json).
