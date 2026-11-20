# Gabarito Comentado — Bloco `H06` (Verificação Sistemática, Arguição e Conclusão)

> **Bloco de referência:** [H06_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/blocos/H06_bloco.md)  
> **Nota para Caça ao Bug:** `H06-E03` no bloco do aluno contém **3 erros intencionais** detalhados abaixo.  
> **Nota sobre Opcionais:** `H06-OP1` e `H06-OP2` são desafios `[OPCIONAIS]` e **não bloqueiam** a conclusão do curso.

---

## 1. Gabarito dos Exercícios (`H06-E01` a `H06-E06` + Opcionais)

### `H06-E01` *(Checklist de Casos de Borda Calculados à Mão)*
- **(a) `ajustarBrilho(img, 40)`:**
  - `(0, 0)`: `10 + 40 = 50`
  - `(1, 1)`: `220 + 40 = 260` $\rightarrow$ **`255`** *(saturado)*
  - `(1, 3)`: `240 + 40 = 280` $\rightarrow$ **`255`** *(saturado)*
  - `(4, 4)`: `250 + 40 = 290` $\rightarrow$ **`255`** *(saturado)*
- **(b) `ajustarBrilho(img, -40)`:**
  - `(0, 0)`: `10 - 40 = -30` $\rightarrow$ **`0`** *(saturado)*
  - `(3, 0)`: `15 - 40 = -25` $\rightarrow$ **`0`** *(saturado)*
  - `(4, 0)`: `0 - 40 = -40` $\rightarrow$ **`0`** *(saturado)*
  - `(4, 2)`: `45 - 40 = 5`
- **(c) `aplicarMediana(img)` em `(2, 2)`:**
  - Vizinhança `3 x 3`: `{220, 230, 240, 100, 255, 110, 120, 130, 140}`
  - Ordenado: `{100, 110, 120, 130, 140, 220, 230, 240, 255}` $\rightarrow$ `v[4] =` **`140`**.
  - `(0, 0) = 10` e `(4, 4) = 250` **não mudam** (são bordas preservadas).
- **(d) `aplicarBlur(img, 5)` em `(2, 2)`:**
  - Soma das 5 linhas: `150 + 820 + 635 + 430 + 385 = 2420`.
  - Média inteira: `2420 / 25 =` **`96`** *(descarta `.80`)*.
  - Com `r = 5 / 2 = 2`, apenas `(2, 2)` é interno; os **`24`** pixels restantes permanecem inalterados como borda.

### `H06-E02` *(Simulado Misto Integrado — Rastreamento Sem Computador)*
- Linha `0`: `min = 5`, `max = 18`; em `m[0] = {12, 5, 18, 9}`, há `3` elementos estritamente maiores que `5` (`12, 18, 9`).
- `ref = 5`. Linha `1`: `min = 3`, `max = 20`; em `m[1] = {20, 3, 14, 7}`, há `3` elementos estritamente maiores que `ref = 5` (`20, 14, 7`).
- **Saída exata:**
  ```text
  L0: 5..18 acima=3
  L1: 3..20 acima=3
  ```

### `H06-E03` *(Arguição Oral + Caça ao Bug em Modificação ao Vivo)*
- **(a) Respostas objetivas de arguição:**
  1. Matrizes locais grandes ficam na pilha (*stack*), cujo limite pode ser excedido (*stack overflow*); com `static`, a matriz é alocada na área estática de memória.
  2. `ajustarBrilho` depende apenas do valor original do próprio pixel `(i, j)`. Já `blur` e `mediana` leem vizinhos ao redor de `(i, j)`: sem `aux`, pixels já atualizados contaminariam o cálculo dos vizinhos seguintes.
  3. O compilador falha ou rejeita a entrada porque arquivos `.h` **não** devem ser passados ao `gcc` (apenas os `.c`); além disso, faltaria `funcoes.c`, causando `undefined reference` na ligação.
- **(b) Erros intencionais no código:**
  1. **Assinatura conflitante (`conflicting types`):** `funcoes.h` declara `int inverterCores(...)`, mas `funcoes.c` define `void inverterCores(...)`. Ambos devem ser `void`.
  2. **Acesso fora dos limites (*off-by-one*):** `i <= ALTURA` e `j <= LARGURA` acessam `img[ALTURA][...]` e `img[...][LARGURA]`, invadindo memória. Deve ser `i < ALTURA` e `j < LARGURA`.
  3. **Ausência de `break;` no `case 4`:** após chamar `inverterCores(img)`, o fluxo cai no `default:` imprimindo `Opcao invalida.\n`.
