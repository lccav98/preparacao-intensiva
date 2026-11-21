# Bloco `D09` — Produto Misto, Coplanaridade e Volumes (Paralelepípedo e Tetraedro)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio D — Vetores em $\mathbb{R}^2/\mathbb{R}^3$, Produtos, Áreas e Volumes / **`D09`** |
| **Micro-habilidade foco** | Calcular o produto misto $(\vec{u},\vec{v},\vec{w}) = \vec{u}\cdot(\vec{v}\times\vec{w})$ via desenvolvimento pela 1ª linha, testar coplanaridade de 3 vetores e de 4 pontos, calcular volumes de paralelepípedo ($|\det|$) e tetraedro ($\frac{1}{6}|\det|$), e resolver $|\det|=V$ encontrando ambas as soluções. |
| **Pré-requisitos** | `D07` *(Produto vetorial $\vec{u}\times\vec{v}$)*; `B01` *(Determinante $3\times 3$ pela 1ª linha)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Prática (`D09-E01`–`D09-E06`, 24 min):** `15 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`D09-C01`–`D09-C03`, 16 min):** `12 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Calcule todo determinante $3\times 3$ exclusivamente por desenvolvimento na 1ª linha** (matriz de sinais $+ - +$) ou por $\vec{u}\cdot(\vec{v}\times\vec{w})$. Nunca omita o valor absoluto $|\det|$ em equações de volume. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`D09-E01`–`D09-E06`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Protocolo:** `PREP-MV-D09-V__-T__` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 6` | **Após autocorreção:** `___ / 6`
- **Checagem independente (sem gabarito) (`D09-C01`–`D09-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Produto misto:** dados $\vec{u} = (x_1, y_1, z_1)$, $\vec{v} = (x_2, y_2, z_2)$ e $\vec{w} = (x_3, y_3, z_3)$ no $\mathbb{R}^3$, define-se o produto misto $(\vec{u}, \vec{v}, \vec{w}) \in \mathbb{R}$ por:
   $$(\vec{u}, \vec{v}, \vec{w}) = \vec{u}\cdot(\vec{v}\times\vec{w}) = \det\begin{bmatrix} x_1 & y_1 & z_1 \\ x_2 & y_2 & z_2 \\ x_3 & y_3 & z_3 \end{bmatrix}.$$
   Calcule o determinante $3\times 3$ desenvolvendo pela **1ª linha** com sinais $+ - +$ (ou calculando $\vec{v}\times\vec{w}$ e fazendo produto escalar com $\vec{u}$).
2. **Propriedades de permutação:** permutações cíclicas preservam o valor ($(\vec{u},\vec{v},\vec{w}) = (\vec{v},\vec{w},\vec{u}) = (\vec{w},\vec{u},\vec{v})$); trocar dois vetores de lugar inverte o sinal.
3. **Coplanaridade:**
   - **3 vetores** $\vec{u}, \vec{v}, \vec{w}$ são coplanares $\iff (\vec{u}, \vec{v}, \vec{w}) = 0$.
   - **4 pontos** $A, B, C, D$ são coplanares $\iff$ os 3 vetores partindo do mesmo vértice são coplanares, isto é, $(\overrightarrow{AB}, \overrightarrow{AC}, \overrightarrow{AD}) = 0$.
4. **Volumes:**
   - **Paralelepípedo** gerado por $\vec{u}, \vec{v}, \vec{w}$:
     $$V_{\text{paral}} = \left|(\vec{u}, \vec{v}, \vec{w})\right|.$$
   - **Tetraedro** de vértices $A, B, C, D$ (equivale a $\frac{1}{6}$ do paralelepípedo formado pelas 3 arestas saindo de $A$):
     $$V_{\text{tetra}} = \frac{1}{6}\left|(\overrightarrow{AB}, \overrightarrow{AC}, \overrightarrow{AD})\right|.$$
