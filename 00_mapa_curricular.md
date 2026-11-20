# Arquitetura Curricular e Mapa Completo do Curso — Algoritmos e Programação em C (UTFPR-PG)

> **Nota de Identidade Pedagógica:** Este curso adota metodologia de **Preparação Intensiva** (aprendizagem por domínio, micro-passos graduados e prática independente).  
> **Escopo e Fontes:** Todo o escopo técnico é ancorado na auditoria das fontes de `CC61A - Algoritmos` da UTFPR – Campus Ponta Grossa (`C:\Users\d7opa\Documents\Algoritmos`), registrada em [00_inventario_fontes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/00_inventario_fontes.md) (**Auditoria parcial com lacunas documentadas**).  
> **Legenda:** `[DOC]` = explicitamente documentado nas fontes; `[INF]` = inferência ou decisão metodológica apoiada nos materiais; `[AUS/AMB]` = lacuna/ambiguidade nas fontes.

---

## 1. Fundamentos Pedagógicos do Curso

### 1.1 Progressão em Estágios e Micro-Blocos
- **Estrutura Modular:** O curso organiza-se em **8 estágios (`A` a `H`)** totalizando **73 blocos**.
- **Micro-habilidade única:** Cada bloco instrutivo concentra-se em **uma única micro-habilidade nova**, isolada de saltos conceituais simultâneos.
- **Blocos de Revisão e Integração:** Ao final dos Estágios `A` a `G`, há um bloco exclusivo de revisão cumulativa (`A10`, `B10`, `C10`, `D10`, `E08`, `F10`, `G09`) que combina habilidades já dominadas. A integração abrangente fica reservada ao **Estágio H** (`H01`–`H06`).
- **Pré-requisitos acíclicos (DAG):** Todo bloco declara seus pré-requisitos estritamente anteriores; nenhum bloco utiliza conceitos ainda não formalizados em blocos precedentes. Pré-requisitos básicos ausentes da ementa (comandos mínimos de terminal Linux em `A02`; potências de 2 e $\lceil \log_2 T\rceil$ em `A08`) são incluídos e sinalizados explicitamente.

### 1.2 Arquitetura de Sessões (15 a 25 Minutos — Estimativas Iniciais)
- **Duração-alvo por sessão:** **15 a 25 minutos**. Blocos de maior densidade cognitiva são divididos em **2 sessões** (30–50 minutos acumulados). Todos os tempos são **estimativas iniciais sujeitas à calibração** na Fase 2 (piloto) e no uso contínuo.
- **Separação explícita de tempos:** Cada bloco discrimina três parcelas:
  1. **Resolução:** leitura das instruções/exemplos e execução da bateria de exercícios.
  2. **Correção:** autocorreção guiada pelo gabarito e conferência/compilação.
  3. **Recuperação (quando necessária):** revisão pontual de erro e aplicação de variante equivalente.

### 1.3 Apresentação e Retirada Gradual de Apoio
- **Instruções curtas e suficientes:** Síntese direta da regra técnica e armadilhas críticas, sem texto discursivo longo.
- **Modelagem em 1 ou 2 exemplos resolvidos:** Todo bloco novo inicia com 1 ou 2 exemplos comentados passo a passo.
- **Gradação sistemática do apoio:**  
  `1. Exemplo resolvido → 2. Completar solução (lacunas/esqueleto) → 3. Resolver com pistas (restrições/dicas de borda) → 4. Resolver sozinho (enunciado limpo)`.
- **Leitura e Teste de Mesa antes do código:** Nos blocos introdutórios de conceitos de fluxo, memória, operadores, laços, vetores, ponteiros e recursão, os primeiros itens exigem rastreamento manual (*teste de mesa* sem compilador) antes da escrita independente de código, refletindo diretamente o estilo avaliativo documentado nas Aulas e Listas 3, 4, 5, 10 e 11.

### 1.4 Critério de Domínio, Fluência e Recuperação
- **Registro separado de tentativas:** Na ficha de acompanhamento (`acertos_iniciais` vs. `acertos_apos_correcao`), registram-se separadamente os acertos de **1ª tentativa** e os obtidos **após autocorreção**.
- **Autocorreção ≠ Avanço:** A autocorreção consolida a aprendizagem, mas **não basta** para liberar o próximo bloco.
- **Checagem Independente de Domínio:** Todo bloco exige conclusão de uma mini-checagem de **2 a 4 questões inéditas equivalentes** (proporcional à carga do bloco), **sem consulta ao gabarito**, com **100% de acerto**.
- **Papel do tempo:** O tempo de resolução serve exclusivamente como **indicador complementar de fluência**, nunca como substituto da correção lógica e da compreensão.
- **Recuperação direcionada:** Em caso de falha na bateria ou na checagem, identifica-se o erro específico, aplica-se recuperação direcionada e realiza-se uma **variante equivalente** do bloco.
- **Regra das 2 tentativas:** Após **duas tentativas malsucedidas** no mesmo bloco, é **proibido repetir o bloco indefinidamente**; o orientador investiga e reabilita os **pré-requisitos** listados no bloco antes de nova tentativa.
- **Desafios opcionais:** Quando presentes (como no Estágio H), permanecem estritamente dentro da ementa da UTFPR-PG, são marcados como `[OPCIONAL]` e **nunca bloqueiam o avanço**.

---

## 2. Visão Geral dos Estágios, Justificativa de Blocos e Dificuldade

### 2.1 Estrutura dos 8 Estágios (73 Blocos Totais)

| Estágio | Título | Blocos | Qtd | Ajuste vs. ~10 Blocos e Justificativa (`[INF]`) | Perfil de Dificuldade nas Fontes (`[DOC]` / `[INF]`) |
|---|---|---|---:|---|---|
| **A** | Fundamentos, Ambiente C, Variáveis e Representação | `A01`–`A10` | **10** | Padrão exato (10 blocos). | **Introdutório / Básico:** `Aula_01`–`Aula_04` (conceitos, GCC/Linux, `printf`/`scanf`, troca com `aux`, binário, `sizeof`, `0.1f+0.2f`). |
| **B** | Expressões, Operadores e Estruturas Condicionais | `B01`–`B10` | **10** | Padrão exato (10 blocos). Inclui `B06` (`&&`/`\|\|`/`!`, tabela-verdade) para suprir lacuna frente à Ementa. | **Básico a Intermediário:** `Aula_05`–`08_v2` e `Lista1`–`Lista3` + `Lista8` Q2 (Bhaskara, descontos/fretes, bolsa com ordem estrita, parque `&&`/`\|\|`, data, triângulo, `switch` aninhado e *fall-through*). |
| **C** | Estruturas de Repetição e Rastreamento de Laços | `C01`–`C10` | **10** | Padrão exato (10 blocos). Inclui `C04` (`do-while`) pela Ementa vigente. | **Básico a Avançado:** `Aula_09`–`11` e `Lista4`–`Lista5` + `Lista8` Q3–Q5 (subtrações sem `%`, Euclides, laço infinito da Lista 5 Q1, série $e$ com $\varepsilon$, série **Prova UFPR 2017**, calendário). |
| **D** | Vetores Unidimensionais e Strings | `D01`–`D10` | **10** | Padrão exato (10 blocos): integra Vetores (`D01`–`D05`) e Strings (`D06`–`D09`) + Revisão (`D10`), espelhando a transição 1D efetiva das Aulas 11–13 (`D09` prepara Matrizes 2D). | **Básico a Avançado:** `Aula_11`–`13` e `Lista6`–`Lista7` + `Lista8` Q6–Q8 (1 percurso, particionamento e subvetor com sobreposição **UFPR 2017**, convolução, espaços extras, palíndromo *in-place*, César, grade `L×C` em vetor 1D). |
| **E** | Matrizes Bidimensionais e Processamento Matricial | `E01`–`E08` | **8** | **Ajuste (-2):** `Aula_14`–`15` e `Lista9` cobrem apenas manipulação direta de matrizes 2D; funções com matrizes ficam em `F07` e filtros PGM em `H02`–`H04`. 8 blocos evitam fragmentação artificial preservando 1 micro-habilidade por bloco. | **Básico a Avançado:** `Aula_14`–`15` e `Lista9` (fatiamento, somas linha/coluna, diagonais, transposta, simetria, produto $A\cdot B$ triplo laço [Entregar], limiarização PGM P2). |
| **F** | Modularização, Funções, Ponteiros e Multi-Arquivo | `F01`–`F10` | **10** | Padrão exato (10 blocos). Incorpora `F09` (`Aula_20`: pré-processamento, compilação vs. interpretação, Ementa item 11). | **Básico a Avançado:** `Aula_16`–`20` e `Lista10` (protótipos, escopo vs. vida, cópia por valor, `&`/`*`, depuração `*temp` [Entregar], múltiplos retornos `const`, remoção *in-place* [Entregar], `m[][3]`, `.h`/`.c` `.zip` [Entregar]). |
| **G** | Recursividade e Pilha de Execução | `G01`–`G09` | **9** | **Ajuste (-1):** `Aula_21`–`24` e `Lista11`–`12` tratam de pilha de execução, recursão linear (inteiros/vetores/strings), Fibonacci e potenciação rápida (sem recursão em matrizes ou árvores gerais). 9 blocos cobrem tudo sem diluição redundante. | **Básico a Avançado:** `Aula_21`–`24` e `Lista11`–`12` (rastreio sem executar, proibição de laços, `maior` $O(n)$, `media` recursiva [Entregar], impressão no retorno [Entregar], `remover` *in-place* sem auxiliar [Entregar], Fibonacci vs. `n/2`). |
| **H** | Integração Geral e Projeto Modularizado (PGM) | `H01`–`H06` | **6** | **Ajuste (-4):** Estágio exclusivamente integrador (sem tópico inédito da ementa), mapeado às 6 etapas reais do `Trabalho_Algoritmos.pdf` (5 arquivos, brilho/limiar, matriz aux + blur, mediana, menu `do-while`/`switch`, testes/arguição oral). | **Integrador (Consolidação):** `Trabalho_Algoritmos.pdf` e `Apresentacao_Trabalho_Algoritmos.pdf` (5 arquivos `.h`/`.c`, bordas em blur `3/5/7` e mediana `3×3`, operações sucessivas, arguição com alteração ao vivo). |

---

## 3. Mapa Detalhado dos 73 Blocos

> **Padronização do Critério de Domínio em Todos os Blocos:** Em cada bloco, (1) `acertos_iniciais` e `acertos_apos_correcao` são registrados em colunas separadas; (2) a autocorreção é obrigatória antes da checagem, mas não libera avanço; (3) a liberação exige **100% de acerto na checagem independente** específica do bloco, sem consulta ao gabarito; (4) o tempo é medido apenas como indicador de fluência; (5) após **2 tentativas malsucedidas**, investigam-se os pré-requisitos listados no bloco.

---

### Estágio A — Fundamentos de Algoritmos, Ambiente C, Variáveis e Representação de Dados (`A01`–`A10`)

#### `A01` — Problemas Computacionais, Algoritmos e Abstração
- **Micro-habilidade foco:** Decompor um enunciado em entradas, processamento passo a passo finito e saídas, distinguindo problema, abstração, algoritmo e programa.
- **Pré-requisitos:** Nenhum pré-requisito de programação (`—`).
- **Conteúdo novo:** Problema computacional (entrada/saída), algoritmo (sequência, finitude, instruções elementares), abstração em níveis, linguagem de máquina vs. alto nível, compilador e programa.
- **Conteúdo revisado:** Conhecimentos prévios cotidianos/escolares (Bhaskara, Pitágoras, regras de cálculo).
- **Tipos de exercício:** Leitura de casos e identificação de E/S; completar passos faltantes em algoritmos em português estruturado; ordenação de passos com pistas; redação independente de algoritmo finito em linguagem natural.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (20 min) — Resolução: 12 min | Correção: 4 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 análise de E/S e abstração, 1 correção de algoritmo não-finito/fora de ordem, 1 algoritmo em passos finitos), sem consulta ao gabarito, 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 1); `Aula_01_Algoritmos.pdf` p. 2–12, 21–32; `Lista8_Algoritmos_Revisao.pdf` p. 1 (Ex. 1a–b).

#### `A02` — Anatomia de um Programa em C e Compilação no GCC/Linux
- **Micro-habilidade foco:** Escrever a estrutura mínima compilável em C (`#include <stdio.h>`, `int main(void)`, `return 0;`, comentários) e compilar/executar via `gcc` no terminal Linux.
- **Pré-requisitos:** `A01`. *(Inclui pré-requisito operacional básico justificado `[INF]`: comandos mínimos de terminal Linux `pwd`, `ls`, `cd` e `./executavel` para viabilizar o ambiente exigido em `Aula_00` p. 3 e `Aula_02` p. 4.)*
- **Conteúdo novo:** Estrutura básica do programa em C, diretiva `#include <stdio.h>`, função `main`, ponto-e-vírgula `;`, comentários `//` e `/* */`, diferenciação maiúsculas/minúsculas (*case-sensitive*), fluxo `.c → gcc → executável`.
- **Conteúdo revisado:** Diferença entre algoritmo e programa implementado (`A01`).
- **Tipos de exercício:** Leitura de código e caça a erros de sintaxe (sem `;`, `Main` maiúsculo, comentário aberto); completar esqueleto mínimo; compilar e executar com pistas de comando `gcc`; criar do zero um programa mínimo válido sem erros de compilação.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (20 min) — Resolução: 11 min | Correção: 5 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 diagnóstico de erro de sintaxe sem compilar, 1 comentário/estrutura válida, 1 criação e compilação limpa via `gcc` de programa mínimo), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (itens 1, 11); `Aula_00_Algoritmos.pdf` p. 3; `Aula_02_Algoritmos.pdf` p. 2, 4–8, 10, 13; `Lista8_Algoritmos_Revisao.pdf` p. 1 (Ex. 1c).

#### `A03` — Saída Formatada com `printf` e Sequências de Escape
- **Micro-habilidade foco:** Construir saídas textuais exatas no terminal usando `printf`, aspas duplas e sequências de escape (`\n`, `\t`, `\"`, `\\`).
- **Pré-requisitos:** `A02`.
- **Conteúdo novo:** `printf("texto");`, quebra de linha `\n`, tabulação `\t`, escape de aspas `\"` e barra invertida `\\`, rastreamento caractere a caractere de saída esperada.
- **Conteúdo revisado:** Esqueleto `int main(void)`, `#include <stdio.h>`, ponto-e-vírgula e compilação com `gcc` (`A02`).
- **Tipos de exercício:** Leitura/teste de mesa (desenhar a saída exata no papel); completar chamadas `printf` com escapes faltantes; resolver com pistas (produzir múltiplas linhas em único `printf`); escrita independente reproduzindo layout exato.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (18 min) — Resolução: 10 min | Correção: 4 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 previsão exata de saída com `\n`/`\t`/`\\`, 1 caça ao bug de aspas/escape, 1 programa com única chamada `printf` multilinhas), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 4); `Aula_02_Algoritmos.pdf` p. 12–15 (incluindo Exercício p. 15).