- **Arquivos corrigidos:** [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_E03_corrigido/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_E03_corrigido/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_E03_corrigido/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_E03_corrigido/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_E03_corrigido/main.c)
- **Comando GCC:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/H06_E03_corrigido/main.c solucoes/H06_E03_corrigido/imagem.c solucoes/H06_E03_corrigido/funcoes.c -o prog
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

void ajustarBrilho(int img[ALTURA][LARGURA], int b);
void aplicarBlur(int img[ALTURA][LARGURA], int t);
void ordenar(int v[], int n);
void aplicarMediana(int img[ALTURA][LARGURA]);
// Bug 1 corrigido: tipo de retorno void alinhado a definicao em funcoes.c
void inverterCores(int img[ALTURA][LARGURA]);

#endif
```

**`funcoes.c`:**
```c
#include "funcoes.h"

void ajustarBrilho(int img[ALTURA][LARGURA], int b) {
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            int novo = img[i][j] + b;
            if (novo < 0) {
                novo = 0;
            } else if (novo > 255) {
                novo = 255;
            }
            img[i][j] = novo;
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
                    soma += img[i + a][j + b];
                }
            }
            aux[i][j] = soma / (t * t);
        }
    }

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            img[i][j] = aux[i][j];
        }
    }
}

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

void inverterCores(int img[ALTURA][LARGURA]) {
    // Bug 2 corrigido: limites estritos < ALTURA e < LARGURA (evita invasao de memoria)
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
    int opcao, b, t;

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 1;
    }

    do {
        printf("===== PROCESSAMENTO DE IMAGENS =====\n");
        printf("1 - Ajustar brilho\n");
        printf("2 - Aplicar desfoque (blur)\n");
        printf("3 - Aplicar filtro da mediana\n");
        printf("4 - Inverter cores\n");
        printf("0 - Salvar e sair\n");
        printf("Escolha uma opcao:\n");
        if (scanf("%d", &opcao) != 1) {
            return 1;
        }

        switch (opcao) {
            case 1:
                scanf("%d", &b);
                ajustarBrilho(img, b);
                break;
            case 2:
                scanf("%d", &t);
                if (t == 3 || t == 5 || t == 7) {
                    aplicarBlur(img, t);
                } else {
                    printf("Tamanho invalido. Use 3, 5 ou 7.\n");
                }
                break;
            case 3:
                aplicarMediana(img);
                break;
            case 4:
                inverterCores(img);
                // Bug 3 corrigido: break obrigatorio para nao cair no default
                break;
            case 0:
                salvarImagem(img);
                break;
            default:
                printf("Opcao invalida.\n");
                break;
        }
    } while (opcao != 0);

    return 0;
}
```

### `H06-E04` *(Modificação ao Vivo 1 — Limiarização como Opção `4`)*
Arquivos: [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_E04/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_E04/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_E04/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_E04/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_E04/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/H06_E04/main.c solucoes/H06_E04/imagem.c solucoes/H06_E04/funcoes.c -o prog
```
*(Os arquivos `imagem.h` e `imagem.c` são idênticos aos de `H06_E03_corrigido`.)*

**`funcoes.h`:**
```c
#ifndef FUNCOES_H
#define FUNCOES_H

#include "imagem.h"

void ajustarBrilho(int img[ALTURA][LARGURA], int b);
void aplicarBlur(int img[ALTURA][LARGURA], int t);
void ordenar(int v[], int n);
void aplicarMediana(int img[ALTURA][LARGURA]);
void limiarizar(int img[ALTURA][LARGURA], int limiar);

#endif
```

