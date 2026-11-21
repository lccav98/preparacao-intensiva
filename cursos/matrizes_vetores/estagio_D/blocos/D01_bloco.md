# Bloco `D01` — Segmento Orientado, Vetor, Módulo, Versor e Ângulos Geométricos

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio D — Vetores em $\mathbb{R}^2/\mathbb{R}^3$, Produtos, Áreas e Volumes / **`D01`** |
| **Micro-habilidade foco** | Distinguir segmento orientado de vetor, operar soma/diferença e multiplicação por escalar geometricamente, interpretar módulo $|\vec{v}|$ e versor $\hat{v}$, e determinar o ângulo $\theta \in [0,\pi]$ entre vetores a partir de origem comum. |
| **Pré-requisitos** | `A01` *(Base conceitual de organização e leitura de dados)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Prática (`D01-E01`–`D01-E06`, 18 min):** `11 min` resol. \| `4 min` corr. \| `3 min` recup.; **Checagem (`D01-C01`–`D01-C03`, 12 min):** `8 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **100% geométrico (sem coordenadas cartesianas $(x,y,z)$ e sem produto escalar/vetorial).** Utilize apenas regras gráficas (triângulo/paralelogramo), módulo $|\vec{v}|$, versor $\hat{v}$ e ângulos em $[0^\circ, 180^\circ]$ com frações e radicais exatos. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`D01-E01`–`D01-E06`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Protocolo:** `PREP-MV-D01-V__-T__` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 6` | **Após autocorreção:** `___ / 6`
- **Checagem independente (sem gabarito) (`D01-C01`–`D01-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Segmento orientado vs. vetor:** um segmento orientado $(A, B)$ tem origem $A$ e extremidade $B$ fixas no espaço. Um **vetor** $\vec{v}$ representa o conjunto de todos os segmentos orientados equipolentes (mesmo **módulo**, mesma **direção** e mesmo **sentido**), podendo ser transladado paralelamente para qualquer ponto de origem.
2. **Módulo e vetor nulo:** o módulo (comprimento) de $\vec{v}$ é indicado com **barras simples**: $|\vec{v}| \ge 0$. O **vetor nulo** $\vec{0}$ tem módulo $0$ e não possui direção nem sentido definidos.
3. **Vetor oposto e multiplicação por escalar:**
   - $-\vec{v}$ tem o mesmo módulo e a mesma direção de $\vec{v}$, mas **sentido contrário**.
   - Para todo escalar real $k \neq 0$, $|k\vec{v}| = |k|\,|\vec{v}|$. Se $k > 0$, $k\vec{v}$ mantém o sentido de $\vec{v}$; se $k < 0$, inverte o sentido.
4. **Versor ($\hat{v}$):** todo vetor não nulo $\vec{v}$ possui um vetor unitário de mesma direção e sentido dado por:
   $$\hat{v} = \frac{\vec{v}}{|\vec{v}|}, \qquad \text{com } |\hat{v}| = 1.$$
5. **Soma e diferença geométrica:**
   - **Regra do triângulo:** encaixar a origem de $\vec{v}$ na extremidade de $\vec{u}$; então $\vec{u}+\vec{v}$ vai da origem de $\vec{u}$ até a extremidade de $\vec{v}$ ($\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}$).
   - **Regra do paralelogramo:** colocar $\vec{u}$ e $\vec{v}$ com a **mesma origem**; a diagonal principal que parte da origem comum é $\vec{u}+\vec{v}$, e a outra diagonal é $\vec{u}-\vec{v}$ (ligando a extremidade de $\vec{v}$ à extremidade de $\vec{u}$).
6. **Ângulo entre dois vetores ($\theta \in [0^\circ, 180^\circ]$):** os dois vetores **devem partir da mesma origem**!
   - Inverter **um** dos vetores transforma o ângulo no suplementar: $\text{ang}(\vec{u}, -\vec{v}) = 180^\circ - \theta$.
   - Inverter **ambos** os vetores ou multiplicar ambos por escalares positivos preserva o ângulo: $\text{ang}(-\vec{u}, -\vec{v}) = \theta$ e $\text{ang}(2\vec{u}, 3\vec{v}) = \theta$.

---

## 2. Exemplos Guiados

### Exemplo 1 — Ângulos ao inverter sentidos e multiplicar por escalares
Sabendo que o ângulo entre $\vec{a}$ e $\vec{b}$ é $\theta = 70^\circ$:
- **Entre $\vec{a}$ e $-\vec{b}$:** apenas $\vec{b}$ teve o sentido invertido $\Rightarrow 180^\circ - 70^\circ = \mathbf{110^\circ}$.
- **Entre $-2\vec{a}$ e $5\vec{b}$:** $-2 < 0$ inverte $\vec{a}$, enquanto $5 > 0$ preserva o sentido de $\vec{b}$ $\Rightarrow 180^\circ - 70^\circ = \mathbf{110^\circ}$.
- **Entre $-3\vec{a}$ e $-\vec{b}$:** ambos inverteram de sentido, logo a abertura entre as semirretas permanece $\mathbf{70^\circ}$.

### Exemplo 2 — Módulo, versor e regra do triângulo sem coordenadas
Considere um triângulo retângulo $ABC$, reto em $A$, com $|\overrightarrow{AB}| = 3$ e $|\overrightarrow{AC}| = 4$.
1. Como $\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}$, tem-se $|\overrightarrow{AB} + \overrightarrow{BC}| = |\overrightarrow{AC}| = \mathbf{4}$.
2. O vetor $\overrightarrow{BC} = \overrightarrow{AC} - \overrightarrow{AB}$ representa a hipotenusa; pelo teorema de Pitágoras, $|\overrightarrow{BC}| = \sqrt{3^2 + 4^2} = \mathbf{5}$.
3. Para o vetor $\vec{w} = -2\overrightarrow{BC}$, seu módulo é $|-2\overrightarrow{BC}| = |-2|\cdot 5 = \mathbf{10}$, e o módulo de seu versor $\hat{w}$ é sempre $|\hat{w}| = \mathbf{1}$.

---

## 3. Exercícios (`D01-E01` a `D01-E06`)

### `D01-E01` *(Reprodução do modelo — Ângulos por inversão e escala)*
Sabendo que o ângulo entre os vetores não nulos $\vec{u}$ e $\vec{v}$ é de $50^\circ$, determine o ângulo (em graus) formado pelos vetores:  
**(a)** $\vec{u}$ e $-\vec{v}$  
**(b)** $-\vec{u}$ e $\vec{v}$  
**(c)** $-\vec{u}$ e $-\vec{v}$  
**(d)** $3\vec{u}$ e $5\vec{v}$

---

### `D01-E02` *(Cálculo direto — Módulo de múltiplos e do versor)*
Dado um vetor $\vec{v}$ tal que $|\vec{v}| = 6$, determine os valores exatos de:  
**(a)** $|-4\vec{v}|$  
**(b)** $\left|\frac{1}{2}\vec{v}\right|$  
**(c)** $|\hat{v}|$  
**(d)** $|5\hat{v}|$

---

### `D01-E03` *(Caça ao Erro — Origem comum na medição de ângulos)*
Em um triângulo $ABC$, o ângulo interno no vértice $B$ mede $40^\circ$. Um estudante afirmou que o ângulo entre os vetores $\overrightarrow{AB}$ e $\overrightarrow{BC}$ também é $40^\circ$.  
Identifique o erro conceitual do estudante (justificando com translação para origem comum) e determine os ângulos corretos (em graus) entre:  
**(a)** $\overrightarrow{AB}$ e $\overrightarrow{BC}$  
**(b)** $\overrightarrow{BA}$ e $\overrightarrow{BC}$

---

### `D01-E04` *(Variação controlada com pistas — Regra do paralelogramo ortogonal)*
Dois vetores $\vec{u}$ e $\vec{v}$ são ortogonais ($\theta = 90^\circ$) e têm módulos $|\vec{u}| = 5$ e $|\vec{v}| = 12$. Determine:  
**(a)** $|\vec{u} + \vec{v}|$  
**(b)** $|\vec{u} - \vec{v}|$

*Pistas:* Coloque $\vec{u}$ e $\vec{v}$ com a mesma origem. O paralelogramo formado pelos dois vetores é um retângulo cujas diagonais medem $|\vec{u}+\vec{v}|$ e $|\vec{u}-\vec{v}|$.

---

### `D01-E05` *(Variação controlada com pistas — Simplificação vetorial e sentido)*
Considere a expressão vetorial $\vec{w} = 2(\vec{a} - \vec{b}) - (3\vec{a} - 4\vec{b}) + \vec{a}$, em que $\vec{b}$ é um vetor não nulo de módulo $|\vec{b}| = 7$. Simplifique $\vec{w}$ na forma $k\vec{b}$ e informe:  
**(a)** O coeficiente escalar $k$  
**(b)** O módulo $|\vec{w}|$  
**(c)** O ângulo (em graus) entre $\vec{w}$ e $-\vec{b}$

*Pistas:* Distribua os escalares antes de agrupar termos semelhantes em $\vec{a}$ e $\vec{b}$; depois compare o sinal de $k$ com o de $-1$ em $-\vec{b}$.

---

### `D01-E06` *(Resolução independente — Geometria do losango)*
Dois vetores $\vec{a}$ e $\vec{b}$ satisfazem $|\vec{a}| = |\vec{b}| = 8$ e formam entre si um ângulo de $60^\circ$. Usando a regra do paralelogramo a partir de uma origem comum, determine:  
**(a)** O ângulo (em graus) entre os vetores diagonais $\vec{a}+\vec{b}$ e $\vec{a}-\vec{b}$  
**(b)** O módulo $|\vec{a} - \vec{b}|$

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `D01-C01` *(Ângulos entre múltiplos positivos e negativos)*
Sabendo que o ângulo entre $\vec{p}$ e $\vec{q}$ é de $115^\circ$, determine o ângulo (em graus) entre:  
**(a)** $\vec{p}$ e $-\vec{q}$  
**(b)** $-2\vec{p}$ e $3\vec{q}$  
**(c)** $-4\vec{p}$ e $-\vec{q}$

### `D01-C02` *(Módulo, versor e equação modular $|k\vec{u}| = c$)*
Seja $\vec{u}$ um vetor não nulo com $|\vec{u}| = 9$ e versor $\hat{u}$. Determine:  
**(a)** $\left|-\frac{2}{3}\vec{u}\right|$  
**(b)** $|\hat{u}|$  
**(c)** Todos os valores reais de $k$ tais que $|k\vec{u}| = 3$

### `D01-C03` *(Triângulo equilátero com soma, diferença e ângulo)*
Em um triângulo equilátero $ABC$ cujo lado mede $6$, determine:  
**(a)** $|\overrightarrow{AB} + \overrightarrow{BC}|$  
**(b)** O ângulo (em graus) entre $\overrightarrow{AB}$ e $\overrightarrow{BC}$  
**(c)** $|\overrightarrow{AB} - \overrightarrow{AC}|$

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `D02` (`Vetores no R^2 e R^3, Base Canônica e AB = B - A`):** somente após autocorreção de `D01-E01..E06` **e** **100% (3/3)** na Checagem Independente `D01-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** identificar se a falha ocorreu em inversão de sentido ($180^\circ - \theta$), propriedade $|k\vec{v}| = |k||\vec{v}|$ ou exigência de origem comum para medir ângulos; refazer o desenho da regra do paralelogramo no papel e aplicar a variante `V2`.
- **Após 2 tentativas malsucedidas:** interromper repetições de `D01`; revisar o conceito de grandeza vetorial vs. escalar e desenhar 3 pares de segmentos orientados equipolentes em papel quadriculado antes de retomar o bloco.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Vetores.pdf` p. 4–28 (segmento orientado, equipolência, vetor, módulo `|\vec{v}|`, versor `\hat{v}`, adição/diferença geométrica, multiplicação por escalar e ângulo entre vetores).
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 78–91 (Cap. 1 do caderno manuscrito — definições geométricas e propriedades do paralelogramo).
- `[DOC]` `Mat_Vet_L6.pdf` p. 1–2 (Ex. 1–3 e Ex. 17 — operações gráficas e ângulos suplementares).
- Gabarito e especificação de validação: [D01_gabarito.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/gabaritos/D01_gabarito.md) e [casos_D01.json](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/testes/casos_D01.json).
