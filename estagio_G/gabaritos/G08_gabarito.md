# Gabarito Comentado — Bloco `G08` (Recursão Múltipla vs. Divisão pela Metade)

> **Bloco de referência:** [G08_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/blocos/G08_bloco.md)  
> **Nota para Caça ao Bug:** `G08-E03` no bloco do aluno contém **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`G08-E01` a `G08-E06`)

### `G08-E01` *(Árvore de Chamadas — `fib(5)`)*
- **Árvore resumida:** `fib(5)` chama `fib(4)` (9 chamadas) e `fib(3)` (5 chamadas).
- **(a)** Total de chamadas: `1 + 9 + 5 =` **`15`** chamadas.
- **(b)** Recomputações:
  - `fib(3)`: **2 vezes**
  - `fib(2)`: **3 vezes**
  - `fib(1)`: **5 vezes**
  - `fib(0)`: **3 vezes**
- **(c)** Valor retornado: **`5`**.

### `G08-E02` *(Completar solução e análise — `potencia_rapida`)*
- **`/* A */`:** `potencia_rapida(x, n / 2)`
- **`/* B */`:** `p * p`
- **`/* C */`:** `x * p * p`
- **(d)** Rastreamento de `potencia_rapida(3.0, 5)`:
  1. `n = 5` (ímpar): chama `n = 2`
  2. `n = 2` (par): chama `n = 1`
  3. `n = 1` (base): retorna `3.0`
  4. Volta para `n = 2` (`p = 3.0`): retorna `3.0 * 3.0 = 9.0`
  5. Volta para `n = 5` (`p = 9.0`): retorna `3.0 * 9.0 * 9.0 = 243.0` (total: **3 chamadas**).
  - **Comparação (casos base `n == 0` e `n == 1`):**
    - `n = 32`: `pot_linear` faz **`32`** chamadas (`32..1`); `potencia_rapida` faz **`6`** chamadas (`32 -> 16 -> 8 -> 4 -> 2 -> 1`).
    - `n = 1024`: `pot_linear` faz **`1024`** chamadas; `potencia_rapida` faz **`11`** chamadas (`1024 -> 512 -> 256 -> 128 -> 64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1`).

### `G08-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. Em `fib`, faltava o segundo caso base `if (n == 1) return 1;`, causando chamadas negativas infinitas e *stack overflow*.
  2. Em `potencia_rapida`, no caso par fazia `potencia_rapida(x, n / 2, chamadas) * potencia_rapida(x, n / 2, chamadas)`, duplicando a chamada recursiva em vez de guardar `double p = potencia_rapida(x, n / 2, chamadas);`.
  3. No caso ímpar de `potencia_rapida`, retornava `x * p` em vez de `x * p * p`.
- **Solução corrigida completa:** [G08_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G08_E03_corrigido.c)
```c
#include <stdio.h>

int fib(int n);
double potencia_rapida(double x, int n, int *chamadas);

int main(void) {
    double x;
    int n, k, chamadas = 0;
    scanf("%lf %d %d", &x, &n, &k);

    double res = potencia_rapida(x, n, &chamadas);
    printf("Potencia: %.2f\n", res);
    printf("Chamadas: %d\n", chamadas);
    printf("Fib: %d\n", fib(k));
    return 0;
}

int fib(int n) {
    if (n == 0) {
        return 0;
    }
    // Erro original 1: faltava o segundo caso base (n == 1), causando recursao infinita para n >= 1.
    // Correcao: retornar 1 quando n == 1.
    if (n == 1) {
        return 1;
    }
    return fib(n - 1) + fib(n - 2);
}

double potencia_rapida(double x, int n, int *chamadas) {
    (*chamadas)++;
    if (n == 0) {
        return 1.0;
    }
    if (n == 1) {
        return x;
    }
    // Erro original 2: chamava potencia_rapida(x, n / 2, chamadas) duas vezes, destruindo o ganho logaritmico.
    // Correcao: guardar o retorno em uma unica variavel local p.
    double p = potencia_rapida(x, n / 2, chamadas);
    if (n % 2 == 0) {
        return p * p;
    }
    // Erro original 3: no caso impar retornava x * p em vez de x * p * p.
    // Correcao: multiplicar x * p * p quando n eh impar.
    return x * p * p;
}
```

### `G08-E04` *(Programa completo — Contador de chamadas em Fibonacci)*
Arquivo: [G08_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G08_E04.c)
```c
#include <stdio.h>

int fib_contado(int n, int *chamadas);

int main(void) {
    int n, chamadas = 0;
    scanf("%d", &n);

    int f = fib_contado(n, &chamadas);
    printf("Fib: %d\n", f);
    printf("Chamadas: %d\n", chamadas);
    return 0;
}

int fib_contado(int n, int *chamadas) {
    (*chamadas)++;
    if (n == 0) {
        return 0;
    }
    if (n == 1) {
        return 1;
    }
    return fib_contado(n - 1, chamadas) + fib_contado(n - 2, chamadas);
}
```