#### `A04` — Identificadores, Palavras Reservadas e Declaração de Variáveis
- **Micro-habilidade foco:** Validar identificadores segundo as regras do C e declarar variáveis com os tipos primitivos básicos (`char`, `int`, `float`, `double`).
- **Pré-requisitos:** `A02`.
- **Conteúdo novo:** Conceito de variável na memória (conteúdo inicialmente indeterminado), regras de formação de identificadores (`a-z`, `A-Z`, `0-9`, `_`, sem iniciar com dígito, sem espaços/acentos/`&`), palavras reservadas, tipos básicos (`char`, `int`, `float`, `double`, `void`).
- **Conteúdo revisado:** *Case-sensitivity* em C e comentários (`A02`).
- **Tipos de exercício:** Classificação válido/inválido com justificativa; caça ao bug em declarações; completar declarações adequadas ao domínio do dado; declaração independente para cenários descritos.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (18 min) — Resolução: 10 min | Correção: 4 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 4 itens inéditos (classificação de identificadores, detecção de palavra reservada/*case*, escolha de tipo para 3 dados reais e declaração correta em C), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 2); `Planejamento_de_Aula_Algoritmos.pdf` p. 1 (28/08); `Aula_02_Algoritmos.pdf` p. 8–9, 16–18.

#### `A05` — Saída de Variáveis, Casas Decimais e Constantes (`#define` e `const`)
- **Micro-habilidade foco:** Exibir valores de variáveis formatados com especificadores (`%d`/`%i`, `%f`, `%.Nf`, `%c`, `%e`) e definir constantes simbólicas (`#define` e `const`).
- **Pré-requisitos:** `A03`, `A04`.
- **Conteúdo novo:** Especificadores de formato do `printf`, precisão de exibição (`%.2f`, `%.3f`, arredondamento visual), inicialização na declaração, definição de constantes via macro `#define NOME valor` (sem `;`) e qualificador `const tipo NOME = valor;`.
- **Conteúdo revisado:** `printf` com `\n` (`A03`), tipos primitivos (`A04`).
- **Tipos de exercício:** Previsão de saída com `%.1f`/`%.2f`; completar formato de `printf` e constantes; resolução com pistas (perímetro com `#define PI` sem cálculo ainda não visto); escrita independente exibindo ficha de dados formatada.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (20 min) — Resolução: 11 min | Correção: 5 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (previsão de `%.2f` e `%c`, correção de erro de `#define` com `;` ou tentativa de alterar `const`, programa completo usando constante e múltiplos especificadores), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (itens 2, 4); `Aula_02_Algoritmos.pdf` p. 20–24; `Aula_03_Algoritmos.pdf` p. 12.

#### `A06` — Entrada de Dados com `scanf` e Operador `&`
- **Micro-habilidade foco:** Ler dados digitados no teclado com `scanf` usando o especificador compatível (`%d`, `%f`, `%lf`, `%c`) e o operador de endereço `&`.
- **Pré-requisitos:** `A05`.
- **Conteúdo novo:** `scanf`, papel intuitivo do operador `&` ("endereço na memória"), compatibilidade estrita especificador × tipo (`%f` para `float`, **`%lf` obrigatório para `double` no `scanf`**), leitura múltipla na mesma chamada (`scanf("%d %d", &a, &b)`), regra de declarar antes de ler.
- **Conteúdo revisado:** Especificadores do `printf` e tipos primitivos (`A04`, `A05`).
- **Tipos de exercício:** Leitura de código identificando incompatibilidade `%f`/`%lf` e ausência de `&`; completar `scanf` em programa guiado; resolução com pistas; programa completo lendo `int`, `double` e `char` e imprimindo-os.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (20 min) — Resolução: 11 min | Correção: 5 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (caça ao bug de falta de `&` e `%f` em `double`, completar leitura múltipla, programa completo de entrada e eco formatado), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 4); `Planejamento_de_Aula_Algoritmos.pdf` p. 1 (28/08); `Aula_03_Algoritmos.pdf` p. 3–8, 13–14.

#### `A07` — Atribuição (`=`), Modelo de Memória e Troca com Variável Auxiliar
- **Micro-habilidade foco:** Executar teste de mesa rastreando sobrescritas de memória com o operador de atribuição `=` e realizar troca segura entre duas variáveis via variável auxiliar `aux`.
- **Pré-requisitos:** `A06`.
- **Conteúdo novo:** Semântica de `variavel = expressao;` (avalia direita → grava na esquerda), três estados na memória (declaração indeterminada `?`, atribuição, leitura), erro de sobrescrita direta (`a = b; b = a;`) e padrão clássico de troca em 3 passos (`aux = a; a = b; b = aux;`).
- **Conteúdo revisado:** Declaração, inicialização (`A04`–`A05`), leitura com `scanf` (`A06`).
- **Tipos de exercício:** Teste de mesa passo a passo desenhando caixa de memória após cada linha; identificar por que `a = b; b = a;` perde valor; completar troca de 3 variáveis (rotação); programa completo lendo dois valores, trocando e exibindo antes/depois.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (20 min) — Resolução: 11 min | Correção: 5 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (rastreamento de sequência de 5 atribuições com tabela de memória, previsão da falha sem `aux`, rotação cíclica de 3 variáveis testada via compilação), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 4); `Aula_03_Algoritmos.pdf` p. 9–12, 15–23.

#### `A08` — Bits, Bytes, Sistema Binário e Capacidade de Representação
- **Micro-habilidade foco:** Converter inteiros simples entre base 10 e base 2 e calcular capacidade de representação ($2^n$) e quantidade mínima de bits ($\lceil \log_2 T \rceil$).
- **Pré-requisitos:** `A04`. *(Inclui pré-requisito matemático básico justificado `[INF]`: potências inteiras de 2 de $2^0$ a $2^{16}$ e definição operacional de $\lceil \log_2 T \rceil$ como menor $n$ tal que $2^n \ge T$, exigidos em `Aula_04` p. 5–9.)*
- **Conteúdo novo:** Bit e byte (`1 byte = 8 bits`), fórmula direta $T(n) = 2^n$, problema inverso $n = \lceil \log_2 T \rceil$, sistema posicional binário (e menção ao hexadecimal base 16).
- **Conteúdo revisado:** Código ASCII em bytes e tipos básicos (`A04`).
- **Tipos de exercício:** Exercícios inteiramente no papel/rastreio: decomposição posicional binária (`1101_2` → `13_10`), cálculo de valores representáveis ($n$ bits → $2^n$), problema inverso ($\lceil \log_2 T \rceil$ para quantidades como 5, 1000, 1 milhão), comparação de bases.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (22 min) — Resolução: 13 min | Correção: 5 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 4 questões inéditas no papel (2 conversões binário↔decimal, 1 cálculo $2^n$, 1 cálculo $\lceil \log_2 T \rceil$), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 3); `Planejamento_de_Aula_Algoritmos.pdf` p. 1 (31/08); `Aula_04_Algoritmos.pdf` p. 4–9, 19–20.

#### `A09` — Tamanhos de Tipos, Modificadores (`sizeof`) e Precisão de Ponto Flutuante (`float` vs `double`)
- **Micro-habilidade foco:** Selecionar tipos inteiros com modificadores (`short`, `long`, `signed`, `unsigned`) ou reais (`float` vs `double`) considerando limites de memória (`sizeof`) e erros de aproximação binária em ponto flutuante.
- **Pré-requisitos:** `A05`, `A08`.
- **Conteúdo novo:** Modificadores `short`, `long`, `signed`, `unsigned`, operador `sizeof` com especificador `%zu`, faixas típicas em Linux x86-64, impossibilidade de representar todos os reais em bits finitos, precisão de `float` (4 bytes, ~6–7 dígitos) vs `double` (8 bytes, ~15–16 dígitos), sufixo `f` (`0.1f`), experimento `0.1f + 0.2f != 0.3`.
- **Conteúdo revisado:** Capacidade com $2^n$ (`A08`), especificadores `%d`/`%f`/`%lf` (`A05`–`A06`).
- **Tipos de exercício:** Previsão de intervalos com `signed`/`unsigned`; completar programa que inspeciona `sizeof` e imprime `0.1f` com `%.20f`; escolha justificada de tipo para problemas reais; pequeno experimento compilado comparando `float` e `double`.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (20 min) — Resolução: 11 min | Correção: 5 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (cálculo de faixa `unsigned`/`signed` de $k$ bytes, diagnóstico de perda de precisão em `float` vs `double`, código funcional com `sizeof` e `%zu`), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (itens 2, 3); `Planejamento_de_Aula_Algoritmos.pdf` p. 1 (31/08); `Aula_02_Algoritmos.pdf` p. 19; `Aula_04_Algoritmos.pdf` p. 10–19.

#### `A10` — Revisão e Consolidação do Estágio A *(Bloco de Revisão)*
- **Micro-habilidade foco:** *(Revisão integrada do Estágio A)* Integrar conceitos básicos de algoritmos, compilação GCC, variáveis, constantes, E/S formatada, atribuição/memória e representação numérica sem introduzir conteúdo novo.
- **Pré-requisitos:** `A07`, `A09`.
- **Conteúdo novo:** Nenhum.
- **Conteúdo revisado:** `A01`–`A09` completos (E/S, escape, identificadores, `#define`/`const`, `scanf` com `&` e `%lf`, memória/troca com `aux`, binário/$2^n$, `sizeof`, `float` vs `double`).
- **Tipos de exercício:** Bateria mista sem consulta: 2 testes de mesa (atribuição/memória e conversão binária/bits), 1 caça ao bug combinando sintaxe/identificadores/`scanf`, 2 programas completos independentes (cálculo de área/salário com `double` e troca de valores lidos).
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (20 min + 20 min) — Sessão 1 (Resolução: 14 min | Correção: 6 min); Sessão 2 (Resolução: 13 min | Correção: 4 min | Recuperação se necessária: 3 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas abrangendo papel e código compilado em C99, 100% de acerto antes de liberar o Estágio B.
- **Fontes:** `[DOC]` `Aula_01`–`Aula_04`; `Aula_03_Algoritmos.pdf` p. 24 (Ex. 1 e Ex. 2); `Lista1_Algoritmos.pdf` p. 2 (Ex. 6 — comissão, após domínio de expressões em `B01` ou aqui como regra simples); `Lista8_Algoritmos_Revisao.pdf` p. 1 (Ex. 1).

---

### Estágio B — Expressões, Operadores e Estruturas Condicionais (`B01`–`B10`)

#### `B01` — Operadores Aritméticos, Divisão Inteira e Resto (`%`)
- **Micro-habilidade foco:** Avaliar expressões com `+`, `-`, `*`, `/` e `%`, prevendo com exatidão quando `/` trunca como divisão inteira vs. quando produz resultado real e decompondo quantidades com `/` e `%`.
- **Pré-requisitos:** `A10`.
- **Conteúdo novo:** Operadores `+`, `-`, `*`, `/`, `%`, distinção entre divisão inteira (`int / int`) e real (ao menos 1 operando `float`/`double`), regra de que o tipo da variável receptora **não** muda o `/` (ex.: `double r = a / b;`), uso de `%` exclusivo para inteiros, decomposição (`a = b * (a / b) + (a % b)`).
- **Conteúdo revisado:** E/S `scanf`/`printf`, atribuição e tipos `int`/`double` (`A06`–`A09`).
- **Tipos de exercício:** Previsão mental de expressões (`5/2`, `5.0/2`, `double r = 5/2;`, `17%5`, `7%10`); completar decomposição de tempo/valor; resolver com pistas; escrita independente do problema de segundos em horas/minutos/segundos.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (22 min) — Resolução: 13 min | Correção: 5 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 4 questões inéditas (2 previsões mentais de divisão/resto, 1 correção de erro `10/100 * valor`, 1 programa de decomposição inteira via `/` e `%`), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 5); `Aula_03_Algoritmos.pdf` p. 24 (Ex. 3 reposicionado); `Aula_05_Algoritmos.pdf` p. 4–13; `Lista1_Algoritmos.pdf` p. 1 (Ex. 1).

#### `B02` — Precedência Aritmética, Conversão de Tipos (*Cast*), `<math.h>` e Atribuições Compostas
- **Micro-habilidade foco:** Aplicar precedência e associatividade aritmética, forçar divisão real por *cast* explícito `(double)` e usar funções de `<math.h>` (`sqrt`) e atribuições compostas (`+=`, `-=`, `*=`, `/=`, `%=`, `++`/`--` isolados).
- **Pré-requisitos:** `B01`.
- **Conteúdo novo:** Precedência `() > */% > +-`, associatividade esquerda→direita, promoção implícita em expressões mistas, *cast* explícito (`(double)a / b`), `#include <math.h>` (`sqrt`) com compilação `-lm`, operadores compostos e `++`/`--` isolados.
- **Conteúdo revisado:** Divisão inteira vs. real (`B01`), compilação no GCC (`A02`).
- **Tipos de exercício:** Avaliação passo a passo de expressões sem computador; inserir parênteses/cast em código bugado (ex.: `(-b + sqrt(delta)) / 2 * a`); resolver fórmula de Bhaskara com pistas; escrita independente de expressão algébrica composta com `<math.h>`.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (24 min) — Resolução: 14 min | Correção: 6 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreamento de precedência + atribuições compostas, 1 correção de falta de parênteses/cast, 1 programa compilado com `-lm` usando `sqrt` e `(double)`), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 5); `Aula_02_Algoritmos.pdf` p. 5 (`-lm`); `Aula_05_Algoritmos.pdf` p. 14–24; `Lista1_Algoritmos.pdf` p. 1–2 (Ex. 2).

#### `B03` — Expressões Relacionais, Verdadeiro/Falso em C (`<stdbool.h>`) e `if` Simples
- **Micro-habilidade foco:** Formular comparações relacionais (`==`, `!=`, `<`, `>`, `<=`, `>=`), compreender o modelo lógico de C (`0` falso / não-zero verdadeiro e `<stdbool.h>`) e controlar desvios simples com `if (...) { ... }`.
- **Pré-requisitos:** `B02`.
- **Conteúdo novo:** Fluxo condicional vs. sequencial, os 6 operadores relacionais, distinção crítica `=` vs. `==`, interpretação inteira de verdadeiro/falso e `<stdbool.h>` (`bool`, `true`, `false`), sintaxe `if (condicao) { ... }`, armadilha do `;` após `if` e omissão de `{ }`.
- **Conteúdo revisado:** `%` para divisibilidade/paridade e expressões aritméticas (`B01`–`B02`).
- **Tipos de exercício:** Tabela V/F de expressões relacionais; teste de mesa de programa com múltiplos `if`s simples; caça aos 4 erros clássicos (`if (x = 5)`, sem parênteses, `;` após `if`, sem `{ }`); programas independentes de limiar simples (`>`, `>=`, `%`).
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (22 min) — Resolução: 13 min | Correção: 5 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreamento de `if` simples + caso de borda exato no limite `>`/`>=`, 1 caça ao bug `=`/`==`/`;`, 1 programa de `if` simples sem `else`), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (itens 2, 5, 6); `Aula_06_Algoritmos.pdf` p. 4–28; `Lista1_Algoritmos.pdf` p. 2 (Ex. 3, 4, 5).

#### `B04` — Desvio Condicional Composto (`if / else`) vs. `if`s Independentes
- **Micro-habilidade foco:** Escolher e implementar corretamente `if / else` para alternativas mutuamente exclusivas vs. múltiplos `if`s independentes quando mais de uma condição pode ocorrer simultaneamente.
- **Pré-requisitos:** `B03`.
- **Conteúdo novo:** Estrutura `if (...) { ... } else { ... }`, garantia de execução de exatamente um ramo, escolha consciente entre dois `if`s complementares, `if / else` ou múltiplos `if`s não-excludentes (com flag de controle para "nenhum").
- **Conteúdo revisado:** `if` simples e operadores relacionais (`B03`), `<math.h>` (`B02`).
- **Tipos de exercício:** Previsão de saída distinguindo `if`s sequenciais de `if/else`; completar programa com ramo `else` e flag de divisibilidade múltipla; escrita independente (ex.: raiz/quadrado ou crédito 30%, e divisibilidade por 10, 5 e 2 sem `else if`).
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (22 min) — Resolução: 13 min | Correção: 5 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 análise de diferenças entre `if`+`if` e `if/else`, 1 programa binário `if/else` com caso de fronteira, 1 programa com condições não-excludentes + caso "nenhum"), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 6); `Aula_07_Algoritmos.pdf` p. 3–9; `Lista2_Algoritmos.pdf` p. 1–2 (Ex. 2, 3, 5).

#### `B05` — Múltiplas Alternativas com `else if` e Ordem das Condições
- **Micro-habilidade foco:** Construir cadeias `if / else if / else` ordenando condições sobrepostas da mais restritiva/extrema para a mais geral, evitando faixas inatingíveis ou lacunas em fronteiras contínuas.
- **Pré-requisitos:** `B04`.
- **Conteúdo novo:** Cadeia `if / else if / else`, avaliação *top-down* (primeiro verdadeiro vence e encerra a cadeia), `else` final opcional, erro de ordem das condições (condição ampla bloqueando específica), codificação contígua de faixas (`< 100`, `< 300`, `< 500` sem lacuna `299.995`).
- **Conteúdo revisado:** `if / else` (`B04`), precisão de `double` em fronteiras (`A09`).
- **Tipos de exercício:** Teste de mesa de cadeia com ordem invertida (identificar ramo morto); completar cadeia de faixas de desconto/frete; resolver cálculo de frete excedente com pistas; escrita independente com faixas contínuas.
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões de prática (`20 min` + `22 min`) + checagem (`18 min`) — Sessão 1 (`E01`–`E03`: `12 min` resol. | `5 min` corr. | `3 min` recup.); Sessão 2 (`E04`–`E06`: `14 min` resol. | `5 min` corr. | `3 min` recup.); Checagem (`13 min` resol. | `5 min` conf.). *(Recalibrado na revisão dos pilotos da Fase 2.)*
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreamento detectando erro de ordenação em `else if`, 1 definição de faixas contínuas sem lacuna, 1 programa completo de faixas com cálculo excedente), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 6); `Aula_07_Algoritmos.pdf` p. 10–15; `Lista2_Algoritmos.pdf` p. 1 (Ex. 1); `Lista8_Algoritmos_Revisao.pdf` p. 1 (Ex. 2); `Como_Estruturar_Condicionais_no_Cálculo_de_Frete.mp4`.

#### `B06` — Operadores Lógicos (`&&`, `||`, `!`), Tabela-Verdade e Precedência Completa
- **Micro-habilidade foco:** Combinar e negar expressões booleanas usando `&&`, `||` e `!` com tabela-verdade e precedência correta (aritméticos → relacionais → `!` → `&&` → `||`).
- **Pré-requisitos:** `B03`. *(Bloco inserido explicitamente para suprir Lacuna L1 por força da Ementa vigente.)*
- **Conteúdo novo:** Conjunção `&&` (E), disjunção `||` (OU), negação `!` (NÃO), tabela-verdade, avaliação em curto-circuito básica, precedência entre relacionais e lógicos (necessidade de `x >= 1 && x <= 10` em vez de `1 <= x <= 10`, e `&&` antes de `||`), parênteses defensivos.
- **Conteúdo revisado:** Operadores relacionais (`B03`), precedência aritmética (`B02`), precisão `double` em comparações (`A09`).
- **Tipos de exercício:** Preenchimento de tabela-verdade e avaliação de expressões compostas sem compilador; caça ao bug clássica (`1 <= x <= 10` e ausência de parênteses em `a || b && c`); completar condição booleana composta; escrita independente validando intervalos e regras combinadas.
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (20 min + 18 min) — Sessão 1 (Resolução: 12 min | Correção: 5 min | Recuperação: 3 min); Sessão 2 (Resolução: 11 min | Correção: 4 min | Recuperação: 3 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 4 questões inéditas (1 tabela-verdade/avaliação, 1 correção de `1 <= x <= 10` e precedência `&&`/`||`, 2 programas com regras compostas e fronteiras exatas usando `double`), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 1–2 (item 5: *"Precedência de operadores lógicos e aritméticos. Lógica booleana, valores e operadores lógicos, tabela-verdade"*); `Planejamento_de_Aula_Algoritmos.pdf` p. 1 (01/09 e 08/09); `Lista2_Algoritmos.pdf` p. 2–4 (Ex. 6, 7, 8); `Aula_08_Algoritmos_v2.pdf` p. 20 (uso de `||`).

#### `B07` — Condicionais Aninhadas, Decisões Hierárquicas e Associação do `else`
- **Micro-habilidade foco:** Estruturar decisões hierárquicas com `if` aninhado (quando a 2ª decisão depende do desfecho da 1ª) e aplicar a regra do *dangling else*.
- **Pré-requisitos:** `B05`, `B06`.
- **Conteúdo novo:** `if` aninhado vs. `else if` (decisão hierárquica vs. alternativas de mesmo nível), regra de associação do `else` ao `if` mais próximo sem `else`, prioridade estrita de verificação (ex.: frequência → nota → renda).
- **Conteúdo revisado:** `else if` (`B05`), `&&`/`||` (`B06`).
- **Tipos de exercício:** Rastreamento de código com `if` aninhado sem chaves identificando a associação do `else`; completar árvore de decisão hierárquica (bolsa / validação de data); resolução com pistas (classificação de triângulos após existência); escrita independente com validação prévia + classificação.
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (22 min + 20 min) — Sessão 1 (Resolução: 13 min | Correção: 5 min | Recuperação: 4 min); Sessão 2 (Resolução: 12 min | Correção: 5 min | Recuperação: 3 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreamento *dangling else*, 1 problema de prioridade estrita de critérios, 1 programa completo de validação + classificação com casos degenerados), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 6); `Aula_07_Algoritmos.pdf` p. 16–23; `Lista2_Algoritmos.pdf` p. 2–4 (Ex. 4, 6, 7, 8 — entrega).

