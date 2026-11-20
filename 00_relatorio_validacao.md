# Relatório de Validação Técnica e Pedagógica — Fase 2 (Diagnóstico, Orientação e Pilotos)

> **Data:** `2026-11-19`  
> **Escopo avaliado:** Instrumentos diagnósticos, manual do orientador, ficha de acompanhamento CSV e três blocos-piloto representativos (`B05`, `D02` e `F05`) do programa de Preparação Intensiva em Algoritmos para `CC61A - Algoritmos` (UTFPR – Campus Ponta Grossa).  
> **Declaração de Validação Empírica:** **Nenhuma validação empírica com estudantes reais foi realizada até este momento.** Todas as durações estimadas e pontos de corte são estimativas iniciais de projeto sujeitas à calibração prática.

---

## 1. Escopo dos Artefatos Produzidos na Fase 2

| Artefato | Descrição | Caminho |
|---|---|---|
| Teste Diagnóstico | 8 itens de Triagem (`T1`–`T8`), 21 itens de Sondagem (`SA-01`–`SG-03`, total 29 IDs), 5 regras de interrupção (`I1`–`I5`) e 4 critérios de posicionamento provisório | [00_teste_diagnostico.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/00_teste_diagnostico.md) |
| Gabarito Diagnóstico | Respostas comentadas, mapeamento erro → pré-requisito em falta e matriz de posicionamento por pré-requisitos demonstrados | [00_gabarito_diagnostico.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/00_gabarito_diagnostico.md) |
| Guia do Orientador | Condução de sessões (15–25 min), critério de 100% na checagem independente, regra das 2 tentativas, dicionário CSV e padrões GCC C99 | [00_guia_orientador.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/00_guia_orientador.md) |
| Ficha de Acompanhamento | Planilha CSV em branco (somente cabeçalho com as 12 colunas especificadas) | [00_acompanhamento.csv](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/00_acompanhamento.csv) |
| Piloto 1 (`B05`) | Bloco de `else if` e ordem das condições (`B05-E01`–`E06`, `B05-C01`–`C03`), gabarito, especificação de testes, 34 casos JSON e 6 soluções `.c` | [B05_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/blocos/B05_bloco.md) \| [B05_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/gabaritos/B05_gabarito.md) \| [B05_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/B05_testes.md) |
| Piloto 2 (`D02`) | Bloco de acumulação/extremos 1D em único percurso (`D02-E01`–`E06`, `D02-C01`–`C03`), gabarito, especificação de testes, 30 casos JSON e 6 soluções `.c` | [D02_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/blocos/D02_bloco.md) \| [D02_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/gabaritos/D02_gabarito.md) \| [D02_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/D02_testes.md) |
| Piloto 3 (`F05`) | Bloco de ponteiros como parâmetros e múltiplos resultados (`F05-E01`–`E06`, `F05-C01`–`C03`), gabarito, especificação de testes, 30 casos JSON e 6 soluções `.c` | [F05_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/blocos/F05_bloco.md) \| [F05_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/gabaritos/F05_gabarito.md) \| [F05_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/F05_testes.md) |

---

## 2. Revisão Crítica nos 4 Eixos e Problemas Corrigidos

### 2.1 Clareza
- **Achado na revisão:** O piloto `F05_bloco.md` dividia as seções de exercícios em `## 3` (Sessão 1) e `## 4` (Sessão 2), empurrando Checagem, Orientação e Referências para `## 5`–`## 7`, enquanto `B05_bloco.md` e `D02_bloco.md` usavam `## 1`–`## 6`. Além disso, `B05-E03` e `D02-E03` não explicavam com clareza onde registrar os bugs identificados (papel ou comentários `//`), e a Instrução 3 de `D02_bloco.md` explicava de forma imprecisa a regra `i = 0` vs `i = 1` ao combinar soma e extremos.
- **Correções aplicadas:**
  - Padronizados todos os três blocos-piloto com a mesma estrutura fixa de 6 seções (`## 1. Instruções Curtas`, `## 2. Exemplos Guiados`, `## 3. Exercícios`, `## 4. Checagem Independente de Domínio`, `## 5. Orientação de Avanço ou Recuperação`, `## 6. Referências do Orientador`), usando subseções `### Sessão 1` e `### Sessão 2` dentro de `## 3`.
  - Mantida distinção explícita entre `Trecho ilustrativo` e `Programa completo` em todos os exemplos e exercícios.
  - Marcados claramente nos gabaritos os erros intencionais das atividades de Caça ao Bug (`B05-E03`, `B05-C02`, `D02-E03`, `D02-C02`, `F05-E03`, `F05-C02`) e padronizada a instrução de resposta em `B05-E03` e `D02-E03`.
  - Refinada a Instrução 3 de `D02_bloco.md` para explicitar quando o laço inicia em `i = 1` (apenas extremos) vs. obrigatoriamente em `i = 0` (quando também acumula `soma` ou faz contagem no mesmo percurso) e por que `else if` quebra acoplamentos e empates iniciais.

### 2.2 Progressão e Não-Antecipação
- **Verificação:** Os 3 pilotos preservam integralmente a curva `Exemplo guiado → Teste de mesa (E01) → Completar lacunas (E02) → Caça ao bug (E03) → Variações com pistas (E04, E05) → Resolução independente (E06) → Checagem inédita com 100% sem gabarito (C01–C03)`.
- **Fronteiras de escopo respeitadas (0 introduções prematuras):**
  - `B05`: sem `&&`, `||`, `!`, `switch`, laços ou vetores.
  - `D02`: sem funções próprias além de `main`, sem strings (`char`/`<string.h>`), matrizes 2D ou VLAs (usa `#define MAX 100`).
  - `F05`: protótipos antes de `main`, apenas escalares e ponteiros para escalares (`int *`, `double *`), sem vetores/matrizes/strings em parâmetros e sem recursividade.
  - Escopo negativo da disciplina (`struct`, `malloc`/`free`, VLAs, aritmética de ponteiros, ordenação própria) rigorosamente respeitado.
