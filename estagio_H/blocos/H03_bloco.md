# Bloco `H03` — Matriz Auxiliar, Preservação de Bordas e Filtro de Desfoque (*Blur*) $t \times t$

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio H — Integração Geral e Projeto Modularizado (PGM) / **`H03`** |
| **Micro-habilidade foco** | *(Integração)* Implementar em `funcoes.h/.c` o filtro de desfoque parametrizável `aplicarBlur(int img[ALTURA][LARGURA], int t)` para `t` em `{3, 5, 7}`, usando raio `r = t / 2`, matriz auxiliar `static int aux[ALTURA][LARGURA]`, preservação estrita de bordas (`r <= i < ALTURA - r`) e média inteira da janela `t * t`. |
| **Pré-requisitos** | `H02` *(Filtros ponto a ponto modularizados em `funcoes.h/.c`)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Sessão 2 (`E04`–`E06`, 24 min):** `14 min` resol. \| `6 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Conteúdo novo de linguagem: NENHUM.** **Não utilize** `struct`, alocação dinâmica (`malloc`/`free`), VLAs, `gets(` ou recursividade. Declare a matriz auxiliar com `static int aux[ALTURA][LARGURA];` dentro de `aplicarBlur`. Respeite a assinatura `void aplicarBlur(int img[ALTURA][LARGURA], int t);` conforme `Trabalho_Algoritmos.pdf` p. 2 (rejeitando o erro de `Lista do Professor.pdf` p. 3 que omite `int t`). Saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Por que o *blur* exige matriz auxiliar `static int aux[ALTURA][LARGURA]`:**
   - Diferente de `ajustarBrilho` e `limiarizar`, no filtro de desfoque cada novo pixel depende da sua **vizinhança** $t \times t$.
   - Se você gravar o novo valor diretamente em `img[i][j]` antes de calcular os vizinhos, os pixels seguintes lerão valores **já alterados** em vez dos valores originais anteriores ao filtro.
   - **Padrão seguro em 2 passos:**
     1) Copie integralmente `img` para `static int aux[ALTURA][LARGURA];` no início de `aplicarBlur` (garantindo atualização mesmo quando o filtro é chamado mais de uma vez!).
     2) Leia os pixels da vizinhança a partir de `aux` e grave a média inteira apenas nos pixels internos de `img`.
2. **Raio `r = t / 2` e preservação automática das bordas:**
   - Para `t = 3`: `r = 1` (preserva `1` linha/coluna em cada borda; janela de `9` pixels).
   - Para `t = 5`: `r = 2` (preserva `2` linhas/colunas em cada borda; janela de `25` pixels).
   - Para `t = 7`: `r = 3` (preserva `3` linhas/colunas em cada borda; janela de `49` pixels).
   - Os laços dos pixels internos percorrem estritamente `r <= i < ALTURA - r` e `r <= j < LARGURA - r`. Como `img` já contém os pixels originais nas bordas e esses laços não escrevem fora desse intervalo, todas as bordas permanecem preservadas.
3. **Janela $t \times t$ e divisão inteira:**
   - Para cada pixel interno `(i, j)`, zere `int soma = 0;` e percorra `a` de `-r` até `r` e `b` de `-r` até `r`, acumulando `aux[i + a][j + b]`.
   - Atribua `img[i][j] = soma / (t * t);` (divisão inteira em C descarta a parte decimal, conforme exigido).

---

## 2. Exemplos Guiados

### Exemplo 1 — Protótipo e implementação completa de `aplicarBlur` *(Trecho ilustrativo)*

**Em `funcoes.h`:**
```c
void aplicarBlur(int img[ALTURA][LARGURA], int t);
```

**Em `funcoes.c`:**
```c
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

### Exemplo 2 — Impacto da matriz auxiliar em `4 x 4` (`t = 3`, `r = 1`) *(Rastreio)*
Matriz original:
```text
10  10  10  10
10  90  10  10
10  10  10  10
10  10  10  10
```
- **Correto (lendo de `aux`):** `(1, 1)` soma `8 * 10 + 90 = 170 -> 170 / 9 = 18`; depois `(1, 2)` ainda lê `aux[1][1] = 90`, obtendo `170 / 9 = 18`.
- **Errado (lendo direto de `img` alterado):** `(1, 1)` vira `18`; ao calcular `(1, 2)`, lê `img[1][1] = 18` no lugar de `90`, somando `8 * 10 + 18 = 98 -> 98 / 9 = 10`!

---

## 3. Exercícios (`H03-E01` a `H03-E06`)

### Sessão 1 (`H03-E01` a `H03-E03` — Teste de Mesa, Lacunas e Caça ao Bug)

### `H03-E01` *(Teste de Mesa `5 x 5` — Com vs. Sem Matriz Auxiliar e Bordas `t = 3` / `t = 5`)*
Sem usar computador, considere a matriz `5 x 5` original abaixo:
```text
90  90  90  90  90
90  90   0  90  90
90   0  90   0  90
90  90   0  90  90
90  90  90  90  90
```
1. Para `t = 3` (`r = 1`), calcule `(1, 1)` e `(1, 2)` **com** matriz auxiliar `aux` e mostre qual valor errado surgiria em `(1, 2)` caso o cálculo fosse feito **sem** matriz auxiliar (reutilizando o novo `(1, 1)`).
2. Escreva toda a matriz `5 x 5` resultante de `aplicarBlur(img, 3)`.
3. Partindo **da matriz original**, quantos e quais pixels `(i, j)` são internos para `t = 5` (`r = 2`)? Calcule o valor resultante desse(s) pixel(is).

---

### `H03-E02` *(Completar Lacunas — `aplicarBlur`)*
Complete as lacunas `/* A */` a `/* E */` na definição de `aplicarBlur` em `funcoes.c`:

```c
void aplicarBlur(int img[ALTURA][LARGURA], int t) {
    /* A */ int aux[ALTURA][LARGURA];
    int r = /* B */;

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            aux[i][j] = img[i][j];
        }
    }

    for (int i = r; i < /* C */; i++) {
        for (int j = r; j < LARGURA - r; j++) {
            int soma = 0;
            for (int a = -r; a <= r; a++) {
                for (int b = -r; b <= r; b++) {
                    soma += /* D */;
                }
            }
            img[i][j] = /* E */;
        }
    }
}
```

---

### `H03-E03` *(Caça ao Bug Multi-Arquivo — `aplicarBlur` `5 x 5`)*
O projeto de 5 arquivos abaixo deveria ler uma imagem PGM P2 `5 x 5` e um tamanho `t` (válido em `{3, 5, 7}`), aplicar `aplicarBlur(img, t)` preservando bordas e exibir a imagem resultante. Identifique os **4 bugs intencionais** em `funcoes.h` e `funcoes.c`, corrija o projeto e explique cada bug usando **comentários `//` diretamente no código**:

**`imagem.h` e `imagem.c`:** padrão correto para `ALTURA 5`, `LARGURA 5`.

**`funcoes.h` (com erro):**
```c
#ifndef FUNCOES_H
#define FUNCOES_H

#include "imagem.h"

void aplicarBlur(int img[ALTURA][LARGURA]);

#endif
```

**`funcoes.c` (com erro):**
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

    for (int i = r; i <= ALTURA - r; i++) {
        for (int j = r; j < LARGURA - r; j++) {
            int soma = 0;
            for (int a = -r; a <= r; a++) {
                for (int b = -r; b <= r; b++) {
                    soma += img[i + a][j + b];
                }
            }
            img[i][j] = soma / t;
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

### Sessão 2 (`H03-E04` a `H03-E06` — Implementação Modularizada em 5 Arquivos)

### `H03-E04` *(Variação controlada com pistas — Blur `3 x 3` em Matriz `5 x 5`)*
Implemente um projeto completo em **5 arquivos** (`ALTURA 5`, `LARGURA 5`):
- `imagem.h/.c`: `lerImagem` e `salvarImagem`.
- `funcoes.h/.c`: `void aplicarBlur(int img[ALTURA][LARGURA], int t);` usando `static int aux[ALTURA][LARGURA]` e preservando bordas `r = t / 2`.
- `main.c`: lê PGM P2 (`lerImagem`; se falhar, imprime `Erro ao ler imagem.\n` e encerra), aplica `aplicarBlur(img, 3)` e exibe a imagem resultante com `salvarImagem(img)`.

*Pista:* Garanta que `i` varie de `r` até `ALTURA - r - 1` (`i < ALTURA - r`) e `j` de `r` até `LARGURA - r - 1` (`j < LARGURA - r`).

---

### `H03-E05` *(Variação controlada com pistas — Blur Parametrizável `t` em `{3, 5, 7}` sobre `7 x 7`)*
Implemente um projeto completo em **5 arquivos** (`ALTURA 7`, `LARGURA 7`):
- `imagem.h/.c`: `lerImagem` e `salvarImagem`.
- `funcoes.h/.c`: `void aplicarBlur(int img[ALTURA][LARGURA], int t);`.
- `main.c`: lê PGM P2 (`lerImagem`; se falhar, imprime `Erro ao ler imagem.\n` e encerra), lê `int t`, aceita apenas `t == 3 || t == 5 || t == 7` (se inválido, imprime `Tamanho t invalido.\n` e encerra), aplica `aplicarBlur(img, t)` e imprime com `salvarImagem(img)`.

*Pista:* Na imagem `7 x 7`, para `t = 7` (`r = 3`), apenas o pixel central `(3, 3)` é interno!

---

### `H03-E06` *(Resolução independente — Blur + Brilho Encadeados em `7 x 7`)*
Construa um projeto completo em **5 arquivos** (`ALTURA 7`, `LARGURA 7`) integrando `H02` e `H03`:
- `imagem.h/.c`: `lerImagem` e `salvarImagem`.
- `funcoes.h/.c`: `void aplicarBlur(int img[ALTURA][LARGURA], int t);` e `void ajustarBrilho(int img[ALTURA][LARGURA], int b);`.
- `main.c`: lê PGM P2 (`lerImagem`; imprime `Erro ao ler imagem.\n` se falhar), lê `int b` e `int t`. Se `t != 3 && t != 5 && t != 7`, imprime `Tamanho t invalido.\n` e encerra. Caso contrário, aplica **primeiro** `aplicarBlur(img, t)` e **depois** `ajustarBrilho(img, b)`, exibindo a imagem final com `salvarImagem(img)`.

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `H03-C01` *(Teste de Mesa `t = 5` e Diferença Com vs. Sem Matriz Auxiliar)*
1. Considere uma matriz `6 x 6` onde todos os pixels valem `100`, exceto `img[2][2] = 0`, `img[2][3] = 125` e `img[3][5] = 50`. Para `aplicarBlur(img, 5)` (`t = 5`, `r = 2`):
   - Quantos pixels do total de `36` são preservados como borda e quantos são recalculados?
   - Calcule os novos valores exatos de `(2, 2)` e `(2, 3)`.
2. Em uma matriz `4 x 4` para `t = 3` (`r = 1`), com `img[1][1] = 90` e todos os demais pixels iguais a `10`, compare o valor obtido em `(1, 2)` **com** matriz auxiliar `aux` vs. **sem** matriz auxiliar.

### `H03-C02` *(Caça ao Bug — Soma Acumulada, Janela Incompleta e Borda Destruída)*
O projeto de 5 arquivos abaixo (`ALTURA 5`, `LARGURA 5`) deveria aplicar `aplicarBlur(img, t)` preservando bordas e usando `static int aux[ALTURA][LARGURA]`. Identifique e corrija os **3 bugs** em `funcoes.c` (com comentários `//`):

**`imagem.h`, `imagem.c`, `funcoes.h` e `main.c`:** padrão correto para `ALTURA 5`, `LARGURA 5` (validando `t` em `{3, 5, 7}`).

**`funcoes.c` (com erro):**
```c
#include "funcoes.h"

void aplicarBlur(int img[ALTURA][LARGURA], int t) {
    static int aux[ALTURA][LARGURA];
    int r = t / 2;
    int soma = 0;

    for (int i = r; i < ALTURA - r; i++) {
        for (int j = r; j < LARGURA - r; j++) {
            for (int a = 0; a <= r; a++) {
                for (int b = 0; b <= r; b++) {
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
```

### `H03-C03` *(Projeto 5-Arquivos Independente — `aplicarBlur` em Matriz `7 x 7`)*
Construa do zero o projeto de **5 arquivos** (`ALTURA 7`, `LARGURA 7`) com `void aplicarBlur(int img[ALTURA][LARGURA], int t);` usando `static int aux[ALTURA][LARGURA]`, preservação de bordas (`r = t / 2`) e média inteira `t * t`. No `main.c`, leia PGM P2 (`lerImagem`), leia `int t`, rejeite `t` fora de `{3, 5, 7}` com `Tamanho t invalido.\n` e, quando válido, aplique `aplicarBlur(img, t)` e imprima via `salvarImagem(img)`. Verifique para `t = 3` e `t = 5`.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `H04` (`Filtro de Mediana 3 x 3 com Extração de Vizinhança e Função ordenar`):** somente após autocorreção de `H03-E01..E06` e **100% (3/3)** na Checagem Independente `H03-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** rastrear na mão uma matriz `5 x 5` destacando em cores/contorno a faixa `r <= i < ALTURA - r` para `t = 3` e `t = 5`, verificar onde `aux` é copiada e onde `soma = 0` é reiniciada, e aplicar variante `V2` de `H03`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`H02`** (modularização em `funcoes.h/.c`), **`E05`** (cópia/matriz auxiliar com `static`) e **`C09`** (4 laços aninhados e controle de índices).

---

## 6. Referências do Orientador
- `[DOC]` `Trabalho_Algoritmos.pdf` p. 2–3 (Seção 4.2: blur $t \times t$ para $t \in \{3,5,7\}$, $r = t/2$, média inteira, bordas e matriz auxiliar `static`).
- `[DOC]` `Apresentacao_Trabalho_Algoritmos.pdf` p. 9–10, 14 (vizinhança $7 \times 7$, por que usar matriz auxiliar e testes manuais em matrizes pequenas).
- `[DOC]` Conflito C8 em [00_inventario_fontes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/00_inventario_fontes.md): manter parâmetro `int t` em `aplicarBlur(int img[ALTURA][LARGURA], int t)`, rejeitando a omissão de `Lista do Professor.pdf` p. 3.
- Casos de teste e soluções verificáveis: [H03_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/gabaritos/H03_gabarito.md) e [H03_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/H03_testes.md).
