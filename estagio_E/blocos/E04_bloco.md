# Bloco `E04` — Diagonais (Principal e Secundária), Matriz Identidade e Regiões Triangulares

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio E — Matrizes Bidimensionais e Processamento Matricial / **`E04`** |
| **Micro-habilidade foco** | Identificar e operar sobre a diagonal principal (`i == j`), diagonal secundária (`i + j == N - 1`), regiões acima/abaixo da diagonal (`j > i`, `i > j`) e construir/verificar matriz identidade `N x N`. |
| **Pré-requisitos** | `E02` *(Percurso completo, soma total, busca 2D e extremos com coordenadas)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão única de prática + checagem (24 min):** `14 min` resol. \| `6 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Não utilize** funções customizadas além de `int main(void)`, VLAs (como `int m[n][n];`), `struct`, alocação dinâmica (`malloc`/`free`), transposição/simetria (`E05`) ou multiplicação matricial (`E06`). Use `#define` para tamanhos e saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Regiões de uma matriz quadrada `N x N` (`0..N-1`):**
   - **Diagonal principal (`i == j`):** acesso direto **$O(N)$** com laço único `m[i][i]`.
   - **Triângulo superior estrito (acima da principal):** `j > i` (ou `i < j`).
   - **Triângulo inferior estrito (abaixo da principal):** `i > j` (ou `j < i`).
2. **Diagonal secundária (`i + j == N - 1`):** liga `(0, N - 1)` a `(N - 1, 0)`. Como `j = N - 1 - i`, o acesso direto **$O(N)$** com laço único é:
   ```c
   for (int i = 0; i < N; i++) { /* usa m[i][N - 1 - i] */ }
   ```
   **Armadilha crítica:** escrever `i + j == N` ou `m[i][N - i]` acessa `m[0][N]` (fora dos limites!) e exclui `m[N - 1][0]`.
3. **Matriz identidade (`I_N`):** é quadrada `N x N` e satisfaz **simultaneamente** para **todos** os pares `(i, j)`:
   - quando `i == j`: `m[i][j] == 1`;
   - quando `i != j`: `m[i][j] == 0`.
4. **Verificação universal com *flag* (sem falso positivo):** inicialize `int eh_id = 1;` antes dos laços. Dentro dos laços, **jamais** coloque `else { eh_id = 1; }` (isso apagaria um erro anterior caso o último elemento `m[N-1][N-1]` seja `1`!). Apenas **desligue** `eh_id = 0;` ao achar qualquer violação:
   ```c
   int eh_id = 1;
   for (int i = 0; i < N && eh_id; i++) {
       for (int j = 0; j < N; j++) {
           if ((i == j && m[i][j] != 1) || (i != j && m[i][j] != 0)) {
               eh_id = 0;
               break;
           }
       }
   }
   ```

---

## 2. Exemplos Guiados

### Exemplo 1 — Mapa de regiões `4 x 4` e correção de omissão acima da diagonal *(Teste de mesa)*
Considere a matriz `4 x 4` (`N = 4`, índices `0..3`):
```c
int m[4][4] = {
    {1, 2, 1, 1},
    {4, 5, 2, 2},
    {7, 8, 9, 2},
    {3, 6, 1, 4}
};
```
- **Diagonal principal (`i == j`):** `(0,0)=1, (1,1)=5, (2,2)=9, (3,3)=4`.
- **Diagonal secundária (`i + j == 3`):** `(0,3)=1, (1,2)=2, (2,1)=8, (3,0)=3`.
- **Acima da diagonal principal (`j > i`):**
  - `i = 0`: `m[0][1]=2, m[0][2]=1, m[0][3]=1` (soma parcial = `4`)
  - `i = 1`: `m[1][2]=2, m[1][3]=2` (soma acumulada = `8`)
  - `i = 2`: **`m[2][3]=2`** → **soma total = `10`**!
  *(Atenção: um erro clássico visto em sala é parar o laço em `i < 2` ou ignorar a linha `2`, obtendo erradamente `8` em vez de `10` porque `m[2][3]` ainda tem `j = 3 > i = 2`!)*
