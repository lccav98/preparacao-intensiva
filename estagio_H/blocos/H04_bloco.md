# Bloco `H04` — Filtro de Mediana `3 x 3` com Extração de Vizinhança e Função de Ordenação Fornecida

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio H — Integração Geral e Projeto Modularizado (PGM) / **`H04`** |
| **Micro-habilidade foco** | *(Integração)* Extrair a vizinhança `3 x 3` de cada pixel interno (preservando bordas via matriz auxiliar `static`) para `int v[9]` com contador `k = 0`, chamar a função `ordenar(v, 9)` fornecida no módulo `funcoes` e atribuir `v[4]` ao pixel resultante. |
| **Pré-requisitos** | `H03` *(Matriz auxiliar `static`, preservação de bordas e filtro de desfoque `blur`)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 20 min):** `12 min` resol. \| `5 min` corr. \| `3 min` recup.; **Sessão 2 (`E04`–`E06`, 22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Conteúdo novo de linguagem: NENHUM.** A função `ordenar(int v[], int n)` é fornecida pronta (não implementar algoritmo de ordenação próprio do zero). **Não utilize** `struct`, alocação dinâmica (`malloc`/`free`), VLAs, aritmética de ponteiros ou `gets(`. Mantenha a arquitetura de 5 arquivos (`main.c`, `imagem.h`, `imagem.c`, `funcoes.h`, `funcoes.c`) e saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Objetivo do filtro de mediana `3 x 3`:**
   - Reduzir o chamado **ruído sal e pimenta** (pixels isolados muito claros, como `255`, ou muito escuros, como `0`) substituindo cada pixel interno pelo valor central da vizinhança ordenada.
2. **Preservação das bordas e matriz auxiliar `static`:**
   - Apenas pixels **internos** possuem todos os 9 vizinhos `3 x 3`: `i` varia de `1` até `ALTURA - 2` (`i < ALTURA - 1`) e `j` varia de `1` até `LARGURA - 2` (`j < LARGURA - 1`).
   - A primeira e a última linha (`i == 0`, `i == ALTURA - 1`) e a primeira e a última coluna (`j == 0`, `j == LARGURA - 1`) permanecem **inalteradas**.
   - **Nunca** leia vizinhos e grave o resultado na mesma matriz `img` durante o cálculo! Copie `img` para uma matriz auxiliar `static int aux[ALTURA][LARGURA];` (ou calcule os internos em `aux` lendo de `img` após copiar as bordas para `aux`) e, somente ao término dos laços, copie `aux` de volta para `img`.
3. **Extração 2D $\rightarrow$ 1D, ordenação e mediana `v[4]`:**
   - Para **cada** pixel interno `(i, j)`, declare `int v[9];` e reinicie **`int k = 0;`** antes dos laços da janela `a` de `-1` a `1` e `b` de `-1` a `1`.
   - Copie cada vizinho: `v[k] = img[i + a][j + b]; k++;`.
   - Chame `ordenar(v, 9);` (fornecida pronta no módulo `funcoes`).
   - Como `v` tem 9 elementos ordenados em ordem crescente (`v[0]` .. `v[8]`), o elemento central (5º menor) é **`v[4]`**. Grave `aux[i][j] = v[4];`.
4. **Arquitetura dos 5 arquivos no GCC:**
   - `imagem.h`: guardas `IMAGEM_H`, constantes `ALTURA` e `LARGURA`, protótipos de `lerImagem` e `salvarImagem`.
   - `imagem.c`: implementação de `lerImagem` e `salvarImagem`.
   - `funcoes.h`: guardas `FUNCOES_H`, `#include "imagem.h"`, protótipos de `ordenar` e `aplicarMediana` (e demais filtros).
   - `funcoes.c`: inclui `"funcoes.h"` e implementa `ordenar` e `aplicarMediana`.
   - `main.c`: inclui `<stdio.h>`, `"imagem.h"` e `"funcoes.h"`; compilar com `gcc -std=c99 -Wall -Wextra main.c imagem.c funcoes.c -o processador`.

---

## 2. Exemplos Guiados

### Exemplo 1 — Cálculo manual da mediana `3 x 3` sobre ruído sal *(Trecho ilustrativo)*
Considere o pixel central de intensidade `255` e sua vizinhança `3 x 3`:

```text
[ 100  102  101 ]
[  99  255  103 ]
[ 100   98  101 ]
```

1. **Extração para `v[9]` (`k = 0..8`):** `v = {100, 102, 101, 99, 255, 103, 100, 98, 101}`.
2. **Após `ordenar(v, 9)`:** `v = {98, 99, 100, 100, 101, 101, 102, 103, 255}`.
3. **Mediana (`v[4]`):** `101`. O ruído isolado `255` é eliminado sem alterar drasticamente os tons da vizinhança.

### Exemplo 2 — Função `ordenar` fornecida e `aplicarMediana` em `funcoes.c` *(Trecho ilustrativo)*
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
            aux[i][j] = img[i][j]; /* preserva todas as bordas */
        }
    }

    for (int i = 1; i < ALTURA - 1; i++) {
        for (int j = 1; j < LARGURA - 1; j++) {
            int k = 0; /* obrigatorio reiniciar k para cada pixel (i, j) */
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

---

## 3. Exercícios (`H04-E01` a `H04-E06`)

### Sessão 1 (`H04-E01` a `H04-E03` — Teste de Mesa, Lacunas e Caça ao Bug)

### `H04-E01` *(Teste de Mesa — Extração `3 x 3`, Ordenação e Matriz Auxiliar)*
Sem usar computador, resolva:
- **(a)** Para a janela `3 x 3` abaixo (com ruído pimenta `0` no centro), escreva `v[9]` antes e depois de `ordenar(v, 9)` e informe o valor atribuído ao pixel central (`v[4]`):
  ```text
  40  42  41
  39   0  44
  43  40  45
  ```
- **(b)** Para a matriz `4 x 4` abaixo (`ALTURA = 4`, `LARGURA = 4`), calcule **toda a matriz resultante** após `aplicarMediana(img)`, indicando quais posições permanecem como borda e mostrando os vetores ordenados dos 4 pixels internos:
  ```text
  90  10  12  14
  92   0  50  95
  94  96 255  98
  10  12  14  16
  ```
  *Dica:* Observe o que ocorreria com o pixel `(1, 2)` se você gravasse o novo valor de `(1, 1)` diretamente em `img` antes de calcular `(1, 2)`!

---

### `H04-E02` *(Completar Solução — Extração, Ordenação e Cópia Final)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */`, `/* D */` e `/* E */` na implementação de `aplicarMediana`:

```c
void aplicarMediana(int img[ALTURA][LARGURA]) {
    /* A */ int aux[ALTURA][LARGURA];
    int v[9];

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            aux[i][j] = img[i][j];
        }
    }

    for (int i = 1; i < ALTURA - 1; i++) {
        for (int j = 1; j < LARGURA - 1; j++) {
            int k = /* B */;
            for (int a = -1; a <= 1; a++) {
                for (int b = -1; b <= 1; b++) {
                    /* C */
                    k++;
                }
            }
            /* D */
            aux[i][j] = /* E */;
        }
    }

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            img[i][j] = aux[i][j];
        }
    }
}
```

---

### `H04-E03` *(Caça ao Bug em Projeto 5-Arquivos — Correção Comentada)*
O projeto de 5 arquivos abaixo (`ALTURA = 5`, `LARGURA = 5`) deveria ler uma imagem PGM P2 da entrada padrão, aplicar o filtro de mediana `3 x 3` e gravar o resultado. Identifique os **3 bugs intencionais** em `funcoes.c`, corrija os arquivos e documente cada correção com **comentários `//`**.

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

**`funcoes.h`:**
```c
#ifndef FUNCOES_H
#define FUNCOES_H

#include "imagem.h"

void ordenar(int v[], int n);
void aplicarMediana(int img[ALTURA][LARGURA]);

#endif
```

**`funcoes.c` (com 3 bugs intencionais):**
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
    int v[9];
    int k = 0;

    for (int i = 1; i < ALTURA - 1; i++) {
        for (int j = 1; j < LARGURA - 1; j++) {
            for (int a = -1; a <= 1; a++) {
                for (int b = -1; b <= 1; b++) {
                    v[k] = img[i + a][j + b];
                    k++;
                }
            }
            ordenar(v, 9);
            img[i][j] = v[5];
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
*(Nota: `imagem.c` implementa `lerImagem` e `salvarImagem` lendo/gravando PGM P2 via `stdin`/`stdout`, representando o módulo de E/S já fornecido no trabalho.)*

---

### Sessão 2 (`H04-E04` a `H04-E06` — Integração em Projeto 5-Arquivos)

### `H04-E04` *(Variação com pistas — Filtro de Mediana `3 x 3` em `5 x 5`)*
Construa o projeto completo em **5 arquivos** (`imagem.h`, `imagem.c`, `funcoes.h`, `funcoes.c`, `main.c`) com `ALTURA 5` e `LARGURA 5`:
- `funcoes.h` / `funcoes.c`: implemente `ordenar(int v[], int n)` (fornecida) e `aplicarMediana(int img[ALTURA][LARGURA])` usando matriz auxiliar `static`.
- `main.c`: leia uma imagem PGM P2 `5 x 5` via `lerImagem(img)` (se falhar, imprima `Erro ao ler imagem.\n` e retorne `1`), chame `aplicarMediana(img)` e grave o resultado com `salvarImagem(img)`.
- *Pista:* Compile com `gcc -std=c99 -Wall -Wextra main.c imagem.c funcoes.c -o processador`.

---

### `H04-E05` *(Variação com pistas — Aplicações Sucessivas da Mediana `3 x 3`)*
Aproveitando a arquitetura de **5 arquivos** (`ALTURA 5`, `LARGURA 5`), leia uma imagem PGM P2 `5 x 5` via `lerImagem(img)` e, em seguida, leia um inteiro `passos` (`passos >= 0`, indicando quantas vezes o filtro da mediana será aplicado sucessivamente sobre o estado atual da imagem):
- `main.c` lê `passos` após `lerImagem(img)`, executa `aplicarMediana(img)` em um laço `passos` vezes e chama `salvarImagem(img)`.
- *Pista:* Se `passos == 0`, a imagem salva deve ser idêntica à original; se `passos == 2`, a 2ª chamada de `aplicarMediana` processa a imagem já modificada pela 1ª chamada, mantendo as bordas intactas em todas as passagens.

---

### `H04-E06` *(Resolução independente — Mediana + Contagem de Pixels Alterados)*
Construa do zero o projeto completo em **5 arquivos** (`ALTURA 5`, `LARGURA 5`) com:
- `aplicarMediana(int img[ALTURA][LARGURA])` no módulo `funcoes`;
- uma função adicional `void copiarImagem(const int orig[ALTURA][LARGURA], int dest[ALTURA][LARGURA]);` e `int contarAlterados(const int a[ALTURA][LARGURA], const int b[ALTURA][LARGURA]);` no módulo `funcoes`;
- `main.c` declara `static int img[ALTURA][LARGURA];` e `static int orig[ALTURA][LARGURA];`, lê a imagem PGM P2 em `img`, copia para `orig`, aplica `aplicarMediana(img)`, chama `salvarImagem(img)` e imprime ao final:
  ```text
  Pixels alterados: K
  ```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `H04-C01` *(Teste de Mesa sem Computador)*
1. Dada a vizinhança `3 x 3` abaixo com ruído pimenta `0`, escreva os 9 elementos em `v[9]`, o vetor após `ordenar(v, 9)` e o valor selecionado por `v[4]`:
   ```text
   50  52  48
   51   0  49
   53  50  54
   ```
2. Em uma matriz `4 x 4` (índices `0..3`), liste exatamente todas as coordenadas `(i, j)` que **recebem** novo valor em `aplicarMediana` e quantos pixels de borda permanecem preservados.

### `H04-C02` *(Diagnóstico sem Compilar)*
Identifique os **2 erros** no trecho abaixo e escreva a correção exata:
```c
void aplicarMediana(int img[ALTURA][LARGURA]) {
    int v[9];
    int k = 0;
    for (int i = 1; i < ALTURA - 1; i++) {
        for (int j = 1; j < LARGURA - 1; j++) {
            for (int a = -1; a <= 1; a++) {
                for (int b = -1; b <= 1; b++) {
                    v[k] = img[i + a][j + b];
                    k++;
                }
            }
            ordenar(v, 9);
            img[i][j] = v[4];
        }
    }
}
```

### `H04-C03` *(Projeto 5-Arquivos Independente — Mediana + Limiarização)*
Construa o projeto completo em **5 arquivos** (`ALTURA 5`, `LARGURA 5`) com `aplicarMediana(int img[ALTURA][LARGURA])` e `limiarizar(int img[ALTURA][LARGURA], int limiar)` (`< limiar -> 0`, `>= limiar -> 255`) em `funcoes.h/.c`. No `main.c`, leia a imagem PGM P2 `5 x 5` e depois um inteiro `limiar`, aplique **primeiro** `aplicarMediana(img)` e **depois** `limiarizar(img, limiar)`, e grave o PGM P2 final com `salvarImagem(img)`.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `H05` (`Menu Interativo de Operações Sucessivas e Validação de Entradas`):** somente após autocorreção de `H04-E01..E06` e **100% (3/3)** em `H04-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):**
  - Errou a mediana ou o índice `v[4]` $\rightarrow$ refazer extração manual `3 x 3` para `v[9]` e conferir que índices pares de tamanho `9` têm centro em `9 / 2 = 4`.
  - Esqueceu `k = 0` dentro do laço `(i, j)` ou contaminou vizinhos sem `aux` $\rightarrow$ desenhar o estado de `img` e `aux` passo a passo como em `H04-E01(b)` e aplicar variante equivalente `V2`.
- **Após 2 tentativas malsucedidas:** interromper novas tentativas em `H04` e investigar os pré-requisitos **`H03`** (matriz auxiliar `static` e preservação de bordas), **`F06`** (vetores como parâmetro) e **`D09`** (mapeamento 2D $\leftrightarrow$ 1D).

---

## 6. Referências do Orientador
- `[DOC]` `Trabalho_Algoritmos.pdf` p. 2–4 (Seção 4.3 — Filtro de mediana `3 x 3`, código exato de `ordenar` e exigência de matriz auxiliar).
- `[DOC]` `Apresentacao_Trabalho_Algoritmos.pdf` p. 11–12 (Mediana `3 x 3` e preservação de bordas).
- `[DOC]` [00_mapa_curricular.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/00_mapa_curricular.md) (linhas 797–806 — Bloco `H04`).
- Casos de teste e soluções verificáveis: [H04_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/gabaritos/H04_gabarito.md) e [H04_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/H04_testes.md).
