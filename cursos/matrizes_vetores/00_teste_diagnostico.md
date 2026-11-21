# Teste Diagnóstico de Posicionamento — Matrizes e Vetores (`MAT121` — UTFPR-PG)

> **Finalidade:** Identificar os pré-requisitos já dominados pelo estudante em `MAT121 - Matrizes e Vetores` e posicioná-lo com segurança no bloco inicial adequado (Estágios `A` a `G`).  
> **Princípio de Avaliação:** O posicionamento baseia-se **nos pré-requisitos demonstrados** e no domínio exato com frações/radicais, nunca pela soma bruta de acertos.

---

## Instruções Gerais de Aplicação

1. **Modalidade:** Aplicação **sem consulta** e **sem calculadora gráfica ou software simbólico** (caneta e papel para rascunho/escalonamento).
2. **Tempos-alvo *(estimativas iniciais sujeitas à calibração)*:**
   - **Etapa 1 (Triagem Inicial Curta):** ~15 a 20 minutos.
   - **Etapa 2 (Sondagem Específica):** ~10 a 15 minutos por sondagem (máximo de 2 sondagens na mesma sessão).
3. **Regra contra chute:** Caso não reconheça um método ou notação, **marque `[ ] Não sei / Não estudei`** em vez de chutar.
4. **Convenções da disciplina:** Mantenha todas as respostas em **frações irredutíveis** e **radicais exatos** (`sqrt(...)`); **não** utilize Regra de Sarrus, Chió, Vandermonde, matriz adjunta ou Regra de Cramer.

---

## Regras Obrigatórias de Interrupção (`I1`–`I5`)

| Regra | Condição de Disparo | Ação Imediata |
|---|---|---|
| **`I1` — Dois erros seguidos na Triagem** | O estudante erra ou marca *"Não sei"* em **2 itens consecutivos** (`T_k` e `T_{k+1}`). | **Interromper imediatamente a Etapa 1** e aplicar apenas a Sondagem do estágio correspondente ao **primeiro item falho** (`T_k`). |
| **`I2` — Iniciante absoluto ou falha em `T1`** | O estudante declara nunca ter visto Matrizes **ou** erra / marca *"Não sei"* em **`T1`**. | **Interromper a Etapa 1.** Se nunca estudou Matrizes, posicionar em **`A01`**; caso contrário, aplicar somente a Sondagem **`S-A`**. |
| **`I3` — Travamento por item (> 3,5 min)** | O estudante trava sem progredir por mais de 3,5 minutos em um item da Triagem. | Pular o item como *"Não demonstrado"* e aplicar `I1`/`I2` normalmente. |
| **`I4` — Falha no item-âncora da Sondagem** | Na Etapa 2, erra o **item 1 (`*-01`, item-âncora)** da Sondagem `S-X`. | **Interromper a Sondagem `S-X`** e posicionar no bloco inicial do estágio `X` (ou no pré-requisito sinalizado). |
| **`I5` — Limite de Sondagens** | Lacunas em múltiplos estágios. | Aplicar **no máximo 2 sondagens** na mesma sessão e posicionar pelo **menor pré-requisito ainda não demonstrado**. |

---

## Etapa 1 — Triagem Inicial Curta (`T1` a `T6`)

### `T1` — Estágio A: Produto e Transposição de Matrizes
Dadas $A = \begin{bmatrix} 2 & -1 \\ 0 & 3 \end{bmatrix}$ e $B = \begin{bmatrix} 1 & 4 \\ -2 & 1 \end{bmatrix}$:  
**(a)** Calcule $(A \cdot B)^T$.  
**(b)** Calcule $D = A + A^T$ e classifique $D$ quanto à simetria.  
`[ ] Não sei / Não estudei`

---

### `T2` — Estágio B: Determinante e Condição de Singularidade
Considere a matriz $M = \begin{bmatrix} 1 & 2 & 0 \\ -1 & 3 & 1 \\ 2 & 0 & k \end{bmatrix}$:  
**(a)** Para qual valor real exato de $k$ a matriz $M$ é **singular** (não admite inversa)?  
**(b)** Para $k = 1$, qual é o valor de $\det(M)$?  
`[ ] Não sei / Não estudei`

---

### `T3` — Estágio C: Sistemas Lineares e Característica (`C_A, C_V`)
Dado o sistema linear:
$$\begin{cases} x + y + z = 6 \\ 2x + 2y + 2z = 12 \\ x - y + z = 2 \end{cases}$$
Escalone a matriz ampliada até a forma de escada e informe:  
**(a)** As características $C_A$, $C_V$, o grau de liberdade $g$ e a classificação (`SPD`, `SPI` ou `SI`).  
**(b)** A expressão geral da solução $(x, y, z)$ usando $z$ como variável arbitrária.  
`[ ] Não sei / Não estudei`

---

### `T4` — Estágio D: Produto Escalar e Produto Vetorial
Dados $\vec{u} = (2, -1, 2)$ e $\vec{v} = (1, 2, -2)$ no $\mathbb{R}^3$:  
**(a)** Calcule $\vec{u} \cdot \vec{v}$ e diga se os vetores são ortogonais.  
**(b)** Calcule $\vec{u} \times \vec{v}$ e a área exata do paralelogramo gerado por $\vec{u}$ e $\vec{v}$.  
`[ ] Não sei / Não estudei`

---

