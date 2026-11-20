# Gabarito Comentado — Bloco `H05` (Menu Interativo `do-while` + `switch` e Validação)

> **Bloco de referência:** [H05_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/blocos/H05_bloco.md)  
> **Nota para Caça ao Bug:** `H05-E03` no bloco do aluno contém **3 erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`H05-E01` a `H05-E06`)

### `H05-E01` *(Teste de Mesa — Operações Sucessivas sobre o Estado Atual)*
- **(a) Após opção `1` (`b = 30`, saturação `[0, 255]`):**
  ```text
  255  130  120
  110  255  140
  100  125  115
  ```
- **(b) Após opção `3` (mediana `3 x 3`):**
  - Vetor extraído de `(1, 1)`: `{255, 130, 120, 110, 255, 140, 100, 125, 115}`
  - Ordenado: `{100, 110, 115, 120, 125, 130, 140, 255, 255}` $\rightarrow$ `v[4] = 125`.
  - Matriz resultante (bordas intactas):
    ```text
    255  130  120
    110  125  140
    100  125  115
    ```
- **(c) Após opção `2` (`t = 3`, blur) e opção `0` (salvar e sair):**
  - Soma da janela `3 x 3`: `255 + 130 + 120 + 110 + 125 + 140 + 100 + 125 + 115 = 1220`.
  - Média inteira: `1220 / 9 = 135`.
  - Borda `(0, 0)`: **`255`** (inalterado pela mediana e pelo blur). Pixel central `(1, 1)`: **`135`**.
  - Matriz final salva:
    ```text
    255  130  120
    110  135  140
    100  125  115
    ```

### `H05-E02` *(Completar Solução)*
- **`/* A */`:** `!lerImagem(img)` *(ou `lerImagem(img) == 0`)*
- **`/* B */`:** `do`
- **`/* C */`:** `t == 3 || t == 5 || t == 7`
- **`/* D */`:** `break;`
- **`/* E */`:** `opcao != 0`

### `H05-E03` *(Caça ao Bug em Projeto 5-Arquivos — Erros intencionais no enunciado)*
- **Erros intencionais em `main.c`:**
  1. `if (!lerImagem(img))` está **dentro** do `do-while`: além de tentar reler a imagem a cada iteração (apagando filtros anteriores ou falhando no `stdin`), deveria executar **uma única vez antes do laço**.
  2. Falta `break;` no `case 1`: após ajustar o brilho, o fluxo cai diretamente no `case 2` (*fall-through* acidental).
  3. Ausência de validação para `t` no `case 2`: aceita valores diferentes de `3, 5, 7` (como `4` ou `-1`), causando bordas/divisões erradas.
- **Arquivos corrigidos:** [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H05_E03_corrigido/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H05_E03_corrigido/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H05_E03_corrigido/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H05_E03_corrigido/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H05_E03_corrigido/main.c)
- **Comando GCC:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/H05_E03_corrigido/main.c solucoes/H05_E03_corrigido/imagem.c solucoes/H05_E03_corrigido/funcoes.c -o prog
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
```

**`main.c`:**
```c
#include <stdio.h>
#include "imagem.h"
#include "funcoes.h"

