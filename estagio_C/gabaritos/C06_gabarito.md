# Gabarito Comentado — Bloco `C06` (Rastreamento de `for`, Efeitos Colaterais e Comando Nulo)

> **Bloco de referência:** [C06_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/blocos/C06_bloco.md)  
> **Nota para Caça ao Bug:** Os códigos em `C06-E04` e `C06-C01` contêm erros conceituais clássicos (desigualdade exata gerando laço infinito e comando nulo `;`). As versões corrigidas compiláveis encontram-se em `testes/solucoes/`.

---

## 1. Gabarito dos Exercícios (`C06-E01` a `C06-E05`)

### `C06-E01` *(Rastreamento de `for` com `i++` no Corpo e na Atualização)*
Código analisado:
```c
int i;
for (i = 0; i < 10; i += 2) {
    printf("%d ", i);
    i++;
}
printf("\nFinal: %d\n", i);
```

**Tabela de Rastreamento Passo a Passo:**

| Iteração | Teste de Entrada (`i < 10`) | Impressão | Corpo (`i++`) | Atualização (`i += 2`) |
|:---:|:---:|:---:|:---:|:---:|
| **1** | `0 < 10` (Verdadeiro) | Imprime `0 ` | `i` vira `1` | `i` vira `3` |
| **2** | `3 < 10` (Verdadeiro) | Imprime `3 ` | `i` vira `4` | `i` vira `6` |
| **3** | `6 < 10` (Verdadeiro) | Imprime `6 ` | `i` vira `7` | `i` vira `9` |
| **4** | `9 < 10` (Verdadeiro) | Imprime `9 ` | `i` vira `10` | `i` vira `12` |
| **Fim** | `12 < 10` (Falso) | *(laço encerra)* | — | — |

**Saída Impressa na Tela:**
```text
0 3 6 9 
Final: 12
```
*Total de iterações executadas:* 4.  
*Valor final da variável de controle:* `12`.

---

### `C06-E02` *(Diagnóstico do Bug do Ponto e Vírgula `;` após `for`)*
1. **Explicação:** Em linguagem C, o ponto e vírgula `;` imediatamente após o cabeçalho `for (i = 1; i <= 5; i++);` é interpretado como uma **instrução vazia (comando nulo)**. Portanto, o laço executa repetidamente essa instrução nula por 5 vezes, apenas incrementando a variável `i`. Quando `i` atinge o valor `6`, a condição `6 <= 5` torna-se falsa e o laço encerra. O bloco `{ fat *= i; }` que aparece em seguida é um bloco de código comum, fora do laço, que é executado **uma única vez** com `i = 6`. Como `fat` foi inicializado com `1`, o cálculo realizado foi simplesmente `fat = 1 * 6 = 6`.
2. **Linha corrigida:**
   ```c
   for (i = 1; i <= 5; i++)
   ```
   *(Basta remover o caractere `;` no final da linha do `for`).*

---

### `C06-E03` *(Rastreamento do Caso UTFPR Lista 5 Ex. 1 — Divisão Inteira e Laço Infinito)*
Código:
```c
int i;
for (i = 10; i >= 1; i /= 2) {
    printf("%d ", i++);
}
```

1. **Tabela de Rastreamento Passo a Passo:**

| Iteração | Teste (`i >= 1`) | `printf("%d ", i++)` | Valor de `i` pós-print | Atualização `i /= 2` | Novo `i` para próxima volta |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | `10 >= 1` (V) | Imprime `10 ` | `11` | `11 / 2 = 5` | `5` |
| **2** | `5 >= 1` (V) | Imprime `5 ` | `6` | `6 / 2 = 3` | `3` |
| **3** | `3 >= 1` (V) | Imprime `3 ` | `4` | `4 / 2 = 2` | `2` |
| **4** | `2 >= 1` (V) | Imprime `2 ` | `3` | `3 / 2 = 1` | `1` |
| **5** | `1 >= 1` (V) | Imprime `1 ` | `2` | `2 / 2 = 1` | `1` |
| **6** | `1 >= 1` (V) | Imprime `1 ` | `2` | `2 / 2 = 1` | `1` |

2. **Refutação do erro da `Lista do Professor.pdf`:** Na página 2 do material desqualificado, o autor alegou que o programa terminava porque na iteração com `i = 2` ocorreria "2 / 2 = 0". Esse é um erro aritmético elementar: na divisão inteira em C, `2 / 2` resulta exatamente em `1`, e **nunca** em `0`.
3. **Demonstração analítica da não-terminação:** Quando `i = 1`, o teste `1 >= 1` é verdadeiro. O `printf` imprime `1` e o pós-incremento `i++` altera `i` para `2`. Na fase de atualização, calcula-se `i = i / 2`, o que resulta em `2 / 2 = 1`. Dessa forma, o valor de `i` no início da próxima iteração volta a ser `1`. Isso cria um ponto fixo cíclico ($1 \rightarrow 2 \rightarrow 1$), aprisionando o programa em um **laço infinito** que imprime indefinidamente o número `1`:
   ```text
   10 5 3 2 1 1 1 1 1 1 1 ...
   ```