**`funcoes.c`:**
```c
#include "funcoes.h"

void ajustarBrilho(int img[ALTURA][LARGURA], int b) {
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            int novo = img[i][j] + b;
            if (novo < 0) {
                novo = 0;
            } else if (novo > 255) {
                novo = 255;
            }
            img[i][j] = novo;
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
                    soma += img[i + a][j + b];
                }
            }
            aux[i][j] = soma / (t * t);
        }
    }

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            img[i][j] = aux[i][j];
        }
    }
}

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
    int opcao, b, t, limiar;

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 1;
    }

    do {
        printf("===== PROCESSAMENTO DE IMAGENS =====\n");
        printf("1 - Ajustar brilho\n");
        printf("2 - Aplicar desfoque (blur)\n");
        printf("3 - Aplicar filtro da mediana\n");
        printf("4 - Aplicar limiarizacao\n");
        printf("0 - Salvar e sair\n");
        printf("Escolha uma opcao:\n");
        if (scanf("%d", &opcao) != 1) {
            return 1;
        }

        switch (opcao) {
            case 1:
                scanf("%d", &b);
                ajustarBrilho(img, b);
                break;
            case 2:
                scanf("%d", &t);
                if (t == 3 || t == 5 || t == 7) {
                    aplicarBlur(img, t);
                } else {
                    printf("Tamanho invalido. Use 3, 5 ou 7.\n");
                }
                break;
            case 3:
                aplicarMediana(img);
                break;
            case 4:
                scanf("%d", &limiar);
                if (limiar >= 0 && limiar <= 255) {
                    limiarizar(img, limiar);
                } else {
                    printf("Limiar invalido. Use 0 a 255.\n");
                }
                break;
            case 0:
                salvarImagem(img);
                break;
            default:
                printf("Opcao invalida.\n");
                break;
        }
    } while (opcao != 0);

    return 0;
}
```

### `H06-E05` *(Modificação ao Vivo 2 — `espelharHorizontal`)*
Arquivos: [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_E05/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_E05/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_E05/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_E05/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_E05/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/H06_E05/main.c solucoes/H06_E05/imagem.c solucoes/H06_E05/funcoes.c -o prog
```
*(Os arquivos `imagem.h` e `imagem.c` são idênticos aos de `H06_E03_corrigido`.)*

**`funcoes.h`:**
```c
#ifndef FUNCOES_H
#define FUNCOES_H

#include "imagem.h"

void ajustarBrilho(int img[ALTURA][LARGURA], int b);
void aplicarBlur(int img[ALTURA][LARGURA], int t);
void ordenar(int v[], int n);
void aplicarMediana(int img[ALTURA][LARGURA]);
void espelharHorizontal(int img[ALTURA][LARGURA]);

#endif
```

**`funcoes.c`:**
```c
#include "funcoes.h"

void ajustarBrilho(int img[ALTURA][LARGURA], int b) {
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            int novo = img[i][j] + b;
            if (novo < 0) {
                novo = 0;
            } else if (novo > 255) {
                novo = 255;
            }
            img[i][j] = novo;
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
                    soma += img[i + a][j + b];
                }
            }
            aux[i][j] = soma / (t * t);
        }
    }

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            img[i][j] = aux[i][j];
        }
    }
}

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

void espelharHorizontal(int img[ALTURA][LARGURA]) {
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA / 2; j++) {
            int temp = img[i][j];
            img[i][j] = img[i][LARGURA - 1 - j];
            img[i][LARGURA - 1 - j] = temp;
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
    int opcao, b, t;

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 1;
    }

    do {
        printf("===== PROCESSAMENTO DE IMAGENS =====\n");
        printf("1 - Ajustar brilho\n");
        printf("2 - Aplicar desfoque (blur)\n");
        printf("3 - Aplicar filtro da mediana\n");
        printf("4 - Espelhar horizontalmente\n");
        printf("0 - Salvar e sair\n");
        printf("Escolha uma opcao:\n");
        if (scanf("%d", &opcao) != 1) {
            return 1;
        }

        switch (opcao) {
            case 1:
                scanf("%d", &b);
                ajustarBrilho(img, b);
                break;
            case 2:
                scanf("%d", &t);
                if (t == 3 || t == 5 || t == 7) {
                    aplicarBlur(img, t);
                } else {
                    printf("Tamanho invalido. Use 3, 5 ou 7.\n");
                }
                break;
            case 3:
                aplicarMediana(img);
                break;
            case 4:
                espelharHorizontal(img);
                break;
            case 0:
                salvarImagem(img);
                break;
            default:
                printf("Opcao invalida.\n");
                break;
        }
    } while (opcao != 0);

    return 0;
}
```

### `H06-E06` *(Simulado Final Integrado — Sistema 5 Arquivos + Resumo via Ponteiros)*
Arquivos: [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_E06/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_E06/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_E06/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_E06/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_E06/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/H06_E06/main.c solucoes/H06_E06/imagem.c solucoes/H06_E06/funcoes.c -o prog
```
*(Os arquivos `imagem.h` e `imagem.c` são idênticos aos de `H06_E03_corrigido`.)*

