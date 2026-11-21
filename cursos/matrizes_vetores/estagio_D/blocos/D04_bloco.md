# Bloco `D04` — Produto Escalar, Módulo Analítico, Distância e Versor

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio D — Vetores em $\mathbb{R}^2/\mathbb{R}^3$, Produtos, Áreas e Volumes / **`D04`** |
| **Micro-habilidade foco** | Calcular o produto escalar $\vec{u}\cdot\vec{v}$, o módulo $|\vec{v}| = \sqrt{\vec{v}\cdot\vec{v}}$, a distância entre pontos $d(A,B) = |\overrightarrow{AB}|$ e o versor $\hat{v} = \vec{v}/|\vec{v}|$, além de resolver equações quadráticas em parâmetros sem omitir a raiz negativa ($\pm$). |
| **Pré-requisitos** | `D02` *(Coordenadas no $\mathbb{R}^2/\mathbb{R}^3$ e $\overrightarrow{AB} = B - A$)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Prática (`D04-E01`–`D04-E06`, 20 min):** `13 min` resol. \| `4 min` corr. \| `3 min` recup.; **Checagem (`D04-C01`–`D04-C03`, 14 min):** `10 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Foco exclusivo em produto escalar, norma e versor.** Ainda sem ângulo/cossenos diretores (`D05`), projeção (`D06`) ou produto vetorial (`D07`). Mantenha todo resultado em frações irredutíveis e radicais exatos. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`D04-E01`–`D04-E06`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Protocolo:** `PREP-MV-D04-V__-T__` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 6` | **Após autocorreção:** `___ / 6`
- **Checagem independente (sem gabarito) (`D04-C01`–`D04-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Produto escalar (ou produto interno):** para $\vec{u} = (x_1, y_1, z_1)$ e $\vec{v} = (x_2, y_2, z_2)$ no $\mathbb{R}^3$ (e analogamente sem $z$ no $\mathbb{R}^2$):
   $$\vec{u}\cdot\vec{v} = x_1x_2 + y_1y_2 + z_1z_2 \in \mathbb{R}.$$
   **Atenção:** o produto escalar retorna um **número real**, nunca um vetor!
2. **Propriedades algébricas do produto escalar:**
   - Comutatividade: $\vec{u}\cdot\vec{v} = \vec{v}\cdot\vec{u}$.
   - Distributividade: $\vec{u}\cdot(\vec{v} + \vec{w}) = \vec{u}\cdot\vec{v} + \vec{u}\cdot\vec{w}$.
   - Escalar: $(k\vec{u})\cdot\vec{v} = k(\vec{u}\cdot\vec{v}) = \vec{u}\cdot(k\vec{v})$.
   - Positividade: $\vec{v}\cdot\vec{v} = x^2 + y^2 + z^2 = |\vec{v}|^2 \ge 0$.
3. **Módulo analítico e distância entre dois pontos:**
   $$|\vec{v}| = \sqrt{\vec{v}\cdot\vec{v}} = \sqrt{x^2 + y^2 + z^2}, \qquad d(A,B) = |\overrightarrow{AB}| = \sqrt{(x_B-x_A)^2 + (y_B-y_A)^2 + (z_B-z_A)^2}.$$
4. **Versor de um vetor não nulo:**
   $$\hat{v} = \frac{\vec{v}}{|\vec{v}|} = \left(\frac{x}{|\vec{v}|},\; \frac{y}{|\vec{v}|},\; \frac{z}{|\vec{v}|}\right).$$
5. **Cuidado com equações quadráticas:** ao resolver $|\vec{v}| = c$ ou $\vec{v}\cdot\vec{v} = c^2$, lembre-se de que $x^2 = k$ ($k > 0$) gera **duas soluções** ($x = \pm\sqrt{k}$).

---

## 2. Exemplos Guiados

### Exemplo 1 — Produto escalar, módulo e versor
Dados $\vec{u} = (1, -2, 2)$ e $\vec{v} = (2, 3, -6)$:
1. $\vec{u}\cdot\vec{v} = 1(2) + (-2)(3) + 2(-6) = 2 - 6 - 12 = \mathbf{-16}$.
2. $|\vec{u}| = \sqrt{1^2 + (-2)^2 + 2^2} = \sqrt{9} = \mathbf{3}$ e $|\vec{v}| = \sqrt{4 + 9 + 36} = \mathbf{7}$.
3. Versor de $\vec{u}$: $\hat{u} = \frac{1}{3}(1, -2, 2) = \mathbf{\left(\frac{1}{3},\, -\frac{2}{3},\, \frac{2}{3}\right)}$.

### Exemplo 2 — Parâmetro para vetor unitário
Determine os valores de $m$ para que $\vec{v} = \left(m,\, \frac{1}{2},\, \frac{1}{2}\right)$ seja unitário ($|\vec{v}| = 1$):
$$|\vec{v}|^2 = 1^2 \implies m^2 + \frac{1}{4} + \frac{1}{4} = 1 \implies m^2 = \frac{1}{2} \implies \mathbf{m = -\frac{\sqrt{2}}{2} \text{ ou } m = \frac{\sqrt{2}}{2}}.$$

---

## 3. Exercícios (`D04-E01` a `D04-E06`)

### `D04-E01` *(Reprodução do modelo — Produto escalar, módulo e versor)*
Dados $\vec{u} = (2, -3, 6)$ e $\vec{v} = (-1, 4, 2)$, determine:  
**(a)** $\vec{u}\cdot\vec{v}$  
**(b)** $|\vec{u}|$  
**(c)** O versor $\hat{u}$

---

### `D04-E02` *(Técnica central — Distância entre pontos e versor de $\overrightarrow{AB}$)*
Dados os pontos $A(1, -1, 3)$ e $B(3, 0, 1)$, determine:  
**(a)** A distância $d(A, B) = |\overrightarrow{AB}|$  
**(b)** O versor $\widehat{AB}$

---

### `D04-E03` *(Caça ao Erro — Perda do sinal $\pm$ ao impor $|\vec{v}| = 1$)*
Ao buscar os valores reais de $n$ para que $\vec{v} = \left(n,\, \frac{1}{3},\, \frac{2}{3}\right)$ seja unitário, um estudante escreveu apenas $n = \frac{2}{3}$.  
Explique a omissão do estudante e determine **todos** os valores reais de $n$ que tornam $\vec{v}$ unitário.

---

### `D04-E04` *(Variação controlada com pistas — Equação com produto escalar)*
Dados os vetores $\vec{u} = (2, a, 1-a)$, $\vec{v} = (a, a+1, -1)$ e $\vec{w} = (1, a, 2)$, determine todos os valores reais de $a$ tais que:
$$\vec{u}\cdot\vec{v} = (\vec{u} + \vec{v})\cdot\vec{w}.$$

*Pistas:* Calcule $\vec{u}\cdot\vec{v}$ e $(\vec{u}+\vec{v})\cdot\vec{w}$ em função de $a$; iguale ambos para obter uma equação do 2º grau e encontre todas as raízes reais.

---

### `D04-E05` *(Variação controlada com pistas — Parâmetro no módulo de combinação linear)*
Dados os pontos $A(0, 1, 2)$, $B(0, 3, -2)$ e $C(1, 3, 0)$, determine todos os valores reais de $m$ para que o vetor $\vec{v} = m\overrightarrow{AC} + \overrightarrow{BC}$ tenha módulo $|\vec{v}| = \sqrt{29}$.

*Pistas:* Encontre primeiro $\overrightarrow{AC} = C - A$ e $\overrightarrow{BC} = C - B$; monte $\vec{v}$ em função de $m$ e resolva $|\vec{v}|^2 = 29$.

---

### `D04-E06` *(Resolução independente — Vetor paralelo com produto escalar fixado)*
Dado o vetor $\vec{u} = (2, -1, 2)$, determine:  
**(a)** O vetor $\vec{v}$, paralelo a $\vec{u}$, tal que $\vec{v}\cdot\vec{u} = -27$  
**(b)** O versor $\hat{u}$

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `D04-C01` *(Produto escalar, módulo e versor)*
Dados $\vec{p} = (4, -4, 2)$ e $\vec{q} = (1, 2, -2)$, calcule:  
**(a)** $\vec{p}\cdot\vec{q}$  
**(b)** $|\vec{p}|$  
**(c)** O versor $\hat{p}$

### `D04-C02` *(Parâmetro com módulo dado)*
Seja $\vec{v} = (m + 3)\hat{\imath} + (m - 1)\hat{\jmath} + 2\hat{k}$. Determine todos os valores reais de $m$ para que $|\vec{v}| = \sqrt{30}$.

### `D04-C03` *(Vetor colinear com condição escalar)*
Determine o vetor $\vec{v}$, colinear a $\vec{u} = (2, -3, 6)$, tal que $\vec{v}\cdot\vec{w} = -28$, sendo $\vec{w} = (1, 0, 2)$.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `D05` (`Ângulo entre Vetores, Ortogonalidade e Cossenos Diretores`):** somente após autocorreção de `D04-E01..E06` **e** **100% (3/3)** na Checagem Independente `D04-C01..C03` sem consulta.
- **Recuperação direcionada (1ª falha):** conferir se a falha foi sinal negativo na subtração $B - A$, erro aritmético em $\vec{u}\cdot\vec{v}$ ou esquecimento de raiz dupla ($\pm$) em $|\vec{v}|^2 = c^2$; revisar os Exemplos 1 e 2 e aplicar a variante `V2`.
- **Após 2 tentativas malsucedidas:** recuar para **`D02`** para reforçar operações com coordenadas, base canônica e regra $\overrightarrow{AB} = B - A$ (além de revisar equações quadráticas de `A02`).

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Vetores.pdf` p. 50–55 (produto escalar $\vec{u}\cdot\vec{v}$, módulo analítico $|\vec{v}|$, distância e versor $\hat{v}$).
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 105–109 (Cap. 3 — propriedades do produto escalar e exemplos).
- `[DOC]` `Mat_Vet_L7.pdf` p. 1 (Ex. 1–5 e Ex. 11–13 — cálculo de parâmetros em módulo e vetor paralelo com produto escalar).
- Gabarito e especificação de validação: [D04_gabarito.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/gabaritos/D04_gabarito.md) e [casos_D04.json](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/testes/casos_D04.json).
