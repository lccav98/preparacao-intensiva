# Gabarito Comentado — Bloco `G03` (Recursão Linear sobre Inteiros e Decomposição Decimal)

> **Bloco de referência:** [G03_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/blocos/G03_bloco.md)  
> **Nota para Caça ao Bug:** `G03-E03` e `G03-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`G03-E01` a `G03-E05`)

### `G03-E01` *(Rastreamento e justificativa de terminação — `misterio(5832)`)*
- **(a)** Rastreamento na pilha:
  - **Descida:**
    - `misterio(5832)` → `2 + misterio(583)`
    - `misterio(583)` → `3 + misterio(58)`
    - `misterio(58)` → `8 + misterio(5)`
    - `misterio(5)` → atinge `n < 10`, retorna `5`
  - **Subida:** `misterio(5) = 5` → `misterio(58) = 8 + 5 = 13` → `misterio(583) = 3 + 13 = 16` → `misterio(5832) = 2 + 16 = 18`.
- **(b)** **Justificativa de terminação:** Para todo `n >= 0`, se `0 <= n < 10`, a função entra diretamente no caso base e retorna sem nova chamada. Se `n >= 10`, o passo recursivo chama `misterio(n / 10)`, e na divisão inteira temos $1 \le \lfloor n / 10 \rfloor < n$. Como o argumento é inteiro não-negativo e diminui estritamente a cada chamada, não pode decrescer infinitamente e inevitavelmente entra no intervalo `[0, 9]`, encerrando a recursão.

### `G03-E02` *(Completar solução — `potencia`)*
- **`/* A */`:** `n == 0`
- **`/* B */`:** `1`
- **`/* C */`:** `x * potencia(x, n - 1)`

### `G03-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. Em `contar_digitos`, `if (n == 0) return 0;` devolve `0` para a entrada `0` (quando `0` possui `1` dígito). O caso base correto é `if (n < 10) return 1;`.
  2. Em `potencia`, foi usado o laço `while`, violando a proibição de laços em funções recursivas. Deve ser substituído pelo caso base `e == 0 -> 1` e passo `x * potencia(x, e - 1)`.
- **Solução corrigida completa:** [G03_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G03_E03_corrigido.c)
```c
#include <stdio.h>

int contar_digitos(int n);
int potencia(int x, int e);

int main(void) {
    int n, x, e;
    scanf("%d %d %d", &n, &x, &e);
    printf("Digitos: %d\n", contar_digitos(n));
    printf("Potencia: %d\n", potencia(x, e));
    return 0;
}

int contar_digitos(int n) {
    // Bug 1 original: if (n == 0) return 0; retornava 0 para a entrada 0.
    // Correcao: qualquer inteiro 0..9 tem 1 digito.
    if (n < 10) {
        return 1;
    }
    return 1 + contar_digitos(n / 10);
}

int potencia(int x, int e) {
    // Bug 2 original: utilizava laco while em funcao que deve ser recursiva.
    if (e == 0) {
        return 1;
    }
    return x * potencia(x, e - 1);
}
```

### `G03-E04` *(Programa completo — Contar dígitos e somar dígitos pares)*
Arquivo: [G03_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G03_E04.c)
```c
#include <stdio.h>

int contar_digitos(int n);
int soma_digitos_pares(int n);

int main(void) {
    int n;
    scanf("%d", &n);
    printf("Digitos: %d\n", contar_digitos(n));
    printf("Soma digitos pares: %d\n", soma_digitos_pares(n));
    return 0;
}

int contar_digitos(int n) {
    if (n < 10) {
        return 1;
    }
    return 1 + contar_digitos(n / 10);
}

int soma_digitos_pares(int n) {
    if (n < 10) {
        if (n % 2 == 0) {
            return n;
        }
        return 0;
    }
    int d = n % 10;
    if (d % 2 == 0) {
        return d + soma_digitos_pares(n / 10);
    }
    return soma_digitos_pares(n / 10);
}
```

