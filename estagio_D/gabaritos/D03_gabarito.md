# Gabarito Comentado — Bloco `D03` (Busca Linear, Inversão *In-Place* e Particionamento)

> **Bloco de referência:** [D03_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/blocos/D03_bloco.md)  
> **Nota para Caça ao Bug:** `D03-E03` e `D03-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`D03-E01` a `D03-E06`)

### `D03-E01` *(Teste de Mesa — Inversão `n / 2` vs `n`)*
1. Para `v = {10, 20, 30, 40, 50}` (`n = 5`):
   - **(a) Com `i < 5 / 2` (`i < 2`):**
     - `i = 0`: troca `v[0]` e `v[4]` → `{50, 20, 30, 40, 10}`
     - `i = 1`: troca `v[1]` e `v[3]` → `{50, 40, 30, 20, 10}`
     - Final: **`{50, 40, 30, 20, 10}`** *(correto!)*.
   - **(b) Com `i < 5` (bug):**
     - `i = 0`: `{50, 20, 30, 40, 10}`
     - `i = 1`: `{50, 40, 30, 20, 10}`
     - `i = 2`: troca `v[2]` com `v[2]` → `{50, 40, 30, 20, 10}`
     - `i = 3`: troca `v[3]` com `v[1]` → `{50, 20, 30, 40, 10}`
     - `i = 4`: troca `v[4]` com `v[0]` → **`{10, 20, 30, 40, 50}`** *(destrocou tudo de volta ao original!)*.
2. Para `u = {1, 2, 3, 4}` (`n = 4`, `i < 2`):
   - `i = 0`: `{4, 2, 3, 1}`; `i = 1`: **`{4, 3, 2, 1}`**.

### `D03-E02` *(Completar solução)*
- **`/* A */`:** `0`
- **`/* B */`:** `k1++`
- **`/* C */`:** `k2++`
- **`/* D */`:** `k1`

### `D03-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `int pos = 0;` confunde "não encontrado" com o índice `0`. Correto: `int pos = -1;`.
  2. Falta `break;` dentro do `if (v[i] == x)`: o laço continua e sobrescreve `pos` com a **última** ocorrência em vez da **1ª**. Correto: `pos = i; break;`.
  3. `for (int i = 0; i < n; i++)` na inversão troca cada par duas vezes, restaurando `v` ao estado original. Correto: `for (int i = 0; i < n / 2; i++)`.
- **Solução corrigida completa:** [D03_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D03_E03_corrigido.c)
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, x, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &x);

    int pos = -1;
    for (int i = 0; i < n; i++) {
        if (v[i] == x) {
            pos = i;
            break;
        }
    }

    for (int i = 0; i < n / 2; i++) {
        int aux = v[i];
        v[i] = v[n - 1 - i];
        v[n - 1 - i] = aux;
    }

    printf("Indice: %d\nInvertido:", pos);
    for (int i = 0; i < n; i++) {
        printf(" %d", v[i]);
    }
    printf("\n");
    return 0;
}
```

### `D03-E04` *(Programa completo — Elemento mais próximo de `x`)*
Arquivo: [D03_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D03_E04.c)
```c
#include <stdio.h>
#include <stdlib.h>
#define MAX 100

int main(void) {
    int n, x, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &x);

    int melhor_dist = abs(v[0] - x);
    int pos_melhor = 0;
    for (int i = 1; i < n; i++) {
        int d = abs(v[i] - x);
        if (d < melhor_dist) {
            melhor_dist = d;
            pos_melhor = i;
        }
    }

    printf("Mais proximo: %d (indice %d, distancia %d)\n",
           v[pos_melhor], pos_melhor, melhor_dist);
    return 0;
}
```

### `D03-E05` *(Programa completo — Particionamento em pares e ímpares)*
Arquivo: [D03_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D03_E05.c)
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int pares[MAX], impares[MAX];
    int k_par = 0, k_imp = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] % 2 == 0) {
            pares[k_par++] = v[i];
        } else {
            impares[k_imp++] = v[i];
        }
    }

    printf("Pares (%d):", k_par);
    if (k_par == 0) {
        printf(" nenhum");
    } else {
        for (int i = 0; i < k_par; i++) {
            printf(" %d", pares[i]);
        }
    }
    printf("\n");

    printf("Impares (%d):", k_imp);
    if (k_imp == 0) {
        printf(" nenhum");
    } else {
        for (int i = 0; i < k_imp; i++) {
            printf(" %d", impares[i]);
        }
    }
    printf("\n");

    return 0;
}
```

