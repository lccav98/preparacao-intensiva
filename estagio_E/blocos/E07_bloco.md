# Bloco `E07` — Matrizes como Imagens em Tons de Cinza (PGM P2), Saturação `[0, 255]`, `static` e Generalização n-Dimensional

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio E — Matrizes Bidimensionais e Processamento Matricial / **`E07`** |
| **Micro-habilidade foco** | Processar matrizes de pixels em escala de cinza `[0, 255]` (ajuste de brilho com saturação e limiarização *in-place* no formato PGM P2), empregando `static` para matrizes grandes e generalizando a indexação para arranjos n-dimensionais. |
| **Pré-requisitos** | `E02` *(Percurso Completo, Soma Total, Busca 2D e Extremos com Coordenadas)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão única de prática + checagem (24 min):** `14 min` resol. \| `6 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Não utilize** funções próprias além de `int main(void)`, VLAs (`int img[alt][larg];`), `struct`, alocação dinâmica (`malloc`/`free`) ou manipulação de arquivos `FILE*` (entrada/saída textual PGM P2 via `stdin`/`stdout`). Use constantes `#define` e matrizes de capacidade fixa. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Imagens PGM P2 e ordem `(largura, altura)`:**
   - Uma imagem em tons de cinza é uma matriz `img[ALTURA][LARGURA]` de inteiros em **`[0, 255]`** (`0` = preto absoluto, `255` = branco absoluto).
   - **Atenção crítica:** o cabeçalho textual do formato **PGM P2** traz:
     1) a assinatura `P2`,
     2) **`largura` (colunas) seguida de `altura` (linhas)**,
     3) o valor máximo `255`,
     4) os pixels linha por linha (`for (int i = 0; i < altura; i++) for (int j = 0; j < largura; j++)`).
2. **Saturação (*clamping*) `[0, 255]` e limiarização:**
   - Ao ajustar brilho somando `delta`: se `img[i][j] < 0`, fixe em `0`; se `img[i][j] > 255`, fixe em `255`. **Nunca** use `% 256` (um pixel `250 + 20 = 270` viraria `14`, preto escuro!).
   - Na **limiarização** com limiar `L`: pixels com `img[i][j] < L` recebem `0`; pixels com `img[i][j] >= L` (inclusive `== L`!) recebem `255`.
3. **Palavra-chave `static` em matrizes grandes:**
   - Matrizes declaradas localmente em `main` ficam na pilha (*stack*), que tem capacidade limitada (~8 MB no Linux). Para matrizes grandes (ex.: `static int img[500][500];` ou `[600][800]`), use **`static`** para alocá-las na área estática de memória e evitar estouro de pilha (*stack overflow*).
4. **Generalização n-dimensional (Ementa item 8):**
   - A sintaxe de matrizes estende-se para 3 ou mais dimensões: `int cubo[P][L][C];` armazena `P * L * C` inteiros contíguos (o último índice varia mais rápido), acessados por `cubo[p][i][j]` em 3 laços aninhados.

---

## 2. Exemplos Guiados

### Exemplo 1 — Saturação `[0, 255]` vs. limiarização *(Trecho ilustrativo)*
Para a linha de pixels `{10, 127, 128, 240}`:
- **Brilho `delta = +30` com saturação:**  
  `10+30 = 40`, `127+30 = 157`, `128+30 = 158`, `240+30 = 270 -> 255` (saturado!).
- **Limiarização sobre os originais com `L = 128`:**  
  `10 < 128 -> 0`, `127 < 128 -> 0`, `128 >= 128 -> 255`, `240 >= 128 -> 255`.

### Exemplo 2 — Brilho com saturação e `static` em PGM P2 *(Programa completo)*
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

---

## 3. Exercícios (`E07-E01` a `E07-E05`)

### `E07-E01` *(Teste de Mesa — Saturação, Limiarização e Array 3D)*
Sem usar computador, resolva:
1. Considere a imagem `3 x 3` abaixo (`largura = 3`, `altura = 3`):
   `img = {{10, 120, 240}, {0, 128, 255}, {45, 200, 180}}`
   - Calcule a matriz resultante após aplicar brilho `delta = +30` com saturação `[0, 255]`.
   - A partir da **matriz original**, calcule a matriz resultante após limiarização com `L = 128` (`< 128 -> 0`, `>= 128 -> 255`).
2. Para o arranjo tridimensional `int cubo[2][3][4];`, informe:
   - Quantos inteiros ele armazena ao todo?
   - Quais são os índices válidos de `[p][i][j]` e qual é o último elemento válido?

---

### `E07-E02` *(Completar solução)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` do trecho abaixo que declara uma imagem grande na área estática, aplica brilho `delta` com saturação `[0, 255]` e em seguida aplica limiarização com limiar `limiar`:

```c
/* A */ int img[500][500];

for (int i = 0; i < altura; i++) {
    for (int j = 0; j < largura; j++) {
        img[i][j] += delta;
        if (img[i][j] < 0) {
            img[i][j] = 0;
        } else if ( /* B */ ) {
            img[i][j] = 255;
        }

        if ( /* C */ ) {
            img[i][j] = 0;
        } else {
            /* D */ ;
        }
    }
}
```

---

### `E07-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler `largura`, `altura`, `maxval`, os `altura * largura` pixels da imagem (`1 <= largura, altura <= 500`) e `delta`, aplicar brilho `delta` com saturação `[0, 255]` e imprimir a saída no formato PGM P2 (`P2`, `<largura> <altura>`, `255` e pixels). Identifique os **3 bugs intencionais** e escreva a versão corrigida completa:

