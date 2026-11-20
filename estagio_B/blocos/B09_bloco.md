# Bloco `B09` — Combinação de `switch` com `if`, `switch` Aninhado e Colapso de Intervalos

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio B — Expressões, Operadores e Estruturas Condicionais / **`B09`** |
| **Micro-habilidade foco** | Integrar `if / else` dentro de ramos `case`, construir `switch` aninhados dominando o alcance local do `break` e colapsar intervalos numéricos contínuos em rótulos discretos via divisão inteira (`n / 10`). |
| **Pré-requisitos** | `B06` *(Operadores Lógicos)*, `B07` *(Condicionais Aninhadas)*, `B08` *(Múltipla Escolha com `switch`)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 20 min):** `12 min` resol. \| `5 min` corr. \| `3 min` recup.; **Sessão 2 (`E04`–`E06`, 20 min):** `12 min` resol. \| `5 min` corr. \| `3 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Não utilize** laços (`while`, `for`, `do-while`), vetores/strings (`char[]`), ou funções além de `main`. Toda validação de faixa prévia deve anteceder o `switch`. Saídas estritamente em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **`switch` com `if` Interno:**
   - O `switch` atua frequentemente como seletor principal da operação desejada (ex.: opções de menu de caixa eletrônico).
   - Dentro de cada `case`, estruturas `if / else` executam a validação de regras de negócio específicas daquela operação (ex.: saldo suficiente, valores positivos).
2. **Alcance Local do `break` em `switch` Aninhado:**
   - Um `switch` pode estar contido dentro de um dos `case`s de outro `switch`.
   - **Regra fundamental:** O comando `break` encerra **apenas o `switch` mais interno** em que está contido. Ele **jamais** encerra o `switch` externo!
   - Portanto, após sair do `switch` interno, o `case` externo ainda necessita de seu próprio `break` para não causar *fall-through* indesejado no nível superior.
3. **Técnica de Colapso de Intervalos (`val / 10`):**
   - O `switch` não aceita intervalos relacionais (como `< 50` ou `60..70`).
   - Contudo, para variáveis inteiras com faixas de 10 em 10 (ex.: notas de 0 a 100), podemos mapear o intervalo para um único dígito usando a divisão inteira `nota / 10`:
     - Notas de 90 a 99 $\rightarrow$ `nota / 10 == 9`
     - Notas de 80 a 89 $\rightarrow$ `nota / 10 == 8`
     - Nota 100 $\rightarrow$ `nota / 10 == 10`
   - **Obrigatoriedade de Validação Prévia:** Antes de aplicar `switch (nota / 10)`, deve-se obrigatoriamente validar se `nota < 0 || nota > 100` via `if` preliminar, evitando que notas inválidas como `-5` ou `150` sejam mapeadas erroneamente pelo `default`.

---

## 2. Exemplos Guiados

### Exemplo 1 — `switch` Aninhado e o Alcance do `break` *(Trecho ilustrativo)*
Observe o fluxo em dois níveis:

```c
int categoria = 1, item = 2;

switch (categoria) {
    case 1:
        printf("Cat 1: ");
        switch (item) {
            case 1: printf("A\n"); break;
            case 2: printf("B\n"); break; /* Sai SOMENTE do switch interno! */
            default: printf("Outro\n"); break;
        }
        break; /* OBRIGATORIO: Sai do switch externo (categoria) */

    case 2:
        printf("Cat 2\n");
        break;
}
```
Se esquecermos o `break` do `case 1:` externo, após imprimir `"Cat 1: B\n"`, a execução continuaria caindo no `case 2:` e imprimiria também `"Cat 2\n"`!

### Exemplo 2 — Mapeamento de Notas com `if` prévio e `switch (nota / 10)` *(Programa completo)*

```c
#include <stdio.h>

int main(void) {
    int nota;
    scanf("%d", &nota);

    /* 1º Passo: Validacao de limites antes do switch */
    if (nota < 0 || nota > 100) {
        printf("Nota Invalida\n");
    } else {
        /* 2º Passo: Colapso do intervalo por divisao inteira */
        switch (nota / 10) {
            case 10:
            case 9:
                printf("Conceito A\n");
                break;
            case 8:
                printf("Conceito B\n");
                break;
            case 7:
                printf("Conceito C\n");
                break;
            case 6:
                printf("Conceito D\n");
                break;
            default: /* Abrange 0, 1, 2, 3, 4, 5 (notas de 0 a 59) */
                printf("Conceito F\n");
                break;
        }
    }

    return 0;
}
```

---

## 3. Exercícios (`B09-E01` a `B09-E06`)

### Sessão 1 (`B09-E01` a `B09-E03` — Rastreio de Níveis e Colapso)

### `B09-E01` *(Teste de Mesa — Switch Aninhado e Escopo do Break)*
Sem usar computador, analise o código:

```c
int grupo = 1, subgrupo = 1;

