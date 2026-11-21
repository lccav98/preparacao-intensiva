# Bloco `D06` — Projeção Ortogonal ($\operatorname{proj}_{\vec{v}}\vec{u}$)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio D — Vetores em $\mathbb{R}^2/\mathbb{R}^3$, Produtos, Áreas e Volumes / **`D06`** |
| **Micro-habilidade foco** | Calcular o vetor projeção ortogonal $\operatorname{proj}_{\vec{v}}\vec{u} = \left(\frac{\vec{u}\cdot\vec{v}}{|\vec{v}|^2}\right)\vec{v}$, seu módulo e a decomposição $\vec{u} = \vec{u}_{\parallel} + \vec{u}_{\perp}$ em relação a um vetor $\vec{v} \neq \vec{0}$. |
| **Pré-requisitos** | `D04` *(Produto escalar e $|\vec{v}|^2$)*; `D05` *(Ortogonalidade $\vec{u}_{\perp}\cdot\vec{v}=0$)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Prática (`D06-E01`–`D06-E06`, 18 min):** `11 min` resol. \| `4 min` corr. \| `3 min` recup.; **Checagem (`D06-C01`–`D06-C03`, 12 min):** `8 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Fórmula direta de projeção ortogonal de um vetor sobre outro no $\mathbb{R}^2/\mathbb{R}^3$.** Respostas exatas com frações irredutíveis e radicais, com verificação obrigatória $\vec{u}_{\perp}\cdot\vec{v} = 0$. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`D06-E01`–`D06-E06`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Protocolo:** `PREP-MV-D06-V__-T__` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 6` | **Após autocorreção:** `___ / 6`
- **Checagem independente (sem gabarito) (`D06-C01`–`D06-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Definição e fórmula da projeção:** sendo $\vec{v} \neq \vec{0}$, o vetor projeção ortogonal de $\vec{u}$ na direção de $\vec{v}$ é o múltiplo de $\vec{v}$ dado por:
   $$\operatorname{proj}_{\vec{v}}\vec{u} = \left(\frac{\vec{u}\cdot\vec{v}}{\vec{v}\cdot\vec{v}}\right)\vec{v} = \left(\frac{\vec{u}\cdot\vec{v}}{|\vec{v}|^2}\right)\vec{v}.$$
   **Atenção dupla:**
   - O vetor que fica **subscrito** ($\vec{v}$) define a direção da projeção, entra no **denominador** ($|\vec{v}|^2$) e é o vetor **multiplicado** pelo escalar!
   - Nunca divida por $|\vec{v}|$ sem elevar ao quadrado ao usar $\vec{v}$ (não-unitário). Dividir por $|\vec{v}|$ ocorre apenas na fórmula do **comprimento** da projeção:
     $$\left|\operatorname{proj}_{\vec{v}}\vec{u}\right| = \frac{|\vec{u}\cdot\vec{v}|}{|\vec{v}|}.$$
2. **Decomposição ortogonal de $\vec{u}$ em relação a $\vec{v}$:** todo vetor $\vec{u}$ escreve-se como soma de uma componente paralela a $\vec{v}$ e uma componente ortogonal a $\vec{v}$:
   $$\vec{u} = \vec{u}_{\parallel} + \vec{u}_{\perp}, \qquad \text{onde } \vec{u}_{\parallel} = \operatorname{proj}_{\vec{v}}\vec{u} \quad \text{e} \quad \vec{u}_{\perp} = \vec{u} - \operatorname{proj}_{\vec{v}}\vec{u}.$$
3. **Teste de prova real:** após calcular $\vec{u}_{\perp}$, verifique sempre que $\vec{u}_{\perp}\cdot\vec{v} = 0$.

---

## 2. Exemplos Guiados

### Exemplo 1 — Vetor projeção $\operatorname{proj}_{\vec{v}}\vec{u}$
Calcule $\operatorname{proj}_{\vec{v}}\vec{u}$ para $\vec{u} = (2, 3, -1)$ e $\vec{v} = (1, -2, 2)$:
1. $\vec{u}\cdot\vec{v} = 2(1) + 3(-2) + (-1)(2) = 2 - 6 - 2 = -6$.
2. $|\vec{v}|^2 = \vec{v}\cdot\vec{v} = 1^2 + (-2)^2 + 2^2 = 9$.
3. $\operatorname{proj}_{\vec{v}}\vec{u} = \frac{-6}{9}(1, -2, 2) = -\frac{2}{3}(1, -2, 2) = \mathbf{\left(-\frac{2}{3},\, \frac{4}{3},\, -\frac{4}{3}\right)}$.

### Exemplo 2 — Decomposição em componente paralela e ortogonal
Decomponha $\vec{u} = (4, 1, -2)$ na direção de $\vec{v} = (2, 1, 2)$:
1. $\vec{u}\cdot\vec{v} = 8 + 1 - 4 = 5$ e $|\vec{v}|^2 = 4 + 1 + 4 = 9$.
2. $\vec{u}_{\parallel} = \operatorname{proj}_{\vec{v}}\vec{u} = \frac{5}{9}(2, 1, 2) = \mathbf{\left(\frac{10}{9},\, \frac{5}{9},\, \frac{10}{9}\right)}$.
3. $\vec{u}_{\perp} = \vec{u} - \vec{u}_{\parallel} = \left(4 - \frac{10}{9},\; 1 - \frac{5}{9},\; -2 - \frac{10}{9}\right) = \mathbf{\left(\frac{26}{9},\, \frac{4}{9},\, -\frac{28}{9}\right)}$.
4. Conferência: $\vec{u}_{\perp}\cdot\vec{v} = \frac{52 + 4 - 56}{9} = 0$.

---

## 3. Exercícios (`D06-E01` a `D06-E06`)

### `D06-E01` *(Reprodução do modelo — Projeção direta)*
Determine o vetor projeção $\operatorname{proj}_{\vec{v}}\vec{u}$ para $\vec{u} = (3, -2, 5)$ e $\vec{v} = (2, 1, -2)$.

---

### `D06-E02` *(Técnica central — Decomposição paralela e ortogonal)*
Dados $\vec{u} = (4, -1, 3)$ e $\vec{v} = (1, 2, 2)$, determine:  
**(a)** A componente paralela $\vec{u}_{\parallel} = \operatorname{proj}_{\vec{v}}\vec{u}$  
**(b)** A componente ortogonal $\vec{u}_{\perp} = \vec{u} - \vec{u}_{\parallel}$

---

### `D06-E03` *(Caça ao Erro — Denominador $|\vec{v}|$ vs. $|\vec{v}|^2$)*
Para $\vec{u} = (5, 1, -2)$ e $\vec{v} = (1, 1, -1)$, um estudante calculou $\operatorname{proj}_{\vec{v}}\vec{u}$ usando $\frac{\vec{u}\cdot\vec{v}}{|\vec{u}|^2}\vec{v}$ e obteve $\frac{4}{15}\vec{v}$.  
Explique a troca de denominador do estudante e calcule exatamente:  
**(a)** $\operatorname{proj}_{\vec{v}}\vec{u}$  
**(b)** O comprimento $|\operatorname{proj}_{\vec{v}}\vec{u}|$

---

### `D06-E04` *(Variação controlada com pistas — Projeção sobre $\overrightarrow{AB}$)*
Dados os pontos $A(1, 0, 2)$, $B(3, 2, 1)$ e o vetor $\vec{u} = (4, -1, 2)$, determine o vetor $\operatorname{proj}_{\overrightarrow{AB}}\vec{u}$.

*Pistas:* Calcule $\vec{v} = \overrightarrow{AB} = B - A$ primeiro, depois aplique $\left(\frac{\vec{u}\cdot\vec{v}}{|\vec{v}|^2}\right)\vec{v}$.

---

### `D06-E05` *(Variação controlada com pistas — Parâmetro na projeção)*
Determine o valor real de $m$ para que a projeção de $\vec{u} = (m, 3, -1)$ na direção de $\vec{v} = (2, -1, 2)$ seja igual ao próprio vetor $\vec{v}$ (isto é, $\operatorname{proj}_{\vec{v}}\vec{u} = (2, -1, 2)$).

*Pistas:* Se $\operatorname{proj}_{\vec{v}}\vec{u} = 1\cdot\vec{v}$, o coeficiente escalar $\frac{\vec{u}\cdot\vec{v}}{|\vec{v}|^2}$ deve valer $1$.

---

### `D06-E06` *(Resolução independente — Decomposição $\vec{a} = \vec{p} + \vec{q}$)*
Decomponha o vetor $\vec{a} = (5, 2, -4)$ na soma $\vec{a} = \vec{p} + \vec{q}$ tal que $\vec{p} \parallel \vec{b}$ e $\vec{q} \perp \vec{b}$, sendo $\vec{b} = (2, -2, 1)$. Informe:  
**(a)** O vetor $\vec{p}$  
**(b)** O vetor $\vec{q}$

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `D06-C01` *(Projeção ortogonal direta)*
Determine $\operatorname{proj}_{\vec{v}}\vec{u}$ para $\vec{u} = (2, -5, 4)$ e $\vec{v} = (1, -2, 2)$.

### `D06-C02` *(Decomposição completa)*
Para $\vec{u} = (7, -4, 3)$ e $\vec{v} = (2, -1, 2)$, determine:  
**(a)** $\vec{u}_{\parallel} = \operatorname{proj}_{\vec{v}}\vec{u}$  
**(b)** $\vec{u}_{\perp} = \vec{u} - \vec{u}_{\parallel}$

### `D06-C03` *(Comprimento da projeção e inversão da base)*
Dados $\vec{u} = (1, 2, 2)$ e $\vec{v} = (3, 0, 4)$, determine:  
**(a)** O comprimento $\left|\operatorname{proj}_{\vec{v}}\vec{u}\right|$  
**(b)** O vetor $\operatorname{proj}_{\vec{u}}\vec{v}$ *(atenção à ordem: agora projeta-se $\vec{v}$ sobre $\vec{u}$!)*

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `D07` (`Produto Vetorial, Propriedades e Ortogonalidade`):** somente após autocorreção de `D06-E01..E06` **e** **100% (3/3)** na Checagem Independente `D06-C01..C03` sem consulta.
- **Recuperação direcionada (1ª falha):** verificar se houve inversão entre $\vec{u}$ e $\vec{v}$ no denominador $|\vec{v}|^2$, esquecimento do expoente $2$ em $|\vec{v}|^2$, ou erro de fração em $\vec{u} - \vec{u}_{\parallel}$; revisar os Exemplos 1 e 2 e aplicar a variante `V2`.
- **Após 2 tentativas malsucedidas:** recuar para **`D04`** (se errou $\vec{u}\cdot\vec{v}$ ou $|\vec{v}|^2$) ou **`D05`** (se não compreendeu o significado geométrico de $\vec{u}_{\perp} \perp \vec{v}$).

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Vetores.pdf` p. 62–64 (dedução e fórmula de $\operatorname{proj}_{\vec{v}}\vec{u}$ e decomposição ortogonal).
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 113–114 (Cap. 3 — interpretação geométrica e exemplo resolvido de projeção).
- `[DOC]` `Mat_Vet_L7.pdf` p. 1 (Ex. 15 — vetor projeção de $\vec{u}$ na direção de $\vec{v}$).
- Gabarito e especificação de validação: [D06_gabarito.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/gabaritos/D06_gabarito.md) e [casos_D06.json](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/testes/casos_D06.json).
