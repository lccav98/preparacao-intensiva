# Mapa Curricular e Progressão em Micro-Blocos — Matrizes e Vetores (`MAT121` — UTFPR-PG)

> **Identidade Pedagógica:** Curso baseado em **Preparação Intensiva** (aprendizagem por domínio, micro-passos graduados, prática independente e checagem sem consulta com critério de **100%**).  
> **Fontes Oficiais:** Estritamente ancorado nos **19 PDFs** de `C:\Users\d7opa\Documents\Matrizes e Vetores` auditados em [00_inventario_fontes.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/00_inventario_fontes.md).  
> **Protocolo da Automação:** `PREP-MV-<BLOCO>-<VARIANTE>-T<TENTATIVA>-<HASH>` (coexiste com `CC61A - Algoritmos` no Portal Multi-Disciplina).

---

## 1. Arquitetura em 7 Estágios e 60 Blocos

O curso cobre os conteúdos das **Avaliações P1, P2, P3 e Reavaliação** do plano `MAT121-RE42B` em **7 estágios (`A` a `G`)** totalizando **60 micro-blocos**:

| Estágio | Pasta | Blocos | Qtd | Foco Curricular e Alinhamento Avaliativo (`[DOC]`/`[INF]`) | Referências das Fontes |
|---|---|---|---:|---|---|
| **A** | `estagio_A` | `A01`–`A09` | 9 | **Matrizes: Definição, Operações, Transposta e Especiais** *(Base P1)* | `Matrizes` p. 1–22; `P1` p. 1–24; `L1`, `L2` |
| **B** | `estagio_B` | `B01`–`B09` | 9 | **Determinantes, Inversão (`[A\|I]`) e Equações Matriciais** *(Conclusão P1)* | `Matrizes` p. 23–36; `P1` p. 25–48; `L3`, `L4` |
| **C** | `estagio_C` | `C01`–`C08` | 8 | **Sistemas Lineares, Escalonamento, Posto (`C_A, C_V`) e Parâmetros** *(1ª Metade P2)* | `Sistemas` p. 1–60; `P2` p. 49–77; `L5` |
| **D** | `estagio_D` | `D01`–`D10` | 10 | **Vetores em `\mathbb{R}^2/\mathbb{R}^3`, Produtos (Escalar, Vetorial, Misto), Áreas e Volumes** *(2ª Metade P2)* | `Vetores` p. 1–75; `P3` p. 78–123; `L6`, `L7` |
| **E** | `estagio_E` | `E01`–`E10` | 10 | **A Reta, O Plano e Distâncias no `\mathbb{R}^3`** *(1ª Metade P3)* | `Parte_4` p. 1–61; `P3` p. 124–164; `L8`–`L10` |
| **F** | `estagio_F` | `F01`–`F08` | 8 | **Seções Cônicas (`\mathbb{R}^2`) e Superfícies Quádricas Canônicas `[INF/AUS]`** *(2ª Metade P3)* | `P3` p. 165–184; `L11`; `Planejamento` Sem. 13–14 |
| **G** | `estagio_G` | `G01`–`G06` | 6 | **Integração Geral e Simulados P1, P2, P3 e Reavaliação** *(Consolidação Final)* | Integração cumulativa `L1`–`L11` e `P1`–`P3` |

---

## 2. Regras Invioláveis de Estrutura e Domínio

1. **Escopo Negativo Estrito:** Proibido ensinar ou usar Regra de Sarrus, Chió, Vandermonde, matriz adjunta, Regra de Cramer, autovalores/autovetores, diagonalização, espaços vetoriais abstratos, Gram-Schmidt ou rotação de cônicas com termo `xy`.
2. **Aritmética Exata:** Todo resultado numérico de matrizes, determinantes, sistemas, vetores, distâncias e cônicas deve ser mantido em **frações irredutíveis** e **radicais exatos** (ex.: `16/\sqrt{21}`, `-4/5`, `(\sqrt{13})/3`), reservando aproximações apenas quando explicitamente indicado.
3. **Critério de Avanço:** Em cada bloco, executa-se a bateria de prática (**4–6 exercícios**, meta `15–25 min`) seguida da **Checagem Independente sem consulta** (**2–3 questões inéditas**, meta `10–18 min`) com exigência de **100% de acerto**.
4. **Regra das 2 Tentativas:** Após duas falhas na Checagem do mesmo bloco (`V1` e `V2`), é proibido repetir pela 3ª vez: o orientador (ou o sistema) recua para o **pré-requisito estrutural** declarado no DAG.

