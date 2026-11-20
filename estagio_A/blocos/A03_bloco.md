# Bloco `A03` — Saída Formatada com `printf` e Sequências de Escape

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio A — Fundamentos de Algoritmos, Ambiente C, Variáveis e Representação de Dados / **`A03`** |
| **Micro-habilidade foco** | Construir saídas textuais exatas no terminal usando `printf`, aspas duplas e sequências de escape (`\n`, `\t`, `\"`, `\\`). |
| **Pré-requisitos** | `A02` *(Anatomia mínima de programa em C e compilação no GCC/Linux)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`A03-E01`–`A03-E05`, 18 min):** `10 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`A03-C01`–`A03-C03`, 15 min):** `10 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Permitido:** tudo de `A02` mais `\n`, `\t`, `\"` e `\\` em `printf` (inclusive único `printf` multilinhas, texto estritamente ASCII sem acentos). **Proibido:** variáveis, `#define`/`const`, especificadores (`%d`, `%f`, `%c`, `%s`), `scanf`, operadores aritméticos/relacionais, `if` ou laços. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`A03-E01`–`A03-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`A03-C01`–`A03-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **`printf` não quebra linha sozinho:** chamadas seguidas como `printf("A"); printf("B");` imprimem `AB` colado na mesma linha. A quebra de linha só acontece exatamente onde existe `\n`.
2. **As 4 sequências de escape essenciais:**
   - `\n` → nova linha (*Enter* / quebra de linha).
   - `\t` → tabulação horizontal (avança até a próxima parada de tabulação).
   - `\"` → exibe aspas duplas literais `"` sem encerrar a string.
   - `\\` → exibe uma única barra invertida literal `\`.
3. **Múltiplas linhas em um único `printf`:** basta encadear `\n` dentro da mesma string (ex.: `printf("Linha 1\nLinha 2\n");`).
4. **Armadilha clássica:** escrever `C:\teste` dentro de `printf` faz o compilador ler `\t` como **tabulação** (imprimindo `C:    este`), e escrever `"` sem barra fecha a string antes da hora e quebra a compilação! Para imprimir uma barra `\`, escreva sempre duas (`\\`).

---

## 2. Exemplos Guiados

### Exemplo 1 — Rastreamento caractere a caractere com `\t`, `\\` e `\"` *(Trecho ilustrativo)*
Analise o trecho ilustrativo abaixo:

```c
printf("Pasta:\tC:\\algoritmos\n");
printf("Aviso: \"Salvar\"\n");
```
**Rastreamento da saída no terminal** (representando o caractere de tabulação por `<TAB>`):
- Linha 1: `Pasta:` → `\t` gera `<TAB>` → `C:` → `\\` vira `\` → `algoritmos` → `\n` quebra a linha.
  Resultado: `Pasta:<TAB>C:\algoritmos`
- Linha 2: `Aviso: ` → `\"` vira `"` → `Salvar` → `\"` vira `"` → `\n` quebra a linha.
  Resultado: `Aviso: "Salvar"`

### Exemplo 2 — Tabela simples em único `printf` multilinhas *(Programa completo)*

```c
#include <stdio.h>

int main(void) {
    printf("Item\tQtd\nCaderno\t2\nCaneta\t5\n");
    return 0;
}
```
**Saída produzida** (com `<TAB>` indicando o byte `\t` emitido pelo programa):
```text
Item<TAB>Qtd
Caderno<TAB>2
Caneta<TAB>5
```
Note que todas as 3 linhas foram geradas por **uma única chamada `printf`**.

---

## 3. Exercícios (`A03-E01` a `A03-E05`)

### `A03-E01` *(Teste de Mesa caractere a caractere — Reprodução do modelo)*
Sem utilizar computador, escreva linha a linha a saída exata do trecho ilustrativo abaixo (indique `<TAB>` onde houver `\t` e sinalize se a última linha tem ou não quebra final):

```c
printf("Log:\t\"ok\"");
printf("\nRota:\t/home\\aluno\n");
printf("Fim");
```

---

### `A03-E02` *(Completar sequências de escape)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` usando exclusivamente `\t`, `\"` ou `\\` para que o trecho ilustrativo exiba exatamente (com `<TAB>` indicando tabulação):
```text
Arquivo: "dados.txt"
Local:<TAB>C:\temp\relatorio
```

