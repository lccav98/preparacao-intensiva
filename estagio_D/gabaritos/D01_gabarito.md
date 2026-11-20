# Gabarito Comentado — Bloco `D01` (Vetores 1D: Declaração, Índices Base 0 e Limites)

> **Bloco de referência:** [D01_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/blocos/D01_bloco.md)  
> **Nota para Caça ao Bug:** `D01-E03` e `D01-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`D01-E01` a `D01-E05`)

### `D01-E01` *(Leitura e Análise de Memória)*
1. `a[0] = 3`, `a[1] = 8`, `a[2] = 1`, `a[3] = 0`, `a[4] = 0` *(inicialização parcial completa os restantes com `0`)*.
2. `b[0] = 0`, `b[1] = 0`, `b[2] = 0`, `b[3] = 0`. Já `c[0..2]` não foi inicializado, portanto contém **lixo de memória** (valores indeterminados).
3. Índices válidos de `a`: `0, 1, 2, 3, 4` (`0 <= i < 5`). `a[5] = 9;` invade uma posição **fora dos limites** do vetor (*out-of-bounds*), causando comportamento indefinido (sobrescreve memória vizinha).

### `D01-E02` *(Completar solução)*
- **`/* A */`:** `N`
- **`/* B */`:** `&v[i]`
- **`/* C */`:** `i += 2`
- **`/* D */`:** `N - 1`

### `D01-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `for (int i = 0; i <= N; i++)` acessa `v[N]` (`v[5]`), ultrapassando o limite `0 .. N - 1`. Correto: `i < N`.
  2. `scanf("%d", v[i]);` omite o operador de endereço `&`. Correto: `scanf("%d", &v[i]);`.
  3. `for (int i = N; i > 0; i--)` começa fora do vetor (`v[N]`) e para antes de `v[0]`. Correto: `for (int i = N - 1; i >= 0; i--)`.
- **Solução corrigida completa:** [D01_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D01_E03_corrigido.c)
```c
#include <stdio.h>
#define N 5

int main(void) {
    int v[N];

    for (int i = 0; i < N; i++) {
        scanf("%d", &v[i]);
    }

    printf("Direta:");
    for (int i = 0; i < N; i++) {
        printf(" %d", v[i]);
    }
    printf("\nInversa:");
    for (int i = N - 1; i >= 0; i--) {
        printf(" %d", v[i]);
    }
    printf("\n");

    return 0;
}
```

### `D01-E04` *(Programa completo — Metade final e metade inicial)*
Arquivo: [D01_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D01_E04.c)
```c
#include <stdio.h>
#define N 6

int main(void) {
    int v[N];

    for (int i = 0; i < N; i++) {
        scanf("%d", &v[i]);
    }

    printf("Metade 2:");
    for (int i = N / 2; i < N; i++) {
        printf(" %d", v[i]);
    }
    printf("\nMetade 1:");
    for (int i = 0; i < N / 2; i++) {
        printf(" %d", v[i]);
    }
    printf("\n");

    return 0;
}
```

### `D01-E05` *(Programa completo — Leitura de `n` elementos e exibição direta/inversa)*
Arquivo: [D01_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D01_E05.c)
```c
#include <stdio.h>
#define MAX 50

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    printf("Direta:");
    for (int i = 0; i < n; i++) {
        printf(" %d", v[i]);
    }
    printf("\nInversa:");
    for (int i = n - 1; i >= 0; i--) {
        printf(" %d", v[i]);
    }
    printf("\n");

    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`D01-C01` a `D01-C03`)

### `D01-C01` *(Análise de Memória e Limites)*
1. `x[0] = 10`, `x[1] = 20`, `x[2] = 0`, `x[3] = 0`.
2. Índices válidos: `0` a `3` (`0 <= i <= TAM - 1`).
3. Erros:
   - `(a)` `int y[m];` usa uma variável como tamanho (VLA — proibida no curso; deve-se usar `#define TAM 4` e `int y[TAM];`).
   - `(b)` `x[4] = 99;` acessa posição além do último índice válido (`3`), gerando acesso fora dos limites (*out-of-bounds*).

### `D01-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `int v[n];` declara VLA com variável `n`. Correto: `int v[MAX];`.
  2. `scanf("%d", v[i]);` omite `&`. Correto: `scanf("%d", &v[i]);`.
  3. `for (int i = n; i >= 1; i--)` no percurso inverso acessa `v[n]` (fora dos limites) e deixa `v[0]` de fora. Correto: `for (int i = n - 1; i >= 0; i--)`.
- **Solução corrigida completa:** [D01_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D01_C02_corrigido.c)
```c
#include <stdio.h>
#define MAX 20

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    printf("Impares:");
    for (int i = 1; i < n; i += 2) {
        printf(" %d", v[i]);
    }
    printf("\nInverso:");
    for (int i = n - 1; i >= 0; i--) {
        printf(" %d", v[i]);
    }
    printf("\n");

    return 0;
}
```

### `D01-C03` *(Programa completo — Extremos posicionais e inverso)*
Arquivo: [D01_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D01_C03.c)
```c
#include <stdio.h>
#define MAX 50

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    printf("Primeiro: %d | Ultimo: %d\n", v[0], v[n - 1]);
    printf("Inverso:");
    for (int i = n - 1; i >= 0; i--) {
        printf(" %d", v[i]);
    }
    printf("\n");

    return 0;
}
```
