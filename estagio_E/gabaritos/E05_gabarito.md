# Gabarito Comentado — Bloco `E05` (Transposição, Verificação de Simetria e Soma de Matrizes)

> **Bloco de referência:** [E05_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/blocos/E05_bloco.md)  
> **Nota para Caça ao Bug:** `E05-E03` e `E05-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`E05-E01` a `E05-E05`)

### `E05-E01` *(Teste de Mesa — Transposição Retangular e Simetria)*
1. Como `A` é `2 x 3`, a transposta `T = A^T` possui dimensões **`3 x 2`** (`3` linhas, `2` colunas):
   - `T[0][1] = A[1][0] = 4`
   - `T[1][0] = A[0][1] = 2`
   - `T[2][0] = A[0][2] = 3`
   - `T[2][1] = A[1][2] = 6`
2. Para `M = {{5, -1, 4}, {-1, 0, 2}, {4, 3, 7}}` testando `j > i`:
   - `(0, 1)`: `M[0][1] = -1` vs `M[1][0] = -1` → iguais.
   - `(0, 2)`: `M[0][2] = 4` vs `M[2][0] = 4` → iguais.
   - `(1, 2)`: `M[1][2] = 2` vs `M[2][1] = 3` → **diferentes!** Aqui `sim` vai para **`0`** e o laço é interrompido.
   - Na diagonal principal (`i == j`), `M[i][i] == M[i][i]` é uma identidade trivial que nunca pode falhar, portanto é desnecessário testá-la.

### `E05-E02` *(Completar solução)*
- **`/* A */`:** `T[j][i]`
- **`/* B */`:** `L != C`
- **`/* C */`:** `i + 1` *(ou `0`, embora `i + 1` evite comparações redundantes)*
- **`/* D */`:** `A[i][j] != A[j][i]`

### `E05-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `T[i][j] = A[j][i];` troca os índices no lado errado e lê `A[j][i]` fora da região preenchida quando `L != C`. Correto: `T[j][i] = A[i][j];`.
  2. `sim = 1;` é reatribuído **dentro** do laço `for (int i = 0; i < L; i++)`, apagando falhas detectadas em linhas anteriores (e falta `if (!sim) break;`). Correto: manter `int sim = 1;` apenas fora dos laços e interromper ao encontrar `sim == 0`.
  3. Na impressão de `T`, os laços usam `i < L` e `j < C` em vez das dimensões invertidas `C x L`. Correto: `for (int i = 0; i < C; i++)` e `for (int j = 0; j < L; j++)`.
- **Solução corrigida completa:** [E05_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E05_E03_corrigido.c)
```c
#include <stdio.h>
#define MAX 20

int main(void) {
    int L, C, A[MAX][MAX], T[MAX][MAX];
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

    int sim = 1;
    if (L != C) {
        sim = 0;
    } else {
        for (int i = 0; i < L; i++) {
            for (int j = i + 1; j < C; j++) {
                if (A[i][j] != A[j][i]) {
                    sim = 0;
                    break;
                }
            }
            if (!sim) {
                break;
            }
        }
    }

    printf("Transposta (%d x %d):\n", C, L);
    for (int i = 0; i < C; i++) {
        for (int j = 0; j < L; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", T[i][j]);
        }
        printf("\n");
    }
    printf("Simetrica: %s\n", sim ? "Sim" : "Nao");
    return 0;
}
```

### `E05-E04` *(Programa completo — Soma e transposta da soma)*
Arquivo: [E05_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E05_E04.c)
```c
#include <stdio.h>
#define MAX 20

int main(void) {
    int L, C, A[MAX][MAX], B[MAX][MAX], S[MAX][MAX], T[MAX][MAX];
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

    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            S[i][j] = A[i][j] + B[i][j];
            T[j][i] = S[i][j];
        }
    }

    printf("Soma (%d x %d):\n", L, C);
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", S[i][j]);
        }
        printf("\n");
    }

    printf("Transposta da soma (%d x %d):\n", C, L);
    for (int i = 0; i < C; i++) {
        for (int j = 0; j < L; j++) {
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

### `E05-E05` *(Programa completo — Matriz `A + A^T` e simetria)*
Arquivo: [E05_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E05_E05.c)
```c
#include <stdio.h>
#define MAX 20

