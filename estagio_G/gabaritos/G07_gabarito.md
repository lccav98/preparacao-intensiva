# Gabarito Comentado — Bloco `G07` (Recursão em Strings com Dois Índices e Modificação *In-Place*)

> **Bloco de referência:** [G07_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/blocos/G07_bloco.md)  
> **Nota para Caça ao Bug:** `G07-E03` no bloco do aluno contém **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`G07-E01` a `G07-E06`)

### `G07-E01` *(Teste de Mesa — Par vs. Ímpar e Adjacentes)*
- **(a)**
  - `"ARARA"` (`len = 5`): `(0, 4)` `'A'=='A'` → `(1, 3)` `'R'=='R'` → `(2, 2)` (`i >= j` → retorna `1`).
  - `"ABBA"` (`len = 4`): `(0, 3)` `'A'=='A'` → `(1, 2)` `'B'=='B'` → `(2, 1)` (`i >= j` → retorna `1`).
  - Se o caso base fosse `if (i == j)`, em `"ABBA"` `i` e `j` saltam de `(1, 2)` direto para `(2, 1)` (`i > j`), nunca satisfazendo `i == j` e avançando indefinidamente para fora dos limites da string até ocorrer *stack overflow*.
- **(b)** `remover_caractere("BANANA", 0, 0, 'A')`:
  - `(i=0, j=0, 'B'!='A')`: `s[0]='B'` → chama `(1, 1)`
  - `(i=1, j=1, 'A'=='A')`: pula → chama `(2, 1)`
  - `(i=2, j=1, 'N'!='A')`: `s[1]='N'` → chama `(3, 2)`
  - `(i=3, j=2, 'A'=='A')`: pula → chama `(4, 2)`
  - `(i=4, j=2, 'N'!='A')`: `s[2]='N'` → chama `(5, 3)`
  - `(i=5, j=3, 'A'=='A')`: pula → chama `(6, 3)`
  - `(i=6, j=3, '\0')`: `s[3] = '\0'` e retorna. String final: **`"BNN"`**.
- **(c)** Na remoção por deslocamento, após apagar o `'A'` da posição `0`, os caracteres restantes deslocam para a esquerda (`"AA\0"`), colocando o segundo `'A'` no índice `0`. Chamando `i + 1` (`1`), o `'A'` recém-movido para o índice `0` é pulado! Ao final, sobra **`"A"`** em vez de `""`.

### `G07-E02` *(Completar solução — `inverter`)*
- **`/* A */`:** `i >= j`
- **`/* B */`:**
  ```c
  char aux = s[i];
  s[i] = s[j];
  s[j] = aux;
  ```
- **`/* C */`:** `i + 1, j - 1`
- **`/* D */`:** `len - 1`

### `G07-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. Em `eh_palindromo`, o caso base `if (i == j)` falha para strings de comprimento par (pula de `i < j` para `i > j`) e para string vazia (`i = 0, j = -1`). Deve ser `if (i >= j)`.
  2. Em `inverter`, a chamada `inverter(s, i + 1, j);` não decrementa `j`, distorcendo a inversão. Deve ser `inverter(s, i + 1, j - 1);`.
  3. Em `main`, `inverter(s, 0, len);` inclui o índice `len` (onde está `'\0'`), colocando `'\0'` em `s[0]` e esvaziando a string. Deve ser `inverter(s, 0, len - 1);`.
- **Solução corrigida completa:** [G07_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G07_E03_corrigido.c)
```c
#include <stdio.h>

int comprimento(const char s[], int i);
int eh_palindromo(const char s[], int i, int j);
void inverter(char s[], int i, int j);

int main(void) {
    char s[100];
    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }

    int len = comprimento(s, 0);
    if (eh_palindromo(s, 0, len - 1)) {
        printf("Palindromo: Sim\n");
    } else {
        printf("Palindromo: Nao\n");
    }

    // Erro original 3: passava len em vez de len - 1, trocando '\0' com s[0].
    // Correcao: passar o indice do ultimo caractere valido (len - 1).
    inverter(s, 0, len - 1);
    printf("Invertida: %s\n", s);
    return 0;
}

int comprimento(const char s[], int i) {
    if (s[i] == '\0') {
        return 0;
    }
    return 1 + comprimento(s, i + 1);
}

int eh_palindromo(const char s[], int i, int j) {
    // Erro original 1: usava i == j, falhando em strings de tamanho par ou vazias.
    // Correcao: usar i >= j para cobrir tamanhos pares, impares e string vazia.
    if (i >= j) {
        return 1;
    }
    if (s[i] != s[j]) {
        return 0;
    }
    return eh_palindromo(s, i + 1, j - 1);
}

void inverter(char s[], int i, int j) {
    if (i >= j) {
        return;
    }
    char aux = s[i];
    s[i] = s[j];
    s[j] = aux;
    // Erro original 2: mantinha j fixo na chamada recursiva em vez de j - 1.
    // Correcao: convergir ambos os indices com i + 1 e j - 1.
    inverter(s, i + 1, j - 1);
}
```

