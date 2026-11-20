# Gabarito Comentado — Bloco `E07` (Imagens PGM P2, Saturação `[0, 255]`, `static` e Arranjos n-Dimensionais)

> **Bloco de referência:** [E07_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/blocos/E07_bloco.md)  
> **Nota para Caça ao Bug:** `E07-E03` e `E07-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`E07-E01` a `E07-E05`)

### `E07-E01` *(Teste de Mesa — Saturação, Limiarização e Array 3D)*
1. Para `img = {{10, 120, 240}, {0, 128, 255}, {45, 200, 180}}`:
   - **Brilho `delta = +30` com saturação `[0, 255]`:**
     `{{40, 150, 255}, {30, 158, 255}, {75, 230, 210}}`
     *(note que `240+30=270 -> 255` e `255+30=285 -> 255`)*.
   - **Limiarização sobre os originais com `L = 128`:**
     `{{0, 0, 255}, {0, 255, 255}, {0, 255, 255}}`
     *(note que `128 >= 128` resulta em `255`)*.
2. Para `int cubo[2][3][4];`:
   - Total de inteiros: `2 * 3 * 4 = 24` inteiros.
   - Índices válidos: `p` em `0..1`, `i` em `0..2`, `j` em `0..3`; último elemento válido: **`cubo[1][2][3]`**.

### `E07-E02` *(Completar solução)*
- **`/* A */`:** `static`
- **`/* B */`:** `img[i][j] > 255`
- **`/* C */`:** `img[i][j] < limiar`
- **`/* D */`:** `img[i][j] = 255`

### `E07-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. Na leitura, os laços usam `i < largura` e `j < altura`, invertendo linhas e colunas da imagem. Correto: `for (int i = 0; i < altura; i++)` e `for (int j = 0; j < largura; j++)`.
  2. `img[i][j] = (img[i][j] + delta) % 256;` faz módulo aritmético (estoura branco para preto escuro e falha com negativos) em vez de saturação `[0, 255]`. Correto: somar `delta` e recortar `< 0 -> 0` e `> 255 -> 255`.
  3. O cabeçalho de saída `printf("P2\n%d %d\n", largura, altura);` omite a linha com o valor máximo **`255`** exigida pelo formato PGM P2. Correto: `printf("P2\n%d %d\n255\n", largura, altura);`.
- **Solução corrigida completa:** [E07_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E07_E03_corrigido.c)
```c
#include <stdio.h>
#define ALTURA_MAX 500
#define LARGURA_MAX 500

int main(void) {
    static int img[ALTURA_MAX][LARGURA_MAX];
    int largura, altura, maxval, delta;

    scanf("%d %d %d", &largura, &altura, &maxval);
    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            scanf("%d", &img[i][j]);
        }
    }
    scanf("%d", &delta);

    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            img[i][j] += delta;
            if (img[i][j] < 0) {
                img[i][j] = 0;
            } else if (img[i][j] > 255) {
                img[i][j] = 255;
            }
        }
    }

    printf("P2\n%d %d\n255\n", largura, altura);
    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", img[i][j]);
        }
        printf("\n");
    }
    return 0;
}
```

### `E07-E04` *(Programa completo — Brilho com saturação e limiarização)*
Arquivo: [E07_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E07_E04.c)
```c
#include <stdio.h>
#define ALTURA_MAX 500
#define LARGURA_MAX 500

int main(void) {
    static int img[ALTURA_MAX][LARGURA_MAX];
    int largura, altura, delta, limiar;

    scanf("%d %d", &largura, &altura);
    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            scanf("%d", &img[i][j]);
        }
    }
    scanf("%d %d", &delta, &limiar);

    int pretos = 0, brancos = 0;
    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            img[i][j] += delta;
            if (img[i][j] < 0) {
                img[i][j] = 0;
            } else if (img[i][j] > 255) {
                img[i][j] = 255;
            }

            if (img[i][j] < limiar) {
                img[i][j] = 0;
                pretos++;
            } else {
                img[i][j] = 255;
                brancos++;
            }
        }
    }

    printf("P2\n%d %d\n255\n", largura, altura);
    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", img[i][j]);
        }
        printf("\n");
    }
    printf("Pretos: %d Brancos: %d\n", pretos, brancos);
    return 0;
}
```

