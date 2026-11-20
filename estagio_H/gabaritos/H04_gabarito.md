# Gabarito Comentado — Bloco `H04` (Filtro de Mediana `3 x 3`)

> **Bloco de referência:** [H04_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/blocos/H04_bloco.md)  
> **Nota para Caça ao Bug:** `H04-E03` no bloco do aluno contém **3 erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`H04-E01` a `H04-E06`)

### `H04-E01` *(Teste de Mesa — Extração `3 x 3`, Ordenação e Matriz Auxiliar)*
- **(a)**
  - `v[9]` antes da ordenação: `{40, 42, 41, 39, 0, 44, 43, 40, 45}`
  - `v[9]` após `ordenar(v, 9)`: `{0, 39, 40, 40, 41, 42, 43, 44, 45}`
  - Valor atribuído ao pixel central (`v[4]`): **`41`** (o ruído pimenta `0` é eliminado).
- **(b)**
  - **Bordas preservadas (12 posições):** linha `0`, linha `3`, coluna `0` e coluna `3` mantêm os valores originais.
  - **Pixels internos calculados sobre a imagem original (`aux`):**
    - `(1, 1)`: `{90, 10, 12, 92, 0, 50, 94, 96, 255}` $\rightarrow$ `{0, 10, 12, 50, 90, 92, 94, 96, 255}` $\rightarrow$ `v[4] = 90`.
    - `(1, 2)`: `{10, 12, 14, 0, 50, 95, 96, 255, 98}` $\rightarrow$ `{0, 10, 12, 14, 50, 95, 96, 98, 255}` $\rightarrow$ `v[4] = 50`. *(Sem `aux`, `(1, 1)` já alterado para `90` entraria na janela e deslocaria a mediana de `(1, 2)` erroneamente para `90`!)*
    - `(2, 1)`: `{92, 0, 50, 94, 96, 255, 10, 12, 14}` $\rightarrow$ `{0, 10, 12, 14, 50, 92, 94, 96, 255}` $\rightarrow$ `v[4] = 50`.
    - `(2, 2)`: `{0, 50, 95, 96, 255, 98, 12, 14, 16}` $\rightarrow$ `{0, 12, 14, 16, 50, 95, 96, 98, 255}` $\rightarrow$ `v[4] = 50`.
  - **Matriz resultante `4 x 4`:**
    ```text
    90  10  12  14
    92  90  50  95
    94  50  50  98
    10  12  14  16
    ```

### `H04-E02` *(Completar Solução)*
- **`/* A */`:** `static`
- **`/* B */`:** `0`
- **`/* C */`:** `v[k] = img[i + a][j + b];`
- **`/* D */`:** `ordenar(v, 9);`
- **`/* E */`:** `v[4]`

### `H04-E03` *(Caça ao Bug em Projeto 5-Arquivos — Erros intencionais no enunciado)*
- **Erros intencionais em `funcoes.c`:**
  1. `int k = 0;` foi declarado fora dos laços `i` e `j`: a partir do 2º pixel interno, `k` passa a valer `9, 10, ...`, invadindo memória fora de `int v[9]`. Correção: declarar `int k = 0;` **dentro** do laço de `j`, antes dos laços `a` e `b`.
  2. Ausência da matriz auxiliar `static int aux[ALTURA][LARGURA];`: alterar `img[i][j]` diretamente contamina os vizinhos dos pixels seguintes. Correção: copiar `img` para `aux`, gravar `v[4]` em `aux[i][j]` e copiar `aux` para `img` ao final.
  3. Atribuição `img[i][j] = v[5];` usa o índice `5` (6º elemento) em vez de `v[4]` (5º elemento, mediana exata dos índices `0..8`).
- **Arquivos corrigidos:** [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H04_E03_corrigido/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H04_E03_corrigido/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H04_E03_corrigido/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H04_E03_corrigido/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H04_E03_corrigido/main.c)
- **Comando GCC:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/H04_E03_corrigido/main.c solucoes/H04_E03_corrigido/imagem.c solucoes/H04_E03_corrigido/funcoes.c -o prog
  ```

**`imagem.h`:**
```c
#ifndef IMAGEM_H
#define IMAGEM_H

