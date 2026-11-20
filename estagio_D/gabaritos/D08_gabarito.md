# Gabarito Comentado — Bloco `D08` (Biblioteca `<string.h>` e Algoritmos Clássicos)

> **Bloco de referência:** [D08_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/blocos/D08_bloco.md)  
> **Nota para Caça ao Bug:** `D08-E03` e `D08-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`D08-E01` a `D08-E05`)

### `D08-E01` *(Leitura e Teste de Mesa)*
1. **Retornos de `strcmp`:**
   - `strcmp("Bola", "bola")`: **`< 0`** (`'B'` = `66` < `'b'` = `98`).
   - `strcmp("casa", "casaco")`: **`< 0`** (no índice `4`, `'\0'` = `0` < `'c'` = `99`).
   - `strcmp("abc", "abc")`: **`== 0`**.
2. **Rastreamento de palíndromo *in-place*:**
   - `"Radar"` (`len = 5`): `(i=0, j=4)` `'r' == 'r'` → `(i=1, j=3)` `'a' == 'a'` → `i=2, j=2` (sai do `while`). **`eh_pal = 1`**.
   - `"cama"` (`len = 4`): `(i=0, j=3)` `'c' == 'a'` é falso → `eh_pal = 0; break;`. **`eh_pal = 0`**.

---

### `D08-E02` *(Completar solução)*
- **`/* A */`:** `strlen`
- **`/* B */`:** `'.'`
- **`/* C */`:** `-1`
- **`/* D */`:** `strcpy`

---

### `D08-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `if (a == b)` compara endereços dos vetores em memória (sempre falso), em vez do conteúdo. Correto: `if (strcmp(a, b) == 0)`.
  2. `strcat(res, a);` lê lixo de `res` não inicializado à procura de um `'\0'` inicial. Correto: iniciar com `strcpy(res, a);`.
  3. O laço de inversão não grava `inv[len] = '\0';` após terminar, causando leitura de lixo em `printf("%s", inv)`.
- **Solução corrigida completa:** [D08_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D08_E03_corrigido.c)
```c
#include <stdio.h>
#include <string.h>
#define MAX 31
#define MAX_RES 65

int main(void) {
    char a[MAX], b[MAX];
    char res[MAX_RES], inv[MAX_RES];

    scanf("%30s %30s", a, b);

    if (strcmp(a, b) == 0) {
        printf("Iguais: Sim\n");
    } else {
        printf("Iguais: Nao\n");
    }

    strcpy(res, a);
    strcat(res, "-");
    strcat(res, b);

    int len = (int)strlen(res);
    for (int i = 0; i < len; i++) {
        inv[i] = res[len - 1 - i];
    }
    inv[len] = '\0';

    printf("Uniao: %s\nInvertida: %s\n", res, inv);
    return 0;
}
```

---

### `D08-E04` *(Programa completo — Inversão manual para nova string)*
Arquivo: [D08_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D08_E04.c)
```c
#include <stdio.h>
#include <string.h>
#define MAX 81

int main(void) {
    char orig[MAX];
    char inv[MAX];

    fgets(orig, MAX, stdin);
    int len = (int)strlen(orig);
    if (len > 0 && orig[len - 1] == '\n') {
        orig[len - 1] = '\0';
        len--;
    }

    for (int i = 0; i < len; i++) {
        inv[i] = orig[len - 1 - i];
    }
    inv[len] = '\0';

    printf("Original: %s\nInvertida: %s\n", orig, inv);
    if (strcmp(orig, inv) == 0) {
        printf("Identicas: Sim\n");
    } else {
        printf("Identicas: Nao\n");
    }
    return 0;
}
```

---