---

## 3. Mapa Completo dos 60 Blocos e Grafo Acíclico de Pré-Requisitos (DAG)

### Estágio A — Matrizes: Definição, Operações, Transposta e Especiais (`A01`–`A09`)

| Bloco | Título e Micro-habilidade Foco | Pré-req. | Conteúdo Novo | Tempo Prática / Checagem | Fontes (`[DOC]`/`[INF]`) |
|---|---|---|---|---|---|
| **`A01`** | Definição de Matriz, Ordem e Tipos Básicos | `—` | `A_{(m,n)} = [a_{ij}]`, lei de formação `a_{ij}`, linha/coluna, retangular vs. quadrada, diagonais principal/secundária, nula `[O]`, diagonal, escalar, identidade `I`, triangulares | 20 min / 12 min | `Matrizes` p. 3–8; `P1` p. 1–6 |
| **`A02`** | Igualdade de Matrizes e Equações por Elementos | `A01` | Igualdade de matrizes, mesma ordem, equações lineares e quadráticas em elementos (`\pm` nas raízes!) | 18 min / 12 min | `Matrizes` p. 9; `L1` Ex. 1–2 |
| **`A03`** | Adição, Subtração e Multiplicação por Escalar | `A02` | `A+B`, `A-B`, `\lambda A`, combinações `X = 2A - 6B + 4C` e propriedades algébricas | 20 min / 12 min | `Matrizes` p. 10–11; `L1` Ex. 3–5 |
| **`A04`** | Produto de Matrizes e Forma Matricial `AX = B` | `A03` | Condição `A_{(m,n)} \times B_{(n,\ell)} = C_{(m,\ell)}`, somatório `c_{ij}`, `AX = B` para sistemas | 22 min / 14 min | `Matrizes` p. 12–13, 16; `L1` Ex. 6–7 |
| **`A05`** | Propriedades do Produto, Não-Comutatividade e Associatividade | `A04` | `AB \neq BA`, `(AB)C = A(BC)`, distributividade e divisores de zero (`AB = O` com `A, B \neq O`) | 20 min / 14 min | `Matrizes` p. 14–15; `L1` Ex. 8–9 |
| **`A06`** | Matriz Transposta e Propriedade Reversa `(AB)^T = B^T A^T` | `A04` | `A^T_{(n,m)}`, linearidade da transposição, inversão da ordem no produto transposto | 20 min / 14 min | `Matrizes` p. 17; `L2` Ex. 1–2 |
| **`A07`** | Matrizes Simétricas, Anti-Simétricas e Ortogonais | `A06` | `S^T=S`, `A^T=-A`, `AA^T` simétrica, decomposição `(A+A^T)/2 + (A-A^T)/2`, `MM^T=I` (rotação) | 22 min / 15 min | `Matrizes` p. 18–20; `L2` Ex. 3–6 |
| **`A08`** | Potências de Matrizes e Classificação Especial | `A05` | `A^n`, periódica (`A^{k+1}=A`, período `k`), idempotente (`A^2=A`), nilpotente (`A^p=O`, índice `p`), produto de triangulares | 22 min / 15 min | `Matrizes` p. 21–22; `L2` Ex. 7–11 |
| **`A09`** | Revisão Cumulativa do Estágio A | `A05`, `A07`, `A08` | Integração de igualdade, combinações, produto não comutativo, transposta e classificações especiais | 24 min / 16 min | `Matrizes` p. 1–22; `L1`–`L2` |

### Estágio B — Determinantes, Inversão (`[A|I]`) e Equações Matriciais (`B01`–`B09`)

