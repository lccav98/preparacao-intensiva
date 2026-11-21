# Bloco `D05` — Ângulo entre Vetores, Ortogonalidade e Cossenos Diretores

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio D — Vetores em $\mathbb{R}^2/\mathbb{R}^3$, Produtos, Áreas e Volumes / **`D05`** |
| **Micro-habilidade foco** | Calcular o ângulo entre vetores via $\cos\theta = \frac{\vec{u}\cdot\vec{v}}{|\vec{u}||\vec{v}|}$, testar ortogonalidade ($\vec{u}\cdot\vec{v}=0$), determinar ângulos internos em triângulos com vetores partindo do vértice comum, e aplicar cossenos diretores e $\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$. |
| **Pré-requisitos** | `D04` *(Produto escalar $\vec{u}\cdot\vec{v}$, módulo $|\vec{v}|$ e versor $\hat{v}$)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Prática (`D05-E01`–`D05-E06`, 22 min):** `14 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`D05-C01`–`D05-C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Baseado exclusivamente no produto escalar.** Sem projeção ortogonal (`D06`) e sem produto vetorial (`D07`). Mantenha ângulos notáveis exatos em graus e cossenos em frações/radicais exatos. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`D05-E01`–`D05-E06`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Protocolo:** `PREP-MV-D05-V__-T__` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 6` | **Após autocorreção:** `___ / 6`
- **Checagem independente (sem gabarito) (`D05-C01`–`D05-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Ângulo entre dois vetores ($\theta \in [0^\circ, 180^\circ]$):**
   $$\cos\theta = \frac{\vec{u}\cdot\vec{v}}{|\vec{u}|\,|\vec{v}|}.$$
   - Se $\vec{u}\cdot\vec{v} > 0 \implies 0^\circ \le \theta < 90^\circ$ (**ângulo agudo**).
   - Se $\vec{u}\cdot\vec{v} = 0 \implies \theta = 90^\circ$ (**vetores ortogonais**, $\vec{u} \perp \vec{v}$).
   - Se $\vec{u}\cdot\vec{v} < 0 \implies 90^\circ < \theta \le 180^\circ$ (**ângulo obtuso**).
2. **Regra de ouro para ângulo interno em triângulo $ABC$:** para calcular o ângulo interno no vértice $B$, os dois vetores **devem partir de $B$**: use $\overrightarrow{BA} = A - B$ e $\overrightarrow{BC} = C - B$. Usar $\overrightarrow{AB}$ e $\overrightarrow{BC}$ mede o ângulo externo suplementar ($180^\circ - \hat{B}$)!
3. **Cuidado com raízes espúrias:** ao resolver $\cos\theta = \frac{\vec{u}\cdot\vec{v}}{|\vec{u}||\vec{v}|}$ elevando ambos os lados ao quadrado, confira o sinal de $\vec{u}\cdot\vec{v}$ na equação original (para $\theta < 90^\circ$, exige-se $\vec{u}\cdot\vec{v} > 0$).
4. **Cossenos diretores de $\vec{v} = (x, y, z) \neq \vec{0}$:** sendo $\alpha, \beta, \gamma$ os ângulos que $\vec{v}$ forma com os versores $\hat{\imath}, \hat{\jmath}, \hat{k}$ (eixos $Ox, Oy, Oz$):
   $$\cos\alpha = \frac{x}{|\vec{v}|}, \qquad \cos\beta = \frac{y}{|\vec{v}|}, \qquad \cos\gamma = \frac{z}{|\vec{v}|}.$$
   Portanto $\hat{v} = (\cos\alpha,\, \cos\beta,\, \cos\gamma)$ e vale sempre a identidade fundamental:
   $$\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1.$$

---

## 2. Exemplos Guiados

### Exemplo 1 — Ângulo interno em um triângulo (vértice comum)
Determine o ângulo interno no vértice $A$ do triângulo $A(0, 0, 0)$, $B(1, 1, 0)$ e $C(1, 0, 1)$.
1. Vetores saindo de $A$: $\overrightarrow{AB} = (1, 1, 0)$ e $\overrightarrow{AC} = (1, 0, 1)$.
2. $\overrightarrow{AB}\cdot\overrightarrow{AC} = 1(1) + 1(0) + 0(1) = 1$, $|\overrightarrow{AB}| = \sqrt{2}$, $|\overrightarrow{AC}| = \sqrt{2}$.
3. $\cos\hat{A} = \frac{1}{\sqrt{2}\cdot\sqrt{2}} = \frac{1}{2} \implies \mathbf{\hat{A} = 60^\circ}$.

### Exemplo 2 — Cossenos diretores e verificação da identidade $\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$
Para $\vec{v} = (2, -3, 6)$, temos $|\vec{v}| = \sqrt{4 + 9 + 36} = 7$.
- $\cos\alpha = \frac{2}{7}$, $\cos\beta = -\frac{3}{7}$, $\cos\gamma = \frac{6}{7}$.
- Conferência: $\left(\frac{2}{7}\right)^2 + \left(-\frac{3}{7}\right)^2 + \left(\frac{6}{7}\right)^2 = \frac{4 + 9 + 36}{49} = \frac{49}{49} = \mathbf{1}$.

---

## 3. Exercícios (`D05-E01` a `D05-E06`)

