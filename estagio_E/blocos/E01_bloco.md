# Bloco `E01` — Matrizes 2D: Declaração, Armazenamento *Row-Major*, Acesso e Leitura/Escrita em Grade

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio E — Matrizes Bidimensionais e Processamento Matricial / **`E01`** |
| **Micro-habilidade foco** | Declarar e inicializar matrizes `tipo m[L][C];` (tamanho fixo), compreender o armazenamento linha por linha (`m[i]` como vetor-linha) e ler/exibir dados em formato de tabela. |
| **Pré-requisitos** | `D10` *(Revisão e Consolidação do Estágio D — Vetores 1D, Strings e Linearização `i * C + j`)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão única de prática + checagem (20 min):** `12 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Não utilize** funções customizadas além de `int main(void)`, VLAs (matrizes de tamanho variável como `int m[l][c];`), `struct`, alocação dinâmica (`malloc`/`free`), busca/extremos (`E02`), somas por linha/coluna (`E03`) ou diagonais (`E04`). Use `#define` ou literais para dimensões e saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Declaração com tamanho fixo (sem VLA):** defina dimensões com `#define L 3` e `#define C 4` (ou `#define MAX 10`) e declare `int m[L][C];`. **Nunca** declare `int m[l][c];` usando variáveis. Quando as dimensões reais `l` e `c` vierem do teclado, declare capacidade máxima fixa `int m[MAX][MAX];` e leia `l` e `c` (`1 <= l, c <= MAX`).
2. **Índices válidos (`0..L-1` e `0..C-1`):** em `m[i][j]`, o **1º índice (`i`)** é a **linha** e o **2º índice (`j`)** é a **coluna**. C não verifica limites: acessar `m[L][0]` ou `m[0][C]` invade memória alheia (*out-of-bounds*).
3. **Armazenamento *row-major* e `m[i]` como vetor-linha:** na memória, C armazena a matriz **linha por linha** (toda a linha `0`, depois toda a linha `1`, etc.), ocupando `L * C` posições contíguas — exatamente na ordem `i * C + j` vista em `D09`. Cada `m[i]` funciona como o vetor-linha `i` de `C` elementos.
4. **Inicialização na declaração:**
   - `int m[2][3] = {{1, 2, 3}, {4, 5, 6}};` inicializa linha por linha.
   - `int m[2][3] = {{1}, {4, 5}};` completa o restante de cada linha com `0` (`{1, 0, 0}` e `{4, 5, 0}`).
   - `int m[3][4] = {0};` zera todas as posições; `int m[3][4];` (local, sem `=`) contém **lixo de memória**.
5. **Leitura e impressão tabular:** use dois laços `for` aninhados (`i` externo para linhas, `j` interno para colunas). Na leitura, `scanf("%d", &m[i][j]);` exige `&`. Na impressão em grade, exiba os elementos da linha no laço interno (`j`) e execute `printf("\n");` **logo após o laço interno** (ainda dentro do laço externo `i`).

---

## 2. Exemplos Guiados

### Exemplo 1 — Armazenamento *row-major*, inicialização parcial e limites *(Trecho ilustrativo)*
Considere `#define L 3` e `#define C 4`:
```c
int a[L][C] = {
    {2, 5},
    {9}
};
```
Mapa completo da matriz `a` na memória (*row-major*):
- **Linha `0` (`a[0]`):** `{2, 5, 0, 0}` → deslocamentos lineares `0, 1, 2, 3`
- **Linha `1` (`a[1]`):** `{9, 0, 0, 0}` → deslocamentos lineares `4, 5, 6, 7`
- **Linha `2` (`a[2]`):** `{0, 0, 0, 0}` → deslocamentos lineares `8, 9, 10, 11`
- O elemento `a[1][2]` vale `0` e ocupa a posição linear `1 * 4 + 2 = 6`.
- `a[3][0]` e `a[1][4]` são **inválidos** (índices válidos são `0 <= i <= 2` e `0 <= j <= 3`).

### Exemplo 2 — Leitura e impressão em grade tabular *(Programa completo)*
```c
#include <stdio.h>
#define L 2
#define C 3

int main(void) {
    int m[L][C];

    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", m[i][j]);
        }
        printf("\n");
    }

    return 0;
}
```
*Observação:* o `if (j > 0) printf(" ");` evita espaço sobrando ao final de cada linha, e `printf("\n");` ocorre exatamente uma vez ao final de cada linha `i`.

---

## 3. Exercícios (`E01-E01` a `E01-E05`)

### `E01-E01` *(Leitura e Análise de Memória — Reprodução do modelo)*
Considere as declarações locais dentro de `main`:
```c
#define L 3
#define C 4
int a[L][C] = {{1, 2}, {3, 4, 5}};
int b[2][2] = {0};
```
Sem usar computador, responda:
1. Qual é o valor armazenado em `a[0][2]`, `a[1][2]`, `a[2][0]` e `b[1][1]`?
2. No armazenamento *row-major* (`0` a `11`), em qual posição linear estão `a[1][3]` e `a[2][1]`?
3. Por que `a[3][1] = 10;` e `a[0][4] = 10;` são acessos inválidos?

---

### `E01-E02` *(Completar solução)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` do trecho abaixo para declarar `int m[L][C]` (`L = 3, C = 4`), ler os `12` inteiros e exibi-los em formato tabular (`3` linhas por `4` colunas):