| Bloco | Título e Micro-habilidade Foco | Pré-req. | Conteúdo Novo | Tempo Prática / Checagem | Fontes (`[DOC]`/`[INF]`) |
|---|---|---|---|---|---|
| **`B01`** | Determinante de 2ª e 3ª Ordem (1ª Linha) | `A01` | Barras verticais `|a_{ij}|`, `a_{11}a_{22}-a_{12}a_{21}`, desenvolvimento de ordem 3 pela 1ª linha (sem Sarrus) | 20 min / 13 min | `Matrizes` p. 23–26; `L3` Ex. 1–3 |
| **`B02`** | Desenvolvimento por Qualquer Linha ou Coluna (`3x3` e `4x4`) | `B01` | Matriz de sinais xadrez `(-1)^{i+j}`, escolha estratégica de linha/coluna mais esparsa, ordem 4 | 24 min / 16 min | `Matrizes` p. 27–28; `P1` p. 30–33 |
| **`B03`** | Propriedades dos Determinantes e Desigualdade da Soma | `B02`, `A06` | As 8 propriedades (`det A^T`, linhas iguais/proporcionais, matriz triangular, escalares em linha, troca de linhas), `det(A+B) != det A + det B`, `det(AB)` | 22 min / 14 min | `Matrizes` p. 29; `L3` Ex. 4–6 |
| **`B04`** | Determinantes por Triangulação e Redução a `I` | `B03` | Operações elementares compensando sinal (troca) e fator multiplicativo `k` em matrizes `3x3` e `4x4` | 24 min / 16 min | `Matrizes` p. 30, 33–34; `L3` Ex. 7 |
| **`B05`** | Equações com Determinantes e Condição de Singularidade | `B02`, `B03` | Resolver `\det(A) = c`, detectar todas as raízes sem perder `r=0` ao simplificar, `det A = 0` | 22 min / 14 min | `L3` Ex. 8–10; `L4` Ex. 7–8 |
| **`B06`** | Matriz Inversa por Definição (`AB = BA = I`) e Singularidade | `A05`, `B05` | Matriz singular vs. não-singular, verificação `AB = I`, determinação de parâmetros `m, n` via `AB = I` | 20 min / 14 min | `Matrizes` p. 31, 36; `L1` Ex. 10–11; `L4` Ex. 4 |
| **`B07`** | Inversão pelo Método de Gauss-Jordan (`[A \| I] -> [I \| A^{-1}]`) | `B04`, `B06` | Algoritmo de escalonamento completo na matriz ampliada `[A \| I]` em `2x2`, `3x3` e `4x4` (sem adjunta!) | 25 min / 18 min | `Matrizes` p. 35; `P1` p. 46–48; `L4` Ex. 1–6 |
| **`B08`** | Propriedades da Inversa e Equações Matriciais Simbólicas | `B06`, `A06` | `(AB)^{-1}=B^{-1}A^{-1}`, `(A^T)^{-1}=(A^{-1})^T`, multiplicação à esquerda vs. à direita para isolar `X` | 22 min / 15 min | `Matrizes` p. 32; `L4` Ex. 9–13 |
| **`B09`** | Revisão Cumulativa do Estágio B (Simulado P1) | `B07`, `B08` | Triangulação `4x4`, equações com `\det`, inversão `[A\|I]` e equações matriciais sem consulta | 25 min / 18 min | `Matrizes` p. 23–36; `L3`–`L4` |

### Estágio C — Sistemas Lineares, Escalonamento, Posto (`C_A, C_V`) e Parâmetros (`C01`–`C08`)