- **Diagnóstico:** Regras de interrupção (`I1`–`I5`) e matriz de posicionamento evitam expor iniciantes a conteúdos distantes e posicionam sempre pelo menor pré-requisito não demonstrado (sinalizando `PROVISÓRIO` em 4 condições).

### 2.3 Carga de Trabalho (Sessões de 15 a 25 Minutos)
- **Problema crítico detectado na revisão dos pilotos:**
  - `B05_bloco.md` e `D02_bloco.md` previam originalmente **1 sessão (22 min)** com `13 min` de resolução para 6 exercícios (incluindo 4 programas completos em C) mais 3 itens de Checagem Independente — carga incompatível com 13 minutos para estudantes iniciantes.
  - `F05_bloco.md` previa originalmente `E04`–`E06` **e** toda a Checagem Independente (`C01`–`C03`) juntos nos `12 min` de resolução da Sessão 2.
- **Correções aplicadas antes de expandir a Fase 3:**
  - Recalibrados `B05`, `D02` e `F05` para **2 sessões de prática dentro da janela de 15–25 min** + **Checagem Independente dedicada (`18 min`: `13 min` resol. + `5 min` conf.)**:
    - `B05`: Sessão 1 (`E01`–`E03`: `20 min` = `12 + 5 + 3`) e Sessão 2 (`E04`–`E06`: `22 min` = `14 + 5 + 3`).
    - `D02`: Sessão 1 (`E01`–`E03`: `22 min` = `13 + 5 + 4`) e Sessão 2 (`E04`–`E06`: `24 min` = `15 + 5 + 4`).
    - `F05`: Sessão 1 (`E01`–`E03`: `22 min` = `13 + 5 + 4`) e Sessão 2 (`E04`–`E06`: `24 min` = `15 + 5 + 4`).
  - Atualizados em sincronia os respectivos blocos em [00_mapa_curricular.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/00_mapa_curricular.md) (linhas 217, 395 e 613), a condução de blocos densos e exemplos fictícios de CSV em [00_guia_orientador.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/00_guia_orientador.md) (mantendo [00_acompanhamento.csv](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/00_acompanhamento.csv) estritamente vazio apenas com o cabeçalho).

### 2.4 Correção Técnica
Problemas técnicos identificados e corrigidos durante a construção e revisão da Fase 2:
1. **Item diagnóstico `T3(a)` ([00_teste_diagnostico.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/00_teste_diagnostico.md) e [00_gabarito_diagnostico.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/00_gabarito_diagnostico.md)):** Na versão inicial (`x = 12, y = 4`), `x > 15` era falso, fazendo com que tanto a precedência correta (`0 || (1 && 0) = 0`) quanto a precedência errada da esquerda para a direita (`(0 || 1) && 0 = 0`) desviassem para `Q`. Corrigido para `int x = 16, y = 4;`, no qual a precedência correta resulta em `P` (`1 || 0 = 1`) e o erro `||` antes de `&&` resulta em `Q` (`1 && 0 = 0`).
2. **Item diagnóstico `SC-01`:** O sentinela original (`0`) não alterava visivelmente o valor da soma mesmo com o bug `soma += x;` antes do reteste. Alterado para sentinela `-1` (`while (x != -1)`), expondo ambos os defeitos (variável `x` não inicializada e inclusão do sentinela `-1` na soma).
3. **Especificação `B05_testes.md`:** Corrigida a contagem citada de casos (`31` → `34` casos em `casos_B05.json`) e corrigido o caso de borda `compra = 199.995` (`5%` de desconto: `199.995 * 0.05 = 9.99975 → R$ 10.00` e `total = 189.99525 → R$ 190.00` no lugar de `R$ 189.99`).
4. **Especificação `D02_testes.md`:** Removida anotação residual de rascunho no caso `D02_C02-T2` mantendo a saída exata verificada (`Menor: -3 (indice 1)`).
5. **Detector de recursão no verificador:** Corrigido falso positivo no script `verify_phase2.py`, que anteriormente fatiava a partir do protótipo antes de `main` e acusava a chamada em `main` como recursão; passou a isolar exatamente o corpo delimitado por chaves da definição auxiliar.
6. **Rigor terminológico em C:** Todos os materiais descrevem a passagem de ponteiros exclusivamente como **passagem por valor** / **passagem de endereços por valor** (nunca como "passagem por referência").

---

## 3. Verificações Executadas vs. Pendência Ambiental (GCC)

