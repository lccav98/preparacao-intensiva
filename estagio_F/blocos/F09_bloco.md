# Bloco `F09` — Pré-Processamento, Etapas de Compilação e Compilação vs. Interpretação

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio F — Modularização, Funções, Ponteiros e Compilação Multi-Arquivo / **`F09`** |
| **Micro-habilidade foco** | Explicar e rastrear as etapas de transformação do código-fonte C em executável (pré-processamento `#include`/`#define`, compilação e ligação) e distinguir compilação (C) de interpretação/máquina virtual (Python/Java). |
| **Pré-requisitos** | `F08` *(Organização multi-arquivo `.h` e `.c`, guardas `#ifndef` e ligação no GCC)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão (`E01`–`E05`, 18 min):** `10 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C04`, 12 min):** `8 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **100% papel e análise conceitual.** **Não há** criação de projetos executáveis nem introdução de recursividade (`G01`). Inspeção opcional de estágios do GCC (`-E`, `-c`) serve apenas como apoio visual conceitual. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C04`, sem gabarito):** `___ / 4` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **As 3 grandes etapas do código-fonte C até o executável:**
   - **1. Pré-processamento (`gcc -E`):** opera puramente sobre **texto** (sem analisar tipos ou sintaxe C). Remove comentários, expande `#include` (colando o conteúdo do `.h`), substitui macros `#define` e avalia diretivas condicionais (`#ifndef`/`#define`/`#endif`).
   - **2. Compilação (`gcc -c`):** analisa sintaxe e tipos C de cada arquivo `.c` **isoladamente** e gera um arquivo-objeto em código de máquina (`.o`), ainda com referências externas pendentes.
   - **3. Ligação / *Linking*:** reúne todos os `.o` (e bibliotecas padrão como `stdio`) e resolve as chamadas entre módulos, produzindo o executável final (`prog`).
2. **Mapeamento direto de erros às etapas:**
   - `No such file or directory` → falha no **Pré-processamento** (`#include`).
   - Erro de sintaxe ou `conflicting types` → falha na **Compilação**.
   - `undefined reference` ou `multiple definition` → falha na **Ligação**.
3. **Compilação vs. Interpretação / VM:**
   - **Compilação (C):** todo o código é traduzido **antes** da execução para código de máquina nativo. Erros de sintaxe/tipos impedem gerar o executável (mesmo em ramos `if (0)` nunca executados); execução é rápida, mas o binário depende da arquitetura/SO alvo.
   - **Interpretação (ex.: Python):** um programa **interpretador** lê e executa o código-fonte (ou *bytecode* interno) linha a linha em tempo de execução. É portátil entre máquinas com o interpretador instalado, mas tende a ser mais lenta e certos erros de nome/tipo aparecem apenas quando o fluxo atinge aquela linha.
   - **Modelo híbrido com *Bytecode* + VM (ex.: Java):** compila para *bytecode* intermediário (`.class`), executado depois por uma máquina virtual (JVM), equilibrando verificação prévia e portabilidade.

---

## 2. Exemplos Guiados *(100% no papel)*

### Exemplo 1 — Expansão textual do pré-processador
Dados:
**`taxa.h`**
```c
#ifndef TAXA_H
#define TAXA_H
#define FATOR 10
int aplicar(int v);
#endif
```
**`main.c`**
```c
#include "taxa.h"
#include "taxa.h" /* segunda inclusao */

int main(void) {
    return aplicar(FATOR);
}
```
**Código após o pré-processamento (visto pelo compilador):**
```c
int aplicar(int v);

int main(void) {
    return aplicar(10);
}
```
Observe: na 1ª inclusão, `TAXA_H` ainda não estava definido, logo `FATOR` foi registrado e `int aplicar(int v);` foi colado. Na 2ª inclusão, `TAXA_H` já existia, portanto o bloco inteiro foi descartado. Por fim, `FATOR` virou `10` e o comentário foi removido.

### Exemplo 2 — Comparação resumida (C × Python × Java)

| Critério | C (Compilada) | Python (Interpretada) | Java (Bytecode + JVM) |
|---|---|---|---|
| **Artefato distribuído** | Executável binário nativo | Código-fonte `.py` | *Bytecode* `.class` / `.jar` |
| **Quem executa** | CPU diretamente (SO) | Interpretador Python | Máquina Virtual (JVM) |
| **Detecção de erro de tipo** | Antes de rodar (compilação) | Em tempo de execução | Antes de rodar (compilação) |

---

## 3. Exercícios (`F09-E01` a `F09-E05` — Papel)

### `F09-E01` *(Rastreamento da expansão textual do pré-processador)*
Dados os arquivos abaixo:

