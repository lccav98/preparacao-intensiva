# Bloco `E08` — Revisão e Consolidação do Estágio E *(Bloco de Revisão)*

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio E — Matrizes Bidimensionais e Processamento Matricial / **`E08`** |
| **Micro-habilidade foco** | *(Revisão integrada de `E01` a `E07`)* Combinar fatiamento, somas por linha/coluna, diagonais, transposição, simetria, multiplicação matricial e processamento de pixels `[0, 255]` sem acesso fora dos limites. |
| **Pré-requisitos** | `E06` *(Multiplicação de Matrizes — Triplo Laço Aninhado)* e `E07` *(Imagens PGM P2, Saturação `[0, 255]`, `static` e Arranjos n-Dimensionais)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 22 min):** `14 min` resol. \| `5 min` corr. \| `3 min` recup.; **Sessão 2 (`E04`–`E06`, 22 min):** `14 min` resol. \| `5 min` corr. \| `3 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Conteúdo novo: NENHUM.** **É terminantemente proibido** o uso de funções customizadas além de `int main(void)`, VLAs (`int m[l][c];`), `struct`, alocação dinâmica (`malloc`/`free`) ou `FILE*`. Use estritamente C99 com matrizes de capacidade fixa e saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Apto para Estágio F`)

---

## 1. Instruções Curtas (Matriz de Consolidação do Estágio E)

1. **Armazenamento, busca 2D e extremos (`E01`–`E02`):**
   - Índices válidos em `m[L][C]`: `0 <= i < L` (linhas) e `0 <= j < C` (colunas).
   - Inicialize `maior`/`menor` com `m[0][0]` e `(0, 0)` — nunca com `0`.
   - Em busca 2D da 1ª ocorrência, use `break` no laço interno **combinado** com `&& li == -1` na condição do laço externo.
2. **Fatiamento, somas e diagonais (`E03`–`E04`):**
   - Somas por linha: `i` externo, `j` interno, zerando `soma = 0` dentro de `i`. Somas por coluna: `j` externo, `i` interno, zerando `soma = 0` dentro de `j`.
   - Em matriz quadrada `N x N`: diagonal principal (`i == j`), diagonal secundária (`i + j == N - 1`), acima da principal (`j > i`), abaixo da principal (`i > j`). Identidade exige `1` na diagonal **e** `0` fora dela.
3. **Transposta, simetria e multiplicação (`E05`–`E06`):**
   - Transposta de `A[L][C]` exige `T[C][L]` com `T[j][i] = A[i][j]` (sem transpor *in-place* em matriz retangular). Simetria exige `L == C` e `A[i][j] == A[j][i]`.
   - Produto `A[LA][CA] * B[LB][CB]` exige `CA == LB`, produz `C[LA][CB]`, zera `C[i][j] = 0;` antes do laço `k`, e acumula `A[i][k] * B[k][j]`.
4. **Imagens PGM P2, saturação e `static` (`E07`):**
   - Ordem PGM P2: `P2`, `largura` (colunas) `altura` (linhas), `255`.
   - Saturação `[0, 255]`: `< 0 -> 0`, `> 255 -> 255`. Limiarização: `< L -> 0`, `>= L -> 255`. Matrizes grandes usam `static`.

---

## 2. Exemplos Guiados

### Exemplo 1 — Triplo laço + verificação de simetria *(Revisão `E05` + `E06`)*
Para `C = A * B` (`LA x CB`):
```c
for (int i = 0; i < LA; i++) {
    for (int j = 0; j < CB; j++) {
        C[i][j] = 0;
        for (int k = 0; k < CA; k++) {
            C[i][j] += A[i][k] * B[k][j];
        }
    }
}
```
Se `LA == CB`, pode-se verificar em seguida se `C` é simétrica testando `C[i][j] != C[j][i]` para `j > i`.

### Exemplo 2 — Saturação `[0, 255]` e limiarização em `static` *(Revisão `E07`)*
```c
static int img[500][500];
/* Apos brilho delta: */
img[i][j] += delta;
if (img[i][j] < 0) img[i][j] = 0;
else if (img[i][j] > 255) img[i][j] = 255;
/* Limiarizacao com limiar L: */
img[i][j] = (img[i][j] < L) ? 0 : 255;
```

---

## 3. Exercícios (`E08-E01` a `E08-E06`)

### Sessão 1 (`E08-E01` a `E08-E03` — Rastreamento e Caça aos Bugs Integrados)

### `E08-E01` *(Teste de Mesa Integrado — Diagonais, Produto Parcial e Saturação)*
Sem usar computador, resolva:
1. Dada a matriz $M_{3 \times 3} = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$:
   calcule a soma da diagonal principal (`i == j`), a soma da diagonal secundária (`i + j == 2`) e a soma da região estritamente acima da diagonal principal (`j > i`).
