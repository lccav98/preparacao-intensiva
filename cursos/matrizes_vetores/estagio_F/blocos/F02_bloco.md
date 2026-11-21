# Bloco `F02` — Parábola Transladada, Completamento de Quadrados e 3 Pontos

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio F — Seções Cônicas ($\mathbb{R}^2$) e Superfícies Quádricas Canônicas / **`F02`** |
| **Micro-habilidade foco** | Transladar parábolas para vértice $V(h,k)$, aplicar completamento de quadrados para reduzir equações gerais a $(x-h)^2 = 2p(y-k)$ ou $(y-k)^2 = 2p(x-h)$ e ajustar parábolas por 3 pontos via sistema linear $3\times 3$ escalonado. |
| **Pré-requisitos** | `F01` *(Parábola na origem)*, `C03` *(Gauss-Jordan na matriz ampliada)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Prática (`F02-E01`–`F02-E06`, 22 min):** `14 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`F02-C01`–`F02-C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Apenas translações de eixos paralelas a $Ox$ e $Oy$.** **Estritamente proibido** rotacionar eixos, usar termo misto $Bxy \neq 0$, matriz de rotação ou diagonalização por autovalores. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`F02-E01`–`F02-E06`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Protocolo:** `PREP-MV-F02-V__-T__` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 6` | **Após autocorreção:** `___ / 6`
- **Checagem independente (sem gabarito) (`F02-C01`–`F02-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Translação de eixos ($x' = x - h$, $y' = y - k$):** deslocando o vértice da origem $(0,0)$ para $V(h, k)$, as equações reduzidas e seus elementos tornam-se:
   - **Eixo de simetria paralelo a $Oy$ ($x = h$):**
     $$(x - h)^2 = 2p(y - k) \quad \Longrightarrow \quad V(h, k),\quad F\!\left(h,\; k + \frac{p}{2}\right),\quad \text{diretriz } y = k - \frac{p}{2}.$$
   - **Eixo de simetria paralelo a $Ox$ ($y = k$):**
     $$(y - k)^2 = 2p(x - h) \quad \Longrightarrow \quad V(h, k),\quad F\!\left(h + \frac{p}{2},\; k\right),\quad \text{diretriz } x = h - \frac{p}{2}.$$
2. **Completamento de quadrados:** isole os termos da variável quadrática no lado esquerdo e some $\left(\frac{b}{2}\right)^2$ **em ambos os membros** da equação antes de colocar em evidência o coeficiente $2p$ do outro lado.
   - *Atenção:* só se lê $V(h,k)$ depois que o lado direito estiver fatorado na forma $2p(y - k)$ ou $2p(x - h)$!
3. **Parábola por 3 pontos:**
   - Eixo paralelo a $Oy$: use $y = ax^2 + bx + c$ ($a \neq 0$).
   - Eixo paralelo a $Ox$: use $x = ay^2 + by + c$ ($a \neq 0$).
   - Substitua os 3 pontos dados e resolva o sistema $3\times 3$ em $(a, b, c)$ por escalonamento (`C03`).

---

## 2. Exemplos Guiados

### Exemplo 1 — Completamento de quadrados em $x^2 - 6x - 8y + 25 = 0$
1. Isolando $x$: $x^2 - 6x = 8y - 25$.
2. Completando o quadrado ($\left(\frac{-6}{2}\right)^2 = 9$):
   $$x^2 - 6x + 9 = 8y - 25 + 9 \implies (x - 3)^2 = 8y - 16 \implies \mathbf{(x - 3)^2 = 8(y - 2)}.$$
3. Leitura direta: $V(3, 2)$, $2p = 8 \implies p = 4$ (concavidade para cima), foco $F(3,\, 2 + 2) = \mathbf{F(3, 4)}$ e diretriz $\mathbf{y = 2 - 2 = 0}$.

### Exemplo 2 — Parábola vertical por 3 pontos: $(0, 1)$, $(1, 0)$ e $(2, 3)$
1. Modelo $y = ax^2 + bx + c$:
   - Em $(0, 1)$: $c = 1$.
   - Em $(1, 0)$: $a + b + 1 = 0 \implies a + b = -1$.
   - Em $(2, 3)$: $4a + 2b + 1 = 3 \implies 2a + b = 1$.
2. Subtraindo as duas equações: $a = 2$, donde $b = -1 - 2 = -3$.
3. Equação obtida: $\mathbf{y = 2x^2 - 3x + 1}$.

---

## 3. Exercícios (`F02-E01` a `F02-E06`)