**`funcoes.h`:**
```c
#ifndef FUNCOES_H
#define FUNCOES_H

#include "imagem.h"

void ajustarBrilho(int img[ALTURA][LARGURA], int b);
void aplicarBlur(int img[ALTURA][LARGURA], int t);
void ordenar(int v[], int n);
void aplicarMediana(int img[ALTURA][LARGURA]);
void limiarizar(int img[ALTURA][LARGURA], int limiar);
void resumoImagem(const int img[ALTURA][LARGURA], int *min, int *max, double *media);

#endif
```

**`funcoes.c`:**
```c
#include "funcoes.h"

void ajustarBrilho(int img[ALTURA][LARGURA], int b) {
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            int novo = img[i][j] + b;
            if (novo < 0) {
                novo = 0;
            } else if (novo > 255) {
                novo = 255;
            }
            img[i][j] = novo;
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
                    soma += img[i + a][j + b];
                }
            }
            aux[i][j] = soma / (t * t);
        }
    }

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            img[i][j] = aux[i][j];
        }
    }
}

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

void resumoImagem(const int img[ALTURA][LARGURA], int *min, int *max, double *media) {
    int mn = img[0][0];
    int mx = img[0][0];
    int soma = 0;

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (img[i][j] < mn) {
                mn = img[i][j];
            }
            if (img[i][j] > mx) {
                mx = img[i][j];
            }
            soma += img[i][j];
        }
    }
    *min = mn;
    *max = mx;
    *media = (double)soma / (ALTURA * LARGURA);
}
```

**`main.c`:**
```c
#include <stdio.h>
#include "imagem.h"
#include "funcoes.h"

int main(void) {
    static int img[ALTURA][LARGURA];
    int opcao, b, t, limiar;
    int min, max;
    double media;

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 1;
    }

    do {
        printf("===== PROCESSAMENTO DE IMAGENS =====\n");
        printf("1 - Ajustar brilho\n");
        printf("2 - Aplicar desfoque (blur)\n");
        printf("3 - Aplicar filtro da mediana\n");
        printf("4 - Aplicar limiarizacao\n");
        printf("0 - Salvar e sair\n");
        printf("Escolha uma opcao:\n");
        if (scanf("%d", &opcao) != 1) {
            return 1;
        }

        switch (opcao) {
            case 1:
                scanf("%d", &b);
                ajustarBrilho(img, b);
                break;
            case 2:
                scanf("%d", &t);
                if (t == 3 || t == 5 || t == 7) {
                    aplicarBlur(img, t);
                } else {
                    printf("Tamanho invalido. Use 3, 5 ou 7.\n");
                }
                break;
            case 3:
                aplicarMediana(img);
                break;
            case 4:
                scanf("%d", &limiar);
                if (limiar >= 0 && limiar <= 255) {
                    limiarizar(img, limiar);
                } else {
                    printf("Limiar invalido. Use 0 a 255.\n");
                }
                break;
            case 0:
                resumoImagem(img, &min, &max, &media);
                printf("Minimo: %d\n", min);
                printf("Maximo: %d\n", max);
                printf("Media: %.2f\n", media);
                salvarImagem(img);
                break;
            default:
                printf("Opcao invalida.\n");
                break;
        }
    } while (opcao != 0);

    return 0;
}
```

