# Bloco `D02` — Vetores no $\mathbb{R}^2$ e $\mathbb{R}^3$, Base Canônica e $\overrightarrow{AB} = B - A$

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio D — Vetores em $\mathbb{R}^2/\mathbb{R}^3$, Produtos, Áreas e Volumes / **`D02`** |
| **Micro-habilidade foco** | Representar vetores em coordenadas $(x,y,z)$ e na base canônica $\{\hat{\imath}, \hat{\jmath}, \hat{k}\}$, calcular $\overrightarrow{AB} = B - A$, resolver equações vetoriais lineares e encontrar os 3 possíveis vértices de um paralelogramo. |
| **Pré-requisitos** | `D01` *(Vetor, sentido, regra do triângulo e do paralelogramo)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Prática (`D02-E01`–`D02-E06`, 22 min):** `14 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`D02-C01`–`D02-C03`, 14 min):** `10 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Apenas álgebra de coordenadas, base canônica e igualdade vetorial.** Sem produto escalar, produto vetorial ou módulo analítico (reservados a `D04`–`D07`). Mantenha todas as coordenadas em frações irredutíveis exatas. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`D02-E01`–`D02-E06`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Protocolo:** `PREP-MV-D02-V__-T__` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 6` | **Após autocorreção:** `___ / 6`
- **Checagem independente (sem gabarito) (`D02-C01`–`D02-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Base canônica:** no $\mathbb{R}^3$, os vetores unitários dos eixos coordenados são $\hat{\imath} = (1,0,0)$, $\hat{\jmath} = (0,1,0)$ e $\hat{k} = (0,0,1)$. Todo vetor $\vec{v} = (x,y,z)$ escreve-se de forma única como:
   $$\vec{v} = x\hat{\imath} + y\hat{\jmath} + z\hat{k}.$$
2. **Operações por coordenadas:** para $\vec{u} = (x_1, y_1, z_1)$, $\vec{v} = (x_2, y_2, z_2)$ e $k \in \mathbb{R}$:
   $$\vec{u} + \vec{v} = (x_1+x_2,\; y_1+y_2,\; z_1+z_2), \qquad k\vec{v} = (kx_2,\; ky_2,\; kz_2).$$
3. **Vetor definido por dois pontos (Extremidade menos Origem):** dados a origem $A(x_A, y_A, z_A)$ e a extremidade $B(x_B, y_B, z_B)$:
   $$\overrightarrow{AB} = B - A = (x_B - x_A,\; y_B - y_A,\; z_B - z_A), \qquad \overrightarrow{BA} = -\overrightarrow{AB} = A - B.$$
   **Armadilha clássica:** nunca subtraia $A - B$ para $\overrightarrow{AB}$; sempre faça **extremidade menos origem**.
4. **Equações vetoriais:** isole o vetor desconhecido usando propriedades algébricas **antes** de substituir as coordenadas.
5. **Os 3 possíveis vértices de um paralelogramo:** se o enunciado informa três vértices $P, Q, R$ **sem fixar a ordem cíclica** dos vértices do paralelogramo, existem **3 soluções distintas** para o 4º vértice $S$ (dependendo de qual par forma a diagonal):
   - $\overrightarrow{PS} = \overrightarrow{QR}$ (ou $\overrightarrow{PQ} = \overrightarrow{RS}$ com ordem alterada): $S_1 = P + Q - R$ (diagonal $PQ$);
   - $\overrightarrow{PR} = \overrightarrow{QS}$: $S_2 = P + R - Q$ (diagonal $PR$);
   - $\overrightarrow{PQ} = \overrightarrow{SR}$: $S_3 = Q + R - P$ (diagonal $QR$).
   *(Se a ordem $PQRS$ for fixada no enunciado, apenas uma igualdade vetorial vale, por exemplo $\overrightarrow{PQ} = \overrightarrow{SR}$.)*

---

## 2. Exemplos Guiados

### Exemplo 1 — Vetor definido por dois pontos e base canônica
Dados $A(1, -2, 4)$ e $B(4, 1, -2)$:
$$\overrightarrow{AB} = B - A = (4 - 1,\; 1 - (-2),\; -2 - 4) = (3, 3, -6) = 3\hat{\imath} + 3\hat{\jmath} - 6\hat{k}.$$

### Exemplo 2 — Determinação dos 3 possíveis quartos vértices de um paralelogramo
Dados os pontos $P(1, 0, 2)$, $Q(3, -1, 4)$ e $R(0, 2, -1)$, encontre todos os possíveis pontos $S$ tais que $P, Q, R, S$ formem um paralelogramo (sem ordem pré-fixada):
1. **Caso 1 ($\overrightarrow{RS} = \overrightarrow{QP}$, diagonal $PQ$):** $S_1 = P + Q - R = (1+3-0,\; 0-1-2,\; 2+4-(-1)) = \mathbf{(4, -3, 7)}$.
2. **Caso 2 ($\overrightarrow{QS} = \overrightarrow{RP}$, diagonal $PR$):** $S_2 = P + R - Q = (1+0-3,\; 0+2-(-1),\; 2-1-4) = \mathbf{(-2, 3, -3)}$.
3. **Caso 3 ($\overrightarrow{PS} = \overrightarrow{QR}$, diagonal $QR$):** $S_3 = Q + R - P = (3+0-1,\; -1+2-0,\; 4-1-2) = \mathbf{(2, 1, 1)}$.

---

## 3. Exercícios (`D02-E01` a `D02-E06`)

