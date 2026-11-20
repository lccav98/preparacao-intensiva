# Gabarito Comentado — Bloco `D07` (Percurso Manual de Strings, ASCII e `<ctype.h>`)

> **Bloco de referência:** [D07_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/blocos/D07_bloco.md)  
> **Nota para Caça ao Bug:** `D07-E03` e `D07-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`D07-E01` a `D07-E06`)

### `D07-E01` *(Leitura e Teste de Mesa)*
1. **Cifra de César (`k = 4`) em `"AxZ 7!"`:**
   - `'A'`: índice `0` $\rightarrow$ `(0 + 4) % 26 = 4` $\rightarrow$ `'E'`
   - `'x'`: índice `23` $\rightarrow$ `(23 + 4) % 26 = 27 % 26 = 1` $\rightarrow$ `'b'`
   - `'Z'`: índice `25` $\rightarrow$ `(25 + 4) % 26 = 29 % 26 = 3` $\rightarrow$ `'D'`
   - `' '`, `'7'`, `'!'`: não são letras $\rightarrow$ permanecem inalterados.
   - **Saída:** `"EbD 7!"`.
2. **Contagem de palavras em `"  ola   C99  "` (`13` chars, índices `0..12`):**
   - `i=0 (' ')`, `i=1 (' ')`: `em_palavra = 0`, `palavras = 0`
   - `i=2 ('o')`: transição `0 -> 1`, `palavras = 1`, `em_palavra = 1`
   - `i=3 ('l')`, `i=4 ('a')`: mantém `em_palavra = 1`, `palavras = 1`
   - `i=5,6,7 (' ')`: `em_palavra = 0`, `palavras = 1`
   - `i=8 ('C')`: transição `0 -> 1`, `palavras = 2`, `em_palavra = 1`
   - `i=9 ('9')`, `i=10 ('9')`: mantém `em_palavra = 1`, `palavras = 2`
   - `i=11,12 (' ')`: `em_palavra = 0`, **`palavras = 2`**.

---

### `D07-E02` *(Completar solução)*
- **`/* A */`:** `isalpha`
- **`/* B */`:** `j`
- **`/* C */`:** `toupper`
- **`/* D */`:** `'\0'`

---

### `D07-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `int palavras = 1;` somando a cada `' '` falha em espaços consecutivos, espaços nas extremidades e string vazia. Correto: usar `em_palavra` com `palavras = 0`.
  2. `dest[i] = orig[i];` usa o índice de leitura `i` na escrita, deixando lixo não inicializado nas posições em que dígitos foram pulados. Correto: usar índice independente `j++`.
  3. Falta inserir `dest[j] = '\0';` após o laço, causando leitura de lixo pelo `printf("%s")`.
- **Solução corrigida completa:** [D07_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D07_E03_corrigido.c)
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

    int palavras = 0;
    int em_palavra = 0;
    int j = 0;

    for (int i = 0; orig[i] != '\0'; i++) {
        if (orig[i] != ' ') {
            if (!em_palavra) {
                palavras++;
                em_palavra = 1;
            }
        } else {
            em_palavra = 0;
        }

        if (!(orig[i] >= '0' && orig[i] <= '9')) {
            dest[j] = orig[i];
            j++;
        }
    }
    dest[j] = '\0';

    printf("Palavras: %d\nLimpa: [%s]\n", palavras, dest);
    return 0;
}
```

---

### `D07-E04` *(Programa completo — Comprimento, vogais, dígitos e palavras)*
Arquivo: [D07_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D07_E04.c)
```c
#include <stdio.h>
#include <ctype.h>
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

    int comp = 0, vogais = 0, digitos = 0, palavras = 0;
    int em_palavra = 0;

    for (int i = 0; s[i] != '\0'; i++) {
        char c = (char)tolower((unsigned char)s[i]);
        comp++;
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            vogais++;
        }
        if (isdigit((unsigned char)s[i])) {
            digitos++;
        }
        if (s[i] != ' ') {
            if (!em_palavra) {
                palavras++;
                em_palavra = 1;
            }
        } else {
            em_palavra = 0;
        }
    }

    printf("Comprimento: %d\nVogais: %d\nDigitos: %d\nPalavras: %d\n",
           comp, vogais, digitos, palavras);
    return 0;
}
```

---

### `D07-E05` *(Programa completo — Remoção de espaços extras)*
Arquivo: [D07_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D07_E05.c)
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

### `D07-E06` *(Programa completo — Cifra de César)*
Arquivo: [D07_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D07_E06.c)
```c
#include <stdio.h>
#define MAX 101