2. Dadas $A_{2 \times 2} = \begin{pmatrix} 2 & -1 \\ 0 & 3 \end{pmatrix}$ e $B_{2 \times 2} = \begin{pmatrix} 4 & 5 \\ 1 & -2 \end{pmatrix}$, calcule o elemento `C[0][1]` de $C = A \cdot B$.
3. Para um pixel `p = 210` após ajuste de brilho `delta = +70` com saturação `[0, 255]`, qual valor fica armazenado e qual é o resultado ao aplicar limiarização com `L = 255`?

---

### `E08-E02` *(Caça ao Bug 1 — Somas por Coluna, Extremos e Identidade)*
O programa completo abaixo deveria ler `N` (`1 <= N <= 20`) e uma matriz `A` (`N x N`), imprimir a soma de cada coluna (`Coluna j: S`), o maior valor com coordenadas da 1ª ocorrência (`Maior: V em (li, co)`) e se `A` é matriz identidade (`Identidade: Sim` ou `Nao`). Identifique os **3 bugs intencionais** e escreva a versão corrigida completa:

```c
#include <stdio.h>
#define MAX 20

int main(void) {
    int N, A[MAX][MAX];
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    int soma = 0;
    for (int j = 0; j < N; j++) {
        for (int i = 0; i < N; i++) {
            soma += A[i][j];
        }
        printf("Coluna %d: %d\n", j, soma);
    }

    int maior = 0, li = 0, co = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (A[i][j] > maior) {
                maior = A[i][j];
                li = i;
                co = j;
            }
        }
    }
    printf("Maior: %d em (%d, %d)\n", maior, li, co);

    int id = 1;
    for (int i = 0; i < N; i++) {
        if (A[i][i] != 1) {
            id = 0;
            break;
        }
    }
    printf("Identidade: %s\n", id ? "Sim" : "Nao");
    return 0;
}
```

---

### `E08-E03` *(Caça ao Bug 2 — Brilho `[0, 255]` e Transposta PGM P2)*
O programa completo abaixo deveria ler `largura`, `altura` (`1 <= largura, altura <= 200`), os pixels (`0..255`) em `static int img[200][200];` e um ajuste `delta`. Deve aplicar brilho `delta` com saturação `[0, 255]`, construir a matriz transposta `T` (`largura` linhas × `altura` colunas) e imprimir a imagem transposta no formato PGM P2 (`P2`, `<nova_largura> <nova_altura>`, `255` e pixels). Identifique os **3 bugs intencionais** e escreva a versão corrigida completa:

```c
#include <stdio.h>
#define MAX_DIM 200

int main(void) {
    static int img[MAX_DIM][MAX_DIM];
    static int T[MAX_DIM][MAX_DIM];
    int largura, altura, delta;

    scanf("%d %d", &largura, &altura);
    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            scanf("%d", &img[i][j]);
        }
    }
    scanf("%d", &delta);

    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            img[i][j] += delta;
            if (img[i][j] > 255) {
                img[i][j] = 255;
            }
            T[i][j] = img[i][j];
        }
    }

    printf("P2\n%d %d\n255\n", largura, altura);
    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", T[i][j]);
        }
        printf("\n");
    }
    return 0;
}
```

---

### Sessão 2 (`E08-E04` a `E08-E06` — Implementação Integrada Independente)

### `E08-E04` *(Integração 1 — Somas por Linha/Coluna, Diagonais e Regiões Triangulares)*
Escreva um programa completo em C99 ([E08_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E08_E04.c)) que leia `N` (`1 <= N <= 20`) e uma matriz quadrada `A` (`N x N`). Calcule e imprima exatamente:
```text
Somas linhas: s0 s1 ...
Somas colunas: c0 c1 ...
Diagonal principal: DP
Diagonal secundaria: DS
Acima principal: U
Abaixo principal: D
```

---

### `E08-E05` *(Integração 2 — Produto Matricial, Simetria e Busca 2D)*
Escreva um programa completo em C99 ([E08_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E08_E05.c)) que leia `LA, CA`, a matriz `A` (`LA x CA`), depois `LB, CB`, a matriz `B` (`LB x CB`) (`1 <= LA, CA, LB, CB <= 20`) e um inteiro `alvo`.
- Se `CA != LB`, imprima apenas `Multiplicacao impossivel`.
- Caso contrário, calcule `C = A * B` (`LA x CB`), imprima `Produto (LA x CB):` e suas linhas, verifique se `C` é simétrica (`Simetrica: Sim` ou `Nao` — matriz não quadrada não é simétrica) e busque a **1ª ocorrência** de `alvo` em `C` (interrompendo ambos os laços ao encontrar), imprimindo `Alvo encontrado em (li, co)` ou `Alvo nao encontrado`.

---