#### `B08` — Múltipla Escolha com `switch / case`, `break`, `default` e *Fall-Through*
- **Micro-habilidade foco:** Implementar decisões discretas sobre expressão inteira (`int` ou `char`) usando `switch/case`, `break`, `default` e agrupamento intencional por *fall-through*.
- **Pré-requisitos:** `B04`.
- **Conteúdo novo:** Sintaxe `switch (expressao)`, restrição a constantes inteiras/`char` (proibido `float`/`double`/string/variável), `default`, efeito *fall-through* acidental vs. agrupamento intencional de rótulos `case`.
- **Conteúdo revisado:** Múltiplas alternativas (`B05` como comparação de uso).
- **Tipos de exercício:** Rastreamento sem compilador prevendo saída exata em `switch` sem `break` (`umdois`); caça ao bug em `case` com `float` ou sem `break`; completar `switch` agrupando rótulos equivalentes; escrita independente de seletor de códigos/opções com `default`.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (22 min) — Resolução: 13 min | Correção: 5 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreamento de *fall-through*, 1 correção de `switch` com `break` faltante e rótulos repetidos, 1 programa com `switch` agrupado + `default`), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 6); `Aula_08_Algoritmos_v2.pdf` p. 3–10; `Lista3_Algoritmos.pdf` p. 1–2 (Ex. 1, 2).

#### `B09` — Combinação de `switch` com `if`, `switch` Aninhado e Colapso de Intervalos
- **Micro-habilidade foco:** Combinar `if/else` com `switch`, estruturar `switch` aninhados e converter faixas discretas de inteiros em rótulos `case` via divisão inteira.
- **Pré-requisitos:** `B06`, `B07`, `B08`.
- **Conteúdo novo:** `switch` como seletor de operação combinado com `if/else if` para validação interna (modelo caixa eletrônico), `switch` aninhado (`break` por nível), transformação de intervalos em valores discretos (`nota / 10` após validação `if (nota < 0 || nota > 100)`).
- **Conteúdo revisado:** Decomposição decimal `n / 10` e `n % 10` (`B01`), `||`/`&&` (`B06`), `switch` (`B08`).
- **Tipos de exercício:** Rastreamento de `switch` aninhado (identificando alcance do `break` interno vs. externo); completar solução de número de 2 dígitos por extenso (exceções `10..19` e dezenas exatas); resolução com pistas (cardápio em 2 níveis); escrita independente combinando `if` + `switch`.
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (20 min + 20 min) — Sessão 1 (Resolução: 12 min | Correção: 5 min | Recuperação: 3 min); Sessão 2 (Resolução: 12 min | Correção: 5 min | Recuperação: 3 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreamento de `switch` aninhado, 1 programa de `if` + `switch (val / 10)` com casos de fronteira, 1 programa `switch` aninhado com `default` em ambos os níveis), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 6); `Aula_08_Algoritmos_v2.pdf` p. 11–21; `Lista3_Algoritmos.pdf` p. 2 (Ex. 3, 4).

#### `B10` — Revisão e Consolidação do Estágio B *(Bloco de Revisão)*
- **Micro-habilidade foco:** *(Revisão integrada do Estágio B)* Consolidar expressões aritméticas, precedência, *cast*, operadores lógicos, tabela-verdade e todas as estruturas condicionais (`if`, `if/else`, `else if`, aninhamento, `switch`) com foco em casos de borda.
- **Pré-requisitos:** `B09`.
- **Conteúdo novo:** Nenhum.
- **Conteúdo revisado:** `B01`–`B09` completos.
- **Tipos de exercício:** Rastreamento misto (precedência aritmética/lógica, *dangling else*, *fall-through*); caça ao bug de precisão `float` vs `double` em fronteiras; 2 problemas completos no nível das entregas da `Lista2` (regras compostas + validação/classificação) e `Lista3`.
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (22 min + 22 min) — Sessão 1 (Resolução: 14 min | Correção: 5 min | Recuperação: 3 min); Sessão 2 (Resolução: 14 min | Correção: 5 min | Recuperação: 3 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 teste de mesa lógico/condicional, 2 programas completos passando por casos normais e fronteiras exatas), 100% de acerto antes do Estágio C.
- **Fontes:** `[DOC]` `Aula_05`–`Aula_08_v2`; `Lista1`–`Lista3`; `Lista8_Algoritmos_Revisao.pdf` p. 1 (Ex. 2).

---

### Estágio C — Estruturas de Repetição e Rastreamento de Laços (`C01`–`C10`)

#### `C01` — Repetição com Pré-Condição (`while`): Anatomia, Teste de Mesa e Pós-Condição
- **Micro-habilidade foco:** Construir e rastrear manualmente laços `while` identificando inicialização, condição pré-teste, atualização, caso de 0 execuções, laço infinito e invariante pós-laço.
- **Pré-requisitos:** `B10`.
- **Conteúdo novo:** Conceito de laço e iteração, sintaxe `while (condicao) { ... }`, teste **antes** da execução (0 execuções se falsa de saída), projeto em 3 perguntas (início, parada, passo), tabela de rastreamento, garantia de negação pós-laço e causas de laço infinito.
- **Conteúdo revisado:** Atribuições compostas/`++`/`--` (`B02`), expressões lógicas (`B03`, `B06`).
- **Tipos de exercício:** Leitura e tabela de teste de mesa obrigatórias antes da escrita (prever saída, número de iterações e valor final da variável de controle); identificar laço infinito ou `;` após `while`; completar laço `while`; escrever laços simples de contagem progressiva/regressiva.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (22 min) — Resolução: 13 min | Correção: 5 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (2 testes de mesa completos — incluindo um com 0 iterações —, 1 escrita de programa com `while` de intervalo fechado), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 7); `Aula_09_Algoritmos.pdf` p. 4–12, 16–18; `Lista4_Algoritmos.pdf` p. 1 (Ex. 1, 2).

#### `C02` — Contadores e Acumuladores com `while`
- **Micro-habilidade foco:** Combinar contadores, acumuladores inicializados, filtragem condicional interna (`if` dentro do `while`) e redução iterativa sem operador `%`.
- **Pré-requisitos:** `C01`.
- **Conteúdo novo:** Padrão contador (`conta++`) vs. padrão acumulador (`soma += x`), obrigação de zerar antes do laço, filtragem seletiva dentro do laço, cálculo de resto por subtrações sucessivas (`while (resto >= M)` — cuidado crítico com `>=` vs. `>`).
- **Conteúdo revisado:** `while` pré-condição (`C01`), `if/else` (`B04`), proteção contra divisão por zero (`B03`).
- **Tipos de exercício:** Rastreamento de contador + acumulador; caça ao bug (variável não inicializada e `resto > M` falhando em múltiplos exatos); completar acumulador condicional; escrita independente (tabuada, resto por subtrações sem `%`, contagem/soma seletiva).
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (22 min) — Resolução: 13 min | Correção: 5 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreamento de acumulador/contador, 1 correção de erro `>` vs `>=` em redução, 1 programa completo com `while` + `if` interno), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 7); `Planejamento_de_Aula_Algoritmos.pdf` p. 2 (18/09); `Aula_09_Algoritmos.pdf` p. 11–15, 19–20; `Lista4_Algoritmos.pdf` p. 1–2 (Ex. 2, 3).

#### `C03` — Leituras por Sentinela e Algoritmos Iterativos com `while` (Máximo e MDC/Euclides)
- **Micro-habilidade foco:** Estruturar laços controlados por valor sentinela (sem processar a sentinela) e atualizar estado iterativo com algoritmo clássico de Euclides e busca de máximo/estatísticas.
- **Pré-requisitos:** `C02`.
- **Conteúdo novo:** Padrão *priming read* (leitura antes do laço + releitura ao final do corpo), tratamento de entrada vazia (sentinela na 1ª leitura), atualização de máximo em fluxo sem armazenar todos os valores, algoritmo de Euclides (`resto = m % n; m = n; n = resto;` enquanto `n != 0`).
- **Conteúdo revisado:** Contadores/acumuladores (`C02`), proteção de divisão por zero (`B04`).
- **Tipos de exercício:** Teste de mesa do algoritmo de Euclides inclusive com `m < n`; caça ao bug (sentinela somada/contada ou máximo iniciado em `0` com negativos/entrada vazia); completar leitura com sentinela; escrita independente (sentinela, maior real, MDC de Euclides).
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (20 min + 22 min) — Sessão 1 (Resolução: 12 min | Correção: 5 min | Recuperação: 3 min); Sessão 2 (Resolução: 13 min | Correção: 5 min | Recuperação: 4 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreio de sentinela + borda vazia, 1 rastreio/correção de ordem das atribuições em Euclides, 1 programa completo de sentinela calculando múltiplas estatísticas), 100% de acerto.
- **Fontes:** `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 2 (18/09); `Aula_09_Algoritmos.pdf` p. 13–14, 19–20; `Lista4_Algoritmos.pdf` p. 2–3 (Ex. 4, 5, 6 — entrega); `Lista8_Algoritmos_Revisao.pdf` p. 1–2 (Ex. 3).

#### `C04` — Repetição com Pós-Condição (`do-while`) e Menus Interativos
- **Micro-habilidade foco:** Implementar laços com teste ao final `do { ... } while (condicao);` garantindo pelo menos uma execução em menus iterativos e validação de entrada.
- **Pré-requisitos:** `C01`, `B09`. *(Bloco inserido explicitamente para suprir Lacuna L2 por força da Ementa vigente e preparar o menu exigido no Trabalho Prático.)*
- **Conteúdo novo:** Sintaxe `do { ... } while (condicao);` (ponto-e-vírgula obrigatório após `while (...)`), execução mínima garantida (1 vez), equivalência/diferença frente ao `while` pré-teste, construção do loop principal de menu (`switch` dentro de `do-while` repetindo até opção sair).
- **Conteúdo revisado:** `while` (`C01`), `switch/case` + `if` no padrão Caixa Eletrônico (`B09`).
- **Tipos de exercício:** Teste de mesa comparando `while` e `do-while` quando a condição inicial já é falsa; caça ao bug (falta de `;` final ou condição invertida `!=` vs `==`); completar menu de caixa eletrônico com repetição; escrita independente de menu interativo + validação de faixa.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (20 min) — Resolução: 12 min | Correção: 4 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 previsão comparativa `while` vs `do-while`, 1 correção de condição/ponto-e-vírgula, 1 programa completo de menu `do-while` + `switch` com estado acumulado), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 1–2 (item 7: *"pós-condição / teste no final"*); `Aula_09_Algoritmos.pdf` p. 3, 22 (anúncio explícito de `do-while`); `Aula_10_Algoritmos.pdf` p. 19, 22 (menção a `do`); `Trabalho_Algoritmos.pdf` p. 3–4 (menu repetido até sair).

#### `C05` — Laço Contado (`for`): Sintaxe, Padrões de Contagem, C99 e Erros *Off-by-One*
- **Micro-habilidade foco:** Escrever e converter laços contados com `for (init; cond; atualiz)` dominando os 4 padrões de contagem, passo variável, declaração `for (int i = 0; ...)` (C99) e prevenção de erros *off-by-one*.
- **Pré-requisitos:** `C02`.
- **Conteúdo novo:** Ordem exata de execução `expr1 → expr2? → corpo → expr3 → expr2?`, equivalência `for` ↔ `while`, os 4 padrões (`0..n-1`, `1..n`, `n-1..0`, `n..1`), passo arbitrário (`i += 2`, `i -= 5`), declaração C99 no `for` e escopo da variável (`-std=c99`), operador vírgula no cabeçalho, critério `for` vs `while`.
- **Conteúdo revisado:** `while` com contador (`C02`), `gcc -std=c99` (`A02`).
- **Tipos de exercício:** Conversão guiada `while ↔ for`; identificação e contagem exata de iterações nos 4 padrões (detectando `<` vs `<=` *off-by-one*); completar `for` com passo variável; escrita independente de filtragem/contagem em intervalo `1..n`.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (22 min) — Resolução: 13 min | Correção: 5 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 contagem de iterações com passo `!= 1` e erro *off-by-one*, 1 conversão `while ↔ for` respeitando escopo C99, 1 programa completo com `for` + filtros lógicos), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 7); `Planejamento_de_Aula_Algoritmos.pdf` p. 2 (21/09); `Aula_10_Algoritmos.pdf` p. 3–18; `Lista5_Algoritmos.pdf` p. 1 (Ex. 2).

#### `C06` — Rastreamento Rigoroso de `for`, Efeitos Colaterais e Comando Nulo (`;`)
- **Micro-habilidade foco:** Executar teste de mesa detalhado de laços `for` com modificações da variável de controle dentro do corpo (`i++`, divisão inteira), omissão de expressões e comando nulo (`;`).
- **Pré-requisitos:** `C05`.
- **Conteúdo novo:** Interação entre atualização no corpo e `expr3` do `for`, armadilha do `;` após `for (...)` e `while (...)` (comando nulo compilando sem erro), omissão de expressões (`expr1`/`expr3`), detecção analítica de não-terminação (laço infinito do tipo `i = 1` → `i++` → `i / 2 == 1`).
- **Conteúdo revisado:** Precedência `i++` vs `i /= 2` (`B01`–`B02`), anatomia do `for` (`C05`).
- **Tipos de exercício:** Bloco fortemente voltado a **leitura, depuração e teste de mesa sem computador**: rastrear 4 trechos traiçoeiros passo a passo (incluindo o caso exato da `Lista5` Ex. 1), diagnosticar bugs de comando nulo `;` e corrigir condições que nunca terminam.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (20 min) — Resolução: 12 min | Correção: 4 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas de rastreamento/depuração sem compilador (1 comando nulo `;`, 1 `for` com efeito colateral finito no corpo, 1 identificação e correção de laço infinito), 100% de acerto.
- **Fontes:** `[DOC]` `Aula_10_Algoritmos.pdf` p. 12, 16, 26–28; `Lista5_Algoritmos.pdf` p. 1 (Ex. 1); *(refuta erro aritmético de `Lista do Professor.pdf` p. 2)*.

#### `C07` — Controle de Fluxo em Laços (`break`, `continue`, `for (;;)`/`while (1)`) e Primalidade
- **Micro-habilidade foco:** Controlar saída antecipada (`break`) e salto de iteração (`continue`) em laços (incluindo `for (;;)`/`while (1)`) e implementar verificação de primalidade com tratamento de borda (`n <= 1`).
- **Pré-requisitos:** `C03`, `C05`.
- **Conteúdo novo:** Semântica de `break` em laços (encerra apenas o laço ou `switch` mais interno), semântica de `continue` (salta para a próxima iteração: em `for` ainda executa `expr3`, em `while` volta ao teste; não existe para `switch`), laços `for (;;)`/`while (1)` com saída intermediária, algoritmo de primalidade (caso especial `n = 1`).
- **Conteúdo revisado:** `while`/`for` (`C01`, `C05`), `break` no `switch` (`B08`), operadores `%` (`B01`).
- **Tipos de exercício:** Rastreamento passo a passo com `continue` e `break` (incluindo armadilha de `continue` antes do incremento em `while`); completar detector de número primo tratando `n <= 1`; resolução com pistas; escrita independente com saída no meio e filtragem.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (22 min) — Resolução: 13 min | Correção: 5 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreamento `continue` em `for` vs `while`, 1 diagnóstico de `break` em laço contendo `switch`, 1 programa de primalidade validado para `n = 1, 2, 4, 13`), 100% de acerto.
- **Fontes:** `[DOC]` `Aula_10_Algoritmos.pdf` p. 17, 19–25; `Lista8_Algoritmos_Revisao.pdf` p. 2 (Ex. 5).

#### `C08` — Séries Numéricas, Atualização Incremental e Convergência por Tolerância ($\varepsilon$)
- **Micro-habilidade foco:** Calcular somatórios e séries matemáticas atualizando numerador, denominador, sinal ou fatorial incrementalmente a cada iteração e interrompendo por critério de tolerância ($\varepsilon$).
- **Pré-requisitos:** `C03`, `C05`.
- **Conteúdo novo:** Atualização incremental de termos ($O(n)$ em vez de recalcular fatorial/potência do zero), alternância de sinal (`sinal = -sinal;`), prevenção de *overflow* em fatorial/potência usando `double`, laço `while` por critério `termo >= eps` **sem somar o termo que viola `< eps`**, prevenção de divisão inteira (`1.0 / fat`) e `k < n` evitando divisão por zero.
- **Conteúdo revisado:** `double` (`A09`), divisão real (`B01`), acumuladores (`C02`), `for` e `while` (`C01`, `C05`).
- **Tipos de exercício:** Teste de mesa manual dos 4 primeiros termos de uma série; caça ao bug (divisão inteira `1 / fat`, *off-by-one* causando divisão por 0 em `(n - k)^2`, somar termo `< eps`); completar série incremental; escrita independente de série contada (`for`) e por tolerância (`while`).
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (22 min + 20 min) — Sessão 1 (Resolução: 13 min | Correção: 5 min | Recuperação: 4 min); Sessão 2 (Resolução: 12 min | Correção: 5 min | Recuperação: 3 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 identificação de bug numérico/borda, 1 série com `for` incremental sem *overflow* de `int`, 1 série com `while` e tolerância $\varepsilon$ incluindo borda $\varepsilon > 1$), 100% de acerto.
- **Fontes:** `[DOC]` `Lista5_Algoritmos.pdf` p. 1–2 (Ex. 3, 4, 5 — adaptado de **Prova AED I UFPR 2017**); `Lista8_Algoritmos_Revisao.pdf` p. 2 (Ex. 4 — $\ln(1+x)$).

#### `C09` — Laços Aninhados e Formatação Tabular
- **Micro-habilidade foco:** Projetar e rastrear dois laços aninhados (`i` externo, `j` interno), tanto com limites independentes (grades) quanto dependentes (`j <= i`), controlando quebras de linha e largura fixa de saída.
- **Pré-requisitos:** `C05`, `C06`.
- **Conteúdo novo:** Execução $M \times N$ de laços aninhados, contadores distintos (`i`, `j`), posicionamento de `printf("\n")` após o laço interno, dependência do laço interno (`j <= i`), múltiplas iterações sequenciais com aritmética modular e largura fixa (`%2d`, `%3d`) para tabelas/calendários.
- **Conteúdo revisado:** `for` (`C05`), operador `%` (`B01`), formatação `printf` (`A03`, `A05`).
- **Tipos de exercício:** Tabela de rastreamento `(i, j)` e desenho da saída exata no papel; completar limites de padrão triangular e grade; resolver calendário mensal com pistas (recuo inicial + quebra semanal + largura); escrita independente de padrão tabular com laços aninhados.
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (20 min + 22 min) — Sessão 1 (Resolução: 12 min | Correção: 5 min | Recuperação: 3 min); Sessão 2 (Resolução: 13 min | Correção: 5 min | Recuperação: 4 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreamento de pares `(i, j)` dependentes desenhando saída exata, 1 correção de erro de recuo/largura tabular, 1 programa com laços aninhados dependentes ou grade formatada), 100% de acerto.
- **Fontes:** `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 2 (22/09); `Aula_11_Algoritmos.pdf` p. 4–9; `Lista5_Algoritmos.pdf` p. 2–3 (Ex. 6).

