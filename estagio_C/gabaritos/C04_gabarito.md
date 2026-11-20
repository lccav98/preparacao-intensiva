# Gabarito Comentado — Bloco `C04` (Repetição com Pós-Condição `do-while` e Menus Interativos)

> **Bloco de referência:** [C04_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/blocos/C04_bloco.md)  
> **Nota para Caça ao Bug:** Em `C04-E02` e `C04-C02`, os trechos originais possuem erros propositais de sintaxe (ausência de `;` após `while (...)`) e de lógica booleana (condição invertida). Apenas as versões corrigidas devem ser compiladas.

---

## 1. Gabarito dos Exercícios (`C04-E01` a `C04-E05`)

### `C04-E01` *(Teste de Mesa / Comparação `while` vs. `do-while`)*
1. **Trecho A (`while`):**
   - `a = 8`. Teste `8 <= 5` é **Falso** logo na 1ª verificação.
   - **Iterações:** `0`.
   - **Saída:** `Fim=8`
   - **Valor final de `a`:** `8`.

2. **Trecho B (`do-while`):**
   - `b = 8`. Entra no corpo antes do teste: imprime `8 ` e `b` vira `9`.
   - Testa `9 <= 5` (**Falso**) e encerra o laço.
   - **Iterações:** `1`.
   - **Saída:** `8 Fim=9`
   - **Valor final de `b`:** `9`.

3. **Trecho C (`do-while` com passo 2):**
   - Iteração 1: imprime `1 `, `k` vira `3`. Testa `3 <= 5` (V).
   - Iteração 2: imprime `3 `, `k` vira `5`. Testa `5 <= 5` (V).
   - Iteração 3: imprime `5 `, `k` vira `7`. Testa `7 <= 5` (F) e encerra.
   - **Iterações:** `3`.
   - **Saída:** `1 3 5 Fim=7`
   - **Valor final de `k`:** `7`.

---

### `C04-E02` *(Caça ao Bug — Falta de `;` e Condição Invertida na Validação)*
1. **Erro de sintaxe:** Falta o ponto e vírgula `;` obrigatório ao final da linha `} while (nota >= 0 && nota <= 10);`. Sem ele, o compilador acusa erro antes da instrução seguinte (`printf`).
2. **Comportamento lógico da condição invertida `nota >= 0 && nota <= 10`:**
   - Se o usuário digitar **`8`** (válida): não entra no `if`, mas `8 >= 0 && 8 <= 10` é **Verdadeiro**, obrigando o programa a pedir uma nova nota em vez de aceitar `8` e sair.
   - Se o usuário digitar **`-2`** (inválida): imprime `Nota invalida`, mas `-2 >= 0 && -2 <= 10` é **Falso**, encerrando o laço imediatamente e registrando a nota inválida `-2`!
3. **Versão corrigida completa:** [C04_E02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C04_E02_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int nota;

    do {
        scanf("%d", &nota);
        if (nota < 0 || nota > 10) {
            printf("Nota invalida\n");
        }
    } while (nota < 0 || nota > 10);

    printf("Nota registrada: %d\n", nota);
    return 0;
}
```

---

### `C04-E03` *(Completar Solução — Validação de Divisor Não-Nulo)*
- **Lacuna `/* A */`:** `do`
- **Lacuna `/* B */`:** `printf("Divisor invalido\n");`
- **Lacuna `/* C */`:** `while (divisor == 0.0);`
- **Código completo:** [C04_E03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C04_E03.c)
```c
#include <stdio.h>

int main(void) {
    double numerador, divisor;

    scanf("%lf", &numerador);

    do {
        scanf("%lf", &divisor);
        if (divisor == 0.0) {
            printf("Divisor invalido\n");
        }
    } while (divisor == 0.0);

    printf("Resultado: %.2f\n", numerador / divisor);
    return 0;
}
```

---

### `C04-E04` *(Completar Solução — Menu Interativo de Caixa Eletrônico)*
- **Lacuna 1:** `opcao`
- **Lacuna 2:** `default`
- **Lacuna 3:** `while (opcao != 0);`
- **Código completo:** [C04_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C04_E04.c)
```c
#include <stdio.h>

int main(void) {
    double saldo = 100.0;
    double valor;
    int opcao;

    do {
        scanf("%d", &opcao);
        switch (opcao) {
            case 1:
                scanf("%lf", &valor);
                if (valor > 0.0) {
                    saldo += valor;
                    printf("Saldo: %.2f\n", saldo);
                } else {
                    printf("Valor invalido\n");
                }
                break;
            case 2:
                scanf("%lf", &valor);
                if (valor > 0.0 && valor <= saldo) {
                    saldo -= valor;
                    printf("Saldo: %.2f\n", saldo);
                } else {
                    printf("Operacao invalida\n");
                }
                break;
            case 3:
                printf("Saldo: %.2f\n", saldo);
                break;
            case 0:
                printf("Encerrando\n");
                break;
            default:
                printf("Opcao invalida\n");
                break;
        }
    } while (opcao != 0);

    return 0;
}
```

---

### `C04-E05` *(Programa Completo Independente — Menu Acumulador de Total)*
Arquivo: [C04_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C04_E05.c)
```c
#include <stdio.h>

