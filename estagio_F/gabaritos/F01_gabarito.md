# Gabarito Comentado — Bloco `F01` (Introdução a Funções: `void`, `return`, Parâmetros e Argumentos)

> **Bloco de referência:** [F01_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/blocos/F01_bloco.md)  
> **Nota para Caça ao Bug:** `F01-E03` e `F01-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`F01-E01` a `F01-E05`)

### `F01-E01` *(Teste de Mesa)*
- **(a)** Saída exata:
  ```text
  ---
  R = 19
  ---
  ```
  *(Rastreamento: `calcular(3, 4)` retorna `3 * 2 + 4 = 10`; `calcular(2, 5)` retorna `2 * 2 + 5 = 9`; `r = 10 + 9 = 19`.)*
- **(b)** Na primeira chamada `calcular(3, 4)`, os **parâmetros formais** são `a` e `b` (declarados na assinatura de `calcular`), e os **argumentos** são `3` e `4` (copiados por valor para `a` e `b`). A chamada `printf("%d", separador());` é inválida porque `separador` tem tipo de retorno `void` (não devolve nenhum valor que possa ser formatado por `%d`).

### `F01-E02` *(Completar solução)*
- **`/* A */`:** `void`
- **`/* B */`:** `int b`
- **`/* C */`:** `return b;`
- **`/* D */`:** `maior2(x, y)`

### `F01-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `int maior_de_dois(int a, b)` omite o tipo `int` antes do parâmetro `b`. Correto: `int maior_de_dois(int a, int b)`.
  2. Falta `return b;` no caminho em que `a < b` (função não-`void` deve retornar valor em todos os caminhos).
  3. Em `main`, `maior_de_dois(x, y);` é chamada sem armazenar o retorno, deixando `m` igual a `0`. Correto: `m = maior_de_dois(x, y);`.
- **Solução corrigida completa:** [F01_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F01_E03_corrigido.c)
```c
#include <stdio.h>

int maior_de_dois(int a, int b) {
    // Erro 1 original: faltava o tipo 'int' antes de 'b' na lista de parametros.
    // Erro 2 original: faltava o comando 'return b;' quando a < b.
    if (a >= b) {
        return a;
    }
    return b;
}

int main(void) {
    int x, y, m;
    scanf("%d %d", &x, &y);
    // Erro 3 original: chamada maior_de_dois(x, y); descartava o valor retornado.
    m = maior_de_dois(x, y);
    printf("Maior: %d\n", m);
    return 0;
}
```

### `F01-E04` *(Programa completo — Exibir faixa e soma do intervalo)*
Arquivo: [F01_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F01_E04.c)
```c
#include <stdio.h>

void exibir_faixa(int ini, int fim) {
    if (ini > fim) {
        printf("Intervalo vazio\n");
    } else {
        for (int i = ini; i <= fim; i++) {
            if (i > ini) {
                printf(" ");
            }
            printf("%d", i);
        }
        printf("\n");
    }
}

int soma_intervalo(int ini, int fim) {
    int soma = 0;
    for (int i = ini; i <= fim; i++) {
        soma += i;
    }
    return soma;
}

int main(void) {
    int a, b;
    scanf("%d %d", &a, &b);
    exibir_faixa(a, b);
    printf("Soma: %d\n", soma_intervalo(a, b));
    return 0;
}
```

### `F01-E05` *(Programa completo — Contagem e soma de dígitos)*
Arquivo: [F01_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F01_E05.c)
```c
#include <stdio.h>

int contar_digitos(int n) {
    if (n == 0) {
        return 1;
    }
    int cont = 0;
    while (n > 0) {
        cont++;
        n /= 10;
    }
    return cont;
}

int soma_digitos(int n) {
    int soma = 0;
    while (n > 0) {
        soma += n % 10;
        n /= 10;
    }
    return soma;
}

int main(void) {
    int n;
    scanf("%d", &n);
    printf("Digitos: %d\n", contar_digitos(n));
    printf("Soma dos digitos: %d\n", soma_digitos(n));
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`F01-C01` a `F01-C03`)

### `F01-C01` *(Teste de Mesa)*
- **(a)** Saída exata:
  ```text
  *
  16
  8
  *
  ```
  *(Rastreamento: `v = 5`; `marca()` imprime `*`; `passo(5)` entra no caminho ímpar e retorna `5 * 3 + 1 = 16`, logo `v` passa a `16` e imprime `16`; `passo(16)` entra em `16 % 2 == 0` e retorna `8`, impresso pelo `printf`; `marca()` imprime `*`.)*
- **(b)** O parâmetro formal de `passo` é `k`. Na 1ª chamada (`passo(v)` com `v == 5`), o argumento avaliado é `5`; na 2ª chamada (`passo(v)` com `v == 16`), o argumento avaliado é `16`.

### `F01-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `double calcular_subtotal(double preco, qtd)` omite o tipo `int` antes de `qtd`. Correto: `double calcular_subtotal(double preco, int qtd)`.
  2. `calcular_desconto` tem `return` apenas quando `total >= 200.0`, faltando `return 0.0;` quando a condição é falsa.
  3. Em `main`, `calcular_desconto(subtotal);` ignora o valor retornado em vez de atribuí-lo a `desc` (`desc = calcular_desconto(subtotal);`).
- **Solução corrigida completa:** [F01_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F01_C02_corrigido.c)
```c
#include <stdio.h>

double calcular_subtotal(double preco, int qtd) {
    return preco * qtd;
}

double calcular_desconto(double total) {
    if (total >= 200.0) {
        return total * 0.10;
    }
    return 0.0;
}

int main(void) {
    double preco, subtotal, desc;
    int qtd;
    scanf("%lf %d", &preco, &qtd);
    subtotal = calcular_subtotal(preco, qtd);
    desc = calcular_desconto(subtotal);
    printf("Total: %.2f\n", subtotal - desc);
    return 0;
}
```

### `F01-C03` *(Programa completo — Linha de caracteres e fatorial iterativo)*
Arquivo: [F01_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F01_C03.c)
```c
#include <stdio.h>

void imprimir_linha(int n, char ch) {
    for (int i = 0; i < n; i++) {
        printf("%c", ch);
    }
    printf("\n");
}

int fatorial(int n) {
    int fat = 1;
    for (int i = 2; i <= n; i++) {
        fat *= i;
    }
    return fat;
}

int main(void) {
    int n;
    char ch;
    scanf("%d %c", &n, &ch);
    imprimir_linha(n, ch);
    printf("Fatorial: %d\n", fatorial(n));
    return 0;
}
```