### `T5` — Estágio E: Plano e Distância Ponto-Plano
Considere o plano $\pi: 2x - y + 2z - 6 = 0$ e o ponto $P_0(1, 3, -1)$:  
**(a)** Escreva um vetor normal $\vec{n}$ a $\pi$ e verifique se $P_0 \in \pi$.  
**(b)** Calcule a distância exata $d(P_0, \pi)$.  
`[ ] Não sei / Não estudei`

---

### `T6` — Estágio F: Reconhecimento e Translação de Cônica
Dada a equação $9x^2 - 4y^2 - 54x + 8y + 113 = 0$ no plano $\mathbb{R}^2$:  
Complete os quadrados para obter a **equação reduzida**, identifique a cônica, informe seu **centro** e calcule sua **excentricidade** exata.  
`[ ] Não sei / Não estudei`

---

## Etapa 2 — Sondagens Específicas (`S-A` a `S-F`)

### Sondagem `S-A` (Estágio A — Matrizes e Especiais)
- **`SA-01` (Âncora):** Construa a matriz $A_{(2,3)} = [a_{ij}]$ definida por $a_{ij} = 2i - j$ e determine sua transposta $A^T$.
- **`SA-02`:** Determine os valores de $m$ e $n$ tais que $\begin{bmatrix} m^2 - 40 & 2 \\ 5 & n^2 + 4 \end{bmatrix} = \begin{bmatrix} 41 & 2 \\ 5 & 13 \end{bmatrix}$.
- **`SA-03`:** Dada $H = \begin{bmatrix} 1 & -1 \\ 1 & -1 \end{bmatrix}$, calcule $H^2$ e classifique $H$ (idempotente, nilpotente, ortogonal ou anti-simétrica).

### Sondagem `S-B` (Estágio B — Determinantes e Inversa)
- **`SB-01` (Âncora):** Calcule $\det(A)$ onde $A = \begin{bmatrix} 2 & -1 & 3 \\ 0 & 4 & -2 \\ 1 & 2 & 5 \end{bmatrix}$ desenvolvendo por qualquer linha ou coluna (sem Sarrus).
- **`SB-02`:** Sabendo que $\det(A) = 5$ e $\det(B) = -2$ para matrizes $3\times 3$, determine $\det(B \cdot A^T)$ e justifique por que em geral $\det(A + B) \neq \det(A) + \det(B)$.
- **`SB-03`:** Encontre $P^{-1}$ pelo método de Gauss-Jordan `[P | I] -> [I | P^{-1}]` para $P = \begin{bmatrix} 3 & 5 \\ 1 & 2 \end{bmatrix}$, e resolva a equação matricial $DX^T = DC$ (supondo $D$ inversível).

### Sondagem `S-C` (Estágio C — Sistemas Lineares)
- **`SC-01` (Âncora):** Resolva pelo escalonamento da matriz ampliada o sistema $\begin{cases} 2x - y = 5 \\ x + 3y = 6 \end{cases}$.
- **`SC-02`:** Determine o valor de $k$ para que o sistema homogêneo $\begin{cases} x + y - z = 0 \\ 2x + y + z = 0 \\ 3x + 2y + kz = 0 \end{cases}$ admita solução própria (não-trivial).
- **`SC-03`:** Estabeleça a condição sobre $a, b, c$ para que $\begin{cases} x - 2y = a \\ 2x + y = b \\ 3x - y = c \end{cases}$ seja compatível.

### Sondagem `S-D` (Estágio D — Vetores e Produtos)
- **`SD-01` (Âncora):** Dados os pontos $A(1, -2, 3)$ e $B(3, 2, -1)$, escreva as coordenadas de $\overrightarrow{AB}$ e obtenha o versor $\widehat{AB}$.
- **`SD-02`:** Determine o vetor projeção $\operatorname{proj}_{\vec{v}}\vec{u}$ para $\vec{u} = (2, 3, 1)$ e $\vec{v} = (1, 0, -1)$.
- **`SD-03`:** Verifique se $\vec{u}=(1,2,-1)$, $\vec{v}=(2,-1,3)$ e $\vec{w}=(1,-8,7)$ são coplanares e calcule o volume do tetraedro formado a partir de um vértice comum.

### Sondagem `S-E` (Estágio E — Retas, Planos e Distâncias)
- **`SE-01` (Âncora):** Escreva as equações paramétricas e reduzidas (em função de $x$) da reta $r$ que passa por $A(2, 1, -3)$ e $B(4, 0, -2)$.
- **`SE-02`:** Determine a equação geral do plano $\pi$ que passa por $A(1, 0, 2)$ e é perpendicular à reta $r: \frac{x-1}{2} = \frac{y+1}{-1} = \frac{z}{3}$.
- **`SE-03`:** Calcule a distância entre os planos paralelos $\pi_1: x - 2y + 2z - 3 = 0$ e $\pi_2: 2x - 4y + 4z + 6 = 0$.

### Sondagem `S-F` (Estágio F — Cônicas e Quádricas)
- **`SF-01` (Âncora):** Para a parábola $y^2 + 6y - 8x + 1 = 0$, ache vértice, foco e equação da diretriz.
- **`SF-02`:** Escreva a equação da elipse centrada na origem com foco $F(3, 0)$ e eixo maior de comprimento $8$, indicando sua excentricidade.
- **`SF-03`:** Identifique a superfície quádrica $\frac{x^2}{4} + \frac{y^2}{9} - \frac{z^2}{16} = 1$ analisando seus traços nos planos $z = 0$ e $x = 0$.
