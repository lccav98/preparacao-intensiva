# Bloco `F02` — Protótipos de Funções, Escopo Local e Tempo de Vida

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio F — Modularização, Funções, Ponteiros e Compilação Multi-Arquivo / **`F02`** |
| **Micro-habilidade foco** | Separar declaração (protótipo) de definição permitindo funções após `main`, e distinguir **escopo** (visibilidade) de **tempo de vida** de variáveis locais e parâmetros. |
| **Pré-requisitos** | `F01` *(Introdução a funções: `void`, `return`, parâmetros e argumentos antes de `main`)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão única de prática + checagem (20 min):** `12 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Não utilize** ponteiros (`int *`, `F04`–`F05`), passagem de `&var` como argumento de função (use `&` apenas em `scanf`), vetores/matrizes/strings como parâmetros (`F06`–`F07`), múltiplos arquivos `.h`/`.c` (`F08`), recursividade (`G01`), `struct`, `malloc`/`free` ou VLAs. Declare **protótipos antes de `main`** e escreva as definições **após `main`**, usando apenas variáveis locais, parâmetros escalares (`int`, `double`) e saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Protótipo vs. Definição:**
   - **Protótipo (declaração):** vai **antes de `main`**, termina com `;` e anuncia a assinatura (`int somar(int a, int b);`).
   - **Definição (implementação):** contém o corpo `{ ... }` e pode ficar **após `main`**, mantendo `main` no topo do arquivo e permitindo que qualquer função chame outra independentemente da ordem em que foram definidas.
2. **Compatibilidade estrita e cabeçalhos padrão:** O protótipo e a definição devem concordar exatamente no tipo de retorno, número e tipos dos parâmetros. Os arquivos padrão como `<stdio.h>` funcionam exatamente assim: trazem os **protótipos** de `printf` e `scanf`.
3. **Variáveis locais homônimas são independentes:** Variáveis com o mesmo nome declaradas em funções distintas (inclusive parâmetros) ocupam regiões separadas na memória. Alterar `x` dentro de `func` **não** altera a variável `x` de `main`.
4. **Escopo (onde o nome é visível):** Uma variável local ou parâmetro só existe dentro da função (ou bloco `{ ... }`, como `for (int i = 0; ...)`) onde foi declarada. Tentar acessar uma variável local de outra função gera erro de compilação.
5. **Tempo de vida (quando a memória existe):** Variáveis locais comuns e parâmetros são criados quando a função inicia e **destruídos** no retorno (`return` ou `}`). A cada nova chamada, são criados novamente do zero (não guardam valores de chamadas anteriores).

---

## 2. Exemplos Guiados

### Exemplo 1 — Protótipo × Definição *(Trecho ilustrativo)*

| Aspecto | Protótipo (Declaração) | Definição (Implementação) |
|---|---|---|
| **Posição no arquivo** | Antes de `main` | Geralmente após `main` |
| **Terminação** | Ponto e vírgula `;` | Bloco `{ ... }` com código |
| **O que informa** | Retorno, nome e tipos dos parâmetros | Corpo completo da função |

```c
int dobro(int x);          /* Prototipo: anuncia a funcao antes de main */
/* Sem este prototipo, chamar dobro(5) dentro de main com definicao abaixo gera erro/aviso C99 */
```

### Exemplo 2 — Protótipos no topo e variáveis homônimas independentes *(Programa completo)*
```c
#include <stdio.h>

int ajustar(int x);
void mostrar(int n);

int main(void) {
    int x = 10;
    int n = ajustar(x);
    mostrar(x);        /* x de main continua 10 */
    mostrar(n);        /* n de main recebeu o retorno 25 */
    return 0;
}

int ajustar(int x) {   /* este 'x' e uma copia local de ajustar */
    int n = 5;         /* este 'n' e local de ajustar, distinto do 'n' de main */
    x = x * 2 + n;     /* x local = 25 */
    return x;          /* ao retornar, 'x' e 'n' de ajustar sao destruidos */
}

void mostrar(int n) {  /* parametro 'n' independente do 'n' de main */
    printf("Valor: %d\n", n);
}
```
Saída produzida: `Valor: 10` e `Valor: 25`.

---

## 3. Exercícios (`F02-E01` a `F02-E05`)

### `F02-E01` *(Teste de Mesa — Variáveis homônimas, escopo e tempo de vida)*
Sem usar computador, acompanhe o programa completo abaixo:

```c
#include <stdio.h>

int acumular_local(int x);

int main(void) {
    int x = 4, acc = 100;
    printf("1: %d\n", acumular_local(x));
    printf("2: %d\n", acumular_local(x));
    printf("main: x=%d acc=%d\n", x, acc);
    return 0;
}

int acumular_local(int x) {
    int acc = 0;
    for (int i = 1; i <= x; i++) {
        acc += i;
    }
    x = 99;
    return acc;
}
```
**(a)** Escreva as 3 linhas exatas impressas no terminal.  
**(b)** Explique por que a 2ª chamada `acumular_local(x)` imprime `10` (e não `20`), e por que `x = 99;` e `acc` dentro de `acumular_local` não alteram `x` nem `acc` de `main`.

---

### `F02-E02` *(Completar solução)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` para que o programa tenha os protótipos corretos antes de `main` e as definições após `main`:

```c
#include <stdio.h>
#define PI 3.14159

/* A */
/* B */

int main(void) {
    double raio;
    scanf("%lf", &raio);
    double area = area_circulo(raio);
    exibir_resumo(raio, area);
    return 0;
}

double area_circulo(double r) {
    /* C */
}

void exibir_resumo(/* D */) {
    printf("Raio: %.2f | Area: %.2f\n", r, area);
}
```

