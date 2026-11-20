# Bloco `H05` — Menu Interativo de Operações Sucessivas (`do-while` + `switch`) e Validação de Entradas

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio H — Integração Geral e Projeto Modularizado (PGM) / **`H05`** |
| **Micro-habilidade foco** | *(Integração)* Integrar em `main.c` a leitura única pré-menu (com tratamento de erro ao falhar), o laço repetitivo `do-while` + `switch` encadeando filtros sobre o estado atual da imagem (`brilho`, `blur` com validação `t` em `{3, 5, 7}`, `mediana`) até gravar e sair (`0`). |
| **Pré-requisitos** | `H04` *(Filtro de mediana `3 x 3`)*, `C04` *(Laço pós-condicional `do-while`)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 20 min):** `12 min` resol. \| `5 min` corr. \| `3 min` recup.; **Sessão 2 (`E04`–`E06`, 22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Conteúdo novo de linguagem: NENHUM.** Mantenha em `main.c` **somente** a função `main`, com o menu principal e as chamadas aos módulos `"imagem.h"` e `"funcoes.h"`. **Não utilize** `struct`, alocação dinâmica (`malloc`/`free`), VLAs, `gets(` ou parser `FILE*` próprio em `main.c`. Saídas estritamente em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Leitura única ANTES do menu:**
   - A função `lerImagem(img)` deve ser chamada **uma única vez antes do `do-while`**.
   - Se `lerImagem(img)` retornar `0` (falha na leitura ou formato inválido), exiba mensagem de erro (`printf("Erro ao ler imagem.\n");`) e encerre com `return 1;`.
   - **Erro crítico proibido:** chamar `lerImagem(img)` dentro do `do-while` apaga todos os filtros já aplicados e/ou trava o fluxo de entrada.
2. **Operações sucessivas sobre o estado atual (`do-while` + `switch`):**
   - A matriz `static int img[ALTURA][LARGURA];` em `main` guarda o **estado atual** da imagem. Cada filtro escolhido modifica `img` *in-place*, de modo que o filtro seguinte opera sobre o resultado do anterior (ex.: `brilho -> blur -> mediana`).
   - O laço repete com `do { ... } while (opcao != 0);`.
   - Nunca esqueça `break;` ao final de cada `case` para evitar *fall-through* indesejado.
3. **Validação estrita das entradas:**
   - No `case 2` (`blur`), leia `t` e aceite **somente** `t == 3 || t == 5 || t == 7`. Qualquer outro valor (como `2`, `4`, `9` ou `-3`) deve ser rejeitado com mensagem clara, sem chamar `aplicarBlur`.
   - No `default:`, informe `"Opcao invalida.\n"` e continue o laço.
   - No `case 0:`, chame `salvarImagem(img);` uma única vez antes de sair do laço.
4. **Organização estrita de `main.c`:**
   - Inclua `<stdio.h>`, `"imagem.h"` e `"funcoes.h"`.
   - Mantenha apenas `int main(void)` em `main.c`; todas as operações ficam em `funcoes.c` e a E/S em `imagem.c`.

---

## 2. Exemplos Guiados

### Exemplo 1 — Estrutura canônica do menu em `main.c` *(Trecho ilustrativo)*
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
*Nota sobre o ambiente de testes do curso:* No projeto entregue ao professor (`Trabalho_Algoritmos.pdf`), `imagem.c` lê `"entrada.pgm"` e grava `"resultado.pgm"`; nos projetos de verificação em `solucoes/`, `imagem.c` realiza exatamente o mesmo papel de módulo de E/S usando `stdin`/`stdout` no formato PGM P2 para permitir execução automatizada determinística.

---

## 3. Exercícios (`H05-E01` a `H05-E06`)

### Sessão 1 (`H05-E01` a `H05-E03` — Rastreamento de Estado, Lacunas e Caça ao Bug)

### `H05-E01` *(Teste de Mesa — Operações Sucessivas sobre o Estado Atual)*
Sem usar computador, considere a matriz `3 x 3` inicial abaixo (`ALTURA = 3`, `LARGURA = 3`) carregada antes do menu:
```text
240  100   90
 80  250  110
 70   95   85
```
O usuário executa a sequência: `1` (com `b = 30`) $\rightarrow$ `3` (mediana `3 x 3`) $\rightarrow$ `2` (com `t = 3`) $\rightarrow$ `0` (salvar e sair).
- **(a)** Escreva a matriz `3 x 3` completa após o passo `1` (`b = 30`).
- **(b)** Escreva a matriz `3 x 3` após o passo `3` (mediana), listando o vetor ordenado do pixel `(1, 1)`.
- **(c)** Escreva a matriz `3 x 3` final salva no passo `0` após o passo `2` (`t = 3`), indicando explicitamente o valor do pixel de borda `(0, 0)` e do pixel central `(1, 1)`.

---

### `H05-E02` *(Completar Solução — Pré-Leitura, `do-while`, `switch` e Validação)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */`, `/* D */` e `/* E */` no `main.c` abaixo:

```c
int main(void) {
    static int img[ALTURA][LARGURA];
    int opcao, b, t;

    if (/* A */) {
        printf("Erro ao ler imagem.\n");
        return 1;
    }

    /* B */ {
        scanf("%d", &opcao);
        switch (opcao) {
            case 1:
                scanf("%d", &b);
                ajustarBrilho(img, b);
                break;
            case 2:
                scanf("%d", &t);
                if (/* C */) {
                    aplicarBlur(img, t);
                } else {
                    printf("Tamanho invalido. Use 3, 5 ou 7.\n");
                }
                break;
            case 3:
                aplicarMediana(img);
                /* D */
            case 0:
                salvarImagem(img);
                break;
            default:
                printf("Opcao invalida.\n");
                break;
        }
    } while (/* E */);

    return 0;
}
```

---

### `H05-E03` *(Caça ao Bug em Projeto 5-Arquivos — Correção Comentada)*
O `main.c` abaixo integra o projeto de 5 arquivos (`ALTURA = 7`, `LARGURA = 7`), mas possui **3 bugs intencionais** que quebram o encadeamento de filtros, o `switch` e a validação do `blur`. Identifique os **3 bugs**, corrija o `main.c` completo mantendo o menu do Exemplo 1 e explique cada correção com **comentários `//`**:

```c
#include <stdio.h>
#include "imagem.h"
#include "funcoes.h"

int main(void) {
    static int img[ALTURA][LARGURA];
    int opcao, b, t;

    do {
        if (!lerImagem(img)) {
            printf("Erro ao ler imagem.\n");
            return 1;
        }

        printf("===== PROCESSAMENTO DE IMAGENS =====\n");
        printf("1 - Ajustar brilho\n");
        printf("2 - Aplicar desfoque (blur)\n");
        printf("3 - Aplicar filtro da mediana\n");
        printf("0 - Salvar e sair\n");
        printf("Escolha uma opcao:\n");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                scanf("%d", &b);
                ajustarBrilho(img, b);
            case 2:
                scanf("%d", &t);
                aplicarBlur(img, t);
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

---

### Sessão 2 (`H05-E04` a `H05-E06` — Integração Completa de `main.c` + Módulos)

### `H05-E04` *(Variação com pistas — Sistema Completo 5 Arquivos em `7 x 7`)*
Construa o projeto completo em **5 arquivos** (`imagem.h`, `imagem.c`, `funcoes.h`, `funcoes.c`, `main.c`) com `ALTURA 7` e `LARGURA 7`:
- `funcoes.h` / `funcoes.c`: `ajustarBrilho(img, b)`, `aplicarBlur(img, t)` (para `t` em `{3, 5, 7}` com matriz auxiliar `static`), `ordenar(v, n)` e `aplicarMediana(img)` (com matriz auxiliar `static`).
- `main.c`: leitura única pré-menu (erro `"Erro ao ler imagem.\n"` e `return 1`), menu idêntico ao Exemplo 1 (`1` brilho, `2` blur com validação `3/5/7`, `3` mediana, `0` salvar e sair, `default` `"Opcao invalida.\n"`).
- *Pista:* Para `ALTURA = 7` e `LARGURA = 7`, o blur `t = 7` (`r = 3`) recalcula exatamente o pixel central `(3, 3)` e preserva todos os 48 pixels ao redor.

---

### `H05-E05` *(Variação com pistas — Menu com Contador de Operações Aplicadas)*
Partindo da arquitetura de **5 arquivos** (`ALTURA 7`, `LARGURA 7`), implemente o mesmo menu de `H05-E04`, adicionando um contador `int ops = 0;` em `main`:
- Incremente `ops` **somente** quando uma operação válida for efetivamente aplicada à imagem (`case 1`, `case 2` com `t` em `{3, 5, 7}`, ou `case 3`). Opções inválidas (`default`) ou `t` inválido no blur **não** incrementam `ops`.
- Ao selecionar `0` (`Salvar e sair`), imprima exatamente:
  ```text
  Operacoes aplicadas: K
  ```
  e em seguida chame `salvarImagem(img);`.
- *Pista:* Inicialize `int ops = 0;` antes do `do-while` e atualize-o apenas dentro dos ramos válidos.

---

### `H05-E06` *(Resolução independente — Menu Estendido com Limiarização `[0, 255]`)*
Construa do zero o projeto completo em **5 arquivos** (`ALTURA 7`, `LARGURA 7`) mantendo todas as operações obrigatórias (`ajustarBrilho`, `aplicarBlur`, `aplicarMediana`) e adicionando `void limiarizar(int img[ALTURA][LARGURA], int limiar);` em `funcoes.h/.c`.
No `main.c`, após leitura única pré-menu, apresente o menu:
```text
===== PROCESSAMENTO DE IMAGENS =====
1 - Ajustar brilho
2 - Aplicar desfoque (blur)
3 - Aplicar filtro da mediana
4 - Aplicar limiarizacao
0 - Salvar e sair
Escolha uma opcao:
```
Valide também o limiar na opção `4`: aceite somente `0 <= limiar && limiar <= 255`; caso contrário, imprima `Limiar invalido. Use 0 a 255.\n` e retorne ao menu sem alterar a imagem.

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `H05-C01` *(Teste de Mesa sem Computador — Estado Acumulado)*
Dada a matriz `3 x 3` inicial:
```text
10   80   90
70  255  100
60   85   95
```
Rastreie a sequência de opções `1` (`b = -40`) $\rightarrow$ `3` (mediana `3 x 3`) $\rightarrow$ `2` (`t = 3`) $\rightarrow$ `0` (salvar e sair) e informe:
1. A matriz após `1` (`b = -40`).
2. O valor do pixel `(1, 1)` após `3` (mediana) e o valor do pixel `(0, 0)`.
3. A matriz final após `2` (`t = 3`).

### `H05-C02` *(Diagnóstico sem Compilar)*
Identifique os **3 erros** no trecho de `main.c` abaixo e explique como corrigi-los:
```c
int main(void) {
    static int img[ALTURA][LARGURA];
    int opcao, t;
    do {
        lerImagem(img);
        scanf("%d", &opcao);
        switch (opcao) {
            case 2:
                scanf("%d", &t);
                aplicarBlur(img, t);
                break;
            case 0:
                salvarImagem(img);
                break;
        }
    } while (opcao == 0);
    return 0;
}
```

### `H05-C03` *(Projeto 5-Arquivos Independente — Menu Completo)*
Crie do zero os **5 arquivos** (`imagem.h`, `imagem.c`, `funcoes.h`, `funcoes.c`, `main.c`) com `ALTURA 7` e `LARGURA 7` para o processador com menu `1` (Brilho), `2` (Blur `3/5/7`), `3` (Mediana) e `0` (Salvar e sair), garantindo:
- Leitura única pré-menu com tratamento de falha (`Erro ao ler imagem.\n` e `return 1;`);
- Validação de `t` (`3, 5, 7`) com mensagem `Tamanho invalido. Use 3, 5 ou 7.\n`;
- Tratamento de opção inválida com `Opcao invalida.\n`;
- Compilação limpa com `gcc -std=c99 -Wall -Wextra main.c imagem.c funcoes.c -o processador` e execução encadeada de $\ge 2$ operações.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `H06` (`Verificação Sistemática, Teste de Mesa Integrado e Preparação para Arguição`):** somente após autocorreção de `H05-E01..E06` e **100% (3/3)** em `H05-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):**
  - Perdeu o estado entre operações ou leu imagem dentro do laço $\rightarrow$ desenhar a linha do tempo de `img` em `main` e revisar o padrão de acumulação pré-laço (`C03`).
  - Esqueceu `break`, errou condição de `do-while` ou aceitou `t` inválido $\rightarrow$ revisar `B08` (`switch`) e `C04` (`do-while`) e aplicar variante equivalente `V2` de `H05`.
- **Após 2 tentativas malsucedidas:** interromper novas tentativas em `H05` e investigar os pré-requisitos **`C04`** (`do-while`), **`B08`** (`switch/case`) e **`H04`** (`aplicarMediana` e `funcoes.h/.c`).

---

## 6. Referências do Orientador
- `[DOC]` `Trabalho_Algoritmos.pdf` p. 3–4 (Seção 5 — Menu principal e integração, regras de leitura única e validação de `t`).
- `[DOC]` `Apresentacao_Trabalho_Algoritmos.pdf` p. 13–14 (Menu principal e fluxo de operações sucessivas).
- `[DOC]` [00_mapa_curricular.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/00_mapa_curricular.md) (linhas 807–816 — Bloco `H05`).
- Casos de teste e soluções verificáveis: [H05_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/gabaritos/H05_gabarito.md) e [H05_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/H05_testes.md).
