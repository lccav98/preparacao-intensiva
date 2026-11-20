# Gabarito Comentado — Bloco `G05` (Parada Antecipada, Máximo Sem Dupla Chamada e Média Recursiva)

> **Bloco de referência:** [G05_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/blocos/G05_bloco.md)  
> **Nota para Caça ao Bug:** `G05-E03` no bloco do aluno contém **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`G05-E01` a `G05-E06`)

### `G05-E01` *(Teste de mesa — Parada antecipada em `contem`)*
- **(a) `contem(v, 5, 12)` para `{4, 9, 12, 7, 3}`:**
  1. `contem(v, 5, 12)`: `v[4] = 3 != 12` → chama `contem(v, 4, 12)`
  2. `contem(v, 4, 12)`: `v[3] = 7 != 12` → chama `contem(v, 3, 12)`
  3. `contem(v, 3, 12)`: `v[2] = 12 == 12` → **para antecipadamente e retorna `1`**
  - Subida: retorna `1` direto até o chamador inicial. **Total: 3 chamadas.**
- **(b) `contem(v, 5, 15)`:**
  - Percorre `n = 5` (`3`), `n = 4` (`7`), `n = 3` (`12`), `n = 2` (`9`), `n = 1` (`4`) até atingir `n = 0` (`n <= 0`), onde retorna `0`.
  - **Total: 6 chamadas** (o dobro do caso **(a)**, pois precisou chegar até `n = 0`).

### `G05-E02` *(Análise de explosão de chamadas — `maior_A` vs. `maior_B`)*
- **(a) Para `n = 4` (`{40, 30, 20, 10}`):**
  - `maior_A(v, 4)` faz apenas **4 chamadas**: `n = 4 -> 3 -> 2 -> 1`.
  - `maior_B(v, 4)`: como cada elemento à direita é menor que todos à esquerda, o teste `v[n - 1] > maior_B(v, n - 1)` dá sempre **falso**, disparando **2 chamadas** de `n - 1` a cada nível:
    - 1 chamada de `n = 4` + 2 de `n = 3` + 4 de `n = 2` + 8 de `n = 1` = **15 chamadas** ($2^4 - 1 = 15$).
- **(b) Para `n = 20`:**
  - `maior_A`: **20 chamadas**.
  - `maior_B`: $2^{20} - 1 =$ **1.048.575 chamadas**!

### `G05-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. Em `maior_vetor`, o caso base `if (n == 0) return 0;` devolve `0` erroneamente quando todos os elementos são negativos (deve ser `if (n == 1) return v[0];`).
  2. Em `maior_vetor`, a chamada `maior_vetor(v, n - 1)` aparece duas vezes (`if` e `return`), gerando explosão exponencial $O(2^n)$ (deve ser guardada em `int m = maior_vetor(v, n - 1);`).
  3. Em `contem`, `v[n - 1] == x` é testado **antes** de `if (n <= 0) return 0;`, causando leitura inválida `v[-1]` quando `x` não está no vetor.
- **Solução corrigida completa:** [G05_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G05_E03_corrigido.c)
```c
#include <stdio.h>

int maior_vetor(const int v[], int n);
int contem(const int v[], int n, int x);

int main(void) {
    int n, x, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &x);
    printf("Maior: %d\n", maior_vetor(v, n));
    printf("Contem: %d\n", contem(v, n, x));
    return 0;
}

int maior_vetor(const int v[], int n) {
    // Bug 1 original: caso base n == 0 retornando 0 falhava quando todos eram negativos.
    if (n == 1) {
        return v[0];
    }
    // Bug 2 original: dupla chamada maior_vetor(v, n - 1) gerava custo O(2^n).
    int m = maior_vetor(v, n - 1);
    if (v[n - 1] > m) {
        return v[n - 1];
    }
    return m;
}

int contem(const int v[], int n, int x) {
    // Bug 3 original: testava v[n - 1] antes de verificar n <= 0 (acesso a v[-1]).
    if (n <= 0) {
        return 0;
    }
    if (v[n - 1] == x) {
        return 1;
    }
    return contem(v, n - 1, x);
}
```

### `G05-E04` *(Completar solução — `media_vetor`)*
- **`/* A */`:** `n == 1`
- **`/* B */`:** `(double)v[0]`
- **`/* C */`:** `(n - 1) * media_vetor(v, n - 1) + v[n - 1]`
- **Programa completo:** [G05_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G05_E04.c)
```c
#include <stdio.h>

double media_vetor(const int v[], int n);

int main(void) {
    int n, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    printf("Media: %.2f\n", media_vetor(v, n));
    return 0;
}

double media_vetor(const int v[], int n) {
    if (n == 1) {
        return (double)v[0];
    }
    return ((n - 1) * media_vetor(v, n - 1) + v[n - 1]) / n;
}
```