### 3.1 O que foi realmente executado (Verificação Automatizada em Python)
Executado por meio do script `verify_phase2.py` após a última edição dos arquivos:
- **Integridade de fontes e saída:** confirmados `45` arquivos originais intactos em `C:\Users\d7opa\Documents\Algoritmos\`, presença exclusiva dos diretórios `estagio_B`, `estagio_D` e `estagio_F`, e `73` blocos únicos em `00_mapa_curricular.md`.
- **Planilha CSV:** validado `00_acompanhamento.csv` com exatamente 1 linha (cabeçalho das 12 colunas obrigatórias).
- **Consistência de IDs e gabaritos:** conferidos todos os `29` IDs diagnósticos (`T1`–`T8`, `SA-01`–`SG-03`), os `27` IDs dos pilotos (`E01`–`E06` e `C01`–`C03` em `B05`, `D02`, `F05`), e correspondência literal de código entre os `18` arquivos `.c` em `solucoes/` e os blocos de código dos respectivos `*_gabarito.md`.
- **Análise estática C99 e não-antecipação:** confirmados `#include <stdio.h>`, `int main(void)`, `return 0;`, ausência de `gets(`, balanceamento de `{}` e `()`, literais `printf` estritamente ASCII (sem acentos), ausência de antecipações proibidas por estágio e ausência de recursão em `F05`.
- **Oráculo matemático e arredondamento:** executada simulação em Python sobre **todos os 94 casos de teste** dos JSONs (`34` em `casos_B05.json`, `30` em `casos_D02.json` e `30` em `casos_F05.json`), validando 100% de correspondência exata com `stdout` esperado e conferindo consistência entre arredondamento IEEE-754 e decimal *half-up* nas saídas `%.2f`.

### 3.2 Pendência Ambiental Crítica — Ausência de Compilador C
- **Diagnóstico de ambiente:** Verificado anteriormente tanto no Windows quanto no WSL2 Ubuntu (`which gcc clang tcc cc python3`): **não há nenhum compilador C (`gcc`, `clang`, `cc` ou `cl`) instalado nesta máquina**.
- **Declaração explícita:** **Nenhum dos 18 arquivos `.c` foi compilado nem executado como binário nativo até o momento.** A verificação realizada até aqui é estática + simulação por oráculo matemático em Python, não substituindo a compilação e execução em GCC exigidas na Fase 4.
- **Para habilitar a compilação real no WSL2 Ubuntu:**
  ```bash
  sudo apt update && sudo apt install -y build-essential
  ```
- **Comando padrão de verificação quando o GCC estiver disponível:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa && ./programa < entrada.txt
  ```

---

## 4. Diretrizes Consolidadas Antes da Produção da Fase 3

1. **Template único de 6 seções:** Todo bloco da Fase 3 seguirá rigorosamente a estrutura `## 1` a `## 6` validada nos pilotos, utilizando subseções `### Sessão 1` / `### Sessão 2` em `## 3` sempre que o bloco exigir 2 sessões de prática.
2. **Calibração realista de carga (15–25 min por sessão):** Blocos densos em escrita de código completo serão planejados com 5–6 exercícios divididos em 2 sessões de prática (20–24 min) mais checagem independente (15–18 min), evitando comprimir 4 ou mais programas completos em 13 minutos.
3. **Execução real em GCC antes da consolidação final:** Manter o ambiente alvo Linux C99 (`-std=c99 -Wall -Wextra`, adicionando `-lm` quando `<math.h>` estiver no escopo) e registrar explicitamente no relatório de cada estágio caso o compilador ainda não esteja instalado.

---

## 5. Validação da Fase 3 — Estágio A (`A01`–`A10`)

### 5.1 Entregáveis Produzidos em [estagio_A](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A)
- **Blocos (`10`):** `A01_bloco.md` a `A10_bloco.md` ([blocos](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/blocos)), todos seguindo o template de 6 seções (`## 1` a `## 6`), com `A10` dividido em `Sessão 1` e `Sessão 2`.
- **Gabaritos (`10`):** `A01_gabarito.md` a `A10_gabarito.md` ([gabaritos](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/gabaritos)), com erros intencionais de Caça ao Bug explicitamente identificados.
- **Especificações de teste (`10`), JSONs (`7`) e Soluções C99 (`32` `.c`):**
  - Blocos conceituais/papel sem código executável em `.c`: `A01` (algoritmos e abstração), `A04` (identificadores e declarações sem variáveis não utilizadas) e `A08` (bits, bytes, binário, $2^n$ e $\lceil \log_2 T \rceil$).
  - Arquivos `.c` verificáveis (`32` no total em [solucoes](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes)) e `7` suítes JSON (`78` casos totais): `A02` (`5` `.c`, `5` casos), `A03` (`5` `.c`, `5` casos), `A05` (`5` `.c`, `5` casos), `A06` (`5` `.c`, `20` casos), `A07` (`4` `.c`, `18` casos), `A09` (`3` `.c`, `3` casos determinísticos IEEE-754 / Linux LP64) e `A10` (`5` `.c`, `22` casos integrando `A01`–`A09` sem `/` nem `%`).

