# Gabarito Comentado — Bloco `E03` (Fatiamento e Acumuladores por Linha e por Coluna)

> **Bloco de referência:** [E03_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/blocos/E03_bloco.md)  
> **Nota para Caça ao Bug:** `E03-E03` e `E03-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`E03-E01` a `E03-E05`)

### `E03-E01` *(Teste de Mesa — Acumulador não zerado e Fatiamento Ordinal)*
1. Sem zerar `soma` antes de cada linha, o valor acumulado das linhas anteriores permanece:
   - `i = 0`: `0 + 1 + 2 + 3 = 6`
   - `i = 1`: `6 + 4 + 5 + 6 = 21`
   - `i = 2`: `21 + 7 + 8 + 9 = 45`
   Serão impressos **`6 21 45`**.
2. - `(a)` **3ª linha** (ordinal → índice `2`): `m[2][j]` com `j = 0..2` → valores **`7, 8, 9`**.
   - `(b)` **1ª coluna** (ordinal → índice `0`): `m[i][0]` com `i = 0..2` → valores **`1, 4, 7`**.

### `E03-E02` *(Completar solução)*
- **`/* A */`:** `int j = 0; j < C; j++`
- **`/* B */`:** `int soma = 0;`
- **`/* C */`:** `int i = 0; i < L; i++`
- **`/* D */`:** `m[i][j]`

### `E03-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `int soma = 0;` está fora do `for (int i = 0; i < L; i++)`, não sendo reinicializado a cada linha. Correto: declarar/zerar `int soma = 0;` dentro do laço externo `i`.
  2. No cálculo das colunas, os limites dos laços estão trocados (`j < L` e `i < C`), ignorando a 4ª coluna (`j = 3`) e acessando linha `i = 3` fora dos limites de `m[3][4]`. Correto: `j < C` no externo e `i < L` no interno.
  3. `soma_col += m[j][i];` inverte linha e coluna na indexação. Correto: `soma_col += m[i][j];`.
- **Solução corrigida completa:** [E03_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E03_E03_corrigido.c)
```c
#include <stdio.h>
#define L 3
#define C 4

int main(void) {
    int m[L][C];
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    printf("Linhas:");
    for (int i = 0; i < L; i++) {
        int soma = 0;
        for (int j = 0; j < C; j++) {
            soma += m[i][j];
        }
        printf(" %d", soma);
    }
    printf("\n");

    printf("Colunas:");
    for (int j = 0; j < C; j++) {
        int soma_col = 0;
        for (int i = 0; i < L; i++) {
            soma_col += m[i][j];
        }
        printf(" %d", soma_col);
    }
    printf("\n");

    return 0;
}
```

### `E03-E04` *(Programa completo — Fatiamento ordinal de linha e coluna)*
Arquivo: [E03_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E03_E04.c)
```c
#include <stdio.h>
#define L 3
#define C 4

int main(void) {
    int m[L][C];
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    int lin, col;
    scanf("%d %d", &lin, &col);
    int idx_l = lin - 1;
    int idx_c = col - 1;

    int soma_l = 0;
    printf("Linha %d:", lin);
    for (int j = 0; j < C; j++) {
        printf(" %d", m[idx_l][j]);
        soma_l += m[idx_l][j];
    }
    printf("\nSoma linha: %d\n", soma_l);

    int soma_c = 0;
    printf("Coluna %d:", col);
    for (int i = 0; i < L; i++) {
        printf(" %d", m[i][idx_c]);
        soma_c += m[i][idx_c];
    }
    printf("\nSoma coluna: %d\n", soma_c);

    return 0;
}
```

### `E03-E05` *(Programa completo — Somas de linhas, colunas e maior linha em `4 x 4`)*
Arquivo: [E03_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E03_E05.c)
```c
#include <stdio.h>
#define N 4

int main(void) {
    int m[N][N];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    int maior_soma = 0;
    int idx_maior = 0;

    printf("Linhas:");
    for (int i = 0; i < N; i++) {
        int soma = 0;
        for (int j = 0; j < N; j++) {
            soma += m[i][j];
        }
        printf(" %d", soma);
        if (i == 0 || soma > maior_soma) {
            maior_soma = soma;
            idx_maior = i;
        }
    }
    printf("\n");

    printf("Colunas:");
    for (int j = 0; j < N; j++) {
        int soma = 0;
        for (int i = 0; i < N; i++) {
            soma += m[i][j];
        }
        printf(" %d", soma);
    }
    printf("\n");

    printf("Maior linha: %d (%d)\n", idx_maior, maior_soma);

    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`E03-C01` a `E03-C03`)

### `E03-C01` *(Análise de Erro de Acumulador e Fatiamento)*
1. - **Com `soma` sem zerar:** coluna 0 dá `5 + 3 = 8`; coluna 1 acumula `8 + (-2) + 1 = 7`; coluna 2 acumula `7 + 4 + (-4) = 7`. Saída errada: **`8 7 7`**.
   - **Valores corretos:** coluna 0 = **`8`**, coluna 1 = **`-1`**, coluna 2 = **`0`**.
2. - **1ª linha** (ordinal → índice `0`): `m[0][j]` (`j = 0..2`) → **`5, -2, 4`**.
   - **3ª coluna** (ordinal → índice `2`): `m[i][2]` (`i = 0..1`) → **`4, -4`**.

### `E03-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `int soma = 0;` está fora do `for (int i = 0; i < L; i++)`, acumulando o total das linhas anteriores. Correto: declarar/zerar `int soma = 0;` dentro do laço externo `i`.
  2. Na exibição da coluna `k`, o laço vai até `C` (`5`) em vez de `L` (`3`), acessando linhas `3` e `4` fora dos limites de `m[3][5]`. Correto: `for (int i = 0; i < L; i++)`.
  3. `m[k][i]` acessa a **linha `k`** em vez da **coluna `k`** (além de estourar a linha quando `k >= 3`). Correto: `m[i][k]`.
- **Solução corrigida completa:** [E03_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E03_C02_corrigido.c)
```c
#include <stdio.h>
#define L 3
#define C 5

int main(void) {
    int m[L][C];
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    int k;
    scanf("%d", &k);

    printf("Linhas:");
    for (int i = 0; i < L; i++) {
        int soma = 0;
        for (int j = 0; j < C; j++) {
            soma += m[i][j];
        }
        printf(" %d", soma);
    }
    printf("\n");

    printf("Coluna %d:", k);
    for (int i = 0; i < L; i++) {
        printf(" %d", m[i][k]);
    }
    printf("\n");

    return 0;
}
```

### `E03-C03` *(Programa completo — Somas por linha e por coluna em `l x c`)*
Arquivo: [E03_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E03_C03.c)
```c
#include <stdio.h>
#define MAX 10

int main(void) {
    int l, c;
    int m[MAX][MAX];
    scanf("%d %d", &l, &c);

    for (int i = 0; i < l; i++) {
        for (int j = 0; j < c; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    printf("Linhas:");
    for (int i = 0; i < l; i++) {
        int soma = 0;
        for (int j = 0; j < c; j++) {
            soma += m[i][j];
        }
        printf(" %d", soma);
    }
    printf("\n");

    printf("Colunas:");
    for (int j = 0; j < c; j++) {
        int soma = 0;
        for (int i = 0; i < l; i++) {
            soma += m[i][j];
        }
        printf(" %d", soma);
    }
    printf("\n");

    return 0;
}
```
