# Gabarito Comentado — Bloco `G04` (Recursão Linear em Vetores 1D: Redução por Tamanho `n - 1`)

> **Bloco de referência:** [G04_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/blocos/G04_bloco.md)  
> **Nota para Caça ao Bug:** `G04-E03` e `G04-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`G04-E01` a `G04-E05`)

### `G04-E01` *(Teste de mesa — `calcular(v, 3)` com `{5, 2, 7}`)*
- **(a)** Descida na pilha:
  1. `calcular(v, 3)`: inspeciona `v[2] = 7` (ímpar) → aguarda `7 + calcular(v, 2)`
  2. `calcular(v, 2)`: inspeciona `v[1] = 2` (par) → aguarda `calcular(v, 1)`
  3. `calcular(v, 1)`: inspeciona `v[0] = 5` (ímpar) → aguarda `5 + calcular(v, 0)`
  4. `calcular(v, 0)`: atinge `n <= 0` → retorna `0`
- **(b)** Subida na pilha: `0` → `5 + 0 = 5` → `5` → `7 + 5 = 12`. Resultado final: **`12`**.

### `G04-E02` *(Completar lacunas — `contar_negativos`)*
- **`/* A */`:** `const int v[]`
- **`/* B */`:** `n <= 0` *(ou `n == 0`)*
- **`/* C */`:** `v[n - 1] < 0`

### `G04-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. Caso base errado `if (n == 1) return v[0];`: falha para vetor vazio (`n == 0`, gerando *stack overflow* por descer para `-1, -2...`) e retorna `v[0]` mesmo quando `v[0] <= 0` (por exemplo, somaria um número negativo). O correto é `if (n <= 0) return 0;`.
  2. Índice errado `v[n]`: os elementos válidos vão de `0` até `n - 1`; acessar `v[n]` lê posição fora do subvetor considerado. O correto é `v[n - 1]`.
- **Solução corrigida completa:** [G04_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G04_E03_corrigido.c)
```c
#include <stdio.h>

int soma_positivos(const int v[], int n);

int main(void) {
    int n, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    printf("Soma positivos: %d\n", soma_positivos(v, n));
    return 0;
}

int soma_positivos(const int v[], int n) {
    // Bug 1 original: caso base n == 1 retornava v[0] mesmo negativo e falhava para n == 0.
    if (n <= 0) {
        return 0;
    }
    // Bug 2 original: acessava v[n] fora dos limites em vez do ultimo elemento v[n - 1].
    if (v[n - 1] > 0) {
        return v[n - 1] + soma_positivos(v, n - 1);
    }
    return soma_positivos(v, n - 1);
}
```

### `G04-E04` *(Programa completo — `contar_positivos` e `soma_pares`)*
Arquivo: [G04_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G04_E04.c)
```c
#include <stdio.h>

int contar_positivos(const int v[], int n);
int soma_pares(const int v[], int n);

int main(void) {
    int n, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    printf("Positivos: %d\n", contar_positivos(v, n));
    printf("Soma pares: %d\n", soma_pares(v, n));
    return 0;
}

int contar_positivos(const int v[], int n) {
    if (n <= 0) {
        return 0;
    }
    if (v[n - 1] > 0) {
        return 1 + contar_positivos(v, n - 1);
    }
    return contar_positivos(v, n - 1);
}

int soma_pares(const int v[], int n) {
    if (n <= 0) {
        return 0;
    }
    if (v[n - 1] % 2 == 0) {
        return v[n - 1] + soma_pares(v, n - 1);
    }
    return soma_pares(v, n - 1);
}
```

### `G04-E05` *(Programa completo — `contar_ocorrencias`)*
Arquivo: [G04_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G04_E05.c)
```c
#include <stdio.h>

int contar_ocorrencias(const int v[], int n, int x);

int main(void) {
    int n, x, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &x);
    printf("Ocorrencias: %d\n", contar_ocorrencias(v, n, x));
    return 0;
}

int contar_ocorrencias(const int v[], int n, int x) {
    if (n <= 0) {
        return 0;
    }
    if (v[n - 1] == x) {
        return 1 + contar_ocorrencias(v, n - 1, x);
    }
    return contar_ocorrencias(v, n - 1, x);
}
```

---

## 2. Gabarito da Checagem Independente (`G04-C01` a `G04-C03`)

### `G04-C01` *(Rastreamento — `soma_multiplos(v, 4, 3)` com `{3, 10, 6, 5}`)*
- **Descida:**
  - `soma_multiplos(v, 4, 3)`: `v[3] = 5` (`5 % 3 != 0`) → `soma_multiplos(v, 3, 3)`
  - `soma_multiplos(v, 3, 3)`: `v[2] = 6` (`6 % 3 == 0`) → `6 + soma_multiplos(v, 2, 3)`
  - `soma_multiplos(v, 2, 3)`: `v[1] = 10` (`10 % 3 != 0`) → `soma_multiplos(v, 1, 3)`
  - `soma_multiplos(v, 1, 3)`: `v[0] = 3` (`3 % 3 == 0`) → `3 + soma_multiplos(v, 0, 3)`
  - `soma_multiplos(v, 0, 3)`: `n <= 0` → retorna `0`.
- **Subida:** `0` → `3 + 0 = 3` → `3` → `6 + 3 = 9` → `9`. Resultado final: **`9`**.

### `G04-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. Lê `v[n]` **antes** de verificar `if (n <= 0) return 0;`: quando `n == 0`, acessaria posição inválida antes de retornar (e mesmo com `v[n - 1]`, leria `v[-1]`).
  2. Usa o índice `v[n]` em vez de `v[n - 1]`.
- **Solução corrigida completa:** [G04_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G04_C02_corrigido.c)
```c
#include <stdio.h>

int contar_acima(const int v[], int n, int lim);

int main(void) {
    int n, lim, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &lim);
    printf("Acima: %d\n", contar_acima(v, n, lim));
    return 0;
}

int contar_acima(const int v[], int n, int lim) {
    // Bug 1 original: acessava o vetor ANTES de testar if (n <= 0) (risco de v[-1]).
    if (n <= 0) {
        return 0;
    }
    // Bug 2 original: acessava v[n] em vez de v[n - 1].
    int ult = v[n - 1];
    if (ult > lim) {
        return 1 + contar_acima(v, n - 1, lim);
    }
    return contar_acima(v, n - 1, lim);
}
```

### `G04-C03` *(Programa completo — `soma_intervalo_vetor`)*
Arquivo: [G04_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G04_C03.c)
```c
#include <stdio.h>

int soma_intervalo_vetor(const int v[], int n, int min_val, int max_val);

int main(void) {
    int n, min_val, max_val, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d %d", &min_val, &max_val);
    printf("Soma no intervalo: %d\n", soma_intervalo_vetor(v, n, min_val, max_val));
    return 0;
}

int soma_intervalo_vetor(const int v[], int n, int min_val, int max_val) {
    if (n <= 0) {
        return 0;
    }
    if (v[n - 1] >= min_val && v[n - 1] <= max_val) {
        return v[n - 1] + soma_intervalo_vetor(v, n - 1, min_val, max_val);
    }
    return soma_intervalo_vetor(v, n - 1, min_val, max_val);
}
```
