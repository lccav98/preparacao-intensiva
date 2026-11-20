# Gabarito Comentado — Bloco `C05` (Laço Contado `for`: Sintaxe, Padrões de Contagem, C99 e Erros *Off-by-One*)

> **Bloco de referência:** [C05_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/blocos/C05_bloco.md)  
> **Nota para Caça ao Bug:** Em `C05-E02`, o trecho original contém erros intencionais de início da contagem e *off-by-one*. Apenas a versão corrigida em `testes/solucoes/` deve ser compilada.

---

## 1. Gabarito dos Exercícios (`C05-E01` a `C05-E05`)

### `C05-E01` *(Teste de Mesa / Padrões de Contagem, Passo Variável e Escopo C99)*
1. **Saídas e contagens de iterações:**
   - **Trecho A (`0 .. 3`):** imprime `0 1 2 3 ` | **4 iterações** (`i = 0, 1, 2, 3`, encerra quando `i` chega a `4`).
   - **Trecho B (`4 .. 0`):** imprime `4 3 2 1 0 ` | **5 iterações** (`i = 4, 3, 2, 1, 0`, encerra quando `i` chega a `-1`).
   - **Trecho C (passo `+3`):** `i` assume `2, 5, 8, 11, 14` (5 iterações) e ao final atualiza para `17` (`17 <= 14` falso).  
     Saída exata: `2 5 8 11 14 | Final=17` | **5 iterações**.
2. **Erro de compilação no Trecho D:** Em C99, a variável `k` declarada dentro do cabeçalho `for (int k = 0; ...)` possui escopo restrito ao próprio laço `for`. Ao tentar acessá-la na linha `printf("Fim=%d\n", k);` após o `}`, o compilador acusa identificador não declarado (`'k' undeclared`).  
   - **Correção:** Declarar `int k;` antes do laço e usar `for (k = 0; k < 3; k++)`.

---

### `C05-E02` *(Caça ao Bug — Off-by-One e Início em `0`)*
1. **Para `n = 4` no código original:** O laço executa **5 vezes** (`i = 0, 1, 2, 3, 4`) e imprime 5 linhas:
   ```text
   0
   3
   6
   9
   12
   ```
2. **Dois erros no cabeçalho `for (int i = 0; i <= n; i++)`:**
   - **Ponto inicial errado:** começa em `i = 0`, imprimindo `0 * 3 = 0`, que não é um múltiplo *positivo* (o padrão `1 .. n` exige iniciar em `i = 1`).
   - **Combinação *off-by-one*:** usar início `0` junto com `<= n` produz `n + 1` iterações (para `n = 4`, imprime 5 valores em vez de 4). Com início em `1`, o limite inclusivo `<= n` produz exatamente `n` múltiplos (`1, 2, ..., n`).
3. **Versão corrigida completa:** [C05_E02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C05_E02_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int n;

    scanf("%d", &n);

    for (int i = 1; i <= n; i++) {
        printf("%d\n", i * 3);
    }

    return 0;
}
```

---

### `C05-E03` *(Completar Solução — Conversão `while` $\rightarrow$ `for` para Fatorial)*
- **Lacuna `/* A */`:** `int i = 1`
- **Lacuna `/* B */`:** `i <= n`
- **Lacuna `/* C */`:** `i++`
- **Lacuna `/* D */`:** `fat *= i`
- **Código completo:** [C05_E03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C05_E03.c)
```c
#include <stdio.h>

int main(void) {
    int n;
    long long fat = 1;

    scanf("%d", &n);

    for (int i = 1; i <= n; i++) {
        fat *= i;
    }

    printf("%d! = %lld\n", n, fat);
    return 0;
}
```
*Comentário:* Para `n = 0`, o teste inicial `1 <= 0` já é falso, executando 0 iterações e preservando `fat = 1` (`0! = 1`).

---

### `C05-E04` *(Completar Solução — Contagem Regressiva com Passo Variável)*
- **Lacuna 1:** `int i = inicio`
- **Lacuna 2:** `i >= 1`
- **Lacuna 3:** `i -= passo`
- **Código completo:** [C05_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C05_E04.c)
```c
#include <stdio.h>