### `H06-OP1 [OPCIONAL]` *(Brilho Recursivo por Linhas)*
Arquivos: [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_OP1_opcional/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_OP1_opcional/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_OP1_opcional/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_OP1_opcional/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_OP1_opcional/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/H06_OP1_opcional/main.c solucoes/H06_OP1_opcional/imagem.c solucoes/H06_OP1_opcional/funcoes.c -o prog
```

**`funcoes.h`:**
```c
#ifndef FUNCOES_H
#define FUNCOES_H

#include "imagem.h"

void ajustarBrilhoLinhaRec(int img[ALTURA][LARGURA], int lin, int b);

#endif
```

**`funcoes.c`:**
```c
#include "funcoes.h"

void ajustarBrilhoLinhaRec(int img[ALTURA][LARGURA], int lin, int b) {
    if (lin == ALTURA) {
        return;
    }
    for (int j = 0; j < LARGURA; j++) {
        int novo = img[lin][j] + b;
        if (novo < 0) {
            novo = 0;
        } else if (novo > 255) {
            novo = 255;
        }
        img[lin][j] = novo;
    }
    ajustarBrilhoLinhaRec(img, lin + 1, b);
}
```

**`main.c`:**
```c
#include <stdio.h>
#include "imagem.h"
#include "funcoes.h"

int main(void) {
    static int img[ALTURA][LARGURA];
    int b;

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 1;
    }
    scanf("%d", &b);
    ajustarBrilhoLinhaRec(img, 0, b);
    salvarImagem(img);
    return 0;
}
```

### `H06-OP2 [OPCIONAL]` *(Módulo `estatisticas.h/.c` — 7 Arquivos)*
Arquivos: [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_OP2_opcional/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_OP2_opcional/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_OP2_opcional/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_OP2_opcional/funcoes.c) | [estatisticas.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_OP2_opcional/estatisticas.h) | [estatisticas.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_OP2_opcional/estatisticas.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_OP2_opcional/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/H06_OP2_opcional/main.c solucoes/H06_OP2_opcional/imagem.c solucoes/H06_OP2_opcional/funcoes.c solucoes/H06_OP2_opcional/estatisticas.c -o prog
```

**`estatisticas.h`:**
```c
#ifndef ESTATISTICAS_H
#define ESTATISTICAS_H

#include "imagem.h"

int minimoImagem(const int img[ALTURA][LARGURA]);
int maximoImagem(const int img[ALTURA][LARGURA]);
double mediaImagem(const int img[ALTURA][LARGURA]);

#endif
```

**`estatisticas.c`:**
```c
#include "estatisticas.h"

int minimoImagem(const int img[ALTURA][LARGURA]) {
    int mn = img[0][0];
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (img[i][j] < mn) {
                mn = img[i][j];
            }
        }
    }
    return mn;
}

int maximoImagem(const int img[ALTURA][LARGURA]) {
    int mx = img[0][0];
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (img[i][j] > mx) {
                mx = img[i][j];
            }
        }
    }
    return mx;
}

double mediaImagem(const int img[ALTURA][LARGURA]) {
    int soma = 0;
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            soma += img[i][j];
        }
    }
    return (double)soma / (ALTURA * LARGURA);
}
```

**`main.c`:**
```c
#include <stdio.h>
#include "imagem.h"
#include "funcoes.h"
#include "estatisticas.h"

int main(void) {
    static int img[ALTURA][LARGURA];
    int opcao, b, t;

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 1;
    }

    do {
        printf("===== PROCESSAMENTO DE IMAGENS =====\n");
        printf("1 - Ajustar brilho\n");
        printf("2 - Aplicar desfoque (blur)\n");
        printf("3 - Aplicar filtro da mediana\n");
        printf("4 - Exibir estatisticas\n");
        printf("0 - Salvar e sair\n");
        printf("Escolha uma opcao:\n");
        if (scanf("%d", &opcao) != 1) {
            return 1;
        }

        switch (opcao) {
            case 1:
                scanf("%d", &b);
                ajustarBrilho(img, b);
                break;
            case 2:
                scanf("%d", &t);
                if (t == 3 || t == 5 || t == 7) {
                    aplicarBlur(img, t);
                } else {
                    printf("Tamanho invalido. Use 3, 5 ou 7.\n");
                }
                break;
            case 3:
                aplicarMediana(img);
                break;
            case 4:
                printf("Minimo: %d\n", minimoImagem(img));
                printf("Maximo: %d\n", maximoImagem(img));
                printf("Media: %.2f\n", mediaImagem(img));
                break;
            case 0:
                salvarImagem(img);
                break;
            default:
                printf("Opcao invalida.\n");
                break;
        }
    } while (opcao != 0);

    return 0;
}
```

---

## 2. Gabarito da Checagem Independente Obrigatória (`H06-C01` a `H06-C03`)

### `H06-C01` *(Arguição Escrita + Teste de Mesa Combinado)*
1. - **(a)** Sem `#ifndef IMAGEM_H`, como `main.c` inclui `"imagem.h"` e `"funcoes.h"` (que também inclui `"imagem.h"`), o pré-processador cola o conteúdo de `imagem.h` duas vezes em `main.c`, podendo gerar redefinições/avisos; a guarda `#ifndef` impede a colagem repetida.
   - **(b)** Porque a média (`blur`) e a mediana (`3 x 3`) dependem dos valores originais dos vizinhos ao redor de `(i, j)`; gravando diretamente em `img[i][j]`, pixels já processados contaminariam o cálculo dos pixels seguintes e dificultariam a preservação das bordas.
   - **(c)** `int b` é passado **por valor** (cópia local na função — alterar `b` não muda o argumento na `main`); `int img[ALTURA][LARGURA]` passa o endereço do primeiro elemento do arranjo, permitindo que a função modifique os pixels da matriz original da `main`.