### `E07-E05` *(Programa completo — Volume 3D com saturação por camada)*
Arquivo: [E07_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E07_E05.c)
```c
#include <stdio.h>
#define MAX_P 10
#define MAX_L 10
#define MAX_C 10

int main(void) {
    static int cubo[MAX_P][MAX_L][MAX_C];
    int P, L, C, delta;

    scanf("%d %d %d", &P, &L, &C);
    for (int p = 0; p < P; p++) {
        for (int i = 0; i < L; i++) {
            for (int j = 0; j < C; j++) {
                scanf("%d", &cubo[p][i][j]);
            }
        }
    }
    scanf("%d", &delta);

    int total = 0, saturados = 0;
    for (int p = 0; p < P; p++) {
        int soma_camada = 0;
        for (int i = 0; i < L; i++) {
            for (int j = 0; j < C; j++) {
                cubo[p][i][j] += delta;
                if (cubo[p][i][j] < 0) {
                    cubo[p][i][j] = 0;
                } else if (cubo[p][i][j] > 255) {
                    cubo[p][i][j] = 255;
                }
                if (cubo[p][i][j] == 0 || cubo[p][i][j] == 255) {
                    saturados++;
                }
                soma_camada += cubo[p][i][j];
            }
        }
        total += soma_camada;
        printf("Camada %d: soma = %d\n", p, soma_camada);
    }
    printf("Total geral: %d\n", total);
    printf("Saturados (0 ou 255): %d\n", saturados);
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`E07-C01` a `E07-C03`)

### `E07-C01` *(Análise de Saturação, `static` e Arranjo 3D)*
1. Para `{0, 40, 127, 128, 250}`:
   - Após `delta = -50` com saturação `[0, 255]`: **`{0, 0, 77, 78, 200}`**.
   - Limiarização nos originais com `L = 128`: **`{0, 0, 0, 255, 255}`**.
2. `int img[1024][1024];` consome `1024 * 1024 * 4 = 4 MB` (ou mais em outras resoluções). Como variáveis locais ficam na pilha (*stack*), matrizes grandes podem causar *stack overflow* (falha de segmentação); `static` move a alocação para a memória estática e evita o estouro.
3. `4 * 5 * 6 = 120` inteiros no total; o último índice válido é **`vol[3][4][5]`**.

### `E07-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. Na leitura, os laços usam `i < largura` e `j < altura` invertidos. Correto: `i < altura` e `j < largura`.
  2. `else if (img[i][j] > limiar)` omite o caso exato **`img[i][j] == limiar`**, deixando esse pixel com seu valor original em vez de `255`. Correto: usar `else { img[i][j] = 255; }`.
  3. `printf("P2\n%d %d\n255\n", altura, largura);` imprime `altura` antes de `largura` no cabeçalho PGM P2. Correto: `largura` primeiro, depois `altura`.
- **Solução corrigida completa:** [E07_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E07_C02_corrigido.c)
```c
#include <stdio.h>
#define ALTURA_MAX 500
#define LARGURA_MAX 500

int main(void) {
    static int img[ALTURA_MAX][LARGURA_MAX];
    int largura, altura, limiar;

    scanf("%d %d", &largura, &altura);
    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            scanf("%d", &img[i][j]);
        }
    }
    scanf("%d", &limiar);

    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            if (img[i][j] < limiar) {
                img[i][j] = 0;
            } else {
                img[i][j] = 255;
            }
        }
    }

    printf("P2\n%d %d\n255\n", largura, altura);
    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", img[i][j]);
        }
        printf("\n");
    }
    return 0;
}
```

### `E07-C03` *(Programa completo — Brilho, contagem acima do limiar e média)*
Arquivo: [E07_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E07_C03.c)
```c
#include <stdio.h>
#define ALTURA_MAX 500
#define LARGURA_MAX 500

int main(void) {
    static int img[ALTURA_MAX][LARGURA_MAX];
    int largura, altura, delta, limiar;

    scanf("%d %d", &largura, &altura);
    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            scanf("%d", &img[i][j]);
        }
    }
    scanf("%d %d", &delta, &limiar);

    int acima = 0;
    long long soma = 0;
    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            img[i][j] += delta;
            if (img[i][j] < 0) {
                img[i][j] = 0;
            } else if (img[i][j] > 255) {
                img[i][j] = 255;
            }
            if (img[i][j] >= limiar) {
                acima++;
            }
            soma += img[i][j];
        }
    }

    double media = (double)soma / (largura * altura);
    printf("P2\n%d %d\n255\n", largura, altura);
    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", img[i][j]);
        }
        printf("\n");
    }
    printf("Acima ou igual ao limiar: %d\n", acima);
    printf("Media: %.2f\n", media);
    return 0;
}
```