### 5.2 Verificações Automatizadas Executadas (`verify_estagio_A.py`)
- **Integridade do ambiente e estrutura:** `45` arquivos originais intactos; diretórios de saída exatos (`estagio_A`, `estagio_B`, `estagio_D`, `estagio_F`); `100%` dos links `file:///` resolvidos para arquivos existentes. *(Durante a revisão do coordenador, foi removida uma pasta `.jev/` residual de `324 bytes` criada dentro de `Curso_Preparacao_Intensiva_Algoritmos\` durante a invocação paralela, mantendo apenas `.jev\` na raiz `C:\Users\d7opa\Documents\Algoritmos\`.)*
- **Consistência bloco ↔ gabarito ↔ `.c`:** conferidos todos os IDs `E01..E0N` e `C01..C0M` (`C01..C04` em `A04` e `A08`; `C01..C03` nos demais) e correspondência literal caractere a caractere entre todos os `32` `.c` e os respectivos gabaritos.
- **Análise estática C99 e não-antecipação:** confirmados `#include <stdio.h>`, `int main(void)`, `return 0;`, `#define` sem `;`, saídas `printf` estritamente ASCII, `" %c"` / espaço em `scanf` antes de `%c` em `A06`, uso obrigatório de `%zu` com `sizeof` em `A09`, e ausência estrita de antecipações proibidas (`A02`/`A03` sem variáveis, `A05` sem `scanf` nem aritmética, `A06` sem aritmética/troca, `A09`/`A10` sem `/` nem `%`, e zero `if`/`switch`/laços/vetores em todo o Estágio A).
- **Oráculo matemático em Python (`78/78` casos):** simulação direta de `printf` e constantes/escapes sobre `A02`, `A03` e `A05`; simulação de entradas/saídas e rotação de variáveis em `A06` e `A07`; conferência IEEE-754 (`ctypes.c_float` e `double` 64 bits + LP64) em `A09`; verificação aritmética com checagem de arredondamento `%.2f` sem empates `.xx5` em `A10`; e conferência numérica das conversões binárias e potências de 2 de `A08`.

### 5.3 Pendências Mantidas
- **Compilação binária em GCC:** Conforme checado no início do Estágio A (`NO_WSL_COMPILER`), `gcc`/`clang` segue ausente no Windows e no WSL2 Ubuntu. **Nenhum dos `32` arquivos `.c` do Estágio A (nem os `18` dos pilotos) foi compilado ou executado como binário nativo.**
- **Validação com alunos:** Nenhuma aplicação empírica com estudantes foi realizada.

---

## 6. Validação da Fase 3 — Estágio B (`B01`–`B10`)

### 6.1 Entregáveis Produzidos em [estagio_B](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B)
- **Blocos (`10`):** `B01_bloco.md` a `B10_bloco.md` ([blocos](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/blocos)), todos rigorosamente estruturados no template uniforme de 6 seções (`## 1` a `## 6`), com cabeçalho de Preparação Intensiva, registro de sessões, critério de domínio de 100% na checagem e regra de investigação de pré-requisitos após 2 insucessos. Blocos densos (`B05`, `B06`, `B07`, `B09`, `B10`) organizados em 2 sessões de prática (20–22 min) mais checagem independente (18 min).
- **Gabaritos (`10`):** `B01_gabarito.md` a `B10_gabarito.md` ([gabaritos](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/gabaritos)), detalhando passo a passo testes de mesa, raciocínio lógico e versões corrigidas de Caça ao Bug.
- **Especificações de teste (`10`), Suítes JSON (`10`) e Soluções C99 (`59` `.c`):**
  - **Suítes de teste JSON (`345` casos no total):** `casos_B01.json` (`34` casos), `casos_B02.json` (`27` casos), `casos_B03.json` (`24` casos), `casos_B04.json` (`32` casos), `casos_B05.json` (`34` casos), `casos_B06.json` (`41` casos), `casos_B07.json` (`32` casos), `casos_B08.json` (`33` casos), `casos_B09.json` (`51` casos) e `casos_B10.json` (`37` casos).
  - **Arquivos `.c` verificáveis (`59` no total em [solucoes](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes)):**
    - `B01` (`6` `.c`): decomposição inteira de notas de dinheiro, conversão de segundos em h/m/s e cédulas bancárias.
    - `B02` (`6` `.c`): Bhaskara simples, precedência, `(double)` cast, operadores compostos e distância euclidiana com `<math.h>` (`-lm`).
    - `B03` (`5` `.c`): `if` simples sem `else`, paridade (`n % 2 == 0`), velocidade/multa e descontos em limiares `>`.
    - `B04` (`6` `.c`): `if / else` binário (par/ímpar, crédito especial) e múltiplos `if`s independentes não-excludentes com flag de controle.
    - `B05` (`6` `.c`): faixas contínuas crescentes em `else if`, planos de internet, estacionamento com excedente (piloto preservado intacto).
    - `B06` (`7` `.c`): operadores lógicos `&&`, `||`, `!`, curto-circuito, validação de intervalos, empréstimos, datas e bolsas de pesquisa.
    - `B07` (`6` `.c`): `if` aninhado, prevenção de *dangling else*, existência geométrica prévia de triângulos e triagem com barreiras hierárquicas.
    - `B08` (`5` `.c`): seleção múltipla com `switch / case`, `break`, `default`, agrupamento intencional (*fall-through*) e menus inteiros/`char`.
    - `B09` (`6` `.c`): `switch` aninhado, `if` interno de validação (caixa eletrônico) e colapso de intervalos via divisão inteira (`nota / 10`, `idade / 10`).
    - `B10` (`6` `.c`): revisão integradora do Estágio B sem conteúdo novo (Bhaskara completa com $\Delta$, ano bissexto, faturas residenciais/comerciais/industriais com `switch`, triângulos com Heron e folha de pagamento com faixas de INSS e IRRF).

### 6.2 Verificações Automatizadas Executadas (`verify_estagio_B.py`)
- **Preservação de recursos anteriores:** O bloco piloto `B05` e seus `6` programas `.c` associados foram mantidos estritamente intactos, sem nenhuma alteração indesejada.
- **Auditoria de não-antecipação (Escopo Negativo):** Confirmada ausência absoluta de:
  - Laços de repetição (`while`, `for`, `do-while`) em todo o Estágio B (**0 ocorrências**).
  - Vetores ou strings indexadas (`char[]`, `int[]`) (**0 ocorrências**).
  - Funções de usuário além de `int main(void)` (**0 ocorrências**).
  - Operadores lógicos (`&&`, `||`, `!`) em `B01`–`B05` (**0 ocorrências** antes de `B06`).
  - Estrutura `switch` em `B01`–`B07` (**0 ocorrências** antes de `B08`).
- **Conformidade de compilação C99:** Todos os `59` arquivos `.c` possuem `int main(void)` e `return 0;`, incluem cabeçalhos obrigatórios (`<stdio.h>`, `<math.h>` com flag `-lm` quando pertinente) e utilizam strings de `printf` estritamente em **ASCII puro** (sem caracteres acentuados ou especiais).
- **Oráculo de Testes Automatizados em Python:** Todos os **`345` casos de teste** foram executados contra os oráculos lógicos e matemáticos em Python, obtendo **`345/345` sucessos (100% de exatidão)** em casos normais, extremos e valores de fronteira.

### 6.3 Pendências Mantidas
- **Compilação binária em GCC:** Continua ausente compilador C no ambiente host Windows/WSL. Nenhum dos `59` arquivos `.c` do Estágio B foi compilado ou executado como binário nativo.
- **Validação com alunos:** Nenhuma aplicação empírica com estudantes foi realizada.

---

## 7. Validação da Fase 3 — Estágio C (`C01`–`C10`)

### 7.1 Entregáveis Produzidos em [estagio_C](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C)
- **Blocos (`10`):** `C01_bloco.md` a `C10_bloco.md` ([blocos](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/blocos)), todos aderentes ao template uniforme de 6 seções (`## 1` a `## 6`), com registro de sessões, critério de domínio de 100% e regra de investigação de pré-requisitos após 2 tentativas malsucedidas. Blocos densos (`C03`, `C08`, `C09`, `C10`) estruturados em 2 sessões de prática mais checagem independente.
- **Gabaritos (`10`):** `C01_gabarito.md` a `C10_gabarito.md` ([gabaritos](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/gabaritos)), com testes de mesa passo a passo e versões corrigidas de Caça ao Bug.
- **Especificações de teste (`10`), Suítes JSON (`10`) e Soluções C99 (`59` `.c`):**
  - **Suítes de teste JSON (`271` casos no total):** `casos_C01.json` (`21`), `casos_C02.json` (`30`), `casos_C03.json` (`31`), `casos_C04.json` (`24`), `casos_C05.json` (`31`), `casos_C06.json` (`18`), `casos_C07.json` (`25`), `casos_C08.json` (`32`), `casos_C09.json` (`29`) e `casos_C10.json` (`30`).
  - **Arquivos `.c` verificáveis (`59` no total em [solucoes](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes)):** cobrindo `while` pré-condição (`C01`–`C03`), contadores/acumuladores e resto sem `%` (`C02`), sentinela por *priming read* e MDC de Euclides (`C03`), `do-while` e menus (`C04`), `for` C99 e padrões de contagem (`C05`), rastreamento de efeitos colaterais e comando nulo `;` (`C06`), `break`/`continue` e primalidade (`C07`), séries numéricas incrementais e tolerância $\varepsilon$ (`C08`), laços aninhados e formatação tabular (`C09`), além da revisão integradora (`C10`).

### 7.2 Verificações Automatizadas Executadas (`verify_estagio_C.py`)
- **Auditoria de não-antecipação (Escopo Negativo):** Confirmada ausência absoluta de:
  - Vetores ou strings indexadas (`char[]`, `int[]`) em todo o Estágio C (**0 ocorrências**).
  - Funções de usuário além de `int main(void)` (**0 ocorrências**).
  - Laços `do-while` e `for` antes de `C04` e `C05`, respectivamente (**0 ocorrências** em `C01`–`C03`).
- **Conformidade C99 e Terminal:** Todos os `59` arquivos `.c` possuem `int main(void)` e `return 0;`, e utilizam strings de `printf` estritamente em **ASCII puro**.
- **Oráculo de Testes:** Todos os **`271` casos de teste** catalogados nas 10 suítes JSON foram validados sem divergências.

### 7.3 Pendências Mantidas
- **Compilação binária em GCC:** Continua ausente compilador C no ambiente host Windows/WSL. Nenhum dos `59` arquivos `.c` do Estágio C foi compilado ou executado como binário nativo.
- **Validação com alunos:** Nenhuma aplicação empírica com estudantes foi realizada.

---

## 8. Validação da Fase 3 — Estágio D (`D01`–`D10`)

### 8.1 Entregáveis Produzidos em [estagio_D](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D)
- **Blocos (`10`):** `D01_bloco.md` a `D10_bloco.md` ([blocos](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/blocos)), aderentes ao template uniforme de 6 seções (`## 1` a `## 6`), com registro de sessões, critério de domínio de 100% e regra de investigação de pré-requisitos após 2 tentativas malsucedidas. O bloco piloto **`D02`** foi mantido estritamente intacto.
- **Gabaritos (`10`):** `D01_gabarito.md` a `D10_gabarito.md` ([gabaritos](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/gabaritos)), com testes de mesa detalhados e versões corrigidas de Caça ao Bug.
- **Especificações de teste (`10`), Suítes JSON (`10`) e Soluções C99 (`56` `.c`):**
  - **Suítes de teste JSON (`280` casos no total):** `casos_D01.json` (`25`), `casos_D02.json` (`30`), `casos_D03.json` (`30`), `casos_D04.json` (`25`), `casos_D05.json` (`30`), `casos_D06.json` (`25`), `casos_D07.json` (`30`), `casos_D08.json` (`25`), `casos_D09.json` (`25`) e `casos_D10.json` (`35`).
  - **Arquivos `.c` verificáveis (`56` no total em [solucoes](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes)):** cobrindo declaração e limites base 0 (`D01`), acumulação e busca de extremos (`D02` — piloto preservado), busca linear/inversão *in-place*/particionamento (`D03`), histogramas e deduplicação (`D04`), casamento de padrão com sobreposição e convolução discreta 1D (`D05`), strings com `\0` e E/S segura com `fgets` e `%Ns` (`D06`), percurso ASCII/`<ctype.h>` (`D07`), `<string.h>` e palíndromo *in-place* (`D08`), linearização *row-major* `i * C + j` com macro `INDICE` sem matrizes 2D (`D09`), além da revisão integradora (`D10`).

### 8.2 Verificações Automatizadas Executadas (`verify_estagio_D.py`)
- **Preservação de piloto:** `D02` (`D02_bloco.md`, `D02_gabarito.md`, `D02_testes.md`, `casos_D02.json` e seus `6` arquivos `.c`) preservado intacto.
- **Auditoria de não-antecipação (Escopo Negativo):** Confirmada ausência absoluta de:
  - Matrizes bidimensionais (`m[i][j]`) em todo o Estágio D (**0 ocorrências**).
  - Funções de usuário além de `int main(void)` (**0 ocorrências**).
  - Uso proibido da função insegura `gets(` (**0 ocorrências**).
  - VLAs (`int v[n]`), `struct` ou alocação dinâmica (`malloc`/`free`) (**0 ocorrências**).
- **Conformidade C99 e Terminal:** Todos os `56` arquivos `.c` possuem `int main(void)` e `return 0;`, e utilizam strings de `printf` estritamente em **ASCII puro**.
- **Oráculo de Testes:** Todos os **`280` casos de teste** catalogados nas 10 suítes JSON foram validados sem divergências.

### 8.3 Pendências Mantidas
- **Compilação binária em GCC:** Continua ausente compilador C no ambiente host Windows/WSL. Nenhum dos `56` arquivos `.c` do Estágio D foi compilado ou executado como binário nativo.
- **Validação com alunos:** Nenhuma aplicação empírica com estudantes foi realizada.

---

## 9. Validação da Fase 3 — Estágio E (`E01`–`E08`)

### 9.1 Entregáveis Produzidos em [estagio_E](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E)
- **Blocos (`8`):** `E01_bloco.md` a `E08_bloco.md` ([blocos](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/blocos)), seguindo o template uniforme de 6 seções (`## 1` a `## 6`), com registro de sessões, critério de domínio de 100% e regra de investigação de pré-requisitos após 2 insucessos. Blocos densos (`E06` e `E08`) divididos em 2 sessões de prática mais checagem independente.
- **Gabaritos (`8`):** `E01_gabarito.md` a `E08_gabarito.md` ([gabaritos](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/gabaritos)), incluindo rastreamentos *row-major* e versões corrigidas de Caça ao Bug.
- **Especificações de teste (`8`), Suítes JSON (`8`) e Soluções C99 (`43` `.c`):**
  - **Suítes de teste JSON (`215` casos no total):** `casos_E01.json` (`25`), `casos_E02.json` (`25`), `casos_E03.json` (`25`), `casos_E04.json` (`25`), `casos_E05.json` (`25`), `casos_E06.json` (`30`), `casos_E07.json` (`25`) e `casos_E08.json` (`35`).
  - **Arquivos `.c` verificáveis (`43` no total em [solucoes](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes)):** cobrindo declaração e E/S tabular (`E01`), busca 2D e extremos com coordenadas `(li, co)` (`E02`), fatiamento e somas por linha e por coluna (`E03`), diagonais, identidade e regiões triangulares (`E04`), transposição retangular, soma e simetria (`E05`), multiplicação matricial com triplo laço `i, j, k` (`E06`), imagens PGM P2 com saturação `[0, 255]`, `static` e generalização n-dimensional (`E07`), além da revisão integradora (`E08`).

### 9.2 Verificações Automatizadas Executadas (`verify_estagio_E.py`)
- **Auditoria de não-antecipação (Escopo Negativo):** Confirmada ausência absoluta de funções de usuário além de `int main(void)` (**0 ocorrências**), VLAs (**0 ocorrências**) e `struct`/`malloc`/`free` (**0 ocorrências**).
- **Conformidade C99 e Terminal:** Todos os `43` arquivos `.c` possuem `int main(void)` e `return 0;`, e utilizam strings de `printf` estritamente em **ASCII puro**.
- **Oráculo de Testes:** Todos os **`215` casos de teste** catalogados nas 8 suítes JSON foram validados sem divergências.

### 9.3 Pendências Mantidas
- **Compilação binária em GCC:** Continua ausente compilador C no ambiente host Windows/WSL. Nenhum dos `43` arquivos `.c` do Estágio E foi compilado ou executado como binário nativo.
- **Validação com alunos:** Nenhuma aplicação empírica com estudantes foi realizada.

---

## 10. Validação da Fase 3 — Estágio F (`F01`–`F10`)

### 10.1 Entregáveis Produzidos em [estagio_F](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F)
- **Blocos (`10`):** `F01_bloco.md` a `F10_bloco.md` ([blocos](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/blocos)), seguindo o template uniforme de 6 seções (`## 1` a `## 6`), com registro de sessões, critério de domínio de 100% e regra de investigação de pré-requisitos após 2 insucessos. O bloco piloto **`F05`** foi mantido estritamente intacto.
- **Gabaritos (`10`):** `F01_gabarito.md` a `F10_gabarito.md` ([gabaritos](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/gabaritos)), com rastreamentos de memória (quadros locais e endereços simbólicos) e versões corrigidas de Caça ao Bug.
- **Especificações de teste (`10`), Suítes JSON (`9`) e Soluções C99 (`54` `.c` + cabeçalhos `.h`):**
  - **Bloco conceitual/papel:** `F09` (Pré-Processamento, Etapas de Compilação e Compilação vs. Interpretação) com gabarito e rubrica verificável em `F09_testes.md`.
  - **Suítes de teste JSON (`230` casos no total):** `casos_F01.json` (`25`), `casos_F02.json` (`25`), `casos_F03.json` (`20`), `casos_F04.json` (`25`), `casos_F05.json` (`30` — piloto), `casos_F06.json` (`25`), `casos_F07.json` (`30`), `casos_F08.json` (`25`) e `casos_F10.json` (`25`).
  - **Arquivos `.c`/`.h` verificáveis (`54` `.c` no total em [solucoes](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes)):** cobrindo funções `void`/`return` (`F01`), protótipos e escopo (`F02`), passagem por valor (`F03`), ponteiros `&`/`*`/`NULL` (`F04`), passagem de endereços por valor (`F05` — piloto), vetores 1D com `const` (`F06`), matrizes 2D `m[][C]` e strings *in-place* (`F07`), organização multi-arquivo `.h`/`.c` com guardas `#ifndef` em subpastas (`F08`), além da revisão integradora multi-arquivo (`F10`).

### 10.2 Verificações Automatizadas Executadas (`verify_estagio_F.py`)
- **Preservação do piloto:** `F05` (`F05_bloco.md`, `F05_gabarito.md`, `F05_testes.md`, `casos_F05.json` e seus `6` arquivos `.c`) preservado intacto.
- **Terminologia C rigorosa:** Confirmadas **0 ocorrências** do termo impróprio *"passagem por referência"* em todos os 10 blocos (uso consistente de *passagem por valor* e *passagem de endereços por valor*).
- **Auditoria de não-antecipação (Escopo Negativo):** Confirmada ausência absoluta de recursividade (**0 ocorrências**), `struct`, VLAs ou alocação dinâmica (`malloc`/`free`) (**0 ocorrências**).
- **Conformidade C99 e Terminal:** Todos os `54` arquivos `.c` utilizam strings de `printf` estritamente em **ASCII puro**.
- **Oráculo de Testes:** Todos os **`230` casos de teste** catalogados nas 9 suítes JSON foram validados sem divergências.

### 10.3 Pendências Mantidas
- **Compilação binária em GCC:** Continua ausente compilador C no ambiente host Windows/WSL. Nenhum dos `54` arquivos `.c` (incluindo os projetos multi-arquivo `.h`/`.c`) foi compilado ou executado como binário nativo.
- **Validação com alunos:** Nenhuma aplicação empírica com estudantes foi realizada.

---

## 11. Validação da Fase 3 — Estágio G (`G01`–`G09`)

### 11.1 Entregáveis Produzidos em [estagio_G](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G)
- **Blocos (`9`):** `G01_bloco.md` a `G09_bloco.md` ([blocos](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/blocos)), aderentes ao template uniforme de 6 seções (`## 1` a `## 6`), com registro de sessões, critério de domínio de 100% e regra de investigação de pré-requisitos após 2 insucessos. Blocos densos (`G05`, `G07`, `G08`, `G09`) organizados em 2 sessões de prática mais checagem independente.
- **Gabaritos (`9`):** `G01_gabarito.md` a `G09_gabarito.md` ([gabaritos](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/gabaritos)), com rastreamentos detalhados de pilha de execução, árvores de chamadas e versões corrigidas de Caça ao Bug.
- **Especificações de teste (`9`), Suítes JSON (`8`) e Soluções C99 (`41` `.c`):**
  - **Bloco conceitual/papel:** `G01` (Conceito de Recursividade e Pilha de Execução — 100% leitura e teste de mesa no papel) com rubrica verificável documentada em `G01_testes.md`.
  - **Suítes de teste JSON (`205` casos no total):** `casos_G02.json` (`20`), `casos_G03.json` (`25`), `casos_G04.json` (`25`), `casos_G05.json` (`30`), `casos_G06.json` (`20`), `casos_G07.json` (`30`), `casos_G08.json` (`25`) e `casos_G09.json` (`30`).
  - **Arquivos `.c` verificáveis (`41` no total em [solucoes](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes)):** cobrindo pré/pós-recursão (`G02`), recursão linear em inteiros e decomposição decimal (`G03`), vetores 1D com redução `n - 1` (`G04`), busca com parada antecipada, máximo sem dupla chamada e média recursiva (`G05`), strings `i + 1` com impressão no retorno (`G06`), dois índices convergentes `i, j` e remoção *in-place* sem laços (`G07`), recursão dupla Fibonacci vs. potenciação rápida `n / 2` (`G08`), além da revisão integradora (`G09`).

### 11.2 Verificações Automatizadas Executadas (`verify_estagio_G.py`)
- **Pureza Recursiva:** Confirmadas **0 ocorrências** de laços (`for`, `while`, `do-while`) dentro de qualquer função recursiva em todos os `41` arquivos `.c`.
- **Auditoria de Escopo Negativo:** Confirmada ausência absoluta de `struct`, VLAs, `gets(` e alocação dinâmica (`malloc`/`free`).
- **Conformidade C99 e Terminal:** Todos os `41` arquivos `.c` possuem `int main(void)` e `return 0;`, e utilizam strings de `printf` estritamente em **ASCII puro**.
- **Oráculo de Testes:** Todos os **`205` casos de teste** catalogados nas 8 suítes JSON foram validados sem divergências.

### 11.3 Pendências Mantidas
- **Compilação binária em GCC:** Continua ausente compilador C no ambiente host Windows/WSL. Nenhum dos `41` arquivos `.c` do Estágio G foi compilado ou executado como binário nativo.
- **Validação com alunos:** Nenhuma aplicação empírica com estudantes foi realizada.

---

## 12. Validação da Fase 3 — Estágio H (`H01`–`H06`)

### 12.1 Entregáveis Produzidos em [estagio_H](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H)
- **Blocos (`6`):** `H01_bloco.md` a `H06_bloco.md` ([blocos](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/blocos)), aderentes ao template uniforme de 6 seções (`## 1` a `## 6`), cobrindo a arquitetura modularizada de 5 arquivos (`main.c`, `imagem.h`, `imagem.c`, `funcoes.h`, `funcoes.c`) do Trabalho Prático PGM P2, além de desafios `[OPCIONAIS]` não bloqueantes em `H06`.
- **Gabaritos (`6`):** `H01_gabarito.md` a `H06_gabarito.md` ([gabaritos](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/gabaritos)).
- **Especificações de teste (`6`), Suítes JSON (`6`) e Projetos Multi-Arquivo C99 (`33` pastas, `100` `.c` + `67` `.h`):**
  - **Suítes de teste JSON (`165` casos no total):** `casos_H01.json` (`25`), `casos_H02.json` (`25`), `casos_H03.json` (`30`), `casos_H04.json` (`25`), `casos_H05.json` (`25`) e `casos_H06.json` (`35`, sendo `25` obrigatórios e `10` `[OPCIONAIS]`).
  - **Projetos verificáveis em [solucoes](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes):** cobrindo esqueleto 5-arquivos e lacuna L3 (`H01`), brilho/limiarização com saturação `[0, 255]` (`H02`), filtro *blur* $t \times t$ com matriz auxiliar `static` e preservação de bordas (`H03`), filtro mediana $3 \times 3$ com função `ordenar` fornecida (`H04`), menu `do-while` + `switch` encadeado (`H05`), modificações ao vivo e desafios opcionais (`H06`).

### 12.2 Verificações Automatizadas Executadas (`verify_estagio_H.py`)
- **Guardas `#ifndef` e Escopo Negativo:** Todos os `67` cabeçalhos `.h` possuem guardas `#ifndef`/`#define`/`#endif`; **0 ocorrências** de `struct`, VLAs, `gets(` ou alocação dinâmica (`malloc`/`free`).
- **Conformidade C99 e Terminal:** Todos os `100` arquivos `.c` utilizam strings de `printf` estritamente em **ASCII puro**.
- **Oráculo de Testes:** Todos os **`165` casos de teste** catalogados nas 6 suítes JSON foram validados sem divergências.

---

## 13. Consolidação Final da Fase 4 — Verificação Global do Curso (`Estágios A–H`)

### 13.1 Inventário Final Consolidado (`verify_global_fase4.py`)
| Estágio | Blocos | Gabaritos | Espec. Testes | Suítes JSON | Casos de Teste | Arquivos `.c` | Cabeçalhos `.h` |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Estágio A** (`A01`–`A10`) | 10 | 10 | 10 | 7 | 78 | 32 | 0 |
| **Estágio B** (`B01`–`B10`) | 10 | 10 | 10 | 10 | 345 | 59 | 0 |
| **Estágio C** (`C01`–`C10`) | 10 | 10 | 10 | 10 | 271 | 59 | 0 |
| **Estágio D** (`D01`–`D10`) | 10 | 10 | 10 | 10 | 280 | 56 | 0 |
| **Estágio E** (`E01`–`E08`) | 8 | 8 | 8 | 8 | 215 | 43 | 0 |
| **Estágio F** (`F01`–`F10`) | 10 | 10 | 10 | 9 | 230 | 54 | 8 |
| **Estágio G** (`G01`–`G09`) | 9 | 9 | 9 | 8 | 205 | 41 | 0 |
| **Estágio H** (`H01`–`H06`) | 6 | 6 | 6 | 6 | 165 | 100 | 67 |
| **TOTAL DO CURSO** | **73** | **73** | **73** | **68** | **1.789** | **444** | **75** |

### 13.2 Integridade Curricular e Pendências Gerais Declaradas
- **Cobertura da ementa:** **11/11 (100%)** dos tópicos oficiais de `ementa_algoritmos.pdf` (`CC61A`) cobertos sem dependências circulares (DAG acíclico).
- **Integridade do diretório:** Todos os `7` documentos estruturais na raiz (`00_inventario_fontes.md`, `00_mapa_curricular.md`, `00_teste_diagnostico.md`, `00_gabarito_diagnostico.md`, `00_guia_orientador.md`, `00_acompanhamento.csv`, `00_relatorio_validacao.md`) presentes e válidos; diretórios residuais `.jev` limpos da pasta de saída; os `45` materiais originais de referência permanecem intactos.
- **Limitação ambiental declarada:** Conforme verificado no Windows e no WSL2 Ubuntu, não há compilador C (`gcc`, `clang`, `cc`, `cl`) instalado nesta máquina. Todas as validações de saída foram realizadas por análise estática de C99 e simulação matemática/lógica via oráculos em Python (`1.789/1.789` casos validados), restando a compilação binária nativa em GCC (`-std=c99 -Wall -Wextra`) pendente para execução em ambiente Linux/GCC com estudantes.
- **Validação empírica com alunos:** Nenhuma aplicação real com estudantes foi executada; todos os tempos estimados de sessão (15–25 min) permanecem como referências iniciais sujeitas à calibração.
