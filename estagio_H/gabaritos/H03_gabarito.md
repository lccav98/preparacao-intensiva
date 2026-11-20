# Gabarito Comentado — Bloco `H03` (Matriz Auxiliar, Bordas e Blur $t \times t$)

> **Bloco de referência:** [H03_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/blocos/H03_bloco.md)  
> **Nota para Caça ao Bug:** `H03-E03` e `H03-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`H03-E01` a `H03-E06`)

### `H03-E01` *(Teste de Mesa `5 x 5` — Com vs. Sem Matriz Auxiliar e Bordas)*
1. **Para `t = 3` (`r = 1`):**
   - **Pixel `(1, 1)` com `aux`:** vizinhança `3 x 3` possui sete `90` e dois `0` → soma `630` → `630 / 9 = 70`.
   - **Pixel `(1, 2)` com `aux`:** lê todos os valores originais (seis `90` e três `0`) → soma `540` → `540 / 9 = 60`.
   - **Pixel `(1, 2)` sem `aux` (erro):** reutiliza `img[1][1] = 70` no lugar de `90` → soma `5 * 90 + 70 = 520` → `520 / 9 = 57` (divisão inteira).
2. **Matriz `5 x 5` resultante de `aplicarBlur(img, 3)`:**
   ```text
   90  90  90  90  90
   90  70  60  70  90
   90  60  50  60  90
   90  70  60  70  90
   90  90  90  90  90
   ```
   *(A primeira e a última linha e coluna permanecem intactas com `90`.)*
3. **Para `t = 5` (`r = 2`) sobre a matriz original:**
   - Faixa interna: `2 <= i < 3` e `2 <= j < 3` → apenas **1 pixel** interno: **`(2, 2)`** (os outros `24` pixels são bordas preservadas).
   - Soma dos `25` pixels (`21 * 90 + 4 * 0 = 1890`) → `1890 / 25 = 75` (divisão inteira). O pixel `(2, 2)` passa de `90` para **`75`**.

---

### `H03-E02` *(Completar Lacunas — `aplicarBlur`)*
- **`/* A */`:** `static`
- **`/* B */`:** `t / 2`
- **`/* C */`:** `ALTURA - r`
- **`/* D */`:** `aux[i + a][j + b]`
- **`/* E */`:** `soma / (t * t)`

---

### `H03-E03` *(Caça ao Bug Multi-Arquivo — `aplicarBlur` `5 x 5`)*
- **Erros intencionais:**
  1. `funcoes.h` omite o parâmetro `int t` (`void aplicarBlur(int img[ALTURA][LARGURA]);`), causando `conflicting types` frente a `funcoes.c`.
  2. `funcoes.c` usa `i <= ALTURA - r` em vez de `i < ALTURA - r`, invadindo a borda inferior (e acessando fora da matriz em `i + a`).
  3. `funcoes.c` acumula `img[i + a][j + b]` em vez de `aux[i + a][j + b]`, reutilizando pixels já alterados.
  4. `funcoes.c` divide por `t` (`soma / t`) em vez de `t * t` (`soma / (t * t)`).
- **Solução corrigida em 5 arquivos:** [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_E03_corrigido/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_E03_corrigido/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_E03_corrigido/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_E03_corrigido/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_E03_corrigido/main.c)
- **Comando GCC:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/H03_E03_corrigido/main.c solucoes/H03_E03_corrigido/imagem.c solucoes/H03_E03_corrigido/funcoes.c -o processador
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
    char tipo[4];
    int larg, alt, maxval;
    if (scanf("%3s %d %d %d", tipo, &larg, &alt, &maxval) != 4) {
        return 0;
    }
    if (tipo[0] != 'P' || tipo[1] != '2' || tipo[2] != '\0') {
        return 0;
    }
    if (larg != LARGURA || alt != ALTURA || maxval != 255) {
        return 0;
    }
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (scanf("%d", &img[i][j]) != 1) {
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

// Correcao: adicionar o parametro int t conforme Trabalho_Algoritmos.pdf
void aplicarBlur(int img[ALTURA][LARGURA], int t);

#endif
```

