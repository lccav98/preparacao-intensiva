# Bloco `D03` — Combinação Linear, Paralelismo e Colinearidade de Pontos

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio D — Vetores em $\mathbb{R}^2/\mathbb{R}^3$, Produtos, Áreas e Volumes / **`D03`** |
| **Micro-habilidade foco** | Expressar um vetor como combinação linear $\vec{w} = a_1\vec{v}_1 + a_2\vec{v}_2$ (ou com 3 vetores) via escalonamento, testar paralelismo $\vec{u} = m\vec{v}$ e verificar/impor colinearidade de 3 pontos via $\overrightarrow{AB} \parallel \overrightarrow{AC}$. |
| **Pré-requisitos** | `D02` *(Vetores no $\mathbb{R}^2/\mathbb{R}^3$ e $\overrightarrow{AB}=B-A$)*; `C03` *(Escalonamento de matriz ampliada)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Prática (`D03-E01`–`D03-E06`, 22 min):** `14 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`D03-C01`–`D03-C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Resolva todo sistema linear gerado por combinação linear exclusivamente por escalonamento da matriz ampliada** (operações elementares $L_{ij}, L_i(\alpha), L_j' = L_j + L_i(\alpha)$). Trabalhe sempre em $\mathbb{R}^2$ ou $\mathbb{R}^3$ com frações exatas. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`D03-E01`–`D03-E06`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Protocolo:** `PREP-MV-D03-V__-T__` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 6` | **Após autocorreção:** `___ / 6`
- **Checagem independente (sem gabarito) (`D03-C01`–`D03-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Combinação linear:** o vetor $\vec{w}$ é combinação linear de $\vec{v}_1, \dots, \vec{v}_r$ quando existem escalares reais $a_1, \dots, a_r$ tais que:
   $$\vec{w} = a_1\vec{v}_1 + a_2\vec{v}_2 + \dots + a_r\vec{v}_r.$$
   Igualando coordenada a coordenada, obtém-se um sistema linear para $(a_1, \dots, a_r)$, resolvido por **escalonamento** da matriz ampliada (e verificado em todas as equações caso haja mais equações do que incógnitas).
2. **Paralelismo (colinearidade de vetores):** dois vetores não nulos $\vec{u} = (x_1, y_1, z_1)$ e $\vec{v} = (x_2, y_2, z_2)$ são paralelos ($\vec{u} \parallel \vec{v}$) se e somente se existir $m \in \mathbb{R}$ tal que $\vec{u} = m\vec{v}$. Quando nenhuma coordenada de $\vec{v}$ é nula, isso equivale à igualdade das três razões:
   $$\frac{x_1}{x_2} = \frac{y_1}{y_2} = \frac{z_1}{z_2} = m.$$
   *(Se alguma coordenada de $\vec{v}$ for zero, a coordenada correspondente de $\vec{u}$ também deve ser zero!)*
3. **Colinearidade de 3 pontos:** três pontos $A, B, C$ são colineares (estão sobre uma mesma reta) se e somente se os vetores $\overrightarrow{AB}$ e $\overrightarrow{AC}$ (ambos com origem em $A$) são paralelos:
   $$\overrightarrow{AC} = k\,\overrightarrow{AB} \quad (k \in \mathbb{R}).$$

---

## 2. Exemplos Guiados

### Exemplo 1 — Combinação linear no $\mathbb{R}^3$ por escalonamento
Determine $a_1, a_2$ tais que $\vec{w} = (-1, -5, 8)$ seja combinação linear de $\vec{v}_1 = (1, -1, 2)$ e $\vec{v}_2 = (2, 1, -1)$:
$$a_1(1, -1, 2) + a_2(2, 1, -1) = (-1, -5, 8) \implies \begin{cases} a_1 + 2a_2 = -1 \\ -a_1 + a_2 = -5 \\ 2a_1 - a_2 = 8 \end{cases}.$$
Escalonando a matriz ampliada:
$$\begin{bmatrix} 1 & 2 & \mid & -1 \\ -1 & 1 & \mid & -5 \\ 2 & -1 & \mid & 8 \end{bmatrix} \xrightarrow{L_2' = L_2 + L_1,\; L_3' = L_3 - 2L_1} \begin{bmatrix} 1 & 2 & \mid & -1 \\ 0 & 3 & \mid & -6 \\ 0 & -5 & \mid & 10 \end{bmatrix} \xrightarrow{L_2(1/3),\; L_3' = L_3 + 5L_2} \begin{bmatrix} 1 & 2 & \mid & -1 \\ 0 & 1 & \mid & -2 \\ 0 & 0 & \mid & 0 \end{bmatrix}.$$
Da 2ª linha, $a_2 = -2$; substituindo na 1ª linha, $a_1 + 2(-2) = -1 \implies \mathbf{a_1 = 3,\, a_2 = -2}$.

### Exemplo 2 — Colinearidade de 3 pontos com parâmetros
Para que valores de $a$ e $b$ os pontos $A(1, 2, -1)$, $B(3, 0, 3)$ e $C(a, b, 7)$ são colineares?
1. Calculamos $\overrightarrow{AB} = B - A = (2, -2, 4)$ e $\overrightarrow{AC} = C - A = (a - 1,\; b - 2,\; 8)$.
2. Impondo $\overrightarrow{AC} = k\,\overrightarrow{AB}$: pela 3ª coordenada, $8 = 4k \implies k = 2$.
3. Logo: $a - 1 = 2(2) \implies \mathbf{a = 5}$ e $b - 2 = 2(-2) \implies \mathbf{b = -2}$.

---

## 3. Exercícios (`D03-E01` a `D03-E06`)

### `D03-E01` *(Reprodução do modelo — Combinação linear no $\mathbb{R}^2$)*
Dados $\vec{u} = (2, -3)$, $\vec{v} = (-1, 4)$ e $\vec{w} = (7, -13)$, determine os escalares:  
**(a)** $k_1$  
**(b)** $k_2$  
tais que $\vec{w} = k_1\vec{u} + k_2\vec{v}$.

---

### `D03-E02` *(Técnica central — Sistema $3\times 2$ por escalonamento)*
Encontre os números reais:  
**(a)** $a_1$  
**(b)** $a_2$  
tais que $\vec{w} = a_1\vec{v}_1 + a_2\vec{v}_2$, sendo $\vec{v}_1 = (1, -2, 1)$, $\vec{v}_2 = (2, 1, -3)$ e $\vec{w} = (-1, -8, 9)$.

---

### `D03-E03` *(Caça ao Erro — Verificação incompleta de paralelismo)*
Um estudante afirmou que $\vec{u} = (4, -2, 6)$ e $\vec{v} = (6, -3, 8)$ são paralelos porque verificou apenas $\frac{4}{6} = \frac{-2}{-3} = \frac{2}{3}$.  
**(a)** Classifique corretamente $\vec{u}$ e $\vec{v}$ (`Paralelos` ou `Nao paralelos`).  
Determine os valores exatos de **(b)** $a$ e **(c)** $b$ para que o vetor $\vec{w} = (6, a, b)$ seja paralelo a $\vec{u} = (4, -2, 6)$.

---

### `D03-E04` *(Variação controlada com pistas — Colinearidade de 3 pontos)*
Verifique se são colineares (`Sao colineares` ou `Nao sao colineares`) os pontos:  
**(a)** $A(-1, -5, 0)$, $B(2, 1, 3)$ e $C(-2, -7, -1)$  
**(b)** $P(2, 1, -1)$, $Q(3, -1, 0)$ e $R(1, 0, 4)$

*Pistas:* Calcule dois vetores partindo do primeiro ponto ($\overrightarrow{AB}$ e $\overrightarrow{AC}$ em **(a)**; $\overrightarrow{PQ}$ e $\overrightarrow{PR}$ em **(b)**) e teste todas as três coordenadas para proporcionalidade.

---

### `D03-E05` *(Variação controlada com pistas — Parâmetros de colinearidade)*
Calcule os valores reais de **(a)** $a$ e **(b)** $b$ de modo que os pontos $A(2, -1, 3)$, $B(4, 3, -1)$ e $C(a, b, -7)$ sejam colineares.

*Pistas:* Monte $\overrightarrow{AB} = B - A$ e $\overrightarrow{AC} = C - A$; use a terceira coordenada (numérica em ambos) para achar o fator $k$ em $\overrightarrow{AC} = k\,\overrightarrow{AB}$.

---

### `D03-E06` *(Resolução independente — Combinação linear de 3 vetores no $\mathbb{R}^3$)*
Escreva $\vec{w} = (1, 4, 8)$ como combinação linear $\vec{w} = c_1\vec{v}_1 + c_2\vec{v}_2 + c_3\vec{v}_3$ dos vetores $\vec{v}_1 = (1, 0, 1)$, $\vec{v}_2 = (0, 1, 2)$ e $\vec{v}_3 = (1, -1, 0)$ via escalonamento, e informe a terna ordenada $(c_1, c_2, c_3)$.

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `D03-C01` *(Combinação linear no $\mathbb{R}^3$)*
Determine **(a)** $a_1$ e **(b)** $a_2$ tais que $(5, -5, 2) = a_1(1, -2, 1) + a_2(2, 1, -1)$.

### `D03-C02` *(Paralelismo com dois parâmetros)*
Determine os valores exatos de **(a)** $m$ e **(b)** $n$ para que os vetores $\vec{u} = (6, -4, 10)$ e $\vec{v} = (9, m, n)$ sejam paralelos.

### `D03-C03` *(Colinearidade com coordenadas desconhecidas)*
Calcule **(a)** $x$ e **(b)** $y$ de modo que os pontos $A(1, 3, -2)$, $B(3, -1, 2)$ e $C(x, y, 8)$ sejam colineares.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `D04` (`Produto Escalar, Módulo Analítico, Distância e Versor`):** somente após autocorreção de `D03-E01..E06` **e** **100% (3/3)** na Checagem Independente `D03-C01..C03` sem consulta.
- **Recuperação direcionada (1ª falha):** verificar se a falha foi erro de sinal/operação elementar no escalonamento ou esquecimento da 3ª coordenada no teste de paralelismo; revisar os Exemplos 1 e 2 e aplicar a variante `V2`.
- **Após 2 tentativas malsucedidas:** investigar os dois pré-requisitos do DAG: se o erro foi em `B - A` ou coordenadas, recuar para **`D02`**; se o erro foi em operações `L_j' = L_j + L_i(\alpha)` ao resolver o sistema linear, recuar para **`C03`**.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Vetores.pdf` p. 37–38, 43–45, 49 (combinação linear, paralelismo de vetores e pontos colineares).
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 101–104 (Cap. 2 — exemplos de paralelismo e colinearidade).
- `[DOC]` `Mat_Vet_L6.pdf` p. 2 (Ex. 7–8 e Ex. 13–16 — $k_1, k_2$, $a_1, a_2$, paralelismo e colinearidade de 3 pontos).
- Gabarito e especificação de validação: [D03_gabarito.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/gabaritos/D03_gabarito.md) e [casos_D03.json](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/testes/casos_D03.json).