5. **Armadilha clássica nas equações de volume ($|\det| = V$):** como o volume usa **módulo**, a equação $|E(m)| = V$ ($V > 0$) **sempre se desdobra em dois casos**:
   $$E(m) = V \quad \text{ou} \quad E(m) = -V,$$
   gerando **2 soluções reais** para o parâmetro!

---

## 2. Exemplos Guiados

### Exemplo 1 — Produto misto pela 1ª linha e teste de coplanaridade
Para $\vec{u} = (1, 2, -1)$, $\vec{v} = (3, 0, 2)$ e $\vec{w} = (-1, 1, 4)$:
$$(\vec{u},\vec{v},\vec{w}) = \begin{vmatrix} 1 & 2 & -1 \\ 3 & 0 & 2 \\ -1 & 1 & 4 \end{vmatrix} = 1\begin{vmatrix} 0 & 2 \\ 1 & 4 \end{vmatrix} - 2\begin{vmatrix} 3 & 2 \\ -1 & 4 \end{vmatrix} + (-1)\begin{vmatrix} 3 & 0 \\ -1 & 1 \end{vmatrix} = 1(-2) - 2(14) - 1(3) = -33.$$
Como $-33 \neq 0$, os vetores **não são coplanares** e determinam um paralelepípedo de volume $V_{\text{paral}} = |-33| = \mathbf{33}$.

### Exemplo 2 — Volume do tetraedro $ABCD$
Dados $A(1, 0, 1)$, $B(3, 1, 1)$, $C(1, 2, 2)$ e $D(2, 1, 5)$:
1. Arestas partindo de $A$: $\overrightarrow{AB} = (2, 1, 0)$, $\overrightarrow{AC} = (0, 2, 1)$ e $\overrightarrow{AD} = (1, 1, 4)$.
2. $(\overrightarrow{AB},\overrightarrow{AC},\overrightarrow{AD}) = 2(8 - 1) - 1(0 - 1) + 0 = 14 + 1 = 15$.
3. $V_{\text{tetra}} = \frac{|15|}{6} = \mathbf{\frac{5}{2}}$.

---

## 3. Exercícios (`D09-E01` a `D09-E06`)

### `D09-E01` *(Reprodução do modelo — Produto misto e volume do paralelepípedo)*
Dados os vetores $\vec{u} = (2, -1, 1)$, $\vec{v} = (1, 2, -1)$ e $\vec{w} = (-1, 3, 2)$, calcule:  
**(a)** O produto misto $(\vec{u}, \vec{v}, \vec{w})$  
**(b)** O volume do paralelepípedo definido por $\vec{u}, \vec{v}, \vec{w}$

---

### `D09-E02` *(Técnica central — Coplanaridade de 3 vetores)*
Verifique se são coplanares (`Sao coplanares` ou `Nao sao coplanares`) os vetores:  
**(a)** $\vec{u} = (2, -1, 3)$, $\vec{v} = (1, 2, -1)$ e $\vec{w} = (4, 3, 1)$  
**(b)** $\vec{u} = (1, 2, -1)$, $\vec{v} = (0, 1, 3)$ e $\vec{w} = (2, -1, 1)$

---

### `D09-E03` *(Caça ao Erro — As 2 soluções de $|\det| = V$)*
Os vetores $\vec{a} = (1, -1, 2)$, $\vec{b} = (2, 1, -1)$ e $\vec{c} = (m, 2, 1)$ determinam um paralelepípedo de volume $18$. Um estudante calculou o produto misto, obteve $13 - m$, igualou $13 - m = 18$ e respondeu apenas $m = -5$.  
Explique o erro do estudante e determine **todos** os valores reais de $m$ que satisfazem a condição.

---

### `D09-E04` *(Variação controlada com pistas — Coplanaridade de 4 pontos)*
Considere os quatro pontos $A(1, 0, 2)$, $B(2, 1, 0)$, $C(0, 2, 3)$ e $D(3, 1, -1)$. Determine:  
**(a)** O valor absoluto do produto misto $\left|(\overrightarrow{AB}, \overrightarrow{AC}, \overrightarrow{AD})\right|$  
**(b)** A classificação dos quatro pontos (`Sao coplanares` ou `Nao sao coplanares`)

