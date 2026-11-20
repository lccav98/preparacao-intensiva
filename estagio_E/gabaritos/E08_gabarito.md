# Gabarito Comentado — Bloco `E08` (Revisão e Consolidação do Estágio E)

> **Bloco de referência:** [E08_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/blocos/E08_bloco.md)  
> **Nota para Caça ao Bug:** `E08-E02` e `E08-E03` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`E08-E01` a `E08-E06`)

### `E08-E01` *(Teste de Mesa Integrado — Diagonais, Produto Parcial e Saturação)*
1. Para `M = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}`:
   - Diagonal principal (`i == j`): `1 + 5 + 9 = 15`.
   - Diagonal secundária (`i + j == 2`): `3 + 5 + 7 = 15`.
   - Acima da diagonal principal (`j > i`): `M[0][1] + M[0][2] + M[1][2] = 2 + 3 + 6 = 11` *(atenção para não omitir `M[1][2] = 6`!)*.
2. `C[0][1]` usa a linha `0` de `A` (`2, -1`) e a coluna `1` de `B` (`5, -2`):
   `C[0][1] = 2*5 + (-1)*(-2) = 10 + 2 = 12`.
3. `210 + 70 = 280` → saturado em `[0, 255]` resulta em **`255`**. Ao limiarizar com `L = 255` (`255 >= 255`), resulta em **`255`**.

### `E08-E02` *(Caça ao Bug 1 — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `int soma = 0;` está **fora** do laço `for (int j = 0; j < N; j++)`, acumulando a soma das colunas anteriores. Correto: declarar `int soma = 0;` **dentro** do laço `j`.
  2. `int maior = 0;` falha quando todos os elementos da matriz são negativos! Correto: `int maior = A[0][0];`.
  3. O laço da matriz identidade verifica apenas a diagonal principal (`A[i][i] != 1`), aceitando falsamente uma matriz que tenha `1` na diagonal e valores diferentes de `0` fora dela! Correto: testar `(i == j && A[i][j] != 1) || (i != j && A[i][j] != 0)` em todos os elementos.
- **Solução corrigida completa:** [E08_E02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E08_E02_corrigido.c)
```c
#include <stdio.h>
#define MAX 20

int main(void) {
    int N, A[MAX][MAX];
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    for (int j = 0; j < N; j++) {
        int soma = 0;
        for (int i = 0; i < N; i++) {
            soma += A[i][j];
        }
        printf("Coluna %d: %d\n", j, soma);
    }

    int maior = A[0][0], li = 0, co = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (A[i][j] > maior) {
                maior = A[i][j];
                li = i;
                co = j;
            }
        }
    }
    printf("Maior: %d em (%d, %d)\n", maior, li, co);

    int id = 1;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if ((i == j && A[i][j] != 1) || (i != j && A[i][j] != 0)) {
                id = 0;
                break;
            }
        }
        if (!id) {
            break;
        }
    }
    printf("Identidade: %s\n", id ? "Sim" : "Nao");
    return 0;
}
```

### `E08-E03` *(Caça ao Bug 2 — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. Falta o recorte inferior `if (img[i][j] < 0) img[i][j] = 0;` quando `delta` é negativo.
  2. `T[i][j] = img[i][j];` apenas copia `img` sem transpor. Correto: `T[j][i] = img[i][j];`.
  3. Na impressão do cabeçalho PGM P2 e dos laços de `T`, as dimensões não foram invertidas (`largura` da transposta é `altura` original, e `altura` da transposta é `largura` original). Correto: `printf("P2\n%d %d\n255\n", altura, largura);` e laços `i < largura`, `j < altura`.