switch (grupo) {
    case 1:
        printf("G1-");
        switch (subgrupo) {
            case 1:
                printf("S1 ");
                break;
            case 2:
                printf("S2 ");
                break;
        }
        /* ATENCAO: Sem break no case 1 externo! */
    case 2:
        printf("G2 ");
        break;
    default:
        printf("Outro ");
        break;
}
printf("\n");
```
1. Qual é a saída impressa para `grupo = 1` e `subgrupo = 1`?
2. Qual é a saída impressa para `grupo = 1` e `subgrupo = 2`?
3. O que deve ser inserido logo após o término do `switch (subgrupo)` para isolar o `case 1` do `case 2` externo?

---

### `B09-E02` *(Teste de Mesa — Colapso por Divisão Inteira)*
Considere o cálculo `faixa = pontos / 10` (com `int pontos` entre `0` e `50`):
- `case 5:` imprime `Nivel 5\n`
- `case 4:` imprime `Nivel 4\n`
- `case 3:` imprime `Nivel 3\n`
- `default:` imprime `Nivel Inicial\n`

Informe a saída para cada uma das entradas:
a) `pontos = 50`  
b) `pontos = 48`  
c) `pontos = 39`  
d) `pontos = 25`  
e) `pontos = 4`  

---

### `B09-E03` *(Caça ao Bug — Break no Nível Incorreto)*
O programa abaixo implementa um cardápio com seleção de refeição e acompanhamento. Há um defeito grave de *fall-through* externo e falta de tratamento de erro:

```c
#include <stdio.h>

int main(void) {
    int prato, bebida;
    scanf("%d %d", &prato, &bebida);

    switch (prato) {
        case 1:
            printf("Prato: Peixe\n");
            switch (bebida) {
                case 1: printf("Bebida: Suco\n"); break;
                case 2: printf("Bebida: Agua\n"); break;
            }
            /* BUG: faltou break aqui! */
        case 2:
            printf("Prato: Frango\n");
            break;
        default:
            printf("Prato Invalido\n");
            break;
    }

    return 0;
}
```
1. O que é impresso quando a entrada for `1 1`?
2. Escreva o programa corrigido completo em C ([B09_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B09_E03_corrigido.c)) garantindo que:
   - Se `prato == 1`: imprime `Prato: Peixe\n`; se `bebida == 1` imprime `Bebida: Suco\n`; se `bebida == 2` imprime `Bebida: Agua\n`; qualquer outra bebida imprime `Bebida Invalida\n`.
   - Se `prato == 2`: imprime `Prato: Frango\n`; se `bebida == 1` imprime `Bebida: Suco\n`; se `bebida == 2` imprime `Bebida: Agua\n`; qualquer outra bebida imprime `Bebida Invalida\n`.
   - Qualquer outro prato: imprime `Prato Invalido\n`.

---

### Sessão 2 (`B09-E04` a `B09-E06` — Escrita Guiada → Independente)

### `B09-E04` *(Variação controlada — Caixa Eletrônico com switch e if interno)*
Escreva um **programa completo** em C que simule um terminal bancário com saldo inicial fixo de `R$ 1000.00` (`double saldo = 1000.00;`).
O programa deve ler o código da operação (`int op`) e, se aplicável, o valor da transação (`double valor`):
- `case 1:` (Saque)
  - Lê `scanf("%lf", &valor);`
  - Se `valor <= 0.0`: imprima `Valor Invalido\n`
  - Senão se `valor > saldo`: imprima `Saldo Insuficiente\n`
  - Senão: debita do saldo (`saldo = saldo - valor;`) e imprima `Saldo Atual: R$ %.2f\n`
- `case 2:` (Depósito)
  - Lê `scanf("%lf", &valor);`
  - Se `valor <= 0.0`: imprima `Valor Invalido\n`
  - Senão: credita no saldo (`saldo = saldo + valor;`) e imprima `Saldo Atual: R$ %.2f\n`
- `case 3:` (Consulta Saldo)
  - Imprima `Saldo Atual: R$ %.2f\n` com o saldo atual.
- `default:`
  - Imprima `Operacao Invalida\n`.

Arquivo correspondente: [B09_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B09_E04.c).

---

### `B09-E05` *(Colapso de Faixas — Classificador de Conceitos A-F)*
Escreva um **programa completo** em C que leia uma nota inteira (`int nota`).
1. Valide a nota: se for menor que `0` ou maior que `100`, imprima `Nota Invalida\n`.
2. Se válida, utilize `switch (nota / 10)` com rótulos agrupados:
   - `10` ou `9`: imprima `Conceito A\n`
   - `8`: imprima `Conceito B\n`
   - `7`: imprima `Conceito C\n`
   - `6`: imprima `Conceito D\n`
   - `0` a `5` (`default`): imprima `Conceito F\n`

Arquivo correspondente: [B09_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B09_E05.c).

---

### `B09-E06` *(Resolução independente — Totem de Autoatendimento com switch Aninhado)*
Escreva um **programa completo** em C que leia dois números inteiros: `categoria` e `item` (`scanf("%d %d", &categoria, &item);`).
Estruture a solução com um `switch (categoria)` contendo `switch (item)` aninhados em cada ramo:
- `categoria == 1` (Bebidas):
  - `item == 1`: imprima `Suco Natural: R$ 7.00\n`
  - `item == 2`: imprima `Refrigerante: R$ 5.00\n`
  - `default`: imprima `Item Invalido\n`
- `categoria == 2` (Lanches):
  - `item == 1`: imprima `Sanduiche: R$ 12.00\n`
  - `item == 2`: imprima `Hamburguer: R$ 18.00\n`
  - `default`: imprima `Item Invalido\n`
- `default` (categoria inexistente):
  - Imprima `Categoria Invalida\n`

Arquivo correspondente: [B09_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B09_E06.c).

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `B09-C01` *(Teste de Mesa — Rastreamento de Switch Aninhado com Fall-Through)*
Considere o seguinte trecho:

```c
int a = 1, b = 2;

