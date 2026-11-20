# Gabarito Comentado — Bloco `E06` (Multiplicação de Matrizes — Triplo Laço Aninhado `i, j, k`)

> **Bloco de referência:** [E06_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/blocos/E06_bloco.md)  
> **Nota para Caça ao Bug:** `E06-E03` e `E06-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`E06-E01` a `E06-E06`)

### `E06-E01` *(Teste de Mesa — Produto Não Quadrado)*
1. Como `A` é `2 x 3` e `B` é `3 x 2` (`CA = 3 == LB = 3`), a matriz resultante $C = A \cdot B$ possui dimensões **`2 x 2`**.
2. Cálculo de cada elemento:
   - `C[0][0] = 1*7 + 2*9 + 3*11 = 7 + 18 + 33 = 58`
   - `C[0][1] = 1*8 + 2*10 + 3*12 = 8 + 20 + 36 = 64`
   - `C[1][0] = 4*7 + 5*9 + 6*11 = 28 + 45 + 66 = 139`
   - `C[1][1] = 4*8 + 5*10 + 6*12 = 32 + 50 + 72 = 154`
3. Sim, $B \cdot A$ também é possível porque `CB = 2 == LA = 2`, gerando uma matriz de dimensões **`3 x 3`**.

### `E06-E02` *(Completar solução)*
- **`/* A */`:** `j < CB`
- **`/* B */`:** `C[i][j] = 0`
- **`/* C */`:** `k < CA` *(ou `k < LB`, já que `CA == LB`)*
- **`/* D */`:** `A[i][k] * B[k][j]`

### `E06-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `if (LA != LB)` testa a condição errada de compatibilidade: a exigência é colunas de `A` igual a linhas de `B` (`CA != LB`).
  2. Falta `C[i][j] = 0;` dentro do laço `j` antes do laço `k`, fazendo `C[i][j] += ...` acumular lixo de memória.
  3. `B[j][k]` inverte linha e coluna de `B` no produto interno. O correto é `B[k][j]` (linha `k`, coluna `j`).
- **Solução corrigida completa:** [E06_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E06_E03_corrigido.c)
```c
#include <stdio.h>
#define MAX 20

int main(void) {
    int LA, CA, LB, CB;
    int A[MAX][MAX], B[MAX][MAX], C[MAX][MAX];

    scanf("%d %d", &LA, &CA);
    for (int i = 0; i < LA; i++) {
        for (int j = 0; j < CA; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    scanf("%d %d", &LB, &CB);
    for (int i = 0; i < LB; i++) {
        for (int j = 0; j < CB; j++) {
            scanf("%d", &B[i][j]);
        }
    }

    if (CA != LB) {
        printf("Multiplicacao impossivel\n");
    } else {
        for (int i = 0; i < LA; i++) {
            for (int j = 0; j < CB; j++) {
                C[i][j] = 0;
                for (int k = 0; k < CA; k++) {
                    C[i][j] += A[i][k] * B[k][j];
                }
            }
        }
        printf("Produto (%d x %d):\n", LA, CB);
        for (int i = 0; i < LA; i++) {
            for (int j = 0; j < CB; j++) {
                if (j > 0) {
                    printf(" ");
                }
                printf("%d", C[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
```

### `E06-E04` *(Programa completo — Produto e maior elemento com coordenadas)*
Arquivo: [E06_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E06_E04.c)
```c
#include <stdio.h>
#define MAX 20

int main(void) {
    int LA, CA, LB, CB;
    int A[MAX][MAX], B[MAX][MAX], C[MAX][MAX];

    scanf("%d %d", &LA, &CA);
    for (int i = 0; i < LA; i++) {
        for (int j = 0; j < CA; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    scanf("%d %d", &LB, &CB);
    for (int i = 0; i < LB; i++) {
        for (int j = 0; j < CB; j++) {
            scanf("%d", &B[i][j]);
        }
    }

    for (int i = 0; i < LA; i++) {
        for (int j = 0; j < CB; j++) {
            C[i][j] = 0;
            for (int k = 0; k < CA; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    int maior = C[0][0], li = 0, co = 0;
    for (int i = 0; i < LA; i++) {
        for (int j = 0; j < CB; j++) {
            if (C[i][j] > maior) {
                maior = C[i][j];
                li = i;
                co = j;
            }
        }
    }

    printf("Produto (%d x %d):\n", LA, CB);
    for (int i = 0; i < LA; i++) {
        for (int j = 0; j < CB; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", C[i][j]);
        }
        printf("\n");
    }
    printf("Maior: %d em (%d, %d)\n", maior, li, co);
    return 0;
}
```

