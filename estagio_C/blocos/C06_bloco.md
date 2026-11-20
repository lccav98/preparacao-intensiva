# Bloco `C06` — Rastreamento Rigoroso de `for`, Efeitos Colaterais e Comando Nulo (`;`)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio C — Estruturas de Repetição e Rastreamento de Laços / **`C06`** |
| **Micro-habilidade foco** | Executar teste de mesa detalhado de laços `for` com modificações da variável de controle dentro do corpo (`i++`, divisão inteira), omissão de expressões e comando nulo (`;`). |
| **Pré-requisitos** | `C05` *(Laço Contado `for`: Sintaxe, Padrões de Contagem e Erros Off-by-One)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão 1 (`E01`–`E05`, 20 min):** `12 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Não utilize** vetores ou strings (`char[]`, `int[]` ou qualquer array `v[i]`), funções customizadas além de `int main(void)`, `struct` ou alocação dinâmica. Saídas de programas C devem ser estritamente em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **A Anatomia em 4 Fases do `for`:**
   ```c
   for (expr1; expr2; expr3) {
       corpo;
   }
   ```
   A ordem de execução é estrita:
   - **Fase 1 (Inicialização):** `expr1` é avaliada exatamente uma vez.
   - **Fase 2 (Teste):** `expr2` é avaliada. Se for falsa (`0`), o laço encerra imediatamente.
   - **Fase 3 (Corpo):** O bloco de instruções `{ ... }` é executado.
   - **Fase 4 (Atualização):** `expr3` é avaliada. Em seguida, retorna para a **Fase 2**.

2. **Efeitos Colaterais no Corpo do Laço:**
   - Modificar a variável de controle dentro do corpo (por exemplo, `i++` ou `i /= 2`) altera o valor antes que a expressão de atualização `expr3` seja executada.
   - Se `expr3` também alterar a mesma variável, ocorrem duas alterações na mesma iteração, o que pode acelerar a terminação ou aprisionar o programa em um ciclo infinito.

3. **A Armadilha Mortal do Ponto e Vírgula (`;` — Comando Nulo):**
   ```c
   for (int i = 0; i < 5; i++); // <-- PONTO E VIRGULA FATAL
   {
       printf("%d\n", i);
   }
   ```
   - O `;` imediatamente após o parêntese do `for` ou `while` é interpretado pelo compilador como um **comando nulo** (uma instrução vazia).
   - O laço executa repetidamente essa instrução vazia até que a condição se torne falsa.
   - O bloco `{ ... }` que vem logo abaixo **não pertence ao laço**; ele vira um bloco isolado que é executado **apenas uma vez**, recebendo o valor que a variável de controle possui após o término do laço!

4. **Comando Nulo no `while`:**
   ```c
   int i = 0;
   while (i < 5); // <-- LACO INFINITO IMEDIATO
   {
       i++;
   }
   ```
   Como o corpo do `while` é apenas o comando nulo `;`, a variável `i` nunca é incrementada. A condição `0 < 5` permanece verdadeira para sempre e o programa congela sem gerar qualquer saída.

5. **Critério de Parada com `<` ou `<=` versus `!=`:**
   - Em laços com passo diferente de 1 (ex.: `i += 2` ou `i /= 2`), **nunca** use desigualdade exata `i != n`. Se `i` "pular" o valor de `n`, a condição nunca se tornará falsa, resultando em laço infinito.
   - Use sempre desigualdades direcionadas (`<`, `<=`, `>`, `>=`).

6. **Detecção Analítica de Não-Terminação:**
   - Um laço infinito ocorre quando o conjunto de transformações sobre a variável de controle a leva a um ciclo fechado de valores ou afasta o valor da condição de terminação.
   - No caso clássico da UTFPR: `for (i = 10; i >= 1; i /= 2) printf("%d ", i++);` — quando `i` atinge `1`, o corpo faz `i++` (resultando em `2`), e a atualização faz `i /= 2` (resultando em `2 / 2 = 1`). A variável fica alternando eternamente entre `1` e `2`.

---

## 2. Exemplos Guiados

### Exemplo 1 — Rastreamento com Efeito Colateral no Corpo e na Atualização

Observe o trecho de código abaixo:
```c
int i;
for (i = 1; i <= 8; i += 2) {
    printf("%d ", i);
    i++;
}
printf("| Final: %d\n", i);
```

**Tabela de Rastreamento (Teste de Mesa):**

| Iteração | Entrada no Teste (`i`) | `i <= 8`? | `printf("%d ", i)` | Efeito no corpo (`i++`) | Atualização (`i += 2`) |
|---|---|---|---|---|---|
| **1** | `1` | `1 <= 8` (V) | Imprime `1 ` | `i` vira `2` | `i` vira `4` |
| **2** | `4` | `4 <= 8` (V) | Imprime `4 ` | `i` vira `5` | `i` vira `7` |
| **3** | `7` | `7 <= 8` (V) | Imprime `7 ` | `i` vira `8` | `i` vira `10` |
| **Fim** | `10` | `10 <= 8` (F) | *(sai do laço)* | — | — |

**Saída Exata na Tela:**
```text
1 4 7 | Final: 10
```
*Note que o laço executou apenas 3 iterações, pois em cada volta `i` avançou 3 unidades (1 no corpo e 2 no cabeçalho).*

---

### Exemplo 2 — Diagnóstico do Comando Nulo (`;`)

```c
#include <stdio.h>

