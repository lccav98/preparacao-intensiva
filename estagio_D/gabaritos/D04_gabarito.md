# Gabarito Comentado — Bloco `D04` (Vetores de Frequência e Deduplicação)

> **Bloco de referência:** [D04_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/blocos/D04_bloco.md)  
> **Nota para Caça ao Bug:** `D04-E03` e `D04-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`D04-E01` a `D04-E05`)

### `D04-E01` *(Teste de Mesa)*
1. Para `v = {3, 0, 3, 2, 0, 3, 1}`:
   - `freq[0] = 2`, `freq[1] = 1`, `freq[2] = 1`, `freq[3] = 3`.
2. Para `u = {-4, 10, -4, 7, 10}`:
   - `i = 0 (-4)`: prefixo vazio (`j < 0`), `repetido = 0` → aceito (`unicos[0] = -4`).
   - `i = 1 (10)`: testa `j = 0 (-4 != 10)`, `repetido = 0` → aceito (`unicos[1] = 10`).
   - `i = 2 (-4)`: testa `j = 0 (-4 == -4)`, `repetido = 1` → descartado.
   - `i = 3 (7)`: testa `j = 0, 1, 2`, `repetido = 0` → aceito (`unicos[2] = 7`).
   - `i = 4 (10)`: testa `j = 0` (`-4 != 10`), `j = 1` (`10 == 10`), `repetido = 1` → descartado.
   - Vetor final: **`unicos = {-4, 10, 7}`** (`k = 3`).

### `D04-E02` *(Completar solução)*
- **`/* A */`:** `{0}`
- **`/* B */`:** `a[i]`
- **`/* C */`:** `b[i]`
- **`/* D */`:** `fa[d] != fb[d]`

### `D04-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `int repetido = 0;` está **fora** do laço `for (int i = 0; i < n; i++)`: depois que encontra um repetido, nunca volta a `0`. Correto: declarar/reiniciar `int repetido = 0;` **dentro** do laço `i`.
  2. `for (int j = 0; j <= i; j++)` usa `<= i`, comparando `v[i]` consigo mesmo (`v[i] == v[i]` sempre verdadeiro!). Correto: `j < i`.
  3. `unicos[i] = v[i];` escreve na posição `i` em vez da próxima posição livre `k` (`unicos[k++] = v[i];`), deixando lixo nas posições puladas!
- **Solução corrigida completa:** [D04_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D04_E03_corrigido.c)
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int unicos[MAX], k = 0;
    for (int i = 0; i < n; i++) {
        int repetido = 0;
        for (int j = 0; j < i; j++) {
            if (v[j] == v[i]) {
                repetido = 1;
                break;
            }
        }
        if (repetido == 0) {
            unicos[k++] = v[i];
        }
    }

    printf("Unicos (%d):", k);
    for (int i = 0; i < k; i++) {
        printf(" %d", unicos[i]);
    }
    printf("\n");
    return 0;
}
```

### `D04-E04` *(Programa completo — Histograma com asteriscos)*
Arquivo: [D04_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D04_E04.c)
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int freq[10] = {0};
    for (int i = 0; i < n; i++) {
        freq[v[i]]++;
    }

    for (int d = 0; d < 10; d++) {
        if (freq[d] > 0) {
            printf("%d: ", d);
            for (int c = 0; c < freq[d]; c++) {
                printf("*");
            }
            printf("\n");
        }
    }
    return 0;
}
```

### `D04-E05` *(Programa completo — Comparação de histogramas e moda conjunta)*
Arquivo: [D04_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D04_E05.c)
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, a[MAX], b[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    for (int i = 0; i < n; i++) {
        scanf("%d", &b[i]);
    }

    int fa[10] = {0}, fb[10] = {0};
    for (int i = 0; i < n; i++) {
        fa[a[i]]++;
        fb[b[i]]++;
    }

    int iguais = 1;
    for (int d = 0; d < 10; d++) {
        if (fa[d] != fb[d]) {
            iguais = 0;
            break;
        }
    }

    int melhor = 0;
    int maior_total = fa[0] + fb[0];
    for (int d = 1; d < 10; d++) {
        int total = fa[d] + fb[d];
        if (total > maior_total) {
            maior_total = total;
            melhor = d;
        }
    }

    if (iguais) {
        printf("Mesmo histograma\n");
    } else {
        printf("Histogramas diferentes\n");
    }
    printf("Mais frequente: %d (total %d)\n", melhor, maior_total);
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`D04-C01` a `D04-C03`)

### `D04-C01` *(Teste de Mesa)*
- `freq[0] = 1`
- `freq[1] = 2`
- `freq[2] = 0`
- `freq[3] = 0`
- `freq[4] = 3`
- Valor com maior frequência: **`4`** (3 ocorrências).

### `D04-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `int freq[6];` não foi inicializado com `{0}`, contendo lixo de memória. Correto: `int freq[6] = {0};`.
  2. `freq[i]++;` indexa pela posição `i` (além de poder invadir além de `freq[5]` se `n > 6`) em vez do valor `v[i]`. Correto: `freq[v[i]]++;`.
  3. `for (int k = 0; k < 5; k++)` deixa de imprimir a nota `5`. Correto: `k <= 5` (ou `k < 6`).
- **Solução corrigida completa:** [D04_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D04_C02_corrigido.c)
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int freq[6] = {0};
    for (int i = 0; i < n; i++) {
        freq[v[i]]++;
    }

    for (int k = 0; k <= 5; k++) {
        printf("Nota %d: %d\n", k, freq[k]);
    }
    return 0;
}
```

### `D04-C03` *(Programa completo — Deduplicação e contagem de removidos)*
Arquivo: [D04_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D04_C03.c)
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int unicos[MAX], k = 0;
    for (int i = 0; i < n; i++) {
        int repetido = 0;
        for (int j = 0; j < i; j++) {
            if (v[j] == v[i]) {
                repetido = 1;
                break;
            }
        }
        if (repetido == 0) {
            unicos[k++] = v[i];
        }
    }

    printf("Unicos (%d):", k);
    for (int i = 0; i < k; i++) {
        printf(" %d", unicos[i]);
    }
    printf("\nRepetidos removidos: %d\n", n - k);
    return 0;
}
```