#### `C10` — Revisão e Consolidação do Estágio C *(Bloco de Revisão)*
- **Micro-habilidade foco:** *(Revisão integrada do Estágio C)* Selecionar adequadamente entre `while`, `do-while` e `for`, aplicar sentinelas, controle de fluxo, séries e laços aninhados sem erros *off-by-one*.
- **Pré-requisitos:** `C04`, `C07`, `C08`, `C09`.
- **Conteúdo novo:** Nenhum.
- **Conteúdo revisado:** `C01`–`C09` completos.
- **Tipos de exercício:** Rastreamento sem computador (laços com efeito colateral, `continue` e laço aninhado); diagnóstico de 2 bugs clássicos (sentinela e divisão por zero em série); 2 problemas integradores completos (sentinela + primalidade/séries + padrão tabular).
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (22 min + 23 min) — Sessão 1 (Resolução: 14 min | Correção: 5 min | Recuperação: 3 min); Sessão 2 (Resolução: 14 min | Correção: 5 min | Recuperação: 4 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreamento completo, 2 programas integrando repetição + condicionais nos moldes de `Lista4`–`Lista5` e `Aula` de 25/09 no Planejamento), 100% de acerto antes do Estágio D.
- **Fontes:** `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 2 (25/09); `Aula_09`–`Aula_11`; `Lista4`–`Lista5`; `Lista8_Algoritmos_Revisao.pdf` p. 1–2 (Ex. 3–5).

---

### Estágio D — Vetores Unidimensionais e Strings (`D01`–`D10`)

#### `D01` — Vetores 1D: Declaração, Índices Base 0, Inicialização e Limites de Memória
- **Micro-habilidade foco:** Declarar vetores de tamanho fixo (`#define N`), inicializar na declaração (`{...}` e `{0}`), ler com `scanf("%d", &v[i])` e percorrer sem ultrapassar os limites `[0 .. N-1]`.
- **Pré-requisitos:** `C10`.
- **Conteúdo novo:** Conceito de vetor (memória contígua homogênea), declaração `tipo v[N];` (tamanho fixo, sem VLA), dois sentidos de `[ ]` (capacidade vs. índice), base 0 (`0` a `N-1`), inicialização completa/parcial/`{0}` vs. lixo local, leitura/impressão em ordem direta e inversa (sem modificar o vetor), comportamento indefinido fora dos limites (`v[N]`).
- **Conteúdo revisado:** `#define` (`A05`), `&` no `scanf` (`A06`), padrão `for (i = 0; i < N; i++)` (`C05`).
- **Tipos de exercício:** Leitura de diagramas de memória de `v[5]` e verificação de índices válidos; caça ao bug (`i <= N` e falta de `&` em `scanf`); completar leitura + impressão reversa; escrita independente com `#define N`.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (22 min) — Resolução: 13 min | Correção: 5 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 análise de memória/índices válidos, 1 caça ao bug de inicialização/*off-by-one*, 1 programa completo de leitura + impressão direta/reversa sem alterar vetor), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 8); `Planejamento_de_Aula_Algoritmos.pdf` p. 3 (06/10); `Aula_11_Algoritmos.pdf` p. 10–29.

#### `D02` — Acumulação, Contagem Condicional e Busca de Extremos com Índices em Vetores
- **Micro-habilidade foco:** Calcular soma, contagem condicional e maior/menor elemento com seus índices em único percurso, aplicando desempate correto (`>` vs `<=` / `>=`).
- **Pré-requisitos:** `D01`.
- **Conteúdo novo:** Inicialização segura do candidato em `v[0]` (nunca `0`, falha com negativos), armazenamento simultâneo de valor e índice (`pos_maior`, `pos_menor`), desempate assimétrico (estrito `>`/`<` → **1ª ocorrência**; `>=`/`<=` → **última ocorrência**), maior e menor no mesmo percurso com dois `if`s independentes, conversão real na média `(double)soma / N`.
- **Conteúdo revisado:** Contadores/acumuladores (`C02`), `if`s independentes (`B04`), vetores 1D (`D01`).
- **Tipos de exercício:** Teste de mesa com valores negativos e empates; completar percurso único com dois `if`s; resolução com pistas (`Lista6` Ex. 1); escrita independente combinando soma/média, contagem condicional (`> x`) e extremos.
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões de prática (`22 min` + `24 min`) + checagem (`18 min`) — Sessão 1 (`E01`–`E03`: `13 min` resol. | `5 min` corr. | `4 min` recup.); Sessão 2 (`E04`–`E06`: `15 min` resol. | `5 min` corr. | `4 min` recup.); Checagem (`13 min` resol. | `5 min` conf.). *(Recalibrado na revisão dos pilotos da Fase 2.)*
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreio de desempates com negativos, 1 correção de `maior = 0` e `if/else`, 1 programa de 1 percurso achando 1º máximo e último mínimo), 100% de acerto.
- **Fontes:** `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 3 (09/10); `Aula_11_Algoritmos.pdf` p. 26; `Aula_12_Algoritmos.pdf` p. 4–13, 25; `Lista6_Algoritmos.pdf` p. 1 (Ex. 1); `Lista8_Algoritmos_Revisao.pdf` p. 3 (Ex. 6).

#### `D03` — Busca Linear, Inversão *In-Place* e Particionamento em Múltiplos Vetores
- **Micro-habilidade foco:** Executar busca linear (com `-1` e `break`), inverter um vetor *in-place* até `N / 2` e construir múltiplos vetores filtrados com índices de escrita independentes.
- **Pré-requisitos:** `D02`.
- **Conteúdo novo:** Busca sequencial (1ª ocorrência com `break` + marcador `-1`, última ocorrência, todas, contagem), inversão efetiva *in-place* trocando `v[i]` com `v[N - 1 - i]` para `i < N / 2`, particionamento em vetores separados usando contadores independentes (`k_men`, `k_mai`) e métrica de distância absoluta (`abs()` de `<stdlib.h>` ou condicional).
- **Conteúdo revisado:** Troca com `aux` (`A07`), `break` (`C07`), média `double` (`D02`).
- **Tipos de exercício:** Teste de mesa da inversão *in-place* até `N` vs `N / 2` (para `N` par e ímpar); completar particionamento sem deixar lixo em posições puladas; resolver busca do mais próximo de `x` com pistas; escrita independente de busca/inversão/particionamento.
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (20 min + 22 min) — Sessão 1 (Resolução: 12 min | Correção: 5 min | Recuperação: 3 min); Sessão 2 (Resolução: 13 min | Correção: 5 min | Recuperação: 4 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreamento de inversão `i < N` bugada, 1 problema de busca com empate/mais próximo, 1 programa de particionamento tratando vetor resultante vazio), 100% de acerto.
- **Fontes:** `[DOC]` `Aula_12_Algoritmos.pdf` p. 14–20, 26; `Lista6_Algoritmos.pdf` p. 1–2 (Ex. 2 — **Prova UFPR 2017** — e Ex. 4).

#### `D04` — Vetores de Frequência (Histograma) e Deduplicação Preservando Ordem
- **Micro-habilidade foco:** Usar um vetor de frequências por indexação indireta (`freq[v[i]]++`) para contagem/comparação de histogramas e filtrar duplicatas em faixa arbitrária preservando a ordem original.
- **Pré-requisitos:** `D03`.
- **Conteúdo novo:** Indexação indireta (`freq[v[i]]++` com vetor `int freq[10] = {0};`), comparação de histogramas de dois vetores, deduplicação por busca no prefixo já percorrido `0 .. i-1` (quando valores não cabem em vetor de contagem pequeno), impressão de histograma com `*`.
- **Conteúdo revisado:** Laços aninhados (`C09`), inicialização `{0}` (`D01`), flags lógicas (`B03`).
- **Tipos de exercício:** Rastreamento de tabela `freq[0..9]` e do prefixo `j < i`; caça ao bug (`freq` não zerado ou laço interno indo até `N` em vez de `i`); completar comparador de histogramas; escrita independente de deduplicação preservando ordem.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (24 min) — Resolução: 14 min | Correção: 6 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 teste de mesa de `freq[v[i]]++`, 1 correção de bug `j <= i` / falta de reset da flag, 1 programa completo de histograma ou deduplicação), 100% de acerto.
- **Fontes:** `[DOC]` `Aula_11_Algoritmos.pdf` p. 31 (Ex. Fixação 1); `Lista6_Algoritmos.pdf` p. 2 (Ex. 3); `Lista8_Algoritmos_Revisao.pdf` p. 3 (Ex. 7).

#### `D05` — Laços Aninhados em Vetores 1D: Subsequência com Sobreposição e Convolução Discreta
- **Micro-habilidade foco:** Implementar casamento de padrão consecutivo com sobreposição e convolução discreta 1D sobre múltiplos vetores usando indexação deslocada e reversa (`y[i + k]`, `h[M - 1 - k]`) com limites seguros (`i <= M - N`).
- **Pré-requisitos:** `D03`, `D04`.
- **Conteúdo novo:** Casamento de subvetor `p[N]` em `v[M]` (`0 <= i <= M - N`), preservação de sobreposição (incrementar `i` de `1`, nunca `+= N`), convolução válida $r[i] = \sum_{k=0}^{M-1} v[i+k]\,h[M-1-k]$ (`r` de tamanho `N - M + 1`), atenção crítica a kernel assimétrico (`h[M-1-k]` vs `h[k]`).
- **Conteúdo revisado:** Laços aninhados (`C09`), acumulador zerado por iteração externa (`C02`).
- **Tipos de exercício:** Teste de mesa manual em exemplo com sobreposição e com kernel **assimétrico** `h = {1, 2, 3}`; caça ao bug (`out-of-bounds` `i < M` ou falha de sobreposição); completar índices `i + k` e `M - 1 - k`; escrita independente de ambos os algoritmos.
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (22 min + 23 min) — Sessão 1 (Resolução: 13 min | Correção: 5 min | Recuperação: 4 min); Sessão 2 (Resolução: 14 min | Correção: 5 min | Recuperação: 4 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 análise de limite `M - N` e borda `M == N`, 1 programa de subvetor com sobreposição, 1 programa de convolução validado com kernel assimétrico), 100% de acerto.
- **Fontes:** `[DOC]` `Aula_11_Algoritmos.pdf` p. 32 (Ex. Fixação 2); `Aula_12_Algoritmos.pdf` p. 21–24; `Lista6_Algoritmos.pdf` p. 2–3 (Ex. 5 — **Prova UFPR 2017** — e Ex. 6).

#### `D06` — Strings em C: Vetor de `char`, Terminador `'\0'` e E/S Segura (`%Ns` e `fgets`)
- **Micro-habilidade foco:** Declarar e ler/exibir strings como vetores de `char` terminados em `'\0'` respeitando a regra `N + 1` e utilizando `scanf` limitado (`%Ns`) ou `fgets` (tratando `'\n'` e evitando `gets`).
- **Pré-requisitos:** `D01`.
- **Conteúdo novo:** Ausência de tipo nativo `string`, terminador `'\0'` (código `0` vs `'0'` = `48`), `'a'` vs `"a"`, regra `N + 1`, inicializações equivalentes, tamanho do vetor vs. comprimento da string, `printf("%s")`, `scanf("%19s", nome)` (sem `&`, para no espaço), `fgets(frase, N, stdin)` (lê espaços, inclui `'\n'`), proibição absoluta de `gets`.
- **Conteúdo revisado:** Vetores de tamanho fixo e limites (`D01`), `char` (`A04`).
- **Tipos de exercício:** Diagramas de memória de `char s[10]` comparando tamanho e `'\0'`; caça ao bug (`char p[4] = "casa";`, `'\0'` vs `'0'`, `scanf` com `&s` ou sem limite); completar remoção do `'\n'` após `fgets`; programa independente lendo palavra e frase segura.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (22 min) — Resolução: 13 min | Correção: 5 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreamento de memória com `'\0'`, 1 diagnóstico de erro `'0'` / `N+1` / `gets`, 1 programa completo com `fgets` removendo `'\n'` e imprimindo palavra/frase), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 2: *cadeia de caracteres*); `Aula_13_Algoritmos.pdf` p. 3–15, 19–20; `Lista7_Algoritmos.pdf` p. 1–2.

#### `D07` — Percurso Manual de Strings e Transformações de Caracteres (ASCII e `<ctype.h>`)
- **Micro-habilidade foco:** Percorrer strings manualmente até `'\0'` para contar, validar, filtrar espaços excedentes e transformar caracteres via intervalos ASCII (`'a'..'z'`, `'A'..'Z'`) ou `<ctype.h>`.
- **Pré-requisitos:** `D06`.
- **Conteúdo novo:** Laço até `s[i] != '\0'`, contagem manual de comprimento e palavras (lidando com múltiplos espaços consecutivos), aritmética ASCII (maiúscula/minúscula e deslocamento circular Cifra de César `(c - base + k) % 26 + base`), `<ctype.h>` (`toupper`), escrita em nova string com índice independente e inserção obrigatória de `'\0'` ao final.
- **Conteúdo revisado:** Strings e `fgets` (`D06`), `%` modular (`B01`), lógica de estados (`B06`).
- **Tipos de exercício:** Rastreamento manual da Cifra de César (inclusive `'x'`..`'z'`) e máquina de estados de espaços extras; completar inserção de `'\0'` no destino; resolver remoção de espaços extras com pistas; escrita independente (Cifra de César ou média de tamanho de palavras).
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (20 min + 22 min) — Sessão 1 (Resolução: 12 min | Correção: 5 min | Recuperação: 3 min); Sessão 2 (Resolução: 13 min | Correção: 5 min | Recuperação: 4 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreio de normalização de espaços e `'\0'`, 1 problema de extensão/contagem com múltiplos espaços, 1 programa completo de transformação ASCII preservando não-letras), 100% de acerto.
- **Fontes:** `[DOC]` `Aula_13_Algoritmos.pdf` p. 16–18, 24; `Lista7_Algoritmos.pdf` p. 1–3 (Ex. 1, 2, 3, 5).

#### `D08` — Biblioteca `<string.h>` e Algoritmos Clássicos de Strings (Inversão e Palíndromo *In-Place*)
- **Micro-habilidade foco:** Empregar funções de `<string.h>` (`strlen`, `strcpy`, `strcat`, `strcmp`) compreendendo por que `=` e `==` falham em strings, e implementar inversão e verificação de palíndromo *in-place*.
- **Pré-requisitos:** `D03`, `D07`.
- **Conteúdo novo:** `<string.h>`: `strlen` (não conta `'\0'`), `strcpy` (cuidado com capacidade do destino), `strcat`, `strcmp` (retorno `0`, `< 0`, `> 0`), erro de usar `=` e `==` em strings; implementação manual de comparação, inversão para segunda string sem função pronta e palíndromo *in-place* com dois índices convergentes e equivalência maiúscula/minúscula.
- **Conteúdo revisado:** Dois índices convergentes (`D03`), percurso até `'\0'` e caixa ASCII/`<ctype.h>` (`D07`).
- **Tipos de exercício:** Rastreamento de `strcmp` e dos dois índices em palíndromo (`"Arara"`, `"casa"`); caça ao bug (`str1 == str2`, `strcpy` sem espaço, esquecer `'\0'`); completar busca de última ocorrência de `'.'` (extensão); escrita independente de inversão manual e palíndromo *in-place*.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (24 min) — Resolução: 14 min | Correção: 6 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 análise `=`/`==` e retorno `strcmp`, 1 inversão manual para nova string com `'\0'`, 1 palíndromo *in-place* case-insensitive sem segunda string), 100% de acerto.
- **Fontes:** `[DOC]` `Aula_13_Algoritmos.pdf` p. 20–23, 25; `Lista7_Algoritmos.pdf` p. 1–2 (Ex. 1, 4); `Lista8_Algoritmos_Revisao.pdf` p. 3 (Ex. 8).

#### `D09` — Linearização de Grades 2D em Vetor 1D (`i * C + j` e Macro `INDICE`)
- **Micro-habilidade foco:** Mapear posições bidimensionais `(i, j)` de uma grade de `L` linhas e `C` colunas em um único vetor unidimensional usando o mapeamento por linhas `i * C + j` (e macro `INDICE(i, j)`).
- **Pré-requisitos:** `D05`, `D07`.
- **Conteúdo novo:** Representação linear (*row-major*) de grade `L × C` em vetor 1D de tamanho `L * C` (ou `L * C + 1` para `'\0'` em strings), fórmula `indice = i * C + j`, macro parametrizada `#define INDICE(i, j) ((i) * COLUNAS + (j))` (com parênteses protetores nos parâmetros), leitura linha a linha em vetor único de `char`.
- **Conteúdo revisado:** `#define` (`A05`), laços aninhados (`C09`), strings (`D06`–`D07`).
- **Tipos de exercício:** Tabela de conversão `(i, j) ↔ índice 1D`; identificar risco de omitir parênteses em macro `INDICE`; completar preenchimento de vetor `char` de `L*C+1`; escrita independente de programa lendo grade de caracteres em vetor único (proibidas matrizes) e consultando `(i, j)`.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (22 min) — Resolução: 13 min | Correção: 5 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 cálculo de índices `i*C+j` e conversão inversa `idx/C, idx%C`, 1 análise de macro sem parênteses, 1 programa completo de grade `L×C` em vetor único de `char`), 100% de acerto.
- **Fontes:** `[DOC]` `Aula_14_Algoritmos.pdf` p. 4–6; `Lista7_Algoritmos.pdf` p. 3 (Ex. 6 — proibidas matrizes).

#### `D10` — Revisão e Consolidação do Estágio D *(Bloco de Revisão)*
- **Micro-habilidade foco:** *(Revisão integrada do Estágio D)* Integrar manipulação de vetores 1D, busca/particionamento/histogramas/convolução e processamento completo de strings com `<string.h>` e linearização 1D.
- **Pré-requisitos:** `D08`, `D09`.
- **Conteúdo novo:** Nenhum.
- **Conteúdo revisado:** `D01`–`D09` completos (equivalente ao escopo completo da `Lista8_Algoritmos_Revisao.pdf`).
- **Tipos de exercício:** Bateria mista estilo revisão pré-matrizes: 1 teste de mesa (subvetor com sobreposição / macro `INDICE`), 1 caça ao bug em string sem `'\0'` / histograma, 2 problemas completos combinando vetores e strings (ex.: histograma de caracteres ou busca de padrão em vetor com remoção de espaços em frase).
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (22 min + 22 min) — Sessão 1 (Resolução: 14 min | Correção: 5 min | Recuperação: 3 min); Sessão 2 (Resolução: 14 min | Correção: 5 min | Recuperação: 3 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreamento, 2 implementações completas cobrindo vetor 1D e string sem violar limites), 100% de acerto antes do Estágio E.
- **Fontes:** `[DOC]` `Aula_11`–`Aula_13`; `Lista6`–`Lista8` completas.

---

### Estágio E — Matrizes Bidimensionais e Processamento Matricial (`E01`–`E08`)

#### `E01` — Matrizes 2D: Declaração, Armazenamento *Row-Major*, Acesso e Leitura/Escrita em Grade
- **Micro-habilidade foco:** Declarar e inicializar matrizes `tipo m[LINHAS][COLUNAS];` (tamanho fixo), compreender o armazenamento linha por linha (`m[i]` como linha `i`) e ler/exibir dados em formato de tabela.
- **Pré-requisitos:** `D10`.
- **Conteúdo novo:** Sintaxe bidimensional `[linhas][colunas]`, intervalos de índices válidos (`0..L-1`, `0..C-1`), inicialização por linhas (`{{...}, {...}}`, `{0}`), conceito de `m[i]` como vetor-linha, leitura e impressão formatada com `for` aninhados (`printf("\n")` após laço interno) e ausência de verificação de limites em C.
- **Conteúdo revisado:** Linearização `i*C+j` (`D09`), laços aninhados (`C09`), `&` em `scanf` (`A06`, `D01`).
- **Tipos de exercício:** Verificação de índices válidos/inválidos em `m[3][4]` (ex.: `m[3][1]`); leitura de diagramas *row-major*; completar laços aninhados para leitura/impressão em grade; escrita independente de leitura e exibição de matriz `3 × 4`.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (20 min) — Resolução: 12 min | Correção: 4 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 validação de índices e inicialização parcial, 1 correção de `printf("\n")` mal posicionado ou `scanf` sem `&`, 1 programa de leitura/exibição tabular `L × C`), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 8); `Planejamento_de_Aula_Algoritmos.pdf` p. 3 (16/10); `Aula_14_Algoritmos.pdf` p. 3, 7–18, 25 (Ex. 1); `Lista9_Algoritmos.pdf` p. 1 (Ex. 1a).

#### `E02` — Percurso Completo, Soma Total, Busca 2D e Extremos com Coordenadas `(i, j)`
- **Micro-habilidade foco:** Percorrer matrizes 2D com laços aninhados para calcular soma total, localizar a primeira ocorrência em busca 2D (interrompendo ambos os laços) e encontrar maior/menor valor com coordenadas `(li, co)`.
- **Pré-requisitos:** `E01`.
- **Conteúdo novo:** Soma total em matriz, candidato inicial `maior = m[0][0]` + coordenadas `(li = 0, co = 0)` com desempate estrito (`>` para 1ª ocorrência), busca em 2D usando `li = -1, co = -1`, `break` no laço interno combinado com `&& li == -1` no laço externo.
- **Conteúdo revisado:** Busca de extremos (`D02`), `break` apenas no laço interno (`C07`).
- **Tipos de exercício:** Teste de mesa de busca 2D (verificando que `break` sozinho sai só do `for` interno); completar saída antecipada com `&& li == -1`; resolver maior valor + coordenadas com pistas; escrita independente em matriz `4 × 5`.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (22 min) — Resolução: 13 min | Correção: 5 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 análise de bug de `break` em busca 2D, 1 rastreamento de desempate com valores negativos, 1 programa completo de extremos `(li, co)` + busca), 100% de acerto.
- **Fontes:** `[DOC]` `Aula_14_Algoritmos.pdf` p. 19–20; `Aula_15_Algoritmos.pdf` p. 20, 25 (Ex. 3); `Lista9_Algoritmos.pdf` p. 1 (Ex. 3).

#### `E03` — Fatiamento e Acumuladores por Linha e por Coluna
- **Micro-habilidade foco:** Fixar linhas ou colunas específicas (`m[k][j]`, `m[i][k]`) e calcular somas independentes por linha e por coluna alternando a ordem dos laços `i`/`j` com reinicialização adequada do acumulador.
- **Pré-requisitos:** `E02`.
- **Conteúdo novo:** Acesso a linha fixa `k` (indexação 0-based vs. ordinal "2ª linha" = índice 1) e coluna fixa `k`, cálculo de soma de cada linha (`i` externo, `j` interno) vs. soma de cada coluna (`j` externo, `i` interno), posicionamento obrigatório de `soma = 0;` entre linhas/colunas, ou vetores de somas por linha/coluna.
- **Conteúdo revisado:** Laços aninhados (`E01`), acumulador reiniciado (`C02`).
- **Tipos de exercício:** Rastreamento de tabela de somas identificando erro de acumulador não zerado fora do laço; completar laço invertido (`j` externo, `i` interno) para colunas; resolver fatiamento ordinal vs. 0-based com pistas; escrita independente em matriz `4 × 4` (King Cap. 8).
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (22 min) — Resolução: 13 min | Correção: 5 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 detecção de acumulador não zerado por linha/coluna, 1 conversão índice ordinal ↔ base 0, 1 programa completo imprimindo somas de cada linha e de cada coluna separadamente), 100% de acerto.
- **Fontes:** `[DOC]` `Aula_15_Algoritmos.pdf` p. 4–12, 23 (Ex. 1); `Lista9_Algoritmos.pdf` p. 1 (Ex. 1b–c, Ex. 2 — adaptado de King Cap. 8).

#### `E04` — Diagonais (Principal e Secundária), Matriz Identidade e Regiões Triangulares
- **Micro-habilidade foco:** Identificar e operar sobre a diagonal principal (`i == j`), diagonal secundária (`i + j == N - 1`), regiões acima/abaixo da diagonal (`j > i`, `i > j`) e construir/verificar matriz identidade `N × N`.
- **Pré-requisitos:** `E02`.
- **Conteúdo novo:** Relações algébricas de índices em matriz quadrada `N × N`: diagonal principal (`i == j`, acesso $O(N)$ `m[i][i]`), diagonal secundária (`i + j == N - 1`, acesso $O(N)$ `m[i][N - 1 - i]`), triângulo superior (`j > i`) e inferior (`i > j`), definição e verificação universal de matriz identidade (`1` se `i == j`, `0` se `i != j`, usando flag).
- **Conteúdo revisado:** Laços aninhados (`E01`), verificação global com flag lógica (`B03`, `D04`).
- **Tipos de exercício:** Colorir/listar índices de matriz `4 × 4` por região (`j > i`, `i == j`, `i + j == 3`); teste de mesa corrigindo o exemplo da `Aula_15` p. 24 (soma acima deve incluir `m[2][3]`, totalizando `10`); completar verificador de identidade; escrita independente de diagonais + soma triangular.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (24 min) — Resolução: 14 min | Correção: 6 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreamento de soma acima/abaixo da diagonal sem omitir elemento, 1 caça ao bug em verificação de identidade com falso positivo, 1 programa completo de diagonais + identidade), 100% de acerto.
- **Fontes:** `[DOC]` `Aula_14_Algoritmos.pdf` p. 21–22, 26 (Ex. 2); `Aula_15_Algoritmos.pdf` p. 13–15, 24 (Ex. 2 — com correção da errata aritmética de `8` para `10`); `Lista9_Algoritmos.pdf` p. 2 (Ex. 4, Ex. 6a).

#### `E05` — Transposição, Verificação de Simetria e Soma de Matrizes
- **Micro-habilidade foco:** Construir matriz transposta `T[C][L]` a partir de matriz retangular `A[L][C]`, somar matrizes elemento a elemento e verificar simetria ($A[i][j] == A[j][i]$).
- **Pré-requisitos:** `E03`, `E04`.
- **Conteúdo novo:** Distinção entre imprimir transposto vs. construir nova matriz `T[COLUNAS][LINHAS]` com `T[j][i] = A[i][j]`, gerenciamento de dimensões assimétricas (`3 × 4` → `4 × 3`), soma matricial `C[i][j] = A[i][j] + B[i][j]`, verificação de matriz simétrica ($A = A^T$, testando todo par `i, j` ou apenas `j > i` com flag).
- **Conteúdo revisado:** Dimensões e índices de matriz (`E01`, `E03`), flag universal (`E04`).
- **Tipos de exercício:** Rastreamento de dimensões de `T[COLUNAS][LINHAS]`; caça ao bug (acesso fora do limite ao tentar transpor *in-place* uma matriz não quadrada `3 × 4`); completar verificador de simetria; escrita independente de transposta `3 × 4 → 4 × 3` e soma/simetria.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (22 min) — Resolução: 13 min | Correção: 5 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 análise de troca `L`/`C` na transposta retangular, 1 rastreamento de flag de simetria, 1 programa completo construindo `T[4][3]` e verificando simetria), 100% de acerto.
- **Fontes:** `[DOC]` `Aula_15_Algoritmos.pdf` p. 16–19; `Lista9_Algoritmos.pdf` p. 2 (Ex. 5, Ex. 6b).

#### `E06` — Multiplicação de Matrizes (Triplo Laço Aninhado `i, j, k`)
- **Micro-habilidade foco:** Implementar o produto matricial $C_{L_A \times C_B} = A_{L_A \times K} \cdot B_{K \times C_B}$ coordenando três índices aninhados (`i`, `j`, `k`) e inicializando cada acumulador `C[i][j] = 0`.
- **Pré-requisitos:** `E03`, `E05`.
- **Conteúdo novo:** Compatibilidade dimensional $(L_A \times K) \cdot (K \times C_B) \to (L_A \times C_B)$, definição $C[i][j] = \sum_{k=0}^{K-1} A[i][k]\,B[k][j]$, arquitetura de 3 laços (`for i`, `for j`, `C[i][j] = 0;`, `for k`), separação de leitura/acumulação entre 3 matrizes de dimensões distintas.
- **Conteúdo revisado:** Acumulador por elemento (`E03`), indexação simultânea de múltiplos arranjos (`D05`, `E05`).
- **Tipos de exercício:** Teste de mesa manual de $2 \times 3$ por $3 \times 2$ (`Lista9` Ex. 7); caça ao bug (troca `B[j][k]` por `B[k][j]` ou `C[i][j]` sem zerar); completar limites do triplo laço; escrita independente de multiplicação matricial.
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (20 min + 22 min) — Sessão 1 (Resolução: 12 min | Correção: 5 min | Recuperação: 3 min); Sessão 2 (Resolução: 13 min | Correção: 5 min | Recuperação: 4 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreamento manual de `C[1][0]` no produto retangular, 1 correção de bug de índice `k`/inicialização de `C[i][j]`, 1 programa completo multiplicando matrizes não quadradas), 100% de acerto.
- **Fontes:** `[DOC]` `Aula_01_Algoritmos.pdf` p. 12–13 (motivação matricial); `Lista9_Algoritmos.pdf` p. 2 (Ex. 7 — marcado **Entregar**).

#### `E07` — Matrizes como Imagens em Tons de Cinza (PGM P2), Saturação `[0, 255]`, `static` e Generalização n-Dimensional
- **Micro-habilidade foco:** Processar matrizes de pixels em escala de cinza `[0, 255]` (clareamento com saturação e limiarização *in-place* em código no formato PGM P2), empregando `static` para matrizes grandes e generalizando a indexação para arranjos n-dimensionais.
- **Pré-requisitos:** `E02`.
- **Conteúdo novo:** Representação de imagem em tons de cinza (`0` preto .. `255` branco), estrutura textual do formato PGM P2 (`P2`, largura, altura, valor máximo `255`, pixels), recorte (*clamping*) nos limites `[0, 255]`, limiarização (`< L → 0`, `>= L → 255`), declaração `static int m[ALTURA][LARGURA];` para evitar estouro de pilha em matrizes grandes (`Trabalho` p. 2), extensão sintática para 3 ou $n$ dimensões (`cubo[P][L][C]`, conforme Ementa item 8).
- **Conteúdo revisado:** Condicionais de intervalo (`B04`–`B05`), percurso de matriz 2D (`E01`–`E02`).
- **Tipos de exercício:** Teste de mesa em pequena matriz `3 × 3` simulando brilho/saturação e limiarização; completar trecho de processamento em esqueleto equivalente ao `processa_imagem.c`; exercício de indexação em array 3D (`[P][L][C]`); escrita independente de rotina de transformação de matriz de pixels `0..255`.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (24 min) — Resolução: 14 min | Correção: 6 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 cálculo manual de pixel com saturação em `0` e `255` e limiar exato `== L`, 1 exercício conceitual de dimensões n-dimensionais, 1 edição/programa funcional aplicando limiarização e brilho), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 8: *Matrizes n-dimensionais*); `Aula_14_Algoritmos.pdf` p. 23–24; `Aula_15_Algoritmos.pdf` p. 21; `Lista9_Algoritmos.pdf` p. 3 (Ex. 8 — `processa_imagem.c`/`utfpr.pgm`); `Trabalho_Algoritmos.pdf` p. 1–2 (PGM P2 e `static`).

#### `E08` — Revisão e Consolidação do Estágio E *(Bloco de Revisão)*
- **Micro-habilidade foco:** *(Revisão integrada do Estágio E)* Combinar fatiamento, somas por linha/coluna, diagonais, transposição, simetria, multiplicação e processamento de pixels `0..255` em matrizes 2D.
- **Pré-requisitos:** `E06`, `E07`.
- **Conteúdo novo:** Nenhum.
- **Conteúdo revisado:** `E01`–`E07` completos.
- **Tipos de exercício:** Bateria mista estilo avaliação intermediária: 1 teste de mesa (diagonais/regiões + produto parcial), 1 caça ao bug (dimensão de transposta ou bordas de `0..255`), 2 programas completos (ex.: produto matricial + verificação de simetria/processamento de imagem `5 × 5`).
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (22 min + 22 min) — Sessão 1 (Resolução: 14 min | Correção: 5 min | Recuperação: 3 min); Sessão 2 (Resolução: 14 min | Correção: 5 min | Recuperação: 3 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreamento matricial, 2 programas completos sem acesso fora dos limites), 100% de acerto antes do Estágio F.
- **Fontes:** `[DOC]` `Aula_14`–`Aula_15`; `Lista9_Algoritmos.pdf` completa.

---

### Estágio F — Modularização, Funções, Ponteiros e Compilação Multi-Arquivo (`F01`–`F10`)

#### `F01` — Introdução a Funções: `void`, `return`, Parâmetros e Argumentos (Definição Antes de `main`)
- **Micro-habilidade foco:** Definir e chamar funções próprias (`void` e com retorno tipado) posicionadas antes de `main`, distinguindo parâmetro formal, argumento e uso do valor retornado.
- **Pré-requisitos:** `E08`.
- **Conteúdo novo:** Motivação da modularização (reuso, legibilidade, responsabilidade única), anatomia `tipo nome(tipo1 p1, tipo2 p2) { ... }`, `void` em retorno e lista de parâmetros (`void linha(void)`), comando `return expr;` garantindo retorno em **todos os caminhos** de função não-`void`, declaração obrigatória do tipo de cada parâmetro (`int a, int b`).
- **Conteúdo revisado:** Estrutura do `main` (`A02`), tipos `int`/`double` (`A04`), condicionais e laços dentro de funções (`Estágios B–C`).
- **Tipos de exercício:** Rastreamento de fluxo entre `main` e função `void`/com retorno; caça ao bug (`int a, b` inválido em parâmetro, função não-`void` sem `return` em ramo `else`, definir sem chamar); completar função com lacunas; escrita independente de funções `void` e com `return`.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (22 min) — Resolução: 13 min | Correção: 5 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreamento de fluxo/expressão com retorno, 1 caça ao bug de assinatura/retorno faltante, 1 programa completo decompondo lógica em duas funções definidas antes de `main`), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 9: *procedimentos, funções, parâmetros e argumentos*); `Planejamento_de_Aula_Algoritmos.pdf` p. 4 (27/10); `Aula_16_Algoritmos.pdf` p. 3–24; `Lista10_Algoritmos.pdf` p. 1 (Ex. 1 — versão iterativa de `contar_digitos`).

#### `F02` — Protótipos de Funções, Escopo Local e Tempo de Vida
- **Micro-habilidade foco:** Separar declaração (protótipo) de definição permitindo funções após `main`, e distinguir **escopo** (visibilidade) de **tempo de vida** de variáveis locais e parâmetros.
- **Pré-requisitos:** `F01`.
- **Conteúdo novo:** Protótipo (`tipo nome(tipos);` antes de `main`), tabela comparativa Protótipo × Definição, relação com cabeçalhos padrão (`<stdio.h>`), variáveis locais independentes com mesmo nome em funções distintas, escopo (onde o nome é visível) vs. tempo de vida (enquanto a função executa).
- **Conteúdo revisado:** Funções antes de `main` (`F01`), escopo de bloco `for (int i = ...)` (`C05`).
- **Tipos de exercício:** Teste de mesa com variáveis de mesmo nome (`x`, `n`) em `main` e função auxiliar; caça ao bug (função chamada antes de ser declarada ou protótipo incompatível); completar protótipos para código com funções após `main`; escrita independente organizando `main` no topo do arquivo.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (20 min) — Resolução: 12 min | Correção: 4 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreamento de escopo/variáveis homônimas, 1 diagnóstico de função não declarada antes da chamada, 1 programa com 2 protótipos no topo e definições abaixo de `main`), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 9: *escopo de variáveis, desvio de chamada*); `Aula_17_Algoritmos.pdf` p. 3–11.

#### `F03` — Passagem por Valor em C e Limites da Cópia Local
- **Micro-habilidade foco:** Compreender que argumentos escalares em C são sempre copiados para os parâmetros (**passagem por valor**) e que modificar o parâmetro não altera a variável original do chamador.
- **Pré-requisitos:** `F02`.
- **Conteúdo novo:** Semântica de cópia na passagem por valor, diagramas de quadros de memória separados (`main` vs. função), análise da falha clássica de `void trocar(int x, int y)` por valor, paralelo com `scanf` exigindo `&`.
- **Conteúdo revisado:** Troca com `aux` (`A07`), escopo e tempo de vida (`F02`).
- **Tipos de exercício:** Exercícios de leitura e teste de mesa de memória (`ajusta(x)` e `swap` falho); responder conceitualmente por que variáveis originais permanecem intactas; distinguir quando `return` resolve (1 resultado) vs. quando é insuficiente (alterar 2 variáveis).
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (18 min) — Resolução: 10 min | Correção: 4 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas de rastreamento e análise conceitual sem compilador (1 previsão exata de saída em função que altera parâmetro escalar, 1 explicação de falha de `swap` por valor, 1 conversão de `void` falho para retorno útil via `return`), 100% de acerto.
- **Fontes:** `[DOC]` `Aula_17_Algoritmos.pdf` p. 12–17; `Aula_18_Algoritmos.pdf` p. 4–7; `Lista10_Algoritmos.pdf` p. 1–2 (Ex. 2 — parte escalar `func1`).

#### `F04` — Introdução a Ponteiros: `&`, `*`, `NULL`, Desreferenciamento e Rastreamento de Memória
- **Micro-habilidade foco:** Declarar ponteiros tipados (`int *p`), obter endereços com `&` (`%p`), inicializar com `&var` ou `NULL`, ler/modificar alvos via `*p` e rastrear passo a passo mudanças de alvo em memória.
- **Pré-requisitos:** `F03`.
- **Conteúdo novo:** Operador `&`, especificador `%p`, conceito de ponteiro (variável que armazena endereço), dois usos de `*` (declaração `int *p;` vs. desreferenciamento `*p = 25;`), declaração ≠ inicialização (lixo vs. `NULL`), comportamento indefinido ao desreferenciar ponteiro não inicializado ou `NULL`, diferença crítica `p` vs `*p`.
- **Conteúdo revisado:** Modelo de memória (`A07`), `&` no `scanf` (`A06`), troca com `aux` (`A07`).
- **Tipos de exercício:** Leitura e teste de mesa intensivo com endereços simbólicos (`0x100`, `0x104`, `0x200`) preenchendo tabela `a`, `&a`, `p`, `*p`, `&p` após redirecionar `p = &b;` (estilo `Aula_17` p. 29–39); caça ao bug (`int *p; *p = 5;` sem inicializar); completar operações indiretas.
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (20 min + 20 min) — Sessão 1 (Resolução: 12 min | Correção: 5 min | Recuperação: 3 min); Sessão 2 (Resolução: 12 min | Correção: 5 min | Recuperação: 3 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (2 testes de mesa completos com tabela de endereços/alvos após redirecionamento e 2 ponteiros no mesmo alvo, 1 diagnóstico de desreferência de ponteiro não inicializado/NULL), 100% de acerto.
- **Fontes:** `[DOC]` `Aula_17_Algoritmos.pdf` p. 18–35, 37–38 (Ex. 1, Ex. 2); `Lista10_Algoritmos.pdf` p. 2 (base conceitual de Ex. 3).

#### `F05` — Ponteiros como Parâmetros, Múltiplos Resultados e Depuração de Ponteiros
- **Micro-habilidade foco:** Passar endereços por valor (`func(&x)`) para modificar variáveis do chamador ou devolver múltiplos resultados por parâmetros de saída, além de repassar e depurar ponteiros entre funções.
- **Pré-requisitos:** `F04`.
- **Conteúdo novo:** Regra "tudo em C é passado por valor — inclusive endereços", alteração de `*p` (afeta chamador) vs. alteração de `p` (cópia local), parâmetros de entrada vs. saída, `void trocar(int *a, int *b)`, repasse de ponteiro entre funções (`ordenar(int *x, int *y)` chamando `troca(x, y)` **sem `&`**), depuração de `*temp` não inicializado em `trocar`.
- **Conteúdo revisado:** Passagem por valor (`F03`), ponteiros e `*`/`&` (`F04`).
- **Tipos de exercício:** Teste de mesa em código com `ordenar(&a, &b)` → `troca(x, y)` respondendo por que um usa `&` e o outro não; caça ao bug comentada com `//` (modelo `Lista10` Ex. 3 — `int *temp;` vs `int temp;`); escrita independente devolvendo múltiplos resultados via ponteiros.
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões de prática (`22 min` + `24 min`) + checagem (`18 min`) — Sessão 1 (`E01`–`E03`: `13 min` resol. | `5 min` corr. | `4 min` recup.); Sessão 2 (`E04`–`E06`: `15 min` resol. | `5 min` corr. | `4 min` recup.); Checagem (`13 min` resol. | `5 min` conf.). *(Recalibrado na revisão dos pilotos da Fase 2.)*
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 análise `&` vs sem `&` no repasse de ponteiros, 1 depuração comentada de wild pointer em função auxiliar, 1 implementação completa com múltiplos parâmetros de saída), 100% de acerto.
- **Fontes:** `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 4 (30/10); `Aula_17_Algoritmos.pdf` p. 36, 39 (Ex. 3); `Aula_18_Algoritmos.pdf` p. 3–14, 32–35 (Ex. 1, 3, 4); `Lista10_Algoritmos.pdf` p. 2 (Ex. 3 — entrega, Ex. 4).

#### `F06` — Funções com Vetores 1D e Modificador `const`
- **Micro-habilidade foco:** Passar vetores 1D (`int v[], int n`) e strings para funções compreendendo por que o vetor não é copiado, protegendo leituras com `const` e respeitando o limite `n`.
- **Pré-requisitos:** `F05`.
- **Conteúdo novo:** Decaimento do nome do vetor para endereço do primeiro elemento (sem cópia integral), necessidade de passar tamanho `n` junto ao vetor, equivalência `int v[]` ≡ `int *v` em parâmetros, modificação do vetor original vs. redirecionamento do ponteiro local, modificador `const int v[]` para funções somente leitura, perigo de passar `n` maior que o vetor real.
- **Conteúdo revisado:** Processamento de vetores 1D (`D02`–`D03`), parâmetros de saída por ponteiro (`F05`).
- **Tipos de exercício:** Análise comparativa `func1(int x)` vs `func2(int v[])`; completar protótipo com `const int v[]` e parâmetros de saída (`estatisticas`); resolução com pistas (`produto_interno`); escrita independente de função de consulta (`const`) e função modificadora em vetor.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (24 min) — Resolução: 14 min | Correção: 6 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 análise explicando alteração de `v[0]` vs imutabilidade de `x`, 1 diagnóstico de tentativa de modificar `const` ou passar `n` inválido, 1 implementação completa estilo `estatisticas` com `const` e ponteiros de saída), 100% de acerto.
- **Fontes:** `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 4 (09/11); `Aula_18_Algoritmos.pdf` p. 15–31, 33 (Ex. 2); `Lista10_Algoritmos.pdf` p. 1–2 (Ex. 2, Ex. 5).

#### `F07` — Funções com Matrizes 2D (`m[][COL]`), Strings *In-Place* e Composição de Funções
- **Micro-habilidade foco:** Implementar funções que recebem matrizes 2D (informando obrigatoriamente a dimensão das colunas `m[][C]`) e strings (`const char s[]` vs `char s[]` *in-place*), além de compor uma função chamando outra.
- **Pré-requisitos:** `F06`.
- **Conteúdo novo:** Regra da dimensão das colunas em parâmetros 2D (`const int m[][3], int linhas`) pelo cálculo *row-major* em memória, strings dispensando `n` graças a `'\0'`, mutação *in-place* em string com 2 índices (leitura/escrita + `'\0'`), composição de funções (`media` chamando `somar`; `relatorio` chamando `ocorrencias`).
- **Conteúdo revisado:** Matrizes 2D (`E01`, `E05`), strings (`D07`–`D08`), `const` (`F06`).
- **Tipos de exercício:** Rastreamento de fluxo entre `main() → f1() → f2()`; caça ao bug (omitir número de colunas em `int m[][]` ou esquecer `'\0'` em remoção *in-place*); completar função de matriz/string; escrita independente de `simetrica(const int m[][3])` e `remover_caractere(char s[], char c)` *in-place*.
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (22 min + 22 min) — Sessão 1 (Resolução: 13 min | Correção: 5 min | Recuperação: 4 min); Sessão 2 (Resolução: 13 min | Correção: 5 min | Recuperação: 4 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 diagnóstico da necessidade do tamanho de coluna em `m[][C]`, 1 função com matriz `const int m[][3]`, 1 função *in-place* em string sem segunda string testada no GCC), 100% de acerto.
- **Fontes:** `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 4 (03/11 e 09/11); `Aula_18_Algoritmos_parte2.pdf` p. 3–10; `Lista10_Algoritmos.pdf` p. 3 (Ex. 6 — entrega, Ex. 7).

#### `F08` — Organização Multi-Arquivo (`.h` e `.c`), Guardas `#ifndef`, Ligação no GCC e Diagnóstico de Erros
- **Micro-habilidade foco:** Decompor um programa em interface (`.h` com guardas `#ifndef`/`#define`/`#endif`), implementação (`.c`) e consumidor (`main.c`), compilando no GCC multi-arquivo e diagnosticando erros de cabeçalho e ligação.
- **Pré-requisitos:** `F07`.
- **Conteúdo novo:** Separação interface × implementação, `#include <...>` vs `#include "..."`, inclusão textual (`.h` não substitui ligação), guardas `#ifndef NOME_H / #define NOME_H / #endif`, compilação multi-arquivo `gcc main.c mod.c -o prog` (nunca passar `.h` ao `gcc`) e no Code::Blocks, diagnóstico dos 4 erros clássicos (`No such file or directory`, `undefined reference`, `multiple definition`, `conflicting types`).
- **Conteúdo revisado:** Protótipos (`F02`), composição de funções e vetores/matrizes em funções (`F06`–`F07`).
- **Tipos de exercício:** Diagnóstico sem compilar das 4 situações de erro de compilação/ligação (estilo `Aula_19` Ex. 2); completar arquivo `.h` com guardas e `#include`s; refatoração com pistas de monolítico para 3 arquivos; criação independente de módulo `vetor.h` + `vetor.c` + `main.c` compilado no GCC.
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (22 min + 23 min) — Sessão 1 (Resolução: 13 min | Correção: 5 min | Recuperação: 4 min); Sessão 2 (Resolução: 14 min | Correção: 5 min | Recuperação: 4 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 diagnóstico completo dos erros `undefined reference`/`multiple definition`/`conflicting types`, 1 escrita de `.h` válido com guardas, 1 projeto 3-arquivos compilado limpo com `gcc -std=c99 -Wall -Wextra`), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (itens 9, 11); `Aula_19_Algoritmos.pdf` p. 3–20; `Lista10_Algoritmos.pdf` p. 3 (Ex. 8 — entrega `questao8.zip`); `Apresentacao_Trabalho_Algoritmos.pdf` p. 5–6.

#### `F09` — Pré-Processamento, Etapas de Compilação e Compilação vs. Interpretação
- **Micro-habilidade foco:** Explicar e verificar as etapas de transformação do código-fonte C em executável (papel do pré-processador em `#include`/`#define`, compilação e ligação) e distinguir compilação de interpretação.
- **Pré-requisitos:** `F08`.
- **Conteúdo novo:** Conceitos e características das linguagens de programação (Ementa item 11), fluxo pré-processamento → compilação → ligação, expansão textual de `#include` e `#define`, diferença conceitual entre compilação (ex.: C) e interpretação/execução gerenciada (ex.: Python, Java), inspeção opcional de compilação sem ligar (`gcc -c`) apenas para compreensão do processo.
- **Conteúdo revisado:** Compilação multi-arquivo e `#include` (`F08`), compilador vs. linguagem de máquina (`A01`–`A02`).
- **Tipos de exercício:** Questões curtas objetivas e de análise conceitual (baseadas na `Aula_20` p. 2); rastreamento de expansão textual de `#include` com e sem guarda `#ifndef`; comparação estruturada C × Python × Java.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (18 min) — Resolução: 10 min | Correção: 4 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 4 questões conceituais inéditas (etapas código → executável, efeito do pré-processador no `#include`, diferença compilação × interpretação, comportamento de C vs Python/Java), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 11: *"Conceitos de linguagem de programação. Características das linguagens de programação. Compilação e interpretação"*); `Aula_20_Algoritmos_Roteiro_Atividade_Assíncrona.pdf` p. 1–2. *(Nota `[AUS/AMB]`: links de vídeo externos indisponíveis offline; escopo restrito aos tópicos e questões da própria `Aula_20`.)*

#### `F10` — Revisão e Consolidação do Estágio F *(Bloco de Revisão)*
- **Micro-habilidade foco:** *(Revisão integrada do Estágio F)* Integrar protótipos, escopo, passagem por valor e de endereços (`*`/`&`), funções com `const` em vetores/matrizes/strings e organização multi-arquivo `.h`/`.c`.
- **Pré-requisitos:** `F09`.
- **Conteúdo novo:** Nenhum.
- **Conteúdo revisado:** `F01`–`F09` completos.
- **Tipos de exercício:** Rastreamento de ponteiros em memória + análise de erros de ligação multi-arquivo; depuração comentada; problema completo multi-arquivo (`main.c`, `matriz_ops.h`, `matriz_ops.c` ou `texto.h`, `texto.c`) integrando parâmetros de saída por ponteiro e vetores/matrizes com `const`.
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (22 min + 23 min) — Sessão 1 (Resolução: 14 min | Correção: 5 min | Recuperação: 3 min); Sessão 2 (Resolução: 14 min | Correção: 5 min | Recuperação: 4 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreamento ponteiros/escopo, 1 diagnóstico multi-arquivo, 1 implementação modular em 3 arquivos compilada via GCC), 100% de acerto antes do Estágio G.
- **Fontes:** `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 4 (10/11); `Aula_16`–`Aula_20`; `Lista10_Algoritmos.pdf` completa.

---

### Estágio G — Recursividade e Pilha de Execução (`G01`–`G09`)

#### `G01` — Conceito de Recursividade e Pilha de Execução (Rastreamento de Chamadas e Retornos)
- **Micro-habilidade foco:** Identificar caso base, passo recursivo e progresso em funções recursivas e rastrear manualmente o empilhamento de chamadas e desempilhamento de retornos sem executar o programa.
- **Pré-requisitos:** `F10`.
- **Conteúdo novo:** Definição de função recursiva (não existe comando especial em C), tripé (caso base, passo recursivo, progresso estrito em direção ao caso base), **pilha de execução** (quadro por chamada com cópia própria dos parâmetros/locais e ponto de retorno; regra *"a chamada mais recente termina primeiro"*, sem estudar pilha como estrutura de dados), caso base inalcançável e *stack overflow*.
- **Conteúdo revisado:** Chamada/retorno de função (`F01`), escopo local e cópia por valor (`F02`–`F03`).
- **Tipos de exercício:** Bloco **100% de leitura, identificação e teste de mesa** (sem escrita livre ainda): desenhar cadeia e pilha de chamadas/retornos (`somaAte(4)`, `fat(4)`), identificar caso base/passo, detectar causa de *stack overflow* (`fat(n + 1)`).
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (22 min) — Resolução: 13 min | Correção: 5 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas sem computador (2 rastreamentos completos de chamadas e valores retornados em pilha, 1 identificação de caso base inalcançável/*stack overflow*), 100% de acerto.
- **Fontes:** `[DOC]` `ementa_algoritmos.pdf` p. 2 (itens 9, 10); `Planejamento_de_Aula_Algoritmos.pdf` p. 4–5 (13/11 e 16/11); `Aula_21_Algoritmos.pdf` p. 3–20; `Aula_22_Algoritmos.pdf` p. 3–14.

#### `G02` — Ordem de Execução na Pilha: Pré-Recursão vs. Pós-Recursão
- **Micro-habilidade foco:** Prever exatamente a saída de funções recursivas `void` diferenciando instruções executadas na descida (antes da chamada recursiva) e na subida/retorno (após a chamada recursiva).
- **Pré-requisitos:** `G01`.
- **Conteúdo novo:** Execução pré-recursiva (ida/empilhamento) vs. execução pós-recursiva (volta/desempilhamento), análise de funções com saída antes e depois da chamada (ex.: `mostrar(3)` produzindo `A3 A2 A1 B1 B2 B3` ou `3 2 1 1 2 3`), comparação estrutural Iteração × Recursão (mecanismo, parada, estado).
- **Conteúdo revisado:** Pilha de execução e caso base (`G01`).
- **Tipos de exercício:** Exercícios rigorosos de teste de mesa sem computador (prever saída completa passo a passo, ordem das chamadas, momento exato de cada `printf` e caso base — estilo `Lista11` Ex. 1 e `Aula_21` Ex. 1); completar pequena função `descer`/`subir` recursiva.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (20 min) — Resolução: 12 min | Correção: 4 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas de rastreamento sem computador (1 só pré-recursão, 1 só pós-recursão, 1 dupla saída pré+pós com 4 níveis), 100% de acerto.
- **Fontes:** `[DOC]` `Aula_21_Algoritmos.pdf` p. 21–24, 27; `Aula_22_Algoritmos.pdf` p. 15–22; `Lista11_Algoritmos.pdf` p. 1 (Ex. 1).

#### `G03` — Recursão Linear sobre Inteiros (Sem Laços) e Decomposição Decimal
- **Micro-habilidade foco:** Projetar e implementar funções recursivas lineares sobre inteiros **sem qualquer estrutura de repetição**, tratando corretamente decomposição decimal (`% 10`, `/ 10`) e argumento de terminação.
- **Pré-requisitos:** `G02`.
- **Conteúdo novo:** Escrita recursiva sob **proibição estrita de `for`/`while`**, formulação de recorrência ($P(x, n) = x \cdot P(x, n-1)$), decomposição decimal recursiva (`n < 10` como caso base vs. `n == 0` para contagem/soma de dígitos), justificação formal simples de terminação para todo $n \ge 0$.
- **Conteúdo revisado:** Decomposição decimal `% 10` e `/ 10` (`B01`, `F01`), caso base e pilha (`G01`–`G02`).
- **Tipos de exercício:** Rastreamento de `misterio(5832)` + justificativa de terminação (`Lista11` Ex. 3); completar caso base e passo recursivo em `potencia`; resolver `contar_digitos` recursivo com pistas; escrita independente de funções recursivas inteiras (sem laços).
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (22 min) — Resolução: 13 min | Correção: 5 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreamento + prova de terminação sobre inteiros, 1 correção de caso base `n == 0` vs `n < 10` para entrada `0`, 1 função recursiva compilada sem `for`/`while`), 100% de acerto.
- **Fontes:** `[DOC]` `Aula_21_Algoritmos.pdf` p. 25–26 (Ex. 2); `Lista11_Algoritmos.pdf` p. 1–2 (Ex. 3, Ex. 4 — entrega).

#### `G04` — Recursão Linear em Vetores 1D: Redução por Tamanho (`n - 1`)
- **Micro-habilidade foco:** Implementar funções recursivas lineares sobre vetores `const int v[]` reduzindo o problema pelo tamanho (`n - 1`) e combinando o último elemento `v[n - 1]` com a chamada recursiva sem usar laços.
- **Pré-requisitos:** `G03`.
- **Conteúdo novo:** Estratégia de redução em vetor mantendo o ponteiro `v` fixo e reduzindo `n` até `n == 0` (em C o vetor não é copiado), obrigatoriedade de testar `n == 0` antes de acessar `v[n - 1]` (prevenir `v[-1]`), acumulação/contagem filtrada no retorno (`soma`, `contar_positivos`, `contar_ocorrencias`).
- **Conteúdo revisado:** Vetores em função com `const int v[]` (`F06`), recursão linear sem laços (`G03`).
- **Tipos de exercício:** Teste de mesa de `calcular(v, 3)` (`Lista11` Ex. 2); completar lacunas (`/* A */`, `/* B */`, `/* C */` como `Aula_22` p. 33); resolver contagem condicional recursiva com pistas; escrita independente de `contar_positivos` e `contar_ocorrencias` (com `main` de teste).
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (24 min) — Resolução: 14 min | Correção: 6 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreamento de chamadas/retornos em vetor de 4 elementos, 1 caça ao bug `v[n]` vs `v[n-1]` / ordem do caso base, 1 função recursiva em vetor compilada sem laços), 100% de acerto.
- **Fontes:** `[DOC]` `Aula_22_Algoritmos.pdf` p. 23–28, 33–34; `Lista11_Algoritmos.pdf` p. 1–2 (Ex. 2, Ex. 5, Ex. 6 — entrega).

#### `G05` — Recursão em Vetores: Parada Antecipada, Máximo Sem Dupla Chamada e Média Recursiva
- **Micro-habilidade foco:** Formular recursões avançadas sobre vetores (`n > 0`): busca com parada antecipada (`1`/`0`), máximo com **chamada recursiva única** guardada em variável local e média aritmética recursiva `double`.
- **Pré-requisitos:** `G04`.
- **Conteúdo novo:** Múltiplos casos de parada (`n == 0 → 0` ou achou `→ 1`) em busca recursiva (`contem`), escolha do caso base `n == 1` em `maior` e `media` (quando `n == 0` não faz sentido), armazenamento do resultado recursivo em variável local evitando dupla chamada $O(2^n)$, recorrência ponderada `((n - 1) * media(v, n - 1) + v[n - 1]) / n` (ou função auxiliar recursiva de soma).
- **Conteúdo revisado:** Redução `n - 1` em `const int v[]` (`G04`), divisão real `double` (`B01`–`B02`).
- **Tipos de exercício:** Rastreamento de busca com parada antecipada (`contem` achando vs. não achando); análise de explosão de chamadas ao repetir `maior(v, n - 1)` no `return`; completar `media` recursiva; escrita independente de `maior` e `media` sem laços.
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (20 min + 22 min) — Sessão 1 (Resolução: 12 min | Correção: 5 min | Recuperação: 3 min); Sessão 2 (Resolução: 13 min | Correção: 5 min | Recuperação: 4 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 análise comparativa de custo com 1 vs 2 chamadas em `maior`, 1 implementação de busca com parada antecipada, 1 implementação de `media` recursiva validada sem laços), 100% de acerto.
- **Fontes:** `[DOC]` `Aula_22_Algoritmos.pdf` p. 29–32; `Lista11_Algoritmos.pdf` p. 2–3 (Ex. 7, Ex. 8 — entrega, adaptados de King Cap. 9 Ex. 10).

#### `G06` — Recursão em Strings por Índice Crescente (`i + 1` até `'\0'`) e Impressão no Retorno
- **Micro-habilidade foco:** Percorrer e comparar strings recursivamente avançando o índice `i + 1` até o terminador `'\0'`, aplicando processamento antes ou no retorno das chamadas.
- **Pré-requisitos:** `G03`, `G04`.
- **Conteúdo novo:** Padrão de recursão em strings por índice crescente (`int i` começando em `0`, caso base `s[i] == '\0'`), soma booleana `(s[i] == c) + contar(s, i + 1, c)`, impressão inversa **no retorno das chamadas** sem modificar a string (`imprimir_inversa`), comparação simultânea de duas strings `iguais(a, b, i)` tratando comprimentos diferentes.
- **Conteúdo revisado:** Strings até `'\0'` (`D06`, `F07`), ordem pós-recursão (`G02`).
- **Tipos de exercício:** Teste de mesa de `comprimento("SOL", 0)`, `contar("ABA", 0, 'A')` e `imprimir_inversa("CASA", 0)`; completar `iguais(a, b, i)` (casos base `a[i] != b[i]` e `a[i] == '\0'`); escrita independente de `imprimir_inversa`, `contar_vogais` e `iguais` (mantendo `const char []`, corrigindo inconsistência da `Aula_23` p. 5/7).
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (22 min) — Resolução: 13 min | Correção: 5 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreamento passo a passo com saída no retorno, 1 correção de comparação com strings de tamanhos distintos, 1 função recursiva sobre string compilada sem laços), 100% de acerto.
- **Fontes:** `[DOC]` `Aula_23_Algoritmos.pdf` p. 4–8, 15; `Lista12_Algoritmos.pdf` p. 1–2 (Ex. 1 — entrega, Ex. 2, Ex. 3).

#### `G07` — Recursão em Strings com Dois Índices (`i, j`) e Modificação *In-Place* Sem Laços
- **Micro-habilidade foco:** Implementar algoritmos recursivos sobre strings com dois índices convergentes (`i`, `j`) e mutação *in-place* (inversão e remoção de caractere) **sem estruturas de repetição e sem vetores auxiliares**.
- **Pré-requisitos:** `G06`.
- **Conteúdo novo:** Caso base `i >= j` para dois índices convergentes (crítico para strings de tamanho par e ímpar), palíndromo recursivo e inversão *in-place* `inverter(s, i + 1, j - 1)`, remoção recursiva de caractere *in-place* via dois índices (leitura/escrita) com escrita final de `'\0'` ou função auxiliar recursiva de deslocamento tratando ocorrências adjacentes.
- **Conteúdo revisado:** Dois índices convergentes e remoção *in-place* iterativa (`D08`, `F07`), recursão em strings (`G06`).
- **Tipos de exercício:** Teste de mesa em strings pares (`"ABBA"`) e ímpares (`"ARARA"`), além de ocorrências adjacentes em remoção (`"BANANA"` → `'A'`, `"AAA"` → `'A'`); completar `inverter(s, i, j)`; projeto próprio de assinatura + implementação independente de `remover` *in-place* recursivo.
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (22 min + 24 min) — Sessão 1 (Resolução: 13 min | Correção: 5 min | Recuperação: 4 min); Sessão 2 (Resolução: 14 min | Correção: 6 min | Recuperação: 4 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreamento de borda par `i >= j` e ocorrências adjacentes, 1 `inverter(char s[], int i, int j)` *in-place*, 1 `remover` recursivo *in-place* sem laços nem vetor auxiliar), 100% de acerto.
- **Fontes:** `[DOC]` `Aula_23_Algoritmos.pdf` p. 9–14; `Lista12_Algoritmos.pdf` p. 1–2 (Ex. 4, Ex. 5 — entrega).

#### `G08` — Recursão Múltipla (Fibonacci / Árvore) vs. Divisão pela Metade (Potenciação Rápida)
- **Micro-habilidade foco:** Rastrear árvores de chamadas em recursão com duas chamadas (Fibonacci) identificando recomputações, e contrastar com redução logarítmica pela metade ($n / 2$) na potenciação rápida reutilizando `int p = potencia_rapida(x, n / 2);`.
- **Pré-requisitos:** `G03`.
- **Conteúdo novo:** Recursão dupla/múltipla (`fibonacci`), dois casos base (`n == 0`, `n == 1`), árvore de chamadas binária, problema de recomputação exponencial vs. Fibonacci iterativo; potenciação rápida dividindo expoente por `2` (casos base `n == 0` e `n == 1`, par `p * p`, ímpar `x * p * p`), redução de chamadas linear (`n`) para logarítmica (`~log_2 n`), erro de chamar `potencia_rapida(x, n / 2)` duas vezes.
- **Conteúdo revisado:** Pilha e rastreamento (`G01`), potência recursiva linear (`G03`).
- **Tipos de exercício:** Desenho completo da árvore de chamadas de `fib(4)`/`fib(5)` contando chamadas repetidas; tabela de rastreamento de `potencia_rapida(2, 8)` e `potencia_rapida(2, 7)` contando multiplicações e chamadas; comparação quantitativa linear × logarítmica (`n = 32, 1024`); escrita independente com variável local `p`.
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (20 min + 20 min) — Sessão 1 (Resolução: 12 min | Correção: 5 min | Recuperação: 3 min); Sessão 2 (Resolução: 12 min | Correção: 5 min | Recuperação: 3 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 árvore de chamadas contando recomputações de `fib(1)`/`fib(2)`, 1 rastreamento de `potencia_rapida` par/ímpar, 1 implementação sem duplicar a chamada recursiva comparada à versão linear), 100% de acerto.
- **Fontes:** `[DOC]` `Aula_23_Algoritmos.pdf` p. 16–25; `Aula_24_Algoritmos.pdf` p. 3–18.

#### `G09` — Revisão e Consolidação do Estágio G *(Bloco de Revisão)*
- **Micro-habilidade foco:** *(Revisão integrada do Estágio G)* Consolidar rastreamento de pilha/árvore, recursão linear em inteiros, vetores (`n - 1`) e strings (`i + 1` / `i, j`) *in-place* sem laços, além de redução `n / 2`.
- **Pré-requisitos:** `G05`, `G07`, `G08`.
- **Conteúdo novo:** Nenhum.
- **Conteúdo revisado:** `G01`–`G08` completos.
- **Tipos de exercício:** Rastreamento sem computador (pilha pré/pós-chamada + árvore curta); diagnóstico de bugs recursivos (dupla chamada em `maior`/`potencia_rapida`, `v[n]` antes de `n == 0`, uso acidental de laço); 2 implementações recursivas puras (1 em vetor `double`/int, 1 em string *in-place*).
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (22 min + 23 min) — Sessão 1 (Resolução: 14 min | Correção: 5 min | Recuperação: 3 min); Sessão 2 (Resolução: 14 min | Correção: 5 min | Recuperação: 4 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 teste de mesa de pilha, 2 funções recursivas completas sem laços), 100% de acerto antes do Estágio H.
- **Fontes:** `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 5 (17/11 e 23/11); `Aula_21`–`Aula_24`; `Lista11`–`Lista12` completas.

