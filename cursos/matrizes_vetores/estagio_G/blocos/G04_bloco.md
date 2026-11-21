# Bloco `G04` — Simulado Integrador P3 (Parte 1) — Retas, Planos e Distâncias

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio G — Integração Geral e Simulados por Avaliação / **`G04`** |
| **Micro-habilidade foco** | Integrar, no padrão P3 sem consulta, equações da reta (reduzida em $x$, paramétrica, simétrica, ortogonal a duas), posições relativas e interseção de retas, equação geral do plano, ângulo reta-plano ($\sin\phi$), interseção de dois planos e reta-plano, volume via interceptos e distâncias entre retas reversas e planos paralelos. |
| **Pré-requisitos** | `E10` *(Revisão cumulativa do Estágio E)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`G04-E01`–`G04-E05`, 25 min):** `16 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`G04-C01`–`G04-C03`, 18 min):** `14 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Simulado P3 (Parte 1) sem consulta.** **Proibido:** Regra de Sarrus, Regra de Cramer, Gram-Schmidt ou aproximações decimais. Sempre expresse a reta reduzida em função de $x$ (quando $v_x \neq 0$), teste paralelismo antes de aplicar a fórmula de retas reversas e normalize coeficientes $(a, b, c)$ antes de calcular distância entre planos paralelos. |