#define ALTURA 5
#define LARGURA 5

int lerImagem(int img[ALTURA][LARGURA]);
void salvarImagem(const int img[ALTURA][LARGURA]);

#endif
```

**`imagem.c`:**
```c
#include <stdio.h>
#include "imagem.h"

int lerImagem(int img[ALTURA][LARGURA]) {
    char tipo[8];
    int largura, altura, maxval;

    if (scanf("%7s", tipo) != 1) {
        return 0;
    }
    if (tipo[0] != 'P' || tipo[1] != '2' || tipo[2] != '\0') {
        return 0;
    }
    if (scanf("%d %d %d", &largura, &altura, &maxval) != 3) {
        return 0;
    }
    if (largura != LARGURA || altura != ALTURA || maxval != 255) {
        return 0;
    }
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (scanf("%d", &img[i][j]) != 1) {
                return 0;
            }
            if (img[i][j] < 0 || img[i][j] > 255) {
                return 0;
            }
        }
    }
    return 1;
}

void salvarImagem(const int img[ALTURA][LARGURA]) {
    printf("P2\n%d %d\n255\n", LARGURA, ALTURA);
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", img[i][j]);
        }
        printf("\n");
    }
}
```

**`funcoes.h`:**
```c
#ifndef FUNCOES_H
#define FUNCOES_H

#include "imagem.h"

void ordenar(int v[], int n);
void aplicarMediana(int img[ALTURA][LARGURA]);

#endif
```

**`funcoes.c`:**
```c
#include "funcoes.h"

void ordenar(int v[], int n) {
    int i, j, temp;
    for (i = 0; i < n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (v[i] > v[j]) {
                temp = v[i];
                v[i] = v[j];
                v[j] = temp;
            }
        }
    }
}

void aplicarMediana(int img[ALTURA][LARGURA]) {
    // Bug 2 corrigido: usar matriz auxiliar static para preservar bordas e nao contaminar vizinhos
    static int aux[ALTURA][LARGURA];
    int v[9];

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            aux[i][j] = img[i][j];
        }
    }

    for (int i = 1; i < ALTURA - 1; i++) {
        for (int j = 1; j < LARGURA - 1; j++) {
            // Bug 1 corrigido: reiniciar k = 0 a cada pixel interno (i, j)
            int k = 0;
            for (int a = -1; a <= 1; a++) {
                for (int b = -1; b <= 1; b++) {
                    v[k] = img[i + a][j + b];
                    k++;
                }
            }
            ordenar(v, 9);
            // Bug 3 corrigido: a mediana de 9 elementos esta no indice 4 (nao 5) e e gravada em aux
            aux[i][j] = v[4];
        }
    }

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            img[i][j] = aux[i][j];
        }
    }
}
```

**`main.c`:**
```c
#include <stdio.h>
#include "imagem.h"
#include "funcoes.h"

int main(void) {
    static int img[ALTURA][LARGURA];
    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 1;
    }
    aplicarMediana(img);
    salvarImagem(img);
    return 0;
}
```

### `H04-E04` *(Projeto 5-Arquivos — Mediana `3 x 3` em `5 x 5`)*
Arquivos: [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H04_E04/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H04_E04/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H04_E04/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H04_E04/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H04_E04/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/H04_E04/main.c solucoes/H04_E04/imagem.c solucoes/H04_E04/funcoes.c -o prog
```
*(Os arquivos `imagem.h` e `imagem.c` são idênticos aos de `H04_E03_corrigido`.)*

**`funcoes.h`:**
```c
#ifndef FUNCOES_H
#define FUNCOES_H

#include "imagem.h"

void ordenar(int v[], int n);
void aplicarMediana(int img[ALTURA][LARGURA]);

#endif
```

