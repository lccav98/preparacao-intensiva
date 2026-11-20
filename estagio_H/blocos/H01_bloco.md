# Bloco `H01` — Arquitetura em 5 Arquivos (`main.c`, `imagem.h/.c`, `funcoes.h/.c`) e Compilação Multi-Arquivo

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio H — Integração Geral e Projeto Modularizado (PGM) / **`H01`** |
| **Micro-habilidade foco** | *(Integração)* Estruturar o projeto de processamento de imagens PGM P2 na arquitetura de **5 arquivos** (`main.c`, `imagem.h`, `imagem.c`, `funcoes.h`, `funcoes.c`), com guardas `#ifndef`/`#define`/`#endif`, inclusão `"imagem.h"` dentro de `"funcoes.h"`, constantes `ALTURA`/`LARGURA` compartilhadas e compilação conjunta no GCC. |
| **Pré-requisitos** | `F10` *(Revisão e consolidação de modularização e multi-arquivo `.h`/`.c`)* e `E08` *(Revisão de matrizes 2D e PGM P2)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão única de prática + checagem (25 min):** `15 min` resol. \| `6 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Conteúdo novo de linguagem: NENHUM.** **Não utilize** `struct`, alocação dinâmica (`malloc`/`free`), VLAs (`int m[alt][larg]`), `gets(` ou parser próprio com `FILE*`. Utilize `#define ALTURA` / `#define LARGURA`, `static int ...[ALTURA][LARGURA]` para matrizes grandes e saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

> **Nota sobre Lacuna L3 (`[AUS/AMB]`):** O arquivo `main.c` inicial e as imagens `.pgm` fornecidos pelo professor não constam no acervo auditado. Neste bloco e nos seguintes, adotamos um esqueleto inicial **equivalente** (`lerImagem`, `limiarizar`, `salvarImagem`) operando sobre formato **PGM textual (P2)** via entrada e saída padrão (`stdin`/`stdout`) com matriz fixa `[ALTURA][LARGURA]`, preservando integralmente a topologia e as responsabilidades dos 5 arquivos do `Trabalho_Algoritmos.pdf`.

1. **Papel de cada um dos 5 arquivos do projeto:**
   - **`imagem.h`:** define `#define ALTURA ...`, `#define LARGURA ...` e os protótipos de `lerImagem` e `salvarImagem`.
   - **`imagem.c`:** inclui `<stdio.h>` e `"imagem.h"`, implementando `lerImagem` e `salvarImagem`.
   - **`funcoes.h`:** inclui `"imagem.h"` (para enxergar `ALTURA` e `LARGURA`) e declara os protótipos dos filtros (ex.: `limiarizar`).
   - **`funcoes.c`:** inclui `"funcoes.h"` e implementa as funções de processamento da imagem.
   - **`main.c`:** inclui `<stdio.h>`, `"imagem.h"` e `"funcoes.h"`, declara a matriz `static int img[ALTURA][LARGURA];`, carrega a imagem, chama o processamento e grava o resultado.
2. **Guardas de inclusão (`#ifndef` / `#define` / `#endif`) e inclusão `"imagem.h"` em `"funcoes.h"`:**
   - Como `main.c` inclui **ambos** `"imagem.h"` e `"funcoes.h"` (e `"funcoes.h"` também inclui `"imagem.h"`), `imagem.h` será pré-processado em cadeia. As guardas impedem redefinição dupla:
     ```c
     #ifndef IMAGEM_H
     #define IMAGEM_H
     /* constantes e prototipos */
     #endif
     ```
   - Sempre inclua `"imagem.h"` dentro de `"funcoes.h"` para que qualquer `.c` que inclua apenas `"funcoes.h"` (como `funcoes.c`) conheça `ALTURA` e `LARGURA`.
3. **Compilação conjunta no GCC (C99):**
   - Liste **apenas os arquivos `.c`** (nunca passe `.h` no comando `gcc`):
     ```bash
     gcc -std=c99 -Wall -Wextra main.c imagem.c funcoes.c -o processador
     ```
4. **Diagnóstico rápido de erros multi-arquivo:**
   - **Omissão de `.c` no `gcc`** (ex.: esquecer `imagem.c`): erro de ligação `undefined reference to 'lerImagem'`.
   - **Corpo de função dentro de `.h`**: erro de ligação `multiple definition of '...'`.
   - **Divergência entre `.h` e `.c`**: erro de compilação `conflicting types for '...'`.
   - **Uso de `<imagem.h>` para arquivo local**: erro de pré-processamento `No such file or directory`.

---

## 2. Exemplos Guiados

### Exemplo 1 — Diagrama de dependências dos 5 arquivos *(Esquema conceitual)*
```text
          main.c
         /      \
  #include      #include
       /          \
  imagem.h <--- funcoes.h   (funcoes.h inclui "imagem.h")
     |              |
  imagem.c      funcoes.c
```
- **Unidades compiladas pelo GCC:** `main.c`, `imagem.c`, `funcoes.c`.
- **Ordem do comando:** `gcc -std=c99 -Wall -Wextra main.c imagem.c funcoes.c -o processador`.

### Exemplo 2 — Projeto mínimo equivalente em 5 arquivos (`3 x 3`) *(Projeto completo)*

**`imagem.h`**
```c
#ifndef IMAGEM_H
#define IMAGEM_H

#define ALTURA 3
#define LARGURA 3

int lerImagem(int img[ALTURA][LARGURA]);
void salvarImagem(const int img[ALTURA][LARGURA]);

#endif
```

**`imagem.c`**
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

**`funcoes.h`**
```c
#ifndef FUNCOES_H
#define FUNCOES_H

#include "imagem.h"

void limiarizar(int img[ALTURA][LARGURA], int limiar);

#endif
```

**`funcoes.c`**
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

**`main.c`**
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

## 3. Exercícios (`H01-E01` a `H01-E05`)

### `H01-E01` *(Diagnóstico sem Compilar — Topologia de 5 Arquivos e Ligação)*
Responda sem usar o compilador:
- **(a)** Por que `funcoes.h` precisa conter `#include "imagem.h"`? E o que acontece em `main.c` (que inclui `"imagem.h"` e `"funcoes.h"`) caso `imagem.h` não possua guardas `#ifndef IMAGEM_H` / `#define IMAGEM_H` / `#endif` e defina macros ou protótipos incompatíveis em cadeia?
- **(b)** Um estudante organizou corretamente os 5 arquivos, mas executou `gcc -std=c99 -Wall -Wextra main.c funcoes.c -o processador`. Qual erro ocorre (`No such file`, `undefined reference`, `multiple definition` ou `conflicting types`) e qual é o comando completo correto?
- **(c)** O que acontece se um estudante implementar o corpo de `salvarImagem` dentro de `imagem.h` em vez de `imagem.c`?

---

### `H01-E02` *(Completar Cabeçalhos `imagem.h` e `funcoes.h`)*
Complete as lacunas `/* A */` a `/* E */` para uma matriz `3 x 3` nos dois arquivos de cabeçalho abaixo:

**`imagem.h`**
```c
/* A */
#define IMAGEM_H

#define /* B */ 3
#define LARGURA 3

int lerImagem(int img[ALTURA][LARGURA]);
void salvarImagem(const int img[ALTURA][LARGURA]);

#endif
```

**`funcoes.h`**
```c
#ifndef FUNCOES_H
#define FUNCOES_H

#include /* C */

void limiarizar(/* D */, int limiar);

/* E */
```

---

### `H01-E03` *(Caça ao Bug Multi-Arquivo — Esqueleto Equivalente `3 x 4`)*
O projeto de 5 arquivos abaixo deveria ler uma imagem PGM P2 de dimensões `ALTURA = 3` (linhas) por `LARGURA = 4` (colunas) e um inteiro `limiar`, aplicar `limiarizar` (`< limiar -> 0`, `>= limiar -> 255`) e exibir a imagem PGM resultante (ou `Erro ao ler imagem.\n` se `lerImagem` falhar). Identifique os **4 bugs intencionais** distribuídos nos arquivos, corrija o projeto e explique cada bug usando **comentários `//` diretamente no código**:

**`imagem.h` (com erro):**
```c
#define ALTURA 3
#define LARGURA 4

int lerImagem(int img[ALTURA][LARGURA]);
void salvarImagem(const int img[ALTURA][LARGURA]);
```

**`imagem.c` (com erro):**
```c
#include <stdio.h>
#include <imagem.h>

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

**`funcoes.h` (com erro):**
```c
#ifndef FUNCOES_H
#define FUNCOES_H

int limiarizar(int img[ALTURA][LARGURA], int limiar);

#endif
```

**`funcoes.c` (com erro):**
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

### `H01-E04` *(Variação controlada com pistas — Negativo PGM em 5 Arquivos `3 x 3`)*
Implemente um projeto completo de **5 arquivos** (`imagem.h`, `imagem.c`, `funcoes.h`, `funcoes.c`, `main.c`) para imagens **`ALTURA 3`** × **`LARGURA 3`**:
- `imagem.h/.c`: funções `lerImagem` e `salvarImagem` (formato PGM P2 via `stdin`/`stdout`, retornando `0` em erro de leitura).
- `funcoes.h/.c`: declare e implemente `void inverterCores(int img[ALTURA][LARGURA]);`, que substitui cada pixel `img[i][j]` por `255 - img[i][j]`.
- `main.c`: declara `static int img[ALTURA][LARGURA];`, chama `lerImagem(img)` (imprimindo `Erro ao ler imagem.\n` e encerrando com `return 0;` se falhar), aplica `inverterCores(img)` e exibe o resultado com `salvarImagem(img)`.

*Pista:* Em `funcoes.h`, inclua `"imagem.h"` dentro das guardas `FUNCOES_H`, e compile com `gcc -std=c99 -Wall -Wextra main.c imagem.c funcoes.c -o processador`.

---

### `H01-E05` *(Resolução independente — Limiarização e Contagem em 5 Arquivos `2 x 4`)*
Construa um projeto completo em **5 arquivos** (`imagem.h`, `imagem.c`, `funcoes.h`, `funcoes.c`, `main.c`) para imagens **`ALTURA 2`** × **`LARGURA 4`**:
- `imagem.h/.c`: `lerImagem` e `salvarImagem`.
- `funcoes.h/.c`:
  - `void limiarizar(int img[ALTURA][LARGURA], int limiar);` (`< limiar -> 0`, `>= limiar -> 255`)
  - `int contarBrancos(const int img[ALTURA][LARGURA]);` (retorna quantos pixels são iguais a `255`).
- `main.c`: lê a imagem PGM P2 (se falhar, imprime `Erro ao ler imagem.\n` e encerra), lê `int limiar`, aplica `limiarizar(img, limiar)`, imprime a imagem via `salvarImagem(img)` e, na linha seguinte, imprime exatamente:
  ```text
  Brancos: B
  ```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `H01-C01` *(Rastreamento de Inclusões e Comando GCC em 5 Arquivos)*
Considere a arquitetura de 5 arquivos (`main.c`, `imagem.h`, `imagem.c`, `funcoes.h`, `funcoes.c`) onde `funcoes.h` inclui `"imagem.h"`, `main.c` inclui `"imagem.h"` e `"funcoes.h"`, `imagem.c` inclui `"imagem.h"` e `funcoes.c` inclui `"funcoes.h"`:
1. Quantas unidades `.c` são passadas ao compilador `gcc`? Escreva o comando completo usando `-std=c99 -Wall -Wextra` gerando o executável `processador`.
2. Explique por que `funcoes.h` deve incluir `"imagem.h"` e qual proteção `imagem.h` precisa ter por causa disso.
3. O que acontece na ligação se o comando `gcc` omitir `funcoes.c`?

### `H01-C02` *(Caça ao Bug em Projeto 5-Arquivos — Zerar Bordas `3 x 3`)*
O projeto de 5 arquivos abaixo deveria ler uma imagem PGM P2 `3 x 3`, zerar os pixels das bordas (`i == 0 || i == ALTURA - 1 || j == 0 || j == LARGURA - 1`) por meio de `zerarBordas(img)` e imprimir o resultado via `salvarImagem(img)`. Identifique e corrija os **3 bugs** presentes (explicando em comentários `//`):

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

**`imagem.c` (com erro):**
```c
#include <stdio.h>
#include <imagem.h>

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

**`funcoes.h` (com erro):**
```c
#include "imagem.h"

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

**`funcoes.c` (com erro):**
```c
#include "funcoes.h"
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

### `H01-C03` *(Projeto 5-Arquivos Independente — Espelhamento Horizontal `3 x 3`)*
Crie os **5 arquivos** (`imagem.h`, `imagem.c`, `funcoes.h`, `funcoes.c`, `main.c`) para imagens **`ALTURA 3`** × **`LARGURA 3`**:
- `funcoes.h/.c`: `void espelharHorizontal(int img[ALTURA][LARGURA]);`, que inverte a ordem das colunas em cada linha *in-place* (ex.: `{10, 20, 30}` passa a `{30, 20, 10}`).
- `main.c`: usa `static int img[ALTURA][LARGURA];`, lê a imagem PGM P2 com `lerImagem(img)` (imprime `Erro ao ler imagem.\n` e encerra se falhar), chama `espelharHorizontal(img)` e imprime via `salvarImagem(img)`.
Verifique compilação limpa com `gcc -std=c99 -Wall -Wextra main.c imagem.c funcoes.c -o processador`.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `H02` (`Filtros Ponto a Ponto Modularizados: Ajuste de Brilho e Limiarização`):** somente após autocorreção de `H01-E01..E05` e **100% (3/3)** na Checagem Independente `H01-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** redesenhar o grafo dos 5 arquivos identificando onde vivem `#define ALTURA`/`LARGURA`, onde ficam protótipos vs. implementações e quais `.c` entram no comando `gcc`; aplicar variante `V2` de `H01`.
- **Após 2 tentativas malsucedidas:** parar a repetição de `H01` e investigar os pré-requisitos **`F10`** (revisão `.h`/`.c`, guardas `#ifndef` e diagnóstico de ligação) e **`E08`** (representação matricial PGM P2 e ordem `largura` × `altura`).

---

## 6. Referências do Orientador
- `[DOC]` `Trabalho_Algoritmos.pdf` p. 1–2, 5 (estrutura obrigatória de 5 arquivos, uso de `static` e compilação `gcc main.c imagem.c funcoes.c -o processador`).
- `[DOC]` `Apresentacao_Trabalho_Algoritmos.pdf` p. 4–7, 14–15 (diagrama dos 5 arquivos, responsabilidades por arquivo e exemplo `.h`/`.c`).
- `[DOC]` `Aula_24_Algoritmos.pdf` p. 19 (primeiros passos para organização em 5 arquivos).
- `[AUS/AMB]` Lacuna L3 documentada em [00_inventario_fontes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/00_inventario_fontes.md): `main.c` inicial do professor ausente no acervo; esqueleto equivalente construído no curso.
- Casos de teste e soluções verificáveis: [H01_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/gabaritos/H01_gabarito.md) e [H01_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/H01_testes.md).