```c
#include <stdio.h>
#define ALTURA_MAX 500
#define LARGURA_MAX 500

int main(void) {
    static int img[ALTURA_MAX][LARGURA_MAX];
    int largura, altura, maxval, delta;

    scanf("%d %d %d", &largura, &altura, &maxval);
    for (int i = 0; i < largura; i++) {
        for (int j = 0; j < altura; j++) {
            scanf("%d", &img[i][j]);
        }
    }
    scanf("%d", &delta);

    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            img[i][j] = (img[i][j] + delta) % 256;
        }
    }

    printf("P2\n%d %d\n", largura, altura);
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

---

### `E07-E04` *(Variação controlada com pistas)*
Escreva um **programa completo** em C99 que leia `largura` e `altura` (`1 <= largura, altura <= 500`), os pixels (`0..255`) para `static int img[ALTURA_MAX][LARGURA_MAX];`, e dois inteiros `delta` e `limiar`.
1. Primeiro aplique o ajuste de brilho `delta` com saturação `[0, 255]`.
2. Em seguida, aplique limiarização (`< limiar -> 0`, `>= limiar -> 255`), contando quantos pixels resultaram pretos (`0`) e quantos resultaram brancos (`255`).

Imprima exatamente:
```text
P2
<largura> <altura>
255
<altura linhas com largura pixels separados por espaco simples>
Pretos: P Brancos: B
```
*Pista:* Após ler `largura` e `altura`, os laços de leitura, processamento e exibição devem usar `i < altura` no laço externo e `j < largura` no laço interno.

---

### `E07-E05` *(Resolução independente)*
Escreva um **programa completo** em C99 sobre um volume 3D de intensidades (`0..255`): leia `P`, `L` e `C` (`1 <= P, L, C <= 10`) e os `P * L * C` inteiros para `static int cubo[10][10][10];`, seguidos de um ajuste inteiro `delta`. Para cada camada `p = 0 .. P - 1`, some `delta` a cada voxel `cubo[p][i][j]` aplicando saturação `[0, 255]`, calcule a soma dos valores da camada `p` e conte quantos voxels ao todo ficaram exatamente nos extremos saturados (`0` ou `255`). Imprima exatamente:
```text
Camada 0: soma = S0
...
Camada P-1: soma = Sk
Total geral: T
Saturados (0 ou 255): Q
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `E07-C01` *(Análise de Saturação, `static` e Arranjo 3D)*
1. Dada a linha de pixels `{0, 40, 127, 128, 250}`:
   - Quais são os valores resultantes após brilho `delta = -50` com saturação `[0, 255]`?
   - A partir dos pixels **originais**, quais são os valores após limiarização com `L = 128`?
2. Por que uma imagem de alta resolução como `static int img[1024][1024];` deve usar `static` em vez de ser declarada como variável local comum dentro de `main`?
3. Em `int vol[4][5][6];`, quantos inteiros há no total e qual é o último índice válido `vol[p][i][j]`?

### `E07-C02` *(Caça ao Bug — Programa completo)*
O programa abaixo deveria ler `largura`, `altura`, os pixels em `static int img[ALTURA_MAX][LARGURA_MAX];` e um `limiar`, aplicar limiarização (`< limiar -> 0`, `>= limiar -> 255`) e imprimir no formato PGM P2 (`P2`, `<largura> <altura>`, `255` e pixels). Corrija todos os defeitos presentes:

```c
#include <stdio.h>
#define ALTURA_MAX 500
#define LARGURA_MAX 500

int main(void) {
    static int img[ALTURA_MAX][LARGURA_MAX];
    int largura, altura, limiar;

    scanf("%d %d", &largura, &altura);
    for (int i = 0; i < largura; i++) {
        for (int j = 0; j < altura; j++) {
            scanf("%d", &img[i][j]);
        }
    }
    scanf("%d", &limiar);

    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            if (img[i][j] < limiar) {
                img[i][j] = 0;
            } else if (img[i][j] > limiar) {
                img[i][j] = 255;
            }
        }
    }

    printf("P2\n%d %d\n255\n", altura, largura);
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

### `E07-C03` *(Programa completo independente)*
Escreva um programa completo em C99 que leia `largura`, `altura` (`1 <= largura, altura <= 500`), os pixels (`0..255`) em `static int img[ALTURA_MAX][LARGURA_MAX];`, e os inteiros `delta` e `limiar`. Aplique brilho `delta` com saturação `[0, 255]`, conte quantos pixels resultantes ficaram `>= limiar` e calcule a média dos pixels após o brilho (`%.2f`). Imprima exatamente:
```text
P2
<largura> <altura>
255
<altura linhas com largura pixels separados por espaco simples>
Acima ou igual ao limiar: K
Media: M.MM
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `E08` (`Revisão e Consolidação do Estágio E`):** somente após autocorreção de `E07-E01..E05` e **100% (3/3)** em `E07-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** revisar a ordem `largura` (colunas) × `altura` (linhas) no PGM P2, o recorte `if (< 0) 0; else if (> 255) 255;` e a borda exata `>= limiar`; aplicar variante `V2` de `E07`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`E02`** (percurso completo de matriz 2D) e **`B04`/`B05`** (condicionais de intervalo e fronteiras exatas).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 8 — matrizes n-dimensionais).
- `[DOC]` `Aula_14_Algoritmos.pdf` p. 23–24 e `Aula_15_Algoritmos.pdf` p. 21 (representação de imagens).
- `[DOC]` `Lista9_Algoritmos.pdf` p. 3 (Ex. 8 — `processa_imagem.c` / `utfpr.pgm`).
- `[DOC]` `Trabalho_Algoritmos.pdf` p. 1–2 (formato PGM P2 e uso de `static`).
- Casos de teste e soluções verificáveis: [E07_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/gabaritos/E07_gabarito.md) e [E07_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/E07_testes.md).
