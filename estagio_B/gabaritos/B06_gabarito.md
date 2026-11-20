# Gabarito Comentado — Bloco `B06` (Operadores Lógicos e Tabela-Verdade)

> **Bloco de referência:** [B06_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/blocos/B06_bloco.md)  
> **Nota para Caça ao Bug:** Os códigos em `B06-E03` e `B06-C02` no bloco do aluno contêm **erros conceituais clássicos** (`min <= x <= max`). Apenas as versões corrigidas devem ser compiladas.

---

## 1. Gabarito dos Exercícios (`B06-E01` a `B06-E06`)

### `B06-E01` *(Tabela-Verdade e Teste de Mesa)*
Variáveis: `x = 4, y = 7, z = 0`.
- **a) `x < y && y != 7`:**
  - `(4 < 7)` é `1` (verdadeiro).
  - `(7 != 7)` é `0` (falso).
  - `1 && 0` $\rightarrow$ **`0`**.
- **b) `x + 3 == y || z > 0`:**
  - `(4 + 3 == 7)` $\rightarrow$ `(7 == 7)` é `1`.
  - Como o primeiro operando do `||` é `1`, ocorre **curto-circuito**: `z > 0` nem é avaliado.
  - Resultado final $\rightarrow$ **`1`**.
- **c) `!z && (x > y || y > 0)`:**
  - `!0` $\rightarrow$ `1`.
  - Dentro dos parênteses: `(4 > 7)` é `0`; `(7 > 0)` é `1`; `0 || 1` $\rightarrow$ `1`.
  - `1 && 1` $\rightarrow$ **`1`**.
- **d) `!(x < y) || !z && y > x`:**
  - `!(4 < 7)` $\rightarrow$ `!(1)` $\rightarrow$ `0`.
  - `!z` $\rightarrow$ `!0` $\rightarrow$ `1`.
  - `(y > x)` $\rightarrow$ `(7 > 4)` $\rightarrow$ `1`.
  - Precedência: `&&` antes de `||`. Logo, avalia `!z && y > x` $\rightarrow$ `1 && 1` $\rightarrow$ `1`.
  - Por fim, `0 || 1` $\rightarrow$ **`1`**.
- **e) `z != 0 && (y / z > 1)`:**
  - `(0 != 0)` é `0` (falso).
  - Devido ao **curto-circuito**, o operando à direita `(y / z > 1)` **não é executado**, o que evita uma falha catastrófica de divisão por zero (*Floating point exception / crash*).
  - Resultado final $\rightarrow$ **`0`**.

---

### `B06-E02` *(Precedência e Parênteses Defensivos)*
Variáveis: `a = 1, b = 0, c = 1`.
1. **Sem parênteses: `a || b && c == 0`**
   - Ordem de avaliação:
     - 1º: `c == 0` $\rightarrow$ `1 == 0` é `0`.
     - 2º: `b && 0` $\rightarrow$ `0 && 0` é `0` (o operador `&&` tem maior precedência que o `||`).
     - 3º: `a || 0` $\rightarrow$ `1 || 0` é `1`.
   - Na prática em C com curto-circuito: como `a = 1`, o `||` encerra imediatamente e o lado direito nem precisa ser avaliado!
   - Resultado final $\rightarrow$ **`1`**.
2. **Com parênteses: `(a || b) && c == 0`**
   - 1º: `(a || b)` $\rightarrow$ `(1 || 0)` é `1`.
   - 2º: `c == 0` $\rightarrow$ `1 == 0` é `0`.
   - 3º: `1 && 0` $\rightarrow$ **`0`**.
   - **Explicação:** Os parênteses forçaram a disjunção `(a || b)` a ser resolvida antes da conjunção, invertendo a prioridade natural de `&&` sobre `||`.

---

### `B06-E03` *(Caça ao Bug — `18 <= idade <= 35`)*
1. **Análise do bug:**
   - Para `idade = 50`, a CPU avalia a subexpressão da esquerda primeiro: `18 <= 50`, que resulta em `1` (verdadeiro).
   - Em seguida, avalia o resultado com a segunda comparação: `1 <= 35`. Como `1 <= 35` é verdadeiro, a expressão toda resulta em `1`, imprimindo `Apto` para alguém de 50 anos!
   - Na verdade, como `18 <= idade` só produz `0` ou `1`, e ambos são `<= 35`, essa expressão é **sempre verdadeira** para qualquer idade inteira!
2. **Versão corrigida completa:** [B06_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B06_E03_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int idade;
    if (scanf("%d", &idade) != 1) {
        return 1;
    }

    if (idade >= 18 && idade <= 35) {
        printf("Apto\n");
    } else {
        printf("Inapto\n");
    }

    return 0;
}
```

---

### `B06-E04` *(Programa completo — Parque de Diversões)*
Arquivo: [B06_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B06_E04.c)
```c
#include <stdio.h>

