# Gabarito Comentado — Bloco `A10` (Revisão e Consolidação do Estágio A)

> **Bloco de referência:** [A10_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/blocos/A10_bloco.md)  
> **Nota para Caça ao Bug:** Os códigos em `A10-E03` e `A10-C02` no bloco do aluno contêm **defeitos intencionais** detalhados abaixo. Apenas as versões corrigidas devem ser compiladas.

---

## 1. Gabarito dos Exercícios (`A10-E01` a `A10-E05`)

### `A10-E01` *(Teste de Mesa — Memória e Atribuição)*
| Passo | Instrução | `m` | `n` | `aux` |
|---|---|---:|---:|---:|
| 0 | `int m = 4, n = 11, aux;` | `4` | `11` | `?` |
| 1 | `aux = m;` | `4` | `11` | `4` |
| 2 | `m = n - m;` | `7` | `11` | `4` |
| 3 | `n = aux + 5;` | `7` | `9` | `4` |
| 4 | `aux = n * 2;` | `7` | `9` | `18` |
| 5 | `m = aux - m;` | `11` | `9` | `18` |

- **Saída exata do `printf`:** `11 9 18`

### `A10-E02` *(Conversão Binário/Decimal e Capacidade em Bits)*
- **(a) `101110_2`:** $1\cdot 32 + 0\cdot 16 + 1\cdot 8 + 1\cdot 4 + 1\cdot 2 + 0\cdot 1 = \mathbf{46_{10}}$.
- **(b) `53_10`:** $53 = 32 + 16 + 4 + 1 \implies \mathbf{110101_2}$.
- **(c)** `9 bits` representam $2^9 = \mathbf{512}$ valores distintos; para `200` códigos, $2^7 = 128 < 200 \le 256 = 2^8 \implies \mathbf{8\text{ bits}}$.

### `A10-E03` *(Caça ao Bug Combinada — Defeitos intencionais no enunciado)*
- **Erros intencionais identificados (5 defeitos):**
  1. `#define BONUS 50.0;` contém ponto-e-vírgula `;` no final da macro (causa erro de sintaxe ao expandir dentro da expressão `salario_final = ... + BONUS;`).
  2. `Int main(void)` usa inicial maiúscula (`C` é *case-sensitive*; deve ser `int`).
  3. `1nota` é identificador inválido (começa com dígito `1`; substituído por `salario_base`).
  4. `scanf("%f", 1nota);` usa especificador `%f` errado para variável `double` (deve ser `%lf`).
  5. `scanf("%f", 1nota);` omite o operador `&` antes do nome da variável.
- **Solução corrigida completa:** [A10_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A10_E03_corrigido.c)
```c
#include <stdio.h>
#define BONUS 50.0

int main(void) {
    double salario_base, salario_final;
    scanf("%lf", &salario_base);
    salario_final = salario_base + BONUS;
    printf("Total: R$ %.2f\n", salario_final);
    return 0;
}
```

### `A10-E04` *(Programa completo — Área e Perímetro de Terreno com `const`)*
Arquivo: [A10_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A10_E04.c)
```c
#include <stdio.h>

int main(void) {
    const double FATOR_PERIMETRO = 2.0;
    double largura, comprimento, area, perimetro;

    scanf("%lf %lf", &largura, &comprimento);

    area = largura * comprimento;
    perimetro = FATOR_PERIMETRO * (largura + comprimento);

    printf("Area: %.2f m2\n", area);
    printf("Perimetro: %.2f m\n", perimetro);
    return 0;
}
```

### `A10-E05` *(Programa completo — Salário Fixo + Comissão 5% e Troca com `aux`)*
Arquivo: [A10_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A10_E05.c)
```c
#include <stdio.h>
#define TAXA 0.05

int main(void) {
    double fixo1, vendas1, fixo2, vendas2;
    double com1, com2, total1, total2, aux;

    scanf("%lf %lf", &fixo1, &vendas1);
    scanf("%lf %lf", &fixo2, &vendas2);

    com1 = TAXA * vendas1;
    com2 = TAXA * vendas2;
    total1 = fixo1 + com1;
    total2 = fixo2 + com2;

    aux = total1;
    total1 = total2;
    total2 = aux;

    printf("Comissao 1: R$ %.2f\n", com1);
    printf("Comissao 2: R$ %.2f\n", com2);
    printf("Total 1: R$ %.2f\n", total1);
    printf("Total 2: R$ %.2f\n", total2);
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`A10-C01` a `A10-C03`)

### `A10-C01` *(Papel — Teste de Mesa + Binário/$2^n$)*
- **(a) Tabela de memória:**

| Passo | Instrução | `a` | `b` | `c` |
|---|---|---:|---:|---:|
| 0 | `int a = 3, b = 10, c = 7;` | `3` | `10` | `7` |
| 1 | `c = b - a;` | `3` | `10` | `7` |
| 2 | `a = c * 2;` | `14` | `10` | `7` |
| 3 | `b = a - b;` | `14` | `4` | `7` |
| 4 | `c = b + a;` | `14` | `4` | `18` |

  **Saída final:** `14 4 18`

- **(b) Binário e Bits:**
  - `11001_2` = $16 + 8 + 1 = \mathbf{25_{10}}$.
  - `38_10` = $32 + 4 + 2 = \mathbf{100110_2}$.
  - `7 bits`: $2^7 = \mathbf{128}$ valores distintos.
  - `130` valores: $2^7 = 128 < 130 \le 256 = 2^8 \implies \mathbf{8\text{ bits}}$.

### `A10-C02` *(Caça ao Bug — `#define`, escapes e `scanf`)*
- **Erros intencionais identificados:**
  1. `#define TAXA 0.10;` contém ponto-e-vírgula `;` indevido ao final da macro.
  2. `scanf("%f", valor);` usa `%f` (errado para `double`) e omite `&` antes de `valor`.
  3. Na string do `printf`, `"10%"` fecha as aspas internas prematuramente (faltou escapar com `\"10%%\"`) e `%` isolado deve ser escapado como `%%` para imprimir literalmente `%`.
- **Solução corrigida completa:** [A10_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A10_C02_corrigido.c)
```c
#include <stdio.h>
#define TAXA 0.10

int main(void) {
    double valor, acrescimo;
    scanf("%lf", &valor);
    acrescimo = valor * TAXA;
    printf("Taxa aplicada: \"10%%\"\nValor final: R$ %.2f\n", valor + acrescimo);
    return 0;
}
```

### `A10-C03` *(Programa completo — Área/Comissão `double` + Troca `aux`)*
Arquivo: [A10_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A10_C03.c)
```c
#include <stdio.h>

int main(void) {
    const double COMISSAO = 0.05;
    double lado_a, lado_b, preco_m2, area, comissao, aux;

    scanf("%lf %lf %lf", &lado_a, &lado_b, &preco_m2);

    area = lado_a * lado_b;
    comissao = area * preco_m2 * COMISSAO;

    aux = lado_a;
    lado_a = lado_b;
    lado_b = aux;

    printf("Dimensoes trocadas: %.2f x %.2f\n", lado_a, lado_b);
    printf("Area: %.2f m2\n", area);
    printf("Comissao: R$ %.2f\n", comissao);
    return 0;
}
```