**`calc.h`**
```c
#ifndef CALC_H
#define CALC_H
#define LIMITE 50
int dobrar(int x);
#endif
```
**`app.c`**
```c
#include "calc.h"
#include "calc.h"

int main(void) {
    /* leitura omitida */
    int r = dobrar(LIMITE);
    return r;
}
```
Escreva exatamente o código resultante que o compilador recebe após o **pré-processamento**, explicando o que ocorreu com a segunda diretiva `#include "calc.h"`, com `LIMITE` e com o comentário.

---

### `F09-E02` *(Completar lacunas — Pipeline e flags do GCC)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */`:
1. A ordem correta das 3 etapas do GCC é: **/* A */** → **/* B */** → **/* C */**.
2. Para parar logo após gerar o código-objeto `.o` de `mod.c` sem ligar o executável, usa-se a opção `gcc -std=c99 /* D */ mod.c`.
3. O erro `undefined reference to 'dobrar'` ocorre na etapa **/* C */**.

---

### `F09-E03` *(Caça ao Erro Conceitual — Sem compilador)*
Analise as 3 afirmações falsas abaixo, explique por que cada uma está incorreta e apresente a afirmação corrigida:
1. *"O pré-processador verifica se a função `soma` foi chamada com argumentos do tipo `int` correto."*
2. *"Escrever `#define PI 3.14;` com ponto-e-vírgula nunca causa problema em expressões como `2 * PI * r`."*
3. *"Durante `gcc -c main.c`, o compilador precisa que `mod.c` já tenha sido compilado para saber onde está o código de máquina da função declarada em `mod.h`."*

---

### `F09-E04` *(Variação controlada com pistas — Compilação vs. Interpretação)*
Responda comparando **C**, **Python** e **Java**:
- **(a)** Por que um programa em C compilado no Linux x86-64 normalmente **não** executa diretamente em um celular ARM, enquanto o mesmo `.class` Java ou `.py` Python pode rodar em ambos?
- **(b)** Em termos de desempenho bruto de CPU, por que o binário C tende a ser mais rápido que um script Python equivalente?
*Pista:* Considere quem traduz as instruções (CPU nativa vs. interpretador/JVM em tempo de execução).

---

### `F09-E05` *(Resolução independente — Cenário completo)*
Considere um projeto com `main.c`, `math_ops.h` e `math_ops.c`:
- **(a)** Se executarmos apenas `gcc -std=c99 -c main.c` (sem citar `math_ops.c`), o comando gera `main.o` ou falha? Por quê?
- **(b)** Se em seguida executarmos `gcc main.o -o prog` (sem `math_ops.o`), qual etapa falha e com qual mensagem típica?
- **(c)** Considere um trecho dentro de `if (0) { z = nao_existe + 1; }` em C e em Python (onde `nao_existe` nunca foi definida). Qual é a diferença de comportamento entre as duas linguagens?

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `F09-C01` *(Etapas do processo de construção em C)*
Liste em ordem cronológica as 3 etapas que transformam arquivos `.c`/`.h` em um programa executável em C e indique a principal função e o resultado de cada etapa.

### `F09-C02` *(Papel do pré-processador e `#ifndef`)*
Explique o que o pré-processador faz ao encontrar `#include "arq.h"` e `#define MAX 100`, e por que a ausência de guardas `#ifndef` pode gerar erros em projetos com múltiplos cabeçalhos.

### `F09-C03` *(Compilação vs. Interpretação)*
Compare **compilação (C)** e **interpretação (Python)** quanto a:
1. Momento da tradução;
2. Necessidade de compilador/interpretador no computador do usuário final;
3. Detecção de erros antes de executar vs. durante a execução.

### `F09-C04` *(Portabilidade e compilação separada `.o`)*
1. Explique a diferença de portabilidade entre um executável gerado pelo GCC em C e um arquivo `.class` em Java.
2. Por que `gcc -c a.c` funciona sem `b.c` (desde que `a.c` inclua `b.h`), mas gerar o executável final exige passar `a.o` e `b.o` (ou `a.c` e `b.c`)?

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `F10` (`Revisão e Consolidação do Estágio F`):** somente após autocorreção de `F09-E01..E05` e **100% (4/4)** na Checagem Independente `F09-C01..C04` sem gabarito.
- **Recuperação direcionada (1ª falha):** redesenhar o diagrama de 3 caixas (`Pré-processamento -> Compilação -> Ligação`) associando cada flag (`-E`, `-c`) e cada erro (`F08`), e aplicar variante `V2` de `F09`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`F08`** (separação `.h`/`.c` e erros de ligação) e **`A02`** (anatomia da compilação C no GCC).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 11 — Conceitos e características das linguagens de programação; compilação e interpretação).
- `[DOC]` `Aula_20_Algoritmos_Roteiro_Atividade_Assíncrona.pdf` p. 1–2 (roteiro conceitual e questões de compilação vs. interpretação e pré-processamento).
- Rubrica e gabarito verificável: [F09_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/gabaritos/F09_gabarito.md) e [F09_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/F09_testes.md).