---

### Estágio H — Integração Geral e Projeto Modularizado: Processamento de Imagens PGM (`H01`–`H06`)

> **Nota sobre Natureza do Estágio H:** Todos os blocos deste estágio integram habilidades já dominadas nos Estágios A–G sobre a arquitetura do **Trabalho Prático (`Trabalho_Algoritmos.pdf`)**. Nenhum conceito novo da ementa é introduzido aqui; `H06` inclui desafios `[OPCIONAIS]` dentro da ementa que não bloqueiam o encerramento.

#### `H01` — Arquitetura em 5 Arquivos (`main.c`, `imagem.h/.c`, `funcoes.h/.c`) e Compilação Multi-Arquivo
- **Micro-habilidade foco:** *(Integração)* Estruturar o esqueleto modular de 5 arquivos (`main.c`, `imagem.h`, `imagem.c`, `funcoes.h`, `funcoes.c`) com guardas `#ifndef`, constantes `ALTURA`/`LARGURA` compartilhadas e compilação conjunta no GCC.
- **Pré-requisitos:** `F10`, `E08`.
- **Conteúdo novo:** Nenhum tópico novo de linguagem (aplica a topologia específica de 5 arquivos do projeto PGM).
- **Conteúdo revisado:** Guardas `#ifndef`/`#define`/`#endif`, inclusão `"imagem.h"` dentro de `"funcoes.h"`, separação protótipo/definição e `gcc main.c imagem.c funcoes.c -o processador` (`F08`), formato PGM P2 (`E07`).
- **Tipos de exercício:** Leitura de diagrama de dependências dos 5 arquivos; diagnóstico de inclusão dupla sem guardas ou omissão de `imagem.c` no comando `gcc`; completar `imagem.h` e `funcoes.h` sobre código inicial equivalente (construído no curso dado que o `main.c` original não está no acervo `[AUS/AMB]`); compilar e testar carregamento/gravação básica de uma matriz PGM sintética pequena.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (25 min) — Resolução: 15 min | Correção: 6 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 tarefas inéditas (1 rastreamento de `#include`s em 5 arquivos, 1 correção de erro de compilação/ligação em projeto de 5 arquivos, 1 compilação limpa `gcc -std=c99 -Wall -Wextra` de esqueleto modular de 5 arquivos), 100% de acerto.
- **Fontes:** `[DOC]` `Trabalho_Algoritmos.pdf` p. 1–2, 5; `Apresentacao_Trabalho_Algoritmos.pdf` p. 4–7, 14–15; `Aula_24_Algoritmos.pdf` p. 19; *(lacuna L3 registrada: `main.c` inicial do professor ausente na pasta)*.