int main(void) {
    double alt;
    int idade;

    if (scanf("%lf %d", &alt, &idade) != 2) {
        return 1;
    }

    if ((alt >= 1.50 && idade >= 12) || (idade >= 16 && alt >= 1.40)) {
        printf("Acesso Permitido\n");
    } else {
        printf("Acesso Negado\n");
    }

    return 0;
}
```

---

### `B06-E05` *(Programa completo — Existência de Triângulo)*
Arquivo: [B06_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B06_E05.c)
```c
#include <stdio.h>

int main(void) {
    double a, b, c;

    if (scanf("%lf %lf %lf", &a, &b, &c) != 3) {
        return 1;
    }

    if (a < b + c && b < a + c && c < a + b) {
        printf("Triangulo Valido\n");
    } else {
        printf("Triangulo Invalido\n");
    }

    return 0;
}
```

---

### `B06-E06` *(Programa completo — Concessão de Empréstimo)*
Arquivo: [B06_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B06_E06.c)
```c
#include <stdio.h>

int main(void) {
    int idade, correntista;
    double renda;

    if (scanf("%d %lf %d", &idade, &renda, &correntista) != 3) {
        return 1;
    }

    if ((idade >= 21 && idade <= 65 && renda >= 2500.00) ||
        (correntista == 1 && idade >= 18 && renda >= 1500.00)) {
        printf("Emprestimo Aprovado\n");
    } else {
        printf("Emprestimo Negado\n");
    }

    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`B06-C01` a `B06-C04`)

### `B06-C01` *(Teste de Mesa — Tabela-Verdade e Curto-Circuito)*
Variáveis: `p = 0, q = 3, r = -1`.
1. `p != 0 && (q / p > 0)`:
   - `p != 0` $\rightarrow$ `0 != 0` é `0`.
   - **Curto-circuito ativado**: o termo `(q / p > 0)` **não é avaliado**. Resultado: **`0`**.
2. `q > 0 || (r / p == 0)`:
   - `q > 0` $\rightarrow$ `3 > 0` é `1`.
   - **Curto-circuito ativado**: o termo `(r / p == 0)` **não é avaliado**. Resultado: **`1`**.
3. `!p && (q > 0 || r > 0)`:
   - `!0` $\rightarrow$ `1`. Avalia o lado direito: `(3 > 0)` é `1` (que por curto-circuito interno não avalia `r > 0`).
   - `1 && 1` $\rightarrow$ **`1`** (o termo `r > 0` não foi avaliado).
4. `!(q > 2 && r < 0) || (p == 0)`:
   - `(3 > 2 && -1 < 0)` $\rightarrow$ `1 && 1` $\rightarrow$ `1`.
   - `!(1)` $\rightarrow$ `0`.
   - Como o primeiro termo é `0`, o segundo termo `(p == 0)` **foi avaliado** (`0 == 0` é `1`).
   - `0 || 1` $\rightarrow$ **`1`** (sem curto-circuito no `||` principal).

---

### `B06-C02` *(Caça ao Bug)*
1. **Defeito:** `6.0 <= nota <= 10.0` avalia como `(6.0 <= nota) <= 10.0`. Se `nota = 2.0`, `6.0 <= 2.0` dá `0`. Depois `0 <= 10.0` dá `1`. Como `freq = 80 >= 75`, a condição inteira vira `1 && 1`, aprovando erroneamente o aluno com nota 2.0.
2. **Solução corrigida:** [B06_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B06_C02_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    double nota;
    int freq;

    if (scanf("%lf %d", &nota, &freq) != 2) {
        return 1;
    }

    if (nota >= 6.0 && nota <= 10.0 && freq >= 75) {
        printf("Aprovado\n");
    } else {
        printf("Reprovado\n");
    }

    return 0;
}
```

---

### `B06-C03` *(Programa completo — Validação de Data)*
Arquivo: [B06_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B06_C03.c)
```c
#include <stdio.h>

int main(void) {
    int dia, mes;

    if (scanf("%d %d", &dia, &mes) != 2) {
        return 1;
    }

    if (mes == 2 && dia >= 1 && dia <= 28) {
        printf("Data Valida\n");
    } else if ((mes == 4 || mes == 6 || mes == 9 || mes == 11) && (dia >= 1 && dia <= 30)) {
        printf("Data Valida\n");
    } else if ((mes == 1 || mes == 3 || mes == 5 || mes == 7 || mes == 8 || mes == 10 || mes == 12) && (dia >= 1 && dia <= 31)) {
        printf("Data Valida\n");
    } else {
        printf("Data Invalida\n");
    }

    return 0;
}
```

---

### `B06-C04` *(Programa completo — Bolsa de IC)*
Arquivo: [B06_C04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B06_C04.c)
```c
#include <stdio.h>

int main(void) {
    double cra, renda;

    if (scanf("%lf %lf", &cra, &renda) != 2) {
        return 1;
    }

    if ((cra >= 8.5 && renda <= 1800.00) || (cra >= 9.5)) {
        printf("Bolsa Concedida\n");
    } else {
        printf("Bolsa Nao Concedida\n");
    }

    return 0;
}
```
