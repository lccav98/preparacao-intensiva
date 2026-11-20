# Gabarito Comentado — Bloco `F04` (Introdução a Ponteiros: `&`, `*`, `NULL` e Rastreamento de Memória)

> **Bloco de referência:** [F04_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/blocos/F04_bloco.md)  
> **Nota para Caça ao Bug:** `F04-E03` e `F04-C03` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`F04-E01` a `F04-E06`)

### `F04-E01` *(Teste de Mesa Intensivo com Endereços Simbólicos)*
Rastreamento passo a passo:
1. Inicialmente: `a = 5` (`0x100`), `b = 12` (`0x104`), `c = 30` (`0x108`), `p = 0x100` (`&a`), `q = 0x104` (`&b`).
2. `p = q;` → `p` passa a guardar `0x104` (`&b`).
3. `*p = 40;` → altera `b` (`0x104`) para `40`.
4. `q = &c;` → `q` passa a guardar `0x108` (`&c`).
5. `*q = *q - *p;` → `c = 30 - 40 = -10`.
6. `a = *p + *q;` → `a = 40 + (-10) = 30`.

Valores finais:
- `a = 30`, `&a = 0x100`
- `b = 40`, `&b = 0x104`
- `c = -10`, `&c = 0x108`
- `p = 0x104`, `*p = 40`, `&p = 0x200`
- `q = 0x108`, `*q = -10`, `&q = 0x204`

### `F04-E02` *(Completar solução)*
- **`/* A */`:** `*p`
- **`/* B */`:** `&y`
- **`/* C */`:** `*q`
- **`/* D */`:** `p = NULL`

### `F04-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `int *p; *p = x * 2;` desreferencia um ponteiro **não inicializado** (endereço indeterminado → comportamento indefinido), sem nunca apontar `p` para `x`. Correto: `int *p = &x; *p = (*p) * 2;`.
  2. `q = y;` tenta atribuir um inteiro `int` ao ponteiro `int *`, em vez do endereço `&y`. Correto: `q = &y;`.
  3. `*p = *p + *q;` desreferencia `q` mesmo quando `y <= 0` (caso em que `q == NULL`), causando falha de segmentação / comportamento indefinido. Correto: proteger com `if (q != NULL)`.
- **Solução corrigida completa:** [F04_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F04_E03_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int x, y;
    scanf("%d %d", &x, &y);

    // Erro 1 original: int *p; *p = x * 2; desreferenciava ponteiro nao inicializado.
    int *p = &x;
    *p = (*p) * 2;

    int *q = NULL;
    if (y > 0) {
        // Erro 2 original: q = y; atribuia um int ao ponteiro em vez do endereco &y.
        q = &y;
    }

    // Erro 3 original: *p = *p + *q; desreferenciava q mesmo quando q == NULL.
    if (q != NULL) {
        *p = *p + *q;
    }

    printf("%d\n", x);
    return 0;
}
```

### `F04-E04` *(Programa completo — Redirecionamento para menor e maior)*
Arquivo: [F04_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F04_E04.c)
```c
#include <stdio.h>

int main(void) {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);

    int *p_menor = &a;
    int *p_maior = &a;

    if (b < *p_menor) {
        p_menor = &b;
    }
    if (c < *p_menor) {
        p_menor = &c;
    }
    if (b > *p_maior) {
        p_maior = &b;
    }
    if (c > *p_maior) {
        p_maior = &c;
    }

    *p_menor = *p_menor + 10;
    printf("Valores: %d %d %d\nApontado por p_maior: %d\n", a, b, c, *p_maior);
    return 0;
}
```

### `F04-E05` *(Programa completo — Ordenação e igualdade via `*px` e `*py`)*
Arquivo: [F04_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F04_E05.c)
```c
#include <stdio.h>

int main(void) {
    int x, y;
    scanf("%d %d", &x, &y);

    int *px = &x;
    int *py = &y;

    if (*px > *py) {
        int aux = *px;
        *px = *py;
        *py = aux;
    }

    int iguais = 0;
    if (*px == *py) {
        iguais = 1;
    }

    printf("Iguais: %d\nOrdenados: %d %d\n", iguais, x, y);
    return 0;
}
```

### `F04-E06` *(Programa completo — Seleção condicional com `NULL`)*
Arquivo: [F04_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F04_E06.c)
```c
#include <stdio.h>

int main(void) {
    double a, b;
    int escolha;
    scanf("%lf %lf %d", &a, &b, &escolha);

    double *alvo = NULL;
    if (escolha == 1) {
        alvo = &a;
    } else if (escolha == 2) {
        alvo = &b;
    }

    if (alvo != NULL) {
        *alvo = (*alvo) * 1.10;
        printf("Atualizado: %.2f\n", *alvo);
    } else {
        printf("Ponteiro nulo\n");
    }
    printf("Valores: %.2f %.2f\n", a, b);
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`F04-C01` a `F04-C03`)

### `F04-C01` *(Teste de Mesa 1 — Redirecionamento)*
1. `a = 8, b = 15, p = 0x100` (`&a`).
2. `*p = 20;` → `a = 20`.
3. `p = &b;` → `p = 0x104`.
4. `*p = *p + a;` → `b = 15 + 20 = 35`.
5. `a = *p - 10;` → `a = 35 - 10 = 25`.

Valores finais:
- `a = 25`, `&a = 0x100`
- `b = 35`, `&b = 0x104`
- `p = 0x104`, `*p = 35`, `&p = 0x200`

### `F04-C02` *(Teste de Mesa 2 — Dois ponteiros no mesmo alvo)*
1. `x = 10, y = 4, p = 0x100 (&x), q = 0x100 (&x)`.
2. `*p = *p + 6;` → `x = 16` *(tanto `*p` quanto `*q` passam a ler `16`)* .
3. `*q = *q * 2;` → `x = 32` *(tanto `*p` quanto `*q` passam a ler `32`)* .
4. `q = &y;` → `q = 0x104`.
5. `*q = *p - *q;` → `y = 32 - 4 = 28`.

Valores finais:
- `x = 32`, `y = 28`
- `p = 0x100`, `*p = 32`, `&p = 0x200`
- `q = 0x104`, `*q = 28`, `&q = 0x204`

### `F04-C03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `int *p; *p = b + 5;` desreferencia ponteiro não inicializado (`p` contém endereço indeterminado e não aponta para `b`). Correto: `int *p = &b; *p = *p + 5;`.
  2. `*q = *q + *p;` desreferencia `q` sem verificar `q != NULL` (quando `cod != 1`, `q` vale `NULL` → comportamento indefinido). Correto: proteger com `if (q != NULL)`.
- **Solução corrigida completa:** [F04_C03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F04_C03_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int a, b, cod;
    scanf("%d %d %d", &a, &b, &cod);

    // Erro 1 original: int *p; *p = b + 5; desreferenciava ponteiro nao inicializado.
    int *p = &b;
    *p = *p + 5;

    int *q = NULL;
    if (cod == 1) {
        q = &a;
    }

    // Erro 2 original: *q = *q + *p; desreferenciava q mesmo quando q == NULL.
    if (q != NULL) {
        *q = *q + *p;
    }

    printf("%d %d\n", a, b);
    return 0;
}
```