#### `H02` — Filtros Ponto a Ponto Modularizados: Ajuste de Brilho e Limiarização com Saturação `[0, 255]`
- **Micro-habilidade foco:** *(Integração)* Implementar e declarar nos módulos `funcoes.h/.c` operações ponto a ponto *in-place* sobre a matriz de pixels (ajuste de brilho com `b` positivo/negativo e limiarização opcional), garantindo saturação `[0, 255]`.
- **Pré-requisitos:** `H01`.
- **Conteúdo novo:** Nenhum tópico novo de linguagem (aplica filtro ponto a ponto completo dentro da arquitetura `funcoes.h/.c`).
- **Conteúdo revisado:** Matrizes como parâmetro `int img[ALTURA][LARGURA]` (`F07`), saturação `[0, 255]` e limiarização (`E07`), condicionais `if/else if/else` (`B05`), modularização `.h`/`.c` (`H01`).
- **Tipos de exercício:** Teste de mesa com matriz `3 × 3` (pixels `200`, `240`, `10` com `b = +30` e `b = -30`); completar protótipo em `funcoes.h` e definição em `funcoes.c`; escrita independente de `ajustarBrilho` e `limiarizar` validadas sobre pequenas matrizes verificadas à mão.
- **Tempo estimado *(sujeito à calibração)*:** 1 sessão (22 min) — Resolução: 13 min | Correção: 5 min | Recuperação (se necessária): 4 min.
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 teste de mesa de brilho com saturação inferior/superior, 1 diagnóstico de divergência de assinatura `.h` vs `.c`, 1 compilação + execução com casos de borda `0` e `255`), 100% de acerto.
- **Fontes:** `[DOC]` `Trabalho_Algoritmos.pdf` p. 2, 4; `Apresentacao_Trabalho_Algoritmos.pdf` p. 7–8.