| Bloco | Título e Micro-habilidade Foco | Pré-req. | Conteúdo Novo | Tempo Prática / Checagem | Fontes (`[DOC]`/`[INF]`) |
|---|---|---|---|---|---|
| **`C01`** | Equação Linear, Forma Matricial, Matriz Ampliada e Operações `L` | `A04`, `B04` | `AX=B`, matriz ampliada, equivalência de sistemas, notação `L_{ij}, L_i(\alpha), L_j' = L_j + L_i(\alpha)` | 18 min / 12 min | `Sistemas` p. 2–8; `P2` p. 49–53 |
| **`C02`** | Eliminação de Gauss e Substituição Regressiva | `C01` | Triangularização superior sem reduzir pivôs superiores, retro-substituição (`n x n`) | 22 min / 14 min | `Sistemas` p. 9–12 |
| **`C03`** | Método de Gauss-Jordan na Matriz Ampliada (`n x n`) | `C02` | Redução completa de `[A\|B]` até `[I\|X]`, sistemas SPD, SPI e SI quadrados | 24 min / 16 min | `Sistemas` p. 14–21; `L5` Ex. 2, 5 |
| **`C04`** | Método da Matriz Inversa (`X = A^{-1}B`) | `B07`, `C01` | Quando `A` é inversível, resolver múltiplos vetores `B` reutilizando `A^{-1}` | 22 min / 16 min | `Sistemas` p. 22–32; `L5` Ex. 20–23 |
| **`C05`** | Forma de Escada (Escalonada), Posto (`C_A, C_V, C`) e Sistemas `m x n` | `C03` | Submatriz `V`, contagem de linhas não nulas (`C_A`, `C_V`), `C_A > C_V -> SI`, `C_A = C_V = C` (SPD vs. SPI), sobredeterminados `m > n` | 24 min / 16 min | `Sistemas` p. 33–51; `L5` Ex. 1, 3, 9–11 |
| **`C06`** | Grau de Liberdade (`g = n - C`) e Sistemas Homogêneos | `C05`, `B05` | Variáveis arbitrárias, parametricidade, solução trivial vs. soluções próprias (`det=0` / `C<n`) | 22 min / 16 min | `Sistemas` p. 13, 49, 52–60; `L5` Ex. 4, 6–8, 19 |
| **`C07`** | Discussão de Sistemas com Parâmetros (`k, a, b, c, d`) | `C05`, `C06` | Carregar termos simbólicos no escalonamento, condições de compatibilidade (`C_A = C_V`), soluções em função de `a, b` | 25 min / 18 min | `L5` Ex. 12–19; `P2` p. 64–77 |
| **`C08`** | Revisão Cumulativa do Estágio C | `C04`, `C07` | Classificação `m x n`, posto, homogeneidade, parâmetros e método da inversa | 25 min / 18 min | `Sistemas` p. 1–60; `L5` |

### Estágio D — Vetores em `\mathbb{R}^2/\mathbb{R}^3`, Produtos, Áreas e Volumes (`D01`–`D10`)