### `D05-E01` *(Reprodução do modelo — Cosseno e classificação do ângulo)*
Dados $\vec{u} = (1, 2, -2)$ e $\vec{v} = (2, -1, 2)$, determine:  
**(a)** $\cos\theta$, onde $\theta$ é o ângulo entre $\vec{u}$ e $\vec{v}$  
**(b)** A classificação de $\theta$ (`agudo`, `reto` ou `obtuso`)

---

### `D05-E02` *(Técnica central — Ortogonalidade com parâmetro)*
Determine todos os valores reais de $\alpha$ para que os vetores $\vec{a} = \alpha\hat{\imath} + 3\hat{\jmath} - 3\hat{k}$ e $\vec{b} = (\alpha - 2)\hat{\imath} + \hat{\jmath} + 2\hat{k}$ sejam ortogonais.

---

### `D05-E03` *(Caça ao Erro — Ângulo interno em triângulo sem vértice comum)*
Para o triângulo de vértices $A(3, 1, 2)$, $B(1, -1, 2)$ e $C(3, -1, 4)$, um estudante calculou o ângulo interno no vértice $B$ usando $\overrightarrow{AB}$ e $\overrightarrow{BC}$ e concluiu que $\hat{B} = 120^\circ$ (ângulo obtuso).  
Identifique a falha geométrica do estudante, recalcule usando vetores partindo do vértice comum $B$ e informe:  
**(a)** $\cos\hat{B}$  
**(b)** A medida correta do ângulo interno $\hat{B}$ (em graus)

---

### `D05-E04` *(Variação controlada com pistas — Cossenos diretores e soma dos quadrados)*
Dado o vetor $\vec{v} = (2, -1, 2)$, determine:  
**(a)** A terna dos cossenos diretores $(\cos\alpha,\, \cos\beta,\, \cos\gamma)$  
**(b)** O valor numérico de $\cos^2\alpha + \cos^2\beta + \cos^2\gamma$

*Pistas:* Calcule primeiro $|\vec{v}|$ e obtenha o versor $\hat{v} = \vec{v}/|\vec{v}|$; suas três coordenadas são exatamente os cossenos diretores.

---

### `D05-E05` *(Variação controlada com pistas — Ângulo diretor faltante via $\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$)*
Um vetor unitário $\hat{u}$ forma um ângulo $\alpha = 60^\circ$ com o eixo $Ox$ e $\beta = 45^\circ$ com o eixo $Oy$. Determine:  
**(a)** Os dois valores possíveis para $\cos\gamma$  
**(b)** A medida do ângulo diretor agudo $\gamma$ (em graus)

*Pistas:* Substitua $\cos 60^\circ = \frac{1}{2}$ e $\cos 45^\circ = \frac{\sqrt{2}}{2}$ em $\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$.

---

### `D05-E06` *(Resolução independente — Parâmetro para ângulo dado e raiz espúria)*
Determine o valor real de $m$ para que o ângulo entre os vetores $\vec{u} = (1, 1, 2)$ e $\vec{v} = (2, -1, m)$ seja $60^\circ$. *(Atenção: verifique o sinal de $\vec{u}\cdot\vec{v}$ antes de aceitar todas as raízes da equação quadrática!)*

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `D05-C01` *(Ângulo interno em triângulo)*
Dados os pontos $P(0, 1, -1)$, $Q(2, 3, -1)$ e $R(2, 1, 1)$, calcule:  
**(a)** $\cos\hat{P}$  
**(b)** O ângulo interno do triângulo $PQR$ no vértice $P$ (em graus)

### `D05-C02` *(Ortogonalidade com parâmetro sem corte de raiz nula)*
Determine todos os valores reais de $k$ para que os vetores $\vec{u} = (k, 2, -k)$ e $\vec{v} = (k + 2, k, 3)$ sejam ortogonais.

### `D05-C03` *(Reconstrução de vetor pelos cossenos diretores)*
Um vetor $\vec{w}$ tem módulo $|\vec{w}| = 6$, cossenos diretores $\cos\alpha = \frac{2}{3}$ e $\cos\beta = \frac{1}{3}$, e forma um ângulo $\gamma$ **obtuso** com o eixo $Oz$. Determine as coordenadas de $\vec{w}$.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `D06` (`Projeção Ortogonal`):** somente após autocorreção de `D05-E01..E06` **e** **100% (3/3)** na Checagem Independente `D05-C01..C03` sem consulta.
- **Recuperação direcionada (1ª falha):** identificar se a falha foi escolher vetores sem vértice comum no triângulo, perder raiz ao fatorar $\vec{u}\cdot\vec{v} = 0$ (como $k=0$), ou aceitar raiz espúria com $\vec{u}\cdot\vec{v} < 0$ para ângulo agudo; revisar os Exemplos 1 e 2 e aplicar a variante `V2`.
- **Após 2 tentativas malsucedidas:** recuar ao pré-requisito **`D04`** para consolidar produto escalar, cálculo exato de módulo e versor.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Vetores.pdf` p. 56–61 (ângulo entre vetores, condição de ortogonalidade e cossenos diretores).
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 110–113 (Cap. 3 — exemplos de ângulo interno em triângulo e $\cos^2\alpha+\cos^2\beta+\cos^2\gamma=1$).
- `[DOC]` `Mat_Vet_L7.pdf` p. 1 (Ex. 6–10 e Ex. 14 — ângulo interno ao vértice $B$, cálculo de $m$ para $\theta = \pi/3$ e ortogonalidade).
- Gabarito e especificação de validação: [D05_gabarito.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/gabaritos/D05_gabarito.md) e [casos_D05.json](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/testes/casos_D05.json).
