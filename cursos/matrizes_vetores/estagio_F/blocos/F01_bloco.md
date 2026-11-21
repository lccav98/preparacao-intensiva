# Bloco `F01` — Parábola na Origem ($x^2 = 2py$ e $y^2 = 2px$)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio F — Seções Cônicas ($\mathbb{R}^2$) e Superfícies Quádricas Canônicas / **`F01`** |
| **Micro-habilidade foco** | Identificar parâmetro $p$, vértice $V(0,0)$, foco $F$, reta diretriz, eixo de simetria e concavidade da parábola centrada na origem nas formas canônicas $x^2 = 2py$ e $y^2 = 2px$, além de deduzir sua equação a partir de elementos geométricos. |
| **Pré-requisitos** | `D04` *(Distância entre pontos e módulo analítico)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Prática (`F01-E01`–`F01-E06`, 18 min):** `11 min` resol. \| `4 min` corr. \| `3 min` recup.; **Checagem (`F01-C01`–`F01-C03`, 12 min):** `8 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Somente parábolas com vértice na origem $V(0,0)$ e eixo de simetria sobre $Ox$ ou $Oy$.** Translações ($V(h,k)$) ficam para `F02`. **Estritamente proibido** usar termo misto $Bxy$, matriz de rotação ou diagonalização por autovalores. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`F01-E01`–`F01-E06`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Protocolo:** `PREP-MV-F01-V__-T__` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 6` | **Após autocorreção:** `___ / 6`
- **Checagem independente (sem gabarito) (`F01-C01`–`F01-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Definição geométrica:** dados um ponto fixo $F$ (**foco**) e uma reta fixa $r$ (**diretriz**, com $F \notin r$), a parábola é o lugar geométrico dos pontos $P(x,y) \in \mathbb{R}^2$ tais que:
   $$d(P, F) = d(P, r).$$
2. **Convenção da disciplina (`x^2 = 2py` e `y^2 = 2px`):** o coeficiente da variável de $1^\circ$ grau na equação reduzida vale **$2p$** (e **não** $4p$!), onde $|p|$ é a distância entre o foco $F$ e a reta diretriz $r$, e $|p|/2$ é a distância do vértice $V(0,0)$ até $F$ e até $r$:
   - **Eixo de simetria $Oy$ (variável quadrática em $x$):**
     $$x^2 = 2py \qquad \Longrightarrow \qquad V(0,0),\quad F\!\left(0, \frac{p}{2}\right),\quad \text{diretriz } y = -\frac{p}{2}.$$
     - Se $p > 0$: concavidade voltada **para cima** ($y \ge 0$).
     - Se $p < 0$: concavidade voltada **para baixo** ($y \le 0$).
   - **Eixo de simetria $Ox$ (variável quadrática em $y$):**
     $$y^2 = 2px \qquad \Longrightarrow \qquad V(0,0),\quad F\!\left(\frac{p}{2}, 0\right),\quad \text{diretriz } x = -\frac{p}{2}.$$
     - Se $p > 0$: concavidade voltada **para a direita** ($x \ge 0$).
     - Se $p < 0$: concavidade voltada **para a esquerda** ($x \le 0$).
3. **Latus rectum (corda focal):** o segmento que passa pelo foco perpendicularmente ao eixo de simetria tem comprimento exato igual a **$|2p|$**.

---

## 2. Exemplos Guiados

### Exemplo 1 — Extrair parâmetro $p$, foco e diretriz de $x^2 = 12y$
1. A equação tem $x$ ao quadrado e $y$ linear $\Rightarrow$ eixo de simetria sobre $Oy$, formato $x^2 = 2py$.
2. Comparando os coeficientes: $2p = 12 \implies p = \mathbf{6} > 0$ (concavidade para cima).
3. Logo, $V(0,0)$, foco $F\!\left(0, \frac{6}{2}\right) = \mathbf{F(0, 3)}$ e reta diretriz $\mathbf{y = -3}$.

### Exemplo 2 — Equação reduzida a partir do foco $F\left(-\frac{5}{2}, 0\right)$ e $V(0,0)$
1. O foco está sobre o eixo $Ox$ com abscissa negativa $\Rightarrow$ eixo de simetria $Ox$, concavidade para a esquerda, formato $y^2 = 2px$.
2. Igualando $\frac{p}{2} = -\frac{5}{2} \implies p = -5$, portanto $2p = -10$.
3. Equação reduzida: $\mathbf{y^2 = -10x}$, com reta diretriz $\mathbf{x = \frac{5}{2}}$.

---

## 3. Exercícios (`F01-E01` a `F01-E06`)

### `F01-E01` *(Reprodução do modelo — Leitura de elementos)*
Dada a parábola de equação $y^2 = 16x$, determine:  
**(a)** O parâmetro $p$  
**(b)** As coordenadas do foco $F$  
**(c)** A equação da reta diretriz

**Formato de resposta:** `(a) p (b) (x, y) (c) x = ...`.

---

### `F01-E02` *(Técnica central — Equação a partir da diretriz)*
Determine a equação reduzida da parábola com vértice na origem $V(0, 0)$ e reta diretriz dada por $y = \frac{7}{2}$.

---

### `F01-E03` *(Caça ao Erro — Confusão entre $p$ e $2p$)*
Ao analisar a parábola $x^2 = -8y$, um estudante escreveu que $p = -8$, concluindo que o foco seria $F(0, -4)$ e a diretriz $y = 4$.  
Identifique o erro conceitual cometido e determine corretamente:  
**(a)** O parâmetro $p$  
**(b)** As coordenadas do foco $F$  
**(c)** A equação da reta diretriz

**Formato de resposta:** `(a) p (b) (x, y) (c) y = ...`.

---

### `F01-E04` *(Variação controlada com pistas — Parábola por vértice e um ponto)*
Determine a equação reduzida da parábola com vértice na origem $V(0, 0)$, eixo de simetria coincidente com o eixo $Ox$ e que passa pelo ponto $P(-3, 6)$.

*Pistas:* Como o eixo de simetria é $Ox$, parta do modelo $y^2 = 2px$ e substitua as coordenadas de $P(-3, 6)$ para encontrar $2p$.

---

### `F01-E05` *(Variação controlada com pistas — Foco e latus rectum)*
Uma parábola com vértice na origem $V(0, 0)$ e concavidade voltada para cima passa pelo ponto $A(4, 2)$. Determine:  
**(a)** A equação reduzida da parábola  
**(b)** As coordenadas do foco $F$  
**(c)** O comprimento $|2p|$ da corda focal perpendicular ao eixo (*latus rectum*)

*Pistas:* Concavidade para cima indica eixo $Oy$ ($x^2 = 2py$). Calcule primeiro $2p$ usando o ponto $A(4, 2)$.

---

### `F01-E06` *(Resolução independente — Dedução por lugar geométrico)*
Usando diretamente a definição $d(P, F) = d(P, r)$ para o foco $F(3, 0)$ e a reta diretriz $r: x = -3$, deduza a equação da parábola e informe:  
**(a)** A equação reduzida da parábola  
**(b)** O valor positivo de $y$ quando $x = 12$

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `F01-C01` *(Elementos a partir da equação)*
Dada a parábola $x^2 = 20y$, determine:  
**(a)** As coordenadas do foco $F$  
**(b)** A equação da reta diretriz

### `F01-C02` *(Equação a partir do foco)*
Determine a equação reduzida da parábola de vértice $V(0, 0)$ e foco $F\!\left(-\frac{3}{2}, 0\right)$.

### `F01-C03` *(Parábola por ponto no eixo $Oy$)*
Uma parábola de vértice na origem $V(0, 0)$ e eixo de simetria sobre o eixo $Oy$ passa pelo ponto $Q(-6, -3)$. Determine:  
**(a)** A equação reduzida da parábola  
**(b)** A equação da reta diretriz

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `F02` (`Parábola Transladada, Completamento de Quadrados e 3 Pontos`):** somente após autocorreção de `F01-E01..E06` **e** **100% (3/3)** na Checagem Independente `F01-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** identificar se o erro foi confundir $2p$ com $p$, trocar $x^2 = 2py$ por $y^2 = 2px$, ou inverter os sinais de foco/diretriz; refazer os Exemplos 1 e 2 desenhando o esboço no plano cartesiano e aplicar a variante `V2`.
- **Após 2 tentativas malsucedidas:** recuar ao pré-requisito **`D04`** para consolidar distância analítica entre pontos antes de retomar a definição métrica da parábola.

---

## 6. Referências do Orientador
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 165–171 (Cap. 7: Seções Cônicas — definição geométrica e parábola na origem no formato $x^2 = 2py$ e $y^2 = 2px$).
- `[DOC]` `Mat_Vet_L11.pdf` p. 1 (Ex. 1–2 — identificação de foco, diretriz e equação reduzida da parábola centrada na origem).
- Gabarito e especificação de validação: [F01_gabarito.md](../gabaritos/F01_gabarito.md) e [casos_F01.json](../testes/casos_F01.json).