int main(void) {
    int contador = 0;
    int soma = 0;

    for (contador = 1; contador <= 4; contador++);
    {
        soma += contador;
    }

    printf("Soma: %d, Contador: %d\n", soma, contador);
    return 0;
}
```

**Diagnóstico:**
1. O `;` na linha do `for` faz com que o laço apenas incremente `contador` de 1 até 5.
2. Quando `contador` chega a 5, `5 <= 4` é falso e o laço encerra.
3. O bloco `{ soma += contador; }` é executado **uma única vez** com `contador = 5`.
4. Saída impressa: `Soma: 5, Contador: 5`. Se o ponto e vírgula não existisse, a soma seria `1 + 2 + 3 + 4 = 10` e a saída seria `Soma: 10, Contador: 5`.

---

## 3. Exercícios (`C06-E01` a `C06-E05`)

### Sessão 1 (`C06-E01` a `C06-E05` — Rastreamento, Diagnóstico e Redução)

### `C06-E01` *(Rastreamento de `for` com `i++` no Corpo e na Atualização)*
Sem utilizar o computador, construa a tabela de teste de mesa completa para o seguinte trecho de código em C:

```c
int i;
for (i = 0; i < 10; i += 2) {
    printf("%d ", i);
    i++;
}
printf("\nFinal: %d\n", i);
```

Preencha a tabela contendo:
1. Número da iteração.
2. Valor de `i` no teste de condição (`i < 10`).
3. Valor impresso.
4. Valor de `i` após a instrução `i++` do corpo.
5. Valor de `i` após a atualização `i += 2`.
6. Saída textual exata produzida pelo programa e o valor final de `i`.

---

### `C06-E02` *(Diagnóstico do Bug do Ponto e Vírgula `;` após `for`)*
Um estudante de Engenharia da UTFPR escreveu o seguinte programa para calcular o fatorial de 5 ($5! = 120$):

```c
#include <stdio.h>

int main(void) {
    int fat = 1;
    int i;

    for (i = 1; i <= 5; i++);
    {
        fat *= i;
    }

    printf("Fatorial = %d\n", fat);
    return 0;
}
```

Ao executar, o programa imprime `Fatorial = 6` em vez de `120`.
1. Explique detalhadamente por que o compilador GCC não acusou nenhum erro sintático e por que o resultado foi 6.
2. Apresente a linha corrigida.

---

### `C06-E03` *(Rastreamento do Caso UTFPR Lista 5 Ex. 1 — Divisão Inteira e Laço Infinito)*
Analise o seguinte trecho de código clássico extraído da `Lista5_Algoritmos.pdf` da UTFPR:

```c
int i;
for (i = 10; i >= 1; i /= 2) {
    printf("%d ", i++);
}
```

1. Monte o teste de mesa passo a passo para as primeiras 6 iterações, registrando o valor de `i` no teste, o valor impresso por `i++`, o valor de `i` após o pós-incremento e o valor após a atualização `i /= 2`.
2. Explique por que uma apostila preliminar (`Lista do Professor.pdf`) errou ao afirmar que o programa terminava com `i = 0` porque "2 / 2 = 0".
3. Demonstre analiticamente por que o laço é estritamente infinito e qual sequência de números é impressa repetidamente.

---

### `C06-E04` *(Caça ao Bug — Laço Infinito por Desigualdade Exata `!=`)*
O programa abaixo deveria ler um número inteiro positivo `n` e calcular a soma dos números ímpares positivos menores ou iguais a `n` ($1 + 3 + 5 + \dots$):

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    int soma = 0;
    for (int i = 1; i != n; i += 2) {
        soma += i;
    }

    printf("Soma = %d\n", soma);
    return 0;
}
```