int main(void) {
    int k, ch;
    char s[MAX];

    scanf("%d", &k);
    while ((ch = getchar()) != '\n' && ch != EOF) {
    }

    fgets(s, MAX, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n') {
            s[i] = '\0';
            break;
        }
    }

    int shift = ((k % 26) + 26) % 26;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] >= 'A' && s[i] <= 'Z') {
            s[i] = (char)('A' + (s[i] - 'A' + shift) % 26);
        } else if (s[i] >= 'a' && s[i] <= 'z') {
            s[i] = (char)('a' + (s[i] - 'a' + shift) % 26);
        }
    }

    printf("Cifrada: %s\n", s);
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`D07-C01` a `D07-C03`)

### `D07-C01` *(Teste de Mesa)*
1. **Gravações em `norm`:**
   - `i=0,1 (' ')`: nada gravado (`j=0`, `em_palavra=0`).
   - `i=2 ('a')`: `j == 0`, grava `norm[0] = 'a'`, `j=1`, `em_palavra=1`.
   - `i=3,4 (' ')`: `em_palavra=0`.
   - `i=5 ('b')`: `j > 0 && !em_palavra`, grava `norm[1] = ' '`, depois `norm[2] = 'b'`, `j=3`, `em_palavra=1`.
   - `i=6 ('c')`: grava `norm[3] = 'c'`, `j=4`.
   - `i=7 (' ')`: `em_palavra=0`.
   - Após o laço: grava `norm[4] = '\0'`.
   - **Resultado:** `norm[0]='a'`, `norm[1]=' '`, `norm[2]='b'`, `norm[3]='c'`, `norm[4]='\0'`.
2. **Por que sem espaços nas pontas:** Antes de `'a'`, `j` vale `0` (impede espaço inicial). No final, o espaço em `i=7` apenas zera `em_palavra`, e nenhum novo caractere não-espaço aparece depois para disparar a gravação do separador `' '`.

---

### `D07-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `for (int i = 0; i < MAX; i++)` ignora o terminador `'\0'`, percorrendo lixo além do fim da string! Correto: `s[i] != '\0'`.
  2. `s[i] = s[i] - 'A' + 'a';` aplica a conversão na direção errada (gera códigos ASCII abaixo de `'a'`). Correto: `s[i] = (char)(s[i] - 'a' + 'A');`.
  3. `double media = letras_uteis / palavras;` faz divisão inteira e causa divisão por zero quando `palavras == 0`. Correto: `(palavras > 0) ? (double)letras_uteis / palavras : 0.0`.
- **Solução corrigida completa:** [D07_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D07_C02_corrigido.c)
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
    for (int i = 0; s[i] != '\0'; i++) {
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
            s[i] = (char)(s[i] - 'a' + 'A');
        }
    }

    double media = (palavras > 0) ? (double)letras_uteis / palavras : 0.0;
    printf("Maiuscula: %s\nMedia palavra: %.2f\n", s, media);
    return 0;
}
```

---

### `D07-C03` *(Programa completo — Filtro alfanumérico em minúsculas)*
Arquivo: [D07_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D07_C03.c)
```c
#include <stdio.h>
#include <ctype.h>
#define MAX 101

int main(void) {
    char orig[MAX];
    char limpa[MAX];

    fgets(orig, MAX, stdin);
    for (int i = 0; orig[i] != '\0'; i++) {
        if (orig[i] == '\n') {
            orig[i] = '\0';
            break;
        }
    }

    int j = 0, removidos = 0;
    for (int i = 0; orig[i] != '\0'; i++) {
        if (isalpha((unsigned char)orig[i]) || isdigit((unsigned char)orig[i])) {
            limpa[j++] = (char)tolower((unsigned char)orig[i]);
        } else {
            removidos++;
        }
    }
    limpa[j] = '\0';

    printf("Limpa: [%s]\nRemovidos: %d\n", limpa, removidos);
    return 0;
}
```