**`funcoes.c`:**
```c
#include "funcoes.h"

void ordenar(int v[], int n) {
    int i, j, temp;
    for (i = 0; i < n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (v[i] > v[j]) {
                temp = v[i];
                v[i] = v[j];
                v[j] = temp;
            }
        }
    }
}

void aplicarMediana(int img[ALTURA][LARGURA]) {
    static int aux[ALTURA][LARGURA];
    int v[9];

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            aux[i][j] = img[i][j];
        }
    }

    for (int i = 1; i < ALTURA - 1; i++) {
        for (int j = 1; j < LARGURA - 1; j++) {
            int k = 0;
            for (int a = -1; a <= 1; a++) {
                for (int b = -1; b <= 1; b++) {
                    v[k] = img[i + a][j + b];
                    k++;
                }
            }
            ordenar(v, 9);
            aux[i][j] = v[4];
        }
    }

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            img[i][j] = aux[i][j];
        }
    }
}
```

**`main.c`:**
```c
#include <stdio.h>
#include "imagem.h"
#include "funcoes.h"

int main(void) {
    static int img[ALTURA][LARGURA];
    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 1;
    }
    aplicarMediana(img);
    salvarImagem(img);
    return 0;
}
```

### `H04-E05` *(Projeto 5-Arquivos — Aplicações Sucessivas da Mediana)*
Arquivos: [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H04_E05/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H04_E05/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H04_E05/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H04_E05/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H04_E05/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/H04_E05/main.c solucoes/H04_E05/imagem.c solucoes/H04_E05/funcoes.c -o prog
```
*(Os arquivos `imagem.h`, `imagem.c`, `funcoes.h` e `funcoes.c` são idênticos aos de `H04_E04`.)*

**`main.c`:**
```c
#include <stdio.h>
#include "imagem.h"
#include "funcoes.h"

int main(void) {
    static int img[ALTURA][LARGURA];
    int passos;

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 1;
    }
    scanf("%d", &passos);
    for (int p = 0; p < passos; p++) {
        aplicarMediana(img);
    }
    salvarImagem(img);
    return 0;
}
```

### `H04-E06` *(Projeto 5-Arquivos — Mediana + Contagem de Pixels Alterados)*
Arquivos: [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H04_E06/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H04_E06/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H04_E06/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H04_E06/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H04_E06/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/H04_E06/main.c solucoes/H04_E06/imagem.c solucoes/H04_E06/funcoes.c -o prog
```
*(Os arquivos `imagem.h` e `imagem.c` são idênticos aos de `H04_E04`.)*

**`funcoes.h`:**
```c
#ifndef FUNCOES_H
#define FUNCOES_H

#include "imagem.h"

void ordenar(int v[], int n);
void aplicarMediana(int img[ALTURA][LARGURA]);
void copiarImagem(const int orig[ALTURA][LARGURA], int dest[ALTURA][LARGURA]);
int contarAlterados(const int a[ALTURA][LARGURA], const int b[ALTURA][LARGURA]);

#endif
```

**`funcoes.c`:**
```c
#include "funcoes.h"

void ordenar(int v[], int n) {
    int i, j, temp;
    for (i = 0; i < n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (v[i] > v[j]) {
                temp = v[i];
                v[i] = v[j];
                v[j] = temp;
            }
        }
    }
}

void copiarImagem(const int orig[ALTURA][LARGURA], int dest[ALTURA][LARGURA]) {
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            dest[i][j] = orig[i][j];
        }
    }
}

void aplicarMediana(int img[ALTURA][LARGURA]) {
    static int aux[ALTURA][LARGURA];
    int v[9];

    copiarImagem(img, aux);

    for (int i = 1; i < ALTURA - 1; i++) {
        for (int j = 1; j < LARGURA - 1; j++) {
            int k = 0;
            for (int a = -1; a <= 1; a++) {
                for (int b = -1; b <= 1; b++) {
                    v[k] = img[i + a][j + b];
                    k++;
                }
            }
            ordenar(v, 9);
            aux[i][j] = v[4];
        }
    }

    copiarImagem(aux, img);
}

int contarAlterados(const int a[ALTURA][LARGURA], const int b[ALTURA][LARGURA]) {
    int cont = 0;
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (a[i][j] != b[i][j]) {
                cont++;
            }
        }
    }
    return cont;
}
```

