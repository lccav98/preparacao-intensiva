# Gabarito Comentado — Bloco `B08` (Múltipla Escolha com `switch / case`)

> **Bloco de referência:** [B08_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/blocos/B08_bloco.md)  
> **Nota para Caça ao Bug:** Os códigos em `B08-E02` e `B08-C02` no bloco do aluno contêm **erros conceituais de tipo inválido, ausência de break e rótulos duplicados**. Apenas as versões corrigidas devem ser compiladas.

---

## 1. Gabarito dos Exercícios (`B08-E01` a `B08-E05`)

### `B08-E01` *(Teste de Mesa — Fall-Through sem break)*
Trecho analisado:
```c
switch (cod) {
    case 1: printf("A");
    case 2: printf("B");
    case 3: printf("C"); break;
    case 4: printf("D");
    default: printf("E");
}
```
1. **Para `cod = 2`:**
   - Entra no `case 2`, imprime `B`.
   - Como não há `break`, continua para o `case 3`, imprime `C`.
   - Encontra o `break` e encerra.
   - Saída: **`BC\n`**.
2. **Para `cod = 4`:**
   - Entra no `case 4`, imprime `D`.
   - Como não há `break`, continua para o `default`, imprime `E`.
   - Encerra o `switch`.
   - Saída: **`DE\n`**.
3. **Para `cod = 9`:**
   - Não casa com nenhum `case (1..4)`, cai no `default`, imprime `E`.
   - Saída: **`E\n`**.

---

### `B08-E02` *(Caça ao Bug — Restrições do switch)*
1. **Motivos de erro em C99:**
   - O `switch (peso)` tenta avaliar uma variável do tipo `double`. Em C, a expressão do `switch` deve ser estritamente de tipo integral (`int`, `char`, etc.).
   - `case 1.0:` tenta usar uma constante de ponto flutuante (`double`). Os rótulos `case` devem ser constantes inteiras.
   - `case limite:` tenta usar uma variável (`limite`). O valor após o `case` deve ser uma expressão constante conhecida em tempo de compilação.
2. **Versão corrigida completa:** [B08_E02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B08_E02_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int tipo;

    if (scanf("%d", &tipo) != 1) {
        return 1;
    }

    switch (tipo) {
        case 1:
            printf("Tarifa A\n");
            break;
        case 2:
            printf("Tarifa B\n");
            break;
        default:
            printf("Tarifa Padrao\n");
            break;
    }

    return 0;
}
```

---

### `B08-E03` *(Completar Solução — Vogais)*
```c
switch (c) {
    case 'a':
    case 'e':
    case 'i':
    case 'o':
    case 'u':
        printf("Vogal\n");
        break;
    default:
        printf("Outro Caractere\n");
        break;
}
```

---

### `B08-E04` *(Programa completo — Calculadora Básica)*
Arquivo: [B08_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B08_E04.c)
```c
#include <stdio.h>

int main(void) {
    double a, b;
    char op;

    if (scanf("%lf %lf %c", &a, &b, &op) != 3) {
        return 1;
    }

    switch (op) {
        case '+':
            printf("Resultado: %.2f\n", a + b);
            break;
        case '-':
            printf("Resultado: %.2f\n", a - b);
            break;
        case '*':
            printf("Resultado: %.2f\n", a * b);
            break;
        case '/':
            if (b == 0.0) {
                printf("Erro: Divisao por Zero\n");
            } else {
                printf("Resultado: %.2f\n", a / b);
            }
            break;
        default:
            printf("Operador Invalido\n");
            break;
    }

    return 0;
}
```

---

### `B08-E05` *(Programa completo — Dias da Semana)*
Arquivo: [B08_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B08_E05.c)
```c
#include <stdio.h>

int main(void) {
    int dia;

    if (scanf("%d", &dia) != 1) {
        return 1;
    }

    switch (dia) {
        case 1:
            printf("Domingo\n");
            break;
        case 2:
            printf("Segunda\n");
            break;
        case 3:
            printf("Terca\n");
            break;
        case 4:
            printf("Quarta\n");
            break;
        case 5:
            printf("Quinta\n");
            break;
        case 6:
            printf("Sexta\n");
            break;
        case 7:
            printf("Sabado\n");
            break;
        default:
            printf("Dia Invalido\n");
            break;
    }

    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`B08-C01` a `B08-C03`)

### `B08-C01` *(Teste de Mesa — Default Intermediário e Fall-Through)*
Trecho analisado:
```c
switch (n) {
    case 1: printf("Um "); break;
    default: printf("Zero ");
    case 2: printf("Dois "); break;
    case 3: printf("Tres ");
    case 4: printf("Quatro "); break;
}
```
1. **Para `n = 3`:**
   - Casa com `case 3`, imprime `Tres `.
   - Não há `break`, continua para `case 4`, imprime `Quatro `.
   - Encontra `break` e sai.
   - Saída: **`Tres Quatro \n`**.
2. **Para `n = 5`:**
   - Não casa com `1, 2, 3, 4`. Desvia para `default`, imprime `Zero `.
   - Como o `default` não possui `break`, o fluxo sofre *fall-through* para o próximo comando (`case 2`), imprimindo `Dois `.
   - Encontra o `break` do `case 2` e encerra.
   - Saída: **`Zero Dois \n`**.
3. **Para `n = 1`:**
   - Casa com `case 1`, imprime `Um `.
   - Encontra `break` imediatamente.
   - Saída: **`Um \n`**.

---

### `B08-C02` *(Caça ao Bug)*
1. **Erros no código original:**
   - **Rótulo duplicado:** Há dois blocos com `case 1:` (`case 1: printf("Saldo\n");` e mais abaixo `case 1: printf("Saque\n");`). Em C, valores duplicados de `case` são proibidos e impedem a compilação (*duplicate case value*).
   - **Ausência de `break`:** O primeiro `case 1:` não tem `break`, o que faria imprimir tanto `Saldo` quanto `Extrato`.
2. **Solução corrigida completa:** [B08_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B08_C02_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int op;

    if (scanf("%d", &op) != 1) {
        return 1;
    }

    switch (op) {
        case 1:
            printf("Saldo\n");
            break;
        case 2:
            printf("Extrato\n");
            break;
        case 3:
            printf("Saque\n");
            break;
        default:
            printf("Opcao Invalida\n");
            break;
    }

    return 0;
}
```

---

### `B08-C03` *(Programa completo — Categorização de Produtos)*
Arquivo: [B08_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B08_C03.c)
```c
#include <stdio.h>

int main(void) {
    int cod;

    if (scanf("%d", &cod) != 1) {
        return 1;
    }

    switch (cod) {
        case 1:
        case 2:
        case 3:
            printf("Alimento Nao-Perecivel\n");
            break;

        case 4:
        case 5:
        case 6:
            printf("Alimento Perecivel\n");
            break;

        case 7:
            printf("Vestuario\n");
            break;

        case 8:
        case 9:
        case 10:
            printf("Limpeza\n");
            break;

        default:
            printf("Codigo Invalido\n");
            break;
    }

    return 0;
}
```