*Pistas:* Construa os três vetores $\overrightarrow{AB} = B - A$, $\overrightarrow{AC} = C - A$ e $\overrightarrow{AD} = D - A$ partindo do mesmo ponto $A$.

---

### `D09-E05` *(Variação controlada com pistas — Volume do tetraedro)*
Calcule o volume exato do tetraedro $ABCD$ cujos vértices são $A(1, 0, 0)$, $B(0, 2, 0)$, $C(0, 0, 3)$ e $D(2, 2, 3)$.

*Pistas:* Monte $\overrightarrow{AB}, \overrightarrow{AC}, \overrightarrow{AD}$, desenvolva o determinante pela 1ª linha e multiplique o módulo do resultado por $\frac{1}{6}$.

---

### `D09-E06` *(Resolução independente — Tetraedro com parâmetro e 2 soluções)*
Determine todos os valores reais de $k$ para que o tetraedro de vértices $A(0, 0, 0)$, $B(2, 1, 0)$, $C(1, 3, 1)$ e $D(0, 1, k)$ tenha volume igual a $\frac{5}{3}$.

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `D09-C01` *(Volume do tetraedro e coplanaridade de 4 pontos)*
Dados os pontos $P(1, 2, -1)$, $Q(2, 0, 1)$, $R(0, 1, 2)$ e $S(3, -1, 2)$, determine:  
**(a)** O volume exato do tetraedro $PQRS$  
**(b)** Se os pontos $P, Q, R, S$ são coplanares (`Sao coplanares` ou `Nao sao coplanares`)

### `D09-C02` *(Paralelepípedo com parâmetro — 2 soluções)*
Determine todos os valores reais de $m$ para que os vetores $\vec{u} = (2, -1, 1)$, $\vec{v} = (1, 3, -2)$ e $\vec{w} = (m, 1, m + 1)$ determinem um paralelepípedo de volume igual a $20$.

### `D09-C03` *(Altura do tetraedro relativa à base)*
Para o tetraedro de vértices $A(1, 1, 0)$, $B(2, 3, 1)$, $C(0, 2, 2)$ e $D(3, 1, 3)$, calcule a altura exata $h$ relativa à base $ABC$, sabendo que $h = \frac{|(\overrightarrow{AB}, \overrightarrow{AC}, \overrightarrow{AD})|}{|\overrightarrow{AB}\times\overrightarrow{AC}|}$.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `D10` (`Revisão Cumulativa do Estágio D — Simulado P2`):** somente após autocorreção de `D09-E01..E06` **e** **100% (3/3)** na Checagem Independente `D09-C01..C03` sem consulta.
- **Recuperação direcionada (1ª falha):** verificar se houve esquecimento do sinal negativo no cofator $(1,2)$ da 1ª linha, esquecimento de dividir por $6$ no tetraedro, ou omissão da segunda solução em $|\det| = V$; revisar os Exemplos 1 e 2 e aplicar a variante `V2`.
- **Após 2 tentativas malsucedidas:** recuar para **`B01`** (se errou o desenvolvimento do determinante $3\times 3$ pela 1ª linha) ou **`D07`** (se confundiu produto vetorial com produto misto).

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Vetores.pdf` p. 70–75 (produto misto $(\vec{u},\vec{v},\vec{w})$, propriedades, coplanaridade e volume do paralelepípedo).
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 120–123 (Cap. 3 — exemplos de produto misto e volume do tetraedro).
- `[DOC]` `Mat_Vet_L7.pdf` p. 2 (Ex. 21, 22, 24 e 25 — coplanaridade de 3 vetores e 4 pontos, volume 42 com 2 soluções para $m$, volume do tetraedro).
- Gabarito e especificação de validação: [D09_gabarito.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/gabaritos/D09_gabarito.md) e [casos_D09.json](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/testes/casos_D09.json).