### `E06-E05` *(Programa completo — Produtos `A*B` e `B*A` independentes)*
Arquivo: [E06_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E06_E05.c)
```c
#include <stdio.h>
#define MAX 20

int main(void) {
    int LA, CA, LB, CB;
    int A[MAX][MAX], B[MAX][MAX], C[MAX][MAX], D[MAX][MAX];

    scanf("%d %d", &LA, &CA);
    for (int i = 0; i < LA; i++) {
        for (int j = 0; j < CA; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    scanf("%d %d", &LB, &CB);
    for (int i = 0; i < LB; i++) {
        for (int j = 0; j < CB; j++) {
            scanf("%d", &B[i][j]);
        }
    }

    if (CA != LB) {
        printf("Produto A*B impossivel\n");
    } else {
        for (int i = 0; i < LA; i++) {
            for (int j = 0; j < CB; j++) {
                C[i][j] = 0;
                for (int k = 0; k < CA; k++) {
                    C[i][j] += A[i][k] * B[k][j];
                }
            }
        }
        printf("A*B (%d x %d):\n", LA, CB);
        for (int i = 0; i < LA; i++) {
            for (int j = 0; j < CB; j++) {
                if (j > 0) {
                    printf(" ");
                }
                printf("%d", C[i][j]);
            }
            printf("\n");
        }
    }

    if (CB != LA) {
        printf("Produto B*A impossivel\n");
    } else {
        for (int i = 0; i < LB; i++) {
            for (int j = 0; j < CA; j++) {
                D[i][j] = 0;
                for (int k = 0; k < CB; k++) {
                    D[i][j] += B[i][k] * A[k][j];
                }
            }
        }
        printf("B*A (%d x %d):\n", LB, CA);
        for (int i = 0; i < LB; i++) {
            for (int j = 0; j < CA; j++) {
                if (j > 0) {
                    printf(" ");
                }
                printf("%d", D[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
```

### `E06-E06` *(Programa completo — Quadrado matricial `A^2` e traço)*
Arquivo: [E06_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E06_E06.c)
```c
#include <stdio.h>
#define MAX 20

int main(void) {
    int N, A[MAX][MAX], P[MAX][MAX];
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            P[i][j] = 0;
            for (int k = 0; k < N; k++) {
                P[i][j] += A[i][k] * A[k][j];
            }
        }
    }

    int traco = 0;
    for (int i = 0; i < N; i++) {
        traco += P[i][i];
    }

    printf("A^2:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", P[i][j]);
        }
        printf("\n");
    }
    printf("Traco de A^2: %d\n", traco);
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`E06-C01` a `E06-C03`)

### `E06-C01` *(Rastreamento Manual e Compatibilidade)*
1. `C[1][0]` utiliza a linha `1` de `A` (`3, 1, -2`) e a coluna `0` de `B` (`1, 0, 5`):
   `C[1][0] = 3*1 + 1*0 + (-2)*5 = 3 + 0 - 10 = -7`.
2. Dimensões de `C`: **`2 x 2`** (`LA = 2` linhas e `CB = 2` colunas).
3. Porque o número de colunas de `A` (`4`) é diferente do número de linhas de `B` (`3`), faltando par para o 4º elemento da linha de `A` na coluna de `B`.

### `E06-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `j < CA` no 2º laço usa as colunas de `A` em vez das colunas de `B` (`CB`). Correto: `j < CB`.
  2. Falta `C[i][j] = 0;` antes do laço `k`, causando soma sobre lixo de memória. Correto: inicializar `C[i][j] = 0;` antes de `for (int k = ...`.
  3. `k < LA` no 3º laço usa as linhas de `A` em vez do eixo comum `CA` (ou `LB`). Correto: `k < CA`.
- **Solução corrigida completa:** [E06_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E06_C02_corrigido.c)
```c
#include <stdio.h>
#define MAX 20

int main(void) {
    int LA, CA, LB, CB;
    int A[MAX][MAX], B[MAX][MAX], C[MAX][MAX];

    scanf("%d %d", &LA, &CA);
    for (int i = 0; i < LA; i++) {
        for (int j = 0; j < CA; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    scanf("%d %d", &LB, &CB);
    for (int i = 0; i < LB; i++) {
        for (int j = 0; j < CB; j++) {
            scanf("%d", &B[i][j]);
        }
    }

    for (int i = 0; i < LA; i++) {
        for (int j = 0; j < CB; j++) {
            C[i][j] = 0;
            for (int k = 0; k < CA; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    printf("Resultado (%d x %d):\n", LA, CB);
    for (int i = 0; i < LA; i++) {
        for (int j = 0; j < CB; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", C[i][j]);
        }
        printf("\n");
    }
    return 0;
}
```

### `E06-C03` *(Programa completo — Matriz de Gram `A * A^T`)*
Arquivo: [E06_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E06_C03.c)
```c
#include <stdio.h>
#define MAX 20

int main(void) {
    int L, C, A[MAX][MAX], T[MAX][MAX], G[MAX][MAX];
    scanf("%d %d", &L, &C);
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            T[j][i] = A[i][j];
        }
    }

    for (int i = 0; i < L; i++) {
        for (int j = 0; j < L; j++) {
            G[i][j] = 0;
            for (int k = 0; k < C; k++) {
                G[i][j] += A[i][k] * T[k][j];
            }
        }
    }

    printf("A * A^T (%d x %d):\n", L, L);
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < L; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", G[i][j]);
        }
        printf("\n");
    }
    return 0;
}
```