int main(void) {
    static int img[ALTURA][LARGURA];
    int opcao, b, t;

    // Bug 1 corrigido: ler a imagem uma unica vez antes do menu para nao apagar filtros anteriores
    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 1;
    }

    do {
        printf("===== PROCESSAMENTO DE IMAGENS =====\n");
        printf("1 - Ajustar brilho\n");
        printf("2 - Aplicar desfoque (blur)\n");
        printf("3 - Aplicar filtro da mediana\n");
        printf("0 - Salvar e sair\n");
        printf("Escolha uma opcao:\n");
        if (scanf("%d", &opcao) != 1) {
            return 1;
        }

        switch (opcao) {
            case 1:
                scanf("%d", &b);
                ajustarBrilho(img, b);
                // Bug 2 corrigido: break obrigatorio para nao cair no case 2 (fall-through)
                break;
            case 2:
                scanf("%d", &t);
                // Bug 3 corrigido: validar t estritamente em {3, 5, 7}
                if (t == 3 || t == 5 || t == 7) {
                    aplicarBlur(img, t);
                } else {
                    printf("Tamanho invalido. Use 3, 5 ou 7.\n");
                }
                break;
            case 3:
                aplicarMediana(img);
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

### `H05-E04` *(Projeto 5-Arquivos — Sistema Completo `7 x 7`)*
Arquivos: [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H05_E04/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H05_E04/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H05_E04/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H05_E04/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H05_E04/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/H05_E04/main.c solucoes/H05_E04/imagem.c solucoes/H05_E04/funcoes.c -o prog
```
*(Os arquivos `imagem.h`, `imagem.c`, `funcoes.h` e `funcoes.c` são idênticos aos de `H05_E03_corrigido`.)*

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

### `H05-E05` *(Projeto 5-Arquivos — Menu com Contador de Operações)*
Arquivos: [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H05_E05/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H05_E05/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H05_E05/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H05_E05/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H05_E05/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/H05_E05/main.c solucoes/H05_E05/imagem.c solucoes/H05_E05/funcoes.c -o prog
```
*(Os arquivos `imagem.h`, `imagem.c`, `funcoes.h` e `funcoes.c` são idênticos aos de `H05_E03_corrigido`.)*

**`main.c`:**
```c
#include <stdio.h>
#include "imagem.h"
#include "funcoes.h"

int main(void) {
    static int img[ALTURA][LARGURA];
    int opcao, b, t;
    int ops = 0;

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 1;
    }

    do {
        printf("===== PROCESSAMENTO DE IMAGENS =====\n");
        printf("1 - Ajustar brilho\n");
        printf("2 - Aplicar desfoque (blur)\n");
        printf("3 - Aplicar filtro da mediana\n");
        printf("0 - Salvar e sair\n");
        printf("Escolha uma opcao:\n");
        if (scanf("%d", &opcao) != 1) {
            return 1;
        }

        switch (opcao) {
            case 1:
                scanf("%d", &b);
                ajustarBrilho(img, b);
                ops++;
                break;
            case 2:
                scanf("%d", &t);
                if (t == 3 || t == 5 || t == 7) {
                    aplicarBlur(img, t);
                    ops++;
                } else {
                    printf("Tamanho invalido. Use 3, 5 ou 7.\n");
                }
                break;
            case 3:
                aplicarMediana(img);
                ops++;
                break;
            case 0:
                printf("Operacoes aplicadas: %d\n", ops);
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

### `H05-E06` *(Projeto 5-Arquivos — Menu Estendido com Limiarização)*
Arquivos: [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H05_E06/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H05_E06/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H05_E06/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H05_E06/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H05_E06/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/H05_E06/main.c solucoes/H05_E06/imagem.c solucoes/H05_E06/funcoes.c -o prog
```
*(Os arquivos `imagem.h` e `imagem.c` são idênticos aos de `H05_E03_corrigido`.)*

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

---

## 2. Gabarito da Checagem Independente (`H05-C01` a `H05-C03`)

### `H05-C01` *(Teste de Mesa sem Computador)*
1. **Após `1` (`b = -40`):**
   ```text
    0   40   50
   30  215   60
   20   45   55
   ```
2. **Após `3` (mediana):** vetor ordenado `{0, 20, 30, 40, 45, 50, 55, 60, 215}` $\rightarrow$ `(1, 1) = 45` e borda `(0, 0) = 0`.
3. **Após `2` (`t = 3`, blur):** soma `0 + 40 + 50 + 30 + 45 + 60 + 20 + 45 + 55 = 345`, `345 / 9 = 38`.
   ```text
    0   40   50
   30   38   60
   20   45   55
   ```

### `H05-C02` *(Diagnóstico sem Compilar)*
1. **`lerImagem(img)` está dentro do `do-while` (e sem checar retorno):** recarrega a imagem a cada ciclo apagando filtros anteriores. Deve ficar **antes** do `do-while` com `if (!lerImagem(img)) return 1;`.
2. **Sem validação de `t` no `case 2`:** aceita qualquer inteiro fora de `{3, 5, 7}`. Correção: `if (t == 3 || t == 5 || t == 7) aplicarBlur(img, t);`.
3. **Condição invertida `while (opcao == 0)` e ausência de `default`:** o laço encerra quando `opcao != 0` em vez de repetir até `0`. Correção: `} while (opcao != 0);` e incluir `default:` para opções inválidas.

### `H05-C03` *(Projeto 5-Arquivos Independente — Menu Completo)*
Arquivos: [imagem.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H05_C03/imagem.h) | [imagem.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H05_C03/imagem.c) | [funcoes.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H05_C03/funcoes.h) | [funcoes.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H05_C03/funcoes.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/solucoes/H05_C03/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/H05_C03/main.c solucoes/H05_C03/imagem.c solucoes/H05_C03/funcoes.c -o prog
```
*(Todos os 5 arquivos coincidem com a estrutura canônica de `H05_E04`.)*
