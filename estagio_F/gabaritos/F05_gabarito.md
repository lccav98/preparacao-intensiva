# Gabarito Comentado — Bloco `F05` (Ponteiros como Parâmetros e Depuração)

> **Bloco de referência:** [F05_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/blocos/F05_bloco.md)  
> **Nota para Caça ao Bug:** `F05-E03` e `F05-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`F05-E01` a `F05-E06`)

### `F05-E01` *(Teste de Mesa)*
- **(a)** Para `12 5`: `ordenar_par(&u, &v)` verifica `*x > *y` (`12 > 5` é verdadeiro), chama `trocar(x, y)` e troca os valores em `u` e `v`; saída: **`5 12`**. Para `4 9`: `*x > *y` (`4 > 9` é falso), não chama `trocar`; saída: **`4 9`**.
- **(b)** Em `main`, `u` e `v` são variáveis do tipo `int`, logo é preciso `&u` e `&v` para passar seus endereços por valor. Já dentro de `ordenar_par`, `x` e `y` são parâmetros do tipo `int *` (já contêm os endereços de `u` e `v`), portanto `trocar(x, y)` repassa diretamente esses endereços sem usar `&` (usar `&x` passaria `int **`, endereço do ponteiro local `x`).

### `F05-E02` *(Completar solução)*
- **`/* A */`:** `int *quoc`
- **`/* B */`:** `int *resto`
- **`/* C */`:** `&q, &r`
- **`/* D */`:**
```c
    *quoc = a / b;
    *resto = a % b;
```

### `F05-E03` *(Caça ao Bug — Erro intencional no enunciado)*
- **Erro intencional:** `int *aux;` declara um ponteiro não inicializado (contendo endereço indeterminado); `*aux = *a;` tenta gravar em posição arbitrária da memória, causando comportamento indefinido. `aux` deve ser uma variável comum do tipo `int`.
- **Solução corrigida completa:** [F05_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F05_E03_corrigido.c)
```c
#include <stdio.h>

void trocar(int *a, int *b);

int main(void) {
    int x, y;
    scanf("%d %d", &x, &y);
    trocar(&x, &y);
    printf("%d %d\n", x, y);
    return 0;
}

void trocar(int *a, int *b) {
    // Erro original: int *aux; declarava ponteiro nao inicializado (endereco indefinido),
    // causando comportamento indefinido ao tentar gravar em *aux = *a.
    // Correcao: aux deve armazenar um valor inteiro comum (int), nao um endereco.
    int aux = *a;
    *a = *b;
    *b = aux;
}
```

### `F05-E04` *(Programa completo — Soma e diferença)*
Arquivo: [F05_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F05_E04.c)
```c
#include <stdio.h>

void soma_e_diferenca(int a, int b, int *soma, int *dif);

int main(void) {
    int a, b, s, d;
    scanf("%d %d", &a, &b);
    soma_e_diferenca(a, b, &s, &d);
    printf("Soma: %d\nDiferenca: %d\n", s, d);
    return 0;
}

void soma_e_diferenca(int a, int b, int *soma, int *dif) {
    *soma = a + b;
    *dif = a - b;
}
```

### `F05-E05` *(Programa completo — Extremos de 3 inteiros)*
Arquivo: [F05_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F05_E05.c)
```c
#include <stdio.h>

void extremos_tres(int a, int b, int c, int *menor, int *maior);

int main(void) {
    int a, b, c, menor, maior;
    scanf("%d %d %d", &a, &b, &c);
    extremos_tres(a, b, c, &menor, &maior);
    printf("Menor: %d\nMaior: %d\n", menor, maior);
    return 0;
}

void extremos_tres(int a, int b, int c, int *menor, int *maior) {
    *menor = a;
    *maior = a;
    if (b < *menor) {
        *menor = b;
    }
    if (c < *menor) {
        *menor = c;
    }
    if (b > *maior) {
        *maior = b;
    }
    if (c > *maior) {
        *maior = c;
    }
}
```

### `F05-E06` *(Programa completo — Decomposição de tempo)*
Arquivo: [F05_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F05_E06.c)
```c
#include <stdio.h>

void decompor_tempo(int total_seg, int *h, int *m, int *s);

int main(void) {
    int total_seg, h, m, s;
    scanf("%d", &total_seg);
    decompor_tempo(total_seg, &h, &m, &s);
    printf("%d h, %d min, %d s\n", h, m, s);
    return 0;
}

void decompor_tempo(int total_seg, int *h, int *m, int *s) {
    *h = total_seg / 3600;
    *m = (total_seg % 3600) / 60;
    *s = total_seg % 60;
}
```

---

## 2. Gabarito da Checagem Independente (`F05-C01` a `F05-C03`)

### `F05-C01` *(Teste de Mesa)*
- **(a)** Saída impressa: **`30`** (`val` recebe `*q` = `15`; `atualizar(q, 15)` executa `*p = 15 + 15 = 30`, alterando `saldo` em `main`).
- **(b)** `q` já é do tipo `int *` e contém o endereço de `saldo`, por isso `atualizar(q, val)` repassa `q` sem `&`. Além disso, `p` em `atualizar` é uma **cópia local** passada por valor contendo o endereço de `saldo`; executar `p = NULL;` altera apenas a variável local `p`, sem modificar `q` nem `saldo`.

### `F05-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. Em `main`, `acumular(saldo, x);` e `acumular(saldo, y);` passam o valor `int` `saldo` em vez do endereço `&saldo` (`int *`).
  2. Em `acumular`, `total = total + valor;` modifica a cópia local do endereço (aritmética de ponteiro sem alterar o apontado), em vez de desreferenciar com `*total = *total + valor;`.
- **Solução corrigida completa:** [F05_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F05_C02_corrigido.c)
```c
#include <stdio.h>

void acumular(int *total, int valor);

int main(void) {
    int saldo = 100, x, y;
    scanf("%d %d", &x, &y);
    acumular(&saldo, x);
    acumular(&saldo, y);
    printf("Saldo: %d\n", saldo);
    return 0;
}

void acumular(int *total, int valor) {
    *total = *total + valor;
}
```

### `F05-C03` *(Programa completo — Área e perímetro de retângulo)*
Arquivo: [F05_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F05_C03.c)
```c
#include <stdio.h>

void retangulo(double base, double altura, double *area, double *perimetro);

int main(void) {
    double base, altura, area, perimetro;
    scanf("%lf %lf", &base, &altura);
    retangulo(base, altura, &area, &perimetro);
    printf("Area: %.2f\nPerimetro: %.2f\n", area, perimetro);
    return 0;
}

void retangulo(double base, double altura, double *area, double *perimetro) {
    *area = base * altura;
    *perimetro = 2.0 * (base + altura);
}
```