### `D03-E06` *(Programa completo — Inversão + média + particionamento)*
Arquivo: [D03_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D03_E06.c)
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    for (int i = 0; i < n / 2; i++) {
        int aux = v[i];
        v[i] = v[n - 1 - i];
        v[n - 1 - i] = aux;
    }

    int soma = 0;
    for (int i = 0; i < n; i++) {
        soma += v[i];
    }
    double media = (double)soma / n;

    int abaixo[MAX], acima_ig[MAX];
    int k_ab = 0, k_ac = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] < media) {
            abaixo[k_ab++] = v[i];
        } else {
            acima_ig[k_ac++] = v[i];
        }
    }

    printf("Invertido:");
    for (int i = 0; i < n; i++) {
        printf(" %d", v[i]);
    }
    printf("\nMedia: %.2f\n", media);

    printf("Abaixo (%d):", k_ab);
    if (k_ab == 0) {
        printf(" nenhum");
    } else {
        for (int i = 0; i < k_ab; i++) {
            printf(" %d", abaixo[i]);
        }
    }
    printf("\n");

    printf("Acima ou igual (%d):", k_ac);
    if (k_ac == 0) {
        printf(" nenhum");
    } else {
        for (int i = 0; i < k_ac; i++) {
            printf(" %d", acima_ig[i]);
        }
    }
    printf("\n");

    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`D03-C01` a `D03-C03`)

### `D03-C01` *(Teste de Mesa)*
Início: `v = {9, 7, 5, 3}`:
- `i = 0`: troca `v[0]` e `v[3]` → `{3, 7, 5, 9}`
- `i = 1`: troca `v[1]` e `v[2]` → `{3, 5, 7, 9}`
- `i = 2`: troca `v[2]` e `v[1]` → `{3, 7, 5, 9}`
- `i = 3`: troca `v[3]` e `v[0]` → `{9, 7, 5, 3}`
- **Explicação:** como cada passo troca um elemento da primeira metade com seu simétrico na segunda metade, passar de `n / 2` desfaz todas as trocas já realizadas. O limite correto é `i < n / 2`.

### `D03-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `break;` dentro do laço de ocorrências interrompe na 1ª ocorrência, impedindo listar **todas** as ocorrências. Correto: remover `break;`.
  2. `v[0] - alvo` e `v[i] - alvo` calculam diferença com sinal em vez da distância absoluta (um valor muito menor que `alvo` gera distância negativa e vence erroneamente!). Correto: usar `abs(...)` ou `if (d < 0) d = -d;`.
  3. `if (d <= melhor_dist)` escolhe a **última** ocorrência em caso de empate, quando o pedido é a **1ª ocorrência** (menor índice). Correto: `if (d < melhor_dist)`.
- **Solução corrigida completa:** [D03_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D03_C02_corrigido.c)
```c
#include <stdio.h>
#include <stdlib.h>
#define MAX 100

int main(void) {
    int n, alvo, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &alvo);

    int qtd = 0;
    printf("Ocorrencias:");
    for (int i = 0; i < n; i++) {
        if (v[i] == alvo) {
            printf(" %d", i);
            qtd++;
        }
    }
    if (qtd == 0) {
        printf(" nenhuma");
    }
    printf("\n");

    int melhor_dist = abs(v[0] - alvo);
    int pos_melhor = 0;
    for (int i = 1; i < n; i++) {
        int d = abs(v[i] - alvo);
        if (d < melhor_dist) {
            melhor_dist = d;
            pos_melhor = i;
        }
    }

    printf("Mais proximo: %d (indice %d)\n", v[pos_melhor], pos_melhor);
    return 0;
}
```

### `D03-C03` *(Programa completo — Particionamento por limiar com inversão seletiva)*
Arquivo: [D03_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D03_C03.c)
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, limiar, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &limiar);

    int menores[MAX], maiores_ig[MAX];
    int k_men = 0, k_mai = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] < limiar) {
            menores[k_men++] = v[i];
        } else {
            maiores_ig[k_mai++] = v[i];
        }
    }

    for (int i = 0; i < k_men / 2; i++) {
        int aux = menores[i];
        menores[i] = menores[k_men - 1 - i];
        menores[k_men - 1 - i] = aux;
    }

    printf("Menores invertidos (%d):", k_men);
    if (k_men == 0) {
        printf(" nenhum");
    } else {
        for (int i = 0; i < k_men; i++) {
            printf(" %d", menores[i]);
        }
    }
    printf("\n");

    printf("Maiores ou iguais (%d):", k_mai);
    if (k_mai == 0) {
        printf(" nenhum");
    } else {
        for (int i = 0; i < k_mai; i++) {
            printf(" %d", maiores_ig[i]);
        }
    }
    printf("\n");

    return 0;
}
```
