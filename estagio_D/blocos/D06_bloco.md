# Bloco `D06` — Strings em C: Vetor de `char`, Terminador `'\0'` e E/S Segura (`%Ns` e `fgets`)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio D — Vetores Unidimensionais e Strings / **`D06`** |
| **Micro-habilidade foco** | Declarar e ler/exibir strings como vetores de `char` terminados em `'\0'` respeitando a regra `N + 1` e utilizando `scanf` limitado (`%Ns`) ou `fgets` (tratando `'\n'` e evitando `gets`). |
| **Pré-requisitos** | `D01` *(Vetores 1D: declaração, índices base 0, inicialização e limites de memória)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão única de prática + checagem (22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Não utilize** `<string.h>` (`strlen`, `strcpy`, `strcmp`, `strcat`), `<ctype.h>`, matrizes 2D, funções próprias além de `int main(void)` ou VLAs. Use `#define MAX ...`, `char s[MAX];`, laços manuais até `'\0'` apenas para remover `'\n'` ou localizar o terminador, nunca use a função obsoleta `gets`, e mantenha saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **String em C é um vetor de `char` terminado por `'\0'`:** C não possui tipo nativo `string`. Uma cadeia de caracteres é um vetor `char s[TAM];` cujo conteúdo útil termina no **primeiro** caractere nulo `'\0'` (código ASCII **`0`**).
2. **Diferenças críticas (`'\0'` vs `'0'`, `'a'` vs `"a"`):**
   - `'\0'` vale **`0`** (encerra a string no `printf("%s", s)`). Já `'0'` vale **`48`** (é o dígito zero impresso na tela — **nunca** termina uma string!).
   - `'a'` (aspas simples) é um único `char` (`1` byte). `"a"` (aspas duplas) é uma string com `2` bytes: `'a'` seguido de `'\0'`.
3. **Regra `N + 1` e Capacidade vs. Comprimento:** Para armazenar até `N` caracteres úteis, declare sempre `char s[N + 1];`. O tamanho do vetor em bytes (`N + 1`, como `sizeof s`) é a **capacidade**; o **comprimento** da string é a quantidade de caracteres antes do primeiro `'\0'`.
4. **Leitura segura de uma palavra (`scanf` com `%Ns` sem `&`):**
   - Use `scanf("%19s", palavra);` para um vetor `char palavra[20];`.
   - **Nunca use `&`** antes do nome do vetor (o identificador `palavra` já representa o endereço do primeiro elemento).
   - Sempre especifique o limite máximo `N` (`%19s` para vetor de `20`) para impedir invasão de memória (*buffer overflow*). Lembre-se de que `%s` lê apenas até o primeiro espaço ou quebra de linha.
5. **Leitura segura de frase com espaços (`fgets`) e remoção de `'\n'`:**
   - Use `fgets(frase, MAX, stdin);` (lê espaços e limita no máximo a `MAX - 1` caracteres + `'\0'`).
   - **Nunca use a função obsoleta `gets`** (removida do padrão C11 por não possuir limite de tamanho).
   - Se a linha couber no vetor, `fgets` armazena também o `'\n'` antes do `'\0'`. Remova-o percorrendo até `'\0'` e trocando `'\n'` por `'\0'`.
   - **Atenção ao misturar `scanf` e `fgets`:** `scanf` deixa o `'\n'` pendente no teclado! Limpe o restante da linha com `while ((ch = getchar()) != '\n' && ch != EOF) {}` antes de chamar `fgets`.

---

## 2. Exemplos Guiados

### Exemplo 1 — Memória de `char s[8]` e truncamento com `'\0'` *(Diagrama e Trecho ilustrativo)*
Considere a declaração `char s[8] = "C99-OK";` (equivalente a `{'C', '9', '9', '-', 'O', 'K', '\0', '\0'}`):

| Índice | `0` | `1` | `2` | `3` | `4` | `5` | `6` | `7` |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Conteúdo inicial** | `'C'` | `'9'` | `'9'` | `'-'` | `'O'` | `'K'` | `'\0'` (`0`) | `'\0'` (`0`) |

- Capacidade do vetor: `8` bytes (`7` caracteres úteis máximos pela regra `N + 1`).
- Comprimento inicial da string: `6` caracteres (`"C99-OK"`).
- Se executarmos `s[3] = '\0';`, a memória em `s[4]` (`'O'`) e `s[5]` (`'K'`) continua lá, mas `printf("%s\n", s);` para imediatamente no índice `3` e imprime apenas **`C99`**.

### Exemplo 2 — Leitura de código (`%15s`) e descrição com espaços (`fgets`) *(Programa completo)*
```c
#include <stdio.h>
#define MAX_COD 16
#define MAX_DESC 51

int main(void) {
    char codigo[MAX_COD];
    char desc[MAX_DESC];
    int ch;

    scanf("%15s", codigo);
    while ((ch = getchar()) != '\n' && ch != EOF) {
    }

    fgets(desc, MAX_DESC, stdin);
    for (int i = 0; desc[i] != '\0'; i++) {
        if (desc[i] == '\n') {
            desc[i] = '\0';
            break;
        }
    }

    printf("Codigo: %s\nDesc: [%s]\n", codigo, desc);
    return 0;
}
```

---

## 3. Exercícios (`D06-E01` a `D06-E05`)

### Sessão Única (`D06-E01` a `D06-E05`)

### `D06-E01` *(Leitura e Teste de Mesa — Memória, `'\0'` vs `'0'`)*
Considere o trecho abaixo executado em um sistema ASCII:
```c
char s[10] = "UTFPR";
s[5] = '!';
s[2] = '\0';
s[1] = '0';
printf("%s\n", s);
```
Sem usar computador, responda:
1. Qual é a **capacidade máxima de caracteres úteis** que `s[10]` pode armazenar com segurança?
2. Qual é a diferença de valor numérico (ASCII) entre o que foi gravado em `s[2]` e o que foi gravado em `s[1]`?
3. O que exatamente `printf("%s\n", s);` imprime na tela? Por que `'!'` em `s[5]` não aparece?

---

### `D06-E02` *(Completar solução)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` do programa abaixo que lê uma frase de **até 40 caracteres úteis** (podendo conter espaços), remove o `'\n'` deixado por `fgets` e exibe a frase entre colchetes `[frase]`:

```c
#include <stdio.h>
#define MAX /* A */

int main(void) {
    char frase[MAX];

    fgets(frase, /* B */, stdin);
    for (int i = 0; frase[i] != /* C */; i++) {
        if (frase[i] == '\n') {
            frase[i] = /* D */;
            break;
        }
    }

    printf("[%s]\n", frase);
    return 0;
}
```

---

### `D06-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler um código sem espaços de **até 15 caracteres úteis** e, na linha seguinte, uma descrição com espaços de **até 50 caracteres úteis**, imprimindo `Codigo: <codigo>\nDesc: [<desc>]\n`. Identifique os **3 bugs intencionais** (no papel ou em comentários `//`) e escreva a versão corrigida completa:

```c
#include <stdio.h>
#define MAX_COD 15
#define MAX_DESC 51

int main(void) {
    char codigo[MAX_COD];
    char desc[MAX_DESC];
    int ch;

    scanf("%s", &codigo);
    while ((ch = getchar()) != '\n' && ch != EOF) {
    }

    fgets(desc, MAX_DESC, stdin);
    for (int i = 0; desc[i] != '\0'; i++) {
        if (desc[i] == '\n') {
            desc[i] = '0';
            break;
        }
    }

    printf("Codigo: %s\nDesc: [%s]\n", codigo, desc);
    return 0;
}
```

---

### `D06-E04` *(Variação controlada com pistas)*
Escreva um **programa completo** em C que leia:
1. Uma palavra `tag` (sem espaços) de até **20 caracteres úteis**;
2. Na linha seguinte, um `titulo` (que pode conter espaços) de até **60 caracteres úteis**.

Remova eventual `'\n'` de `titulo` e imprima exatamente:
```text
Tag: <tag>
Titulo: [<titulo>]
```
*Pista:* Respeite a regra `N + 1` (`#define MAX_TAG 21` e `#define MAX_TITULO 61`), use `%20s` sem `&` e limpe o buffer com `getchar()` antes do `fgets`.

---

### `D06-E05` *(Resolução independente)*
Escreva um **programa completo** em C que leia uma linha de texto com até **80 caracteres úteis** (podendo conter espaços) usando `fgets` e removendo `'\n'`. Em seguida, leia um único caractere `alvo` (`scanf(" %c", &alvo);`) e **trunque** a string na primeira ocorrência de `alvo`, substituindo-o por `'\0'` (se `alvo` não existir na linha, mantenha a string intacta). Imprima exatamente:
```text
Resultado: [<texto>]
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `D06-C01` *(Teste de Mesa)*
Dado o trecho:
```c
char v[8] = "ALGO";
v[4] = 'X';
v[2] = '\0';
printf("%s\n", v);
```
Responda sem compilar:
1. Qual é a saída exata impressa por `printf`?
2. Qual é o valor numérico armazenado em `v[2]` e qual seria o valor se estivesse escrito `'0'`?
3. O caractere `'X'` em `v[4]` pertence à string impressa? Justifique.

---

### `D06-C02` *(Caça ao Bug — Programa completo)*
O programa abaixo deveria ler uma `sigla` sem espaços de **até 10 caracteres úteis** e, na linha seguinte, o nome de uma `cidade` com espaços de **até 30 caracteres úteis**, imprimindo `Sigla: <sigla> | Cidade: <cidade>\n`. Corrija todos os **3 defeitos** presentes:

```c
#include <stdio.h>
#define MAX_SIGLA 10
#define MAX_CIDADE 31

int main(void) {
    char sigla[MAX_SIGLA];
    char cidade[MAX_CIDADE];

    scanf("%s", &sigla);

    fgets(cidade, MAX_CIDADE, stdin);
    for (int i = 0; cidade[i] != '\0'; i++) {
        if (cidade[i] == '\n') {
            cidade[i] = '\0';
            break;
        }
    }

    printf("Sigla: %s | Cidade: %s\n", sigla, cidade);
    return 0;
}
```

---

### `D06-C03` *(Programa completo independente)*
Escreva um programa completo em C que leia:
1. Uma matrícula `mat` (palavra sem espaços de até **12 caracteres úteis**);
2. Na linha seguinte, um `nome` completo com espaços (até **50 caracteres úteis**);
3. Na terceira linha, uma `disciplina` com espaços (até **40 caracteres úteis**).

Remova eventual `'\n'` das linhas lidas com `fgets` e imprima exatamente:
```text
Matricula: <mat>
Nome: <nome>
Disciplina: <disciplina>
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `D07` (`Percurso Manual de Strings e Transformações de Caracteres`):** somente após autocorreção de `D06-E01..E05` e **100% (3/3)** em `D06-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** revisar a diferença entre `'\0'` (`0`) e `'0'` (`48`), a regra `N + 1`, a omissão do `&` em `%Ns` e a limpeza do `\n` entre `scanf` e `fgets`; aplicar variante `V2` de `D06`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar o pré-requisito **`D01`** (índices base `0`, capacidade `N` vs. último índice válido `N - 1` e endereço com `&` em tipos escalares vs. vetores).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 2 — cadeia de caracteres).
- `[DOC]` `Aula_13_Algoritmos.pdf` p. 3–15, 19–20 (strings como vetores de `char`, `'\0'`, `scanf`, `fgets`, proibição de `gets`).
- `[DOC]` `Lista7_Algoritmos.pdf` p. 1–2.
- Casos de teste e soluções verificáveis: [D06_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/gabaritos/D06_gabarito.md) e [D06_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/D06_testes.md).