### `G07-E04` *(Programa completo — Palíndromo recursivo)*
Arquivo: [G07_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G07_E04.c)
```c
#include <stdio.h>

int comprimento(const char s[], int i);
int eh_palindromo(const char s[], int i, int j);

int main(void) {
    char s[100];
    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }

    int len = comprimento(s, 0);
    if (eh_palindromo(s, 0, len - 1)) {
        printf("Palindromo: Sim\n");
    } else {
        printf("Palindromo: Nao\n");
    }
    return 0;
}

int comprimento(const char s[], int i) {
    if (s[i] == '\0') {
        return 0;
    }
    return 1 + comprimento(s, i + 1);
}

int eh_palindromo(const char s[], int i, int j) {
    if (i >= j) {
        return 1;
    }
    if (s[i] != s[j]) {
        return 0;
    }
    return eh_palindromo(s, i + 1, j - 1);
}
```

### `G07-E05` *(Programa completo — Inversão *in-place*)*
Arquivo: [G07_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G07_E05.c)
```c
#include <stdio.h>

int comprimento(const char s[], int i);
void inverter(char s[], int i, int j);

int main(void) {
    char s[100];
    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }

    int len = comprimento(s, 0);
    inverter(s, 0, len - 1);
    printf("Invertida: %s\n", s);
    return 0;
}

int comprimento(const char s[], int i) {
    if (s[i] == '\0') {
        return 0;
    }
    return 1 + comprimento(s, i + 1);
}

void inverter(char s[], int i, int j) {
    if (i >= j) {
        return;
    }
    char aux = s[i];
    s[i] = s[j];
    s[j] = aux;
    inverter(s, i + 1, j - 1);
}
```

### `G07-E06` *(Programa completo — Remoção *in-place* sem laço e sem auxiliar)*
Arquivo: [G07_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G07_E06.c)
```c
#include <stdio.h>

void remover_caractere(char s[], int i, int j, char c);

int main(void) {
    char s[100], c;
    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }
    scanf(" %c", &c);

    remover_caractere(s, 0, 0, c);
    printf("Resultado: %s\n", s);
    return 0;
}

void remover_caractere(char s[], int i, int j, char c) {
    if (s[i] == '\0') {
        s[j] = '\0';
        return;
    }
    if (s[i] != c) {
        s[j] = s[i];
        remover_caractere(s, i + 1, j + 1, c);
    } else {
        remover_caractere(s, i + 1, j, c);
    }
}
```

---

## 2. Gabarito da Checagem Independente (`G07-C01` a `G07-C03`)

### `G07-C01` *(Teste de Mesa e Borda)*
1. Rastreamento de `remover_caractere("AABAA", 0, 0, 'A')`:
   - `(0, 0, 'A')` → descarta, chama `(1, 0)`
   - `(1, 0, 'A')` → descarta, chama `(2, 0)`
   - `(2, 0, 'B')` → `s[0] = 'B'`, chama `(3, 1)`
   - `(3, 1, 'A')` → descarta, chama `(4, 1)`
   - `(4, 1, 'A')` → descarta, chama `(5, 1)`
   - `(5, 1, '\0')` → grava `s[1] = '\0'` e retorna. String final: **`"B"`**.
2. Em `"CASA"` (`len = 4`, índices `0..3`), as chamadas vão de `(0, 3)` → `(1, 2)` → `(2, 1)`. Como `i` nunca é igual a `j`, `if (i == j)` jamais é satisfeito; a função continua trocando fora dos limites (`s[2]` com `s[1]`, `s[3]` com `s[0]`, depois `s[4]` (`'\0'`) com `s[-1]` etc.) até estourar a pilha (*stack overflow*).

### `G07-C02` *(Programa completo — Palíndromo e Inversão)*
Arquivo: [G07_C02.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G07_C02.c)
```c
#include <stdio.h>

int comprimento(const char s[], int i);
int eh_palindromo(const char s[], int i, int j);
void inverter(char s[], int i, int j);

int main(void) {
    char s[100];
    scanf("%99s", s);

    int len = comprimento(s, 0);
    if (eh_palindromo(s, 0, len - 1)) {
        printf("Palindromo: Sim\n");
    } else {
        printf("Palindromo: Nao\n");
    }
    inverter(s, 0, len - 1);
    printf("Invertida: %s\n", s);
    return 0;
}

int comprimento(const char s[], int i) {
    if (s[i] == '\0') {
        return 0;
    }
    return 1 + comprimento(s, i + 1);
}

int eh_palindromo(const char s[], int i, int j) {
    if (i >= j) {
        return 1;
    }
    if (s[i] != s[j]) {
        return 0;
    }
    return eh_palindromo(s, i + 1, j - 1);
}

void inverter(char s[], int i, int j) {
    if (i >= j) {
        return;
    }
    char aux = s[i];
    s[i] = s[j];
    s[j] = aux;
    inverter(s, i + 1, j - 1);
}
```

### `G07-C03` *(Programa completo — Remoção de espaços *in-place*)*
Arquivo: [G07_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G07_C03.c)
```c
#include <stdio.h>

void remover_espacos(char s[], int i, int j);
int comprimento(const char s[], int i);

int main(void) {
    char s[100];
    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }

    remover_espacos(s, 0, 0);
    printf("Sem espacos: %s\n", s);
    printf("Comprimento: %d\n", comprimento(s, 0));
    return 0;
}

void remover_espacos(char s[], int i, int j) {
    if (s[i] == '\0') {
        s[j] = '\0';
        return;
    }
    if (s[i] != ' ') {
        s[j] = s[i];
        remover_espacos(s, i + 1, j + 1);
    } else {
        remover_espacos(s, i + 1, j);
    }
}

int comprimento(const char s[], int i) {
    if (s[i] == '\0') {
        return 0;
    }
    return 1 + comprimento(s, i + 1);
}
```