- **Abaixo da diagonal principal (`i > j`):** `m[1][0]=4, m[2][0]=7, m[2][1]=8, m[3][0]=3, m[3][1]=6, m[3][2]=1` (soma = `29`).

### Exemplo 2 — Diagonais $O(N)$, soma superior e checagem de identidade (`4 x 4`) *(Programa completo)*
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

    printf("Principal:");
    for (int i = 0; i < N; i++) {
        printf(" %d", m[i][i]);
    }
    printf("\n");

    printf("Secundaria:");
    for (int i = 0; i < N; i++) {
        printf(" %d", m[i][N - 1 - i]);
    }
    printf("\n");

    int soma_acima = 0;
    int eh_id = 1;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (j > i) {
                soma_acima += m[i][j];
            }
            if ((i == j && m[i][j] != 1) || (i != j && m[i][j] != 0)) {
                eh_id = 0;
            }
        }
    }

    printf("Soma acima: %d\n", soma_acima);
    printf("Identidade: %s\n", eh_id ? "SIM" : "NAO");

    return 0;
}
```

---

## 3. Exercícios (`E04-E01` a `E04-E05`)

### `E04-E01` *(Teste de Mesa — Regiões, Diagonais e Soma Triangular)*
Considere a matriz `4 x 4`:
```c
int m[4][4] = {
    {2, 1, 2, 1},
    {3, 4, 1, 3},
    {5, 0, 6, 2},
    {1, 2, 4, 8}
};
```
Sem usar computador, responda:
1. Liste os elementos da **diagonal principal** (`m[i][i]`) e da **diagonal secundária** (`m[i][3 - i]`).
2. Liste todas as coordenadas `(i, j)` estritamente **acima** da diagonal principal (`j > i`) e calcule a soma total (verificando que `m[2][3]` está incluído, totalizando `10`).
3. Liste as coordenadas `(i, j)` estritamente **abaixo** da diagonal principal (`i > j`) e calcule sua soma.

---

### `E04-E02` *(Completar solução)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` do trecho abaixo (sobre `int m[N][N]`, com `N = 4`) para exibir a diagonal secundária em um único laço $O(N)$ e verificar com parada antecipada se `m` é matriz identidade:

```c
printf("Secundaria:");
for (int i = 0; i < N; i++) {
    printf(" %d", /* A */ );
}
printf("\n");

/* B */
for (int i = 0; /* C */ ; i++) {
    for (int j = 0; j < N; j++) {
        if ( /* D */ ) {
            eh_id = 0;
            break;
        }
    }
}
```

---

### `E04-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler uma matriz `3 x 3`, exibir a diagonal secundária (`Diag secundaria: ...`) e informar se ela é matriz identidade (`Identidade: SIM` ou `Identidade: NAO`). Identifique os **3 bugs intencionais** (no papel ou em comentários `//`) e escreva a versão corrigida completa:

```c
#include <stdio.h>
#define N 3

int main(void) {
    int m[N][N];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    printf("Diag secundaria:");
    for (int i = 0; i < N; i++) {
        printf(" %d", m[i][N - i]);
    }
    printf("\n");

    int eh_id = 1;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i == j && m[i][j] != 1) {
                eh_id = 0;
            } else {
                eh_id = 1;
            }
        }
    }

    if (eh_id) {
        printf("Identidade: SIM\n");
    } else {
        printf("Identidade: NAO\n");
    }

    return 0;
}
```

---

### `E04-E04` *(Variação controlada com pistas)*
Escreva um **programa completo** em C usando `#define N 4` que leia uma matriz `4 x 4` de inteiros e imprima exatamente:
```text
Diag principal: d0 d1 d2 d3
Diag secundaria: s0 s1 s2 s3
Soma acima: A
Soma abaixo: B
```
*Pista:* use laços únicos $O(N)$ para as diagonais (`m[i][i]` e `m[i][N - 1 - i]`) e laços aninhados acumulando `j > i` em `soma_acima` e `i > j` em `soma_abaixo`.