### `G05-E05` *(Programa completo — `menor_vetor` e `contem`)*
Arquivo: [G05_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G05_E05.c)
```c
#include <stdio.h>

int menor_vetor(const int v[], int n);
int contem(const int v[], int n, int x);

int main(void) {
    int n, x, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &x);
    printf("Menor: %d\n", menor_vetor(v, n));
    if (contem(v, n, x)) {
        printf("Encontrado: Sim\n");
    } else {
        printf("Encontrado: Nao\n");
    }
    return 0;
}

int menor_vetor(const int v[], int n) {
    if (n == 1) {
        return v[0];
    }
    int m = menor_vetor(v, n - 1);
    if (v[n - 1] < m) {
        return v[n - 1];
    }
    return m;
}

int contem(const int v[], int n, int x) {
    if (n <= 0) {
        return 0;
    }
    if (v[n - 1] == x) {
        return 1;
    }
    return contem(v, n - 1, x);
}
```

### `G05-E06` *(Programa completo — `maior_vetor` e `media_vetor`)*
Arquivo: [G05_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G05_E06.c)
```c
#include <stdio.h>

int maior_vetor(const int v[], int n);
double media_vetor(const int v[], int n);

int main(void) {
    int n, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    printf("Maior: %d\n", maior_vetor(v, n));
    printf("Media: %.2f\n", media_vetor(v, n));
    return 0;
}

int maior_vetor(const int v[], int n) {
    if (n == 1) {
        return v[0];
    }
    int m = maior_vetor(v, n - 1);
    if (v[n - 1] > m) {
        return v[n - 1];
    }
    return m;
}

double media_vetor(const int v[], int n) {
    if (n == 1) {
        return (double)v[0];
    }
    return ((n - 1) * media_vetor(v, n - 1) + v[n - 1]) / n;
}
```

---

## 2. Gabarito da Checagem Independente (`G05-C01` a `G05-C03`)

### `G05-C01` *(Análise comparativa 1 vs. 2 chamadas)*
- **(a)** No pior caso crescente para `menor`:
  - **Versão 1 (chamada única):** `n = 5` → **5 chamadas**; `n = 10` → **10 chamadas**.
  - **Versão 2 (dupla chamada):** `n = 5` → $2^5 - 1 =$ **31 chamadas**; `n = 10` → $2^{10} - 1 =$ **1023 chamadas**.
- **(b)** Porque `0` não é elemento do vetor; se o vetor contiver apenas valores positivos (para `menor`) ou apenas negativos (para `maior`), retornar `0` no caso base `n == 0` contaminaria o resultado com um falso `0` inexistente no vetor. Com `n == 1` retornando `v[0]`, a comparação ocorre sempre entre elementos reais do vetor.

### `G05-C02` *(Programa completo — `indice_ultimo`)*
Arquivo: [G05_C02.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G05_C02.c)
```c
#include <stdio.h>

int indice_ultimo(const int v[], int n, int x);

int main(void) {
    int n, x, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &x);
    printf("Indice: %d\n", indice_ultimo(v, n, x));
    return 0;
}

int indice_ultimo(const int v[], int n, int x) {
    if (n <= 0) {
        return -1;
    }
    if (v[n - 1] == x) {
        return n - 1;
    }
    return indice_ultimo(v, n - 1, x);
}
```

### `G05-C03` *(Programa completo — `media_vetor` e `contar_acima`)*
Arquivo: [G05_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G05_C03.c)
```c
#include <stdio.h>

double media_vetor(const int v[], int n);
int contar_acima(const int v[], int n, double lim);

int main(void) {
    int n, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    double m = media_vetor(v, n);
    printf("Media: %.2f\n", m);
    printf("Acima da media: %d\n", contar_acima(v, n, m));
    return 0;
}

double media_vetor(const int v[], int n) {
    if (n == 1) {
        return (double)v[0];
    }
    return ((n - 1) * media_vetor(v, n - 1) + v[n - 1]) / n;
}

int contar_acima(const int v[], int n, double lim) {
    if (n <= 0) {
        return 0;
    }
    if (v[n - 1] > lim) {
        return 1 + contar_acima(v, n - 1, lim);
    }
    return contar_acima(v, n - 1, lim);
}
```
