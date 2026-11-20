# Gabarito Comentado — Bloco `D05` (Subsequência com Sobreposição e Convolução Discreta)

> **Bloco de referência:** [D05_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/blocos/D05_bloco.md)  
> **Nota para Caça ao Bug:** `D05-E03` e `D05-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`D05-E01` a `D05-E06`)

### `D05-E01` *(Teste de Mesa — Sobreposição e Kernel Assimétrico)*
1. `v = {2, 2, 2, 1, 2, 2}`, `p = {2, 2}` (`n - m = 4`):
   - `i = 0`: `{2, 2} == {2, 2}` → **casa**
   - `i = 1`: `{2, 2} == {2, 2}` → **casa** *(sobreposição com `i = 0`!)*
   - `i = 2`: `{2, 1} != {2, 2}` → falha em `k = 1`
   - `i = 3`: `{1, 2} != {2, 2}` → falha em `k = 0`
   - `i = 4`: `{2, 2} == {2, 2}` → **casa**
   - Índices: **`0, 1, 4`** (total **`3`** ocorrências).
2. `v = {4, 1, 3, 2}`, `h = {1, 2, 5}` (`m = 3`):
   - **Correto (`h[m - 1 - k]`, isto é, pesos `{5, 2, 1}`):**
     - `r[0] = 4*5 + 1*2 + 3*1 = 20 + 2 + 3 = 25`
     - `r[1] = 1*5 + 3*2 + 2*1 = 5 + 6 + 2 = 13`
   - **Errado (se usasse `h[k]`, pesos `{1, 2, 5}`):**
     - `r[0]` daria `4*1 + 1*2 + 3*5 = 21` (errado)
     - `r[1]` daria `1*1 + 3*2 + 2*5 = 17` (errado).

### `D05-E02` *(Completar solução)*
- **`/* A */`:** `i <= n - m`
- **`/* B */`:** `1`
- **`/* C */`:** `v[i + k]`
- **`/* D */`:** `ocorrencias++`

### `D05-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `int soma = 0;` está **fora** do laço `i`, acumulando resultados de janelas anteriores em `r[i]`. Correto: declarar/zerar `int soma = 0;` **dentro** do laço `i`.
  2. `for (int i = 0; i < n; i++)` acessa `v[i + k]` fora dos limites quando `i > n - m`. Correto: `for (int i = 0; i <= n - m; i++)`.
  3. `soma += v[i + k] * h[k];` não inverte o kernel (calcula correlação em vez de convolução). Correto: `soma += v[i + k] * h[m - 1 - k];`.
- **Solução corrigida completa:** [D05_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D05_E03_corrigido.c)
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, m, v[MAX], h[MAX], r[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &m);
    for (int k = 0; k < m; k++) {
        scanf("%d", &h[k]);
    }

    for (int i = 0; i <= n - m; i++) {
        int soma = 0;
        for (int k = 0; k < m; k++) {
            soma += v[i + k] * h[m - 1 - k];
        }
        r[i] = soma;
    }

    printf("Convolucao:");
    for (int i = 0; i < n - m + 1; i++) {
        printf(" %d", r[i]);
    }
    printf("\n");
    return 0;
}
```

### `D05-E04` *(Programa completo — Todas as posições com sobreposição)*
Arquivo: [D05_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D05_E04.c)
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, m, v[MAX], p[MAX], pos[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &m);
    for (int k = 0; k < m; k++) {
        scanf("%d", &p[k]);
    }

    int qtd = 0;
    for (int i = 0; i <= n - m; i++) {
        int casou = 1;
        for (int k = 0; k < m; k++) {
            if (v[i + k] != p[k]) {
                casou = 0;
                break;
            }
        }
        if (casou) {
            pos[qtd++] = i;
        }
    }

    printf("Ocorrencias: %d\n", qtd);
    printf("Indices:");
    if (qtd == 0) {
        printf(" nenhum");
    } else {
        for (int i = 0; i < qtd; i++) {
            printf(" %d", pos[i]);
        }
    }
    printf("\n");
    return 0;
}
```

