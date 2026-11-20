# Bloco `E06` — Multiplicação de Matrizes (Triplo Laço Aninhado `i, j, k`)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio E — Matrizes Bidimensionais e Processamento Matricial / **`E06`** |
| **Micro-habilidade foco** | Implementar o produto matricial $C_{L_A \times C_B} = A_{L_A \times K} \cdot B_{K \times C_B}$ coordenando três índices aninhados (`i`, `j`, `k`) e inicializando cada acumulador `C[i][j] = 0`. |
| **Pré-requisitos** | `E03` *(Fatiamento e Acumuladores por Linha e por Coluna)* e `E05` *(Transposição, Simetria e Soma de Matrizes)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 20 min):** `12 min` resol. \| `5 min` corr. \| `3 min` recup.; **Sessão 2 (`E04`–`E06`, 22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Não utilize** funções próprias além de `int main(void)`, VLAs (`int a[la][ca];`), `struct` ou alocação dinâmica (`malloc`/`free`). Use `#define MAX 20` e matrizes de capacidade fixa. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Compatibilidade dimensional (`CA == LB`):**
   - O produto matricial $C = A \cdot B$ de `A` (`LA x CA`) por `B` (`LB x CB`) **só existe** quando o número de colunas de `A` é igual ao número de linhas de `B` (**`CA == LB`**). Chamando esse eixo comum de $K = CA = LB$, a matriz resultante `C` terá dimensões **`LA x CB`**.
   - A multiplicação **não é comutativa**: $A \cdot B$ pode existir enquanto $B \cdot A$ é impossível, e mesmo quando ambos existem, em geral $A \cdot B \ne B \cdot A$.
2. **Definição de cada elemento (`C[i][j]`):**
   - Cada posição `(i, j)` de `C` é o produto escalar da **linha `i` de `A`** pela **coluna `j` de `B`**:
     $$C[i][j] = \sum_{k=0}^{K-1} A[i][k] \cdot B[k][j]$$
   - Note a posição de `k`: em `A[i][k]` ele percorre a **coluna** (horizontalmente); em `B[k][j]` ele percorre a **linha** (verticalmente).
3. **Arquitetura do triplo laço (`i`, `j`, `k`) e inicialização:**
   - Laço 1 (`i` de `0` a `LA - 1`): escolhe a linha de `C` (e de `A`).
   - Laço 2 (`j` de `0` a `CB - 1`): escolhe a coluna de `C` (e de `B`).
   - **Regra de ouro:** zere **`C[i][j] = 0;`** **dentro** do laço `j` e **antes** do laço `k`! Se esquecer de zerar (ou zerar fora), `C[i][j]` somará sobre lixo de memória.
   - Laço 3 (`k` de `0` a `CA - 1`): acumula `C[i][j] += A[i][k] * B[k][j];`.

---

## 2. Exemplos Guiados

### Exemplo 1 — Rastreamento de matrizes não quadradas `2 x 3` por `3 x 2` *(Trecho ilustrativo)*
Para $A_{2 \times 3} = \begin{pmatrix} 1 & 0 & -2 \\ 3 & 1 & 4 \end{pmatrix}$ e $B_{3 \times 2} = \begin{pmatrix} 2 & -1 \\ 0 & 3 \\ 1 & 2 \end{pmatrix}$:
- Compatibilidade: `CA = 3 == LB = 3` → resultado `C` tem dimensões **`2 x 2`**.
- Cálculo de `C[0][0]`: linha `0` de `A` (`1, 0, -2`) × coluna `0` de `B` (`2, 0, 1`):  
  `1*2 + 0*0 + (-2)*1 = 2 + 0 - 2 = 0`.
- Cálculo de `C[0][1]`: `1*(-1) + 0*3 + (-2)*2 = -1 + 0 - 4 = -5`.
- Cálculo de `C[1][0]`: `3*2 + 1*0 + 4*1 = 6 + 0 + 4 = 10`.
- Cálculo de `C[1][1]`: `3*(-1) + 1*3 + 4*2 = -3 + 3 + 8 = 8`.

### Exemplo 2 — Triplo laço completo em C99 *(Programa completo)*
```c
#include <stdio.h>
#define MAX 20

int main(void) {
    int LA, CA, LB, CB;
    int A[MAX][MAX], B[MAX][MAX], C[MAX][MAX];

    scanf("%d %d", &LA, &CA);
    for (int i = 0; i < LA; i++) {
        for (int j = 0; j < CA; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    scanf("%d %d", &LB, &CB);
    for (int i = 0; i < LB; i++) {
        for (int j = 0; j < CB; j++) {
            scanf("%d", &B[i][j]);
        }
    }

    if (CA != LB) {
        printf("Multiplicacao impossivel\n");
    } else {
        for (int i = 0; i < LA; i++) {
            for (int j = 0; j < CB; j++) {
                C[i][j] = 0;
                for (int k = 0; k < CA; k++) {
                    C[i][j] += A[i][k] * B[k][j];
                }
            }
        }
        printf("Produto (%d x %d):\n", LA, CB);
        for (int i = 0; i < LA; i++) {
            for (int j = 0; j < CB; j++) {
                if (j > 0) {
                    printf(" ");
                }
                printf("%d", C[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
```

---

## 3. Exercícios (`E06-E01` a `E06-E06`)

### Sessão 1 (`E06-E01` a `E06-E03` — Rastreamento, Lacunas e Depuração)

### `E06-E01` *(Teste de Mesa — Produto Não Quadrado)*
Sem usar computador, dadas as matrizes *(baseadas na Lista 9 Ex. 7)*:
$$A_{2 \times 3} = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}, \qquad B_{3 \times 2} = \begin{pmatrix} 7 & 8 \\ 9 & 10 \\ 11 & 12 \end{pmatrix}$$
1. Informe as dimensões da matriz resultante $C = A \cdot B$.
2. Calcule manualmente `C[0][0]`, `C[0][1]`, `C[1][0]` e `C[1][1]`, mostrando os 3 produtos somados em cada elemento.
3. Verifique se o produto inverso $B \cdot A$ também é possível e, em caso positivo, informe suas dimensões.