| Bloco | Título e Micro-habilidade Foco | Pré-req. | Conteúdo Novo | Tempo Prática / Checagem | Fontes (`[DOC]`/`[INF]`) |
|---|---|---|---|---|---|
| **`D01`** | Segmento Orientado, Vetor, Módulo, Versor e Ângulos Geométricos | `A01` | Segmento orientado vs. vetor, `|\vec{v}|`, `\hat{v} = \vec{v}/|\vec{v}|`, soma/diferença geométrica, paralelogramo, `\theta \in [0,\pi]` e `\pi-\theta` | 18 min / 12 min | `Vetores` p. 4–28; `L6` Ex. 1–3, 17 |
| **`D02`** | Vetores no `\mathbb{R}^2` e `\mathbb{R}^3`, Base Canônica e `\overrightarrow{AB}=B-A` | `D01` | `{\hat{\imath},\hat{\jmath},\hat{k}}`, coordenadas `(x,y,z)`, vetor definido por dois pontos, equações vetoriais, vértices do paralelogramo (3 soluções) | 22 min / 14 min | `Vetores` p. 29–42, 46–48; `L6` Ex. 4–6, 9–12 |
| **`D03`** | Combinação Linear, Paralelismo e Colinearidade de Pontos | `D02`, `C03` | `\vec{w} = a_1\vec{v}_1 + a_2\vec{v}_2` via sistema escalonado, `\vec{u}=m\vec{v}`, colinearidade de 3 pontos (`\overrightarrow{AB} \parallel \overrightarrow{AC}`) | 22 min / 15 min | `Vetores` p. 37–38, 43–45, 49; `L6` Ex. 7–8, 13–16 |
| **`D04`** | Produto Escalar, Módulo Analítico, Distância e Versor | `D02` | `\vec{u}\cdot\vec{v}`, `|\vec{v}|=\sqrt{\vec{v}\cdot\vec{v}}`, distância `|\overrightarrow{AB}|`, versor unitário e propriedades algébricas | 20 min / 14 min | `Vetores` p. 50–55; `L7` Ex. 1–5, 11 |
| **`D05`** | Ângulo entre Vetores, Ortogonalidade e Cossenos Diretores | `D04` | `\cos\theta = \frac{\vec{u}\cdot\vec{v}}{|\vec{u}||\vec{v}|}`, `\vec{u}\perp\vec{v}`, ângulo interno em triângulos (vetores saindo do vértice!), `\cos^2\alpha+\cos^2\beta+\cos^2\gamma=1` | 22 min / 15 min | `Vetores` p. 56–61; `L7` Ex. 6–10, 12–14 |
| **`D06`** | Projeção Ortogonal (`\operatorname{proj}_{\vec{v}}\vec{u}`) | `D04`, `D05` | Fórmula `\left(\frac{\vec{u}\cdot\vec{v}}{|\vec{v}|^2}\right)\vec{v}`, componente paralela e ortogonal a `\vec{v}` | 18 min / 12 min | `Vetores` p. 62–64; `L7` Ex. 15 |
| **`D07`** | Produto Vetorial (`\vec{u}\times\vec{v}`), Propriedades e Ortogonalidade | `D05`, `B01` | Determinante simbólico com `\hat{\imath},\hat{\jmath},\hat{k}`, anti-comutatividade, mão direita, Lagrange, vetor ortogonal a dois vetores | 22 min / 15 min | `Vetores` p. 65–68; `L7` Ex. 16, 19–20, 23 |
| **`D08`** | Áreas via Produto Vetorial (Paralelogramo e Triângulo) | `D07` | Área do paralelogramo `|\vec{u}\times\vec{v}|`, área do triângulo `\frac{1}{2}|\overrightarrow{AB}\times\overrightarrow{AC}|` | 20 min / 14 min | `Vetores` p. 69; `L7` Ex. 17–18 |
| **`D09`** | Produto Misto, Coplanaridade e Volumes (Paralelepípedo e Tetraedro) | `D07`, `B01` | `(\vec{u},\vec{v},\vec{w})`, teste de coplanaridade de 3 vetores e 4 pontos, `V_{paral}=|(\vec{u},\vec{v},\vec{w})|`, `V_{tetra}=\frac{1}{6}|\dots|` (atenção às 2 soluções de `|det|=V`!) | 24 min / 16 min | `Vetores` p. 70–75; `L7` Ex. 21–22, 24–25 |
| **`D10`** | Revisão Cumulativa do Estágio D (Simulado P2) | `D06`, `D08`, `D09`, `C08` | Combinação linear, ângulo/projeção, produtos vetorial e misto, áreas, coplanaridade e volumes | 25 min / 18 min | `Vetores` p. 1–75; `L6`–`L7` |

### Estágio E — A Reta, O Plano e Distâncias no `\mathbb{R}^3` (`E01`–`E10`)

