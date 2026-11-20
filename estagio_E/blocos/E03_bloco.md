# Bloco `E03` — Fatiamento e Acumuladores por Linha e por Coluna

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio E — Matrizes Bidimensionais e Processamento Matricial / **`E03`** |
| **Micro-habilidade foco** | Fixar linhas ou colunas específicas (`m[k][j]`, `m[i][k]`) e calcular somas independentes por linha e por coluna alternando a ordem dos laços `i`/`j` com reinicialização adequada do acumulador. |
| **Pré-requisitos** | `E02` *(Percurso completo, soma total, busca 2D e extremos com coordenadas)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão única de prática + checagem (22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Não utilize** funções customizadas além de `int main(void)`, VLAs (como `int m[l][c];`), `struct`, alocação dinâmica (`malloc`/`free`), diagonais/matriz identidade (`E04`) ou transposição (`E05`). Use `#define` para dimensões e saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Fatiamento (fixar 1 linha ou 1 coluna com laço único):**
   - **Linha fixa `k`** (`0 <= k < L`): fixe o 1º índice e varie a coluna `j`:
     ```c
     for (int j = 0; j < C; j++) { /* usa m[k][j] */ }
     ```
   - **Coluna fixa `k`** (`0 <= k < C`): fixe o 2º índice e varie a linha `i`:
     ```c
     for (int i = 0; i < L; i++) { /* usa m[i][k] */ }
     ```
2. **Armadilha ordinal vs. base 0:** quando o enunciado pede a *"2ª linha"* ou *"3ª coluna"* em contagem humana (ordinal, a partir de 1), converta para base 0 subtraindo 1 (`linha = 2 - 1 = 1`, `coluna = 3 - 1 = 2`). Se o enunciado já fornece o *"índice `k` (`0 <= k < L`)"*, use `k` diretamente.
3. **Soma de CADA linha vs. soma de CADA coluna:**
   - **Cada linha:** `i` no laço externo (`0..L-1`), `j` no laço interno (`0..C-1`).
   - **Cada coluna:** inverta os laços — **`j` no laço externo (`0..C-1`), `i` no laço interno (`0..L-1`)** — mantendo o acesso **`m[i][j]`** (nunca troque para `m[j][i]`!).
4. **Reinicialização obrigatória do acumulador:** zere `int soma = 0;` **dentro do laço externo, imediatamente antes do laço interno**. Se inicializar `soma = 0` fora de ambos os laços sem zerar a cada iteração, a soma das linhas/colunas anteriores vaza para as seguintes. *(Opcionalmente, você também pode acumular em vetores `somas_lin[L] = {0}` e `somas_col[C] = {0}`.)*

---

## 2. Exemplos Guiados

### Exemplo 1 — Fatiamento de linha e coluna com contagem ordinal *(Trecho ilustrativo)*
Em uma matriz `int m[3][4];`, para exibir a **2ª linha** (ordinal → índice `2 - 1 = 1`) e a **4ª coluna** (ordinal → índice `4 - 1 = 3`):
```c
/* 2a linha (indice 1): varia j de 0 ate 3 */
for (int j = 0; j < 4; j++) {
    printf("%d ", m[1][j]);
}
printf("\n");

/* 4a coluna (indice 3): varia i de 0 ate 2 */
for (int i = 0; i < 3; i++) {
    printf("%d ", m[i][3]);
}
printf("\n");
```

### Exemplo 2 — Somas de todas as linhas e de todas as colunas (`4 x 4`) *(Programa completo)*
```c
#include <stdio.h>
#define N 4

int main(void) {
    int m[N][N];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    printf("Somas das linhas:");
    for (int i = 0; i < N; i++) {
        int soma = 0;
        for (int j = 0; j < N; j++) {
            soma += m[i][j];
        }
        printf(" %d", soma);
    }
    printf("\n");

    printf("Somas das colunas:");
    for (int j = 0; j < N; j++) {
        int soma = 0;
        for (int i = 0; i < N; i++) {
            soma += m[i][j];
        }
        printf(" %d", soma);
    }
    printf("\n");

    return 0;
}
```

---

## 3. Exercícios (`E03-E01` a `E03-E05`)

### `E03-E01` *(Teste de Mesa — Acumulador não zerado e Fatiamento Ordinal)*
Considere a matriz `3 x 3`:
```c
int m[3][3] = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};
```
Sem usar computador, responda:
1. No trecho **bugado** abaixo, `soma` foi zerada apenas fora do laço externo. Quais três números serão impressos em `Linhas:` em vez de `6 15 24`?
   ```c
   int soma = 0;
   printf("Linhas:");
   for (int i = 0; i < 3; i++) {
       for (int j = 0; j < 3; j++) {
           soma += m[i][j];
       }
       printf(" %d", soma);
   }
   ```
2. Escreva a expressão de acesso em `m` (com índice base 0) e liste os valores resultantes para:
   - `(a)` a **3ª linha** (ordinal);
   - `(b)` a **1ª coluna** (ordinal).

---

### `E03-E02` *(Completar solução)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` do trecho abaixo (com `int m[L][C]` já preenchida, `L = 3, C = 4`) para calcular e imprimir a soma de **cada uma das 4 colunas**:

```c
printf("Colunas:");
for ( /* A */ ) {
    /* B */
    for ( /* C */ ) {
        soma += /* D */ ;
    }
    printf(" %d", soma);
}
printf("\n");
```

---

### `E03-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler uma matriz `3 x 4` e imprimir a soma de cada linha (`Linhas: s0 s1 s2`) e a soma de cada coluna (`Colunas: c0 c1 c2 c3`). Identifique os **3 bugs intencionais** (no papel ou em comentários `//`) e escreva a versão corrigida completa:

```c
#include <stdio.h>
#define L 3
#define C 4

int main(void) {
    int m[L][C];
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    int soma = 0;
    printf("Linhas:");
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            soma += m[i][j];
        }
        printf(" %d", soma);
    }
    printf("\n");

    printf("Colunas:");
    for (int j = 0; j < L; j++) {
        int soma_col = 0;
        for (int i = 0; i < C; i++) {
            soma_col += m[j][i];
        }
        printf(" %d", soma_col);
    }
    printf("\n");

    return 0;
}
```

---

### `E03-E04` *(Variação controlada com pistas)*
Escreva um **programa completo** em C usando `#define L 3` e `#define C 4` que leia uma matriz `3 x 4` de inteiros e depois leia dois inteiros **ordinais** `lin` (`1 <= lin <= 3`) e `col` (`1 <= col <= 4`). Imprima exatamente:
```text
Linha <lin>: x0 x1 x2 x3
Soma linha: S_L
Coluna <col>: y0 y1 y2
Soma coluna: S_C
```
*Pista:* converta `int idx_l = lin - 1;` e `int idx_c = col - 1;` para base 0 antes de percorrer `m[idx_l][j]` e `m[i][idx_c]`.

---

### `E03-E05` *(Resolução independente)*
Escreva um **programa completo** em C usando `#define N 4` que leia uma matriz `4 x 4` de inteiros e imprima exatamente:
```text
Linhas: s0 s1 s2 s3
Colunas: c0 c1 c2 c3
Maior linha: idx (M)
```
onde `idx` (`0..3`) é o índice base 0 da linha com a maior soma (em caso de empate, mantenha a **1ª ocorrência** com `>`) e `M` é o valor dessa soma.

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `E03-C01` *(Análise de Erro de Acumulador e Fatiamento)*
Considere a matriz `2 x 3`:
```c
int m[2][3] = {
    {5, -2, 4},
    {3, 1, -4}
};
```
Responda sem compilador:
1. Se um programa calcular a soma das colunas com `int soma = 0;` fora do `for (int j = 0; j < 3; j++)` (sem zerar antes de cada coluna), quais valores serão exibidos para as 3 colunas? Quais seriam os valores corretos?
2. Quais são os elementos da **1ª linha** (ordinal) e da **3ª coluna** (ordinal), e quais expressões `m[...][...]` os acessam?

### `E03-C02` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler uma matriz `3 x 5` e um índice **base 0** `k` (`0 <= k < 5`), imprimindo a soma de cada linha (`Linhas: s0 s1 s2`) e os elementos da coluna `k` (`Coluna <k>: ...`). Corrija todos os defeitos presentes:

```c
#include <stdio.h>
#define L 3
#define C 5

int main(void) {
    int m[L][C];
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    int k;
    scanf("%d", &k);

    int soma = 0;
    printf("Linhas:");
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            soma += m[i][j];
        }
        printf(" %d", soma);
    }
    printf("\n");

    printf("Coluna %d:", k);
    for (int i = 0; i < C; i++) {
        printf(" %d", m[k][i]);
    }
    printf("\n");

    return 0;
}
```

### `E03-C03` *(Programa completo independente)*
Escreva um programa completo em C usando `#define MAX 10` que leia `l` e `c` (`1 <= l, c <= MAX`) e uma matriz `l x c` de inteiros em `m[MAX][MAX]`, imprimindo exatamente:
```text
Linhas: s0 s1 ... sl-1
Colunas: c0 c1 ... cc-1
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `E04` (`Diagonais, Matriz Identidade e Regiões Triangulares`):** somente após autocorreção de `E03-E01..E05` e **100% (3/3)** em `E03-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** revisar a inversão de cabeçalhos `for (j...) { for (i...) }` mantendo `m[i][j]`, o posicionamento de `soma = 0;` entre o laço externo e o interno, e a subtração `- 1` para entradas ordinais; aplicar variante `V2` de `E03`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`E01`** (dimensões `L` e `C` e indexação `m[linha][coluna]`), **`E02`** (extremos e percurso completo) e **`C02`** (reinicialização de acumuladores).

---

## 6. Referências do Orientador
- `[DOC]` `Aula_15_Algoritmos.pdf` p. 4–12, 23 (Ex. 1 — fatiamento linha/coluna, soma por linha e soma por coluna).
- `[DOC]` `Lista9_Algoritmos.pdf` p. 1 (Ex. 1b–c e Ex. 2 — somas de linhas e colunas em `4 x 4`, adaptado de K. N. King Cap. 8).
- Casos de teste e soluções verificáveis: [E03_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/gabaritos/E03_gabarito.md) e [E03_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/E03_testes.md).