- **Solução corrigida completa:** [E08_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E08_E03_corrigido.c)
```c
#include <stdio.h>
#define MAX_DIM 200

int main(void) {
    static int img[MAX_DIM][MAX_DIM];
    static int T[MAX_DIM][MAX_DIM];
    int largura, altura, delta;

    scanf("%d %d", &largura, &altura);
    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            scanf("%d", &img[i][j]);
        }
    }
    scanf("%d", &delta);

    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            img[i][j] += delta;
            if (img[i][j] < 0) {
                img[i][j] = 0;
            } else if (img[i][j] > 255) {
                img[i][j] = 255;
            }
            T[j][i] = img[i][j];
        }
    }

    printf("P2\n%d %d\n255\n", altura, largura);
    for (int i = 0; i < largura; i++) {
        for (int j = 0; j < altura; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", T[i][j]);
        }
        printf("\n");
    }
    return 0;
}
```

### `E08-E04` *(Programa completo — Somas por linha/coluna, diagonais e triângulos)*
Arquivo: [E08_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E08_E04.c)
```c
#include <stdio.h>
#define MAX 20

int main(void) {
    int N, A[MAX][MAX];
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    printf("Somas linhas:");
    for (int i = 0; i < N; i++) {
        int s = 0;
        for (int j = 0; j < N; j++) {
            s += A[i][j];
        }
        printf(" %d", s);
    }
    printf("\n");

    printf("Somas colunas:");
    for (int j = 0; j < N; j++) {
        int s = 0;
        for (int i = 0; i < N; i++) {
            s += A[i][j];
        }
        printf(" %d", s);
    }
    printf("\n");

    int dp = 0, ds = 0, acima = 0, abaixo = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i == j) {
                dp += A[i][j];
            } else if (j > i) {
                acima += A[i][j];
            } else {
                abaixo += A[i][j];
            }
            if (i + j == N - 1) {
                ds += A[i][j];
            }
        }
    }

    printf("Diagonal principal: %d\n", dp);
    printf("Diagonal secundaria: %d\n", ds);
    printf("Acima principal: %d\n", acima);
    printf("Abaixo principal: %d\n", abaixo);
    return 0;
}
```

### `E08-E05` *(Programa completo — Produto matricial, simetria e busca 2D)*
Arquivo: [E08_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E08_E05.c)
```c
#include <stdio.h>
#define MAX 20

int main(void) {
    int LA, CA, LB, CB, alvo;
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
    scanf("%d", &alvo);

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

        int sim = 1;
        if (LA != CB) {
            sim = 0;
        } else {
            for (int i = 0; i < LA; i++) {
                for (int j = i + 1; j < CB; j++) {
                    if (C[i][j] != C[j][i]) {
                        sim = 0;
                        break;
                    }
                }
                if (!sim) {
                    break;
                }
            }
        }
        printf("Simetrica: %s\n", sim ? "Sim" : "Nao");

        int li = -1, co = -1;
        for (int i = 0; i < LA && li == -1; i++) {
            for (int j = 0; j < CB; j++) {
                if (C[i][j] == alvo) {
                    li = i;
                    co = j;
                    break;
                }
            }
        }
        if (li == -1) {
            printf("Alvo nao encontrado\n");
        } else {
            printf("Alvo encontrado em (%d, %d)\n", li, co);
        }
    }
    return 0;
}
```