```c
printf("Arquivo: /* A */dados.txt/* B */\n");
printf("Local:/* C */C:/* D */temp/* D */relatorio\n");
```

---

### `A03-E03` *(Caça ao Bug de aspas e barra — Programa completo)*
O programa completo abaixo deveria imprimir exatamente as duas linhas:
```text
Diretorio: C:\usuarios\aluno
Mensagem: "Compilado!"
```
Identifique os **3 bugs intencionais** nas sequências de escape (anotando no papel ou em comentários `//`) e escreva a **versão corrigida completa**:

```c
#include <stdio.h>

int main(void) {
    printf("Diretorio: C:\usuarios\aluno\n");
    printf("Mensagem: "Compilado!"\n");
    return 0;
}
```

---

### `A03-E04` *(Variação controlada com pistas — Único `printf` multilinhas)*
Inspirado no exercício da `Aula_02` (p. 15), escreva um **programa completo** em C (com comentário inicial descrevendo a finalidade) utilizando **apenas uma única chamada à função `printf`** que imprima exatamente as 3 linhas abaixo (sem acentos):

```text
UTFPR - Campus Ponta Grossa
Disciplina: Algoritmos
Padrao: "C99"
```
*Pistas:* Encadeie `\n` entre os textos dentro da mesma string entre aspas duplas, use `\"` ao redor de `C99` e inclua `\n` ao final da terceira linha.

---

### `A03-E05` *(Resolução independente — Layout tabular e escapes)*
Escreva um **programa completo** em C que exiba a tabela abaixo no terminal, separando as duas colunas de cada linha com **exatamente uma tabulação (`\t`)** (indicada abaixo por `<TAB>`), preservando aspas duplas, barras invertidas e quebra de linha `\n` ao final de cada linha:

```text
Comando<TAB>Funcao
"gcc"<TAB>Compila C
\n<TAB>Nova linha
\\<TAB>Barra literal
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `A03-C01` *(Previsão de saída no papel)*
Sem usar computador, escreva exatamente o que será exibido no terminal (marcando `<TAB>` para tabulação e cada quebra de linha) pelo trecho abaixo:

```c
printf("Caminho:\t\"src\\main.c\"\n");
printf("Status:\tPronto\n");
```

### `A03-C02` *(Caça ao Bug de escapes — Programa completo)*
O programa abaixo deveria imprimir exatamente (onde `<TAB>` representa `\t`):
```text
Codigo:<TAB>100
Rota:<TAB>C:\projetos\teste
Nota:<TAB>"Aprovado"
```
Identifique os **4 defeitos** de quebra de linha, barra invertida e aspas, e escreva a **versão corrigida completa**:

```c
#include <stdio.h>

int main(void) {
    printf("Codigo:\t100");
    printf("Rota:\tC:\projetos\teste\n");
    printf("Nota:\t"Aprovado"\n");
    return 0;
}
```

### `A03-C03` *(Único `printf` multilinhas independente)*
Escreva um **programa completo** em C que utilize **apenas uma única chamada `printf`** para imprimir exatamente as 3 linhas abaixo (usando `\t` onde aparece `<TAB>` e terminando com `\n`):

```text
Relatorio<TAB>"Final"
Pasta:<TAB>D:\aulas\c
Situacao:<TAB>OK
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `A04` (`Identificadores, Palavras Reservadas e Declaração de Variáveis`)** *(ou seguir para `A05` quando `A04` já estiver concluído)*: somente após autocorreção de `A03-E01..E05` **e** **100% (3/3)** na Checagem Independente `A03-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** rastrear no papel caractere a caractere onde `\` inicia um comando especial (`\n`, `\t`, `\"`, `\\`), revisando a diferença entre `\` simples (início de escape) e `\\` (barra literal), e aplicar a variante `V2` de `A03`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar o pré-requisito **`A02`** (estrutura básica `int main(void)`, pontuação `;` e delimitação de strings entre `"..."` no `printf`) antes de retornar a `A03`.

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 4 — Instruções de entrada, saída e atribuição: definições, sintaxe e exemplos).
- `[DOC]` `Aula_02_Algoritmos.pdf` p. 12–15 (saída de dados `printf`, sequências de escape `\n`, `\t`, `\"`, `\\` e Exercício da p. 15 com única chamada `printf`).
- Gabarito comentado, casos JSON e especificação de testes: [A03_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/gabaritos/A03_gabarito.md) e [A03_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/A03_testes.md).