| Bloco | Título e Micro-habilidade Foco | Pré-req. | Conteúdo Novo | Tempo Prática / Checagem | Fontes (`[DOC]`/`[INF]`) |
|---|---|---|---|---|---|
| **`E01`** | Equações da Reta no `\mathbb{R}^3` e Pertinência | `D02`, `D03` | Vetorial, paramétricas, simétricas, reduzidas em `x`, leitura correta de vetor diretor em coordenadas constantes (`x=3, z=1`) | 22 min / 14 min | `Parte_4` p. 3–9; `L8` Ex. 1–6 |
| **`E02`** | Ângulo, Paralelismo, Ortogonalidade e Reta Ortogonal a Duas | `E01`, `D05`, `D07` | `\cos\theta = \frac{|\vec{v}_1\cdot\vec{v}_2|}{|\vec{v}_1||\vec{v}_2|}` (`\le 90^\circ`), paralelismo, `\vec{v}_r = \vec{v}_1\times\vec{v}_2` | 22 min / 14 min | `Parte_4` p. 10–11, 14–17; `L8` Ex. 7–11 |
| **`E03`** | Coplanaridade de Retas, Posições Relativas e Interseção | `E02`, `D09`, `C05` | Produto misto `\vec{v}_1\cdot(\vec{v}_2\times\overrightarrow{A_1A_2})`, concorrentes vs. paralelas vs. reversas, sistema com parâmetros `t_1, t_2` | 24 min / 16 min | `Parte_4` p. 12–13, 18–22; `L8` Ex. 12–13 |
| **`E04`** | Equação Geral e Paramétricas do Plano | `D07`, `D09`, `E01` | `ax+by+cz+d=0` via `\vec{n}\cdot\overrightarrow{AP}=0`, plano por 3 pontos, mediador, via produto misto, contendo 2 retas (concorrentes e paralelas), forma paramétrica `(h,t)` | 24 min / 16 min | `Parte_4` p. 24–32; `L9` Ex. 1–11, 21–25 |
| **`E05`** | Ângulos e Posições Relativas Plano-Plano e Reta-Plano | `E04`, `E02` | Ângulo entre planos (`\cos\theta`), ângulo reta-plano (`\sin\phi = \frac{|\vec{v}\cdot\vec{n}|}{|\vec{v}||\vec{n}|}`), verificação de ponto fora para paralelismo estrito `r \parallel \pi` | 22 min / 15 min | `Parte_4` p. 33–34; `L9` Ex. 12–15 |
| **`E06`** | Interseções: Dois Planos, Reta-Plano e Eixos/Planos Coordenados | `E04`, `C05` | Reta interseção de `\pi_1\cap\pi_2`, ponto `r\cap\pi` via escalonamento, interceptos nos eixos + área/volume de tetraedro | 24 min / 16 min | `Parte_4` p. 35–44; `L9` Ex. 16–20 |
| **`E07`** | Distâncias Ponto-Ponto e Ponto-Reta | `E01`, `D08` | `d(P_1,P_2)`, `d(P_0,r)=\frac{|\vec{v}\times\overrightarrow{P_1P_0}|}{|\vec{v}|}` e distâncias aos eixos coordenados `x, y, z` | 20 min / 14 min | `Parte_4` p. 46–47; `L10` Ex. 1–2 |
| **`E08`** | Distância entre Duas Retas (Concorrentes, Paralelas e Reversas) | `E03`, `E07`, `D09` | Verificar se `\vec{v}_1 \parallel \vec{v}_2` antes de escolher `d(P_0, s)` vs. fórmula do paralelepípedo `\frac{|(\vec{u},\vec{v},\overrightarrow{P_1P_2})|}{|\vec{u}\times\vec{v}|}` | 22 min / 15 min | `Parte_4` p. 48–49, 53–58; `L10` Ex. 3–4 |
| **`E09`** | Distâncias Envolvendo Planos (Ponto-Plano, Planos Paralelos, Reta-Plano) | `E05`, `E07` | `d(P_0,\pi)=\frac{|ax_0+by_0+cz_0+d|}{\sqrt{a^2+b^2+c^2}}`, normalização de `(a,b,c)` antes de `|d_1-d_2|`, `d(r,\pi)` para reta paralela | 22 min / 15 min | `Parte_4` p. 50–52, 59–61; `L10` Ex. 5–9 |
| **`E10`** | Revisão Cumulativa do Estágio E | `E06`, `E08`, `E09` | Posições relativas, planos contendo retas, interseções e distância entre retas reversas / planos | 25 min / 18 min | `Parte_4` p. 1–61; `L8`–`L10` |

### Estágio F — Seções Cônicas (`\mathbb{R}^2`) e Superfícies Quádricas (`F01`–`F08`)

