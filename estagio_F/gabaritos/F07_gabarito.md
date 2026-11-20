# Gabarito Comentado — Bloco `F07` (Matrizes 2D, Strings *In-Place* e Composição)

> **Bloco de referência:** [F07_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/blocos/F07_bloco.md)  
> **Nota para Caça ao Bug:** `F07-E03` no bloco do aluno contém **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`F07-E01` a `F07-E06`)

### `F07-E01` *(Teste de Mesa e Composição)*
- **(a)** Saída exata:
  ```text
  L0: 6.00
  L1: 2.00
  ```
- **(b)** Cadeia de chamadas da 1ª linha: `main` chama `media_linha(mat, 0)` → `media_linha` chama `soma_linha(mat, 0)` → `soma_linha` soma `3 + 6 + 9 = 18` e retorna `18` → `media_linha` calcula `(double)18 / 3 = 6.0` e retorna `6.0` para `main`.  
  A dimensão das colunas (`COL = 3`) é obrigatória em `const int m[][COL]` porque a matriz é armazenada em sequência linha por linha (*row-major*): o compilador precisa saber quantos elementos formam uma linha (`COL`) para calcular o endereço de `m[linha][j]` usando `linha * COL + j`.

### `F07-E02` *(Completar solução)*
- **`/* A */`:** `char s[]`
- **`/* B */`:** `s[i] != '\0'`
- **`/* C */`:**
```c
            s[j] = s[i];
            j++;
```
- **`/* D */`:** `s[j] = '\0';`

### `F07-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `const int m[][]` omite a dimensão das colunas no protótipo e na definição de `somar_matriz`, impedindo a compilação. Deve ser `const int m[][COL]`.
  2. `remover_digitos` não grava `s[j] = '\0';` após o laço, mantendo o antigo terminador `'\0'` na posição original e deixando caracteres residuais no fim da string.
- **Solução corrigida completa:** [F07_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F07_E03_corrigido.c)
```c
#include <stdio.h>

#define COL 3

int somar_matriz(const int m[][COL], int linhas);
void remover_digitos(char s[]);

int main(void) {
    int linhas, m[10][COL];
    char texto[50];

    scanf("%d", &linhas);
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < COL; j++) {
            scanf("%d", &m[i][j]);
        }
    }
    scanf("%49s", texto);

    printf("Soma: %d\n", somar_matriz(m, linhas));
    remover_digitos(texto);
    printf("Texto: %s\n", texto);
    return 0;
}

// Erro original 1: omitia o numero de colunas (const int m[][]), o que impede o compilador de calcular o deslocamento das linhas.
// Correcao: informar obrigatoriamente a dimensao das colunas (const int m[][COL]).
int somar_matriz(const int m[][COL], int linhas) {
    int soma = 0;
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < COL; j++) {
            soma += m[i][j];
        }
    }
    return soma;
}

void remover_digitos(char s[]) {
    int j = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] < '0' || s[i] > '9') {
            s[j] = s[i];
            j++;
        }
    }
    // Erro original 2: nao inseria o terminador '\0' na nova posicao final j.
    // Correcao: encerrar explicitamente a string modificada com s[j] = '\0';.
    s[j] = '\0';
}
```

### `F07-E04` *(Programa completo — Simetria em matriz `3 x 3`)*
Arquivo: [F07_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F07_E04.c)
```c
#include <stdio.h>

#define N 3

int eh_simetrica(const int m[][N]);

int main(void) {
    int m[N][N];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &m[i][j]);
        }
    }
    if (eh_simetrica(m)) {
        printf("Simetrica: Sim\n");
    } else {
        printf("Simetrica: Nao\n");
    }
    return 0;
}

int eh_simetrica(const int m[][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            if (m[i][j] != m[j][i]) {
                return 0;
            }
        }
    }
    return 1;
}
```

