# Bloco `E02` — Percurso Completo, Soma Total, Busca 2D e Extremos com Coordenadas `(i, j)`

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio E — Matrizes Bidimensionais e Processamento Matricial / **`E02`** |
| **Micro-habilidade foco** | Percorrer matrizes 2D com laços aninhados para calcular soma total, localizar a primeira ocorrência em busca 2D (interrompendo ambos os laços) e encontrar maior/menor valor com coordenadas `(li, co)`. |
| **Pré-requisitos** | `E01` *(Matrizes 2D: declaração, armazenamento row-major, acesso e leitura/escrita em grade)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão única de prática + checagem (22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Não utilize** funções customizadas além de `int main(void)`, VLAs (como `int m[l][c];`), `struct`, alocação dinâmica (`malloc`/`free`), somas individuais por linha/coluna (`E03`) ou diagonais (`E04`). Use `#define` para dimensões e saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Soma total e média em matriz:** inicialize `int soma = 0;` antes dos laços aninhados e acumule `soma += m[i][j];` para todo `(i, j)`. Para média real, use `(double)soma / (L * C)`.
2. **Extremos com coordenadas `(li, co)`:** **nunca** inicialize `maior` ou `menor` com `0` ou `999` (falha quando toda a matriz é negativa ou toda maior que `999`). Inicialize com o primeiro elemento:
   ```c
   int maior = m[0][0], li = 0, co = 0;
   ```
3. **Desempate em ordem *row-major*:**
   - Comparação **estrita** (`m[i][j] > maior` ou `m[i][j] < menor`) preserva a **1ª ocorrência** (menor linha `i`; em caso de empate na mesma linha, menor coluna `j`).
   - Comparação **inclusiva** (`>=` ou `<=`) guarda a **última ocorrência**.
4. **Busca 2D com saída de AMBOS os laços:** inicialize `int li = -1, co = -1;`. Ao encontrar `m[i][j] == alvo`, salve `li = i; co = j; break;`.
   - **Armadilha crítica:** o `break` interrompe **apenas o laço interno (`j`)**! Sem controle no laço externo (`i`), o programa continua testando as linhas seguintes e pode sobrescrever `(li, co)` com uma ocorrência posterior.
   - **Solução padrão:** combine `break;` no laço interno com **`&& li == -1`** na condição do laço externo: `for (int i = 0; i < L && li == -1; i++)`.

---

## 2. Exemplos Guiados

### Exemplo 1 — Por que `break` sozinho falha na busca 2D *(Teste de mesa)*
Considere `int m[3][3] = {{4, 7, 1}, {9, 7, 2}, {3, 5, 7}};` e `alvo = 7`:
- **Com `for (int i = 0; i < 3; i++)` (BUG — sem `&& li == -1`):**
  - `i = 0, j = 1`: acha `7` → `li = 0, co = 1`, `break` sai apenas do `for (j)`.
  - `i = 1, j = 1`: testa a linha 1, acha `7` → **sobrescreve** `li = 1, co = 1`!
  - `i = 2, j = 2`: acha `7` → **sobrescreve** `li = 2, co = 2`!
  - Resultado errado: `(2, 2)` (última ocorrência, com custo extra).
- **Com `for (int i = 0; i < 3 && li == -1; i++)` (CORRETO):**
  - `i = 0, j = 1`: acha `7` → `li = 0, co = 1`, `break` sai do `for (j)`.
  - Antes de `i = 1`: `li == -1` é **falso** (`0 == -1`), encerrando também o `for (i)`!
  - Resultado exato: `(0, 1)` (1ª ocorrência).

### Exemplo 2 — Soma total, maior com coordenadas e busca 2D *(Programa completo)*
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

    int alvo;
    scanf("%d", &alvo);

    int soma = 0;
    int maior = m[0][0], max_i = 0, max_j = 0;

    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            soma += m[i][j];
            if (m[i][j] > maior) {
                maior = m[i][j];
                max_i = i;
                max_j = j;
            }
        }
    }

    int pos_i = -1, pos_j = -1;
    for (int i = 0; i < L && pos_i == -1; i++) {
        for (int j = 0; j < C; j++) {
            if (m[i][j] == alvo) {
                pos_i = i;
                pos_j = j;
                break;
            }
        }
    }

    printf("Soma: %d\n", soma);
    printf("Maior: %d (%d, %d)\n", maior, max_i, max_j);
    if (pos_i != -1) {
        printf("Alvo: (%d, %d)\n", pos_i, pos_j);
    } else {
        printf("Alvo: nao encontrado\n");
    }

    return 0;
}
```

---

## 3. Exercícios (`E02-E01` a `E02-E05`)

### `E02-E01` *(Teste de Mesa — Desempate e Busca 2D)*
Considere a matriz `3 x 3`:
```c
int m[3][3] = {
    {-9, -4, -9},
    {-2, -7, -2},
    {-10, -2, -5}
};
```
Sem usar computador, responda:
1. Inicializando `maior = m[0][0]; li = 0; co = 0;`, quais serão os valores finais de `(maior, li, co)` usando `m[i][j] > maior` vs. usando `m[i][j] >= maior`?
2. Na busca por `alvo = -2`, indique quais linhas `i` são visitadas e qual `(pos_i, pos_j)` final é obtido:
   - `(a)` com `for (int i = 0; i < 3; i++)` e `break;` no interno;
   - `(b)` com `for (int i = 0; i < 3 && pos_i == -1; i++)` e `break;` no interno.

---

### `E02-E02` *(Completar solução)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` do trecho abaixo (com `int m[L][C]` já preenchida, `L = 3, C = 4`) para encontrar o **menor** valor (1ª ocorrência) com coordenadas `(li_min, co_min)` e localizar a **1ª ocorrência** de `alvo` parando ambos os laços:

```c
int menor = /* A */;
int li_min = 0, co_min = 0;

for (int i = 0; i < L; i++) {
    for (int j = 0; j < C; j++) {
        if ( /* B */ ) {
            menor = m[i][j];
            li_min = i;
            co_min = j;
        }
    }
}

int pos_i = -1, pos_j = -1;
for (int i = 0; /* C */ ; i++) {
    for (int j = 0; j < C; j++) {
        if (m[i][j] == alvo) {
            pos_i = i;
            pos_j = j;
            /* D */
        }
    }
}
```

---

### `E02-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler uma matriz `3 x 3` e um inteiro `alvo`, imprimindo `Soma: S`, `Maior: M (li, co)` (1ª ocorrência) e `Alvo: (ai, aj)` ou `Alvo: nao encontrado`. Identifique os **3 bugs intencionais** (no papel ou em comentários `//`) e escreva a versão corrigida completa:

```c
#include <stdio.h>
#define L 3
#define C 3

int main(void) {
    int m[L][C];
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    int alvo;
    scanf("%d", &alvo);

    int soma = 0;
    int maior = 0, li = 0, co = 0;
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            soma += m[i][j];
            if (m[i][j] >= maior) {
                maior = m[i][j];
                li = i;
                co = j;
            }
        }
    }

    int ai = -1, aj = -1;
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            if (m[i][j] == alvo) {
                ai = i;
                aj = j;
                break;
            }
        }
    }

    printf("Soma: %d\n", soma);
    printf("Maior: %d (%d, %d)\n", maior, li, co);
    if (ai != -1) {
        printf("Alvo: (%d, %d)\n", ai, aj);
    } else {
        printf("Alvo: nao encontrado\n");
    }

    return 0;
}
```

---

### `E02-E04` *(Variação controlada com pistas)*
Escreva um **programa completo** em C usando `#define L 3` e `#define C 4` que leia `12` inteiros para `m[L][C]`, calcule a média aritmética real da matriz e conte quantos elementos são **estritamente maiores** que a média, imprimindo exatamente:
```text
Media: X.XX
Acima da media: K
```
*Pista:* faça um primeiro percurso para calcular `soma` e `double media = (double)soma / (L * C);`, e depois um segundo percurso contando quando `m[i][j] > media`.

---

