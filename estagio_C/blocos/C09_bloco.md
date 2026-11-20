# Bloco `C09` — Laços Aninhados e Formatação Tabular

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio C — Estruturas de Repetição e Rastreamento de Laços / **`C09`** |
| **Micro-habilidade foco** | Projetar e rastrear dois laços aninhados (`i` externo, `j` interno), com limites independentes (grades $M \times N$) e dependentes (`j <= i`), posicionando corretamente `printf("\n")` e usando largura fixa (`%2d`, `%3d`, `%4d`). |
| **Pré-requisitos** | `C05` *(Laço Contado `for`)*, `C06` *(Rastreamento Rigoroso de `for`)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 20 min):** `12 min` resol. \| `5 min` corr. \| `3 min` recup.; **Sessão 2 (`E04`–`E06`, 22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Não utilize** vetores ou strings (`char[]`, `int[]` ou qualquer array `v[i]`), funções customizadas além de `int main(void)`, `struct` ou alocação dinâmica. Use estritamente C99 com saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Anatomia de Dois Laços Aninhados (`i` externo, `j` interno):**
   - Para cada única iteração do laço externo (`i` representa a **linha**), o laço interno (`j` representa a **coluna**) executa seu ciclo completo do início ao fim.
   - Se o laço externo executa $M$ vezes e o interno $N$ vezes (limites independentes), o corpo interno é executado $M \times N$ vezes.
   - **Regra obrigatória:** Use variáveis de controle **distintas** (`i` no externo, `j` no interno). Reutilizar `i` nos dois laços destrói a contagem externa.

2. **Limites Independentes vs. Limites Dependentes (`j <= i`):**
   - **Limites independentes (grade $M \times N$):** `for (int i = 1; i <= M; i++)` e `for (int j = 1; j <= N; j++)` produzem retângulos ou tabelas completas.
   - **Limites dependentes:** Quando a condição do laço interno depende de `i` (como `j <= i` ou `j >= i`), o número de colunas varia a cada linha, formando triângulos numéricos e padrões escalonados.

3. **Posicionamento Crítico de `printf("\n")`:**
   - A quebra de linha `printf("\n");` deve ficar **imediatamente após o fechamento `}` do laço interno**, ainda **dentro** do bloco do laço externo.
   - Se colocada *dentro* do laço interno, cada célula ocupa uma linha separada.
   - Se colocada *fora* do laço externo, toda a tabela sai achatada em uma única linha.

4. **Largura Fixa (`%2d`, `%3d`, `%4d`) para Alinhamento Tabular:**
   - Imprimir com `%d` puro desalinhará colunas assim que surgirem números de 2 ou 3 dígitos (ex.: `9` seguido de `10`).
   - Especificadores como `%3d` reservam no mínimo 3 caracteres por número, alinhando à direita com espaços à esquerda (`"  1"`, `" 10"`, `"100"`).

5. **Quebra Periódica com `%` em Laços Lineares (Calendário):**
   - Em impressões tabulares de sequência contínua (como os dias `1..dias` de um mês), após imprimir `inicio - 1` recuos iniciais e o dia `d`, testa-se `(inicio - 1 + d) % 7 == 0` para emitir `\n` ao fechar cada semana de 7 colunas.

---

## 2. Exemplos Guiados

### Exemplo 1 — Grade de Multiplicação $3 \times 4$ com `%3d` (Limites Independentes)

```c
#include <stdio.h>

int main(void) {
    for (int i = 1; i <= 3; i++) {
        for (int j = 1; j <= 4; j++) {
            printf("%3d", i * j);
        }
        printf("\n"); // Quebra apenas ao terminar todas as colunas da linha i
    }
    return 0;
}
```

**Saída Produzida:**
```text
  1  2  3  4
  2  4  6  8
  3  6  9 12
```
*Observe como `%3d` mantém todas as colunas perfeitamente alinhadas à direita, inclusive com o `12` de 2 dígitos.*

---

### Exemplo 2 — Triângulo Numérico Dependente (`j <= i`) para `n = 4`

```c
#include <stdio.h>

int main(void) {
    int n = 4;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%2d", j);
        }
        printf("\n");
    }
    return 0;
}
```

**Rastreamento resumido:**
- `i = 1`: `j` percorre `1` $\rightarrow$ imprime ` 1\n`
- `i = 2`: `j` percorre `1, 2` $\rightarrow$ imprime ` 1 2\n`
- `i = 3`: `j` percorre `1, 2, 3` $\rightarrow$ imprime ` 1 2 3\n`
- `i = 4`: `j` percorre `1, 2, 3, 4` $\rightarrow$ imprime ` 1 2 3 4\n`

---

## 3. Exercícios (`C09-E01` a `C09-E06`)

### Sessão 1 (`C09-E01` a `C09-E03` — Rastreamento, Depuração e Grade Independente)

### `C09-E01` *(Teste de Mesa — Laços Aninhados Dependentes)*
Sem usar computador, analise o trecho abaixo e faça o rastreamento completo:

```c
for (int i = 1; i <= 4; i++) {
    for (int j = 1; j <= i; j++) {
        printf("%3d", i * j);
    }
    printf("\n");
}
```

1. Liste todos os pares `(i, j)` executados na ordem em que ocorrem e informe o total de iterações do laço interno.
2. Desenhe a saída exata impressa no terminal, respeitando os espaços gerados por `%3d` e as quebras de linha `\n`.

---

### `C09-E02` *(Caça ao Bug — `printf("\n")` Mal Posicionado e Limite Invertido)*
Um estudante tentou escrever um programa para ler um inteiro positivo `n` e imprimir um triângulo numérico crescente com `n` linhas usando `%3d` (ex.: para `n = 3`: linha 1 com `  1`, linha 2 com `  1  2`, linha 3 com `  1  2  3`):

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    if (n <= 0) {
        printf("Entrada Invalida\n");
        return 0;
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) { // Bug 1: limite independente
            printf("%3d", j);
            printf("\n");              // Bug 2: quebra dentro do laco interno
        }
    }

    return 0;
}
```

1. Explique o efeito visual de cada um dos 2 bugs quando `n = 3`.
2. Escreva o programa corrigido completo em C99 ([C09_E02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C09_E02_corrigido.c)).

---

### `C09-E03` *(Completar — Grade de Tabuada Formatada $L \times C$)*
Complete a lógica de laços aninhados no programa ([C09_E03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C09_E03.c)) que lê dois inteiros `linhas` e `cols`:
- Se `linhas <= 0 || cols <= 0`, imprima `Entrada Invalida\n` e encerre.
- Caso contrário, imprima uma grade de `linhas` linhas por `cols` colunas onde cada célula `(i, j)` ($1 \le i \le \text{linhas}$, $1 \le j \le \text{cols}$) exibe o produto `i * j` formatado com `%4d`.
- Quebre a linha com `\n` exatamente ao final de cada linha `i`.

*Exemplo de entrada:* `3 4`  
*Saída esperada:*
```text
   1   2   3   4
   2   4   6   8
   3   6   9  12