| Bloco | Título e Micro-habilidade Foco | Pré-req. | Conteúdo Novo | Tempo Prática / Checagem | Fontes (`[DOC]`/`[INF]`) |
|---|---|---|---|---|---|
| **`F01`** | Parábola na Origem (`x^2=2py` e `y^2=2px`) | `D04` | Vértice `V(0,0)`, foco, reta diretriz, parâmetro `p`, eixo de simetria, concavidade | 18 min / 12 min | `P3` p. 165–171; `L11` Ex. 1–2 |
| **`F02`** | Parábola Transladada, Completamento de Quadrados e 3 Pontos | `F01`, `C03` | Translação `V(h,k)`, completamento de quadrado, ajuste por 3 pontos (`y=ax^2+bx+c`) | 22 min / 15 min | `P3` p. 169–171; `L11` Ex. 3–6 |
| **`F03`** | Elipse na Origem e Circunferência (`a^2=b^2+c^2`) | `D04` | Semi-eixos `a > b`, eixos maior horizontal vs. vertical, focos, excentricidade `e=c/a < 1`, circunferência (`a=b, e=0`) | 20 min / 14 min | `P3` p. 172–177; `L11` Ex. 7–8 |
| **`F04`** | Elipse Transladada e Completamento de Quadrados | `F03`, `F02` | Fatoração `A(x^2 + bx) + B(y^2 + dy)`, centro `C(h,k)`, vértices, focos e excentricidade | 22 min / 15 min | `P3` p. 176–177; `L11` Ex. 9–10 |
| **`F05`** | Hipérbole na Origem e Assíntotas (`c^2=a^2+b^2`) | `F03` | Termo positivo define eixo real (`a`!), focos, `e=c/a > 1`, assíntotas (`\pm b/a` vs `\pm a/b`), hipérbole equilátera | 22 min / 15 min | `P3` p. 178–182; `L11` Ex. 11–12 |
| **`F06`** | Hipérbole Transladada e Reconhecimento Geral de Cônicas (sem `xy`) | `F05`, `F04` | Armadilha do sinal ao dividir lado direito negativo (`9(x-3)^2 - 4(y-1)^2 = -36`), classificação geral por `A, C` | 24 min / 16 min | `P3` p. 181–184; `L11` Ex. 13–15 |
| **`F07`** | Superfícies Quádricas Canônicas e Traços `[INF/AUS]` | `F03`, `F05`, `E06` | Classificação das 6 quádricas centradas/não-centradas (elipsoide, hiperboloides de 1 e 2 folhas, paraboloides elíptico e hiperbólico, cone e cilindros) por sinais e traços coordenados | 22 min / 15 min | `Planejamento` Sem. 13–14 `[INF/AUS]` |
| **`F08`** | Revisão Cumulativa do Estágio F | `F06`, `F07` | Completamento de quadrados em parábola, elipse e hipérbole + identificação de quádricas por traços | 24 min / 16 min | `P3` p. 165–184; `L11` |

### Estágio G — Integração Geral e Simulados por Avaliação (`G01`–`G06`)

| Bloco | Título e Micro-habilidade Foco | Pré-req. | Conteúdo Novo | Tempo Prática / Checagem | Fontes (`[DOC]`/`[INF]`) |
|---|---|---|---|---|---|
| **`G01`** | Simulado Integrador P1 — Matrizes, Determinantes e Inversa | `A09`, `B09` | Revisão mista P1: operações/especiais + triangulação + `[A\|I]` + equação matricial | 25 min / 18 min | `Planejamento` Sem. 1–4; `L1`–`L4` |
| **`G02`** | Simulado Integrador P2 (Parte 1) — Sistemas Lineares e Parâmetros | `C08` | Escalonamento `m x n`, `C_A, C_V, g`, homogêneos não-triviais e discussão paramétrica | 25 min / 18 min | `Planejamento` Sem. 5–6; `L5` |
| **`G03`** | Simulado Integrador P2 (Parte 2) — Vetores e Produtos | `D10` | Combinação linear, ângulos/projeção, áreas (`1/2`) e volumes (`1/6`) com parâmetros | 25 min / 18 min | `Planejamento` Sem. 7–10; `L6`–`L7` |
| **`G04`** | Simulado Integrador P3 (Parte 1) — Retas, Planos e Distâncias | `E10` | Equações de retas e planos, posições relativas, interseções e distâncias exatas | 25 min / 18 min | `Planejamento` Sem. 11–12; `L8`–`L10` |
| **`G05`** | Simulado Integrador P3 (Parte 2) — Cônicas e Quádricas | `F08` | Completamento de quadrados em cônicas transladadas + classificação de quádricas | 25 min / 18 min | `Planejamento` Sem. 13–15; `L11` |
| **`G06`** | Simulado Geral Completo `MAT121` (Preparação Reavaliação) | `G01`–`G05` | Síntese completa dos 6 estágios integrando álgebra matricial, geometria vetorial e cônicas/quádricas | 25 min / 18 min | Toda a disciplina `MAT121` |
