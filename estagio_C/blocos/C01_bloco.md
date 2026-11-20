# Bloco `C01` — Repetição com Pré-Condição (`while`): Anatomia, Teste de Mesa e Pós-Condição

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio C — Estruturas de Repetição e Rastreamento de Laços / **`C01`** |
| **Micro-habilidade foco** | Construir e rastrear manualmente laços `while` identificando inicialização, condição pré-teste, atualização, caso de 0 execuções, laço infinito e invariante pós-laço. |
| **Pré-requisitos** | `B10` *(Revisão e Consolidação do Estágio B — Expressões e Condicionais)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão única de prática + checagem (22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Não utilize** laços `do-while` ou `for`, comandos de salto (`break`, `continue`), vetores (`char[]`, `int[]`) ou funções customizadas além de `main`. Use estritamente o laço `while`, tipos escalares (`int`, `double`), condicionais simples e E/S padrão com saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Conceito de Laço e Iteração:** Um laço repete um bloco de comandos enquanto uma condição lógica for verdadeira. Cada repetição completa do bloco chama-se **iteração**.
2. **Anatomia do `while`:** O laço com pré-condição possui quatro partes fundamentais:
   - **Inicialização:** Definição do valor inicial da variável de controle *antes* do laço.
   - **Condição de Pré-Teste:** `while (condicao)` avaliada *antes* de cada iteração.
   - **Corpo:** Bloco delimitado por `{ ... }` executado enquanto a condição for verdadeira.
   - **Atualização:** Modificação obrigatória da variável de controle no corpo do laço, caminhando em direção à falsidade da condição.
3. **Pré-Teste e 0 Execuções:** Como o teste ocorre *antes* de entrar no corpo, se a condição for falsa já na primeira avaliação, o corpo é executado exatamente **0 vezes**.
4. **Projeto de Laço em 3 Perguntas:** Antes de digitar código, responda mentalmente:
   - *Onde começa?* (Qual é a inicialização?)
   - *Onde para?* (Qual é a condição de parada/continuação?)
   - *Qual é o passo?* (Como a variável de controle é atualizada a cada iteração?)
5. **Garantia de Término e Causas de Laço Infinito:**
   - Esquecer de atualizar a variável de controle dentro do corpo.
   - Atualizar a variável na direção errada (ex.: somar quando deveria subtrair).
   - Colocar ponto-e-vírgula logo após o cabeçalho: `while (condicao);`. O `;` constitui um comando nulo que repete indefinidamente sem jamais executar o bloco entre chaves.
6. **Invariante Pós-Laço:** Ao término imediato de um laço `while (i <= n)`, tem-se a garantia lógica e matemática de que `i > n` (a condição tornou-se falsa).

---

## 2. Exemplos Guiados

### Exemplo 1 — Contagem progressiva e teste de mesa *(Trecho ilustrativo)*
Considere o seguinte trecho que imprime os números de 1 a 4:

```c
int i = 1;               /* Inicializacao */
while (i <= 4) {         /* Condicao de pre-teste */
    printf("%d\n", i);   /* Corpo */
    i++;                 /* Atualizacao */
}
/* Pos-laco: i vale 5 */
```

**Tabela de Teste de Mesa:**

| Passo / Linha | `i` antes do teste | Teste `i <= 4` | Saída na tela | `i` após atualização |
|:---:|:---:|:---:|:---:|:---:|
| Início | 1 | `1 <= 4` (V) | `1` | 2 |
| Iteração 2 | 2 | `2 <= 4` (V) | `2` | 3 |
| Iteração 3 | 3 | `3 <= 4` (V) | `3` | 4 |
| Iteração 4 | 4 | `4 <= 4` (V) | `4` | 5 |
| Saída | 5 | `5 <= 4` (F) | *(nenhuma)* | *(encerra o laço com `i = 5`)* |

Total de iterações executadas: **4**. Valor final da variável `i`: **5**.

---

### Exemplo 2 — Contagem regressiva com pré-teste falso imediato *(Programa completo)*
O programa abaixo lê um número inteiro `n` e imprime a contagem regressiva de `n` até 1. Se `n <= 0`, o laço executa 0 vezes.

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    while (n >= 1) {
        printf("%d\n", n);
        n--;
    }

    printf("Fim!\n");
    return 0;
}
```
- Se a entrada for `3`: imprime `3`, `2`, `1`, `Fim!`.
- Se a entrada for `0`: a condição `0 >= 1` é falsa logo na primeira verificação; o corpo executa 0 vezes e imprime apenas `Fim!`.

---

## 3. Exercícios (`C01-E01` a `C01-E05`)

### `C01-E01` *(Teste de Mesa / Previsão Mental)*
Sem usar o computador, preencha a tabela de rastreamento para cada um dos trechos abaixo, indicando a saída exata na tela, o número de iterações e o valor final da variável de controle:

**Trecho A:**
```c
int k = 1;
while (k < 5) {
    printf("%d ", k * 2);
    k++;
}
```

**Trecho B:**
```c
int w = 10;
while (w < 4) {
    printf("%d ", w);
    w++;
}
```

---

### `C01-E02` *(Caça ao Bug — Laço Infinito e Comando Nulo)*
Dois alunos cometeram erros conceituais graves ao tentar imprimir os inteiros de 1 a 5:

**Código do Aluno 1:**
```c
#include <stdio.h>