### `E08-E06` *(Integração 3 — Pipeline de Imagem PGM P2 com Brilho, Extremos e Limiarização)*
Escreva um programa completo em C99 ([E08_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E08_E06.c)) que leia `largura` e `altura` (`1 <= largura, altura <= 500`), os pixels (`0..255`) em `static int img[500][500];`, e os inteiros `delta` e `limiar`.
1. Aplique o ajuste de brilho `delta` com saturação `[0, 255]`.
2. Encontre o **menor** e o **maior** pixel da imagem após o brilho (1ª ocorrência em ordem *row-major*, com coordenadas).
3. Em seguida, aplique limiarização (`< limiar -> 0`, `>= limiar -> 255`), contando `Pretos` e `Brancos`.

Imprima exatamente:
```text
P2
<largura> <altura>
255
<altura linhas com largura pixels separados por espaco simples>
Minimo: V1 em (i1, j1)
Maximo: V2 em (i2, j2)
Pretos: P Brancos: B
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `E08-C01` *(Teste de Mesa Integrado)*
Sem usar computador:
1. Dada a matriz $M_{3 \times 3} = \begin{pmatrix} 4 & 1 & -2 \\ 1 & 0 & 5 \\ -2 & 5 & 3 \end{pmatrix}$: informe se `M` é simétrica, qual é a soma da sua diagonal secundária (`i + j == 2`) e qual é a soma da 2ª coluna (`j = 1`, base 0).
2. Dadas $X_{2 \times 3} = \begin{pmatrix} 1 & 0 & -1 \\ 2 & 3 & 1 \end{pmatrix}$ e $Y_{3 \times 1} = \begin{pmatrix} 5 \\ -2 \\ 4 \end{pmatrix}$, calcule manualmente a matriz resultante `Z = X * Y`.

---

### `E08-C02` *(Programa Completo — Soma, Transposição e Busca 2D)*
Escreva um programa completo em C99 ([E08_C02.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E08_C02.c)) que leia `L, C` (`1 <= L, C <= 20`), duas matrizes `A` e `B` de dimensões `L x C` e um inteiro `alvo`. Calcule a transposta `T = (A + B)^T` (`C x L`) e busque a **1ª ocorrência** de `alvo` em `T` (ordem *row-major* em `T`, parando os dois laços ao encontrar). Imprima exatamente:
```text
Transposta de A+B (C x L):
<C linhas com L elementos separados por espaco simples>
Busca em T: (li, co)   (ou "Busca em T: nao encontrado")
```

---

### `E08-C03` *(Programa Completo — Produto Matricial, Identidade e Saturação `[0, 255]`)*
Escreva um programa completo em C99 ([E08_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/solucoes/E08_C03.c)) que leia `N` (`1 <= N <= 20`) e duas matrizes quadradas `A` e `B` (`N x N`). Calcule `P = A * B`, verifique se `P` é matriz identidade (antes da saturação) e, em seguida, sature todos os elementos de `P` para o intervalo `[0, 255]`. Imprima exatamente:
```text
Produto saturado [0, 255]:
<N linhas com N elementos separados por espaco simples>
Identidade (antes de saturar): Sim   (ou Nao)
```

---

## 5. Orientação de Avanço ou Recuperação (Conclusão do Estágio E)

- **Avançar para o Estágio F (`F01 — Introdução a Funções: void, return, Parâmetros e Argumentos`):** somente após autocorreção dos exercícios `E08-E01..E06` **e** **100% de acerto (3/3)** na Checagem Independente `E08-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada por sub-habilidade (1ª falha):**
  - Falha em limites, busca 2D ou inicialização de extremos $\rightarrow$ revisar **`E01`** e **`E02`**.
  - Falha em somas por linha/coluna, diagonais, triângulos ou identidade $\rightarrow$ revisar **`E03`** e **`E04`**.
  - Falha em transposta retangular, simetria ou produto matricial `i, j, k` $\rightarrow$ revisar **`E05`** e **`E06`**.
  - Falha em PGM P2 `(largura, altura)`, saturação `[0, 255]` ou `static` $\rightarrow$ revisar **`E07`**.
- **Após 2 tentativas malsucedidas:** interromper novas tentativas em `E08`, diagnosticar qual pré-requisito (`E01`–`E07`) falhou e reabilitá-lo integralmente antes de refazer a checagem de conclusão do Estágio E.

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 8 — matrizes bidimensionais e n-dimensionais).
- `[DOC]` `Aula_14_Algoritmos.pdf` e `Aula_15_Algoritmos.pdf` (matrizes 2D, somas, diagonais, transposição, simetria e imagens).
- `[DOC]` `Lista9_Algoritmos.pdf` completa (Ex. 1–8) e `Trabalho_Algoritmos.pdf` p. 1–2 (PGM P2 e `static`).
- Casos de teste e soluções verificáveis: [E08_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/gabaritos/E08_gabarito.md) e [E08_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/E08_testes.md).
