# Gabarito Comentado — Bloco `E04` (Diagonais, Matriz Identidade e Regiões Triangulares)

> **Bloco de referência:** [E04_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/blocos/E04_bloco.md)  
> **Nota para Caça ao Bug:** `E04-E03` e `E04-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`E04-E01` a `E04-E05`)

### `E04-E01` *(Teste de Mesa — Regiões, Diagonais e Soma Triangular)*
1. - **Diagonal principal (`i == j`):** `m[0][0]=2`, `m[1][1]=4`, `m[2][2]=6`, `m[3][3]=8` → **`2, 4, 6, 8`**.
   - **Diagonal secundária (`i + j == 3`):** `m[0][3]=1`, `m[1][2]=1`, `m[2][1]=0`, `m[3][0]=1` → **`1, 1, 0, 1`**.
2. **Acima da diagonal principal (`j > i`):**
   - `(0, 1) = 1`, `(0, 2) = 2`, `(0, 3) = 1`
   - `(1, 2) = 1`, `(1, 3) = 3`
   - `(2, 3) = 2`
   - Soma: `1 + 2 + 1 + 1 + 3 + 2 =` **`10`** *(incluindo `m[2][3] = 2`; omitir a linha 2 daria `8`)*.
3. **Abaixo da diagonal principal (`i > j`):**
   - `(1, 0) = 3`, `(2, 0) = 5`, `(2, 1) = 0`, `(3, 0) = 1`, `(3, 1) = 2`, `(3, 2) = 4`
   - Soma: `3 + 5 + 0 + 1 + 2 + 4 =` **`15`**.

### `E04-E02` *(Completar solução)*
- **`/* A */`:** `m[i][N - 1 - i]`
- **`/* B */`:** `int eh_id = 1;`
- **`/* C */`:** `i < N && eh_id`
- **`/* D */`:** `(i == j && m[i][j] != 1) || (i != j && m[i][j] != 0)`

### `E04-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `m[i][N - i]` na diagonal secundária acessa `m[0][3]` fora dos limites quando `i = 0` e ignora `m[2][0]`. Correto: `m[i][N - 1 - i]`.
  2. A condição `if (i == j && m[i][j] != 1)` testa apenas os elementos da diagonal principal e **não verifica** se os elementos fora dela (`i != j`) são iguais a `0` (aceitaria uma matriz cheia de `1`s). Correto: `if ((i == j && m[i][j] != 1) || (i != j && m[i][j] != 0))`.
  3. O ramo `else { eh_id = 1; }` reativa a flag a cada elemento válido posterior, gerando falso positivo sempre que o último elemento `m[2][2]` vale `1`. Correto: remover o `else` (e opcionalmente usar `&& eh_id` no laço externo / `break`).
- **Solução corrigida completa:** [E04_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E04_E03_corrigido.c)
```c
#include <stdio.h>
#define N 3

int main(void) {
    int m[N][N];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    printf("Diag secundaria:");
    for (int i = 0; i < N; i++) {
        printf(" %d", m[i][N - 1 - i]);
    }
    printf("\n");

    int eh_id = 1;
    for (int i = 0; i < N && eh_id; i++) {
        for (int j = 0; j < N; j++) {
            if ((i == j && m[i][j] != 1) || (i != j && m[i][j] != 0)) {
                eh_id = 0;
                break;
            }
        }
    }

    if (eh_id) {
        printf("Identidade: SIM\n");
    } else {
        printf("Identidade: NAO\n");
    }

    return 0;
}
```

### `E04-E04` *(Programa completo — Diagonais e somas triangulares `4 x 4`)*
Arquivo: [E04_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E04_E04.c)
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

    printf("Diag principal:");
    for (int i = 0; i < N; i++) {
        printf(" %d", m[i][i]);
    }
    printf("\n");

    printf("Diag secundaria:");
    for (int i = 0; i < N; i++) {
        printf(" %d", m[i][N - 1 - i]);
    }
    printf("\n");

    int soma_acima = 0;
    int soma_abaixo = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (j > i) {
                soma_acima += m[i][j];
            } else if (i > j) {
                soma_abaixo += m[i][j];
            }
        }
    }

    printf("Soma acima: %d\n", soma_acima);
    printf("Soma abaixo: %d\n", soma_abaixo);

    return 0;
}
```

### `E04-E05` *(Programa completo — Diagonais e matriz identidade `n x n`)*
Arquivo: [E04_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E04_E05.c)
```c
#include <stdio.h>
#define MAX 10