### `D05-E05` *(Programa completo — Convolução 1D e maior valor)*
Arquivo: [D05_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D05_E05.c)
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, m, v[MAX], h[MAX], r[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &m);
    for (int k = 0; k < m; k++) {
        scanf("%d", &h[k]);
    }

    int tam_r = n - m + 1;
    for (int i = 0; i <= n - m; i++) {
        int soma = 0;
        for (int k = 0; k < m; k++) {
            soma += v[i + k] * h[m - 1 - k];
        }
        r[i] = soma;
    }

    int maior = r[0], pos_maior = 0;
    for (int i = 1; i < tam_r; i++) {
        if (r[i] > maior) {
            maior = r[i];
            pos_maior = i;
        }
    }

    printf("Resultado (%d):", tam_r);
    for (int i = 0; i < tam_r; i++) {
        printf(" %d", r[i]);
    }
    printf("\nMaior convolucao: %d (indice %d)\n", maior, pos_maior);
    return 0;
}
```

### `D05-E06` *(Programa completo — Subvetor e convolução tratando `m > n`)*
Arquivo: [D05_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D05_E06.c)
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, m, v[MAX], p[MAX], r[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &m);
    for (int k = 0; k < m; k++) {
        scanf("%d", &p[k]);
    }

    int ocorrencias = 0;
    for (int i = 0; i <= n - m; i++) {
        int casou = 1;
        for (int k = 0; k < m; k++) {
            if (v[i + k] != p[k]) {
                casou = 0;
                break;
            }
        }
        if (casou) {
            ocorrencias++;
        }
    }

    printf("Ocorrencias: %d\n", ocorrencias);
    if (m > n) {
        printf("Convolucao: vazia\n");
    } else {
        int tam_r = n - m + 1;
        for (int i = 0; i <= n - m; i++) {
            int soma = 0;
            for (int k = 0; k < m; k++) {
                soma += v[i + k] * p[m - 1 - k];
            }
            r[i] = soma;
        }
        printf("Convolucao:");
        for (int i = 0; i < tam_r; i++) {
            printf(" %d", r[i]);
        }
        printf("\n");
    }

    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`D05-C01` a `D05-C03`)

### `D05-C01` *(Análise de Limite e Casos de Borda)*
1. Quando `i = n - m` e `k = m - 1`, o índice acessado é `(n - m) + (m - 1) = n - 1`, que é exatamente o **último índice válido** de `v`. Com `i < n` e `m >= 2`, para `i = n - 1` e `k = 1`, acessa-se `v[n]` (fora dos limites!).
2. Quando `m == n`, `n - m = 0`, logo `i <= 0` executa **1 iteração** (`i = 0`, comparando o vetor inteiro).
3. Quando `m > n`, `n - m < 0`, logo `0 <= n - m` é falso logo no início e executa **0 iterações** (sem acesso indevido).

### `D05-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `int casou = 1;` foi declarado fora do laço `i`: assim que uma janela falha (`casou = 0`), todas as janelas seguintes permanecem com `casou = 0`! Correto: declarar `int casou = 1;` **dentro** do laço `i`.
  2. `i < n - m` exclui a última janela válida (`i == n - m`). Correto: `i <= n - m`.
  3. `i += m - 1;` dentro de `if (casou)` pula posições intermediárias e impede detectar **sobreposições** (ex.: `{1, 1}` em `{1, 1, 1}`). Correto: remover `i += m - 1;` deixando apenas o `i++` do `for`.
- **Solução corrigida completa:** [D05_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D05_C02_corrigido.c)
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, m, v[MAX], p[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &m);
    for (int k = 0; k < m; k++) {
        scanf("%d", &p[k]);
    }

    int ocorrencias = 0;
    for (int i = 0; i <= n - m; i++) {
        int casou = 1;
        for (int k = 0; k < m; k++) {
            if (v[i + k] != p[k]) {
                casou = 0;
                break;
            }
        }
        if (casou) {
            ocorrencias++;
        }
    }

    printf("Ocorrencias: %d\n", ocorrencias);
    return 0;
}
```

### `D05-C03` *(Programa completo — Convolução discreta e soma total)*
Arquivo: [D05_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D05_C03.c)
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, m, v[MAX], h[MAX], r[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &m);
    for (int k = 0; k < m; k++) {
        scanf("%d", &h[k]);
    }

    int tam_r = n - m + 1;
    int soma_total = 0;
    for (int i = 0; i <= n - m; i++) {
        int soma = 0;
        for (int k = 0; k < m; k++) {
            soma += v[i + k] * h[m - 1 - k];
        }
        r[i] = soma;
        soma_total += r[i];
    }

    printf("Tamanho: %d\nValores:", tam_r);
    for (int i = 0; i < tam_r; i++) {
        printf(" %d", r[i]);
    }
    printf("\nSoma total: %d\n", soma_total);
    return 0;
}
```
