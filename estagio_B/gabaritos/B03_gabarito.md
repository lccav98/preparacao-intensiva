# Gabarito Comentado — Bloco `B03` (Expressões Relacionais, `<stdbool.h>` e `if` Simples)

> **Bloco de referência:** [B03_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/blocos/B03_bloco.md)  
> **Nota para Caça ao Bug:** Os códigos em `B03-E03` e `B03-C02` contêm **erros intencionais** clássicos (`=` em vez de `==`, `;` após `if`, falta de parênteses/chaves). Apenas as versões corrigidas devem ser compiladas.

---

## 1. Gabarito dos Exercícios (`B03-E01` a `B03-E05`)

### `B03-E01` *(Tabela-Verdade de Operadores Relacionais)*
Considerando `int a = 5, b = 8;`:
1. `a == b` $\to 5 == 8 \to$ **`0`** (`false`).
2. `a != b` $\to 5 \neq 8 \to$ **`1`** (`true`).
3. `a < b` $\to 5 < 8 \to$ **`1`** (`true`).
4. `b <= 8` $\to 8 \le 8 \to$ **`1`** (`true`).
5. `a > 5` $\to 5 > 5 \to$ **`0`** (`false`).
6. `a >= 5` $\to 5 \ge 5 \to$ **`1`** (`true`).
7. `b - a == 3` $\to 3 == 3 \to$ **`1`** (`true`).

---

### `B03-E02` *(Teste de Mesa — Múltiplos ifs Simples)*
Considere o trecho com `int x;`:
```c
if (x > 10) {
    printf("Maior que 10\n");
}
if (x % 2 == 0) {
    printf("Par\n");
}
if (x > 20) {
    printf("Maior que 20\n");
}
printf("Fim\n");
```
- **Para `x = 12`:**
  - `x > 10` ($12 > 10$) é verdadeiro $\to$ imprime `Maior que 10`.
  - `x % 2 == 0` ($12 \% 2 == 0$) é verdadeiro $\to$ imprime `Par`.
  - `x > 20` ($12 > 20$) é falso $\to$ não imprime.
  - Imprime `Fim`.  
  *Saída:*
  ```text
  Maior que 10
  Par
  Fim
  ```
- **Para `x = 7`:**
  - Todas as três condições são falsas.  
  *Saída:*
  ```text
  Fim
  ```

---

### `B03-E03` *(Caça ao Bug — 4 Erros Clássicos de Sintaxe)*
- **Erros intencionais no enunciado:**
  1. `if x > 0`: Falta de parênteses obrigatórios em torno da condição em C.
  2. `if (x > 0);`: Ponto e vírgula indevido após a condição, que encerra o comando do `if` como uma instrução vazia.
  3. `if (x = 10)`: Uso de operador de atribuição `=` em vez de comparação de igualdade `==`. Isso atribui 10 a `x`, avalia para 10 (verdadeiro!) e sempre executa o bloco.
  4. Omissão de chaves `{ }` quando há mais de uma instrução que deveria pertencer ao bloco condicional.
- **Solução corrigida completa:** [B03_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B03_E03_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int x;
    scanf("%d", &x);

    if (x > 0) {
        printf("Positivo\n");
    }

    if (x == 10) {
        printf("Numero igual a 10\n");
    }

    printf("Fim\n");
    return 0;
}
```

---

### `B03-E04` *(Completar Solução — Verificação de Paridade)*
Arquivo: [B03_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B03_E04.c)
```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    if (n % 2 == 0) {
        printf("O numero %d eh par\n", n);
    }

    printf("Fim do programa\n");
    return 0;
}
```

---

### `B03-E05` *(Resolução Independente — Radar de Velocidade)*
Arquivo: [B03_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B03_E05.c)
```c
#include <stdio.h>

int main(void) {
    double vel, multa;
    scanf("%lf", &vel);

    if (vel > 80.0) {
        multa = (vel - 80.0) * 5.0;
        printf("Multa: R$ %.2f\n", multa);
    }

    printf("Boa viagem\n");
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`B03-C01` a `B03-C03`)

### `B03-C01` *(Teste de Mesa — Limiar Estrito `>` vs. Inclusivo `>=`)*
Considere `double nota = 7.0;`:
```c
if (nota > 7.0) {
    printf("Aprovado direto\n");
}
if (nota >= 7.0) {
    printf("Atingiu a media\n");
}
```
- `nota > 7.0` $\to 7.0 > 7.0$ é **falso** (`0`). A mensagem `Aprovado direto` **não** é impressa.
- `nota >= 7.0` $\to 7.0 \ge 7.0$ é **verdadeiro** (`1`). A mensagem `Atingiu a media` **é** impressa.  
*Saída gerada:*
```text
Atingiu a media
```

---

### `B03-C02` *(Caça ao Bug — `;` após `if` e `=` vs `==`)*
- **Erros intencionais:**
  1. `if (n > 0);`: o `;` finaliza a instrução condicional. O bloco `{ printf("Positivo\n"); }` executa de forma incondicional mesmo para `n <= 0`.
  2. `if (n = 100)`: altera o valor de `n` para 100 e avalia como verdadeiro para qualquer entrada original.
- **Solução corrigida completa:** [B03_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B03_C02_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    if (n > 0) {
        printf("Positivo\n");
    }

    if (n == 100) {
        printf("Cem\n");
    }

    printf("Fim\n");
    return 0;
}
```

---

### `B03-C03` *(Programa Completo Independente — Desconto Simples sem else)*
Arquivo: [B03_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B03_C03.c)
```c
#include <stdio.h>

int main(void) {
    double valor;
    scanf("%lf", &valor);

    if (valor >= 100.0) {
        valor = valor * 0.90;
    }

    printf("Valor final: R$ %.2f\n", valor);
    return 0;
}
```
*(Para `valor = 100.00`, a condição `>= 100.0` é verdadeira e o desconto é aplicado, resultando em `R$ 90.00`).*
