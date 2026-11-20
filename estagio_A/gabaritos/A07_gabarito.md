# Gabarito Comentado — Bloco `A07` (Atribuição `=`, Memória e Troca com `aux`)

> **Bloco de referência:** [A07_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/blocos/A07_bloco.md)  
> **Nota para Caça ao Bug:** O código em `A07-E04` no bloco do aluno contém um **erro intencional** detalhado abaixo. Apenas a versão corrigida deve ser compilada.

---

## 1. Gabarito dos Exercícios (`A07-E01` a `A07-E06`)

### `A07-E01` *(Teste de Mesa — 5 atribuições)*
| Passo | Instrução | `x` | `y` | `z` |
|---|---|---:|---:|---:|
| 0 | `int x = 8, y = 3, z;` | `8` | `3` | `?` |
| 1 | `z = x;` | `8` | `3` | `8` |
| 2 | `x = x - y;` | `5` | `3` | `8` |
| 3 | `y = z + y;` | `5` | `11` | `8` |
| 4 | `z = y - x;` | `5` | `11` | `6` |
| 5 | `x = z;` | `6` | `11` | `6` |

- **Saída exata do `printf`:** `6 11 6`

### `A07-E02` *(Análise Conceitual — Falha sem `aux`)*
1. Valores finais: **`p = 4.0`** e **`q = 4.0`**. Na primeira linha (`p = q;`), o valor original **`12.5`** de `p` é sobrescrito por `4.0` e perdido definitivamente. Na segunda linha (`q = p;`), copia-se `4.0` de volta para `q`.
2. **Correção em 3 passos:**
```c
double aux;
aux = p;
p = q;
q = aux;
```

### `A07-E03` *(Completar solução — Rotação cíclica de 3 variáveis)*
- **`/* A */`:** `a`
- **`/* B */`:** `b`
- **`/* C */`:** `b`
- **`/* D */`:** `aux`
*(Sequência resultante: `aux = a; a = b; b = c; c = aux;`.)*

### `A07-E04` *(Caça ao Bug — Erro intencional no enunciado)*
- **Erro intencional:** A instrução `x = y;` executa **antes** de salvar `x` em `aux` (`aux = x;` vem depois, copiando já o valor de `y`). Assim, o valor original de `x` é destruído e ambos terminam iguais a `y`.
- **Solução corrigida completa:** [A07_E04_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A07_E04_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int x, y, aux;
    scanf("%d %d", &x, &y);

    aux = x;
    x = y;
    y = aux;

    printf("x = %d, y = %d\n", x, y);
    return 0;
}
```

### `A07-E05` *(Programa completo — Troca de `double` com antes e depois)*
Arquivo: [A07_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A07_E05.c)
```c
#include <stdio.h>

int main(void) {
    double a, b, aux;
    scanf("%lf %lf", &a, &b);

    printf("Antes: a = %.2f, b = %.2f\n", a, b);

    aux = a;
    a = b;
    b = aux;

    printf("Depois: a = %.2f, b = %.2f\n", a, b);
    return 0;
}
```

### `A07-E06` *(Programa completo — Rotação cíclica à direita de 3 inteiros)*
Arquivo: [A07_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A07_E06.c)
```c
#include <stdio.h>

int main(void) {
    int a, b, c, aux;
    scanf("%d %d %d", &a, &b, &c);

    printf("Antes: %d %d %d\n", a, b, c);

    aux = c;
    c = b;
    b = a;
    a = aux;

    printf("Depois: %d %d %d\n", a, b, c);
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`A07-C01` a `A07-C03`)

### `A07-C01` *(Teste de Mesa com Tabela de Memória)*
| Passo | Instrução | `a` | `b` | `c` |
|---|---|---:|---:|---:|
| 0 | `int a = 5, b = 12, c = 2;` | `5` | `12` | `2` |
| 1 | `c = b - a;` | `5` | `12` | `7` |
| 2 | `a = a + c;` | `12` | `12` | `7` |
| 3 | `b = a - 3;` | `12` | `9` | `7` |
| 4 | `c = b + c;` | `12` | `9` | `16` |
| 5 | `a = c - b;` | `7` | `9` | `16` |

- **Saída exata:** `7 9 16`

### `A07-C02` *(Previsão da falha sem `aux`)*
- Valores finais: **`u = 9`** e **`v = 9`**.
- Motivo: `u = v;` sobrescreve `u` com `9`, destruindo `-4`; logo `v = u;` apenas copia `9` para `v`.
- Correção: `int aux = u; u = v; v = aux;` (ou `int aux; aux = u; u = v; v = aux;`).

### `A07-C03` *(Programa completo — Rotação cíclica à esquerda de 3 variáveis)*
Arquivo: [A07_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A07_C03.c)
```c
#include <stdio.h>

int main(void) {
    int p, q, r, aux;
    scanf("%d %d %d", &p, &q, &r);

    aux = p;
    p = q;
    q = r;
    r = aux;

    printf("Resultado: %d %d %d\n", p, q, r);
    return 0;
}
```
