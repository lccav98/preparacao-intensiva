# Gabarito Comentado — Bloco `H01` (Arquitetura em 5 Arquivos PGM)

> **Bloco de referência:** [H01_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/blocos/H01_bloco.md)  
> **Nota para Caça ao Bug:** `H01-E03` e `H01-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo.  
> **Nota sobre Lacuna L3 (`[AUS/AMB]`):** Como o `main.c` inicial do professor não integra o acervo, os arquivos abaixo utilizam a versão equivalente via `stdin`/`stdout` (PGM P2).

---

## 1. Gabarito dos Exercícios (`H01-E01` a `H01-E05`)

### `H01-E01` *(Diagnóstico sem Compilar — Topologia de 5 Arquivos e Ligação)*
- **(a)** `funcoes.h` declara protótipos que usam as constantes `ALTURA` e `LARGURA` (definidas em `imagem.h`) nas dimensões dos parâmetros matriciais `int img[ALTURA][LARGURA]`; sem `#include "imagem.h"`, `funcoes.c` não reconhece essas constantes. Quando `main.c` inclui `"imagem.h"` e `"funcoes.h"`, `imagem.h` é alcançado duas vezes; as guardas `#ifndef IMAGEM_H` / `#define IMAGEM_H` / `#endif` impedem que o pré-processador processe o conteúdo do cabeçalho uma segunda vez na mesma unidade de tradução.
- **(b)** Erro de ligação **`undefined reference to 'lerImagem'`** (e **`undefined reference to 'salvarImagem'`**), porque `imagem.c` não foi passado ao ligador. Comando correto:
  ```bash
  gcc -std=c99 -Wall -Wextra main.c imagem.c funcoes.c -o processador
  ```
- **(c)** Como `imagem.h` é incluído por `main.c` e `imagem.c`, o corpo de `salvarImagem` será compilado nos dois arquivos-objeto (`.o`), gerando erro de ligação **`multiple definition of 'salvarImagem'`**.

---

### `H01-E02` *(Completar Cabeçalhos `imagem.h` e `funcoes.h`)*
- **`/* A */`:** `#ifndef IMAGEM_H`
- **`/* B */`:** `ALTURA`
- **`/* C */`:** `"imagem.h"`
- **`/* D */`:** `int img[ALTURA][LARGURA]`
- **`/* E */`:** `#endif`

---

### `H01-E03` *(Caça ao Bug Multi-Arquivo — Esqueleto Equivalente `3 x 4`)*
- **Erros intencionais:**
  1. `imagem.h` não possui guardas `#ifndef IMAGEM_H` / `#define IMAGEM_H` / `#endif` para proteger contra inclusões múltiplas via `main.c` + `funcoes.h`.
  2. `imagem.c` usa `#include <imagem.h>` em vez de `#include "imagem.h"` (`No such file or directory`).
  3. `funcoes.h` não inclui `"imagem.h"`, impedindo `funcoes.c` de enxergar `ALTURA` e `LARGURA`.
  4. `funcoes.h` declara `int limiarizar(...)` enquanto `funcoes.c` implementa `void limiarizar(...)` (`conflicting types for 'limiarizar'`).
- **Solução corrigida em 5 arquivos:** [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H01_E03_corrigido/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H01_E03_corrigido/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H01_E03_corrigido/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H01_E03_corrigido/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H01_E03_corrigido/main.c)
- **Comando GCC:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/H01_E03_corrigido/main.c solucoes/H01_E03_corrigido/imagem.c solucoes/H01_E03_corrigido/funcoes.c -o processador
  ```

**`imagem.h`:**
```c
#ifndef IMAGEM_H
#define IMAGEM_H
// Correcao: adicionadas guardas #ifndef/#define/#endif contra inclusao dupla

#define ALTURA 3
#define LARGURA 4

int lerImagem(int img[ALTURA][LARGURA]);
void salvarImagem(const int img[ALTURA][LARGURA]);

#endif
```

**`imagem.c`:**
```c
#include <stdio.h>
// Correcao: cabecalho local deve usar aspas duplas "imagem.h", nao <imagem.h>
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

// Correcao: incluir "imagem.h" para enxergar ALTURA e LARGURA
#include "imagem.h"

// Correcao: retorno deve ser void, igual ao definido em funcoes.c
void limiarizar(int img[ALTURA][LARGURA], int limiar);

#endif
```

**`funcoes.c`:**
```c
#include "funcoes.h"

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
        return 0;
    }
    scanf("%d", &limiar);
    limiarizar(img, limiar);
    salvarImagem(img);
    return 0;
}
```

---

### `H01-E04` *(Projeto 5-Arquivos — Negativo PGM `3 x 3`)*
Arquivos: [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H01_E04/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H01_E04/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H01_E04/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H01_E04/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H01_E04/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/H01_E04/main.c solucoes/H01_E04/imagem.c solucoes/H01_E04/funcoes.c -o processador
```

**`imagem.h`:**
```c
#ifndef IMAGEM_H
#define IMAGEM_H

#define ALTURA 3
#define LARGURA 3

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

void inverterCores(int img[ALTURA][LARGURA]);

#endif
```