```

---

### Sessão 2 (`C09-E04` a `C09-E06` — Padrões Dependentes, Calendário e Moldura)

### `C09-E04` *(Triângulo Numérico Invertido com Pistas)*
Escreva um programa completo em C99 ([C09_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C09_E04.c)) que leia um inteiro `n`.
- Se `n <= 0`, imprima `Entrada Invalida\n`.
- Caso contrário, utilize um laço externo decrescente (`i` de `n` até `1`) e um laço interno crescente (`j` de `1` até `i`) para imprimir cada número `j` com largura `%3d`, quebrando a linha após cada linha `i`.

*Exemplo de entrada:* `4`  
*Saída esperada:*
```text
  1  2  3  4
  1  2  3
  1  2
  1
```

---

### `C09-E05` *(Calendário Mensal Formatado — Lista 5 Ex. 6 UTFPR)*
Adaptação da questão 6 da Lista 5 da UTFPR. Escreva um programa completo em C99 ([C09_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C09_E05.c)) que leia dois inteiros: `dias` (quantidade de dias do mês, de `28` a `31`) e `inicio` (dia da semana em que cai o dia 1: `1` = Dom, `2` = Seg, ..., `7` = Sab).
- Se `dias < 28 || dias > 31 || inicio < 1 || inicio > 7`, imprima `Entrada Invalida\n` e encerre.
- Caso contrário:
  1. Imprima o cabeçalho exato: `Dom Seg Ter Qua Qui Sex Sab\n`
  2. Imprima `inicio - 1` blocos de 4 espaços (`"    "`) para posicionar o dia `1` na coluna correta.
  3. Para cada dia `d` de `1` até `dias`: imprima o dia com `%3d`. Se o dia fechar um sábado (`(inicio - 1 + d) % 7 == 0`) ou for o último dia (`d == dias`), imprima `\n`; caso contrário, imprima um espaço `" "` separador de coluna.

*Exemplo de entrada:* `30 3`  
*Saída esperada:*
```text
Dom Seg Ter Qua Qui Sex Sab
          1   2   3   4   5
  6   7   8   9  10  11  12
 13  14  15  16  17  18  19
 20  21  22  23  24  25  26
 27  28  29  30
