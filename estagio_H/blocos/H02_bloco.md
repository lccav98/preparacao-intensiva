# Bloco `H02` — Filtros Ponto a Ponto Modularizados: Ajuste de Brilho e Limiarização com Saturação `[0, 255]`

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio H — Integração Geral e Projeto Modularizado (PGM) / **`H02`** |
| **Micro-habilidade foco** | *(Integração)* Declarar em `funcoes.h` e implementar em `funcoes.c` os filtros ponto a ponto *in-place* `ajustarBrilho(int img[ALTURA][LARGURA], int b)` (com saturação estrita `[0, 255]`) e `limiarizar(int img[ALTURA][LARGURA], int limiar)`, validados sobre matrizes pequenas. |
| **Pré-requisitos** | `H01` *(Arquitetura de 5 arquivos, `#ifndef` e compilação multi-arquivo)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão única de prática + checagem (22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Conteúdo novo de linguagem: NENHUM.** **Não utilize** `struct`, alocação dinâmica (`malloc`/`free`), VLAs, `gets(` ou recursividade. Mantenha `ALTURA`/`LARGURA` em `imagem.h`, `static int img[ALTURA][LARGURA];` em `main.c` e saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Filtro ponto a ponto *in-place* (sem matriz auxiliar):**
   - Cada novo pixel $I'(i, j)$ depende **apenas** do próprio pixel $I(i, j)$ na mesma posição (não depende dos vizinhos). Por isso, `ajustarBrilho` e `limiarizar` alteram `img[i][j]` diretamente *in-place*.
2. **Regra do ajuste de brilho `ajustarBrilho(int img[ALTURA][LARGURA], int b)`:**
   - Para cada pixel `(i, j)`, some `b` (positivo ou negativo):
     ```c
     int novo = img[i][j] + b;
     if (novo < 0) {
         img[i][j] = 0;
     } else if (novo > 255) {
         img[i][j] = 255;
     } else {
         img[i][j] = novo;
     }
     ```
   - **Erro clássico:** usar `% 256` em vez de condicionais de saturação (`240 + 30 = 270`, que com `% 256` viraria `14` escuro em vez de `255` branco).
3. **Regra da limiarização `limiarizar(int img[ALTURA][LARGURA], int limiar)`:**
   - Se `img[i][j] < limiar`, atribua `0`; caso contrário (`>= limiar`, incluindo a igualdade exata `== limiar`), atribua `255`.
4. **Coerência `.h` × `.c`:**
   - O protótipo em `funcoes.h` deve coincidir exatamente (tipo de retorno `void` e tipos dos parâmetros `int img[ALTURA][LARGURA], int b`) com a implementação em `funcoes.c`, que deve incluir `"funcoes.h"`.

---

## 2. Exemplos Guiados

### Exemplo 1 — Saturação `[0, 255]` em `ajustarBrilho` *(Rastreio tabular)*
Considere três pixels individuais submetidos a diferentes valores de `b`:

| Pixel original $I(i, j)$ | Ajuste $b$ | Soma $I(i, j) + b$ | Saturação `[0, 255]` | Resultado $I'(i, j)$ |
|---:|---:|---:|---|---:|
| `200` | `+30` | `230` | `0 <= 230 <= 255` | **`230`** |
| `240` | `+30` | `270` | `270 > 255` → satura | **`255`** |
| `10` | `-30` | `-20` | `-20 < 0` → satura | **`0`** |

### Exemplo 2 — Módulo `funcoes.h` / `funcoes.c` com brilho e limiarização *(Trecho ilustrativo)*

**`funcoes.h`**
```c
#ifndef FUNCOES_H
#define FUNCOES_H

#include "imagem.h"

void ajustarBrilho(int img[ALTURA][LARGURA], int b);
void limiarizar(int img[ALTURA][LARGURA], int limiar);

#endif
```

**`funcoes.c`**
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

---

## 3. Exercícios (`H02-E01` a `H02-E05`)

### `H02-E01` *(Teste de Mesa com Matriz `3 x 3` — Brilho e Limiarização)*
Sem usar computador, considere a matriz `3 x 3` original abaixo:
```text
  5   200   240
 10   128   255
  0    30   250
```
1. Calcule a matriz resultante após aplicar `ajustarBrilho(img, 30)` (`b = +30`).
2. Partindo **novamente da matriz original**, calcule a matriz resultante após `ajustarBrilho(img, -30)` (`b = -30`).
3. Partindo **novamente da matriz original**, calcule a matriz resultante após `limiarizar(img, 128)`.

---

### `H02-E02` *(Completar Protótipo em `funcoes.h` e Implementação em `funcoes.c`)*
Complete as lacunas `/* A */` a `/* D */` para declarar e implementar `ajustarBrilho` e `limiarizar`:

**`funcoes.h`**
```c
#ifndef FUNCOES_H
#define FUNCOES_H

#include "imagem.h"

/* A */ ajustarBrilho(int img[ALTURA][LARGURA], int b);
void limiarizar(int img[ALTURA][LARGURA], int limiar);

#endif
```

**`funcoes.c`**
```c
#include "funcoes.h"

void ajustarBrilho(int img[ALTURA][LARGURA], int b) {
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            img[i][j] += b;
            if (/* B */) {
                img[i][j] = 0;
            } else if (/* C */) {
                img[i][j] = 255;
            }
        }
    }
}

void limiarizar(int img[ALTURA][LARGURA], int limiar) {
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (/* D */) {
                img[i][j] = 0;
            } else {
                img[i][j] = 255;
            }
        }
    }
}
```

---

### `H02-E03` *(Caça ao Bug Multi-Arquivo — Saturação e Assinatura `3 x 3`)*
O projeto de 5 arquivos abaixo deveria ler uma imagem PGM P2 `3 x 3` e um inteiro `b`, aplicar `ajustarBrilho(img, b)` com saturação `[0, 255]` e exibir o resultado via `salvarImagem(img)`. Identifique os **3 bugs intencionais** espalhados entre `funcoes.h`, `funcoes.c` e `main.c`, corrija os arquivos e explique cada bug usando **comentários `//` diretamente no código**:

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

**`funcoes.h` (com erro):**
```c
#ifndef FUNCOES_H
#define FUNCOES_H

#include "imagem.h"

int ajustarBrilho(int img[ALTURA][LARGURA], int b);

#endif
```

**`funcoes.c` (com erro):**
```c
#include "funcoes.h"

void ajustarBrilho(int img[ALTURA][LARGURA], int b) {
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            img[i][j] = (img[i][j] + b) % 256;
        }
    }
}
```

**`main.c` (com erro):**
```c
#include <stdio.h>
#include "imagem.h"

int main(void) {
    static int img[ALTURA][LARGURA];
    int b;

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 0;
    }
    scanf("%d", &b);
    ajustarBrilho(img, b);
    salvarImagem(img);
    return 0;
}
```

---

### `H02-E04` *(Variação controlada com pistas — Brilho e Contagem de Extremos `3 x 3`)*
Implemente um projeto completo em **5 arquivos** (`ALTURA 3`, `LARGURA 3`):
- `imagem.h/.c`: `lerImagem` e `salvarImagem`.
- `funcoes.h/.c`:
  - `void ajustarBrilho(int img[ALTURA][LARGURA], int b);` (saturação `[0, 255]`)
  - `int contarExtremos(const int img[ALTURA][LARGURA]);` (conta quantos pixels ficaram exatamente iguais a `0` ou `255`).
- `main.c`: lê a imagem PGM P2 (`lerImagem`; se falhar, imprime `Erro ao ler imagem.\n` e encerra), lê `int b`, chama `ajustarBrilho(img, b)`, exibe a imagem via `salvarImagem(img)` e imprime na linha seguinte:
  ```text
  Extremos (0 ou 255): K
  ```

*Pista:* Em `contarExtremos`, use `const int img[ALTURA][LARGURA]` tanto em `funcoes.h` quanto em `funcoes.c`.

---

### `H02-E05` *(Resolução independente — Brilho Seguido de Limiarização `3 x 4`)*
Construa um projeto completo em **5 arquivos** (`ALTURA 3`, `LARGURA 4`):
- `imagem.h/.c`: `lerImagem` e `salvarImagem`.
- `funcoes.h/.c`: `void ajustarBrilho(int img[ALTURA][LARGURA], int b);` e `void limiarizar(int img[ALTURA][LARGURA], int limiar);`.
- `main.c`: lê a imagem PGM P2 (`lerImagem`; imprime `Erro ao ler imagem.\n` se falhar), lê os inteiros `b` e `limiar`, aplica **primeiro** `ajustarBrilho(img, b)` e **depois** `limiarizar(img, limiar)`, e grava o resultado com `salvarImagem(img)`.

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `H02-C01` *(Teste de Mesa de Brilho e Limiarização Encadeados)*
Considere a matriz `3 x 3` abaixo:
```text
  0    15   220
 40   127   255
 25   190   245
```
1. Calcule a matriz após `ajustarBrilho(img, 40)` (`b = +40`).
2. Partindo **da matriz original**, calcule a matriz após `ajustarBrilho(img, -40)` (`b = -40`).
3. Partindo **do resultado obtido no item 2**, calcule a matriz após `limiarizar(img, 100)`.

### `H02-C02` *(Caça ao Bug — Assinatura, Fronteira de Limiarização e Ordem em `main.c`)*
O projeto de 5 arquivos abaixo (`ALTURA 3`, `LARGURA 3`) deveria ler uma imagem PGM P2 e um limiar `L`, aplicar `limiarizar(img, L)` (`< L -> 0`, `>= L -> 255`) e imprimir a imagem resultante. Identifique e corrija os **3 bugs** presentes (com comentários `//` no código):

**`imagem.h` e `imagem.c`:** padrão correto para `ALTURA 3`, `LARGURA 3`.

**`funcoes.h` (com erro):**
```c
#ifndef FUNCOES_H
#define FUNCOES_H

#include "imagem.h"

void limiarizar(int img[ALTURA][LARGURA], double L);

#endif
```

**`funcoes.c` (com erro):**
```c
#include "funcoes.h"

void limiarizar(int img[ALTURA][LARGURA], int L) {
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (img[i][j] < L) {
                img[i][j] = 0;
            } else if (img[i][j] > L) {
                img[i][j] = 255;
            }
        }
    }
}
```

**`main.c` (com erro):**
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
    salvarImagem(img);
    limiarizar(img, limiar);
    return 0;
}
```

### `H02-C03` *(Projeto 5-Arquivos Independente — `ajustarBrilho` com Casos de Borda `0` e `255`)*
Construa um projeto completo em **5 arquivos** (`ALTURA 3`, `LARGURA 3`) com `ajustarBrilho(int img[ALTURA][LARGURA], int b)` em `funcoes.h/.c` e `main.c` que lê a imagem PGM P2 (`lerImagem`), lê `int b`, aplica `ajustarBrilho(img, b)` e imprime via `salvarImagem(img)`. Compile com `gcc -std=c99 -Wall -Wextra main.c imagem.c funcoes.c -o processador` e verifique casos com saturação em `0` e `255`.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `H03` (`Matriz Auxiliar, Preservação de Bordas e Filtro de Desfoque Blur t x t`):** somente após autocorreção de `H02-E01..E05` e **100% (3/3)** na Checagem Independente `H02-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** revisar a tabela de saturação (`< 0 -> 0`, `> 255 -> 255`), conferir igualdade de assinaturas entre `funcoes.h` e `funcoes.c` e aplicar variante `V2` de `H02`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`H01`** (arquitetura `.h`/`.c` de 5 arquivos) e **`E07`** (saturação `[0, 255]` e limiarização em PGM P2).

---

## 6. Referências do Orientador
- `[DOC]` `Trabalho_Algoritmos.pdf` p. 2, 4 (Seção 4.1: ajuste de brilho `I'(i,j) = I(i,j) + b`, saturação `[0, 255]`, exemplos `200+30`, `240+30`, `10-30`, e limiarização opcional em `funcoes`).
- `[DOC]` `Apresentacao_Trabalho_Algoritmos.pdf` p. 7–8 (responsabilidades de `funcoes.h/.c` e filtro de brilho).
- Casos de teste e soluções verificáveis: [H02_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/gabaritos/H02_gabarito.md) e [H02_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/H02_testes.md).
