# Bloco `D07` — Produto Vetorial ($\vec{u}\times\vec{v}$), Propriedades e Ortogonalidade

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio D — Vetores em $\mathbb{R}^2/\mathbb{R}^3$, Produtos, Áreas e Volumes / **`D07`** |
| **Micro-habilidade foco** | Calcular o produto vetorial $\vec{u}\times\vec{v}$ por desenvolvimento na 1ª linha (matriz de sinais $+ - +$), aplicar anti-comutatividade, regra da mão direita e Identidade de Lagrange, e construir vetores/versores simultaneamente ortogonais a dois vetores no $\mathbb{R}^3$. |
| **Pré-requisitos** | `D05` *(Ortogonalidade e ângulo entre vetores)*; `B01` *(Determinante $3\times 3$ pela 1ª linha)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Prática (`D07-E01`–`D07-E06`, 22 min):** `14 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`D07-C01`–`D07-C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Desenvolva o determinante simbólico exclusivamente pela 1ª linha** ($\hat{\imath}, -\hat{\jmath}, +\hat{k}$ com cofatores $2\times 2$). O produto vetorial é definido apenas no $\mathbb{R}^3$. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`D07-E01`–`D07-E06`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Protocolo:** `PREP-MV-D07-V__-T__` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 6` | **Após autocorreção:** `___ / 6`
- **Checagem independente (sem gabarito) (`D07-C01`–`D07-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Definição por desenvolvimento de Laplace na 1ª linha:** dados $\vec{u} = (x_1, y_1, z_1)$ e $\vec{v} = (x_2, y_2, z_2)$ no $\mathbb{R}^3$:
   $$\vec{u}\times\vec{v} = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ x_1 & y_1 & z_1 \\ x_2 & y_2 & z_2 \end{vmatrix} = \begin{vmatrix} y_1 & z_1 \\ y_2 & z_2 \end{vmatrix}\hat{\imath} - \begin{vmatrix} x_1 & z_1 \\ x_2 & z_2 \end{vmatrix}\hat{\jmath} + \begin{vmatrix} x_1 & y_1 \\ x_2 & y_2 \end{vmatrix}\hat{k}.$$
   **Armadilha clássica:** nunca esqueça o **sinal negativo** na frente do cofator de $\hat{\jmath}$ (posição $(1,2)$ da matriz de sinais $+ - +$).
2. **Propriedades algébricas e geométricas:**
   - **Anti-comutatividade:** $\vec{v}\times\vec{u} = -(\vec{u}\times\vec{v})$.
   - **Paralelismo / Nulidade:** $\vec{u}\times\vec{u} = \vec{0}$; mais geralmente, $\vec{u}\times\vec{v} = \vec{0} \iff \vec{u} \parallel \vec{v}$ (ou algum é nulo).
   - **Distributividade e escalar:** $\vec{u}\times(\vec{v}+\vec{w}) = \vec{u}\times\vec{v} + \vec{u}\times\vec{w}$ e $(k\vec{u})\times\vec{v} = k(\vec{u}\times\vec{v})$.
   - **Ortogonalidade simultânea:** $\vec{u}\times\vec{v}$ é ortogonal tanto a $\vec{u}$ quanto a $\vec{v}$, isto é: $\vec{u}\cdot(\vec{u}\times\vec{v}) = 0$ e $\vec{v}\cdot(\vec{u}\times\vec{v}) = 0$ (teste de prova real obrigatório!).
   - **Regra da mão direita:** $\hat{\imath}\times\hat{\jmath} = \hat{k}$, $\hat{\jmath}\times\hat{k} = \hat{\imath}$, $\hat{k}\times\hat{\imath} = \hat{\jmath}$ (e invertendo a ordem troca o sinal).
3. **Módulo e Identidade de Lagrange:** sendo $\theta$ o ângulo entre $\vec{u}$ e $\vec{v}$:
   $$|\vec{u}\times\vec{v}| = |\vec{u}|\,|\vec{v}|\sin\theta, \qquad |\vec{u}\times\vec{v}|^2 = |\vec{u}|^2|\vec{v}|^2 - (\vec{u}\cdot\vec{v})^2.$$