int main(void) {
    int i = 1;
    while (i <= 5) {
        printf("%d\n", i);
    }
    return 0;
}
```

**Código do Aluno 2:**
```c
#include <stdio.h>

int main(void) {
    int i = 1;
    while (i <= 5); {
        printf("%d\n", i);
        i++;
    }
    return 0;
}
```
1. Explique por que o Código do Aluno 1 entra em laço infinito.
2. Explique o efeito exato do caractere `;` após `while (i <= 5)` no Código do Aluno 2.
3. Escreva a versão corrigida completa e funcional do programa em C.

---

### `C01-E03` *(Completar Solução — Contagem Progressiva de 1 a N)*
O programa abaixo deve ler um inteiro positivo `n` e imprimir todos os inteiros de `1` até `n`, um por linha. Se `n <= 0`, nada deve ser impresso. Complete as lacunas `/* A */`, `/* B */` e `/* C */`:

```c
#include <stdio.h>

int main(void) {
    int n, i;
    scanf("%d", &n);

    i = /* A */;
    while (/* B */) {
        printf("%d\n", i);
        /* C */;
    }

    return 0;
}
```

---

### `C01-E04` *(Completar Solução — Contagem Regressiva Par com Passo 2)*
O programa a seguir deve ler um número inteiro positivo `n` e imprimir, em ordem decrescente, todos os números pares a partir do maior número par menor ou igual a `n`, até chegar em `0`.  
Exemplo: se `n = 7`, o maior par `<= 7` é 6, logo imprime `6`, `4`, `2`, `0`. Se `n = 8`, imprime `8`, `6`, `4`, `2`, `0`. Complete as lacunas:

```c
#include <stdio.h>

int main(void) {
    int n, atual;
    scanf("%d", &n);

    if (n % 2 != 0) {
        atual = n - 1;
    } else {
        atual = n;
    }

    while (/* Lacuna 1: condicao */) {
        printf("%d\n", atual);
        /* Lacuna 2: atualizacao com passo 2 */;
    }

    return 0;
}
```

---

### `C01-E05` *(Resolução Independente — Intervalo Fechado [A, B])*
Escreva um programa completo em C que leia dois números inteiros `a` e `b`.  
Usando estritamente um laço `while`, imprima todos os números inteiros pertencentes ao intervalo fechado $[a, b]$ (ou seja, de `a` até `b`, inclusive), um por linha.  
Se $a > b$, o laço não deve executar nenhuma iteração (saída vazia).

Exemplo de entrada:
```text
3 7
```
Exemplo de saída:
```text
3
4
5
6
7
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `C01-C01` *(Teste de Mesa / Avaliação de Iterações com Pré-Teste)*
Sem usar o computador, analise o trecho a seguir:

```c
int x = 2;
while (x <= 10) {
    printf("%d\n", x);
    x += 3;
}
```
1. Quais valores exatos serão impressos na tela?
2. Quantas iterações foram executadas?
3. Qual é o valor final armazenado em `x` após o encerramento do laço?
4. Se o valor inicial fosse `int x = 12;`, quantas iterações seriam executadas?

---

### `C01-C02` *(Teste de Mesa / Laço Regressivo com Condição Estrita)*
Sem usar o computador, analise o trecho a seguir:

```c
int c = 10;
while (c > 3) {
    c -= 2;
    printf("%d\n", c);
}
```
1. Note que a atualização `c -= 2;` ocorre *antes* do `printf`. Quais números serão impressos?
2. Quantas iterações foram executadas?
3. Qual o valor final de `c` ao término do laço?

---

### `C01-C03` *(Programa Completo Independente — Intervalo com Passo Personalizado)*
Escreva um programa completo em C que leia três números inteiros: `inicio`, `fim` e `passo` (considere que `passo > 0`).  
Usando um laço `while`, o programa deve imprimir os valores a partir de `inicio`, incrementando de `passo` em `passo`, enquanto o valor for menor ou igual a `fim`. Cada valor deve ser impresso em uma linha separada.  
Se `inicio > fim`, nada deve ser impresso.

Exemplo de entrada:
```text
2 11 3
```
Exemplo de saída:
```text
2
5
8
11
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `C02` (`Contadores e Acumuladores com while`):** somente após autocorreção dos exercícios `C01-E01..E05` **e** **100% (3/3)** na Checagem Independente `C01-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** revisar as três perguntas fundamentais do projeto de laços (início, condição de parada e passo), refazer a tabela de teste de mesa do Exemplo 1 no papel e aplicar a variante `V2` do bloco.
- **Após 2 tentativas malsucedidas:** retornar para **`B02`** (atribuições compostas e incremento `++`) e **`B10`** (estruturas de controle do Estágio B).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 7 — Estruturas de repetição: pré-condição `while`).
- `[DOC]` `Aula_09_Algoritmos.pdf` p. 4–12, 16–18 (Conceito de repetição, sintaxe do `while`, tabela de rastreamento e armadilha do `;`).
- `[DOC]` `Lista4_Algoritmos.pdf` p. 1 (Ex. 1 e 2 — contagem progressiva e regressiva com `while`).
- Casos de teste e soluções verificáveis: [C01_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/gabaritos/C01_gabarito.md) e [C01_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/C01_testes.md).