int main(void) {
    int N, A[MAX][MAX], T[MAX][MAX], S[MAX][MAX];
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            T[j][i] = A[i][j];
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            S[i][j] = A[i][j] + T[i][j];
        }
    }

    int simA = 1;
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            if (A[i][j] != A[j][i]) {
                simA = 0;
                break;
            }
        }
        if (!simA) {
            break;
        }
    }

    int simS = 1;
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            if (S[i][j] != S[j][i]) {
                simS = 0;
                break;
            }
        }
        if (!simS) {
            break;
        }
    }

    printf("Simetrica A: %s\n", simA ? "Sim" : "Nao");
    printf("Matriz A + A^T:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", S[i][j]);
        }
        printf("\n");
    }
    printf("Simetrica A + A^T: %s\n", simS ? "Sim" : "Nao");
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`E05-C01` a `E05-C03`)

### `E05-C01` *(Análise de Dimensões e Simetria)*
1. Como `A` tem `3` linhas e `4` colunas, a transposta precisa ter `4` linhas e `3` colunas; gravar `A[3][0]` na própria `A[3][4]` causaria acesso fora dos limites de linhas (`0..2`). Logo, `T` deve ser declarada com dimensões invertidas `int T[4][3];`.
2. Para uma matriz `4 x 4`, os pares `j > i` são: `(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)` — no máximo **`6` comparações** ($\frac{4 \times 3}{2} = 6$).

### `E05-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `if (L1 != L2 && C1 != C2)` usa `&&` em vez de `||`: aceita somar matrizes com apenas uma dimensão diferente (ex.: `2 x 3` e `2 x 4`). Correto: `if (L1 != L2 || C1 != C2)`.
  2. Falta o bloco `else { ... }` após o `if`, fazendo o programa somar e imprimir mesmo quando imprime `Soma impossivel`. Correto: colocar cálculo e impressão da soma dentro de `else`.
  3. `S[i][j] = A[i][j] + B[j][i];` inverte os índices de `B`, errando a soma e invadindo memória quando `L1 != C1`. Correto: `S[i][j] = A[i][j] + B[i][j];`.
- **Solução corrigida completa:** [E05_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E05_C02_corrigido.c)
```c
#include <stdio.h>
#define MAX 20

int main(void) {
    int L1, C1, L2, C2;
    int A[MAX][MAX], B[MAX][MAX], S[MAX][MAX];

    scanf("%d %d", &L1, &C1);
    for (int i = 0; i < L1; i++) {
        for (int j = 0; j < C1; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    scanf("%d %d", &L2, &C2);
    for (int i = 0; i < L2; i++) {
        for (int j = 0; j < C2; j++) {
            scanf("%d", &B[i][j]);
        }
    }

    if (L1 != L2 || C1 != C2) {
        printf("Soma impossivel\n");
    } else {
        for (int i = 0; i < L1; i++) {
            for (int j = 0; j < C1; j++) {
                S[i][j] = A[i][j] + B[i][j];
            }
        }
        printf("Soma:\n");
        for (int i = 0; i < L1; i++) {
            for (int j = 0; j < C1; j++) {
                if (j > 0) {
                    printf(" ");
                }
                printf("%d", S[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
```

### `E05-C03` *(Programa completo — Transposta de `A + B` e simetria)*
Arquivo: [E05_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E05_C03.c)
```c
#include <stdio.h>
#define MAX 20

int main(void) {
    int N, A[MAX][MAX], B[MAX][MAX], S[MAX][MAX], T[MAX][MAX];
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
            S[i][j] = A[i][j] + B[i][j];
            T[j][i] = S[i][j];
        }
    }

    int sim = 1;
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            if (S[i][j] != S[j][i]) {
                sim = 0;
                break;
            }
        }
        if (!sim) {
            break;
        }
    }

    printf("Transposta de (A + B):\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", T[i][j]);
        }
        printf("\n");
    }
    printf("Simetrica (A + B): %s\n", sim ? "Sim" : "Nao");
    return 0;
}
```