---

### `C06-E04` *(Caça ao Bug — Laço Infinito por Desigualdade Exata `!=`)*
1. **Para `n = 5`:** Os valores de `i` são `1, 3, 5`. Quando `i = 5`, a condição `i != 5` torna-se falsa e o laço encerra. Imprime `Soma = 4` ($1 + 3$). O programa aparentemente funcionou (embora não tenha somado o 5).
2. **Para `n = 6`:** A variável `i` assume os valores `1, 3, 5, 7, 9...` Como `i` é incrementado de 2 em 2, ele salta diretamente sobre o número `6` sem nunca ser igual a ele. A condição `i != 6` será verdadeira para sempre, resultando em um **laço infinito** com estouro de inteiros.
3. **Programa corrigido completo:** [C06_E04_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C06_E04_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int n;
    if (scanf("%d", &n) != 1) {
        return 1;
    }

    int soma = 0;
    for (int i = 1; i <= n; i += 2) {
        soma += i;
    }

    printf("Soma = %d\n", soma);
    return 0;
}
```

---

### `C06-E05` *(Programa Completo — Sequência de Collatz / $3n+1$ Limitada)*
Solução completa: [C06_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C06_E05.c)
```c
#include <stdio.h>

int main(void) {
    long long n;
    if (scanf("%lld", &n) != 1 || n <= 0) {
        printf("Entrada Invalida\n");
        return 0;
    }

    long long atual = n;
    int passos = 0;

    printf("%lld", atual);
    while (atual != 1 && passos < 200) {
        if (atual % 2 == 0) {
            atual = atual / 2;
        } else {
            atual = 3 * atual + 1;
        }
        passos++;
        printf(" %lld", atual);
    }
    printf("\n");
    printf("Passos: %d\n", passos);

    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`C06-C01` a `C06-C03`)

### `C06-C01` *(Teste de Mesa sem Computador — Comando Nulo em `while`)*
1. **Análise:** Devido ao ponto e vírgula imediatamente após `while (k < 5);`, o compilador executa a instrução nula enquanto `k < 5`. Como `k` inicia com `1` e a instrução vazia não altera o valor de `k`, a condição `1 < 5` permanece eternamente verdadeira. O programa entra em **laço infinito travado**, consumindo 100% de CPU sem produzir qualquer saída na tela. O comando `printf` jamais será alcançado.
2. **Código reescrito corretamente:**
   ```c
   int c = 0, k = 1;
   while (k < 5) {
       c += k++;
   }
   printf("%d %d\n", c, k);
   ```
   *Saída do código corrigido:* `10 5` (pois $1 + 2 + 3 + 4 = 10$ e `k` termina em 5).

---

### `C06-C02` *(Rastreamento de Efeito Colateral Finito no Corpo)*
Código:
```c
int total = 0;
for (int i = 20; i > 2; i -= 3) {
    if (i % 2 == 0) {
        i--;
    }
    total += i;
}
printf("Total = %d\n", total);
```

**Tabela de Rastreamento Passo a Passo:**

| Iteração | `i` inicial | `i > 2`? | `i % 2 == 0`? | `i` após `if` | `total += i` | Atualização `i -= 3` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | `20` | Sim (`20 > 2`) | Sim (`20 % 2 == 0`) | `19` | `total = 0 + 19 = 19` | `19 - 3 = 16` |
| **2** | `16` | Sim (`16 > 2`) | Sim (`16 % 2 == 0`) | `15` | `total = 19 + 15 = 34` | `15 - 3 = 12` |
| **3** | `12` | Sim (`12 > 2`) | Sim (`12 % 2 == 0`) | `11` | `total = 34 + 11 = 45` | `11 - 3 = 8` |
| **4** | `8` | Sim (`8 > 2`) | Sim (`8 % 2 == 0`) | `7` | `total = 45 + 7 = 52` | `7 - 3 = 4` |
| **5** | `4` | Sim (`4 > 2`) | Sim (`4 % 2 == 0`) | `3` | `total = 52 + 3 = 55` | `3 - 3 = 0` |
| **Fim** | `0` | Não (`0 > 2` é Falso) | — | — | — | *(encerra o laço)* |

**Saída Exata:**
```text
Total = 55
```

---

### `C06-C03` *(Programa Completo — Redução Numérica e Soma de Dígitos Controlada)*
Solução completa: [C06_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C06_C03.c)
```c
#include <stdio.h>

int main(void) {
    long long n;
    if (scanf("%lld", &n) != 1 || n <= 0) {
        printf("Valor Invalido\n");
        return 0;
    }

    long long temp = n;
    int soma = 0;
    int digitos = 0;

    while (temp > 0) {
        soma += (int)(temp % 10);
        digitos++;
        temp /= 10;
    }

    printf("Soma = %d\n", soma);
    printf("Digitos = %d\n", digitos);

    return 0;
}
```