---

### `E06-E02` *(Completar solução)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` para multiplicar `A` (`LA x CA`) por `B` (`LB x CB`), sabendo que já foi verificado `CA == LB`:

```c
for (int i = 0; i < LA; i++) {
    for (int j = 0; /* A */ ; j++) {
        /* B */ ;
        for (int k = 0; /* C */ ; k++) {
            C[i][j] += /* D */ ;
        }
    }
}
```

---

### `E06-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler `LA, CA`, a matriz `A`, depois `LB, CB` e a matriz `B` (`1 <= LA, CA, LB, CB <= 20`). Se `CA != LB`, deve imprimir `Multiplicacao impossivel\n`; senão, calcular `C = A * B` e imprimir `Produto (LA x CB):\n` e as linhas de `C`. Identifique os **3 bugs intencionais** e escreva a versão corrigida completa:

```c
#include <stdio.h>
#define MAX 20

int main(void) {
    int LA, CA, LB, CB;
    int A[MAX][MAX], B[MAX][MAX], C[MAX][MAX];

    scanf("%d %d", &LA, &CA);
    for (int i = 0; i < LA; i++) {
        for (int j = 0; j < CA; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    scanf("%d %d", &LB, &CB);
    for (int i = 0; i < LB; i++) {
        for (int j = 0; j < CB; j++) {
            scanf("%d", &B[i][j]);
        }
    }

    if (LA != LB) {
        printf("Multiplicacao impossivel\n");
    } else {
        for (int i = 0; i < LA; i++) {
            for (int j = 0; j < CB; j++) {
                for (int k = 0; k < CA; k++) {
                    C[i][j] += A[i][k] * B[j][k];
                }
            }
        }
        printf("Produto (%d x %d):\n", LA, CB);
        for (int i = 0; i < LA; i++) {
            for (int j = 0; j < CB; j++) {
                if (j > 0) {
                    printf(" ");
                }
                printf("%d", C[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
```

---

### Sessão 2 (`E06-E04` a `E06-E06` — Escrita Guiada → Independente)

### `E06-E04` *(Variação controlada com pistas)*
Escreva um **programa completo** em C99 que leia `LA, CA`, a matriz `A` (`LA x CA`), depois `LB, CB` e a matriz `B` (`LB x CB`), garantindo-se `CA == LB` (`1 <= LA, CA, LB, CB <= 20`). Calcule `C = A * B`, imprima a matriz `C` e localize o **maior elemento** de `C` e suas coordenadas `(li, co)` (**1ª ocorrência** em ordem *row-major*). Imprima exatamente:
```text
Produto (LA x CB):
<LA linhas com CB elementos separados por espaco simples>
Maior: V em (li, co)
```
*Pista:* Após preencher `C`, inicialize `maior = C[0][0]; li = 0; co = 0;` e use comparação estrita `C[i][j] > maior`.

---