### `G03-E05` *(Programa completo — Produto e maior dígito sem laços)*
Arquivo: [G03_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G03_E05.c)
```c
#include <stdio.h>

int produto_digitos(int n);
int maior_digito(int n);

int main(void) {
    int n;
    scanf("%d", &n);
    printf("Produto: %d\n", produto_digitos(n));
    printf("Maior digito: %d\n", maior_digito(n));
    return 0;
}

int produto_digitos(int n) {
    if (n < 10) {
        return n;
    }
    return (n % 10) * produto_digitos(n / 10);
}

int maior_digito(int n) {
    if (n < 10) {
        return n;
    }
    int ult = n % 10;
    int resto = maior_digito(n / 10);
    if (ult > resto) {
        return ult;
    }
    return resto;
}
```

---

## 2. Gabarito da Checagem Independente (`G03-C01` a `G03-C03`)

### `G03-C01` *(Rastreamento e prova de terminação — `contar_altos(7409)`)*
- **Rastreamento:**
  - `contar_altos(7409)`: `9 >= 5` → `1 + contar_altos(740)`
  - `contar_altos(740)`: `0 < 5` → `contar_altos(74)`
  - `contar_altos(74)`: `4 < 5` → `contar_altos(7)`
  - `contar_altos(7)`: `7 < 10` e `7 >= 5` → retorna `1`
  - **Retornos na subida:** `1` → `1` → `1` → `1 + 1 = 2`.
- **Justificativa de terminação:** Para todo `n >= 0`, se `n < 10`, retorna imediatamente no caso base. Se `n >= 10`, `n / 10` produz um inteiro estritamente menor e não-negativo (`1 <= n / 10 < n`), de modo que o argumento decresce até atingir o intervalo `0..9` em quantidade finita de chamadas.

### `G03-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erro intencional:** O caso base `if (n == 0) return 0;` devolve `0` para a entrada `0` (ignorando que `0` possui um dígito zero). Por outro lado, apenas trocar `return 0;` por `return 1;` manteria erro para qualquer número positivo terminado em dígito não-nulo após dividir até `0` (ex.: `15 -> 1 -> 0` somaria `1`). A correção exata é usar `if (n < 10)` distinguindo `n == 0` (`1`) de `1..9` (`0`).
- **Solução corrigida completa:** [G03_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G03_C02_corrigido.c)
```c
#include <stdio.h>

int contar_zeros(int n);

int main(void) {
    int n;
    scanf("%d", &n);
    printf("Zeros: %d\n", contar_zeros(n));
    return 0;
}

int contar_zeros(int n) {
    // Bug original: if (n == 0) return 0; falhava para a entrada 0.
    // Correcao: tratar n < 10 no caso base (0 possui 1 zero; 1..9 possuem 0 zeros).
    if (n < 10) {
        if (n == 0) {
            return 1;
        }
        return 0;
    }
    if (n % 10 == 0) {
        return 1 + contar_zeros(n / 10);
    }
    return contar_zeros(n / 10);
}
```

### `G03-C03` *(Programa completo — Dígitos maiores que `lim` e potência)*
Arquivo: [G03_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G03_C03.c)
```c
#include <stdio.h>

int contar_digitos_maiores(int n, int lim);
int potencia(int x, int e);

int main(void) {
    int n, lim, x, e;
    scanf("%d %d %d %d", &n, &lim, &x, &e);
    printf("Maiores que lim: %d\n", contar_digitos_maiores(n, lim));
    printf("Potencia: %d\n", potencia(x, e));
    return 0;
}

int contar_digitos_maiores(int n, int lim) {
    if (n < 10) {
        if (n > lim) {
            return 1;
        }
        return 0;
    }
    if (n % 10 > lim) {
        return 1 + contar_digitos_maiores(n / 10, lim);
    }
    return contar_digitos_maiores(n / 10, lim);
}

int potencia(int x, int e) {
    if (e == 0) {
        return 1;
    }
    return x * potencia(x, e - 1);
}
```