int main(void) {
    int n;
    int m[MAX][MAX];
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    printf("Diag principal:");
    for (int i = 0; i < n; i++) {
        printf(" %d", m[i][i]);
    }
    printf("\n");

    printf("Diag secundaria:");
    for (int i = 0; i < n; i++) {
        printf(" %d", m[i][n - 1 - i]);
    }
    printf("\n");

    int eh_id = 1;
    for (int i = 0; i < n && eh_id; i++) {
        for (int j = 0; j < n; j++) {
            if ((i == j && m[i][j] != 1) || (i != j && m[i][j] != 0)) {
                eh_id = 0;
                break;
            }
        }
    }

    if (eh_id) {
        printf("Identidade: SIM\n");
    } else {
        printf("Identidade: NAO\n");
    }

    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`E04-C01` a `E04-C03`)

### `E04-C01` *(Rastreamento Triangular e Falso Positivo de Identidade)*
1. - **Acima (`j > i`):** `m[0][1]=3, m[0][2]=1, m[0][3]=2, m[1][2]=4, m[1][3]=1, m[2][3]=3` → soma = `3 + 1 + 2 + 4 + 1 + 3 =` **`14`**.
   - **Abaixo (`i > j`):** `m[1][0]=2, m[2][0]=0, m[2][1]=5, m[3][0]=1, m[3][1]=0, m[3][2]=2` → soma = `2 + 0 + 5 + 1 + 0 + 2 =` **`10`**.
2. Embora vários elementos fora da diagonal (como `m[0][1] = 3`) desliguem `eh_id = 0`, o último elemento visitado nos laços (`m[3][3] = 1`) satisfaz a condição de identidade e entra no ramo `else { eh_id = 1; }`, sobrescrevendo os erros anteriores e produzindo o falso positivo `SIM`.

### `E04-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `if (i + j == N)` identifica uma diagonal deslocada (e ignora `(0, 3)`). A diagonal secundária satisfaz `i + j == N - 1`.
  2. `if (j > i)` soma os elementos **acima** da diagonal principal em vez de **abaixo**. Correto: `if (i > j)`.
  3. O bloco `else { eh_id = 1; }` apaga violações anteriores quando um elemento subsequente satisfaz a regra. Correto: remover o `else`.
- **Solução corrigida completa:** [E04_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E04_C02_corrigido.c)
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

    int soma_sec = 0, soma_abaixo = 0;
    int eh_id = 1;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i + j == N - 1) {
                soma_sec += m[i][j];
            }
            if (i > j) {
                soma_abaixo += m[i][j];
            }
            if ((i == j && m[i][j] != 1) || (i != j && m[i][j] != 0)) {
                eh_id = 0;
            }
        }
    }

    printf("Soma sec: %d\n", soma_sec);
    printf("Soma abaixo: %d\n", soma_abaixo);
    if (eh_id) {
        printf("Identidade: SIM\n");
    } else {
        printf("Identidade: NAO\n");
    }

    return 0;
}
```

### `E04-C03` *(Programa completo — Somas de diagonais/regiões e identidade `n x n`)*
Arquivo: [E04_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E04_C03.c)
```c
#include <stdio.h>
#define MAX 10

int main(void) {
    int n;
    int m[MAX][MAX];
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    int soma_p = 0, soma_s = 0;
    for (int i = 0; i < n; i++) {
        soma_p += m[i][i];
        soma_s += m[i][n - 1 - i];
    }

    int soma_acima = 0, soma_abaixo = 0;
    int eh_id = 1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (j > i) {
                soma_acima += m[i][j];
            } else if (i > j) {
                soma_abaixo += m[i][j];
            }
            if ((i == j && m[i][j] != 1) || (i != j && m[i][j] != 0)) {
                eh_id = 0;
            }
        }
    }

    printf("Soma principal: %d\n", soma_p);
    printf("Soma secundaria: %d\n", soma_s);
    printf("Soma acima: %d\n", soma_acima);
    printf("Soma abaixo: %d\n", soma_abaixo);
    if (eh_id) {
        printf("Identidade: SIM\n");
    } else {
        printf("Identidade: NAO\n");
    }

    return 0;
}
```