```

---

### `C09-E06` *(Moldura Retangular Oca com Laços Aninhados)*
Escreva um programa completo em C99 ([C09_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C09_E06.c)) que leia dois inteiros `linhas` e `cols`.
- Se `linhas < 2 || cols < 2`, imprima `Entrada Invalida\n`.
- Caso contrário, utilize dois laços aninhados (`i` de `1` a `linhas`, `j` de `1` a `cols`) para desenhar uma moldura retangular: imprima `'#'` quando estiver na primeira/última linha ou na primeira/última coluna (`i == 1 || i == linhas || j == 1 || j == cols`), e espaço `' '` no interior, com `\n` ao final de cada linha.

*Exemplo de entrada:* `4 5`  
*Saída esperada:*
```text
#####
#   #
#   #
#####
```

---

## 4. Checagem Independente de Domínio (`C09-C01` a `C09-C03`)

> **Instruções:** Resolva estas 3 questões sem consulta a materiais ou gabaritos. Tempo limite: 18 minutos. Exige **100% de acerto (3/3)**.

### `C09-C01` *(Teste de Mesa — Pares `(i, j)` Dependentes)*
Sem usar computador, execute o teste de mesa completo para o trecho abaixo:

```c
for (int i = 1; i <= 4; i++) {
    for (int j = i; j <= 4; j++) {
        printf("%2d", i + j);
    }
    printf("\n");
}
```

1. Liste os pares `(i, j)` executados em cada valor de `i` e indique o número total de chamadas a `printf("%2d", i + j)`.
2. Desenhe a saída exata produzida no terminal.

---

### `C09-C02` *(Caça ao Bug — Grade Sequencial com Quebra e Largura Incorretas)*
Um programa deveria ler `linhas` e `cols` positivos e imprimir os números de `1` até `linhas * cols` em forma de tabela retangular alinhada com `%3d` (ex.: `3 4` imprime 3 linhas com 4 números cada, de `  1` a ` 12`):

```c
#include <stdio.h>

int main(void) {
    int linhas, cols;
    scanf("%d %d", &linhas, &cols);

    if (linhas <= 0 || cols <= 0) {
        printf("Entrada Invalida\n");
        return 0;
    }

    int num = 1;
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d", num++); // Erro 1: sem largura fixa nem separacao
            printf("\n");        // Erro 2: quebra de linha no laco interno
        }
    }

    return 0;
}
```

1. Explique por que o código falha tanto no alinhamento das colunas quanto na formatação das linhas.
2. Escreva a versão corrigida completa em C99 ([C09_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C09_C02_corrigido.c)) usando `%3d` e posicionamento correto de `printf("\n")`.

---

### `C09-C03` *(Programa Completo — Triângulo de Floyd com Largura Fixa)*
Escreva um programa completo em C99 ([C09_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C09_C03.c)) que leia um inteiro `n`.
- Se `n <= 0`, imprima `Entrada Invalida\n`.
- Caso contrário, imprima as `n` primeiras linhas do **Triângulo de Floyd**, no qual a linha `i` ($1 \le i \le n$) contém `i` números inteiros consecutivos iniciados em `1`, cada um formatado com largura fixa `%3d` (`printf("%3d", num++);`) e quebra `\n` ao fim de cada linha.

*Exemplo de entrada:* `4`  
*Saída esperada:*
```text
  1
  2  3
  4  5  6
  7  8  9 10
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `C10` (`Revisão e Consolidação do Estágio C`):** somente após autocorreção dos exercícios `C09-E01..E06` **e** **100% de acerto (3/3)** na Checagem Independente `C09-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** refazer o rastreamento linha a linha de `(i, j)` separando claramente o que pertence ao laço interno (células) do que pertence ao laço externo (`printf("\n")`).
- **Após 2 tentativas malsucedidas:** retornar a **`C05`** (laço contado `for` e limites *off-by-one*) e **`C06`** (rastreamento rigoroso de `for`).

---

## 6. Referências do Orientador
- `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 2 (22/09 — Laços aninhados).
- `[DOC]` `Aula_11_Algoritmos.pdf` p. 4–9 (execução $M \times N$, limites dependentes `j <= i` e formatação tabular).
- `[DOC]` `Lista5_Algoritmos.pdf` p. 2–3 (Ex. 6 — calendário mensal com alinhamento tabular).
- Casos de teste e soluções verificáveis: [C09_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/gabaritos/C09_gabarito.md) e [C09_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/C09_testes.md).