### `G08-E05` *(Programa completo — Potenciação linear vs. rápida)*
Arquivo: [G08_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G08_E05.c)
```c
#include <stdio.h>

double pot_linear(double x, int n, int *chamadas);
double pot_rapida(double x, int n, int *chamadas);

int main(void) {
    double x;
    int n, c_lin = 0, c_rap = 0;
    scanf("%lf %d", &x, &n);

    pot_linear(x, n, &c_lin);
    double r = pot_rapida(x, n, &c_rap);

    printf("Resultado: %.2f\n", r);
    printf("Chamadas linear: %d\n", c_lin);
    printf("Chamadas rapida: %d\n", c_rap);
    return 0;
}

double pot_linear(double x, int n, int *chamadas) {
    (*chamadas)++;
    if (n == 0) {
        return 1.0;
    }
    if (n == 1) {
        return x;
    }
    return x * pot_linear(x, n - 1, chamadas);
}

double pot_rapida(double x, int n, int *chamadas) {
    (*chamadas)++;
    if (n == 0) {
        return 1.0;
    }
    if (n == 1) {
        return x;
    }
    double p = pot_rapida(x, n / 2, chamadas);
    if (n % 2 == 0) {
        return p * p;
    }
    return x * p * p;
}
```

### `G08-E06` *(Programa completo — Potenciação rápida com expoentes negativos/positivos)*
Arquivo: [G08_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G08_E06.c)
```c
#include <stdio.h>

double potencia_rapida(double x, int n, int *mult);

int main(void) {
    double x;
    int n, mult = 0;
    scanf("%lf %d", &x, &n);

    double res = potencia_rapida(x, n, &mult);
    printf("Potencia: %.2f\n", res);
    printf("Multiplicacoes: %d\n", mult);
    return 0;
}

double potencia_rapida(double x, int n, int *mult) {
    if (n < 0) {
        return 1.0 / potencia_rapida(x, -n, mult);
    }
    if (n == 0) {
        return 1.0;
    }
    if (n == 1) {
        return x;
    }
    double p = potencia_rapida(x, n / 2, mult);
    if (n % 2 == 0) {
        (*mult) += 1;
        return p * p;
    }
    (*mult) += 2;
    return x * p * p;
}
```

---

## 2. Gabarito da Checagem Independente (`G08-C01` a `G08-C03`)

### `G08-C01` *(Árvore de chamadas e recomputação)*
- **(a)** `g(4)` chama `g(3)` e `g(2)`; `g(3)` chama `g(2)` e `g(1)`; cada `g(2)` chama `g(1)` e `g(0)`.
- **(b)**
  - `g(0)=1`, `g(1)=1`, `g(2)=1+1+1=3`, `g(3)=3+1+1=5`, `g(4)=5+3+1=` **`9`**.
  - Total de chamadas: **`9`** (`g(4)` 1x, `g(3)` 1x, `g(2)` **2 vezes**, `g(1)` **3 vezes**, `g(0)` 2x).

### `G08-C02` *(Rastreamento e análise de dupla chamada)*
1. **`potencia_rapida(3.0, 6)`:**
   - `n=6` → chama `n=3` → chama `n=1` (base, retorna `3.0`).
   - `n=3` (`p=3.0`, ímpar): retorna `3.0 * 3.0 * 3.0 = 27.0`.
   - `n=6` (`p=27.0`, par): retorna `27.0 * 27.0 = 729.0`.
   - Total: **3 chamadas**.
   **`potencia_rapida(2.0, 5)`:**
   - `n=5` → chama `n=2` → chama `n=1` (base, retorna `2.0`).
   - `n=2` (`p=2.0`, par): retorna `2.0 * 2.0 = 4.0`.
   - `n=5` (`p=4.0`, ímpar): retorna `2.0 * 4.0 * 4.0 = 32.0`.
   - Total: **3 chamadas**.
2. Chamar `potencia_rapida(x, n / 2)` duas vezes na mesma expressão faz cada nó gerar **2 filhos idênticos**, criando uma árvore binária com ~$n$ chamadas (tempo linear/exponencial na altura) em vez de uma única cadeia com $\approx \log_2 n$ chamadas.

### `G08-C03` *(Programa completo — Fibonacci + Potenciação rápida)*
Arquivo: [G08_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G08_C03.c)
```c
#include <stdio.h>

int fib(int n);
double potencia_rapida(double x, int n, int *chamadas);

int main(void) {
    double x;
    int n, k, chamadas = 0;
    scanf("%lf %d %d", &x, &n, &k);

    double pot = potencia_rapida(x, n, &chamadas);
    printf("Potencia: %.2f\n", pot);
    printf("Chamadas: %d\n", chamadas);
    printf("Fib(K): %d\n", fib(k));
    return 0;
}

int fib(int n) {
    if (n == 0) {
        return 0;
    }
    if (n == 1) {
        return 1;
    }
    return fib(n - 1) + fib(n - 2);
}

double potencia_rapida(double x, int n, int *chamadas) {
    (*chamadas)++;
    if (n == 0) {
        return 1.0;
    }
    if (n == 1) {
        return x;
    }
    double p = potencia_rapida(x, n / 2, chamadas);
    if (n % 2 == 0) {
        return p * p;
    }
    return x * p * p;
}
```
