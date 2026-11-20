# Bloco `D07` — Percurso Manual de Strings e Transformações de Caracteres (ASCII e `<ctype.h>`)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio D — Vetores Unidimensionais e Strings / **`D07`** |
| **Micro-habilidade foco** | Percorrer strings manualmente até `'\0'` para contar, validar, filtrar espaços excedentes e transformar caracteres via intervalos ASCII (`'a'..'z'`, `'A'..'Z'`) ou `<ctype.h>`. |
| **Pré-requisitos** | `D06` *(Strings em C: vetor de `char`, terminador `'\0'` e E/S segura)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 20 min):** `12 min` resol. \| `5 min` corr. \| `3 min` recup.; **Sessão 2 (`E04`–`E06`, 22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Não utilize** `<string.h>` (`strlen`, `strcpy`, `strcmp`, `strcat`), matrizes 2D, funções próprias além de `int main(void)` ou VLAs. Use `#define MAX ...`, percurso manual com `s[i] != '\0'`, aritmética ASCII e `<ctype.h>`, nunca use `gets`, e mantenha saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Percurso manual até o terminador:** Para inspecionar ou contar caracteres sem conhecer o comprimento prévio, use `for (int i = 0; s[i] != '\0'; i++)`. O laço encerra automaticamente no primeiro `'\0'`.
2. **Contagem de palavras com múltiplos espaços (Máquina de Estados):** Contar `' ' + 1` **falha** para espaços consecutivos, espaços no início/fim ou string vazia. Use uma flag `int em_palavra = 0;`:
   - Se `s[i] != ' '` e `!em_palavra`: é o início de uma nova palavra (`palavras++; em_palavra = 1;`).
   - Se `s[i] == ' '`: marque `em_palavra = 0;`.
3. **Aritmética ASCII e Intervalos Contíguos:** Na tabela ASCII, `'0'..'9'` (`48..57`), `'A'..'Z'` (`65..90`) e `'a'..'z'` (`97..122`) são contíguos:
   - Minúscula para maiúscula: `c - 'a' + 'A'` (quando `c >= 'a' && c <= 'z'`).
   - Maiúscula para minúscula: `c - 'A' + 'a'` (quando `c >= 'A' && c <= 'Z'`).
4. **Cifra de César Circular (`% 26`):** Normalize o deslocamento `shift = ((k % 26) + 26) % 26;` para suportar qualquer inteiro `k` (inclusive negativos ou `>= 26`). Para letras com `base` `'A'` ou `'a'`:
   `nova = (char)(base + (c - base + shift) % 26);`
   Preserve espaços, dígitos e pontuação inalterados.
5. **Biblioteca `<ctype.h>`:** Funções como `isalpha`, `isdigit`, `isupper`, `islower`, `toupper` e `tolower` simplificam testes e conversões. Passe sempre `(unsigned char)s[i]` como argumento para evitar comportamento indefinido.
6. **Construção de nova string (`dest`) com índice independente `j`:** Ao filtrar caracteres (como remover dígitos ou espaços extras), mantenha `int j = 0;` separado de `i`, grave apenas em `dest[j++]` e **finalize obrigatoriamente com `dest[j] = '\0';`** após o laço!

---

## 2. Exemplos Guiados

### Exemplo 1 — Cifra de César (`k = 3`) e preservação de não-letras *(Rastreamento)*
Aplicando `shift = 3` em `"Luz 9!"`:
- `'L'` (`'A' + 11`): `'A' + (11 + 3) % 26 = 'O'`
- `'u'` (`'a' + 20`): `'a' + (20 + 3) % 26 = 'x'`
- `'z'` (`'a' + 25`): `'a' + (25 + 3) % 26 = 'a' + 2 = 'c'` *(volta circularmente para o início do alfabeto!)*
- `' '`, `'9'`, `'!'`: não são letras → permanecem `' '`, `'9'`, `'!'`.
- **Resultado:** `"Oxc 9!"`.

### Exemplo 2 — Remoção de espaços extras com `j` independente *(Programa completo)*
```c
#include <stdio.h>
#define MAX 101

int main(void) {
    char orig[MAX];
    char norm[MAX];

    fgets(orig, MAX, stdin);
    for (int i = 0; orig[i] != '\0'; i++) {
        if (orig[i] == '\n') {
            orig[i] = '\0';
            break;
        }
    }

    int j = 0;
    int em_palavra = 0;
    for (int i = 0; orig[i] != '\0'; i++) {
        if (orig[i] != ' ') {
            if (j > 0 && !em_palavra) {
                norm[j++] = ' ';
            }
            norm[j++] = orig[i];
            em_palavra = 1;
        } else {
            em_palavra = 0;
        }
    }
    norm[j] = '\0';

    printf("[%s]\n", norm);
    return 0;
}
```

---

## 3. Exercícios (`D07-E01` a `D07-E06`)

### Sessão 1 (`D07-E01` a `D07-E03` — Rastreamento, Lacunas e Depuração)

### `D07-E01` *(Leitura e Teste de Mesa — César e Máquina de Estados)*
Sem usar computador:
1. Aplique manualmente a Cifra de César com deslocamento `k = 4` na string `"AxZ 7!"`, indicando o índice no alfabeto `(c - base)` antes e depois do `% 26` para cada letra.
2. Rastreie a contagem de palavras com `em_palavra` (iniciado em `0`) sobre a string `"  ola   C99  "`, listando o valor de `em_palavra` e `palavras` ao final de cada índice `i` (`0..12`).

---

### `D07-E02` *(Completar solução)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` do trecho abaixo que copia de `orig` para `dest` **apenas as letras**, convertendo-as para maiúsculas com `<ctype.h>`, e fecha `dest` corretamente:

```c
#include <ctype.h>

/* Considere char orig[MAX] ja lida sem '\n' e char dest[MAX] */
int j = 0;
for (int i = 0; orig[i] != '\0'; i++) {
    if ( /* A */ ((unsigned char)orig[i])) {
        dest[ /* B */ ] = (char) /* C */ ((unsigned char)orig[i]);
        j++;
    }
}
dest[j] = /* D */;
```

---

### `D07-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler uma linha (`MAX 101`), contar o número de **palavras** (separadas por um ou mais espaços `' '`) e gerar uma nova string `dest` contendo **todos os caracteres exceto dígitos (`'0'..'9'`)**, imprimindo `Palavras: X\nLimpa: [Y]\n`. Identifique os **3 bugs intencionais** e escreva a versão corrigida completa:

```c
#include <stdio.h>
#define MAX 101

int main(void) {
    char orig[MAX];
    char dest[MAX];

    fgets(orig, MAX, stdin);
    for (int i = 0; orig[i] != '\0'; i++) {
        if (orig[i] == '\n') {
            orig[i] = '\0';
            break;
        }
    }

    int palavras = 1;
    for (int i = 0; orig[i] != '\0'; i++) {
        if (orig[i] == ' ') {
            palavras++;
        }
        if (!(orig[i] >= '0' && orig[i] <= '9')) {
            dest[i] = orig[i];
        }
    }

    printf("Palavras: %d\nLimpa: [%s]\n", palavras, dest);
    return 0;
}
```

---

### Sessão 2 (`D07-E04` a `D07-E06` — Escrita Guiada → Independente)

### `D07-E04` *(Variação controlada com pistas)*
Escreva um **programa completo** em C que leia uma linha de texto (`MAX 101`) com `fgets`, remova o `'\n'` e, em percurso manual até `'\0'`, calcule e imprima exatamente:
```text
Comprimento: X
Vogais: Y
Digitos: Z
Palavras: W
```
onde `Vogais` conta `'a','e','i','o','u'` (maiúsculas ou minúsculas) e `Palavras` trata corretamente múltiplos espaços consecutivos e strings vazias ou só com espaços (`Palavras: 0`).  
*Pista:* Use `tolower((unsigned char)s[i])` e `isdigit((unsigned char)s[i])` de `<ctype.h>`, além da flag `em_palavra`.

---

### `D07-E05` *(Variação controlada com pistas)*
Escreva um **programa completo** em C que leia uma linha (`MAX 101`) com `fgets`, remova o `'\n'` e gere em um segundo vetor `norm[MAX]` a frase normalizada: sem espaços no início, sem espaços no final e com qualquer sequência de múltiplos espaços internos reduzida a **um único espaço `' '`**. Imprima exatamente `[<norm>]\n`.  
*Pista:* Grave `' '` antes da próxima palavra apenas quando `j > 0 && !em_palavra`. Não esqueça `norm[j] = '\0';`.

---

### `D07-E06` *(Resolução independente)*
Escreva um **programa completo** em C que leia um inteiro `k` (deslocamento da Cifra de César, podendo ser positivo, zero, negativo ou maior que 26) e, na linha seguinte, uma mensagem (`MAX 101`) via `fgets`. Remova o `'\n'`, aplique a Cifra de César mantendo maiúsculas como maiúsculas, minúsculas como minúsculas e preservando dígitos, espaços e pontuação. Imprima exatamente:
```text
Cifrada: <mensagem>
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `D07-C01` *(Teste de Mesa)*
Rastreie o algoritmo do Exemplo 2 (normalização de espaços com `j` e `em_palavra`) sobre a string `orig = "  a  bc "`:
1. Preencha os valores gravados em `norm[0]`, `norm[1]`, `norm[2]`, `norm[3]` e em qual índice é gravado `'\0'`.
2. Explique por que não foi gravado espaço antes de `'a'` nem ao final após `'c'`.

---

### `D07-C02` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler uma linha (`MAX 101`), converter **todas as letras minúsculas em maiúsculas** via aritmética ASCII, contar palavras e caracteres não-espaço e imprimir `Maiuscula: <str>\nMedia palavra: <M.MM>\n` (imprimindo `0.00` se não houver palavras). Corrija os **3 defeitos** presentes:

```c
#include <stdio.h>
#define MAX 101

int main(void) {
    char s[MAX];

    fgets(s, MAX, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n') {
            s[i] = '\0';
            break;
        }
    }

    int palavras = 0, letras_uteis = 0, em_palavra = 0;
    for (int i = 0; i < MAX; i++) {
        if (s[i] != ' ') {
            letras_uteis++;
            if (!em_palavra) {
                palavras++;
                em_palavra = 1;
            }
        } else {
            em_palavra = 0;
        }
        if (s[i] >= 'a' && s[i] <= 'z') {
            s[i] = s[i] - 'A' + 'a';
        }
    }

    double media = letras_uteis / palavras;
    printf("Maiuscula: %s\nMedia palavra: %.2f\n", s, media);
    return 0;
}
```

---

### `D07-C03` *(Programa completo independente)*
Escreva um programa completo em C que leia uma linha (`MAX 101`) com `fgets`, remova o `'\n'` e construa uma nova string `limpa[MAX]` contendo apenas letras e dígitos (`isalpha` ou `isdigit`), convertendo todas as letras para minúsculas. Contabilize quantos caracteres foram descartados (`removidos`) e imprima exatamente:
```text
Limpa: [<limpa>]
Removidos: <removidos>
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `D08` (`Biblioteca <string.h> e Algoritmos Clássicos de Strings`):** somente após autocorreção de `D07-E01..E06` e **100% (3/3)** em `D07-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** refazer rastreamento da máquina de estados `em_palavra` e da aritmética modular `% 26` em papel, reforçando o uso de índice `j` independente + `dest[j] = '\0'`; aplicar variante `V2` de `D07`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`D06`** (terminador `'\0'`, remoção de `'\n'` e buffer após `scanf`), **`B01`** (operador `%`) e **`B06`** (condições lógicas de intervalo).

---

## 6. Referências do Orientador
- `[DOC]` `Aula_13_Algoritmos.pdf` p. 16–18, 24 (percurso até `'\0'`, contagem, tabela ASCII).
- `[DOC]` `Lista7_Algoritmos.pdf` p. 1–3 (Ex. 1, 2, 3, 5 — remoção de espaços extras, contagem de palavras, Cifra de César).
- Casos de teste e soluções verificáveis: [D07_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/gabaritos/D07_gabarito.md) e [D07_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/D07_testes.md).
