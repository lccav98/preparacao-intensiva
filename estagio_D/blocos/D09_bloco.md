# Bloco `D09` — Linearização de Grades 2D em Vetor 1D (`i * C + j` e Macro `INDICE`)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio D — Vetores Unidimensionais e Strings / **`D09`** |
| **Micro-habilidade foco** | Mapear posições bidimensionais `(i, j)` de uma grade de `L` linhas e `C` colunas em um único vetor unidimensional usando o mapeamento por linhas `i * C + j` (e macro `INDICE(i, j)`). |
| **Pré-requisitos** | `D05` *(Laços aninhados em vetores 1D)*, `D07` *(Percurso manual de strings até `'\0'`)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão única de prática + checagem (22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **É TERMINANTEMENTE PROIBIDO usar matrizes 2D (`tipo m[L][C]`)** — matrizes 2D pertencem ao Estágio E! Também **não utilize** funções customizadas além de `int main(void)`, VLAs ou `gets`. Armazene toda grade `L × C` em um único vetor 1D (`L * C` ou `L * C + 1` para `char`) com saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Representação *row-major* em vetor 1D:** Uma grade de `L` linhas (`0..L-1`) e `C` colunas (`0..C-1`) possui `L * C` células que podem ser guardadas linha após linha em um **único vetor 1D**:
   - Para inteiros/reais: `int v[L * C];` (ou capacidade fixa `#define MAX ...`).
   - Para string linearizada de `char`: `char g[L * C + 1];` (reservando `+ 1` para o `'\0'` na posição `L * C`).
2. **Fórmula direta `(i, j) → idx`:**
   $$\text{idx} = i \cdot C + j$$
   Cada linha completa ocupa `C` posições contíguas; avançar `i` linhas salta `i * C` posições, e `+ j` seleciona a coluna dentro da linha `i`.
3. **Fórmula inversa `idx → (i, j)`:** Dado o índice linear `idx` (`0 <= idx < L * C`), recupera-se a coordenada original por divisão inteira e resto:
   $$i = \text{idx} / C \qquad j = \text{idx} \% C$$
4. **Macro `INDICE` com parênteses protetores:**
   ```c
   #define INDICE(i, j) ((i) * COLUNAS + (j))
   ```
   *(ou `#define INDICE(i, j, cols) ((i) * (cols) + (j))` quando `C` é lido em execução).*  
   **Armadilha crítica:** nunca omita parênteses em macros! Se definir `#define INDICE(i, j) i * COLUNAS + j`, a chamada `INDICE(1 + 1, 2)` expande para `1 + 1 * COLUNAS + 2` (calculando `1 * COLUNAS` primeiro, em vez de `2 * COLUNAS`)! Os parênteses externos `(...)` também protegem expressões como `2 * INDICE(i, j)`.

---

## 2. Exemplos Guiados

### Exemplo 1 — Tabela de mapeamento `3 × 4` (`COLUNAS = 4`) *(Rastreamento)*
| `(i, j)` | `idx = i * 4 + j` | Conversão inversa `(idx / 4, idx % 4)` |
|---|:---:|:---:|
| `(0, 0)` | `0` | `(0, 0)` |
| `(0, 3)` | `3` | `(0, 3)` |
| `(1, 0)` | `4` | `(1, 0)` |
| `(2, 1)` | `9` | `(9 / 4, 9 % 4) = (2, 1)` |
| `(2, 3)` | `11` | `(11 / 4, 11 % 4) = (2, 3)` |

- Veja o perigo sem parênteses: com `#define IND_BUG(i, j) i * 4 + j`, chamar `IND_BUG(2 - 1, 3)` gera `2 - 1 * 4 + 3 = 1`, quando o índice correto de `(1, 3)` é `((2 - 1) * 4 + (3)) = 7`.

### Exemplo 2 — Grade `3 × 4` em vetor 1D com macro `INDICE` *(Programa completo)*
```c
#include <stdio.h>
#define LINHAS 3
#define COLUNAS 4
#define INDICE(i, j) ((i) * COLUNAS + (j))

int main(void) {
    int v[LINHAS * COLUNAS];

    for (int i = 0; i < LINHAS; i++) {
        for (int j = 0; j < COLUNAS; j++) {
            scanf("%d", &v[INDICE(i, j)]);
        }
    }

    int li, co;
    scanf("%d %d", &li, &co);

    for (int i = 0; i < LINHAS; i++) {
        for (int j = 0; j < COLUNAS; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", v[INDICE(i, j)]);
        }
        printf("\n");
    }

    printf("Consulta: %d\n", v[INDICE(li - 1, co - 1)]);
    return 0;
}
```

---

## 3. Exercícios (`D09-E01` a `D09-E05`)

### Sessão Única (`D09-E01` a `D09-E05`)

### `D09-E01` *(Leitura e Teste de Mesa — Fórmulas Direta/Inversa e Macro)*
Para uma grade de `4` linhas e `5` colunas (`COLUNAS = 5`), sem usar computador:
1. Calcule o índice 1D `idx` correspondente às coordenadas `(2, 3)`, `(3, 0)` e `(0, 4)`.
2. Recupere as coordenadas `(i, j)` correspondentes aos índices lineares `idx = 14` e `idx = 7`.
3. Dada a macro defeituosa `#define IND(i, j) i * 5 + j`, mostre a expansão textual literal e o valor numérico produzido para `IND(1 + 1, 2 + 1)` e para `2 * IND(1, 2)`, comparando com os valores corretos.

---

### `D09-E02` *(Completar solução)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` do trecho abaixo que armazena uma grade `3 × 4` de caracteres em **um único vetor 1D** `grade`, lê as `3` linhas e imprime a linha `k` (`0 <= k < 3`):

```c
#define LINHAS 3
#define COLUNAS 4
#define INDICE(i, j) /* A */

char grade[LINHAS * COLUNAS + /* B */];
char buf[COLUNAS + 1];

for (int i = 0; i < LINHAS; i++) {
    scanf("%4s", buf);
    for (int j = 0; j < COLUNAS; j++) {
        grade[INDICE(i, j)] = /* C */;
    }
}
grade[LINHAS * COLUNAS] = /* D */;

int k;
scanf("%d", &k);
for (int j = 0; j < COLUNAS; j++) {
    printf("%c", grade[INDICE(k, j)]);
}
printf("\n");
```

---

### `D09-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler `3 × 4` inteiros em vetor 1D, imprimir a grade formatada e exibir o valor da coordenada **1-based** `(li, co)` (`1 <= li <= 3`, `1 <= co <= 4`). Identifique os **3 bugs intencionais** e escreva a versão corrigida completa:

```c
#include <stdio.h>
#define LINHAS 3
#define COLUNAS 4
#define INDICE(i, j) i * COLUNAS + j

int main(void) {
    int v[LINHAS + COLUNAS];

    for (int i = 0; i < LINHAS; i++) {
        for (int j = 0; j < COLUNAS; j++) {
            scanf("%d", &v[INDICE(i, j)]);
        }
    }

    int li, co;
    scanf("%d %d", &li, &co);

    for (int i = 0; i < LINHAS; i++) {
        for (int j = 0; j < COLUNAS; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", v[INDICE(j, i)]);
        }
        printf("\n");
    }

    printf("Consulta: %d\n", v[INDICE(li - 1, co - 1)]);
    return 0;
}
```

---

### `D09-E04` *(Variação controlada com pistas)*
Escreva um **programa completo** em C (proibidas matrizes 2D!) que leia `L` e `C` (`1 <= L <= 20`, `1 <= C <= 20`) e depois `L * C` inteiros para um único vetor 1D `int v[400]`. Usando `#define INDICE(i, j, cols) ((i) * (cols) + (j))`, calcule e imprima:
1. A soma de cada linha `i` (`0 .. L-1`) no formato `Linha i: S`;
2. O maior elemento (1ª ocorrência em ordem *row-major*) e suas coordenadas `(i, j)` no formato `Maior: X em (i, j)`.

*Pista:* Após achar o índice linear `idx_maior` em um laço `0 .. L*C - 1`, recupere `(idx_maior / c, idx_maior % c)`.

---

### `D09-E05` *(Resolução independente)*
Escreva um **programa completo** em C (proibidas matrizes 2D!) que leia `L` e `C` (`1 <= L <= 10`, `1 <= C <= 10`), seguidos de `L` linhas com `C` caracteres cada (sem espaços, lidas com `%10s` em um buffer de linha) e armazene **todos os caracteres em um único vetor 1D** `char grade[101]` finalizado com `'\0'` em `L * C`. Depois, leia `q` (`q >= 0`) consultas `(r, s)` base `0`: para cada consulta válida (`0 <= r < L` e `0 <= s < C`), imprima o caractere em `(r, s)`; caso contrário, imprima `Invalido`. Ao final, imprima `Linear: <grade>\n`.

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `D09-C01` *(Teste de Mesa)*
Para uma grade `3 × 6` (`COLUNAS = 6`), sem compilar:
1. Calcule `idx` para `(2, 5)` e `(1, 4)`.
2. Converta `idx = 11` e `idx = 13` para `(i, j)`.
3. Dada `#define POS(i, j) i * 6 + j`, calcule o valor errado obtido por `POS(1 + 1, 3)` e compare com o valor correto.

---

### `D09-C02` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler `3` linhas de `5` caracteres (sem espaços) para um vetor 1D `char g[...]`, ler `lin1` (`1..3`, base 1) e `col` (`0..4`, base 0), imprimir a célula `(lin1 - 1, col)`, imprimir os `3` caracteres da coluna `col` e a string linear completa `g`. Corrija todos os **3 defeitos** presentes (sem usar matriz 2D!):

```c
#include <stdio.h>
#define LINHAS 3
#define COLUNAS 5
#define INDICE(i, j) i * COLUNAS + j

int main(void) {
    char g[LINHAS * COLUNAS];
    char buf[COLUNAS + 1];

    for (int i = 0; i < LINHAS; i++) {
        scanf("%5s", buf);
        for (int j = 0; j < COLUNAS; j++) {
            g[INDICE(i, j)] = buf[j];
        }
    }

    int lin1, col;
    scanf("%d %d", &lin1, &col);

    printf("Celula: %c\n", g[INDICE(lin1 - 1, col)]);
    printf("Coluna:");
    for (int i = 0; i < LINHAS; i++) {
        printf(" %c", g[col * LINHAS + i]);
    }
    printf("\nLinear: %s\n", g);
    return 0;
}
```

---

### `D09-C03` *(Programa completo independente)*
Escreva um programa completo em C (proibidas matrizes 2D!) que leia `L` e `C` (`1 <= L <= 15`, `1 <= C <= 15`), leia `L * C` inteiros em um único vetor 1D `int v[225]`, e depois leia um inteiro `alvo`. Imprima:
1. A soma de cada coluna `j` (`0 .. C-1`) no formato `Coluna j: S`;
2. A quantidade total de ocorrências de `alvo` (`Ocorrencias: Q`);
3. As coordenadas `(i, j)` da **primeira ocorrência** de `alvo` em ordem *row-major* (`Primeira: (i, j)`), ou `Primeira: Nao encontrado` se `Q == 0`.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `D10` (`Revisão e Consolidação do Estágio D`):** somente após autocorreção de `D09-E01..E05` e **100% (3/3)** em `D09-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** refazer tabelas de conversão `(i, j) ↔ idx` com dimensões diferentes (`3 × 4`, `4 × 3`) e revisar a expansão textual de macros com e sem parênteses; aplicar variante `V2` de `D09`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`D05`** (laços aninhados sobre vetores 1D), **`D07`** (percurso de strings e terminador `'\0'`) e **`A05`** (macros `#define`).

---

## 6. Referências do Orientador
- `[DOC]` `Aula_14_Algoritmos.pdf` p. 4–6 (linearização *row-major* de grade 2D em vetor 1D).
- `[DOC]` `Lista7_Algoritmos.pdf` p. 3 (Ex. 6 — grade de caracteres em vetor único de `char`, proibidas matrizes).
- Casos de teste e soluções verificáveis: [D09_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/gabaritos/D09_gabarito.md) e [D09_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/D09_testes.md).
