# Gabarito Comentado — Bloco `C02` (Contadores e Acumuladores com `while`)

> **Bloco de referência:** [C02_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/blocos/C02_bloco.md)  
> **Nota para Caça ao Bug:** Em `C02-E02` e `C02-C02`, a condição `resto > divisor` e a variável `quociente` não zerada constituem falhas conceituais intencionais. Apenas as versões corrigidas devem ser compiladas.

---

## 1. Gabarito dos Exercícios (`C02-E01` a `C02-E05`)

### `C02-E01` *(Teste de Mesa / Rastreamento de Contador e Acumulador)*
Tabela de rastreamento de `num = 1` a `5`:
- `num = 1`: `1 % 2 == 0` (F) $\rightarrow$ `soma = 0`, `conta = 0`, `num` vira 2.
- `num = 2`: `2 % 2 == 0` (V) $\rightarrow$ `soma = 0 + 2 = 2`, `conta = 1`, `num` vira 3.
- `num = 3`: `3 % 2 == 0` (F) $\rightarrow$ `soma = 2`, `conta = 1`, `num` vira 4.
- `num = 4`: `4 % 2 == 0` (V) $\rightarrow$ `soma = 2 + 4 = 6`, `conta = 2`, `num` vira 5.
- `num = 5`: `5 % 2 == 0` (F) $\rightarrow$ `soma = 6`, `conta = 2`, `num` vira 6.
- `num = 6`: sai do laço (`6 <= 5` é falso).

1. **Números que entraram no `if`:** `2` e `4`.
2. **Valor final de `soma`:** `6`.
3. **Valor final de `conta`:** `2`.
4. **Valor final de `num`:** `6`.

---

### `C02-E02` *(Caça ao Bug — Variável Não Zerada e Resto de Múltiplos Exatos)*
1. **Erro de `quociente`:** A variável local `quociente` foi declarada sem inicialização (`int quociente;`). Ao executar `quociente++`, o programa tenta somar 1 a lixo de memória da pilha, produzindo resultado imprevisível. O correto é inicializar com zero: `int quociente = 0;`.
2. **Erro na entrada `15 5`:**
   - Como $15$ é múltiplo exato de $5$, após 2 subtrações temos `resto = 5`.
   - O teste `resto > b` torna-se `5 > 5`, que é **Falso**!
   - O laço para antes da última subtração, imprimindo incorretamente `Quociente: 2` (ou valor indefinido) e `Resto: 5`, em vez do correto `Quociente: 3` e `Resto: 0`.
3. **Versão corrigida completa:** [C02_E02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C02_E02_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int a, b;
    int quociente = 0;
    int resto;

    scanf("%d %d", &a, &b);

    resto = a;
    while (resto >= b) {
        resto = resto - b;
        quociente++;
    }

    printf("Quociente: %d\n", quociente);
    printf("Resto: %d\n", resto);
    return 0;
}
```

---

### `C02-E03` *(Completar Solução — Tabuada com while)*
- **Lacuna `/* A */`:** `1`
- **Lacuna `/* B */`:** `i <= 10`
- **Lacuna `/* C */`:** `i++`
- **Código completo:** [C02_E03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C02_E03.c)
```c
#include <stdio.h>

int main(void) {
    int n;
    int i = 1;
    scanf("%d", &n);

    while (i <= 10) {
        printf("%d x %d = %d\n", n, i, n * i);
        i++;
    }

    return 0;
}
```

---

### `C02-E04` *(Completar Solução — Divisão por Subtrações Sucessivas)*
- **Lacuna 1 (condição):** `resto >= divisor`
- **Lacuna 2:** `resto - divisor`
- **Lacuna 3:** `quociente++`
- **Código completo:** [C02_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C02_E04.c)
```c
#include <stdio.h>

int main(void) {
    int dividendo, divisor;
    int quociente = 0;
    int resto;

    scanf("%d %d", &dividendo, &divisor);

    resto = dividendo;
    while (resto >= divisor) {
        resto -= divisor;
        quociente++;
    }

    printf("Quociente: %d\n", quociente);
    printf("Resto: %d\n", resto);
    return 0;
}
```

---

### `C02-E05` *(Resolução Independente — Soma e Contagem de Pares em Intervalo)*
Arquivo: [C02_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C02_E05.c)
```c
#include <stdio.h>

int main(void) {
    int a, b;
    int conta = 0;
    int soma = 0;
    int atual;

    scanf("%d %d", &a, &b);

    atual = a;
    while (atual <= b) {
        if (atual % 2 == 0) {
            conta++;
            soma += atual;
        }
        atual++;
    }

    printf("Quantidade: %d\n", conta);
    printf("Soma: %d\n", soma);
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`C02-C01` a `C02-C03`)

### `C02-C01` *(Teste de Mesa / Acumulação com Filtros Lógicos)*
Valores de `i` entre 1 e 10 testados:
- Múltiplos de 3 ou de 5 no intervalo: `3, 5, 6, 9, 10`.
1. **Valores que entraram no `if`:** `3, 5, 6, 9, 10`.
2. **Valor final de `qtd`:** `5`.
3. **Valor final de `soma`:** $3 + 5 + 6 + 9 + 10 =$ **`33`**.

---

### `C02-C02` *(Caça ao Bug — Resto de Múltiplo Exato)*
1. **Entrada `12 4`:** O programa executa:
   - Início: `resto = 12`.
   - Iteração 1: `12 > 4` (V) $\rightarrow$ `resto = 8`.
   - Iteração 2: `8 > 4` (V) $\rightarrow$ `resto = 4`.
   - Teste seguinte: `4 > 4` é **Falso**!
   - Saída gerada: `Resto: 4`. Saída correta esperada: `Resto: 0`.
2. **Razão matemática:** Quando o dividendo é múltiplo exato do divisor, o resto final deve ser zero. Ao usar o operador estrito `>`, o algoritmo para quando o resto atinge exatamente o divisor. Deve-se usar `>=` para permitir a última subtração.
3. **Versão corrigida:** [C02_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C02_C02_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int a, b;
    int resto;
    scanf("%d %d", &a, &b);

    resto = a;
    while (resto >= b) {
        resto -= b;
    }

    printf("Resto: %d\n", resto);
    return 0;
}
```

---

### `C02-C03` *(Programa Completo Independente — Estatísticas de Intervalo)*
Arquivo: [C02_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C02_C03.c)
```c
#include <stdio.h>

int main(void) {
    int inicio, fim;
    int impares = 0;
    int soma_mult3 = 0;
    int atual;

    scanf("%d %d", &inicio, &fim);

    atual = inicio;
    while (atual <= fim) {
        if (atual % 2 != 0) {
            impares++;
        }
        if (atual % 3 == 0) {
            soma_mult3 += atual;
        }
        atual++;
    }

    printf("Impares: %d\n", impares);
    printf("Soma mult 3: %d\n", soma_mult3);
    return 0;
}
```