### `F07-E05` *(Programa completo — Composição em matriz `m[][4]`)*
Arquivo: [F07_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F07_E05.c)
```c
#include <stdio.h>

#define COL 4

int soma_matriz(const int m[][COL], int linhas);
double media_matriz(const int m[][COL], int linhas);
int contar_acima_media(const int m[][COL], int linhas);

int main(void) {
    int linhas, m[10][COL];
    scanf("%d", &linhas);
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < COL; j++) {
            scanf("%d", &m[i][j]);
        }
    }
    printf("Soma: %d\n", soma_matriz(m, linhas));
    printf("Media: %.2f\n", media_matriz(m, linhas));
    printf("Acima da media: %d\n", contar_acima_media(m, linhas));
    return 0;
}

int soma_matriz(const int m[][COL], int linhas) {
    int soma = 0;
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < COL; j++) {
            soma += m[i][j];
        }
    }
    return soma;
}

double media_matriz(const int m[][COL], int linhas) {
    return (double)soma_matriz(m, linhas) / (linhas * COL);
}

int contar_acima_media(const int m[][COL], int linhas) {
    double med = media_matriz(m, linhas);
    int cont = 0;
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < COL; j++) {
            if (m[i][j] > med) {
                cont++;
            }
        }
    }
    return cont;
}
```

### `F07-E06` *(Programa completo — Remoção in-place de caractere)*
Arquivo: [F07_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F07_E06.c)
```c
#include <stdio.h>

void remover_caractere(char s[], char c);

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
    remover_caractere(s, c);
    printf("Resultado: %s\n", s);
    return 0;
}

void remover_caractere(char s[], char c) {
    int j = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] != c) {
            s[j] = s[i];
            j++;
        }
    }
    s[j] = '\0';
}
```

---

## 2. Gabarito da Checagem Independente (`F07-C01` a `F07-C03`)

### `F07-C01` *(Análise Conceitual e Rastreamento)*
1. A memória é linearizada por linhas (*row-major*). Para acessar `m[i][j]`, o compilador precisa calcular `i * COL + j`. Sem conhecer `COL`, o tipo do elemento linha fica incompleto (`int []`) e o programa não compila; com `m[][4]`, cada linha tem tamanho fixo `4 * sizeof(int)`.
2. Toda string válida em C possui o terminador `'\0'` marcando o final do conteúdo útil, permitindo parar o percurso em `s[i] != '\0'`. Já um vetor numérico `int v[]` não tem valor sentinela reservado, exigindo a passagem explícita de `n`.
3. `h(a, 4)` retorna **`5.0`**. Ordem de execução: `main` (ou chamador) inicia `h(a, 4)` → `h` chama `g(v, 4)` → `g` calcula `2+4+6+8 = 20` e termina retornando `20` → `h` divide `(double)20 / 4 = 5.0` e termina retornando `5.0`.

### `F07-C02` *(Programa completo — Diagonais e composição)*
Arquivo: [F07_C02.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F07_C02.c)
```c
#include <stdio.h>

#define N 3

int soma_diagonal_principal(const int m[][N]);
int soma_diagonal_secundaria(const int m[][N]);
void resumo_diagonais(const int m[][N], int *dp, int *ds);

int main(void) {
    int m[N][N], dp, ds;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &m[i][j]);
        }
    }
    resumo_diagonais(m, &dp, &ds);
    printf("Diagonal principal: %d\n", dp);
    printf("Diagonal secundaria: %d\n", ds);
    return 0;
}

int soma_diagonal_principal(const int m[][N]) {
    int soma = 0;
    for (int i = 0; i < N; i++) {
        soma += m[i][i];
    }
    return soma;
}

int soma_diagonal_secundaria(const int m[][N]) {
    int soma = 0;
    for (int i = 0; i < N; i++) {
        soma += m[i][N - 1 - i];
    }
    return soma;
}

void resumo_diagonais(const int m[][N], int *dp, int *ds) {
    *dp = soma_diagonal_principal(m);
    *ds = soma_diagonal_secundaria(m);
}
```

### `F07-C03` *(Programa completo — Remoção de vogais in-place e comprimento)*
Arquivo: [F07_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F07_C03.c)
```c
#include <stdio.h>

void remover_vogais(char s[]);
int tamanho_string(const char s[]);

int main(void) {
    char s[100];
    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }
    remover_vogais(s);
    printf("Sem vogais: %s\n", s);
    printf("Comprimento: %d\n", tamanho_string(s));
    return 0;
}

void remover_vogais(char s[]) {
    int j = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        char c = s[i];
        int vogal = (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
                     c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
        if (!vogal) {
            s[j] = s[i];
            j++;
        }
    }
    s[j] = '\0';
}

int tamanho_string(const char s[]) {
    int len = 0;
    while (s[len] != '\0') {
        len++;
    }
    return len;
}
```