---

## 2. Exemplos Guiados

### Exemplo 1 — Produto vetorial pela 1ª linha e verificação de ortogonalidade
Calcule $\vec{u}\times\vec{v}$ para $\vec{u} = (1, -2, 3)$ e $\vec{v} = (2, 1, -1)$:
$$\vec{u}\times\vec{v} = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ 1 & -2 & 3 \\ 2 & 1 & -1 \end{vmatrix} = \begin{vmatrix} -2 & 3 \\ 1 & -1 \end{vmatrix}\hat{\imath} - \begin{vmatrix} 1 & 3 \\ 2 & -1 \end{vmatrix}\hat{\jmath} + \begin{vmatrix} 1 & -2 \\ 2 & 1 \end{vmatrix}\hat{k}.$$
- Componente $\hat{\imath}$: $(-2)(-1) - 3(1) = 2 - 3 = -1$.
- Componente $\hat{\jmath}$: $-\big(1(-1) - 3(2)\big) = -(-1 - 6) = 7$.
- Componente $\hat{k}$: $1(1) - (-2)(2) = 1 + 4 = 5$.
Logo $\vec{u}\times\vec{v} = \mathbf{(-1, 7, 5)}$.  
*Prova real:* $(1,-2,3)\cdot(-1,7,5) = -1 - 14 + 15 = 0$ e $(2,1,-1)\cdot(-1,7,5) = -2 + 7 - 5 = 0$.

### Exemplo 2 — Módulo pela Identidade de Lagrange
Se $|\vec{a}| = 2$, $|\vec{b}| = 5$ e $\vec{a}\cdot\vec{b} = 6$, então:
$$|\vec{a}\times\vec{b}|^2 = |\vec{a}|^2|\vec{b}|^2 - (\vec{a}\cdot\vec{b})^2 = 2^2\cdot 5^2 - 6^2 = 100 - 36 = 64 \implies |\vec{a}\times\vec{b}| = \mathbf{8}.$$

---

## 3. Exercícios (`D07-E01` a `D07-E06`)

### `D07-E01` *(Reprodução do modelo — Anti-comutatividade)*
Dados $\vec{u} = (2, -1, 3)$ e $\vec{v} = (1, 4, -2)$, calcule:  
**(a)** $\vec{u}\times\vec{v}$  
**(b)** $\vec{v}\times\vec{u}$

---

### `D07-E02` *(Técnica central — Propriedades algébricas do produto vetorial)*
Dados os vetores $\vec{a} = (1, 2, -1)$ e $\vec{b} = (2, 0, 1)$, calcule:  
**(a)** $2\vec{a}\times(\vec{a} + \vec{b})$  
**(b)** $(\vec{a} + 2\vec{b})\times(\vec{a} - 2\vec{b})$

---

### `D07-E03` *(Caça ao Erro — Sinal do cofator de $\hat{\jmath}$ e prova real)*
Ao calcular $\vec{u}\times\vec{v}$ para $\vec{u} = (3, -1, 2)$ e $\vec{v} = (1, 2, -4)$, um estudante esqueceu o sinal negativo da componente $\hat{\jmath}$ e respondeu $(0, -14, 7)$.  
Mostre que $(0, -14, 7)$ falha na verificação de ortogonalidade $\vec{u}\cdot\vec{w} = 0$, e informe:  
**(a)** O vetor correto $\vec{u}\times\vec{v}$  
**(b)** O valor exato de $\vec{u}\cdot(\vec{u}\times\vec{v})$

---

### `D07-E04` *(Variação controlada com pistas — Expressão com pontos no $\mathbb{R}^3$)*
Dados os pontos $A(1, 0, 2)$, $B(2, -1, 3)$ e $C(0, 2, 1)$, determine o vetor:
$$\overrightarrow{CB}\times\left(\overrightarrow{BC} - 2\overrightarrow{CA}\right).$$