### `E02-E05` *(Resolução independente)*
Escreva um **programa completo** em C usando `#define L 4` e `#define C 5` que leia `20` inteiros para `m[L][C]` e imprima exatamente:
```text
Soma: S
Maior: M (li_max, co_max)
Menor: N (li_min, co_min)
```
preservando a **1ª ocorrência** em caso de empate tanto para o maior quanto para o menor elemento.

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `E02-C01` *(Rastreamento com Negativos e Análise de `break`)*
Dada a matriz `2 x 3`:
```c
int m[2][3] = {
    {-5, -1, -5},
    {-1, -8, -8}
};
```
Responda sem compilador:
1. Qual será a saída para `Maior` e `Menor` com suas coordenadas `(li, co)` usando desempate pela **1ª ocorrência** (`>` e `<`) vs. pela **última ocorrência** (`>=` e `<=`)?
2. Por que, ao buscar `alvo = -1` em uma matriz 2D, escrever `break;` apenas dentro do laço interno `j` falha na missão de localizar a 1ª ocorrência? Qual condição falta no laço externo `i`?

### `E02-C02` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler `l` e `c` (`1 <= l, c <= 10`), ler a matriz `l x c` e um inteiro `alvo`, imprimindo `Menor: M (li, co)` (1ª ocorrência) e `Posicao: (pi, pj)` ou `Posicao: nao encontrada`. Corrija todos os defeitos presentes:

```c
#include <stdio.h>
#define MAX 10

int main(void) {
    int l, c;
    scanf("%d %d", &l, &c);
    int m[l][c];

    for (int i = 0; i < l; i++) {
        for (int j = 0; j < c; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    int alvo;
    scanf("%d", &alvo);

    int menor = 999, li = 0, co = 0;
    for (int i = 0; i < l; i++) {
        for (int j = 0; j < c; j++) {
            if (m[i][j] < menor) {
                menor = m[i][j];
                li = i;
                co = j;
            }
        }
    }

    int pi = -1, pj = -1;
    for (int i = 0; i < l; i++) {
        for (int j = 0; j < c; j++) {
            if (m[i][j] == alvo) {
                pi = i;
                pj = j;
                break;
            }
        }
    }

    printf("Menor: %d (%d, %d)\n", menor, li, co);
    if (pi != -1) {
        printf("Posicao: (%d, %d)\n", pi, pj);
    } else {
        printf("Posicao: nao encontrada\n");
    }

    return 0;
}
```

### `E02-C03` *(Programa completo independente)*
Escreva um programa completo em C usando `#define MAX 10` que leia `l` e `c` (`1 <= l, c <= MAX`), os `l * c` inteiros da matriz `m[MAX][MAX]` e um valor `alvo`. Imprima exatamente:
```text
Soma: S
Maior: M (li, co)
Busca: (bi, bj)
```
*(ou `Busca: nao encontrado` caso `alvo` não exista na matriz)*, garantindo **1ª ocorrência** para `Maior` e para `Busca`.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `E03` (`Fatiamento e Acumuladores por Linha e por Coluna`):** somente após autocorreção de `E02-E01..E05` e **100% (3/3)** em `E02-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** revisar a inicialização obrigatória com `m[0][0]` em `(0, 0)`, o efeito do operador `>` vs. `>=` no desempate e a condição dupla `i < L && li == -1` para interromper o laço externo na busca 2D; aplicar variante `V2` de `E02`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`E01`** (percurso em matriz 2D), **`D02`** (busca de extremos sem sentinela fixa e média com *cast* `(double)`) e **`C07`** (alcance de `break` em laços aninhados).

---

## 6. Referências do Orientador
- `[DOC]` `Aula_14_Algoritmos.pdf` p. 19–20 (soma e percurso completo em matriz 2D).
- `[DOC]` `Aula_15_Algoritmos.pdf` p. 20, 25 (Ex. 3 — busca 2D com interrupção de laços aninhados).
- `[DOC]` `Lista9_Algoritmos.pdf` p. 1 (Ex. 3 — maior elemento e suas coordenadas).
- Casos de teste e soluções verificáveis: [E02_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/gabaritos/E02_gabarito.md) e [E02_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/E02_testes.md).