#### `H03` — Matriz Auxiliar, Preservação de Bordas e Filtro de Desfoque (*Blur*) $t \times t$
- **Micro-habilidade foco:** *(Integração)* Implementar filtro de vizinhança parametrizável (`t = 3, 5, 7`) utilizando matriz auxiliar (`static`), preservando bordas de raio $r = t / 2$ e calculando a média inteira da janela $t \times t$.
- **Pré-requisitos:** `H02`.
- **Conteúdo novo:** Nenhum tópico novo de linguagem (integra matriz auxiliar + raio dinâmico $r = t/2$ + 4 laços coordenados).
- **Conteúdo revisado:** Laços aninhados (`C09`, `E01`), cópia de matriz e alocação `static` (`E05`, `E07`), divisão inteira (`B01`), `funcoes.h/.c` (`H01`).
- **Tipos de exercício:** Teste de mesa manual em matriz `5 × 5` comparando o resultado errado (sem matriz auxiliar, reutilizando pixel já alterado) vs. o resultado correto (com matriz auxiliar `aux`); completar definição de limites `r <= i < ALTURA - r`; escrita independente de `aplicarBlur(int img[ALTURA][LARGURA], int t)` para `t ∈ {3, 5, 7}`. *(Nota: respeitar parâmetro `int t` conforme `Trabalho` p. 2, rejeitando erro de `Lista do Professor.pdf` p. 3.)*
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (22 min + 24 min) — Sessão 1 (Resolução: 13 min | Correção: 5 min | Recuperação: 4 min); Sessão 2 (Resolução: 14 min | Correção: 6 min | Recuperação: 4 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 teste de mesa provando diferença com vs. sem `aux` e bordas preservadas para `t = 5`, 1 detecção de bug de soma inteira ou borda violada, 1 implementação compilada validada em matriz pequena para `t = 3` e `t = 5`), 100% de acerto.
- **Fontes:** `[DOC]` `Trabalho_Algoritmos.pdf` p. 2, 4; `Apresentacao_Trabalho_Algoritmos.pdf` p. 9–10, 14.

