# Bloco `C02` — Contadores e Acumuladores com `while`

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio C — Estruturas de Repetição e Rastreamento de Laços / **`C02`** |
| **Micro-habilidade foco** | Combinar contadores, acumuladores inicializados, filtragem condicional interna (`if` dentro do `while`) e redução iterativa sem operador `%`. |
| **Pré-requisitos** | `C01` *(Repetição com Pré-Condição `while`)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão única de prática + checagem (22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Não utilize** `do-while` ou `for`, comandos de salto (`break`, `continue`), vetores ou funções customizadas além de `main`. Use estritamente o laço `while`, tipos escalares (`int`, `double`), condicionais `if/else` e saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Padrão Contador (`conta++`):** Uma variável inteira destinada a registrar a quantidade de vezes que um evento ou critério ocorre.
   - **Regra obrigatória:** Deve ser inicializada com `0` *antes* do início do laço (`int conta = 0;`).
   - A cada ocorrência válida, é incrementada de 1: `conta++;` ou `conta = conta + 1;`.
2. **Padrão Acumulador (`soma += valor`):** Uma variável que totaliza valores parciais variáveis ao longo das iterações.
   - **Regra obrigatória:** Deve ser inicializada com `0` (o elemento neutro da adição) antes do laço (`int soma = 0;`). Se fosse produto acumulado, o neutro seria `1`.
   - A cada iteração relevante, recebe o valor corrente: `soma += x;` ou `soma = soma + x;`.
3. **O Perigo da Variável Não Inicializada:** Em C, variáveis locais não inicializadas contêm "lixo de memória" (resíduos de bits deixados por execuções anteriores na pilha). Fazer `soma += x;` sem zerar `soma` produz um resultado imprevisível e incorreto.
4. **Filtragem Condicional (`if` dentro do `while`):** O laço `while` atua como motor de percurso por uma sequência de elementos, enquanto o `if` interno atua como filtro decisório, selecionando quais elementos participam da contagem ou acumulação.
5. **Divisão Inteira e Resto por Subtrações Sucessivas (Sem `%` nem `/`):**
   - Para dividir `dividendo` por `divisor`: subtrai-se repetidamente `divisor` do `dividendo` e conta-se quantas subtrações foram feitas.
   - **Cuidado crítico de fronteira (`>=` vs `>`):** A repetição deve continuar enquanto `resto >= divisor`. Se for utilizado `>`, o algoritmo falha gravemente para múltiplos exatos (exemplo: ao dividir `10` por `5`, a subtração pararia prematuramente em `resto = 5` com `quociente = 1`, em vez de subtrair mais uma vez para obter `resto = 0` e `quociente = 2`).

---

## 2. Exemplos Guiados

### Exemplo 1 — Contagem e acumulação seletiva *(Trecho ilustrativo)*
Considere somar os números ímpares e contar quantos são múltiplos de 3 no intervalo de 1 a 6:

```c
int i = 1;
int soma_impares = 0;   /* Acumulador zerado */
int qtd_mult3 = 0;      /* Contador zerado */

while (i <= 6) {
    if (i % 2 != 0) {
        soma_impares += i;
    }
    if (i % 3 == 0) {
        qtd_mult3++;
    }
    i++;
}
```

**Tabela de Teste de Mesa:**

| `i` | `i % 2 != 0`? | `soma_impares` | `i % 3 == 0`? | `qtd_mult3` | Próximo `i` |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | V (1 é ímpar) | $0 + 1 = 1$ | F | 0 | 2 |
| 2 | F | 1 | F | 0 | 3 |
| 3 | V (3 é ímpar) | $1 + 3 = 4$ | V (3 é mult 3) | $0 + 1 = 1$ | 4 |
| 4 | F | 4 | F | 1 | 5 |
| 5 | V (5 é ímpar) | $4 + 5 = 9$ | F | 1 | 6 |
| 6 | F | 9 | V (6 é mult 3) | $1 + 1 = 2$ | 7 |
| 7 | *(sai do laço: `7 <= 6` é falso)* | | | | |

Resultado final: `soma_impares = 9` e `qtd_mult3 = 2`.

---

### Exemplo 2 — Divisão inteira e resto por subtrações sucessivas *(Programa completo)*
O programa abaixo calcula o quociente e o resto da divisão inteira de dois números inteiros positivos sem utilizar os operadores `/` ou `%`:

```c
#include <stdio.h>

int main(void) {
    int dividendo, divisor;
    int quociente = 0;   /* Contador de subtracoes */
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
Se a entrada for `14 4`:
- Início: `resto = 14`, `quociente = 0`.
- 1ª subtração: `resto = 10`, `quociente = 1`.
- 2ª subtração: `resto = 6`, `quociente = 2`.
- 3ª subtração: `resto = 2`, `quociente = 3`.
- Teste `2 >= 4` é falso. Término: `Quociente: 3`, `Resto: 2`. (Prova: $4 \times 3 + 2 = 14$).

---

## 3. Exercícios (`C02-E01` a `C02-E05`)

### `C02-E01` *(Teste de Mesa / Rastreamento de Contador e Acumulador)*
Sem usar o computador, preencha a tabela de rastreamento para o trecho abaixo e determine o valor final das variáveis `soma` e `conta`:

```c
int num = 1;
int soma = 0;
int conta = 0;

while (num <= 5) {
    if (num % 2 == 0) {
        soma += num;
        conta++;
    }
    num++;
}
```
1. Quais números entraram no `if`?
2. Qual o valor final de `soma`?
3. Qual o valor final de `conta`?
4. Qual o valor final de `num`?

---

### `C02-E02` *(Caça ao Bug — Variável Não Zerada e Resto de Múltiplos Exatos)*
Um estudante escreveu o programa abaixo para calcular a divisão inteira por subtrações sucessivas de `a` por `b`:

```c
#include <stdio.h>

int main(void) {
    int a, b;
    int quociente;    /* Bug 1 */
    int resto;

    scanf("%d %d", &a, &b);

    resto = a;
    while (resto > b) {   /* Bug 2 */
        resto = resto - b;
        quociente++;
    }

    printf("Quociente: %d\n", quociente);
    printf("Resto: %d\n", resto);
    return 0;
}
```
1. Explique por que a variável `quociente` causa comportamento indefinido no programa.
2. Suponha que a entrada seja `15 5`. Qual saída incorreta a condição `while (resto > b)` produzirá para `quociente` e `resto`?
3. Escreva a versão corrigida completa e funcional do programa em C.

---

### `C02-E03` *(Completar Solução — Tabuada com while)*
O programa a seguir deve ler um número inteiro `n` e imprimir a sua tabuada de multiplicação de 1 a 10 no formato exato:  
`%d x %d = %d\n`  
Complete as lacunas `/* A */`, `/* B */` e `/* C */`:

```c
#include <stdio.h>

int main(void) {
    int n;
    int i = /* A */;
    scanf("%d", &n);

    while (/* B */) {
        printf("%d x %d = %d\n", n, i, n * i);
        /* C */;
    }

    return 0;
}
```

---

### `C02-E04` *(Completar Solução — Divisão por Subtrações Sucessivas)*
Complete o programa em C que lê dois números inteiros positivos (`dividendo` e `divisor`, com `divisor > 0`) e calcula o quociente e o resto da divisão inteira sem utilizar `/` nem `%`:

```c
#include <stdio.h>

int main(void) {
    int dividendo, divisor;
    int quociente = 0;
    int resto;

    scanf("%d %d", &dividendo, &divisor);

    resto = dividendo;
    while (/* Lacuna 1: condicao */) {
        resto = /* Lacuna 2 */;
        /* Lacuna 3: incrementa quociente */;
    }

    printf("Quociente: %d\n", quociente);
    printf("Resto: %d\n", resto);
    return 0;
}
```

---

### `C02-E05` *(Resolução Independente — Soma e Contagem de Pares em Intervalo)*
Escreva um programa completo em C que leia dois números inteiros `a` e `b` ($a \le b$).  
Usando um laço `while`, percorra todos os números de `a` até `b` (inclusive) e determine:
- Quantos números são pares (contador).
- A soma desses números pares (acumulador).

Imprima exatamente:
```text
Quantidade: %d\n
Soma: %d\n
```
Se não houver nenhum número par no intervalo, o programa deve imprimir:
```text
Quantidade: 0\n
Soma: 0\n
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `C02-C01` *(Teste de Mesa / Acumulação com Filtros Lógicos)*
Sem usar o computador, analise o trecho a seguir:

```c
int i = 1;
int soma = 0;
int qtd = 0;

while (i <= 10) {
    if (i % 3 == 0 || i % 5 == 0) {
        soma += i;
        qtd++;
    }
    i++;
}
```
1. Liste todos os valores de `i` que satisfazem a condição do `if`.
2. Qual o valor final da variável `qtd`?
3. Qual o valor final da variável `soma`?

---

### `C02-C02` *(Caça ao Bug — Resto de Múltiplo Exato)*
Um desenvolvedor escreveu a seguinte lógica para calcular o resto da divisão inteira de `a` por `b` por subtrações sucessivas:

```c
#include <stdio.h>

int main(void) {
    int a, b;
    int resto;
    scanf("%d %d", &a, &b);

    resto = a;
    while (resto > b) {
        resto -= b;
    }

    printf("Resto: %d\n", resto);
    return 0;
}
```
1. Teste mentalmente o programa para `a = 12` e `b = 4`. Qual valor é impresso para `Resto`? Qual deveria ser o valor correto?
2. Explique a razão matemática do erro e forneça o código corrigido completo.

---

### `C02-C03` *(Programa Completo Independente — Estatísticas de Intervalo)*
Escreva um programa completo em C que leia dois inteiros `inicio` e `fim` ($inicio \le fim$).  
Usando um laço `while`, o programa deve percorrer o intervalo fechado $[inicio, fim]$ e calcular:
1. A quantidade de números que são ímpares.
2. A soma de todos os números que são múltiplos de 3.

A saída deve imprimir estritamente:
```text
Impares: %d\n
Soma mult 3: %d\n
```

Exemplo de entrada:
```text
1 6
```
Exemplo de saída:
```text
Impares: 3
Soma mult 3: 9
```
*(Explicação: Ímpares no intervalo: 1, 3, 5 $\rightarrow$ total 3. Múltiplos de 3: 3 e 6 $\rightarrow$ soma 9).*

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `C03` (`Leituras por Sentinela e Algoritmos Iterativos com while`):** somente após autocorreção dos exercícios `C02-E01..E05` **e** **100% (3/3)** na Checagem Independente `C02-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** revisar a regra de zerar contadores/acumuladores antes do laço, exercitar a condição `>=` nas subtrações sucessivas e aplicar a variante `V2` do bloco.
- **Após 2 tentativas malsucedidas:** retornar para **`C01`** (anatomia do `while`) e **`B04`** (desvio condicional composto).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 7 — Padrões de repetição, contadores e acumuladores).
- `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 2 (18/09 — Exercícios de contagem e acumulação com `while`).
- `[DOC]` `Aula_09_Algoritmos.pdf` p. 11–15, 19–20 (Contadores, acumuladores, cálculo de quociente e resto por subtrações sucessivas).
- `[DOC]` `Lista4_Algoritmos.pdf` p. 1–2 (Ex. 2 e 3 — somatórios e filtragens condicionais).
- Casos de teste e soluções verificáveis: [C02_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/gabaritos/C02_gabarito.md) e [C02_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/C02_testes.md).
