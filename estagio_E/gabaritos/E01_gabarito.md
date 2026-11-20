# Gabarito Comentado — Bloco `E01` (Matrizes 2D: Declaração, *Row-Major*, Acesso e Leitura/Escrita)

> **Bloco de referência:** [E01_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/blocos/E01_bloco.md)  
> **Nota para Caça ao Bug:** `E01-E03` e `E01-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`E01-E01` a `E01-E05`)

### `E01-E01` *(Leitura e Análise de Memória)*
1. `a[0][2] = 0` *(linha 0 inicializada parcialmente: `{1, 2, 0, 0}`)*, `a[1][2] = 5` *(linha 1: `{3, 4, 5, 0}`)*, `a[2][0] = 0` *(linha 2 não informada é zerada: `{0, 0, 0, 0}`)*, `b[1][1] = 0`.
2. Em *row-major* (`idx = i * C + j`, com `C = 4`):
   - `a[1][3]` → `1 * 4 + 3 = 7`.
   - `a[2][1]` → `2 * 4 + 1 = 9`.
3. Os índices válidos de `a[3][4]` são `0..2` para linhas e `0..3` para colunas. Logo, `a[3][1]` ultrapassa a última linha (`2`) e `a[0][4]` ultrapassa a última coluna (`3`), gerando acesso fora dos limites (*out-of-bounds*) e comportamento indefinido.

### `E01-E02` *(Completar solução)*
- **`/* A */`:** `L`
- **`/* B */`:** `&m[i][j]`
- **`/* C */`:** `j < C`
- **`/* D */`:** `printf("\n");`

### `E01-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `for (int j = 0; j <= C; j++)` na leitura acessa `m[i][C]` (`m[i][3]`), fora dos limites `0..C-1`. Correto: `j < C`.
  2. `scanf("%d", m[i][j]);` omite o operador de endereço `&`. Correto: `scanf("%d", &m[i][j]);`.
  3. `printf("\n");` está dentro do laço interno `j`, quebrando a linha após cada elemento em vez de apenas ao fim de cada linha `i`. Correto: mover `printf("\n");` para logo após o fechamento do laço `for (int j ...)`.
- **Solução corrigida completa:** [E01_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E01_E03_corrigido.c)
```c
#include <stdio.h>
#define L 2
#define C 3

int main(void) {
    int m[L][C];

    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", m[i][j]);
        }
        printf("\n");
    }

    return 0;
}
```

### `E01-E04` *(Programa completo — Linhas em ordem inversa)*
Arquivo: [E01_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E01_E04.c)
```c
#include <stdio.h>
#define L 3
#define C 3

int main(void) {
    int m[L][C];

    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    for (int i = L - 1; i >= 0; i--) {
        for (int j = 0; j < C; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", m[i][j]);
        }
        printf("\n");
    }

    return 0;
}
```

### `E01-E05` *(Programa completo — Grade `l x c` e cantos)*
Arquivo: [E01_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E01_E05.c)
```c
#include <stdio.h>
#define MAX_L 10
#define MAX_C 10

int main(void) {
    int l, c;
    int m[MAX_L][MAX_C];
    scanf("%d %d", &l, &c);

    for (int i = 0; i < l; i++) {
        for (int j = 0; j < c; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    printf("Cantos: %d %d\n", m[0][0], m[l - 1][c - 1]);
    for (int i = 0; i < l; i++) {
        for (int j = 0; j < c; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", m[i][j]);
        }
        printf("\n");
    }

    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`E01-C01` a `E01-C03`)

### `E01-C01` *(Análise de Memória, Row-Major e Limites)*
1. `x[0][1] = 0`, `x[1][1] = 9`, `x[2][0] = 0`.
2. Posição linear de `x[2][1]` com `C = 3`: `2 * 3 + 1 = 7`.
3. Erros:
   - `(a)` `int y[l][c];` declara VLA usando variáveis em tempo de execução (proibida no curso; usar `#define MAX 10` e `int y[MAX][MAX];`).
   - `(b)` `x[2][3] = 5;` acessa coluna `3`, além do último índice válido (`2`), causando comportamento indefinido (*out-of-bounds*).

### `E01-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `int m[l][c];` declara VLA. Correto: `int m[MAX][MAX];`.
  2. `scanf("%d", m[i][j]);` omite `&`. Correto: `scanf("%d", &m[i][j]);`.
  3. Falta `printf("\n");` após o laço interno `j` na impressão (todas as linhas sairiam grudadas na mesma linha). Correto: adicionar `printf("\n");` após o `for (int j ...)`.
- **Solução corrigida completa:** [E01_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E01_C02_corrigido.c)
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

    for (int i = 0; i < l; i++) {
        for (int j = 0; j < c; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", m[i][j]);
        }
        printf("\n");
    }

    return 0;
}
```

### `E01-C03` *(Programa completo — Matriz `3 x 4` original e percurso inverso total)*
Arquivo: [E01_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E01_C03.c)
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

    printf("Matriz:\n");
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", m[i][j]);
        }
        printf("\n");
    }

    printf("Inversa:\n");
    for (int i = L - 1; i >= 0; i--) {
        for (int j = C - 1; j >= 0; j--) {
            if (j < C - 1) {
                printf(" ");
            }
            printf("%d", m[i][j]);
        }
        printf("\n");
    }

    return 0;
}
```