#### `H04` — Filtro de Mediana $3 \times 3$ com Extração de Vizinhança e Função de Ordenação Fornecida
- **Micro-habilidade foco:** *(Integração)* Extrair a vizinhança $3 \times 3$ de cada pixel interno (preservando bordas via matriz auxiliar) para um vetor linear de 9 elementos, ordená-lo usando a função `ordenar` fornecida e atribuir o elemento de índice `4`.
- **Pré-requisitos:** `H03`.
- **Conteúdo novo:** Nenhum tópico novo de linguagem (a função `ordenar(int v[], int n)` é fornecida pronta conforme `Trabalho` p. 3, respeitando escopo negativo).
- **Conteúdo revisado:** Vetores 1D e passagem para função (`D01`, `F06`), matriz auxiliar e bordas (`H03`), indexação 2D→1D (`D09`, `E01`).
- **Tipos de exercício:** Teste de mesa com vizinhança contendo ruído sal (`255`) ou pimenta (`0`) verificando o vetor ordenado e índice `4`; completar extração `3 × 3` para vetor `v[9]` com contador `k = 0`; escrita independente de `aplicarMediana` integrada a `funcoes.h/.c` preservando bordas e usando `ordenar`.
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (20 min + 22 min) — Sessão 1 (Resolução: 12 min | Correção: 5 min | Recuperação: 3 min); Sessão 2 (Resolução: 13 min | Correção: 5 min | Recuperação: 4 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreamento manual de mediana `3 × 3` com ruído extremo `0`/`255`, 1 correção de erro de reutilização de `k` ou mutação sem matriz auxiliar, 1 implementação testada em matriz `5 × 5` conferida à mão), 100% de acerto.
- **Fontes:** `[DOC]` `Trabalho_Algoritmos.pdf` p. 2–4 (inclui código exato de `ordenar`, p. 3); `Apresentacao_Trabalho_Algoritmos.pdf` p. 11–12.

#### `H05` — Menu Interativo de Operações Sucessivas (`do-while` + `switch`) e Validação de Entradas
- **Micro-habilidade foco:** *(Integração)* Integrar em `main.c` a leitura única pré-menu (com tratamento de erro ao abrir arquivo), o laço repetitivo `do-while` + `switch` aplicando filtros encadeados sobre o estado atual da imagem e validação de `t` (`3, 5, 7`) e opções inválidas até gravar e sair (`0`).
- **Pré-requisitos:** `H04`, `C04`.
- **Conteúdo novo:** Nenhum tópico novo de linguagem (integração completa de `main.c` com os módulos).
- **Conteúdo revisado:** `do-while` + `switch` (`C04`, `B08`–`B09`), leitura única pré-laço vs. estado acumulado (`C03`), chamadas entre módulos (`H01`–`H04`).
- **Tipos de exercício:** Rastreamento de sequência de operações sucessivas (`brilho → blur → mediana → salvar`); caça ao bug (carregar imagem dentro do `do-while` apagando filtros anteriores, aceitar `t = 4` no blur, esquecer `break` no `switch`); escrita independente completa de `main.c` integrado aos módulos.
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (20 min + 22 min) — Sessão 1 (Resolução: 12 min | Correção: 5 min | Recuperação: 3 min); Sessão 2 (Resolução: 13 min | Correção: 5 min | Recuperação: 4 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente com 3 questões inéditas (1 rastreamento de estado cumulativo em menu, 1 diagnóstico de bug de releitura/validação de `t`, 1 compilação e execução encadeada de ≥ 2 operações gravando saída PGM válida), 100% de acerto.
- **Fontes:** `[DOC]` `Trabalho_Algoritmos.pdf` p. 3–4 (Seções 5 e 6); `Apresentacao_Trabalho_Algoritmos.pdf` p. 13–14.

#### `H06` — Verificação Sistemática, Teste de Mesa Integrado e Preparação para Arguição/Reavaliação *(Inclui Desafios Opcionais)*
- **Micro-habilidade foco:** *(Integração e Síntese Final)* Validar o sistema de 5 arquivos contra casos de borda calculados à mão, executar pequenas modificações sob restrições (simulando arguição oral ao vivo) e revisar integralmente os 8 estágios para avaliação global.
- **Pré-requisitos:** `H05`, `G09`.
- **Conteúdo novo:** Nenhum.
- **Conteúdo revisado:** Todos os estágios (`A`–`H`) integrados: rastreamento de laços/ponteiros/recursão, matrizes e modularização de 5 arquivos.
- **Tipos de exercício:** Checklist de testes em matrizes pequenas conferidas à mão; exercícios de **"modificação ao vivo"** (ex.: adicionar filtro de limiarização como opção `4` no menu, inverter cálculo de brilho ou alterar regra de borda); simulado misto integrado (rastreamento + código multi-arquivo + recursão pura); **Desafios `[OPCIONAIS]` dentro da ementa** (ex.: aplicar um filtro simples de forma recursiva por linhas ou calcular estatísticas da imagem — mínimo, máximo e média — em novo módulo `estatisticas.h/.c`), marcados como não bloqueantes.
- **Tempo estimado *(sujeito à calibração)*:** 2 sessões (24 min + 24 min) — Sessão 1 (Resolução: 15 min | Correção: 5 min | Recuperação: 4 min); Sessão 2 (Resolução: 15 min | Correção: 5 min | Recuperação: 4 min).
- **Critério de domínio:** Registro separado de 1ª tentativa/autocorreção; checagem independente obrigatória com 3 questões inéditas cobrindo o núcleo obrigatório (1 explicação estrutural de ponteiros/matrizes/bordas e modificação pontual no projeto 5-arquivos, 1 rastreamento combinado sem computador, 1 problema completo verificado via GCC), 100% de acerto. *(Desafios `[OPCIONAIS]` não contam como critério de bloqueio.)*
- **Fontes:** `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 5–6 (23/11, 24/11, 08/12, 11/12); `Trabalho_Algoritmos.pdf` p. 4–5 (Seções 6 e 7); `Apresentacao_Trabalho_Algoritmos.pdf` p. 14, 16–17.

---

## 4. Matriz de Cobertura: Ementa Oficial (`ementa_algoritmos.pdf`) × Blocos Previstos

A tabela a seguir relaciona **todos os 11 itens numerados do Conteúdo Programático** de `ementa_algoritmos.pdf` (p. 2) aos blocos do curso e às respectivas fontes documentais:

| # Ementa (`[DOC]`) | Tópico Oficial e Subconteúdo da Ementa (`ementa_algoritmos.pdf`, p. 2) | Bloco(s) Introdutório(s) | Bloco(s) de Prática e Aprofundamento | Revisão / Integração | Fontes Diretas (`[DOC]`) |
|---:|---|---|---|---|---|
| **1** | **Introdução a algoritmos e resolução de problemas:** problema, abstração, algoritmo, linguagem de programação, programa; exemplos de algoritmos. | `A01`, `A02` | `A01`, `A02`, `A07`, `C03` | `A10` | `ementa` p. 1–2; `Aula_01` p. 2–32; `Aula_02` p. 2; `Lista8` Q1 |
| **2** | **Variáveis e constantes. Tipos primitivos e compostos (`inteiro`, `real`, `booleano`, `caractere`, `cadeia de caracteres`):** definição, identificador (regras e palavras reservadas), tipo, conteúdo e sintaxe. | `A04`, `A05`, `B03`, `D06` | `A04`, `A05`, `A09`, `B03`, `D06`–`D08` | `A10`, `B10`, `D10` | `ementa` p. 2; `Aula_02` p. 8–9, 16–24; `Aula_06` p. 12 (`<stdbool.h>`); `Aula_13`; `Lista7` |
| **3** | **Precisão numérica:** bits e bytes; representação binária (capacidade $2^n$ e quantificação de bits $\lceil \log_2 T \rceil$ para representar dados). | `A08`, `A09` | `A08`, `A09` | `A10`, `B02` | `ementa` p. 2; `Planejamento` p. 1 (31/08); `Aula_04` p. 4–20 |
| **4** | **Instruções de entrada, saída e atribuição:** definições, sintaxe e exemplos. | `A03`, `A05`, `A06`, `A07` | `A03`, `A05`–`A07`, `D06` | `A10`, `D10` | `ementa` p. 2; `Aula_02` p. 12–15, 20–22; `Aula_03` p. 3–23; `Aula_13` p. 11–15 |
| **5** | **Expressões aritméticas, relacionais e booleanas:** precedência de operadores lógicos e aritméticos; lógica booleana, valores/operadores lógicos, tabela-verdade. | `B01`, `B02`, `B03`, `B06` | `B01`–`B03`, `B06` | `B10` | `ementa` p. 2 (cobre lacuna L1 em `B06`); `Aula_05` p. 4–24; `Aula_06` p. 7–12; `Lista1`; `Lista2` Q6–Q8 |
| **6** | **Estruturas condicionais (simples e múltipla):** decisão simples, composta e múltipla escolha. | `B03`, `B04`, `B05`, `B08` | `B04`, `B05`, `B07`, `B08`, `B09` | `B10`, `H02`, `H05` | `ementa` p. 2; `Aula_06` p. 13–28; `Aula_07`; `Aula_08_v2`; `Lista1`–`Lista3`; `Lista8` Q2 |
| **7** | **Estruturas de repetição (pré-condição, pós-condição e laços contados):** teste no início, teste no final e variável de controle; sintaxe em C. | `C01`, `C04`, `C05` | `C02`, `C03`, `C04`, `C06`–`C09` | `C10`, `H05` | `ementa` p. 2 (cobre lacuna L2 em `C04`); `Aula_09`; `Aula_10`; `Aula_11` p. 4–9; `Lista4`–`Lista5`; `Trabalho` p. 3–4 |
| **8** | **Matrizes n-dimensionais:** vetores e matrizes — definição, declaração e exemplos de procedimentos. | `D01`, `D09`, `E01`, `E07` | `D02`–`D05`, `D06`–`D09`, `E02`–`E07` | `D10`, `E08`, `H02`–`H04` | `ementa` p. 2; `Aula_11`–`Aula_15`; `Lista6`–`Lista9`; `Trabalho` p. 1–3 |
| **9** | **Modularização:** procedimentos, funções, escopo, parâmetros/argumentos; desvio de chamada e pilha de execução; cabeçalhos e bibliotecas em C. | `F01`, `F02`, `F08`, `G01` | `F03`–`F08`, `G02` | `F10`, `G09`, `H01`–`H06` | `ementa` p. 2; `Aula_16`–`Aula_19`; `Aula_21` p. 18 (pilha); `Lista10`; `Trabalho` p. 1–2 |
| **10** | **Recursão:** definições e exemplos. | `G01`, `G02` | `G03`–`G08` | `G09` | `ementa` p. 2; `Aula_21`–`Aula_24`; `Lista11`–`Lista12` |
| **11** | **Implementação de problemas em uma linguagem de programação:** conceitos/características das linguagens, compilação e interpretação, implementação de programas, procedimentos, funções e bibliotecas. | `A02`, `F08`, `F09` | `A03`–`G08` (prática contínua em C), `F08`, `F09` | `F10`, `H01`–`H06` | `ementa` p. 2; `Aula_00` p. 3; `Aula_02` p. 2–5; `Aula_19`–`Aula_20`; `Trabalho` p. 1–5 |

**Resultado da Cobertura:** **11/11 (100%)** dos tópicos e subtópicos da ementa oficial vigente de `CC61A` estão integralmente cobertos pelos **73 blocos**.

---

## 5. Verificação de Coerência da Arquitetura Curricular (Fase 1)

1. **Integridade do Grafo de Pré-Requisitos (DAG):** Todas as arestas apontam estritamente de blocos anteriores para posteriores (ex.: `A01 → ... → A10 → B01 → ... → B10 → C01 → ... → C10 → D01 → ... → D10 → E01 → ... → E08 → F01 → ... → F10 → G01 → ... → G09 → H06`, com `H01` unindo `F10` e `E08`, e `H05` unindo `H04` e `C04`). **Zero dependências circulares.**
2. **Prevenção de Introduções Prematuras:**
   - A falha cronológica detectada na `Aula_03` p. 24 (pedir quociente inteiro e resto `%` antes de ensinar divisão inteira e `%`) foi corrigida movendo esse tópico para `B01`.
   - Operadores lógicos e tabela-verdade (`B06`) precedem decisões hierárquicas compostas (`B07`, ex.: parque e validação de data) e seleção composta (`B09`).
   - `do-while` (`C04`) precede o menu do projeto final (`H05`).
   - Strings e linearização 1D (`D06`–`D09`) consolidam o domínio 1D antes da introdução das matrizes 2D (`E01`).
   - Matrizes 2D (`Estágio E`) e Funções/Ponteiros (`Estágio F`) são completamente dominados antes da arquitetura multi-arquivo de processamento de imagens (`Estágio H`).
   - Rastreamento de pilha e ordem pré/pós-chamada (`G01`–`G02`) antecedem qualquer escrita independente de função recursiva (`G03`–`G08`).
3. **Respeito ao Escopo Negativo:** Nenhum bloco introduz `struct`, alocação dinâmica (`malloc`/`free`), VLAs, aritmética de ponteiros, implementação própria de algoritmos de ordenação ou criação de parser `FILE*` do zero — mantendo fidelidade estrita ao comprovado nas fontes da UTFPR-PG.
