# Bloco `D01` — Vetores 1D: Declaração, Índices Base 0, Inicialização e Limites de Memória

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio D — Vetores Unidimensionais e Strings / **`D01`** |
| **Micro-habilidade foco** | Declarar vetores de tamanho fixo (`#define N`), inicializar na declaração (`{...}` e `{0}`), ler com `scanf("%d", &v[i])` e percorrer sem ultrapassar os limites `[0 .. N-1]`. |
| **Pré-requisitos** | `C10` *(Revisão e Consolidação do Estágio C — Estruturas de Repetição)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão única de prática + checagem (22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Não utilize** funções próprias além de `main`, strings (`char[]`/`<string.h>`), matrizes 2D ou VLAs (vetores de tamanho variável como `int v[n];`). Use constantes (`#define N 5`, `#define MAX 50`) para declarar o tamanho do vetor. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Vetor é memória contígua homogênea:** um vetor armazena `N` valores do **mesmo tipo** em posições vizinhas na memória.
2. **Tamanho fixo em compilação (sem VLA):** defina o tamanho com `#define N 5` (ou constante literal) e declare `int v[N];`. **Nunca** declare `int v[n];` usando variável `n`. Quando a quantidade de dados variar em tempo de execução, declare um vetor de capacidade fixa `#define MAX 50`, `int v[MAX];`, e leia `n` (`1 <= n <= MAX`).
3. **Dois papéis dos colchetes `[ ]` e base 0:**
   - Na **declaração** (`int v[5];`): o número indica a **capacidade total** (`5` elementos).
   - No **acesso** (`v[i]`): `i` é o **índice** (deslocamento a partir do início), que vai obrigatoriamente de **`0` até `N - 1`**.
   - **Cuidado crítico:** `v[N]` (como `v[5]` em um vetor de tamanho `5`) **não existe**! C não verifica limites automaticamente: acessar `v[-1]` ou `v[N]` causa comportamento indefinido (*out-of-bounds*).
4. **Inicialização vs. lixo de memória:**
   - `int v[5];` (local, sem `=`) contém **lixo de memória** em todas as posições.
   - `int v[5] = {10, 20};` (parcial) preenche `v[0] = 10`, `v[1] = 20` e zera automaticamente `v[2..4]`.
   - `int v[5] = {0};` zera todas as `5` posições.
5. **Leitura com `&v[i]` e impressão inversa sem modificar o vetor:**
   - Cada `v[i]` é uma variável comum do tipo do vetor, logo exige `&` no `scanf`: `scanf("%d", &v[i]);`.
   - Para exibir do fim para o começo **sem alterar `v`**, use `for (int i = n - 1; i >= 0; i--)`.

---

## 2. Exemplos Guiados

### Exemplo 1 — Mapa de memória, inicialização parcial e índices válidos *(Trecho ilustrativo)*
Considere `#define N 5` e as declarações abaixo:
```c
int a[N] = {7, 4};    /* a = {7, 4, 0, 0, 0} */
int b[N] = {0};       /* b = {0, 0, 0, 0, 0} */
int c[N];             /* lixo indeterminado em c[0..4] */
```
Mapa de memória de `a`:
- Índices válidos: `0`, `1`, `2`, `3`, `4` (`0 <= i < N`).
- `a[0]` vale `7`, `a[1]` vale `4`, `a[2]`, `a[3]` e `a[4]` valem `0`.
- `a[5]` é **inválido** (fora do vetor!).

### Exemplo 2 — Leitura, exibição direta e exibição inversa *(Programa completo)*
```c
#include <stdio.h>
#define N 5

int main(void) {
    int v[N];

    for (int i = 0; i < N; i++) {
        scanf("%d", &v[i]);
    }

    printf("Direta:");
    for (int i = 0; i < N; i++) {
        printf(" %d", v[i]);
    }
    printf("\n");

    printf("Inversa:");
    for (int i = N - 1; i >= 0; i--) {
        printf(" %d", v[i]);
    }
    printf("\n");

    return 0;
}
```
*Observação:* o percurso `N - 1` até `0` apenas **lê** os elementos ao contrário; na memória, `v[0]` continua sendo o primeiro elemento lido.

---

## 3. Exercícios (`D01-E01` a `D01-E05`)

### `D01-E01` *(Leitura e Análise de Memória — Reprodução do modelo)*
Considere as declarações locais dentro de `main`:
```c
#define TAM 5
int a[TAM] = {3, 8, 1};
int b[4] = {0};
int c[3];
```
Sem usar computador, responda:
1. Qual é o conteúdo exato de `a[0]`, `a[1]`, `a[2]`, `a[3]` e `a[4]`?
2. Qual é o conteúdo de `b[0..3]` e o que se pode afirmar sobre `c[0..2]`?
3. Quais índices são válidos para acessar `a`? Por que `a[5] = 9;` é um erro grave?

---

### `D01-E02` *(Completar solução)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` do trecho abaixo para declarar um vetor de tamanho fixo `N = 6`, ler os `6` inteiros e depois imprimir primeiro os elementos em **índices pares** (`0, 2, 4`) e em seguida todos em **ordem inversa**:

```c
#define N 6
/* ... dentro de main ... */
int v[ /* A */ ];

for (int i = 0; i < N; i++) {
    scanf("%d", /* B */ );
}

printf("Indices pares:");
for (int i = 0; i < N; /* C */ ) {
    printf(" %d", v[i]);
}
printf("\nInversa:");
for (int i = /* D */ ; i >= 0; i--) {
    printf(" %d", v[i]);
}
printf("\n");
```

---

### `D01-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler `5` inteiros para `v[N]` e imprimir os valores na ordem direta e na ordem inversa, no formato `Direta: ...` e `Inversa: ...`. Identifique os **3 bugs intencionais** (no papel ou em comentários `//`) e escreva a versão corrigida completa:

```c
#include <stdio.h>
#define N 5

int main(void) {
    int v[N];

    for (int i = 0; i <= N; i++) {
        scanf("%d", v[i]);
    }

    printf("Direta:");
    for (int i = 0; i < N; i++) {
        printf(" %d", v[i]);
    }
    printf("\nInversa:");
    for (int i = N; i > 0; i--) {
        printf(" %d", v[i]);
    }
    printf("\n");

    return 0;
}
```

---

### `D01-E04` *(Variação controlada com pistas)*
Escreva um **programa completo** em C usando `#define N 6` que leia `6` inteiros em `v[N]` e imprima em duas linhas:
```text
Metade 2: v[3] v[4] v[5]
Metade 1: v[0] v[1] v[2]
```
(substituindo pelos valores lidos, **sem alterar o vetor `v`**).  
*Pista:* Use um laço de `i = N / 2` até `i < N` para `Metade 2:` e outro de `i = 0` até `i < N / 2` para `Metade 1:`.

---

### `D01-E05` *(Resolução independente)*
Escreva um **programa completo** em C usando `#define MAX 50` que leia `n` (`1 <= n <= MAX`) e depois `n` inteiros para `v[MAX]`. Imprima exatamente no formato abaixo, sem modificar o vetor `v`:
```text
Direta: x0 x1 ... xn-1
Inversa: xn-1 ... x1 x0
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `D01-C01` *(Análise de Memória e Limites)*
Dado `#define TAM 4` e `int x[TAM] = {10, 20};`, responda sem compilador:
1. Quais são os valores de `x[0]`, `x[1]`, `x[2]` e `x[3]`?
2. Qual é o intervalo de índices válidos para `x`?
3. Explique qual erro existe em cada declaração/acesso abaixo:
   - `(a)` `int m = 4; int y[m];`
   - `(b)` `x[4] = 99;`

### `D01-C02` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler `n` (`1 <= n <= 20`), ler `n` inteiros e imprimir os elementos de **índice ímpar** (`1, 3, ...`) e depois todos em **ordem inversa**, no formato `Impares:` e `Inverso:`. Corrija todos os defeitos presentes:

```c
#include <stdio.h>
#define MAX 20

int main(void) {
    int n;
    scanf("%d", &n);
    int v[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", v[i]);
    }

    printf("Impares:");
    for (int i = 1; i < n; i += 2) {
        printf(" %d", v[i]);
    }
    printf("\nInverso:");
    for (int i = n; i >= 1; i--) {
        printf(" %d", v[i]);
    }
    printf("\n");

    return 0;
}
```

### `D01-C03` *(Programa completo independente)*
Escreva um programa completo em C usando `#define MAX 50` que leia `n` (`1 <= n <= MAX`) e `n` inteiros para `v[MAX]`. Sem modificar o vetor `v`, imprima exatamente:
```text
Primeiro: A | Ultimo: B
Inverso: x_n-1 ... x_0
```
onde `A` é `v[0]` e `B` é `v[n - 1]`.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `D02` (`Acumulação, Contagem Condicional e Busca de Extremos`):** somente após autocorreção de `D01-E01..E05` e **100% (3/3)** em `D01-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** revisar a diferença entre capacidade na declaração (`v[N]`) e intervalo de índices (`0 .. N-1`), além da obrigatoriedade de `&` em `scanf("%d", &v[i])`; aplicar variante `V2` de `D01`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`A05`** (`#define`), **`A06`** (`&` no `scanf`) e **`C05`/`C10`** (`for` de `0` até `< n` e regressivo de `n - 1` até `>= 0`).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 8 — vetores unidimensionais).
- `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 3 (06/10).
- `[DOC]` `Aula_11_Algoritmos.pdf` p. 10–29 (declaração fixa, base 0, inicialização `{0}`, leitura com `&v[i]`, percurso direto/inverso e limites).
- Casos de teste e soluções verificáveis: [D01_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/gabaritos/D01_gabarito.md) e [D01_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/D01_testes.md).
