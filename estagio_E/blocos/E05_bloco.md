# Bloco `E05` — Transposição, Verificação de Simetria e Soma de Matrizes

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio E — Matrizes Bidimensionais e Processamento Matricial / **`E05`** |
| **Micro-habilidade foco** | Construir a matriz transposta `T[C][L]` a partir de uma matriz retangular `A[L][C]`, somar matrizes elemento a elemento e verificar simetria ($A[i][j] == A[j][i]$) com flag universal. |
| **Pré-requisitos** | `E03` *(Fatiamento e Acumuladores por Linha e por Coluna)* e `E04` *(Diagonais, Matriz Identidade e Regiões Triangulares)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão única de prática + checagem (22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Não utilize** funções próprias além de `int main(void)`, VLAs (`int a[l][c];`), `struct`, alocação dinâmica (`malloc`/`free`) ou multiplicação de matrizes (tópico de `E06`). Use `#define MAX 20` e matrizes de capacidade fixa. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Imprimir transposta vs. construir matriz transposta (`T[j][i] = A[i][j]`):**
   - Apenas imprimir colunas como linhas não gera a matriz transposta na memória. Para construir a transposta real `T` de `A` (`L` linhas × `C` colunas), declare `T` com dimensões invertidas (`C` linhas × `L` colunas) e atribua **`T[j][i] = A[i][j];`** para `0 <= i < L` e `0 <= j < C`.
   - **Armadilha de dimensões assimétricas:** em uma matriz retangular (`L != C`, ex.: `3 x 4` → `4 x 3`), **não** é possível transpor *in-place* dentro da própria matriz `A` sem invadir índices fora dos limites! Ao exibir `T`, os laços devem usar `i < C` (linhas de `T`) e `j < L` (colunas de `T`).
2. **Soma de matrizes (`S[i][j] = A[i][j] + B[i][j]`):**
   - Duas matrizes `A` (`L1 x C1`) e `B` (`L2 x C2`) só podem ser somadas se possuírem **exatamente as mesmas dimensões** (`L1 == L2 && C1 == C2`). Se `L1 != L2 || C1 != C2`, a soma é impossível.
3. **Verificação de simetria ($A = A^T$):**
   - Uma matriz só pode ser simétrica se for **quadrada** (`L == C`) e satisfizer `A[i][j] == A[j][i]` para todo par `(i, j)`.
   - Como `A[i][i] == A[i][i]` é sempre verdadeiro e `A[i][j] == A[j][i]` equivale a `A[j][i] == A[i][j]`, basta iniciar `int sim = 1;` e testar apenas o triângulo superior (`j > i`, isto é, `for (int j = i + 1; j < N; j++)`). Na primeira diferença (`A[i][j] != A[j][i]`), zere `sim = 0;` e interrompa.

---

## 2. Exemplos Guiados

### Exemplo 1 — Transposição de matriz retangular `2 x 3` → `3 x 2` *(Trecho ilustrativo)*
Dada `A[2][3] = {{1, 2, 3}, {4, 5, 6}}` (`L = 2`, `C = 3`):
```c
int T[MAX][MAX];
for (int i = 0; i < L; i++) {
    for (int j = 0; j < C; j++) {
        T[j][i] = A[i][j];
    }
}
/* T ocupa 3 linhas e 2 colunas:
   Linha 0: 1 4   (T[0][0] = A[0][0], T[0][1] = A[1][0])
   Linha 1: 2 5   (T[1][0] = A[0][1], T[1][1] = A[1][1])
   Linha 2: 3 6   (T[2][0] = A[0][2], T[2][1] = A[1][2]) */
```

### Exemplo 2 — Soma e verificação de simetria *(Programa completo)*
```c
#include <stdio.h>
#define MAX 20

int main(void) {
    int N, A[MAX][MAX], B[MAX][MAX], S[MAX][MAX];
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &A[i][j]);
        }
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &B[i][j]);
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            S[i][j] = A[i][j] + B[i][j];
        }
    }

    int sim = 1;
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            if (S[i][j] != S[j][i]) {
                sim = 0;
                break;
            }
        }
        if (!sim) {
            break;
        }
    }

    printf("Simetrica: %s\n", sim ? "Sim" : "Nao");
    return 0;
}
```

---

## 3. Exercícios (`E05-E01` a `E05-E05`)

### `E05-E01` *(Teste de Mesa — Transposição Retangular e Simetria)*
Sem usar computador, resolva:
1. Para a matriz `A` (`2 x 3`):
   `A = {{1, 2, 3}, {4, 5, 6}}`
   Informe as dimensões de `T = A^T` e os valores armazenados em `T[0][1]`, `T[1][0]`, `T[2][0]` e `T[2][1]`.
2. Para a matriz `M` (`3 x 3`):
   `M = {{5, -1, 4}, {-1, 0, 2}, {4, 3, 7}}`
   Rastreie os pares `(i, j)` com `j > i` (`(0, 1)`, `(0, 2)`, `(1, 2)`), indicando o resultado de cada comparação `M[i][j] != M[j][i]`, em qual par a flag `sim` vai a `0`, e por que não é necessário comparar os elementos da diagonal principal (`i == j`).

---

### `E05-E02` *(Completar solução)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` do trecho abaixo que constrói `T` (transposta de `A`, dimensões `L x C`) e verifica com flag universal se `A` é simétrica:

```c
for (int i = 0; i < L; i++) {
    for (int j = 0; j < C; j++) {
        /* A */ = A[i][j];
    }
}

int sim = 1;
if ( /* B */ ) {
    sim = 0;
} else {
    for (int i = 0; i < L; i++) {
        for (int j = /* C */ ; j < C; j++) {
            if ( /* D */ ) {
                sim = 0;
                break;
            }
        }
        if (!sim) {
            break;
        }
    }
}
```

---

### `E05-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler `L` e `C` (`1 <= L, C <= 20`), ler uma matriz `A` (`L x C`), construir sua transposta `T` (`C x L`), imprimir `Transposta (C x L):` seguida das `C` linhas de `T` e imprimir `Simetrica: Sim` ou `Simetrica: Nao`. Identifique os **3 bugs intencionais** e escreva a versão corrigida completa:

```c
#include <stdio.h>
#define MAX 20

int main(void) {
    int L, C, A[MAX][MAX], T[MAX][MAX];
    scanf("%d %d", &L, &C);
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            T[i][j] = A[j][i];
        }
    }

    int sim = 1;
    if (L != C) {
        sim = 0;
    } else {
        for (int i = 0; i < L; i++) {
            sim = 1;
            for (int j = i + 1; j < C; j++) {
                if (A[i][j] != A[j][i]) {
                    sim = 0;
                    break;
                }
            }
        }
    }

    printf("Transposta (%d x %d):\n", C, L);
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", T[i][j]);
        }
        printf("\n");
    }
    printf("Simetrica: %s\n", sim ? "Sim" : "Nao");
    return 0;
}
```

---

### `E05-E04` *(Variação controlada com pistas)*
Escreva um **programa completo** em C99 que leia `L` e `C` (`1 <= L, C <= 20`), leia os `L * C` inteiros da matriz `A` e em seguida os `L * C` inteiros da matriz `B`. Calcule a matriz soma `S = A + B` (`L x C`) e a transposta `T = S^T` (`C x L`). Imprima exatamente:
```text
Soma (L x C):
<L linhas com C elementos separados por espaco simples>
Transposta da soma (C x L):
<C linhas com L elementos separados por espaco simples>
```
*Pista:* Em um mesmo par de laços `for (int i = 0; i < L; i++)` / `for (int j = 0; j < C; j++)`, você já pode gravar `S[i][j] = A[i][j] + B[i][j];` e `T[j][i] = S[i][j];`.

---

### `E05-E05` *(Resolução independente)*
Escreva um **programa completo** em C99 que leia `N` (`1 <= N <= 20`) e uma matriz quadrada `A` (`N x N`).
1. Construa a matriz transposta `T = A^T` (`N x N`);
2. Calcule a matriz `S = A + T` (`N x N`);
3. Verifique com flag universal se `A` é simétrica e se `S` é simétrica.

Imprima exatamente:
```text
Simetrica A: Sim   (ou Nao)
Matriz A + A^T:
<N linhas com N elementos separados por espaco simples>
Simetrica A + A^T: Sim   (ou Nao)
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `E05-C01` *(Análise de Dimensões e Simetria)*
1. Considere uma matriz retangular declarada como `int A[3][4];`. Por que não é possível transpor `A` *in-place* (sobrescrevendo a própria `A`), e quais devem ser as dimensões declaradas para a matriz transposta `T`?
2. Quantas comparações `M[i][j] != M[j][i]` no máximo são necessárias para verificar se uma matriz `4 x 4` é simétrica testando apenas `j > i`?

### `E05-C02` *(Caça ao Bug — Programa completo)*
O programa abaixo deveria ler `L1, C1`, a matriz `A` (`L1 x C1`), depois `L2, C2` e a matriz `B` (`L2 x C2`). Se as dimensões forem incompatíveis, deve imprimir `Soma impossivel\n`; caso contrário, deve calcular `S = A + B` e imprimir `Soma:\n` seguido das linhas de `S`. Corrija todos os defeitos presentes:

```c
#include <stdio.h>
#define MAX 20

int main(void) {
    int L1, C1, L2, C2;
    int A[MAX][MAX], B[MAX][MAX], S[MAX][MAX];

    scanf("%d %d", &L1, &C1);
    for (int i = 0; i < L1; i++) {
        for (int j = 0; j < C1; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    scanf("%d %d", &L2, &C2);
    for (int i = 0; i < L2; i++) {
        for (int j = 0; j < C2; j++) {
            scanf("%d", &B[i][j]);
        }
    }

    if (L1 != L2 && C1 != C2) {
        printf("Soma impossivel\n");
    }
    for (int i = 0; i < L1; i++) {
        for (int j = 0; j < C1; j++) {
            S[i][j] = A[i][j] + B[j][i];
        }
    }
    printf("Soma:\n");
    for (int i = 0; i < L1; i++) {
        for (int j = 0; j < C1; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", S[i][j]);
        }
        printf("\n");
    }
    return 0;
}
```

### `E05-C03` *(Programa completo independente)*
Escreva um programa completo em C99 que leia `N` (`1 <= N <= 20`) e duas matrizes quadradas `A` (`N x N`) e `B` (`N x N`). Calcule `S = A + B`, construa `T = S^T` e verifique se `S` é simétrica. Imprima exatamente:
```text
Transposta de (A + B):
<N linhas com N elementos separados por espaco simples>
Simetrica (A + B): Sim   (ou Nao)
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `E06` (`Multiplicação de Matrizes — Triplo Laço Aninhado i, j, k`):** somente após autocorreção de `E05-E01..E05` e **100% (3/3)** em `E05-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** revisar a troca de dimensões `L x C` → `C x L` na construção e impressão de `T[j][i] = A[i][j]` e o posicionamento da flag `sim = 1` fora dos laços; aplicar variante `V2` de `E05`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`E03`** (laços por linha/coluna com limites distintos) e **`E04`** (verificação universal com flag e regiões `j > i`).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 8 — matrizes bidimensionais).
- `[DOC]` `Aula_15_Algoritmos.pdf` p. 16–19 (matriz transposta e simetria).
- `[DOC]` `Lista9_Algoritmos.pdf` p. 2 (Ex. 5 e Ex. 6b — transposta, soma e simetria).
- Casos de teste e soluções verificáveis: [E05_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/gabaritos/E05_gabarito.md) e [E05_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/E05_testes.md).
