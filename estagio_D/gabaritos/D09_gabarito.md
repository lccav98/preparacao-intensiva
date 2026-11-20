# Gabarito Comentado — Bloco `D09` (Linearização de Grades 2D em Vetor 1D)

> **Bloco de referência:** [D09_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/blocos/D09_bloco.md)  
> **Nota para Caça ao Bug:** `D09-E03` e `D09-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`D09-E01` a `D09-E05`)

### `D09-E01` *(Leitura e Teste de Mesa)*
1. **Conversão direta `(i, j) -> i * 5 + j`:**
   - `(2, 3)` → `2 * 5 + 3 = 13`
   - `(3, 0)` → `3 * 5 + 0 = 15`
   - `(0, 4)` → `0 * 5 + 4 = 4`
2. **Conversão inversa `(idx / 5, idx % 5)`:**
   - `idx = 14`: `(14 / 5, 14 % 5) = (2, 4)`
   - `idx = 7`: `(7 / 5, 7 % 5) = (1, 2)`
3. **Expansão defeituosa `#define IND(i, j) i * 5 + j`:**
   - `IND(1 + 1, 2 + 1)` expande para `1 + 1 * 5 + 2 + 1 = 1 + 5 + 2 + 1 = 9` *(correto seria `(2) * 5 + (3) = 13`)*.
   - `2 * IND(1, 2)` expande para `2 * 1 * 5 + 2 = 10 + 2 = 12` *(correto seria `2 * (1 * 5 + 2) = 14`)*.

---

### `D09-E02` *(Completar solução)*
- **`/* A */`:** `((i) * COLUNAS + (j))`
- **`/* B */`:** `1`
- **`/* C */`:** `buf[j]`
- **`/* D */`:** `'\0'`

---

### `D09-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `#define INDICE(i, j) i * COLUNAS + j` não possui parênteses protetores; em `INDICE(li - 1, co - 1)`, expande para `li - 1 * 4 + co - 1` (índice errado ou negativo!). Correto: `((i) * COLUNAS + (j))`.
  2. `int v[LINHAS + COLUNAS];` aloca apenas `7` posições em vez de `12`. Correto: `int v[LINHAS * COLUNAS];`.
  3. `v[INDICE(j, i)]` inverte linha e coluna na impressão da grade (acessando inclusive fora dos limites quando `j == 3`, pois `LINHAS == 3`). Correto: `v[INDICE(i, j)]`.
- **Solução corrigida completa:** [D09_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D09_E03_corrigido.c)
```c
#include <stdio.h>
#define LINHAS 3
#define COLUNAS 4
#define INDICE(i, j) ((i) * COLUNAS + (j))

int main(void) {
    int v[LINHAS * COLUNAS];

    for (int i = 0; i < LINHAS; i++) {
        for (int j = 0; j < COLUNAS; j++) {
            scanf("%d", &v[INDICE(i, j)]);
        }
    }

    int li, co;
    scanf("%d %d", &li, &co);

    for (int i = 0; i < LINHAS; i++) {
        for (int j = 0; j < COLUNAS; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", v[INDICE(i, j)]);
        }
        printf("\n");
    }

    printf("Consulta: %d\n", v[INDICE(li - 1, co - 1)]);
    return 0;
}
```

---

### `D09-E04` *(Programa completo — Soma por linha e maior com coordenadas 1D)*
Arquivo: [D09_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D09_E04.c)
```c
#include <stdio.h>
#define MAX 400
#define INDICE(i, j, cols) ((i) * (cols) + (j))

int main(void) {
    int l, c;
    int v[MAX];

    scanf("%d %d", &l, &c);
    for (int i = 0; i < l; i++) {
        for (int j = 0; j < c; j++) {
            scanf("%d", &v[INDICE(i, j, c)]);
        }
    }

    for (int i = 0; i < l; i++) {
        int soma = 0;
        for (int j = 0; j < c; j++) {
            soma += v[INDICE(i, j, c)];
        }
        printf("Linha %d: %d\n", i, soma);
    }

    int maior = v[0], idx_maior = 0;
    for (int idx = 1; idx < l * c; idx++) {
        if (v[idx] > maior) {
            maior = v[idx];
            idx_maior = idx;
        }
    }

    printf("Maior: %d em (%d, %d)\n", maior, idx_maior / c, idx_maior % c);
    return 0;
}
```

---