*Pistas:* Calcule $\overrightarrow{CB} = B - C$, $\overrightarrow{BC} = -\overrightarrow{CB}$ e $\overrightarrow{CA} = A - C$; substitua no segundo fator antes de calcular o produto vetorial (ou aplique distributividade com $\overrightarrow{CB}\times\overrightarrow{BC} = \vec{0}$).

---

### `D07-E05` *(Variação controlada com pistas — Vetor e versor ortogonais a dois vetores)*
Dados $\vec{u} = (1, 2, 0)$ e $\vec{v} = (0, -2, 1)$, determine:  
**(a)** Um vetor não nulo simultaneamente ortogonal a $\vec{u}$ e $\vec{v}$  
**(b)** Um versor simultaneamente ortogonal a $\vec{u}$ e $\vec{v}$

*Pistas:* Qualquer múltiplo não nulo de $\vec{u}\times\vec{v}$ atende **(a)**; para **(b)**, divida $\vec{u}\times\vec{v}$ por seu módulo $|\vec{u}\times\vec{v}|$.

---

### `D07-E06` *(Resolução independente — Norma do produto vetorial e escalar pelo ângulo)*
Sabendo que $|\vec{a}| = 4$, $|\vec{b}| = \sqrt{3}$ e o ângulo entre $\vec{a}$ e $\vec{b}$ é $60^\circ$, calcule os valores exatos de:  
**(a)** $|\vec{a}\times\vec{b}|$  
**(b)** $|\vec{a}\cdot\vec{b}|$

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `D07-C01` *(Produto vetorial com propriedades)*
Dados $\vec{u} = (2, 1, -1)$ e $\vec{v} = (1, -2, 3)$, determine $(\vec{u} + \vec{v})\times(\vec{u} - \vec{v})$.

### `D07-C02` *(Versor ortogonal a dois vetores)*
Determine um versor simultaneamente ortogonal a $\vec{p} = (1, 0, 2)$ e $\vec{q} = (1, 2, -2)$.

### `D07-C03` *(Identidade de Lagrange)*
Sabendo que $|\vec{u}| = 5$, $|\vec{v}| = 4$ e $\vec{u}\cdot\vec{v} = 12$, calcule o valor exato de $|\vec{u}\times\vec{v}|$.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `D08` (`Áreas via Produto Vetorial — Paralelogramo e Triângulo`):** somente após autocorreção de `D07-E01..E06` **e** **100% (3/3)** na Checagem Independente `D07-C01..C03` sem consulta.
- **Recuperação direcionada (1ª falha):** verificar se houve troca de sinal na componente $\hat{\jmath}$, confusão de ordem $\vec{u}\times\vec{v}$ vs. $\vec{v}\times\vec{u}$, ou esquecimento de normalizar no versor; revisar os Exemplos 1 e 2 (sempre fazendo $\vec{u}\cdot(\vec{u}\times\vec{v})=0$) e aplicar a variante `V2`.
- **Após 2 tentativas malsucedidas:** recuar para **`B01`** (se errou o desenvolvimento $3\times 3$ pela 1ª linha e sinais $+ - +$) ou **`D05`** (se errou a condição de ortogonalidade ou relação trigonométrica com $\theta$).

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Vetores.pdf` p. 65–68 (definição do produto vetorial pela 1ª linha, propriedades, regra da mão direita e $|\vec{u}\times\vec{v}|$).
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 115–118 (Cap. 3 — exemplos resolvidos de $\vec{u}\times\vec{v}$ e vetor ortogonal a dois vetores).
- `[DOC]` `Mat_Vet_L7.pdf` p. 2 (Ex. 16, 19, 20 e 23 — cálculo algébrico de produtos vetoriais e $|\vec{a}\times\vec{b}|$).
- Gabarito e especificação de validação: [D07_gabarito.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/gabaritos/D07_gabarito.md) e [casos_D07.json](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/testes/casos_D07.json).