### `E06-E05` *(Variação controlada com pistas)*
Escreva um **programa completo** em C99 *(inspirado na Lista 9 Ex. 7)* que leia `LA, CA`, `A`, `LB, CB` e `B` (`1 <= LA, CA, LB, CB <= 20`).
1. Se `CA == LB`, calcule e imprima `A*B (LA x CB):` seguido das linhas do produto; caso contrário, imprima `Produto A*B impossivel`.
2. Independentemente do item 1, verifique se $B \cdot A$ existe (`CB == LA`): se sim, calcule e imprima `B*A (LB x CA):` seguido das linhas do produto; caso contrário, imprima `Produto B*A impossivel`.

*Pista:* Use uma quarta matriz `D[MAX][MAX]` para `B * A` e lembre-se de inverter os limites dos três laços (`i < LB`, `j < CA`, `k < CB`) com `B[i][k] * A[k][j]`.

---

### `E06-E06` *(Resolução independente)*
Escreva um **programa completo** em C99 que leia `N` (`1 <= N <= 20`) e uma matriz quadrada `A` (`N x N`). Calcule a matriz $P = A^2 = A \cdot A$ usando o triplo laço (em matriz separada `P[MAX][MAX]`, nunca sobrescrevendo `A` durante o cálculo!) e o traço de `P` (soma da diagonal principal de `P`). Imprima exatamente:
```text
A^2:
<N linhas com N elementos separados por espaco simples>
Traco de A^2: T
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `E06-C01` *(Rastreamento Manual e Compatibilidade)*
Dadas $A_{2 \times 3} = \begin{pmatrix} 2 & -1 & 0 \\ 3 & 1 & -2 \end{pmatrix}$ e $B_{3 \times 2} = \begin{pmatrix} 1 & 4 \\ 0 & -3 \\ 5 & 2 \end{pmatrix}$:
1. Calcule manualmente `C[1][0]` no produto $C = A \cdot B$, mostrando os três produtos e a soma final.
2. Quais são as dimensões da matriz resultante `C`?
3. Se `A` fosse `2 x 4` e `B` fosse `3 x 2`, por que `A * B` seria inválido?

### `E06-C02` *(Caça ao Bug — Programa completo)*
O programa abaixo deveria ler `LA, CA`, `A`, `LB, CB`, `B` (com `CA == LB`), calcular `C = A * B` e imprimir `Resultado (LA x CB):` seguido das linhas de `C`. Corrija todos os defeitos presentes:

```c
#include <stdio.h>
#define MAX 20

int main(void) {
    int LA, CA, LB, CB;
    int A[MAX][MAX], B[MAX][MAX], C[MAX][MAX];

    scanf("%d %d", &LA, &CA);
    for (int i = 0; i < LA; i++) {
        for (int j = 0; j < CA; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    scanf("%d %d", &LB, &CB);
    for (int i = 0; i < LB; i++) {
        for (int j = 0; j < CB; j++) {
            scanf("%d", &B[i][j]);
        }
    }

    for (int i = 0; i < LA; i++) {
        for (int j = 0; j < CA; j++) {
            for (int k = 0; k < LA; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    printf("Resultado (%d x %d):\n", LA, CB);
    for (int i = 0; i < LA; i++) {
        for (int j = 0; j < CB; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", C[i][j]);
        }
        printf("\n");
    }
    return 0;
}
```

### `E06-C03` *(Programa completo independente)*
Escreva um programa completo em C99 que leia `L` e `C` (`1 <= L, C <= 20`) e uma matriz retangular `A` (`L x C`). Construa sua transposta `T = A^T` (`C x L`) e calcule o produto matricial `G = A * T` (dimensões `L x L`). Imprima exatamente:
```text
A * A^T (L x L):
<L linhas com L elementos separados por espaco simples>
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `E07` (`Matrizes como Imagens em Tons de Cinza PGM P2, Saturação [0, 255], static e Generalização n-Dimensional`):** somente após autocorreção de `E06-E01..E06` e **100% (3/3)** em `E06-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** refazer rastreamento manual de `2 x 3` por `3 x 2` associando cada variável de laço ao seu eixo (`i -> LA`, `j -> CB`, `k -> CA == LB`) e conferindo `C[i][j] = 0;` antes do laço `k`; aplicar variante `V2` de `E06`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`E03`** (acumuladores por linha/coluna com limites distintos) e **`E05`** (gerenciamento de dimensões assimétricas `L x C` em múltiplas matrizes).

---

## 6. Referências do Orientador
- `[DOC]` `Aula_01_Algoritmos.pdf` p. 12–13 (motivação matricial).
- `[DOC]` `Lista9_Algoritmos.pdf` p. 2 (Ex. 7 — multiplicação de matrizes, marcado **Entregar**).
- Casos de teste e soluções verificáveis: [E06_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/gabaritos/E06_gabarito.md) e [E06_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/E06_testes.md).