### Registro da Sessão (Preenchido na Prática)
- **Protocolo:** `PREP-MV-G04-<VARIANTE>-T<TENTATIVA>-<HASH>`
- **Sessão única (`G04-E01`–`G04-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`G04-C01`–`G04-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **A Reta no $\mathbb{R}^3$ (`E01`–`E03`):**
   - Formas equivalentes: vetorial $(x,y,z)=P_0+t\vec{v}$, paramétricas, simétricas e **reduzidas em função de $x$** ($y=mx+n,\; z=px+q$).
   - Reta ortogonal a $\vec{v}_1$ e $\vec{v}_2$: vetor diretor $\vec{v} = \vec{v}_1 \times \vec{v}_2$.
   - Posição relativa entre $r_1(P_1,\vec{v}_1)$ e $r_2(P_2,\vec{v}_2)$: verifique se $\vec{v}_1 \parallel \vec{v}_2$ (paralelas/coincidentes); caso contrário, calcule o produto misto $(\vec{v}_1, \vec{v}_2, \overrightarrow{P_1P_2})$: se $\neq 0$, são **reversas**; se $= 0$, são **concorrentes**.
2. **O Plano no $\mathbb{R}^3$ (`E04`–`E06`):**
   - Equação geral $\pi: ax + by + cz + d = 0$ com normal $\vec{n} = (a, b, c)$.
   - Ângulo reta-plano: $\sin\phi = \frac{|\vec{v}\cdot\vec{n}|}{|\vec{v}|\,|\vec{n}|}$ *(atenção: seno, não cosseno!)*.
3. **Distâncias (`E07`–`E09`):**
   - Ponto-reta: $d(P_0, r) = \frac{|\vec{v}\times\overrightarrow{P_1P_0}|}{|\vec{v}|}$.
   - Retas reversas: $d(r_1, r_2) = \frac{|(\vec{u}, \vec{v}, \overrightarrow{P_1P_2})|}{|\vec{u}\times\vec{v}|}$ *(somente após confirmar $\vec{u}\times\vec{v} \neq \vec{0}$!)*.
   - Planos paralelos: iguale $(a, b, c)$ nas duas equações antes de aplicar $d(\pi_1, \pi_2) = \frac{|d_1 - d_2|}{\sqrt{a^2 + b^2 + c^2}}$.

---

## 2. Exemplos Guiados

### Exemplo 1 — Duas Armadilhas Clássicas de P3 (Parte 1)
1. **Planos paralelos:** entre $2x - y + 2z - 3 = 0$ e $4x - 2y + 4z + 12 = 0$, **nunca** faça $|12 - (-3)|$ diretamente: divida o segundo plano por $2$ ($2x - y + 2z + 6 = 0$) para igualar o vetor normal $(2, -1, 2)$, obtendo $d = \frac{|6 - (-3)|}{\sqrt{4+1+4}} = 3$.
2. **Ângulo reta-plano:** $\phi$ é o complementar do ângulo entre $\vec{v}$ e $\vec{n}$; por isso utiliza-se $\sin\phi = \frac{|\vec{v}\cdot\vec{n}|}{|\vec{v}||\vec{n}|}$.

---

## 3. Exercícios (`G04-E01` a `G04-E05`)

### `G04-E01` *(Equações da reta e reta ortogonal a duas retas)*
**(a)** Determine as equações reduzidas em função de $x$ da reta $r$ que passa pelos pontos $A(1, 2, -1)$ e $B(3, 6, 3)$.  
**(b)** Determine uma equação da reta $s$ que passa pela origem $O(0, 0, 0)$ e é ortogonal simultaneamente a duas retas de vetores diretores $\vec{v}_1 = (1, -1, 2)$ e $\vec{v}_2 = (2, 1, -1)$.

*Formato de resposta:* `(a) y = ..., z = ... (b) (x, y, z) = (0, 0, 0) + t(...)`.

---

### `G04-E02` *(Posição relativa de duas retas e interseção)*
Considere as retas:
$$r_1: \begin{cases} x = 1 + t \\ y = 2 - t \\ z = 3 + 2t \end{cases} \qquad \text{e} \qquad r_2: \begin{cases} x = 3 - s \\ y = -1 + 2s \\ z = 6 - s \end{cases}$$
**(a)** Classifique a posição relativa entre $r_1$ e $r_2$ (`concorrentes`, `paralelas` ou `reversas`).  
**(b)** Caso sejam concorrentes, determine o ponto de interseção $r_1 \cap r_2$.

*Formato de resposta:* `(a) classificacao (b) (x, y, z)`.

---

### `G04-E03` *(Equação geral do plano por 3 pontos e ângulo reta-plano)*
**(a)** Determine a equação geral do plano $\pi$ que passa pelos pontos $A(1, 0, 1)$, $B(2, 1, 1)$ e $C(0, 1, 2)$.  
**(b)** Calcule o valor exato de $\sin\phi$, em que $\phi$ é o ângulo formado entre a reta $r: (x, y, z) = (0, 0, 0) + t(1, 2, 2)$ e o plano $\pi$.

*Formato de resposta:* `(a) ax + by + cz + d = 0 (b) valor_exato`.

---

### `G04-E04` *(Interseção de dois planos e volume pelos interceptos)*
**(a)** Determine as equações paramétricas da reta $r$ obtida pela interseção dos planos $\pi_1: x + y - z = 2$ e $\pi_2: 2x - y + z = 4$.  
**(b)** Calcule o volume do tetraedro limitado pelo plano $\alpha: 2x + 3y + 6z = 12$ e pelos três planos coordenados.

*Formato de resposta:* `(a) x = ..., y = ..., z = ... (b) valor`.

---

### `G04-E05` *(Distância entre retas reversas e entre planos paralelos)*
**(a)** Calcule a distância exata entre as retas reversas $r_1: (x, y, z) = (1, 0, 1) + t(1, 1, 0)$ e $r_2: (x, y, z) = (0, 1, 2) + s(0, 1, 1)$.  
**(b)** Calcule a distância exata entre os planos paralelos $\pi_1: 2x - y + 2z - 3 = 0$ e $\pi_2: 4x - 2y + 4z + 12 = 0$.

*Formato de resposta:* `(a) valor_exato (b) valor`.

---

## 4. Checagem Independente (`G04-C01` a `G04-C03`)
*(Simulado P3 Parte 1 sem consulta. Critério de aprovação: **100% — 3/3**.)*

### `G04-C01` *(Plano por ponto e reta + interseção reta-plano)*
**(a)** Determine a equação geral do plano $\pi$ que contém o ponto $P(1, 2, 0)$ e a reta $r: \frac{x - 1}{2} = \frac{y}{1} = \frac{z + 1}{1}$.  
**(b)** Determine o ponto de interseção da reta $s: (x, y, z) = (2, 1, -1) + t(1, -1, 2)$ com o plano $\beta: 2x + y - z = 10$.

*Formato de resposta:* `(a) ax + by + cz + d = 0 (b) (x, y, z)`.

---

### `G04-C02` *(Distância entre retas reversas sem consulta)*
Calcule a distância exata entre as retas reversas:
$$r_1: \begin{cases} x = 1 + t \\ y = 2t \\ z = -1 + t \end{cases} \qquad \text{e} \qquad r_2: \begin{cases} x = 2 - s \\ y = 1 + s \\ z = 2s \end{cases}$$

*Formato de resposta:* radical exato (ex.: `sqrt(3)/3`).

---

### `G04-C03` *(Distância entre planos paralelos e distância ponto-reta)*
**(a)** Calcule a distância exata entre os planos paralelos $\pi_1: x + 2y - 2z + 4 = 0$ e $\pi_2: -3x - 6y + 6z + 15 = 0$.  
**(b)** Calcule a distância exata do ponto $Q(3, 1, -2)$ à reta $r: (x, y, z) = (1, 0, 1) + t(2, 1, -2)$.

*Formato de resposta:* `(a) valor (b) valor_exato`.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `G05` (`Simulado Integrador P3 — Parte 2`):** somente após autocorreção de `G04-E01`–`G04-E05` e **100% (3/3)** na Checagem Independente `G04-C01`–`G04-C03`.
- **Recuperação direcionada (1ª falha):** identifique o tópico com erro (reta reduzida/ortogonal → `E01`/`E02`; posição relativa → `E03`; plano/ângulo → `E04`/`E05`; interseções → `E06`; distâncias → `E07`/`E08`/`E09`) e aplique a variante `V2` de `G04`.
- **Após 2 tentativas malsucedidas:** recuar no DAG para **`E10`** (ou diretamente ao pré-requisito da falha em **`E03`**, **`E06`**, **`E08`** ou **`E09`**).

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_RE42B_Planejamento.pdf` (Semanas 11–12 — 1ª metade da Avaliação P3).
- `[DOC]` `MAT121_Parte_4.pdf` p. 1–61; `Matrizes_Vetores_P3.pdf` p. 124–164; `Mat_Vet_L8.pdf` a `Mat_Vet_L10.pdf`.
- Gabarito comentado e casos de teste: [G04_gabarito.md](../gabaritos/G04_gabarito.md) e [casos_G04.json](../testes/casos_G04.json).
