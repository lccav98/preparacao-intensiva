# Bloco `A02` — Anatomia de um Programa em C e Compilação no GCC/Linux

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio A — Fundamentos de Algoritmos, Ambiente C, Variáveis e Representação de Dados / **`A02`** |
| **Micro-habilidade foco** | Escrever a estrutura mínima compilável em C (`#include <stdio.h>`, `int main(void)`, `return 0;`, comentários) e compilar/executar via `gcc` no terminal Linux. |
| **Pré-requisitos** | `A01` *(Problemas computacionais, algoritmos e abstração)* + `[INF]` comandos mínimos de terminal Linux (`pwd`, `ls`, `cd`, `./executavel`) |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`A02-E01`–`A02-E05`, 20 min):** `11 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`A02-C01`–`A02-C03`, 15 min):** `10 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Permitido:** `#include <stdio.h>`, `int main(void)`, `return 0;`, `;`, `//`, `/* */`, diferenciação maiúsculas/minúsculas (*case-sensitive*) e `printf` simples usando **no máximo `\n`** (texto estritamente ASCII, sem acentos). **Proibido:** qualquer variável, `scanf`, `\t`, `\"`, `\\`, `%d`, `%f`, `%c`, operadores aritméticos/relacionais, `if` ou laços. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`A02-E01`–`A02-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`A02-C01`–`A02-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Comandos mínimos de terminal Linux (`[INF]` pré-requisito operacional):**
   - `pwd` → exibe a pasta atual onde você está; `ls` → lista os arquivos da pasta; `cd pasta` → entra na subpasta indicada.
   - Compilar no padrão **C99** exigido no curso: `gcc -std=c99 -Wall -Wextra arquivo.c -o programa`
   - Executar o binário gerado na pasta atual: `./programa`
2. **Anatomia mínima obrigatória em C:**
   - `#include <stdio.h>`: inclui a biblioteca padrão de entrada e saída (necessária para reconhecer `printf`).
   - `int main(void) { ... }`: função principal onde a execução do programa sempre começa.
   - `;` (ponto-e-vírgula): encerra instruções em C (como `printf(...);` e `return 0;`). Diretivas `#include` **não** levam `;`.
   - `return 0;`: encerra `main` sinalizando término normal ao sistema operacional.
3. **C é *case-sensitive*:** diferencia maiúsculas de minúsculas (`int` ≠ `Int`; `main` ≠ `Main`; `printf` ≠ `Printf`; `return` ≠ `Return`).
4. **Comentários (ignorados pelo compilador):**
   - Linha única: `// texto ate o fim da linha`
   - Bloco (múltiplas linhas): `/* texto */` — sempre feche com `*/`, caso contrário o compilador ignora o restante do arquivo!
5. **Algoritmo vs. Programa em C (`Lista8` Ex. 1c):** o algoritmo descreve a solução em linguagem natural/independente de máquina; o programa em C é a tradução exata sujeita às regras rígidas de sintaxe do compilador.

---

## 2. Exemplos Guiados

### Exemplo 1 — Diagnosticando erros de sintaxe e fluxo no terminal *(Trecho ilustrativo)*
Observe os 3 erros neste trecho inválido:

```c
int Main(void) {
    Printf("Inicio do programa\n")
    return 0;
}
```
- **Erro 1:** `Main` com `M` maiúsculo (C é *case-sensitive*; a função de entrada obrigatória chama-se `main`).
- **Erro 2:** `Printf` com `P` maiúsculo (a função da biblioteca `<stdio.h>` chama-se `printf`, além de faltar `#include <stdio.h>` no topo).
- **Erro 3:** falta ponto-e-vírgula `;` ao final da linha `Printf(...)`.

**Fluxo no terminal após corrigir e salvar como `inicio.c` dentro da pasta `aula02`:**
```text
cd aula02
ls
gcc -std=c99 -Wall -Wextra inicio.c -o inicio
./inicio
```

### Exemplo 2 — Estrutura completa do programa mínimo compilável *(Programa completo)*

```c
/*
   Programa: Boas-vindas
   Objetivo: Exibir saudacao simples no terminal
*/
#include <stdio.h>

int main(void) {
    // Imprime uma linha de texto e quebra a linha com \n
    printf("Bem-vindo a CC61A!\n");
    return 0;
}
```
**Leitura da estrutura:** o comentário `/* ... */` abre e fecha corretamente antes de `#include <stdio.h>`; `int main(void)` abre `{` e fecha `}`; dentro dela há um comentário `//`, uma chamada `printf` terminada por `;` (texto estritamente ASCII, sem acentos) e `return 0;`.

---

## 3. Exercícios (`A02-E01` a `A02-E05`)

### `A02-E01` *(Leitura e Diagnóstico no papel — Reprodução do modelo)*
Sem utilizar computador, analise os 4 trechos ilustrativos abaixo (supondo `#include <stdio.h>` já incluído e estando dentro de `int main(void)`). Para cada item, indique se está válido ou qual **erro exato** impede a compilação:
- **(a)** `printf("Curso de C);`
- **(b)** `Printf("Teste\n");`
- **(c)** `printf "Algoritmos\n";`
- **(d)** `print("Ola\n");`

**(e)** No terminal Linux, após compilar `gcc -std=c99 -Wall -Wextra ola.c -o meu_prog`, por que digitamos `./meu_prog` em vez de apenas `meu_prog`?

---

### `A02-E02` *(Completar esqueleto + comando GCC)*
Suponha que o arquivo `saudacao.c` está salvo na subpasta `pratica_a02`. Complete as lacunas `/* A */`, `/* B */` e `/* C */` no programa completo abaixo para que ele imprima `Linguagem C ativa` seguido de quebra de linha (`\n`), e preencha os 3 comandos de terminal:

```c
/* Programa de saudacao */
/* A */

int main(void) {
    /* B */
    /* C */
}
```
Sequência no terminal Linux:
1. Entrar na pasta: `(___ 1 ___) pratica_a02`
2. Compilar no padrão do curso gerando executável `saudacao`: `gcc -std=c99 -Wall -Wextra (___ 2 ___) -o saudacao`
3. Executar o programa gerado: `(___ 3 ___)`

---

### `A02-E03` *(Caça ao Bug — Programa completo)*
O programa abaixo deveria compilar sem avisos no GCC e exibir exatamente as duas linhas:
```text
UTFPR Ponta Grossa
Laboratorio GCC
```
Identifique os **4 bugs intencionais** no código (anotando no papel ou em comentários `//`) e escreva a **versão corrigida completa**:

```c
/*
   Exercicio A02-E03
   Objetivo: Exibir instituicao e laboratorio
#include <stdio.h>

Int main(void) {
    printf("UTFPR Ponta Grossa\n")
    Printf("Laboratorio GCC\n");
    return 0;
}
```

---

### `A02-E04` *(Variação controlada com pistas)*
Escreva um **programa completo** em C que comece com um **comentário de linha (`//`)** descrevendo a finalidade do arquivo e imprima exatamente as três linhas abaixo (sem acentos e sem variáveis):

```text
Passo 1: Editar codigo
Passo 2: Compilar com gcc
Passo 3: Executar no Linux
```
*Pistas:* Inclua `<stdio.h>`, declare `int main(void)`, use três chamadas `printf("...\n");` (terminando cada uma com `\n` dentro das aspas e `;` fora dos parênteses) e finalize com `return 0;`.

---

### `A02-E05` *(Resolução independente)*
**(a)** Escreva um **programa completo** em C com um **comentário de bloco (`/* ... */`)** no topo descrevendo sua finalidade, que imprima exatamente o quadro informativo abaixo (sem variáveis, sem acentos e com `\n` ao final de cada linha):

```text
Curso: Algoritmos CC61A
Padrao: C99
Compilador: GCC Linux
```

**(b)** *(Reflexão — `Lista8` Ex. 1c)* Em 2 linhas no papel, explique a diferença entre o **algoritmo** em linguagem natural para exibir essas três informações e o **programa em C** que você escreveu no item (a).

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `A02-C01` *(Diagnóstico de erros de sintaxe no papel)*
Sem usar computador, analise o trecho completo abaixo e aponte os **3 erros** que impedem a compilação limpa ou execução esperada, explicando brevemente cada falha:

```c
#include <stdio.h>

int main(void) {
    printf("Linha 1\n")
    print("Linha 2\n");
    Return 0;
}
```

### `A02-C02` *(Caça ao Bug — Comentário, case e estrutura — Programa completo)*
O programa abaixo deveria compilar sem avisos e exibir exatamente:
```text
Sistema pronto
Status: OK
```
Identifique todos os defeitos de comentário, *case-sensitivity* e estrutura, e escreva a **versão corrigida completa**:

```c
/* Inicio do programa
#include <stdio.h>

int Main(void) {
    printf("Sistema pronto\n");
    // printf("Status: OK\n");
    return 0
}
```

### `A02-C03` *(Programa mínimo compilável do zero)*
Escreva do zero um **programa completo** em C (com comentário inicial, `#include <stdio.h>`, `int main(void)` e `return 0;`) que imprima exatamente as duas linhas abaixo:

```text
Compilacao limpa
Execucao concluida
```
Informe também o comando exato no terminal Linux para compilar o arquivo `A02_C03.c` gerando o executável `app` no padrão C99 (`-Wall -Wextra`) e o comando para executá-lo.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `A03` (`Saída Formatada com printf e Sequências de Escape`):** somente após autocorreção da bateria `A02-E01..E05` **e** **100% (3/3)** na Checagem Independente `A02-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** revisar a lista de erros comuns (`;`, aspas fechadas, fechamento `*/`, palavras reservadas em minúsculas) ou os comandos de terminal (`cd`, `gcc ... -o ...`, `./...`) no Exemplo 1 e aplicar a variante `V2` de `A02`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar o pré-requisito **`A01`** (compreensão da transição algoritmo → código-fonte → compilador → executável) e praticar passo a passo os comandos de navegação no terminal (`pwd`, `ls`, `cd`) antes de retornar a `A02`.

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (itens 1 e 11 — algoritmo, linguagem de programação, programa e compilação).
- `[DOC]` `Aula_00_Algoritmos.pdf` p. 3 (ambiente obrigatório: C, compilador GCC em plataforma Linux).
- `[DOC]` `Aula_02_Algoritmos.pdf` p. 2, 4–8, 10, 13 (código-fonte, GCC/Linux, `<stdio.h>`, estrutura básica, comentários `//` e `/* */`, *case-sensitive*, primeiro programa e erros comuns em `printf`).
- `[DOC]` `Lista8_Algoritmos_Revisao.pdf` p. 1 (Ex. 1c — diferença entre algoritmo e implementação em programa C).
- `[INF]` Pré-requisito operacional mínimo (`pwd`, `ls`, `cd`, `./executavel`) e padrão de compilação `gcc -std=c99 -Wall -Wextra` adotados em [00_mapa_curricular.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/00_mapa_curricular.md) e [00_guia_orientador.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/00_guia_orientador.md).
- Gabarito comentado e especificação de testes: [A02_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/gabaritos/A02_gabarito.md) e [A02_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/A02_testes.md).