int main(void) {
    int inicio, passo;
    int qtd = 0;

    scanf("%d %d", &inicio, &passo);

    for (int i = inicio; i >= 1; i -= passo) {
        printf("%d\n", i);
        qtd++;
    }

    printf("Contagem: %d\n", qtd);
    return 0;
}
```

---

### `C05-E05` *(Programa Completo Independente — Filtro Múltiplo de 3 e Não-Múltiplo de 5)*
Arquivo: [C05_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C05_E05.c)
```c
#include <stdio.h>

int main(void) {
    int n;
    int qtd = 0;
    int soma = 0;

    scanf("%d", &n);

    for (int i = 1; i <= n; i++) {
        if (i % 3 == 0 && i % 5 != 0) {
            printf("%d\n", i);
            qtd++;
            soma += i;
        }
    }

    printf("Quantidade: %d\n", qtd);
    printf("Soma: %d\n", soma);
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`C05-C01` a `C05-C03`)

### `C05-C01` *(Teste de Mesa / Passo != 1 e Erro Off-by-One)*
1. **Trecho 1 (`k -= 3`):**
   - Iteração 1: `k = 10` (`10 > 0` V) $\rightarrow$ `s = 10`.
   - Iteração 2: `k = 7` (`7 > 0` V) $\rightarrow$ `s = 17`.
   - Iteração 3: `k = 4` (`4 > 0` V) $\rightarrow$ `s = 21`.
   - Iteração 4: `k = 1` (`1 > 0` V) $\rightarrow$ `s = 22`.
   - Atualização para `-2`: `-2 > 0` (F) $\rightarrow$ sai do laço.
   - **Total de iterações:** `4`. **Saída exata:** `s=22`.
2. **Trecho 2 (*off-by-one*):**
   - Imprime **6 números** (`0 1 2 3 4 5`).
   - **Erro cometido:** ao iniciar em `0`, o operador inclusivo `<= 5` inclui o `5`, gerando 1 iteração a mais (*off-by-one*) do que os 5 índices desejados.
   - **Condição correta:** `j < 5` (padrão `0 .. n-1`: `for (int j = 0; j < 5; j++)`).

---

### `C05-C02` *(Conversão `while` $\leftrightarrow$ `for` Respeitando Escopo C99)*
1. **Análise de escopo C99:**
   - **Caso A (removendo `int i;` externo e usando `for (int i = a; ...)`):** o programa **não compila**, pois `i` existe apenas dentro do escopo do `for` e o `printf("Proximo i: %d\n", i);` falha por variável não declarada.
   - **Caso B (mantendo `int i;` externo e também escrevendo `for (int i = a; ...)`):** ocorre **sombreamento (*shadowing*)** — o `for` cria uma variável interna distinta que morre no `}`, enquanto o `printf` externo lê o `i` externo **não inicializado** (lixo de memória / comportamento indefinido)!
2. **Versão corrigida completa:** [C05_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C05_C02_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int a, b;
    int soma = 0;
    int i;

    scanf("%d %d", &a, &b);

    for (i = a; i <= b; i++) {
        if (i % 2 == 0) {
            soma += i;
        }
    }

    printf("Soma pares: %d\n", soma);
    printf("Proximo i: %d\n", i);
    return 0;
}
```

---

### `C05-C03` *(Programa Completo Independente — Estatísticas com `for` e Filtros Lógicos)*
Arquivo: [C05_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C05_C03.c)
```c
#include <stdio.h>

int main(void) {
    int n;
    int qtd_par_ou_m7 = 0;
    int soma_impares_gt5 = 0;
    int soma_total = 0;

    scanf("%d", &n);

    if (n <= 0) {
        printf("Entrada invalida\n");
    } else {
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0 || i % 7 == 0) {
                qtd_par_ou_m7++;
            }
            if (i % 2 != 0 && i > 5) {
                soma_impares_gt5 += i;
            }
            soma_total += i;
        }

        printf("Qtd par ou mult7: %d\n", qtd_par_ou_m7);
        printf("Soma impares > 5: %d\n", soma_impares_gt5);
        printf("Media total: %.2f\n", (double)soma_total / n);
    }

    return 0;
}
```
*Comentário:* Os dois `if`s independentes permitem que um número ímpar múltiplo de 7 maior que 5 (ex.: `7`) seja contado em `qtd_par_ou_m7` e também somado em `soma_impares_gt5`, enquanto o operador `||` evita contar duas vezes números pares múltiplos de 7 (ex.: `14`).