---

### `E04-E05` *(Resolução independente)*
Escreva um **programa completo** em C usando `#define MAX 10` que leia `n` (`1 <= n <= MAX`) e os `n * n` inteiros de `m[MAX][MAX]`. Imprima exatamente:
```text
Diag principal: p0 ... pn-1
Diag secundaria: s0 ... sn-1
Identidade: SIM
```
*(ou `Identidade: NAO` caso não seja matriz identidade `n x n`)*.

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `E04-C01` *(Rastreamento Triangular e Falso Positivo de Identidade)*
Considere a matriz `4 x 4`:
```c
int m[4][4] = {
    {1, 3, 1, 2},
    {2, 1, 4, 1},
    {0, 5, 1, 3},
    {1, 0, 2, 1}
};
```
Responda sem compilador:
1. Qual é a soma exata dos elementos estritamente **acima** da diagonal principal (`j > i`) e dos estritamente **abaixo** (`i > j`)?
2. Por que um verificador de identidade que escreve `else { eh_id = 1; }` dentro dos laços devolve erradamente `SIM` para a matriz `m` acima?

### `E04-C02` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler uma matriz `4 x 4` e imprimir a soma da diagonal secundária (`Soma sec: S`), a soma abaixo da diagonal principal (`Soma abaixo: B`) e se ela é matriz identidade (`Identidade: SIM` / `Identidade: NAO`). Corrija todos os defeitos presentes:

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

    int soma_sec = 0, soma_abaixo = 0;
    int eh_id = 1;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i + j == N) {
                soma_sec += m[i][j];
            }
            if (j > i) {
                soma_abaixo += m[i][j];
            }
            if ((i == j && m[i][j] != 1) || (i != j && m[i][j] != 0)) {
                eh_id = 0;
            } else {
                eh_id = 1;
            }
        }
    }

    printf("Soma sec: %d\n", soma_sec);
    printf("Soma abaixo: %d\n", soma_abaixo);
    if (eh_id) {
        printf("Identidade: SIM\n");
    } else {
        printf("Identidade: NAO\n");
    }

    return 0;
}
```

### `E04-C03` *(Programa completo independente)*
Escreva um programa completo em C usando `#define MAX 10` que leia `n` (`1 <= n <= MAX`) e uma matriz quadrada `n x n` em `m[MAX][MAX]`, imprimindo exatamente:
```text
Soma principal: P
Soma secundaria: S
Soma acima: A
Soma abaixo: B
Identidade: SIM
```
*(ou `Identidade: NAO` quando não for matriz identidade)*.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `E05` (`Transposição, Verificação de Simetria e Soma de Matrizes`):** somente após autocorreção de `E04-E01..E05` e **100% (3/3)** em `E04-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** revisar a fórmula da diagonal secundária (`i + j == N - 1` → `m[i][N - 1 - i]`), a distinção `j > i` (acima) vs. `i > j` (abaixo) com inclusão de `m[N - 2][N - 1]`, e a proibição de rearmar a flag (`eh_id = 1;`) dentro dos laços; aplicar variante `V2` de `E04`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`E02`** (percurso completo em 2D e saída antecipada com flag), **`E01`** (limites `0..N-1`) e **`B03`/`D04`** (verificação universal com flag sem falso positivo).

---

## 6. Referências do Orientador
- `[DOC]` `Aula_14_Algoritmos.pdf` p. 21–22, 26 (Ex. 2 — diagonal principal e identidade).
- `[DOC]` `Aula_15_Algoritmos.pdf` p. 13–15, 24 (Ex. 2 — diagonais e regiões triangulares, com correção da errata aritmética de `8` para `10`).
- `[DOC]` `Lista9_Algoritmos.pdf` p. 2 (Ex. 4 e Ex. 6a — diagonais e matriz identidade).
- Casos de teste e soluções verificáveis: [E04_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/gabaritos/E04_gabarito.md) e [E04_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/E04_testes.md).
