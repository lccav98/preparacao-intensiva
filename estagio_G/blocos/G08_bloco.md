# Bloco `G08` — Recursão Múltipla (Fibonacci / Árvore) vs. Divisão pela Metade (Potenciação Rápida)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio G — Recursividade e Pilha de Execução / **`G08`** |
| **Micro-habilidade foco** | Rastrear árvores de chamadas em recursão dupla (Fibonacci), identificando recomputações exponenciais, e contrastar com a redução logarítmica pela metade (`n / 2`) na potenciação rápida reutilizando o resultado em variável local `p`. |
| **Pré-requisitos** | `G03` *(Recursão linear sobre inteiros sem laços)* e `G01` *(Pilha de execução)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 20 min):** `12 min` resol. \| `5 min` corr. \| `3 min` recup.; **Sessão 2 (`E04`–`E06`, 20 min):** `12 min` resol. \| `5 min` corr. \| `3 min` recup.; **Checagem (`C01`–`C03`, 16 min):** `11 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **PROIBIÇÃO DE LAÇOS EM FUNÇÕES RECURSIVAS:** nenhuma função recursiva pode conter `for`, `while` ou `do-while` (laços são permitidos apenas na `main`, se necessários para E/S). **Não utilize** `struct`, alocação dinâmica (`malloc`/`free`), `gets(` ou VLAs. Saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Recursão dupla/múltipla (`fibonacci`) e dois casos base:**
   - A sequência de Fibonacci é definida por `fib(0) = 0`, `fib(1) = 1` e `fib(n) = fib(n - 1) + fib(n - 2)` para `n >= 2`.
   - Como cada chamada abre **duas** novas chamadas (`n - 1` e `n - 2`), são obrigatórios **dois casos base** (`n == 0` e `n == 1`). Esquecer `n == 1` faz `fib(1)` chamar `fib(0) + fib(-1)` e causar *stack overflow*.
2. **Árvore de chamadas e recomputação exponencial:**
   - Em recursão dupla, a execução forma uma **árvore binária** de chamadas. Os mesmos subproblemas (`fib(2)`, `fib(1)`, `fib(0)`) são recalculados repetidamente, fazendo o total de chamadas crescer exponencialmente (para `n = 40`, são mais de 330 milhões de chamadas; nesse cenário, a solução iterativa em `for`/`while` na `main` ou função iterativa é ordens de grandeza mais rápida).
3. **Divisão pela metade (`n / 2`) — Potenciação Rápida:**
   - Na potenciação linear (`G03`), $x^n = x \cdot x^{n-1}$ reduz `n` em `1` e faz cerca de $n$ chamadas.
   - Dividindo o expoente por `2` (casos base `n == 0` retorna `1.0` e `n == 1` retorna `x`):
     ```c
     double p = potencia_rapida(x, n / 2);
     if (n % 2 == 0) return p * p;
     return x * p * p;
     ```
   - O número de chamadas cai de **linear** ($n$) para **logarítmico** ($\approx \log_2 n$): para $n = 1024$, cai de `1024` chamadas para apenas **`11`**!
4. **Armadilha fatal — Duplicar a chamada `potencia_rapida(x, n / 2)`:**
   - Escrever `return potencia_rapida(x, n / 2) * potencia_rapida(x, n / 2);` (sem guardar em `double p`) faz **duas chamadas por nível**, transformando o algoritmo em uma árvore exponencial com ~$n$ chamadas e anulando todo o ganho de dividir por `2`!

---

## 2. Exemplos Guiados

### Exemplo 1 — Árvore de chamadas de `fib(4)` *(Sem código de repetição)*
```c
int fib(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fib(n - 1) + fib(n - 2);
}
```
Árvore de chamadas para `fib(4)`:
```text
                fib(4) -> 3
               /           \
         fib(3) -> 2      fib(2) -> 1
         /       \          /      \
    fib(2)->1  fib(1)->1  fib(1)->1 fib(0)->0
     /     \
fib(1)->1 fib(0)->0
```
Contagem: **9 chamadas no total** (`fib(2)` foi calculado **2 vezes**, `fib(1)` **3 vezes**, `fib(0)` **2 vezes**).

### Exemplo 2 — Rastreamento de `potencia_rapida(2.0, 7)` e `(2.0, 8)`
- `potencia_rapida(2.0, 7)`:
  1. `n = 7` (ímpar): chama `p = potencia_rapida(2.0, 3)`
  2. `n = 3` (ímpar): chama `p = potencia_rapida(2.0, 1)`
  3. `n = 1` (caso base): retorna `2.0`
  4. Volta para `n = 3`: `2.0 * 2.0 * 2.0 = 8.0`
  5. Volta para `n = 7`: `2.0 * 8.0 * 8.0 = 128.0` → **3 chamadas**!
- `potencia_rapida(2.0, 8)`: `8 -> 4 -> 2 -> 1` → **4 chamadas** (`2.0 -> 4.0 -> 16.0 -> 256.0`).

---

## 3. Exercícios (`G08-E01` a `G08-E06`)

### Sessão 1 (`G08-E01` a `G08-E03` — Árvore, Lacunas e Caça ao Bug)

### `G08-E01` *(Árvore de Chamadas sem Compilar — `fib(5)`)*
Sem usar computador, desenhe a árvore completa de chamadas de `fib(5)` usando a definição do Exemplo 1 e responda:
- **(a)** Quantas chamadas à função `fib` ocorrem no total?
- **(b)** Quantas vezes cada subproblema `fib(3)`, `fib(2)`, `fib(1)` e `fib(0)` é calculado?
- **(c)** Qual é o valor final retornado por `fib(5)`?

---

### `G08-E02` *(Completar solução e análise — `potencia_rapida`)*
Complete as lacunas `/* A */`, `/* B */` e `/* C */` na função `potencia_rapida` abaixo (sem usar laços):

```c
double potencia_rapida(double x, int n) {
    if (n == 0) return 1.0;
    if (n == 1) return x;
    double p = /* A */;
    if (n % 2 == 0) {
        return /* B */;
    }
    return /* C */;
}
```
**(d)** Trace as chamadas de `potencia_rapida(3.0, 5)` (mostrando `n`, `p` e o retorno de cada nível) e compare a quantidade de chamadas entre `pot_linear(x, n)` e `potencia_rapida(x, n)` para `n = 32` e `n = 1024` (considerando casos base `n == 0` e `n == 1`).

---

### `G08-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler `double x`, `int n` (`n >= 0`) e `int k` (`k >= 0`), calcular $x^n$ de forma rápida contando as chamadas recursivas em `chamadas` e calcular `fib(k)`. Identifique os **3 bugs intencionais**, corrija o programa completo e explique cada correção usando **comentários `//`**:

```c
#include <stdio.h>

int fib(int n);
double potencia_rapida(double x, int n, int *chamadas);

int main(void) {
    double x;
    int n, k, chamadas = 0;
    scanf("%lf %d %d", &x, &n, &k);

    double res = potencia_rapida(x, n, &chamadas);
    printf("Potencia: %.2f\n", res);
    printf("Chamadas: %d\n", chamadas);
    printf("Fib: %d\n", fib(k));
    return 0;
}

int fib(int n) {
    if (n == 0) {
        return 0;
    }
    return fib(n - 1) + fib(n - 2);
}

double potencia_rapida(double x, int n, int *chamadas) {
    (*chamadas)++;
    if (n == 0) {
        return 1.0;
    }
    if (n == 1) {
        return x;
    }
    if (n % 2 == 0) {
        return potencia_rapida(x, n / 2, chamadas) * potencia_rapida(x, n / 2, chamadas);
    }
    double p = potencia_rapida(x, n / 2, chamadas);
    return x * p;
}
```

---

### Sessão 2 (`G08-E04` a `G08-E06` — Medição de Chamadas e Potenciação Rápida)

### `G08-E04` *(Variação controlada com pistas — Contador de chamadas em Fibonacci)*
Escreva um **programa completo** em C99 (sem laços na função recursiva) contendo:
- `int fib_contado(int n, int *chamadas);` — incrementa `(*chamadas)++` logo na entrada da função e calcula o $n$-ésimo termo de Fibonacci (`fib(0) = 0`, `fib(1) = 1`).

No `main`, leia `n` (`0 <= n <= 20`) e imprima exatamente:
```text
Fib: F
Chamadas: C
```
*Pista:* repasse `chamadas` (sem `&`) nas chamadas recursivas `fib_contado(n - 1, chamadas)` e `fib_contado(n - 2, chamadas)`.

---

### `G08-E05` *(Variação controlada com pistas — Linear vs. Rápida com contador)*
Escreva um **programa completo** em C99 (sem laços nas funções recursivas) com duas funções usando casos base `n == 0` (`1.0`) e `n == 1` (`x`):
- `double pot_linear(double x, int n, int *chamadas);` *(passo `n - 1`)*
- `double pot_rapida(double x, int n, int *chamadas);` *(passo `n / 2` com variável local `p`)*

Ambas incrementam `(*chamadas)++` na entrada. No `main`, leia `double x` e `int n` (`n >= 0`) e imprima exatamente:
```text
Resultado: R.RR
Chamadas linear: CL
Chamadas rapida: CR
```

---

### `G08-E06` *(Resolução independente — Potenciação rápida para expoentes negativos e positivos)*
Implemente um **programa completo** em C99 (sem laços na função recursiva) com:
- `double potencia_rapida(double x, int n, int *mult);`
  - Para `n < 0` (`x != 0`): retorna `1.0 / potencia_rapida(x, -n, mult)`.
  - Para `n == 0`: retorna `1.0` (`0` multiplicações).
  - Para `n == 1`: retorna `x` (`0` multiplicações).
  - Para `n > 1`: armazena `double p = potencia_rapida(x, n / 2, mult);`; se `n` for par, soma `1` em `*mult` e retorna `p * p`; se `n` for ímpar, soma `2` em `*mult` e retorna `x * p * p`.

No `main`, leia `double x` e `int n` (`-10 <= n <= 20`) e imprima exatamente:
```text
Potencia: P.PP
Multiplicacoes: M
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `G08-C01` *(Árvore de chamadas e recomputação)*
Considere a função recursiva abaixo (sem laços):
```c
int g(int n) {
    if (n == 0 || n == 1) return 1;
    return g(n - 1) + g(n - 2) + 1;
}
```
**(a)** Desenhe a árvore completa de chamadas para `g(4)`.  
**(b)** Informe o valor retornado por `g(4)`, o total de chamadas à função `g` e quantas vezes `g(2)` e `g(1)` foram recalculados.

### `G08-C02` *(Rastreamento de `potencia_rapida` e análise de dupla chamada)*
1. Rastreie `potencia_rapida(3.0, 6)` e `potencia_rapida(2.0, 5)` (casos base `n == 0` e `n == 1`, guardando `double p = potencia_rapida(x, n / 2);`), listando cada chamada `(n, p, retorno)` e o total de chamadas em cada caso.
2. Explique por que substituir `double p = potencia_rapida(x, n / 2);` por `potencia_rapida(x, n / 2) * potencia_rapida(x, n / 2)` destrói a eficiência da divisão pela metade.

### `G08-C03` *(Implementação independente)*
Escreva um **programa completo** em C99 (sem laços nas funções recursivas) com:
- `int fib(int n);` (`fib(0) = 0`, `fib(1) = 1`)
- `double potencia_rapida(double x, int n, int *chamadas);` (casos base `n == 0` e `n == 1`, armazenando `double p` em variável local e incrementando `(*chamadas)++` na entrada)

No `main`, leia `double x`, `int n` (`n >= 0`) e `int k` (`k >= 0`), e imprima exatamente:
```text
Potencia: P.PP
Chamadas: C
Fib(K): F
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `G09` (`Revisão e Consolidação do Estágio G`):** somente após autocorreção de `G08-E01..E06` e **100% (3/3)** na Checagem Independente `G08-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** redesenhar a árvore de `fib(4)` comparando com a cadeia linear de `potencia_rapida(x, 8)`, conferir os dois casos base de `fib` (`0` e `1`) e aplicar variante `V2` de `G08`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`G03`** (recursão linear sobre inteiros e potência simples), **`G01`** (pilha de chamadas) e **`F05`** (repasse de ponteiro contador `int *chamadas`).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (itens 9 e 10 — pilha de execução e recursão).
- `[DOC]` `Aula_23_Algoritmos.pdf` p. 16–25 (Fibonacci recursivo, árvore de chamadas e comparação com versão iterativa).
- `[DOC]` `Aula_24_Algoritmos.pdf` p. 3–18 (potenciação rápida dividindo por `2` e análise da chamada dupla).
- Casos de teste e soluções verificáveis: [G08_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/gabaritos/G08_gabarito.md) e [G08_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/G08_testes.md).