1. Teste o programa mentalmente para `n = 5`. O programa funciona? Qual é a saída?
2. Teste o programa mentalmente para `n = 6`. O que acontece com a execução e por quê?
3. Escreva o programa corrigido completo em C99 ([C06_E04_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C06_E04_corrigido.c)), substituindo o critério frágil por uma condição que funcione tanto para `n` par quanto para `n` ímpar.

---

### `C06-E05` *(Programa Completo — Sequência de Collatz / $3n+1$ Limitada)*
A famosa conjectura de Collatz gera uma sequência a partir de um número inteiro positivo $n$:
- Se $n$ for par: o próximo número é $n / 2$.
- Se $n$ for ímpar: o próximo número é $3n + 1$.
- O processo repete até que $n$ se torne igual a $1$.

Escreva um programa completo em C99 ([C06_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C06_E05.c)) que:
1. Leia um número inteiro positivo `n` (`scanf("%d", &n);`). Se `n <= 0`, o programa deve imprimir `Entrada Invalida\n` e encerrar.
2. Imprima na primeira linha cada termo da sequência separado por um espaço, iniciando pelo próprio `n` e finalizando em `1`.
3. Na segunda linha, imprima a quantidade total de passos necessários para atingir o valor 1 no formato: `Passos: %d\n` (se $n = 1$, são 0 passos).
4. *Restrição de segurança:* O laço deve parar se atingir 1 ou se atingir o limite de 200 passos (prevenção contra laço infinito). Proibido usar vetores ou funções externas.

*Exemplo de entrada:* `6`  
*Saída esperada:*
```text
6 3 10 5 16 8 4 2 1
Passos: 8
```

---

## 4. Checagem Independente de Domínio (`C06-C01` a `C06-C03`)

> **Instruções:** Resolva estas 3 questões sem consulta a materiais ou gabaritos. Tempo limite: 18 minutos.

### `C06-C01` *(Teste de Mesa sem Computador — Comando Nulo em `while`)*
Analise o seguinte trecho de código:

```c
int c = 0, k = 1;
while (k < 5);
    c += k++;
printf("%d %d\n", c, k);
```

1. O que acontece quando esse programa é executado no computador? A linha com `printf` chega a ser executada? Justifique com base no conceito de comando nulo.
2. Como o código deveria ser reescrito para que `c` acumule a soma de $1 + 2 + 3 + 4$ e imprima o resultado correto?

---

### `C06-C02` *(Rastreamento de Efeito Colateral Finito no Corpo)*
Sem usar computador, elabore a tabela de teste de mesa completa para o código abaixo:

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

Indique cada iteração, o valor inicial de `i`, se a condição do `if` é satisfeita, o valor de `i` somado a `total`, a atualização do `for` e o valor final impresso em `Total = %d\n`.

---

### `C06-C03` *(Programa Completo — Redução Numérica e Soma de Dígitos Controlada)*
Escreva um programa completo em C99 ([C06_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C06_C03.c)) que leia um número inteiro positivo `n` e decomponha o número calculando a soma de seus dígitos e a contagem de dígitos através de divisões inteiras sucessivas por 10.

- Se o número lido for menor ou igual a zero (`n <= 0`), imprima: `Valor Invalido\n`.
- Caso contrário, processe os dígitos usando um laço e imprima:
  ```text
  Soma = %d
  Digitos = %d
  ```

*Exemplo de entrada:* `4096`  
*Saída esperada:*
```text
Soma = 19
Digitos = 4
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `C07` (`Controle de Fluxo em Laços: break, continue e Primalidade`):** somente após autocorreção dos exercícios `C06-E01..E05` **e** **100% de acerto (3/3)** na Checagem Independente `C06-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** revisar a ordem de 4 fases do `for` e a armadilha do ponto e vírgula `;`, refazendo manualmente o teste de mesa de `C06-E01` e `C06-C02`.
- **Após 2 tentativas malsucedidas:** retornar a **`C05`** (padrões de contagem e equivalência com `while`) e **`B02`** (efeitos de atribuição composta e operadores de incremento/decremento).

---

## 6. Referências do Orientador
- `[DOC]` `Aula_10_Algoritmos.pdf` p. 12, 16, 26–28 (semântica do `for`, comando nulo `;` e efeitos colaterais).
- `[DOC]` `Lista5_Algoritmos.pdf` p. 1 (Ex. 1: rastreamento de laço com divisão inteira e detecção de laço infinito).
- `[DOC]` `00_inventario_fontes.md` Conflito C8 (refutação do erro da `Lista do Professor.pdf` p. 2).
- Casos de teste e soluções verificáveis: [C06_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/gabaritos/C06_gabarito.md) e [C06_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/C06_testes.md).