**`main.c`:**
```c
#include <stdio.h>
#include "imagem.h"
#include "funcoes.h"

int main(void) {
    static int img[ALTURA][LARGURA];
    static int orig[ALTURA][LARGURA];

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 1;
    }
    copiarImagem(img, orig);
    aplicarMediana(img);
    salvarImagem(img);
    printf("Pixels alterados: %d\n", contarAlterados(orig, img));
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`H04-C01` a `H04-C03`)

### `H04-C01` *(Teste de Mesa sem Computador)*
1. - `v[9]` extraído: `{50, 52, 48, 51, 0, 49, 53, 50, 54}`
   - `v[9]` após `ordenar(v, 9)`: `{0, 48, 49, 50, 50, 51, 52, 53, 54}`
   - Mediana (`v[4]`): **`50`**.
2. Em uma matriz `4 x 4`:
   - Coordenadas internas atualizadas (4 pixels): **`(1, 1)`, `(1, 2)`, `(2, 1)`, `(2, 2)`**.
   - Pixels de borda preservados: **`12`** pixels (`4 * 4 - 4 = 12`).

### `H04-C02` *(Diagnóstico sem Compilar)*
1. **`k` não é reiniciado para cada pixel `(i, j)`:** `int k = 0;` está fora dos laços `i, j`, causando estouro do vetor `v[9]` a partir do 2º pixel interno. Deve estar **dentro** do laço de `j`.
2. **Mutação direta sem matriz auxiliar `aux`:** `img[i][j] = v[4];` sobrescreve o pixel original antes que os pixels seguintes leiam a vizinhança. Correção: usar `static int aux[ALTURA][LARGURA];`, copiar `img` para `aux` antes, gravar `aux[i][j] = v[4];` e copiar `aux` de volta para `img` ao término.

### `H04-C03` *(Projeto 5-Arquivos Independente — Mediana + Limiarização)*
Arquivos: [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H04_C03/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H04_C03/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H04_C03/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H04_C03/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H04_C03/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/H04_C03/main.c solucoes/H04_C03/imagem.c solucoes/H04_C03/funcoes.c -o prog
```
*(Os arquivos `imagem.h` e `imagem.c` são idênticos aos de `H04_E04`.)*

**`funcoes.h`:**
```c
#ifndef FUNCOES_H
#define FUNCOES_H

#include "imagem.h"

void ordenar(int v[], int n);
void aplicarMediana(int img[ALTURA][LARGURA]);
void limiarizar(int img[ALTURA][LARGURA], int limiar);

#endif
```

**`funcoes.c`:**
```c
#include "funcoes.h"

void ordenar(int v[], int n) {
    int i, j, temp;
    for (i = 0; i < n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (v[i] > v[j]) {
                temp = v[i];
                v[i] = v[j];
                v[j] = temp;
            }
        }
    }
}

void aplicarMediana(int img[ALTURA][LARGURA]) {
    static int aux[ALTURA][LARGURA];
    int v[9];

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            aux[i][j] = img[i][j];
        }
    }

    for (int i = 1; i < ALTURA - 1; i++) {
        for (int j = 1; j < LARGURA - 1; j++) {
            int k = 0;
            for (int a = -1; a <= 1; a++) {
                for (int b = -1; b <= 1; b++) {
                    v[k] = img[i + a][j + b];
                    k++;
                }
            }
            ordenar(v, 9);
            aux[i][j] = v[4];
        }
    }

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            img[i][j] = aux[i][j];
        }
    }
}

void limiarizar(int img[ALTURA][LARGURA], int limiar) {
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (img[i][j] < limiar) {
                img[i][j] = 0;
            } else {
                img[i][j] = 255;
            }
        }
    }
}
```

**`main.c`:**
```c
#include <stdio.h>
#include "imagem.h"
#include "funcoes.h"

int main(void) {
    static int img[ALTURA][LARGURA];
    int limiar;

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 1;
    }
    scanf("%d", &limiar);
    aplicarMediana(img);
    limiarizar(img, limiar);
    salvarImagem(img);
    return 0;
}
```