**`funcoes.c`:**
```c
#include "funcoes.h"

void aplicarBlur(int img[ALTURA][LARGURA], int t) {
    static int aux[ALTURA][LARGURA];
    int r = t / 2;

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            aux[i][j] = img[i][j];
        }
    }

    // Correcao: usar i < ALTURA - r (nao <=) para preservar a borda inferior
    for (int i = r; i < ALTURA - r; i++) {
        for (int j = r; j < LARGURA - r; j++) {
            int soma = 0;
            for (int a = -r; a <= r; a++) {
                for (int b = -r; b <= r; b++) {
                    // Correcao: ler de aux (nao de img) para nao reutilizar pixels alterados
                    soma += aux[i + a][j + b];
                }
            }
            // Correcao: dividir por (t * t), total de pixels da janela t x t
            img[i][j] = soma / (t * t);
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
    int t;

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 0;
    }
    scanf("%d", &t);
    if (t != 3 && t != 5 && t != 7) {
        printf("Tamanho t invalido.\n");
        return 0;
    }
    aplicarBlur(img, t);
    salvarImagem(img);
    return 0;
}
```

---

### `H03-E04` *(Projeto 5-Arquivos — Blur `3 x 3` em `5 x 5`)*
Arquivos: [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_E04/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_E04/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_E04/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_E04/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_E04/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/H03_E04/main.c solucoes/H03_E04/imagem.c solucoes/H03_E04/funcoes.c -o processador
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
    char tipo[4];
    int larg, alt, maxval;
    if (scanf("%3s %d %d %d", tipo, &larg, &alt, &maxval) != 4) {
        return 0;
    }
    if (tipo[0] != 'P' || tipo[1] != '2' || tipo[2] != '\0') {
        return 0;
    }
    if (larg != LARGURA || alt != ALTURA || maxval != 255) {
        return 0;
    }
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (scanf("%d", &img[i][j]) != 1) {
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

void aplicarBlur(int img[ALTURA][LARGURA], int t);

#endif
```

**`funcoes.c`:**
```c
#include "funcoes.h"

void aplicarBlur(int img[ALTURA][LARGURA], int t) {
    static int aux[ALTURA][LARGURA];
    int r = t / 2;

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            aux[i][j] = img[i][j];
        }
    }

    for (int i = r; i < ALTURA - r; i++) {
        for (int j = r; j < LARGURA - r; j++) {
            int soma = 0;
            for (int a = -r; a <= r; a++) {
                for (int b = -r; b <= r; b++) {
                    soma += aux[i + a][j + b];
                }
            }
            img[i][j] = soma / (t * t);
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
        return 0;
    }
    aplicarBlur(img, 3);
    salvarImagem(img);
    return 0;
}
```

---

### `H03-E05` *(Projeto 5-Arquivos — Blur Parametrizável `t` em `{3, 5, 7}` sobre `7 x 7`)*
Arquivos: [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_E05/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_E05/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_E05/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_E05/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_E05/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/H03_E05/main.c solucoes/H03_E05/imagem.c solucoes/H03_E05/funcoes.c -o processador
```

**`imagem.h`:**
```c
#ifndef IMAGEM_H
#define IMAGEM_H

#define ALTURA 7
#define LARGURA 7

int lerImagem(int img[ALTURA][LARGURA]);
void salvarImagem(const int img[ALTURA][LARGURA]);

#endif
```

**`imagem.c`:**
```c
#include <stdio.h>
#include "imagem.h"

int lerImagem(int img[ALTURA][LARGURA]) {
    char tipo[4];
    int larg, alt, maxval;
    if (scanf("%3s %d %d %d", tipo, &larg, &alt, &maxval) != 4) {
        return 0;
    }
    if (tipo[0] != 'P' || tipo[1] != '2' || tipo[2] != '\0') {
        return 0;
    }
    if (larg != LARGURA || alt != ALTURA || maxval != 255) {
        return 0;
    }
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (scanf("%d", &img[i][j]) != 1) {
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

void aplicarBlur(int img[ALTURA][LARGURA], int t);

#endif
```

**`funcoes.c`:**
```c
#include "funcoes.h"

void aplicarBlur(int img[ALTURA][LARGURA], int t) {
    static int aux[ALTURA][LARGURA];
    int r = t / 2;

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            aux[i][j] = img[i][j];
        }
    }

    for (int i = r; i < ALTURA - r; i++) {
        for (int j = r; j < LARGURA - r; j++) {
            int soma = 0;
            for (int a = -r; a <= r; a++) {
                for (int b = -r; b <= r; b++) {
                    soma += aux[i + a][j + b];
                }
            }
            img[i][j] = soma / (t * t);
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
    int t;

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 0;
    }
    scanf("%d", &t);
    if (t != 3 && t != 5 && t != 7) {
        printf("Tamanho t invalido.\n");
        return 0;
    }
    aplicarBlur(img, t);
    salvarImagem(img);
    return 0;
}
```

---

### `H03-E06` *(Projeto 5-Arquivos — Blur + Brilho Encadeados em `7 x 7`)*
Arquivos: [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_E06/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_E06/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_E06/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_E06/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_E06/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/H03_E06/main.c solucoes/H03_E06/imagem.c solucoes/H03_E06/funcoes.c -o processador
```

**`imagem.h`:**
```c
#ifndef IMAGEM_H
#define IMAGEM_H

#define ALTURA 7
#define LARGURA 7

int lerImagem(int img[ALTURA][LARGURA]);
void salvarImagem(const int img[ALTURA][LARGURA]);

#endif
```

**`imagem.c`:**
```c
#include <stdio.h>
#include "imagem.h"

int lerImagem(int img[ALTURA][LARGURA]) {
    char tipo[4];
    int larg, alt, maxval;
    if (scanf("%3s %d %d %d", tipo, &larg, &alt, &maxval) != 4) {
        return 0;
    }
    if (tipo[0] != 'P' || tipo[1] != '2' || tipo[2] != '\0') {
        return 0;
    }
    if (larg != LARGURA || alt != ALTURA || maxval != 255) {
        return 0;
    }
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (scanf("%d", &img[i][j]) != 1) {
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

void ajustarBrilho(int img[ALTURA][LARGURA], int b);
void aplicarBlur(int img[ALTURA][LARGURA], int t);

#endif
```

**`funcoes.c`:**
```c
#include "funcoes.h"

void ajustarBrilho(int img[ALTURA][LARGURA], int b) {
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            img[i][j] += b;
            if (img[i][j] < 0) {
                img[i][j] = 0;
            } else if (img[i][j] > 255) {
                img[i][j] = 255;
            }
        }
    }
}

void aplicarBlur(int img[ALTURA][LARGURA], int t) {
    static int aux[ALTURA][LARGURA];
    int r = t / 2;

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            aux[i][j] = img[i][j];
        }
    }

    for (int i = r; i < ALTURA - r; i++) {
        for (int j = r; j < LARGURA - r; j++) {
            int soma = 0;
            for (int a = -r; a <= r; a++) {
                for (int b = -r; b <= r; b++) {
                    soma += aux[i + a][j + b];
                }
            }
            img[i][j] = soma / (t * t);
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
    int b, t;

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 0;
    }
    scanf("%d %d", &b, &t);
    if (t != 3 && t != 5 && t != 7) {
        printf("Tamanho t invalido.\n");
        return 0;
    }
    aplicarBlur(img, t);
    ajustarBrilho(img, b);
    salvarImagem(img);
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`H03-C01` a `H03-C03`)

### `H03-C01` *(Teste de Mesa `t = 5` e Diferença Com vs. Sem Matriz Auxiliar)*
1. **Matriz `6 x 6` com `t = 5` (`r = 2`):**
   - Pixels internos: `2 <= i < 4` e `2 <= j < 4` → `2 * 2 = 4` pixels recalculados (`(2,2), (2,3), (3,2), (3,3)`) e `36 - 4 = 32` pixels preservados nas bordas.
   - **Pixel `(2, 2)`** (janela linhas `0..4`, colunas `0..4`): contém `img[2][2] = 0`, `img[2][3] = 125` e `23` pixels `100` (não inclui `img[3][5] = 50`). Soma = `23 * 100 + 0 + 125 = 2425` → `2425 / 25 = 97`.
   - **Pixel `(2, 3)`** (janela linhas `0..4`, colunas `1..5`): contém `img[2][2] = 0`, `img[2][3] = 125`, `img[3][5] = 50` e `22` pixels `100`. Soma = `22 * 100 + 0 + 125 + 50 = 2375` → `2375 / 25 = 95`.
2. **Matriz `4 x 4` (`t = 3`, `r = 1`):**
   - **Com `aux`:** `(1, 1)` vira `(8 * 10 + 90) / 9 = 170 / 9 = 18`; ao calcular `(1, 2)`, `aux[1][1]` ainda vale `90`, então `(1, 2)` também resulta em `170 / 9 = 18`.
   - **Sem `aux`:** `(1, 2)` lê `img[1][1] = 18` já modificado, somando `8 * 10 + 18 = 98` → `98 / 9 = 10` (valor incorreto).

---

### `H03-C02` *(Caça ao Bug — Soma Acumulada, Janela Incompleta e Borda Destruída)*
- **Erros intencionais em `funcoes.c`:**
  1. `int soma = 0;` está fora dos laços `i, j`, acumulando somas de pixels anteriores em vez de zerar para cada pixel.
  2. Os laços da vizinhança começam em `a = 0` e `b = 0` em vez de `-r` a `+r`, somando apenas o quadrante inferior direito em vez dos `t * t` pixels.
  3. Escreve em `aux[i][j]` sem ter copiado `img` para `aux` antes, e depois sobrescreve toda `img` com `aux`, zerando todas as bordas (ou deixando lixo de chamadas anteriores).
- **Solução corrigida em 5 arquivos:** [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_C02_corrigido/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_C02_corrigido/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_C02_corrigido/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_C02_corrigido/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_C02_corrigido/main.c)

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
    char tipo[4];
    int larg, alt, maxval;
    if (scanf("%3s %d %d %d", tipo, &larg, &alt, &maxval) != 4) {
        return 0;
    }
    if (tipo[0] != 'P' || tipo[1] != '2' || tipo[2] != '\0') {
        return 0;
    }
    if (larg != LARGURA || alt != ALTURA || maxval != 255) {
        return 0;
    }
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (scanf("%d", &img[i][j]) != 1) {
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

void aplicarBlur(int img[ALTURA][LARGURA], int t);

#endif
```

**`funcoes.c`:**
```c
#include "funcoes.h"

void aplicarBlur(int img[ALTURA][LARGURA], int t) {
    static int aux[ALTURA][LARGURA];
    int r = t / 2;

    // Correcao: copiar img para aux antes de calcular para preservar as bordas
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            aux[i][j] = img[i][j];
        }
    }

    for (int i = r; i < ALTURA - r; i++) {
        for (int j = r; j < LARGURA - r; j++) {
            // Correcao: zerar soma dentro dos lacos i, j para cada pixel
            int soma = 0;
            // Correcao: percorrer janela completa de -r ate +r
            for (int a = -r; a <= r; a++) {
                for (int b = -r; b <= r; b++) {
                    soma += aux[i + a][j + b];
                }
            }
            img[i][j] = soma / (t * t);
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
    int t;

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 0;
    }
    scanf("%d", &t);
    if (t != 3 && t != 5 && t != 7) {
        printf("Tamanho t invalido.\n");
        return 0;
    }
    aplicarBlur(img, t);
    salvarImagem(img);
    return 0;
}
```

---

### `H03-C03` *(Projeto 5-Arquivos Independente — `aplicarBlur` em `7 x 7`)*
Arquivos: [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_C03/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_C03/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_C03/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_C03/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H03_C03/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/H03_C03/main.c solucoes/H03_C03/imagem.c solucoes/H03_C03/funcoes.c -o processador
```

**`imagem.h`:**
```c
#ifndef IMAGEM_H
#define IMAGEM_H

#define ALTURA 7
#define LARGURA 7

int lerImagem(int img[ALTURA][LARGURA]);
void salvarImagem(const int img[ALTURA][LARGURA]);

#endif
```

**`imagem.c`:**
```c
#include <stdio.h>
#include "imagem.h"

int lerImagem(int img[ALTURA][LARGURA]) {
    char tipo[4];
    int larg, alt, maxval;
    if (scanf("%3s %d %d %d", tipo, &larg, &alt, &maxval) != 4) {
        return 0;
    }
    if (tipo[0] != 'P' || tipo[1] != '2' || tipo[2] != '\0') {
        return 0;
    }
    if (larg != LARGURA || alt != ALTURA || maxval != 255) {
        return 0;
    }
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (scanf("%d", &img[i][j]) != 1) {
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

void aplicarBlur(int img[ALTURA][LARGURA], int t);

#endif
```

**`funcoes.c`:**
```c
#include "funcoes.h"

void aplicarBlur(int img[ALTURA][LARGURA], int t) {
    static int aux[ALTURA][LARGURA];
    int r = t / 2;

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            aux[i][j] = img[i][j];
        }
    }

    for (int i = r; i < ALTURA - r; i++) {
        for (int j = r; j < LARGURA - r; j++) {
            int soma = 0;
            for (int a = -r; a <= r; a++) {
                for (int b = -r; b <= r; b++) {
                    soma += aux[i + a][j + b];
                }
            }
            img[i][j] = soma / (t * t);
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
    int t;

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 0;
    }
    scanf("%d", &t);
    if (t != 3 && t != 5 && t != 7) {
        printf("Tamanho t invalido.\n");
        return 0;
    }
    aplicarBlur(img, t);
    salvarImagem(img);
    return 0;
}
```