### `D08-E05` *(Programa completo — Palíndromo in-place ignorando espaços e caixa)*
Arquivo: [D08_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D08_E05.c)
```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define MAX 101

int main(void) {
    char s[MAX];

    fgets(s, MAX, stdin);
    int len = (int)strlen(s);
    if (len > 0 && s[len - 1] == '\n') {
        s[len - 1] = '\0';
        len--;
    }

    int i = 0;
    int j = len - 1;
    int eh_pal = 1;

    while (i < j) {
        while (i < j && s[i] == ' ') {
            i++;
        }
        while (i < j && s[j] == ' ') {
            j--;
        }
        if (tolower((unsigned char)s[i]) != tolower((unsigned char)s[j])) {
            eh_pal = 0;
            break;
        }
        i++;
        j--;
    }

    if (eh_pal) {
        printf("Palindromo\n");
    } else {
        printf("Nao palindromo\n");
    }
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`D08-C01` a `D08-C03`)

### `D08-C01` *(Teste de Mesa e Análise)*
1. `x == y` resulta em **`0` (falso)**, pois compara os endereços distintos de `x` e `y` na memória, não os caracteres armazenados.
2. `strcmp("Zebra", "abacaxi")` retorna **`< 0` (negativo)**, porque `'Z'` (`90`) é menor que `'a'` (`97`) na tabela ASCII.
3. **Rastreamento:**
   - `"Omo"` (`len = 3`): `(i=0, j=2)` `'o' == 'o'` → `i=1, j=1` (encerra `while`). **`eh_pal = 1`**.
   - `"abca"` (`len = 4`): `(i=0, j=3)` `'a' == 'a'` → `(i=1, j=2)` `'b' == 'c'` é falso → `eh_pal = 0; break;`. **`eh_pal = 0`**.

---

### `D08-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `if (s1 > s2)` compara endereços de memória em vez de conteúdo lexicográfico. Correto: `if (strcmp(s1, s2) > 0)`.
  2. `aux = s1; s1 = s2; s2 = aux;` é inválido em C (vetores não são atribuíveis com `=`). Correto: `strcpy(aux, s1); strcpy(s1, s2); strcpy(s2, aux);`.
  3. `if (s1[i] != s1[j])` não normaliza a caixa, falhando para palíndromos como `"Arara"`. Correto: `tolower((unsigned char)s1[i]) != tolower((unsigned char)s1[j])`.
- **Solução corrigida completa:** [D08_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D08_C02_corrigido.c)
```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define MAX 41

int main(void) {
    char s1[MAX], s2[MAX], aux[MAX];

    scanf("%40s %40s", s1, s2);

    if (strcmp(s1, s2) > 0) {
        strcpy(aux, s1);
        strcpy(s1, s2);
        strcpy(s2, aux);
    }

    int len = (int)strlen(s1);
    int i = 0, j = len - 1, eh_pal = 1;
    while (i < j) {
        if (tolower((unsigned char)s1[i]) != tolower((unsigned char)s1[j])) {
            eh_pal = 0;
            break;
        }
        i++;
        j--;
    }

    printf("Ordem: %s <= %s\nPalindromo menor: %s\n",
           s1, s2, eh_pal ? "Sim" : "Nao");
    return 0;
}
```

---

### `D08-C03` *(Programa completo — Menor, maior e contagem de palíndromos)*
Arquivo: [D08_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D08_C03.c)
```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define MAX_PAL 31

int main(void) {
    int n;
    char atual[MAX_PAL];
    char menor[MAX_PAL], maior[MAX_PAL];
    int palindromos = 0;

    scanf("%d", &n);
    for (int k = 0; k < n; k++) {
        scanf("%30s", atual);
        if (k == 0) {
            strcpy(menor, atual);
            strcpy(maior, atual);
        } else {
            if (strcmp(atual, menor) < 0) {
                strcpy(menor, atual);
            }
            if (strcmp(atual, maior) > 0) {
                strcpy(maior, atual);
            }
        }

        int len = (int)strlen(atual);
        int i = 0, j = len - 1, eh_pal = 1;
        while (i < j) {
            if (tolower((unsigned char)atual[i]) != tolower((unsigned char)atual[j])) {
                eh_pal = 0;
                break;
            }
            i++;
            j--;
        }
        if (eh_pal) {
            palindromos++;
        }
    }

    printf("Menor: %s\nMaior: %s\nPalindromos: %d\n", menor, maior, palindromos);
    return 0;
}
```
