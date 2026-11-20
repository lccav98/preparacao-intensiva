# Gabarito Comentado — Bloco `F02` (Protótipos de Funções, Escopo Local e Tempo de Vida)

> **Bloco de referência:** [F02_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/blocos/F02_bloco.md)  
> **Nota para Caça ao Bug:** `F02-E03` e `F02-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`F02-E01` a `F02-E05`)

### `F02-E01` *(Teste de Mesa)*
- **(a)** Saída exata:
  ```text
  1: 10
  2: 10
  main: x=4 acc=100
  ```
- **(b)** A variável local `acc` de `acumular_local` tem **tempo de vida** restrito à execução de uma chamada: ao retornar, ela é destruída, e na 2ª chamada é criada novamente e reinicializada com `0` (`1 + 2 + 3 + 4 = 10`). Além disso, `x` e `acc` de `acumular_local` têm **escopo** local à função e ocupam endereços independentes dos homônimos `x` e `acc` de `main`; logo `x = 99;` e `acc += i;` não afetam `main`.

### `F02-E02` *(Completar solução)*
- **`/* A */`:** `double area_circulo(double r);`
- **`/* B */`:** `void exibir_resumo(double r, double area);`
- **`/* C */`:** `return PI * r * r;`
- **`/* D */`:** `double r, double area`

### `F02-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. Protótipo incompatível: `double quadrado(int x);` diverge da definição `int quadrado(int x)`. Correto: `int quadrado(int x);`.
  2. Protótipo ausente: falta `int soma_quadrados(int a, int b);` antes de `main`, pois a definição aparece após `main`.
  3. Violação de escopo: `main` tenta imprimir `resultado`, variável local que existe apenas dentro do escopo de `soma_quadrados`; `main` deve imprimir `total` (que recebeu o retorno).
- **Solução corrigida completa:** [F02_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F02_E03_corrigido.c)
```c
#include <stdio.h>

int quadrado(int x);
int soma_quadrados(int a, int b);

int main(void) {
    int u, v, total;
    scanf("%d %d", &u, &v);
    total = soma_quadrados(u, v);
    printf("Soma dos quadrados: %d\n", total);
    return 0;
}

int quadrado(int x) {
    return x * x;
}

int soma_quadrados(int a, int b) {
    int resultado = quadrado(a) + quadrado(b);
    return resultado;
}
```

### `F02-E04` *(Programa completo — Ano bissexto e dias no mês)*
Arquivo: [F02_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F02_E04.c)
```c
#include <stdio.h>

int eh_bissexto(int ano);
int dias_no_mes(int mes, int ano);

int main(void) {
    int mes, ano, dias;
    scanf("%d %d", &mes, &ano);
    dias = dias_no_mes(mes, ano);
    if (dias < 0) {
        printf("Mes invalido\n");
    } else {
        printf("Dias: %d\n", dias);
    }
    return 0;
}

int eh_bissexto(int ano) {
    if ((ano % 400 == 0) || (ano % 4 == 0 && ano % 100 != 0)) {
        return 1;
    }
    return 0;
}

int dias_no_mes(int mes, int ano) {
    switch (mes) {
        case 1: case 3: case 5: case 7: case 8: case 10: case 12:
            return 31;
        case 4: case 6: case 9: case 11:
            return 30;
        case 2:
            if (eh_bissexto(ano)) {
                return 29;
            }
            return 28;
        default:
            return -1;
    }
}
```

### `F02-E05` *(Programa completo — Números perfeitos em `[a, b]`)*
Arquivo: [F02_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F02_E05.c)
```c
#include <stdio.h>

int soma_divisores_proprios(int n);
int eh_perfeito(int n);

int main(void) {
    int a, b, soma = 0;
    scanf("%d %d", &a, &b);
    for (int n = a; n <= b; n++) {
        if (eh_perfeito(n)) {
            soma++;
        }
    }
    printf("Perfeitos: %d\n", soma);
    return 0;
}

int soma_divisores_proprios(int n) {
    int soma = 0;
    for (int i = 1; i <= n / 2; i++) {
        if (n % i == 0) {
            soma += i;
        }
    }
    return soma;
}

int eh_perfeito(int n) {
    if (n <= 1) {
        return 0;
    }
    if (soma_divisores_proprios(n) == n) {
        return 1;
    }
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`F02-C01` a `F02-C03`)

### `F02-C01` *(Teste de Mesa)*
- **(a)** Saída exata:
  ```text
  A=3 C=10
  B=24
  ```
  *(Rastreamento: `atualizar(3)` usa sua cópia local `a = 3`, `cont = 2`, calcula `a = 5` e retorna `10`, logo `cont` de `main` vale `10` e `a` de `main` continua `3`. Na segunda chamada, `atualizar(10)` calcula `a = 10 + 2 = 12` e retorna `24`.)*
- **(b)** **Escopo** refere-se à visibilidade do nome no código-fonte: `cont` de `atualizar` só é visível dentro das chaves de `atualizar` (não colide com `cont` de `main`). **Tempo de vida** refere-se à duração na memória: `cont` de `atualizar` nasce quando `atualizar` é chamada e é destruída assim que `atualizar` executa `return`.

### `F02-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. Falta o protótipo `int mdc(int a, int b);` antes de `main`.
  2. O protótipo `double mmc(int a, int b);` declara retorno `double`, conflitando com a definição `int mmc(int a, int b)`. Correto: `int mmc(int a, int b);`.
  3. `printf("Divisor: %d\n", d);` em `main` tenta acessar a variável local `d` que pertence exclusivamente ao escopo de `mmc`.
- **Solução corrigida completa:** [F02_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F02_C02_corrigido.c)
```c
#include <stdio.h>

int mdc(int a, int b);
int mmc(int a, int b);

int main(void) {
    int x, y;
    scanf("%d %d", &x, &y);
    printf("MDC: %d\n", mdc(x, y));
    printf("MMC: %d\n", mmc(x, y));
    return 0;
}

int mdc(int a, int b) {
    while (b != 0) {
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int mmc(int a, int b) {
    int d = mdc(a, b);
    return (a / d) * b;
}
```

### `F02-C03` *(Programa completo — Contagem de primos em `[ini, fim]`)*
Arquivo: [F02_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F02_C03.c)
```c
#include <stdio.h>

int eh_primo(int n);
int contar_primos(int ini, int fim);

int main(void) {
    int ini, fim;
    scanf("%d %d", &ini, &fim);
    printf("Primos: %d\n", contar_primos(ini, fim));
    return 0;
}

int eh_primo(int n) {
    if (n <= 1) {
        return 0;
    }
    for (int d = 2; d * d <= n; d++) {
        if (n % d == 0) {
            return 0;
        }
    }
    return 1;
}

int contar_primos(int ini, int fim) {
    int cont = 0;
    for (int n = ini; n <= fim; n++) {
        if (eh_primo(n)) {
            cont++;
        }
    }
    return cont;
}
```