switch (a) {
    case 1:
        printf("A1 ");
        switch (b) {
            case 1: printf("B1 "); break;
            case 2: printf("B2 ");
            case 3: printf("B3 "); break;
            default: printf("BX "); break;
        }
        break;
    case 2:
        printf("A2 ");
        break;
    default:
        printf("AX ");
        break;
}
printf("\n");
```
1. Qual será a saída se `a = 1` e `b = 2`?
2. Qual será a saída se `a = 1` e `b = 4`?
3. Qual será a saída se `a = 2` e `b = 1`?

---

### `B09-C02` *(Programa completo — Faixas Etárias Decimais com colapso `idade / 10`)*
Escreva um programa completo em C que leia a idade de uma pessoa (`int idade`).
- Primeiro teste com `if`: se `idade < 0 || idade > 120`, imprima `Idade Invalida\n`.
- Se válida, use `switch (idade / 10)`:
  - `0` (0 a 9 anos): imprima `Crianca\n`
  - `1` (10 a 19 anos): imprima `Jovem\n`
  - `2`, `3`, `4`, `5` (20 a 59 anos): imprima `Adulto\n`
  - `6` ou mais (`6..12`, use `default` já validado): imprima `Idoso\n`

Arquivo correspondente: [B09_C02.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B09_C02.c).

---

### `B09-C03` *(Programa completo — Central Telefônica com Switch Aninhado e Defaults)*
Escreva um programa completo em C que receba dois dígitos de discagem: `int setor, int ramal;` (`scanf("%d %d", &setor, &ramal);`).
- Se `setor == 1` (Suporte Técnico):
  - `ramal == 1`: imprima `Hardware\n`
  - `ramal == 2`: imprima `Software\n`
  - `default`: imprima `Ramal Invalido\n`
- Se `setor == 2` (Financeiro):
  - `ramal == 1`: imprima `Contas a Pagar\n`
  - `ramal == 2`: imprima `Contas a Receber\n`
  - `default`: imprima `Ramal Invalido\n`
- Qualquer outro setor (`default` externo):
  - Imprima `Setor Invalido\n`

Arquivo correspondente: [B09_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B09_C03.c).

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `B10` (`Revisão e Consolidação do Estágio B`):** somente após autocorreção dos exercícios `B09-E01..E06` **e** **100% (3/3)** na Checagem Independente `B09-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** verificar se o `break` do `switch` interno não foi confundido com o `break` do `case` externo e conferir a validação estrita prévia antes da divisão inteira.
- **Após 2 tentativas malsucedidas:** retornar a **`B07`** (aninhamento e prioridade) e **`B08`** (`switch/case` isolado).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 6 — Condicionais aninhadas e seleção múltipla).
- `[DOC]` `Aula_08_Algoritmos_v2.pdf` p. 11–21 (`switch` aninhado, `if` dentro de `case`, colapso de faixas com `n / 10`).
- `[DOC]` `Lista3_Algoritmos.pdf` p. 2 (Ex. 3 e 4 — menus hierárquicos e classificação de conceitos).
- Casos de teste e soluções verificáveis: [B09_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/gabaritos/B09_gabarito.md) e [B09_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/B09_testes.md).