2. **`contar_pares_rec(v, 5)`** para `v = {4, 11, 7, 15, 2}`:
   - `contar_pares_rec(v, 5)` = `(2%2==0)` (`1`) + `contar_pares_rec(v, 4)`
   - `contar_pares_rec(v, 4)` = `0` + `contar_pares_rec(v, 3)`
   - `contar_pares_rec(v, 3)` = `0` + `contar_pares_rec(v, 2)`
   - `contar_pares_rec(v, 2)` = `0` + `contar_pares_rec(v, 1)`
   - `contar_pares_rec(v, 1)` = `(4%2==0)` (`1`) + `contar_pares_rec(v, 0)`
   - `contar_pares_rec(v, 0)` = `0`
   - **Retorno final:** **`2`**.

### `H06-C02` *(Modificação ao Vivo no Papel)*
1. **Em `funcoes.h`:**
   ```c
   void limiarizar(int img[ALTURA][LARGURA], int limiar);
   ```
2. **Em `funcoes.c`:**
   ```c
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
3. **Em `main.c` (`case 4:`):**
   ```c
   case 4:
       scanf("%d", &limiar);
       if (limiar >= 0 && limiar <= 255) {
           limiarizar(img, limiar);
       } else {
           printf("Limiar invalido. Use 0 a 255.\n");
       }
       break;
   ```

### `H06-C03` *(Projeto Integrado Verificado — 5 Arquivos com Negativo)*
Arquivos: [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_C03/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_C03/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_C03/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_C03/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H06_C03/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/H06_C03/main.c solucoes/H06_C03/imagem.c solucoes/H06_C03/funcoes.c -o prog
```
*(Os arquivos `imagem.h` e `imagem.c` são idênticos aos de `H06_E03_corrigido`.)*

**`funcoes.h`:**
```c
#ifndef FUNCOES_H
#define FUNCOES_H

#include "imagem.h"

void ajustarBrilho(int img[ALTURA][LARGURA], int b);
void aplicarBlur(int img[ALTURA][LARGURA], int t);
void ordenar(int v[], int n);
void aplicarMediana(int img[ALTURA][LARGURA]);
void aplicarNegativo(int img[ALTURA][LARGURA]);

#endif
```

**`funcoes.c`:**
```c
#include "funcoes.h"

void ajustarBrilho(int img[ALTURA][LARGURA], int b) {
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            int novo = img[i][j] + b;
            if (novo < 0) {
                novo = 0;
            } else if (novo > 255) {
                novo = 255;
            }
            img[i][j] = novo;
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
                    soma += img[i + a][j + b];
                }
            }
            aux[i][j] = soma / (t * t);
        }
    }

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            img[i][j] = aux[i][j];
        }
    }
}

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

void aplicarNegativo(int img[ALTURA][LARGURA]) {
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
    int opcao, b, t;

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 1;
    }

    do {
        printf("===== PROCESSAMENTO DE IMAGENS =====\n");
        printf("1 - Ajustar brilho\n");
        printf("2 - Aplicar desfoque (blur)\n");
        printf("3 - Aplicar filtro da mediana\n");
        printf("4 - Aplicar negativo\n");
        printf("0 - Salvar e sair\n");
        printf("Escolha uma opcao:\n");
        if (scanf("%d", &opcao) != 1) {
            return 1;
        }

        switch (opcao) {
            case 1:
                scanf("%d", &b);
                ajustarBrilho(img, b);
                break;
            case 2:
                scanf("%d", &t);
                if (t == 3 || t == 5 || t == 7) {
                    aplicarBlur(img, t);
                } else {
                    printf("Tamanho invalido. Use 3, 5 ou 7.\n");
                }
                break;
            case 3:
                aplicarMediana(img);
                break;
            case 4:
                aplicarNegativo(img);
                break;
            case 0:
                salvarImagem(img);
                break;
            default:
                printf("Opcao invalida.\n");
                break;
        }
    } while (opcao != 0);

    return 0;
}
```