**`funcoes.c`:**
```c
#include "funcoes.h"

void inverterCores(int img[ALTURA][LARGURA]) {
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            img[i][j] = 255 - img[i][j];
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
    inverterCores(img);
    salvarImagem(img);
    return 0;
}
```

---

### `H01-E05` *(Projeto 5-Arquivos — Limiarização e Contagem `2 x 4`)*
Arquivos: [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H01_E05/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H01_E05/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H01_E05/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H01_E05/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H01_E05/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/H01_E05/main.c solucoes/H01_E05/imagem.c solucoes/H01_E05/funcoes.c -o processador
```

**`imagem.h`:**
```c
#ifndef IMAGEM_H
#define IMAGEM_H

#define ALTURA 2
#define LARGURA 4

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

void limiarizar(int img[ALTURA][LARGURA], int limiar);
int contarBrancos(const int img[ALTURA][LARGURA]);

#endif
```

**`funcoes.c`:**
```c
#include "funcoes.h"

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

int contarBrancos(const int img[ALTURA][LARGURA]) {
    int brancos = 0;
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (img[i][j] == 255) {
                brancos++;
            }
        }
    }
    return brancos;
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
        return 0;
    }
    scanf("%d", &limiar);
    limiarizar(img, limiar);
    salvarImagem(img);
    printf("Brancos: %d\n", contarBrancos(img));
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`H01-C01` a `H01-C03`)

### `H01-C01` *(Rastreamento de Inclusões e Comando GCC)*
1. São compiladas **3** unidades de tradução (`.c`): `main.c`, `imagem.c` e `funcoes.c`. Comando:
   ```bash
   gcc -std=c99 -Wall -Wextra main.c imagem.c funcoes.c -o processador
   ```
2. `funcoes.h` precisa incluir `"imagem.h"` para ter acesso às macros `ALTURA` e `LARGURA` usadas nos protótipos das funções de processamento. Por causa disso, `imagem.h` precisa das guardas `#ifndef IMAGEM_H` / `#define IMAGEM_H` / `#endif` para não ser inserido em duplicidade quando `main.c` inclui ambos `"imagem.h"` e `"funcoes.h"`.
3. Ocorre erro de ligação **`undefined reference`** para as funções declaradas em `funcoes.h` e chamadas em `main.c`, pois seus códigos compilados não foram entregues ao ligador.

---

### `H01-C02` *(Caça ao Bug em Projeto 5-Arquivos — Zerar Bordas `3 x 3`)*
- **Erros intencionais:**
  1. `imagem.c` usa `#include <imagem.h>` em vez de `#include "imagem.h"` (`No such file or directory`).
  2. `funcoes.h` não tem guardas `#ifndef FUNCOES_H` / `#define FUNCOES_H` / `#endif`.
  3. `funcoes.h` contém a implementação completa de `zerarBordas` (gerando `multiple definition of 'zerarBordas'` ao incluir em `main.c` e `funcoes.c`), enquanto `funcoes.c` está vazio sem a definição.
- **Solução corrigida em 5 arquivos:** [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H01_C02_corrigido/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H01_C02_corrigido/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H01_C02_corrigido/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H01_C02_corrigido/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H01_C02_corrigido/main.c)

**`imagem.h`:**
```c
#ifndef IMAGEM_H
#define IMAGEM_H

#define ALTURA 3
#define LARGURA 3

int lerImagem(int img[ALTURA][LARGURA]);
void salvarImagem(const int img[ALTURA][LARGURA]);

#endif
```

**`imagem.c`:**
```c
#include <stdio.h>
// Correcao: cabecalho local deve usar aspas duplas "imagem.h"
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
// Correcao: adicionadas guardas #ifndef/#define/#endif

#include "imagem.h"

// Correcao: .h deve conter apenas o prototipo (corpo movido para funcoes.c)
void zerarBordas(int img[ALTURA][LARGURA]);

#endif
```

**`funcoes.c`:**
```c
#include "funcoes.h"

// Correcao: implementacao movida de funcoes.h para funcoes.c
void zerarBordas(int img[ALTURA][LARGURA]) {
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (i == 0 || i == ALTURA - 1 || j == 0 || j == LARGURA - 1) {
                img[i][j] = 0;
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

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 0;
    }
    zerarBordas(img);
    salvarImagem(img);
    return 0;
}
```

---

### `H01-C03` *(Projeto 5-Arquivos Independente — Espelhamento Horizontal `3 x 3`)*
Arquivos: [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H01_C03/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H01_C03/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H01_C03/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H01_C03/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H01_C03/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/H01_C03/main.c solucoes/H01_C03/imagem.c solucoes/H01_C03/funcoes.c -o processador
```

**`imagem.h`:**
```c
#ifndef IMAGEM_H
#define IMAGEM_H

#define ALTURA 3
#define LARGURA 3

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

void espelharHorizontal(int img[ALTURA][LARGURA]);

#endif
```

**`funcoes.c`:**
```c
#include "funcoes.h"

void espelharHorizontal(int img[ALTURA][LARGURA]) {
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA / 2; j++) {
            int aux = img[i][j];
            img[i][j] = img[i][LARGURA - 1 - j];
            img[i][LARGURA - 1 - j] = aux;
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
    espelharHorizontal(img);
    salvarImagem(img);
    return 0;
}
```
