# Gabarito Comentado — Bloco `C08` (Séries Numéricas, Atualização Incremental e Convergência por Tolerância)

> **Bloco de referência:** [C08_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/blocos/C08_bloco.md)  
> **Nota para Caça ao Bug:** Os códigos de `C08-E02`, `C08-E03` e `C08-C01` apresentam armadilhas numéricas clássicas (divisão inteira truncada, avaliação tardia em `do-while` e divisão por zero *off-by-one*). As versões corrigidas compiláveis encontram-se em `testes/solucoes/`.

---

## 1. Gabarito dos Exercícios (`C08-E01` a `C08-E06`)

### `C08-E01` *(Teste de Mesa dos 4 Primeiros Termos de Série Incremental)*
Série de Leibniz: $\frac{\pi}{4} = \sum_{k=0}^{\infty} \frac{(-1)^k}{2k + 1}$.

| $k$ | `sinal` | Denominador ($2k+1$) | `termo` (Fração) | `termo` (Decimal 4 casas) | `soma` acumulada (4 casas) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **0** | `+1.0` | `1` | $+1/1$ | `1.0000` | `1.0000` |
| **1** | `-1.0` | `3` | $-1/3$ | `-0.3333` | `0.6667` |
| **2** | `+1.0` | `5` | $+1/5$ | `0.2000` | `0.8667` |
| **3** | `-1.0` | `7` | $-1/7$ | `-0.1429` | `0.7238` |

*Observação:* Mantendo a precisão completa em `double`, após $k=3$ temos $\frac{76}{105} \approx 0.7238095\dots$

---

### `C08-E02` *(Caça ao Bug 1 — Divisão Inteira Destrutiva em Denominador)*
1. **Explicação analítica:** Na linha `soma += 1 / fat;`, o numerador `1` é um literal `int` e a variável `fat` foi declarada como `int`. Em C, a divisão entre dois operandos inteiros executa **divisão inteira truncada** (descartando a parte fracionária):
   - Para $k = 1$: `fat = 1`, logo `1 / 1` resulta `1`.
   - Para $k \ge 2$: `fat` passa a valer `2, 6, 24, 120...`, e em todas essas iterações `1 / fat` resulta exatamente **`0`**.
   - Por isso, apenas o primeiro termo foi somado, imprimindo `Soma = 1.000000`. Além disso, declarar `fat` como `int` provoca *overflow* para $n \ge 13$; usar `double fat = 1.0;` e `1.0 / fat` resolve ambos os problemas.
2. **Solução completa corrigida:** [C08_E02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C08_E02_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int n;
    if (scanf("%d", &n) != 1) {
        return 1;
    }

    double soma = 0.0;
    double fat = 1.0;

    for (int k = 1; k <= n; k++) {
        fat *= k;
        soma += 1.0 / fat;
    }

    printf("Soma = %.6f\n", soma);
    return 0;
}
```

---

### `C08-E03` *(Caça ao Bug 2 — Somar o Termo Violador que Falha em $< \varepsilon$)*
1. **Demonstração:** A estrutura `do-while` testa a condição `termo >= eps` apenas **ao final** do corpo do laço:
   - Se o usuário informar $\varepsilon > 1.0$ (por exemplo, `eps = 1.5`), o primeiro termo (`1.0`) já viola o critério ($1.0 < 1.5$), mas ainda assim o bloco `do` é executado uma vez e soma `1.0` indevidamente antes de encerrar.
   - Adicionalmente, no código original `termo` inicia em `1.0` e dentro do corpo `k` inicia em `1`, recalculando `1.0 / (1 * 1) = 1.0` e somando $\frac{1}{1^2}$ em duplicidade quando $\varepsilon \le 1.0$.
   - A correção utiliza um laço `while (termo >= eps)` pré-teste, garantindo que todo termo seja validado antes de entrar em `soma` e atualizando `k++` antes de calcular o próximo termo `1.0 / ((double)k * k)`.
2. **Solução completa corrigida:** [C08_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C08_E03_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    double eps;
    if (scanf("%lf", &eps) != 1) {
        return 1;
    }

    double soma = 0.0;
    double termo = 1.0;
    int k = 1;

    while (termo >= eps) {
        soma += termo;
        k++;
        termo = 1.0 / ((double)k * k);
    }

    printf("Soma = %.6f\n", soma);
    return 0;
}
```

---

### `C08-E04` *(Série Exponencial $e^x$ com Atualização Incremental $O(n)$)*
Solução completa: [C08_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C08_E04.c)
```c
#include <stdio.h>

int main(void) {
    double x;
    int n;
    if (scanf("%lf %d", &x, &n) != 2) {
        return 1;
    }

    double soma = 0.0;
    double termo = 1.0;

    for (int k = 0; k < n; k++) {
        soma += termo;
        termo = termo * x / (k + 1);
    }

    printf("e^x aprox: %.6f\n", soma);
    return 0;
}
```
*Comentário:* Para $k = 0$, `termo = 1.0` ($\frac{x^0}{0!}$). Ao final da iteração $k$, o próximo termo $k+1$ é obtido em $O(1)$ por `termo = termo * x / (k + 1)`.

