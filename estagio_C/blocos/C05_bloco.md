# Bloco `C05` — Laço Contado (`for`): Sintaxe, Padrões de Contagem, C99 e Erros *Off-by-One*

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio C — Estruturas de Repetição e Rastreamento de Laços / **`C05`** |
| **Micro-habilidade foco** | Escrever e converter laços contados com `for (init; cond; atualiz)` dominando os 4 padrões de contagem, passo variável, declaração `for (int i = 0; ...)` (C99) e prevenção de erros *off-by-one*. |
| **Pré-requisitos** | `C02` *(Contadores e Acumuladores com `while`)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão 1 (`E01`–`E05`, 22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Não utilize** `break` ou `continue` em laços, vetores (`char[]`, `int[]`, `v[i]`) ou funções customizadas além de `int main(void)`. Utilize o padrão **C99** (`gcc -std=c99 -Wall -Wextra`) e saídas `printf` estritamente em ASCII puro (sem acentos). |

### Registro das Sessões (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Sintaxe e Ordem Exata de Execução do `for`:**
   ```c
   for (expr1; expr2; expr3) {
       corpo;
   }
   ```
   - `expr1` (**Inicialização**): executada **uma única vez** no início do laço.
   - `expr2` (**Condição**): avaliada **antes** de cada iteração; se falsa (`0`), encerra o laço.
   - `corpo`: executado quando `expr2` é verdadeira.
   - `expr3` (**Atualização**): executada ao **final** de cada iteração, antes de retornar para `expr2`.
2. **Equivalência `for` $\leftrightarrow$ `while`:**
   Todo laço `for (init; cond; atualiz) { corpo; }` sem `continue` equivale a:
   ```c
   init;
   while (cond) {
       corpo;
       atualiz;
   }
   ```
3. **Os 4 Padrões Clássicos de Contagem (`n` iterações):**
   - `0 .. n-1`: `for (int i = 0; i < n; i++)` (padrão base-0, `n` iterações: `0, 1, ..., n-1`).
   - `1 .. n`: `for (int i = 1; i <= n; i++)` (padrão base-1, `n` iterações: `1, 2, ..., n`).
   - `n-1 .. 0`: `for (int i = n - 1; i >= 0; i--)` (regressivo base-0, `n` iterações).
   - `n .. 1`: `for (int i = n; i >= 1; i--)` (regressivo base-1, `n` iterações).
4. **Erros *Off-by-One* (Erro por 1 Iteração):**
   - Confundir `<` com `<=` altera a contagem em 1 iteração. Por exemplo, `for (int i = 0; i <= n; i++)` executa **`n + 1` vezes** (e não `n`).
   - Sempre confira os dois extremos: qual é o **1º valor** e qual é o **último valor** válido.
5. **Passo Variável e Operador Vírgula:**
   - O passo não precisa ser `1`: use `i += 2`, `i -= 5`, `i *= 2`.
   - Use desigualdades direcionadas (`<`, `<=`, `>`, `>=`) em vez de `!=`, para não pular o limite quando o passo for maior que 1.
   - É possível inicializar e atualizar duas variáveis no cabeçalho separadas por vírgula: `for (int i = 0, j = 10; i < j; i++, j--)`.
6. **Declaração no Cabeçalho em C99 e Escopo Local:**
   - Em **C99** (`-std=c99`), `for (int i = 0; i < n; i++)` declara `i` com **escopo restrito ao laço**: após o fechamento `}`, a variável `i` **deixa de existir**.
   - Se o programa precisar consultar o valor final de `i` depois do laço, declare `int i;` **antes** do `for`.
7. **Quando escolher `for` vs. `while`:** Use `for` quando a contagem, os limites ou o passo forem conhecidos/regulares; use `while` quando a parada depender de sentinela ou evento imprevisível.

---

## 2. Exemplos Guiados

### Exemplo 1 — Conversão `while` $\leftrightarrow$ `for` e Escopo C99 *(Trecho ilustrativo)*
Somar os quadrados de `1` a `4`:

**Forma com `while`:**
```c
int soma = 0;
int i = 1;
while (i <= 4) {
    soma += i * i;
    i++;
}
/* Aqui i ainda existe e vale 5 */
```

**Forma equivalente em `for` (C99):**
```c
int soma = 0;
for (int i = 1; i <= 4; i++) {
    soma += i * i;
}
/* Aqui i NAO existe mais (escopo restrito ao for em C99) */
```
- **Rastreamento:** `i = 1` ($\text{soma}=1$) $\rightarrow$ `i = 2` ($\text{soma}=5$) $\rightarrow$ `i = 3` ($\text{soma}=14$) $\rightarrow$ `i = 4` ($\text{soma}=30$) $\rightarrow$ `i = 5` (sai).
- Total: **4 iterações**, `soma = 30`.

---

### Exemplo 2 — Passo variável e contagem regressiva *(Programa completo)*
O programa lê um inteiro `n` e imprime todos os múltiplos pares de `0` até `n` (passo `+2`) e depois conta regressivamente de `n` até `1` (padrão `n .. 1`):

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    printf("Pares:");
    for (int i = 0; i <= n; i += 2) {
        printf(" %d", i);
    }
    printf("\n");

    printf("Regressiva:");
    for (int i = n; i >= 1; i--) {
        printf(" %d", i);
    }
    printf("\n");

    return 0;
}
```
- Para `n = 5`:
  - `Pares: 0 2 4` (quando `i` vai de `4` para `6`, `6 <= 5` é falso e encerra com segurança).
  - `Regressiva: 5 4 3 2 1`.

---

## 3. Exercícios (`C05-E01` a `C05-E05`)

### `C05-E01` *(Teste de Mesa / Padrões de Contagem, Passo Variável e Escopo C99)*
Sem usar o computador, analise cada trecho abaixo e responda:

**Trecho A:**
```c
for (int i = 0; i < 4; i++) {
    printf("%d ", i);
}
```
**Trecho B:**
```c
for (int i = 4; i >= 0; i--) {
    printf("%d ", i);
}
```
**Trecho C:**
```c
int i;
for (i = 2; i <= 14; i += 3) {
    printf("%d ", i);
}
printf("| Final=%d\n", i);
```
**Trecho D:**
```c
for (int k = 0; k < 3; k++) {
    printf("%d ", k);
}
printf("Fim=%d\n", k);
```
1. Indique a saída exata e a quantidade de iterações dos trechos **A**, **B** e **C**.
2. Explique por que o **Trecho D** gera erro de compilação em C99 e como corrigi-lo caso se deseje imprimir `Fim=3`.

---

### `C05-E02` *(Caça ao Bug — Off-by-One e Início em `0`)*
Um estudante queria imprimir um por linha os `n` primeiros múltiplos **positivos** de `3` (para `n = 4`, esperava `3`, `6`, `9`, `12`), mas escreveu:

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    for (int i = 0; i <= n; i++) {   /* Bugs de contagem aqui */
        printf("%d\n", i * 3);
    }

    return 0;
}
```
1. Para a entrada `n = 4`, quantas linhas o programa imprime e qual é a saída gerada?
2. Identifique os dois erros no cabeçalho do `for` (*ponto inicial* e *erro off-by-one*).
3. Escreva a versão corrigida completa em C99 ([C05_E02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C05_E02_corrigido.c)).