### `E08-E06` *(Programa completo — Pipeline de imagem PGM P2)*
Arquivo: [E08_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E08_E06.c)
```c
#include <stdio.h>
#define ALTURA_MAX 500
#define LARGURA_MAX 500

int main(void) {
    static int img[ALTURA_MAX][LARGURA_MAX];
    int largura, altura, delta, limiar;

    scanf("%d %d", &largura, &altura);
    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            scanf("%d", &img[i][j]);
        }
    }
    scanf("%d %d", &delta, &limiar);

    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            img[i][j] += delta;
            if (img[i][j] < 0) {
                img[i][j] = 0;
            } else if (img[i][j] > 255) {
                img[i][j] = 255;
            }
        }
    }

    int min_v = img[0][0], min_i = 0, min_j = 0;
    int max_v = img[0][0], max_i = 0, max_j = 0;
    int pretos = 0, brancos = 0;

    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            if (img[i][j] < min_v) {
                min_v = img[i][j];
                min_i = i;
                min_j = j;
            }
            if (img[i][j] > max_v) {
                max_v = img[i][j];
                max_i = i;
                max_j = j;
            }
            if (img[i][j] < limiar) {
                img[i][j] = 0;
                pretos++;
            } else {
                img[i][j] = 255;
                brancos++;
            }
        }
    }

    printf("P2\n%d %d\n255\n", largura, altura);
    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", img[i][j]);
        }
        printf("\n");
    }
    printf("Minimo: %d em (%d, %d)\n", min_v, min_i, min_j);
    printf("Maximo: %d em (%d, %d)\n", max_v, max_i, max_j);
    printf("Pretos: %d Brancos: %d\n", pretos, brancos);
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`E08-C01` a `E08-C03`)

### `E08-C01` *(Teste de Mesa Integrado)*
1. Para `M = {{4, 1, -2}, {1, 0, 5}, {-2, 5, 3}}`:
   - **Simétrica:** **Sim** (`M[0][1] == M[1][0] == 1`, `M[0][2] == M[2][0] == -2`, `M[1][2] == M[2][1] == 5`).
   - **Soma da diagonal secundária (`i + j == 2`):** `-2 + 0 + (-2) = -4`.
   - **Soma da 2ª coluna (`j = 1`, base 0):** `1 + 0 + 5 = 6`.
2. Para `X` (`2 x 3`) e `Y` (`3 x 1`), `Z = X * Y` tem dimensões **`2 x 1`**:
   - `Z[0][0] = 1*5 + 0*(-2) + (-1)*4 = 5 + 0 - 4 = 1`
   - `Z[1][0] = 2*5 + 3*(-2) + 1*4 = 10 - 6 + 4 = 8`
   - Logo, $Z = \begin{pmatrix} 1 \\ 8 \end{pmatrix}$.

### `E08-C02` *(Programa Completo — Transposta de `A + B` e busca 2D)*
Arquivo: [E08_C02.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E08_C02.c)
```c
#include <stdio.h>
#define MAX 20

int main(void) {
    int L, C, alvo;
    int A[MAX][MAX], B[MAX][MAX], T[MAX][MAX];

    scanf("%d %d", &L, &C);
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &A[i][j]);
        }
    }
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &B[i][j]);
        }
    }
    scanf("%d", &alvo);

    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            T[j][i] = A[i][j] + B[i][j];
        }
    }

    int li = -1, co = -1;
    for (int i = 0; i < C && li == -1; i++) {
        for (int j = 0; j < L; j++) {
            if (T[i][j] == alvo) {
                li = i;
                co = j;
                break;
            }
        }
    }

    printf("Transposta de A+B (%d x %d):\n", C, L);
    for (int i = 0; i < C; i++) {
        for (int j = 0; j < L; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", T[i][j]);
        }
        printf("\n");
    }
    if (li == -1) {
        printf("Busca em T: nao encontrado\n");
    } else {
        printf("Busca em T: (%d, %d)\n", li, co);
    }
    return 0;
}
```

### `E08-C03` *(Programa Completo — Produto, identidade e saturação `[0, 255]`)*
Arquivo: [E08_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E08_C03.c)
```c
#include <stdio.h>
#define MAX 20

int main(void) {
    int N, A[MAX][MAX], B[MAX][MAX], P[MAX][MAX];
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &A[i][j]);
        }
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &B[i][j]);
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            P[i][j] = 0;
            for (int k = 0; k < N; k++) {
                P[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    int id = 1;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if ((i == j && P[i][j] != 1) || (i != j && P[i][j] != 0)) {
                id = 0;
                break;
            }
        }
        if (!id) {
            break;
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (P[i][j] < 0) {
                P[i][j] = 0;
            } else if (P[i][j] > 255) {
                P[i][j] = 255;
            }
        }
    }

    printf("Produto saturado [0, 255]:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", P[i][j]);
        }
        printf("\n");
    }
    printf("Identidade (antes de saturar): %s\n", id ? "Sim" : "Nao");
    return 0;
}
```