int main(void) {
    int total = 0;
    int opcao, v;

    do {
        scanf("%d", &opcao);
        switch (opcao) {
            case 1:
                scanf("%d", &v);
                total += v;
                printf("Total: %d\n", total);
                break;
            case 2:
                scanf("%d", &v);
                total -= v;
                printf("Total: %d\n", total);
                break;
            case 3:
                total = 0;
                printf("Total: %d\n", total);
                break;
            case 0:
                printf("Final: %d\n", total);
                break;
            default:
                printf("Opcao invalida\n");
                break;
        }
    } while (opcao != 0);

    return 0;
}
```
*Comentário:* Cada `break` encerra apenas o `switch` interno, devolvendo o fluxo para o teste `while (opcao != 0);`.

---

## 2. Gabarito da Checagem Independente (`C04-C01` a `C04-C03`)

### `C04-C01` *(Teste de Mesa / Previsão Comparativa `while` vs. `do-while`)*
1. **Trecho 1 (`while`):** Como `n = 5`, o teste `5 < 5` é **Falso** antes de entrar no corpo. Executa **0 iterações** e imprime exatamente: `Fim: 5`.
2. **Trecho 2 (`do-while`):** Executa o corpo **1 iteração** antes de testar a condição: `n` passa de `5` para `7` e imprime `7 `. Só então avalia `7 < 5` (**Falso**) e sai do laço, imprimindo `Fim: 7`. Saída exata completa: `7 Fim: 7`.
3. **Justificativa da divergência:** O `while` realiza **pré-teste** (pode executar 0 vezes se a condição começar falsa), enquanto o `do-while` realiza **pós-teste** (o corpo executa obrigatoriamente pelo menos 1 vez antes da primeira avaliação da condição).

---

### `C04-C02` *(Caça ao Bug — Condição de Saída e Ponto e Vírgula em Menu)*
1. **Dois erros na linha do `while`:**
   - Falta o ponto e vírgula `;` obrigatório ao final de `while (op == 0);`.
   - Condição invertida: `op == 0` faz o menu repetir *apenas* quando o usuário escolhe sair (`0`) e encerrar em qualquer outra opção, quando o correto é `op != 0`.
2. **Efeito lógico (apenas com `;` corrigido):**
   - Entrada `1 0`: lê `1`, adiciona o item, testa `1 == 0` (**Falso**) e **encerra o programa imediatamente**, deixando de ler o `0`.
   - Entrada `0`: lê `0`, imprime `Total: 0`, testa `0 == 0` (**Verdadeiro**) e **não sai do menu**, tentando ler outra opção (em entrada finita causaria leitura repetida até EOF ou loop inesperado).
3. **Versão corrigida completa:** [C04_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C04_C02_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int op;
    int cont = 0;

    do {
        scanf("%d", &op);
        switch (op) {
            case 1:
                cont++;
                printf("Item adicionado\n");
                break;
            case 0:
                printf("Total: %d\n", cont);
                break;
            default:
                printf("Opcao invalida\n");
                break;
        }
    } while (op != 0);

    return 0;
}
```

---

### `C04-C03` *(Programa Completo Independente — Menu de Calculadora com Validação Interna)*
Arquivo: [C04_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C04_C03.c)
```c
#include <stdio.h>

int main(void) {
    int op, a, b;

    do {
        scanf("%d", &op);
        switch (op) {
            case 1:
                scanf("%d %d", &a, &b);
                printf("Resultado: %d\n", a + b);
                break;
            case 2:
                scanf("%d %d", &a, &b);
                printf("Resultado: %d\n", a * b);
                break;
            case 3:
                scanf("%d", &a);
                do {
                    scanf("%d", &b);
                    if (b == 0) {
                        printf("Divisor invalido\n");
                    }
                } while (b == 0);
                printf("Resultado: %d\n", a / b);
                break;
            case 0:
                printf("Saindo\n");
                break;
            default:
                printf("Opcao invalida\n");
                break;
        }
    } while (op != 0);

    return 0;
}
```
*Comentário:* Combina um laço `do-while` externo (menu com `switch`) e um laço `do-while` interno no `case 3` para impedir divisão por zero antes da execução de `a / b`.
