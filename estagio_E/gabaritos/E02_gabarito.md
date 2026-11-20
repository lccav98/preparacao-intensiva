# Gabarito Comentado — Bloco `E02` (Percurso Completo, Soma Total, Busca 2D e Extremos)

> **Bloco de referência:** [E02_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/blocos/E02_bloco.md)  
> **Nota para Caça ao Bug:** `E02-E03` e `E02-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`E02-E01` a `E02-E05`)

### `E02-E01` *(Teste de Mesa — Desempate e Busca 2D)*
1. - Com `m[i][j] > maior`: atualiza em `(0, 1)` (`maior = -4`) e em `(1, 0)` (`maior = -2`). Em `(1, 2)` e `(2, 1)`, `-2 > -2` é falso. Resultado: **`maior = -2, li = 1, co = 0`** (1ª ocorrência).
   - Com `m[i][j] >= maior`: atualiza também em `(1, 2)` e `(2, 1)`. Resultado: **`maior = -2, li = 2, co = 1`** (última ocorrência).
2. - `(a)` Sem `&& pos_i == -1`: visita `i = 0`, `i = 1` (encontra `-2` em `(1, 0)` e dá `break` no `for (j)`), mas **continua** para `i = 2`, encontrando `-2` em `(2, 1)` e sobrescrevendo `(pos_i, pos_j) = (2, 1)`.
   - `(b)` Com `&& pos_i == -1`: visita `i = 0` e `i = 1`; ao encontrar `-2` em `(1, 0)`, faz `pos_i = 1; pos_j = 0; break;`. Na checagem para `i = 2`, `pos_i == -1` é falso e o laço externo encerra. Resultado: **`(1, 0)`**.

### `E02-E02` *(Completar solução)*
- **`/* A */`:** `m[0][0]`
- **`/* B */`:** `m[i][j] < menor`
- **`/* C */`:** `i < L && pos_i == -1`
- **`/* D */`:** `break;`

### `E02-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `int maior = 0;` falha quando todos os elementos da matriz são negativos (devolveria `0` em `(0, 0)` mesmo sem `0` na matriz). Correto: `int maior = m[0][0];`.
  2. `if (m[i][j] >= maior)` guarda a **última ocorrência** em caso de empate, em vez da **1ª ocorrência**. Correto: `if (m[i][j] > maior)`.
  3. `for (int i = 0; i < L; i++)` na busca 2D não interrompe o laço externo após `break;` no interno, podendo sobrescrever `(ai, aj)` com outra ocorrência de `alvo` em linha posterior. Correto: `for (int i = 0; i < L && ai == -1; i++)`.
- **Solução corrigida completa:** [E02_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E02_E03_corrigido.c)
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
    int maior = m[0][0], li = 0, co = 0;
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            soma += m[i][j];
            if (m[i][j] > maior) {
                maior = m[i][j];
                li = i;
                co = j;
            }
        }
    }

    int ai = -1, aj = -1;
    for (int i = 0; i < L && ai == -1; i++) {
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

### `E02-E04` *(Programa completo — Média e contagem acima da média)*
Arquivo: [E02_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E02_E04.c)
```c
#include <stdio.h>
#define L 3
#define C 4

int main(void) {
    int m[L][C];
    int soma = 0;

    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &m[i][j]);
            soma += m[i][j];
        }
    }

    double media = (double)soma / (L * C);
    int acima = 0;
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            if (m[i][j] > media) {
                acima++;
            }
        }
    }

    printf("Media: %.2f\n", media);
    printf("Acima da media: %d\n", acima);

    return 0;
}
```

### `E02-E05` *(Programa completo — Soma, maior e menor com coordenadas)*
Arquivo: [E02_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E02_E05.c)
```c
#include <stdio.h>
#define L 4
#define C 5

int main(void) {
    int m[L][C];
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    int soma = 0;
    int maior = m[0][0], li_max = 0, co_max = 0;
    int menor = m[0][0], li_min = 0, co_min = 0;

    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            soma += m[i][j];
            if (m[i][j] > maior) {
                maior = m[i][j];
                li_max = i;
                co_max = j;
            }
            if (m[i][j] < menor) {
                menor = m[i][j];
                li_min = i;
                co_min = j;
            }
        }
    }

    printf("Soma: %d\n", soma);
    printf("Maior: %d (%d, %d)\n", maior, li_max, co_max);
    printf("Menor: %d (%d, %d)\n", menor, li_min, co_min);

    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`E02-C01` a `E02-C03`)

### `E02-C01` *(Rastreamento com Negativos e Análise de `break`)*
1. - **1ª ocorrência (`>` / `<`):** `Maior = -1` em `(0, 1)`; `Menor = -8` em `(1, 1)`.
   - **Última ocorrência (`>=` / `<=`):** `Maior = -1` em `(1, 0)`; `Menor = -8` em `(1, 2)`.
2. O comando `break;` interrompe somente o laço mais interno (`j`). Ao terminar `i = 0` após encontrar `-1` em `(0, 1)`, o laço externo avança para `i = 1`, encontra `-1` em `(1, 0)` e sobrescreve a primeira posição encontrada. Falta a condição `&& pi == -1` no laço externo (`for (int i = 0; i < 2 && pi == -1; i++)`).

### `E02-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `int m[l][c];` declara VLA. Correto: `int m[MAX][MAX];`.
  2. `int menor = 999;` falha quando todos os valores da matriz são maiores ou iguais a `999`. Correto: `int menor = m[0][0];`.
  3. `for (int i = 0; i < l; i++)` na busca não encerra o laço externo ao achar a 1ª ocorrência. Correto: `for (int i = 0; i < l && pi == -1; i++)`.
- **Solução corrigida completa:** [E02_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E02_C02_corrigido.c)
```c
#include <stdio.h>
#define MAX 10

int main(void) {
    int l, c;
    int m[MAX][MAX];
    scanf("%d %d", &l, &c);

    for (int i = 0; i < l; i++) {
        for (int j = 0; j < c; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    int alvo;
    scanf("%d", &alvo);

    int menor = m[0][0], li = 0, co = 0;
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
    for (int i = 0; i < l && pi == -1; i++) {
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

### `E02-C03` *(Programa completo — Soma, maior e busca 2D em matriz `l x c`)*
Arquivo: [E02_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E02_C03.c)
```c
#include <stdio.h>
#define MAX 10

int main(void) {
    int l, c;
    int m[MAX][MAX];
    scanf("%d %d", &l, &c);

    for (int i = 0; i < l; i++) {
        for (int j = 0; j < c; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    int alvo;
    scanf("%d", &alvo);

    int soma = 0;
    int maior = m[0][0], li = 0, co = 0;
    for (int i = 0; i < l; i++) {
        for (int j = 0; j < c; j++) {
            soma += m[i][j];
            if (m[i][j] > maior) {
                maior = m[i][j];
                li = i;
                co = j;
            }
        }
    }

    int bi = -1, bj = -1;
    for (int i = 0; i < l && bi == -1; i++) {
        for (int j = 0; j < c; j++) {
            if (m[i][j] == alvo) {
                bi = i;
                bj = j;
                break;
            }
        }
    }

    printf("Soma: %d\n", soma);
    printf("Maior: %d (%d, %d)\n", maior, li, co);
    if (bi != -1) {
        printf("Busca: (%d, %d)\n", bi, bj);
    } else {
        printf("Busca: nao encontrado\n");
    }

    return 0;
}
```