---

### `F02-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria manter `main` no topo, ler dois inteiros `u` e `v` e imprimir `Soma dos quadrados: S`, mas possui **3 erros de protótipo/escopo**. Identifique os erros (no papel ou em comentários `//`) e escreva a versão corrigida completa:

```c
#include <stdio.h>

double quadrado(int x);

int main(void) {
    int u, v, total;
    scanf("%d %d", &u, &v);
    total = soma_quadrados(u, v);
    printf("Soma dos quadrados: %d\n", resultado);
    return 0;
}

int quadrado(int x) {
    return x * x;
}

int soma_quadrados(int a, int b) {
    int resultado = quadrado(a) + quadrado(b);
    return resultado;
}
```

---

### `F02-E04` *(Variação controlada com pistas)*
Escreva um **programa completo** em C com **protótipos antes de `main`** e **definições após `main`** para as funções:
- `int eh_bissexto(int ano);` — retorna `1` se `ano` for bissexto (`ano % 400 == 0` ou `ano % 4 == 0 && ano % 100 != 0`), ou `0` caso contrário.
- `int dias_no_mes(int mes, int ano);` — retorna a quantidade de dias de `mes` (`1..12`), chamando `eh_bissexto(ano)` no caso `mes == 2`, ou `-1` se `mes` estiver fora de `1..12`.

No `main`, leia `mes` e `ano`, chame `dias_no_mes(mes, ano)` e imprima `Dias: D` (ou `Mes invalido` caso retorne `-1`).  
*Pista:* declare ambos os protótipos antes de `main` para que `dias_no_mes` possa chamar `eh_bissexto` sem depender da ordem das definições após `main`.

---

### `F02-E05` *(Resolução independente)*
Escreva um **programa completo** em C com **protótipos antes de `main`** e **definições após `main`** para:
- `int soma_divisores_proprios(int n);` — retorna a soma dos divisores positivos de `n` estritamente menores que `n` (use variável local `int soma = 0;`).
- `int eh_perfeito(int n);` — retorna `1` se `n > 1` e `soma_divisores_proprios(n) == n`, ou `0` caso contrário.

No `main`, leia dois inteiros `a` e `b` (`a <= b`), use uma variável local `int soma = 0;` em `main` para contar quantos números perfeitos existem no intervalo `[a, b]` e imprima exatamente:
```text
Perfeitos: K
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `F02-C01` *(Teste de Mesa)*
Sem usar computador, execute o rastreamento do programa abaixo e responda:

```c
#include <stdio.h>

int atualizar(int a);

int main(void) {
    int a = 3, cont = 10;
    cont = atualizar(a);
    printf("A=%d C=%d\n", a, cont);
    printf("B=%d\n", atualizar(cont));
    return 0;
}

int atualizar(int a) {
    int cont = 2;
    a = a + cont;
    return a * 2;
}
```
**(a)** Qual é a saída exata impressa no terminal?  
**(b)** Explique a diferença entre **escopo** e **tempo de vida** da variável `cont` declarada dentro de `atualizar`.

### `F02-C02` *(Caça ao Bug — Programa completo)*
O programa abaixo lê dois inteiros positivos `x` e `y` e deveria exibir o `MDC` e o `MMC` utilizando `mdc` e `mmc` definidas após `main`. Identifique e corrija **todos os erros de protótipo e escopo**:

```c
#include <stdio.h>

double mmc(int a, int b);

int main(void) {
    int x, y;
    scanf("%d %d", &x, &y);
    printf("MDC: %d\n", mdc(x, y));
    printf("MMC: %d\n", mmc(x, y));
    printf("Divisor: %d\n", d);
    return 0;
}

int mdc(int a, int b) {
    while (b != 0) {
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int mmc(int a, int b) {
    int d = mdc(a, b);
    return (a / d) * b;
}
```
*(Nota: o programa corrigido deve imprimir apenas `MDC: ...` e `MMC: ...`, removendo o acesso inválido à variável local `d` de `mmc`.)*

### `F02-C03` *(Programa completo independente)*
Escreva um programa completo em C declarando **2 protótipos antes de `main`** e suas **definições após `main`**:
- `int eh_primo(int n);` — retorna `1` se `n` for primo (`n >= 2` sem divisores entre `2` e `sqrt(n)`, testado via `d * d <= n`), ou `0` caso contrário.
- `int contar_primos(int ini, int fim);` — conta quantos primos existem no intervalo fechado `[ini, fim]` chamando `eh_primo`.

No `main`, leia `ini` e `fim` e imprima exatamente:
```text
Primos: K
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `F03` (`Passagem por Valor em C e Limites da Cópia Local`):** somente após autocorreção de `F02-E01..E05` e **100% (3/3)** em `F02-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** revisar a sintaxe de protótipos antes de `main` (com `;` e assinatura idêntica à definição) e desenhar caixas separadas para variáveis locais homônimas indicando criação e destruição em cada chamada; aplicar variante `V2` de `F02`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`F01`** (assinatura e `return` de funções) e **`C05`** (escopo de bloco em `for`).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 9 — escopo de variáveis, desvio de chamada).
- `[DOC]` `Aula_17_Algoritmos.pdf` p. 3–11.
- Casos de teste e soluções verificáveis: [F02_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/gabaritos/F02_gabarito.md) e [F02_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/F02_testes.md).