```c
#define L 3
#define C 4
/* ... dentro de main ... */
int m[ /* A */ ][C];

for (int i = 0; i < L; i++) {
    for (int j = 0; j < C; j++) {
        scanf("%d", /* B */ );
    }
}

for (int i = 0; i < L; i++) {
    for (int j = 0; /* C */ ; j++) {
        if (j > 0) {
            printf(" ");
        }
        printf("%d", m[i][j]);
    }
    /* D */
}
```

---

### `E01-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler uma matriz `2 x 3` de inteiros e imprimi-la em grade tabular (`2` linhas, `3` números por linha separados por espaço). Identifique os **3 bugs intencionais** (no papel ou em comentários `//`) e escreva a versão corrigida completa:

```c
#include <stdio.h>
#define L 2
#define C 3

int main(void) {
    int m[L][C];

    for (int i = 0; i < L; i++) {
        for (int j = 0; j <= C; j++) {
            scanf("%d", m[i][j]);
        }
    }

    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", m[i][j]);
            printf("\n");
        }
    }

    return 0;
}
```

---

### `E01-E04` *(Variação controlada com pistas)*
Escreva um **programa completo** em C usando `#define L 3` e `#define C 3` que leia `9` inteiros para `m[L][C]` e imprima a matriz com as **linhas em ordem inversa** (primeiro a linha `2`, depois a linha `1`, depois a linha `0`), mantendo as colunas em ordem direta (`0` a `2`) e separando os valores da mesma linha por um espaço simples.  
*Pista:* na exibição, faça o laço externo com `for (int i = L - 1; i >= 0; i--)` e o interno com `for (int j = 0; j < C; j++)`.

---

### `E01-E05` *(Resolução independente)*
Escreva um **programa completo** em C usando `#define MAX_L 10` e `#define MAX_C 10` que leia `l` (`1 <= l <= MAX_L`) e `c` (`1 <= c <= MAX_C`) e em seguida leia os `l * c` inteiros da matriz `m[MAX_L][MAX_C]`. Imprima exatamente no formato abaixo:
```text
Cantos: A B
<linha 0 separada por espaco>
...
<linha l-1 separada por espaco>
```
onde `A` é `m[0][0]` e `B` é `m[l - 1][c - 1]`.

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `E01-C01` *(Análise de Memória, Row-Major e Limites)*
Dado `#define L 3`, `#define C 3` e `int x[L][C] = {{7}, {8, 9}};`, responda sem compilador:
1. Quais são os valores de `x[0][1]`, `x[1][1]` e `x[2][0]`?
2. Qual posição linear (`0..8`) em *row-major* corresponde a `x[2][1]`?
3. Explique o erro em cada código abaixo:
   - `(a)` `int l = 3, c = 3; int y[l][c];`
   - `(b)` `x[2][3] = 5;`

### `E01-C02` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler `l` e `c` (`1 <= l, c <= 10`), ler uma matriz `l x c` de inteiros e imprimi-la em grade tabular (`l` linhas, `c` valores por linha separados por espaço). Corrija todos os defeitos presentes:

```c
#include <stdio.h>
#define MAX 10

int main(void) {
    int l, c;
    scanf("%d %d", &l, &c);
    int m[l][c];

    for (int i = 0; i < l; i++) {
        for (int j = 0; j < c; j++) {
            scanf("%d", m[i][j]);
        }
    }

    for (int i = 0; i < l; i++) {
        for (int j = 0; j < c; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", m[i][j]);
        }
    }

    return 0;
}
```

### `E01-C03` *(Programa completo independente)*
Escreva um programa completo em C usando `#define L 3` e `#define C 4` que leia `12` inteiros para `m[L][C]` e imprima a grade original (`Matriz:`) seguida da grade percorrida de baixo para cima e da direita para a esquerda (`Inversa:`):
```text
Matriz:
<3 linhas com 4 inteiros cada>
Inversa:
<3 linhas com 4 inteiros cada, de i=L-1..0 e j=C-1..0>
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `E02` (`Percurso Completo, Soma Total, Busca 2D e Extremos com Coordenadas`):** somente após autocorreção de `E01-E01..E05` e **100% (3/3)** em `E01-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** revisar a ordem `[linha][coluna]` (`0..L-1`, `0..C-1`), a obrigatoriedade de `&m[i][j]` no `scanf`, a proibição de VLA (`int m[l][c];`) e o posicionamento do `printf("\n");` após o laço interno `j`; aplicar variante `V2` de `E01`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`D09`** (mapeamento *row-major* `i * C + j`), **`D01`** (declaração fixa com `#define`, base 0 e `&` no `scanf`) e **`C09`** (laços `for` aninhados).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 8 — matrizes multidimensionais).
- `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 3 (16/10).
- `[DOC]` `Aula_14_Algoritmos.pdf` p. 3, 7–18, 25 (Ex. 1 — declaração, *row-major*, inicialização, `m[i]` como vetor-linha, leitura/impressão).
- `[DOC]` `Lista9_Algoritmos.pdf` p. 1 (Ex. 1a).
- Casos de teste e soluções verificáveis: [E01_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/gabaritos/E01_gabarito.md) e [E01_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/E01_testes.md).