---

### `C05-E03` *(Completar Solução — Conversão `while` $\rightarrow$ `for` para Fatorial)*
Observe o cálculo de $n!$ ($n \ge 0$) escrito com `while`:
```c
int i = 1;
while (i <= n) {
    fat *= i;
    i++;
}
```
Complete a versão equivalente em C99 usando `for` no código abaixo (`/* A */`, `/* B */`, `/* C */`, `/* D */`), sabendo que para `n = 0` o resultado deve ser `0! = 1`:

```c
#include <stdio.h>

int main(void) {
    int n;
    long long fat = 1;

    scanf("%d", &n);

    for (/* A: init */; /* B: condicao */; /* C: atualizacao */) {
        /* D: acumulacao multiplicativa */;
    }

    printf("%d! = %lld\n", n, fat);
    return 0;
}
```

---

### `C05-E04` *(Completar Solução — Contagem Regressiva com Passo Variável)*
Complete o programa em C99 ([C05_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C05_E04.c)) que lê `inicio` e `passo` (`passo > 0`), imprime um por linha todos os valores a partir de `inicio` que sejam maiores ou iguais a `1`, diminuindo de `passo` em `passo`, e ao final imprime `Contagem: %d\n` com a quantidade de números exibidos:

```c
#include <stdio.h>

int main(void) {
    int inicio, passo;
    int qtd = 0;

    scanf("%d %d", &inicio, &passo);

    for (/* Lacuna 1 */; /* Lacuna 2 */; /* Lacuna 3 */) {
        printf("%d\n", i);
        qtd++;
    }

    printf("Contagem: %d\n", qtd);
    return 0;
}
```

---