### `F02-E01` *(Reprodução do modelo — Leitura com vértice $V(h,k)$)*
Dada a parábola de equação $(y - 1)^2 = 12(x + 2)$, determine:  
**(a)** As coordenadas do vértice $V$  
**(b)** As coordenadas do foco $F$  
**(c)** A equação da reta diretriz

**Formato de resposta:** `(a) (h, k) (b) (x, y) (c) x = ...`.

---

### `F02-E02` *(Técnica central — Completamento de quadrados)*
Reduza a equação $x^2 + 4x + 8y - 12 = 0$ à forma canônica transladada e informe:  
**(a)** As coordenadas do vértice $V$  
**(b)** As coordenadas do foco $F$  
**(c)** A equação da reta diretriz

**Formato de resposta:** `(a) (h, k) (b) (x, y) (c) y = ...`.

---

### `F02-E03` *(Caça ao Erro — Esquecer de compensar o quadrado e errar a fatoração)*
Ao reduzir a parábola $y^2 - 6y - 4x + 13 = 0$, um estudante escreveu:
$$(y - 3)^2 = 4x - 13 \implies (y - 3)^2 = 4\left(x - \frac{13}{4}\right)$$
e concluiu que o vértice seria $V\!\left(\frac{13}{4}, 3\right)$.  
Identifique o erro cometido no completamento de quadrados e determine corretamente:  
**(a)** A equação reduzida na forma $(y - k)^2 = 2p(x - h)$  
**(b)** As coordenadas do vértice $V$  
**(c)** As coordenadas do foco $F$

---

### `F02-E04` *(Variação controlada com pistas — Foco e diretriz fora da origem)*
Determine a equação reduzida da parábola cujo foco é $F(4, -1)$ e cuja reta diretriz é $y = 5$.

*Pistas:* O vértice $V$ é o ponto médio entre o foco $F(4, -1)$ e sua projeção $(4, 5)$ sobre a diretriz; observe se $F$ está acima ou abaixo da diretriz para acertar o sinal de $p$.

---

### `F02-E05` *(Variação controlada com pistas — Parábola vertical por 3 pontos)*
Determine a equação da parábola com eixo de simetria paralelo ao eixo $Oy$ ($y = ax^2 + bx + c$) que passa pelos pontos $A(-1, 6)$, $B(0, 1)$ e $C(2, 3)$.

*Pistas:* O ponto $B(0,1)$ fornece imediatamente $c = 1$; resolva o sistema restante em $a$ e $b$ por eliminação de Gauss-Jordan.

---

### `F02-E06` *(Resolução independente — Parábola horizontal por 3 pontos)*
Determine a equação da parábola com eixo de simetria paralelo ao eixo $Ox$ ($x = ay^2 + by + c$) que passa pelos pontos $P(3, 0)$, $Q(2, 1)$ e $R(11, -2)$.

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `F02-C01` *(Completamento de quadrados completo)*
Reduza a equação $y^2 + 4y - 12x + 28 = 0$ à forma canônica e determine:  
**(a)** As coordenadas do vértice $V$  
**(b)** As coordenadas do foco $F$  
**(c)** A equação da reta diretriz

### `F02-C02` *(Equação por foco e diretriz horizontal)*
Determine a equação reduzida da parábola com foco $F(-1, 3)$ e reta diretriz $x = 3$.

### `F02-C03` *(Ajuste por 3 pontos)*
Determine a equação da parábola de eixo paralelo a $Oy$ ($y = ax^2 + bx + c$) que passa pelos pontos $(0, 2)$, $(1, 3)$ e $(-1, 5)$.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `F03` (`Elipse na Origem e Circunferência`) ou `F04` (após concluir `F03`):** somente após autocorreção de `F02-E01..E06` **e** **100% (3/3)** na Checagem Independente `F02-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** identificar se a falha ocorreu no sinal de $(h,k)$ ao ler $(x-h)$ e $(y-k)$, na falta de compensação ao completar o quadrado, ou na resolução do sistema $3\times 3$; refazer os Exemplos 1 e 2 e aplicar a variante `V2`.
- **Após 2 tentativas malsucedidas:** recuar ao pré-requisito **`F01`** (se errou foco/diretriz/sinal de $p$) ou **`C03`** (se errou o escalonamento do ajuste por 3 pontos) antes de retornar a `F02`.

---

## 6. Referências do Orientador
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 169–171 (Cap. 7 — translação de eixos e equação da parábola com vértice $V(h,k)$).
- `[DOC]` `Mat_Vet_L11.pdf` p. 1 (Ex. 3–6 — completamento de quadrados, vértice/foco/diretriz fora da origem e parábola por 3 pontos).
- Gabarito e especificação de validação: [F02_gabarito.md](../gabaritos/F02_gabarito.md) e [casos_F02.json](../testes/casos_F02.json).