### `D02-E01` *(Reprodução do modelo — Extremidade menos origem)*
Dados os pontos $A(2, -3, 1)$ e $B(-1, 4, 5)$, determine as coordenadas de:  
**(a)** $\overrightarrow{AB}$ (escreva também na notação com $\hat{\imath}, \hat{\jmath}, \hat{k}$)  
**(b)** $\overrightarrow{BA}$

---

### `D02-E02` *(Técnica central — Equação vetorial linear)*
Dados os vetores $\vec{u} = (3, -1, 2)$ e $\vec{v} = (-1, 2, 1)$, determine o vetor $\vec{w}$ tal que:
$$3(\vec{u} - \vec{v}) + \frac{1}{2}\vec{w} = 2\vec{u} - \vec{w}.$$

---

### `D02-E03` *(Caça ao Erro — Subtração invertida e razão de segmento)*
Para os pontos $A(1, -2, 3)$ e $B(4, 2, -1)$, um estudante calculou $\overrightarrow{AB}$ fazendo $A - B$ e tentou achar o ponto $P$ que satisfaz $\overrightarrow{AP} = 2\overrightarrow{PB}$ calculando $P = A + 2B$.  
Corrija os dois erros e determine exatamente:  
**(a)** O vetor $\overrightarrow{AB}$  
**(b)** As coordenadas do ponto $P$ tal que $\overrightarrow{AP} = 2\overrightarrow{PB}$

---

### `D02-E04` *(Variação controlada com pistas — Combinação de segmentos e ordem fixa)*
Dados os pontos $A(-1, 3, 2)$, $B(2, 5, -1)$ e $C(3, -1, 4)$, determine:  
**(a)** O vetor $2\overrightarrow{AB} - \overrightarrow{BC}$  
**(b)** As coordenadas do ponto $D$ tal que $\overrightarrow{DC} = \overrightarrow{BA}$

*Pistas:* Calcule $\overrightarrow{AB} = B-A$, $\overrightarrow{BC} = C-B$ e $\overrightarrow{BA} = A-B$; em $\overrightarrow{DC} = \overrightarrow{BA}$, use $C - D = A - B$ para isolar $D$.

---

### `D02-E05` *(As 3 soluções do paralelogramo)*
Sejam $P(1, -2, 3)$, $Q(3, 1, 0)$ e $R(-2, 4, 2)$ três vértices de um paralelogramo no $\mathbb{R}^3$ (sem ordem cíclica fixada). Determine o conjunto dos **3 possíveis pontos $S$** que completam o paralelogramo.

---

### `D02-E06` *(Resolução independente — Ponto médio e prolongamento)*
Dados os pontos $A(-2, 1, 4)$ e $B(1, -3, 2)$, determine as coordenadas do ponto $P$ tal que:  
**(a)** $\overrightarrow{AP} = \overrightarrow{PB}$  
**(b)** $\overrightarrow{AP} = 3\overrightarrow{AB}$

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `D02-C01` *(Equação vetorial na base canônica)*
Dados $\vec{a} = 2\hat{\imath} - 3\hat{\jmath} + \hat{k}$ e $\vec{b} = -\hat{\imath} + 4\hat{\jmath} - 2\hat{k}$, determine o vetor $\vec{x}$ em coordenadas tal que:
$$2\vec{x} + \vec{a} = 3(\vec{b} - \vec{x}).$$

### `D02-C02` *(Combinação de vetores entre pontos e fração de segmento)*
Dados $A(3, -1, 2)$, $B(0, 5, -2)$ e $C(1, 2, 3)$, determine:  
**(a)** O vetor $3\overrightarrow{BA} - 2\overrightarrow{CB}$  
**(b)** O ponto $M$ tal que $\overrightarrow{AM} = \frac{1}{2}\overrightarrow{AB}$

### `D02-C03` *(Os 3 possíveis vértices do paralelogramo)*
Dados os pontos $P(0, 2, -1)$, $Q(2, -1, 3)$ e $R(4, 3, 1)$ no $\mathbb{R}^3$, determine todos os **3 possíveis pontos $S$** de modo que $P, Q, R, S$ sejam vértices de um paralelogramo.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `D03` (`Combinação Linear, Paralelismo e Colinearidade de Pontos`):** somente após autocorreção de `D02-E01..E06` **e** **100% (3/3)** na Checagem Independente `D02-C01..C03` sem consulta.
- **Recuperação direcionada (1ª falha):** verificar se o erro ocorreu na ordem $B - A$, no isolamento algébrico da equação vetorial ou na omissão de uma das 3 diagonais do paralelogramo; revisar os Exemplos 1 e 2 e aplicar a variante `V2`.
- **Após 2 tentativas malsucedidas:** recuar ao pré-requisito estrutural **`D01`** para consolidar a regra do triângulo e do paralelogramo no plano antes de retomar coordenadas no $\mathbb{R}^3$.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Vetores.pdf` p. 29–42, 46–48 (vetores em $\mathbb{R}^2/\mathbb{R}^3$, base canônica $\{\hat{\imath}, \hat{\jmath}, \hat{k}\}$, igualdade, operações algébricas e $\overrightarrow{AB} = B - A$).
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 92–100 (Cap. 2 do caderno manuscrito — exemplos de $\overrightarrow{AB}$, ponto $P$ e vértices do paralelogramo).
- `[DOC]` `Mat_Vet_L6.pdf` p. 1–2 (Ex. 4–6 e Ex. 9–12 — equações vetoriais, $\overrightarrow{DC}=\overrightarrow{BA}$, $\overrightarrow{AP}=\overrightarrow{PB}$, $\overrightarrow{AP}=3\overrightarrow{AB}$).
- Gabarito e especificação de validação: [D02_gabarito.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/gabaritos/D02_gabarito.md) e [casos_D02.json](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/testes/casos_D02.json).