### `C05-E05` *(Programa Completo Independente — Filtro Múltiplo de 3 e Não-Múltiplo de 5)*
Escreva um programa completo em C99 ([C05_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C05_E05.c)) que leia um inteiro `n` e percorra os números de `1` até `n` (inclusive) com um laço `for`.  
Para cada número do intervalo que seja múltiplo de `3` **e não** seja múltiplo de `5`, imprima-o em uma linha (`%d\n`).  
Ao final, imprima a quantidade de números exibidos e a soma deles no formato exato:
```text
Quantidade: %d\n
Soma: %d\n
```

*Exemplo de entrada:* `15`  
*Saída esperada:*
```text
3
6
9
12
Quantidade: 4
Soma: 30
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `C05-C01` *(Teste de Mesa / Passo != 1 e Erro Off-by-One)*
Sem usar o computador, analise os dois trechos em C99:

**Trecho 1:**
```c
int s = 0;
for (int k = 10; k > 0; k -= 3) {
    s += k;
}
printf("s=%d\n", s);
```

**Trecho 2:**
```c
/* Objetivo pretendido: imprimir os 5 primeiros indices a partir de 0 (0 1 2 3 4) */
for (int j = 0; j <= 5; j++) {
    printf("%d ", j);
}
```
1. No **Trecho 1**, liste os valores assumidos por `k` em cada iteração, o total de iterações e a saída exata de `s=%d`.
2. No **Trecho 2**, quantos números são impressos, qual o erro cometido (*off-by-one*) e qual deve ser a condição correta para imprimir exatamente 5 números a partir de `0`?

---

### `C05-C02` *(Conversão `while` $\leftrightarrow$ `for` Respeitando Escopo C99)*
Dado o programa abaixo escrito com `while`:
```c
#include <stdio.h>

int main(void) {
    int a, b;
    int soma = 0;
    int i;

    scanf("%d %d", &a, &b);

    i = a;
    while (i <= b) {
        if (i % 2 == 0) {
            soma += i;
        }
        i++;
    }

    printf("Soma pares: %d\n", soma);
    printf("Proximo i: %d\n", i);
    return 0;
}
```
1. Se um estudante substituir `i = a; while (i <= b) { ... }` por `for (int i = a; i <= b; i++)` (mantendo o `printf("Proximo i: %d\n", i);` após o laço e mantendo `int i;` fora ou removendo `int i;`), o que acontece na compilação ou no valor impresso em cada caso?
2. Escreva a conversão correta completa em C99 ([C05_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C05_C02_corrigido.c)) preservando exatamente a mesma saída do `while`.

---

### `C05-C03` *(Programa Completo Independente — Estatísticas com `for` e Filtros Lógicos)*
Escreva um programa completo em C99 ([C05_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C05_C03.c)) que leia um inteiro `n`.  
Se `n <= 0`, imprima exatamente `Entrada invalida\n`.  
Caso contrário, percorra todos os inteiros de `1` até `n` (inclusive) com `for (int i = 1; i <= n; i++)` e calcule:
1. A quantidade de números que são pares **ou** múltiplos de `7` (sem contar duas vezes um número que atenda a ambas as condições).
2. A soma apenas dos números ímpares estritamente maiores que `5`.
3. A média aritmética real (`double`) de todos os inteiros de `1` a `n`.

Formato exato de saída:
```text
Qtd par ou mult7: %d\n
Soma impares > 5: %d\n
Media total: %.2f\n
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `C06` (`Rastreamento Rigoroso de for, Efeitos Colaterais e Comando Nulo ;`):** somente após autocorreção dos exercícios `C05-E01..E05` **e** **100% (3/3)** na Checagem Independente `C05-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** revisar os 4 padrões de contagem (`< n` vs `<= n`), a ordem de execução `init → cond → corpo → atualiz` e a diferença de escopo entre `for (int i = ...)` e `int i;` antes do laço, aplicando a variante `V2` do bloco.
- **Após 2 tentativas malsucedidas:** retornar para **`C02`** (contadores e acumuladores em `while`) e **`A02`** (compilação em C99 com `gcc -std=c99`).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 7 — estruturas de repetição com variável de controle).
- `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 2 (21/09 — laço contado `for`).
- `[DOC]` `Aula_10_Algoritmos.pdf` p. 3–18 (anatomia do `for`, equivalência `while`, 4 padrões, passo variável, *off-by-one*, C99 e `gcc -std=c99`).
- `[DOC]` `Lista5_Algoritmos.pdf` p. 1 (Ex. 2 — filtro múltiplos de 3 e não de 5).
- Casos de teste e soluções verificáveis: [C05_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/gabaritos/C05_gabarito.md) e [C05_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/C05_testes.md).