---

### `C08-E05` *(Série Contada da Lista 5 Ex. 5 — Prova AED I UFPR 2017)*
Solução completa: [C08_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C08_E05.c)
```c
#include <stdio.h>

int main(void) {
    int n;
    if (scanf("%d", &n) != 1) {
        return 1;
    }

    if (n <= 0) {
        printf("Entrada Invalida\n");
        return 0;
    }

    double soma = 0.0;
    double pot2 = 1.0;

    for (int k = 0; k < n; k++) {
        double den = (double)(n - k) * (n - k);
        soma += pot2 / den;
        pot2 *= 2.0;
    }

    printf("S = %.6f\n", soma);
    return 0;
}
```
*Comentário:* O limite `k < n` impede que `(n - k)` chegue a `0`, e o *cast* `(double)(n - k) * (n - k)` evita *overflow* no cálculo do quadrado do denominador.

---

### `C08-E06` *(Série por Tolerância com Contagem Exata de Termos)*
Solução completa: [C08_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C08_E06.c)
```c
#include <stdio.h>

int main(void) {
    double eps;
    if (scanf("%lf", &eps) != 1) {
        return 1;
    }

    if (eps <= 0.0) {
        printf("Tolerancia Invalida\n");
        return 0;
    }

    double soma = 0.0;
    double termo = 1.0;
    int k = 0;

    while (termo >= eps) {
        soma += termo;
        k++;
        termo = termo / k;
    }

    printf("Soma = %.8f\n", soma);
    printf("Termos = %d\n", k);
    return 0;
}
```
*Nota numérica:* Para $\varepsilon = 0.001$, são somados os 7 termos de $k=0$ até $k=6$ ($1 + 1 + 0.5 + \frac{1}{6} + \frac{1}{24} + \frac{1}{120} + \frac{1}{720} = 2.71805556$), pois $\frac{1}{7!} \approx 0.00019841 < 0.001$. *(Nota de errata ao enunciado: `2.71825397` incluiria erroneamente o termo $k=7$).*

---

## 2. Gabarito da Checagem Independente (`C08-C01` a `C08-C03`)

### `C08-C01` *(Identificação de Bug Numérico e Divisão por Zero)*
1. **Perda de precisão (divisão inteira):** Nas expressões `(1 / (k + 1))` e `(n / (n - k))`, todos os operandos são inteiros (`int`). Para qualquer $k \ge 1$, `1 / (k + 1)` resulta em **`0`**, anulando todo o produto `termo` (e `n / (n - k)` também sofre truncamento inteiro). Correção: usar literais reais e conversão explícita, por exemplo `(1.0 / (k + 1)) * ((double)n / (n - k))`.
2. **Divisão por zero (*off-by-one*):** Como o laço usa a condição `k <= n`, na última iteração ($k = n$) o denominador `(n - k)` torna-se `n - n = 0`, provocando divisão inteira por zero e falha fatal em tempo de execução (*Floating Point Exception*). Correção: alterar a condição do laço para `k < n`.

---

### `C08-C02` *(Programa Completo — Série Alternada do Logaritmo Natural $\ln(1+x)$)*
Solução completa: [C08_C02.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C08_C02.c)
```c
#include <stdio.h>

int main(void) {
    double x;
    int n;
    if (scanf("%lf %d", &x, &n) != 2) {
        return 1;
    }

    double soma = 0.0;
    double pot_x = x;
    double sinal = 1.0;

    for (int k = 1; k <= n; k++) {
        soma += sinal * pot_x / k;
        pot_x *= x;
        sinal = -sinal;
    }

    printf("ln(1+x) aprox: %.6f\n", soma);
    return 0;
}
```

---

### `C08-C03` *(Programa Completo — Série com Tolerância e Borda $\varepsilon > 1$)*
Solução completa: [C08_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C08_C03.c)
```c
#include <stdio.h>

int main(void) {
    double eps;
    if (scanf("%lf", &eps) != 1) {
        return 1;
    }

    double soma = 0.0;
    double termo = 1.0;
    int termos = 0;
    int k = 1;

    while (termo >= eps) {
        soma += termo;
        termos++;
        k++;
        termo = 1.0 / ((double)k * k);
    }

    printf("Soma = %.6f\n", soma);
    printf("Termos = %d\n", termos);
    return 0;
}
```
*Comentário:* Quando $\varepsilon > 1.0$, a condição inicial `1.0 >= eps` falha imediatamente: o laço executa `0` vezes, imprimindo `Soma = 0.000000` e `Termos = 0`.