### `D09-E05` *(Programa completo — Grade de caracteres em vetor único 1D)*
Arquivo: [D09_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D09_E05.c)
```c
#include <stdio.h>
#define MAX_GRADE 101
#define MAX_LINHA 11
#define INDICE(i, j, cols) ((i) * (cols) + (j))

int main(void) {
    int l, c, q;
    char grade[MAX_GRADE];
    char buf[MAX_LINHA];

    scanf("%d %d", &l, &c);
    for (int i = 0; i < l; i++) {
        scanf("%10s", buf);
        for (int j = 0; j < c; j++) {
            grade[INDICE(i, j, c)] = buf[j];
        }
    }
    grade[l * c] = '\0';

    scanf("%d", &q);
    for (int k = 0; k < q; k++) {
        int r, s;
        scanf("%d %d", &r, &s);
        if (r >= 0 && r < l && s >= 0 && s < c) {
            printf("%c\n", grade[INDICE(r, s, c)]);
        } else {
            printf("Invalido\n");
        }
    }

    printf("Linear: %s\n", grade);
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`D09-C01` a `D09-C03`)

### `D09-C01` *(Teste de Mesa)*
1. `(2, 5)` → `2 * 6 + 5 = 17`; `(1, 4)` → `1 * 6 + 4 = 10`.
2. `idx = 11`: `(11 / 6, 11 % 6) = (1, 5)`; `idx = 13`: `(13 / 6, 13 % 6) = (2, 1)`.
3. `POS(1 + 1, 3)` expande para `1 + 1 * 6 + 3 = 10` *(errado)*. O valor correto com `((1 + 1) * 6 + (3))` é **`15`**.

---

### `D09-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `#define INDICE(i, j) i * COLUNAS + j` sem parênteses faz `INDICE(lin1 - 1, col)` calcular `lin1 - 1 * 5 + col` (gerando índice errado/negativo). Correto: `((i) * COLUNAS + (j))`.
  2. `char g[LINHAS * COLUNAS];` não reserva `+ 1` byte nem grava `g[LINHAS * COLUNAS] = '\0';` antes do `printf("%s", g)`.
  3. `g[col * LINHAS + i]` usa indexação *column-major* em vez de *row-major*. Correto: `g[INDICE(i, col)]`.
- **Solução corrigida completa:** [D09_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D09_C02_corrigido.c)
```c
#include <stdio.h>
#define LINHAS 3
#define COLUNAS 5
#define INDICE(i, j) ((i) * COLUNAS + (j))

int main(void) {
    char g[LINHAS * COLUNAS + 1];
    char buf[COLUNAS + 1];

    for (int i = 0; i < LINHAS; i++) {
        scanf("%5s", buf);
        for (int j = 0; j < COLUNAS; j++) {
            g[INDICE(i, j)] = buf[j];
        }
    }
    g[LINHAS * COLUNAS] = '\0';

    int lin1, col;
    scanf("%d %d", &lin1, &col);

    printf("Celula: %c\n", g[INDICE(lin1 - 1, col)]);
    printf("Coluna:");
    for (int i = 0; i < LINHAS; i++) {
        printf(" %c", g[INDICE(i, col)]);
    }
    printf("\nLinear: %s\n", g);
    return 0;
}
```

---

### `D09-C03` *(Programa completo — Soma por coluna e busca com conversão inversa)*
Arquivo: [D09_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D09_C03.c)
```c
#include <stdio.h>
#define MAX 225
#define INDICE(i, j, cols) ((i) * (cols) + (j))

int main(void) {
    int l, c, alvo;
    int v[MAX];

    scanf("%d %d", &l, &c);
    for (int i = 0; i < l; i++) {
        for (int j = 0; j < c; j++) {
            scanf("%d", &v[INDICE(i, j, c)]);
        }
    }
    scanf("%d", &alvo);

    for (int j = 0; j < c; j++) {
        int soma = 0;
        for (int i = 0; i < l; i++) {
            soma += v[INDICE(i, j, c)];
        }
        printf("Coluna %d: %d\n", j, soma);
    }

    int ocorrencias = 0, pos = -1;
    for (int idx = 0; idx < l * c; idx++) {
        if (v[idx] == alvo) {
            if (pos == -1) {
                pos = idx;
            }
            ocorrencias++;
        }
    }

    printf("Ocorrencias: %d\n", ocorrencias);
    if (pos == -1) {
        printf("Primeira: Nao encontrado\n");
    } else {
        printf("Primeira: (%d, %d)\n", pos / c, pos % c);
    }
    return 0;
}
```
