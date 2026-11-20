# Bloco `C04` — Repetição com Pós-Condição (`do-while`) e Menus Interativos

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio C — Estruturas de Repetição e Rastreamento de Laços / **`C04`** |
| **Micro-habilidade foco** | Implementar laços com teste ao final `do { ... } while (condicao);` garantindo pelo menos uma execução em validação de entrada e menus interativos com `switch`. |
| **Pré-requisitos** | `C01` *(Repetição com Pré-Condição `while`)*, `B09` *(Combinação de `switch` com `if` e Caixa Eletrônico)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão 1 (`E01`–`E05`, 20 min):** `12 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Não utilize** laço `for`, comandos de salto `break` ou `continue` em laços (`break` é permitido **apenas** para encerrar cada `case` dentro de `switch`), vetores (`char[]`, `int[]`, `v[i]`) ou funções customizadas além de `int main(void)`. Saídas `printf` devem ser estritamente em ASCII puro (sem acentos). |

### Registro das Sessões (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Sintaxe do `do-while` (Ponto e Vírgula Obrigatório):**
   ```c
   do {
       /* corpo executado ao menos 1 vez */
   } while (condicao);   /* <-- PONTO E VIRGULA OBRIGATORIO */
   ```
   - Diferentemente do `while` e do `for`, o `do-while` **exige** `;` logo após os parênteses da condição. Esquecê-lo provoca erro de compilação.
2. **Teste ao Final e Execução Mínima Garantida:**
   - **No `while` (pré-teste):** a condição é avaliada *antes* do corpo; se for falsa de início, o corpo executa **0 vezes**.
   - **No `do-while` (pós-teste):** o corpo executa **primeiro**, e só depois `condicao` é testada. Logo, o corpo sempre executa **pelo menos 1 vez**, mesmo que `condicao` já seja falsa na entrada.
3. **Validação de Entrada em Faixa:**
   - Para garantir que um valor digitado pertença a um intervalo válido (ex.: nota entre `0` e `10`), repita a leitura **enquanto o valor for inválido**:
     `while (nota < 0 || nota > 10);`
   - **Atenção à negação:** A condição do `do-while` descreve quando **continuar repetindo** (ou seja, quando o dado ainda é inválido), não quando parar.
4. **Menus Interativos (`do-while` + `switch`):**
   - Um menu sempre precisa ser exibido/lido ao menos uma vez, tornando o `do-while` a escolha natural:
     - Leia `opcao` dentro do `do { ... }`.
     - Despache a ação com `switch (opcao)` usando `break` apenas ao final de cada `case` e tratando entradas desconhecidas em `default`.
     - Repita `while (opcao != 0);` (ou até o código escolhido para sair).

---

## 2. Exemplos Guiados

### Exemplo 1 — Comparação direta `while` vs. `do-while` *(Trecho ilustrativo)*
Considere `int x = 10;` em ambos os trechos:

**Com `while` (pré-teste):**
```c
int x = 10;
while (x < 5) {
    printf("while: %d\n", x);
    x++;
}
printf("Apos while: %d\n", x);
```
- `10 < 5` é **Falso** na 1ª verificação $\rightarrow$ o corpo executa **0 vezes**.
- Saída: `Apos while: 10`.

**Com `do-while` (pós-teste):**
```c
int x = 10;
do {
    printf("do-while: %d\n", x);
    x++;
} while (x < 5);
printf("Apos do-while: %d\n", x);
```
- O corpo executa **antes** do teste: imprime `do-while: 10` e altera `x` para `11`.
- Só então testa `11 < 5` (**Falso**), encerrando o laço após **1 execução**.
- Saída:
  ```text
  do-while: 10
  Apos do-while: 11
  ```

---

### Exemplo 2 — Validação de entrada positiva com `do-while` *(Programa completo)*
O programa lê a idade de um aluno garantindo que seja estritamente positiva (`idade > 0`), repetindo a leitura caso contrário:

```c
#include <stdio.h>

int main(void) {
    int idade;

    do {
        scanf("%d", &idade);
        if (idade <= 0) {
            printf("Idade invalida\n");
        }
    } while (idade <= 0);

    printf("Idade valida: %d\n", idade);
    return 0;
}
```
- Entrada `0 -3 19` $\rightarrow$ imprime `Idade invalida` duas vezes e depois `Idade valida: 19`.
- Entrada `21` $\rightarrow$ `21 <= 0` é falso ao final da 1ª volta $\rightarrow$ imprime diretamente `Idade valida: 21`.

---

## 3. Exercícios (`C04-E01` a `C04-E05`)

### `C04-E01` *(Teste de Mesa / Comparação `while` vs. `do-while`)*
Sem usar o computador, trace a execução passo a passo dos dois trechos abaixo, indicando a saída exata na tela, o número de iterações executadas e o valor final da variável de controle:

**Trecho A:**
```c
int a = 8;
while (a <= 5) {
    printf("%d ", a);
    a++;
}
printf("Fim=%d\n", a);
```

**Trecho B:**
```c
int b = 8;
do {
    printf("%d ", b);
    b++;
} while (b <= 5);
printf("Fim=%d\n", b);
```

**Trecho C:**
```c
int k = 1;
do {
    printf("%d ", k);
    k += 2;
} while (k <= 5);
printf("Fim=%d\n", k);
```

---

### `C04-E02` *(Caça ao Bug — Falta de `;` e Condição Invertida na Validação)*
Um estudante escreveu o programa abaixo para ler uma nota inteira válida entre `0` e `10` (inclusive), exibindo `Nota invalida\n` a cada tentativa fora do intervalo:

```c
#include <stdio.h>

int main(void) {
    int nota;

    do {
        scanf("%d", &nota);
        if (nota < 0 || nota > 10) {
            printf("Nota invalida\n");
        }
    } while (nota >= 0 && nota <= 10)   /* Bugs aqui */

    printf("Nota registrada: %d\n", nota);
    return 0;
}
```
1. Qual erro de sintaxe impede a compilação na linha do `while`?
2. Supondo apenas o erro de sintaxe corrigido, o que ocorre logicamente se o usuário digitar `8` (nota válida)? E se digitar `-2` (nota inválida)?
3. Escreva a versão corrigida completa e compilável em C ([C04_E02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C04_E02_corrigido.c)).

---

### `C04-E03` *(Completar Solução — Validação de Divisor Não-Nulo)*
O programa abaixo lê um `numerador` real (`double`) e, em seguida, exige que o usuário digite um `divisor` real diferente de zero (`0.0`). Enquanto o divisor for zero, imprime `Divisor invalido\n`. Ao obter um divisor válido, imprime `Resultado: %.2f\n`. Complete as lacunas `/* A */`, `/* B */` e `/* C */`:

```c
#include <stdio.h>

int main(void) {
    double numerador, divisor;

    scanf("%lf", &numerador);

    /* A: palavra-chave de inicio do laco pos-teste */ {
        scanf("%lf", &divisor);
        if (divisor == 0.0) {
            /* B: mensagem de erro */;
        }
    } /* C: clausula while com condicao e ponto-e-virgula */

    printf("Resultado: %.2f\n", numerador / divisor);
    return 0;
}
```

---

### `C04-E04` *(Completar Solução — Menu Interativo de Caixa Eletrônico)*
Complete o programa em C que inicia `saldo = 100.0` e apresenta um menu interativo em laço `do-while` repetido enquanto `opcao != 0`.  
Regras das opções lidas via `scanf`:
- `1`: lê `double valor`; se `valor > 0.0`, soma ao `saldo` e imprime `Saldo: %.2f\n`; senão imprime `Valor invalido\n`.
- `2`: lê `double valor`; se `valor > 0.0 && valor <= saldo`, subtrai do `saldo` e imprime `Saldo: %.2f\n`; senão imprime `Operacao invalida\n`.
- `3`: imprime `Saldo: %.2f\n`.
- `0`: imprime `Encerrando\n`.
- Outra opção: imprime `Opcao invalida\n`.

Complete as lacunas `/* Lacuna 1 */`, `/* Lacuna 2 */` e `/* Lacuna 3 */`:
```c
#include <stdio.h>

int main(void) {
    double saldo = 100.0;
    double valor;
    int opcao;

    do {
        scanf("%d", &opcao);
        switch (/* Lacuna 1 */) {
            case 1:
                scanf("%lf", &valor);
                if (valor > 0.0) {
                    saldo += valor;
                    printf("Saldo: %.2f\n", saldo);
                } else {
                    printf("Valor invalido\n");
                }
                break;
            case 2:
                scanf("%lf", &valor);
                if (valor > 0.0 && valor <= saldo) {
                    saldo -= valor;
                    printf("Saldo: %.2f\n", saldo);
                } else {
                    printf("Operacao invalida\n");
                }
                break;
            case 3:
                printf("Saldo: %.2f\n", saldo);
                break;
            case 0:
                printf("Encerrando\n");
                break;
            /* Lacuna 2: tratamento de opcoes invalidas */:
                printf("Opcao invalida\n");
                break;
        }
    } /* Lacuna 3: condicao de continuacao do menu com ';' */

    return 0;
}
```

---

### `C04-E05` *(Programa Completo Independente — Menu Acumulador de Total)*
Escreva um programa completo em C ([C04_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C04_E05.c)) que mantenha um acumulador inteiro `total` iniciado em `0` e execute um menu em laço `do-while` com `switch` até que o usuário digite `0`:
- Opção `1`: lê um inteiro `v`, soma `v` a `total` e imprime `Total: %d\n`.
- Opção `2`: lê um inteiro `v`, subtrai `v` de `total` e imprime `Total: %d\n`.
- Opção `3`: zera `total = 0` e imprime `Total: %d\n`.
- Opção `0`: imprime `Final: %d\n` e encerra o laço.
- Qualquer outro inteiro: imprime `Opcao invalida\n`.

*Exemplo de entrada:* `1 50 2 15 9 0`  
*Saída esperada:*
```text
Total: 50
Total: 35
Opcao invalida
Final: 35
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `C04-C01` *(Teste de Mesa / Previsão Comparativa `while` vs. `do-while`)*
Sem usar o computador, considere que o usuário digite `5` para `n` em ambos os trechos:

**Trecho 1:**
```c
int n;
scanf("%d", &n);
while (n < 5) {
    n += 2;
    printf("%d ", n);
}
printf("Fim: %d\n", n);
```

**Trecho 2:**
```c
int n;
scanf("%d", &n);
do {
    n += 2;
    printf("%d ", n);
} while (n < 5);
printf("Fim: %d\n", n);
```
1. Qual a saída exata e o número de iterações do **Trecho 1**?
2. Qual a saída exata e o número de iterações do **Trecho 2**?
3. Explique por que o comportamento divergiu mesmo com a condição `n < 5` falsa desde o início.

---

### `C04-C02` *(Caça ao Bug — Condição de Saída e Ponto e Vírgula em Menu)*
Analise o código abaixo de um contador de itens em menu:
```c
#include <stdio.h>

int main(void) {
    int op;
    int cont = 0;

    do {
        scanf("%d", &op);
        switch (op) {
            case 1:
                cont++;
                printf("Item adicionado\n");
                break;
            case 0:
                printf("Total: %d\n", cont);
                break;
            default:
                printf("Opcao invalida\n");
                break;
        }
    } while (op == 0)   /* Bugs aqui */

    return 0;
}
```
1. Identifique os dois erros na linha do `while`.
2. Supondo apenas o ponto e vírgula corrigido, o que ocorre para a entrada `1 0`? E para a entrada `0`?
3. Escreva a versão corrigida completa do programa ([C04_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C04_C02_corrigido.c)).

---

### `C04-C03` *(Programa Completo Independente — Menu de Calculadora com Validação Interna)*
Escreva um programa completo em C ([C04_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C04_C03.c)) utilizando `do-while` e `switch` que repita o menu abaixo enquanto `op != 0`:
- Opção `1` (Soma): lê dois inteiros `a` e `b` e imprime `Resultado: %d\n` com `a + b`.
- Opção `2` (Produto): lê dois inteiros `a` e `b` e imprime `Resultado: %d\n` com `a * b`.
- Opção `3` (Divisão inteira segura): lê o inteiro `a` e, usando um **`do-while` interno** para validar `b`, lê `b` repetidamente enquanto `b == 0`, imprimindo `Divisor invalido\n` a cada tentativa nula; ao obter `b != 0`, imprime `Resultado: %d\n` com `a / b`.
- Opção `0` (Sair): imprime `Saindo\n`.
- Outra opção: imprime `Opcao invalida\n`.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `C05` (`Laço Contado for: Sintaxe, Padrões de Contagem, C99 e Erros Off-by-One`):** somente após autocorreção dos exercícios `C04-E01..E05` **e** **100% (3/3)** na Checagem Independente `C04-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** revisar a obrigatoriedade do `;` após `while (condicao);`, o sentido lógico da condição de continuação na validação (`fora da faixa`) e o uso de `break` exclusivamente dentro de `switch`, aplicando a variante `V2` do bloco.
- **Após 2 tentativas malsucedidas:** retornar para **`C01`** (pré-teste vs. pós-teste no `while`) e **`B09`** (`switch/case` e validação combinada com `if`).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 1–2 (item 7 — *"pós-condição / teste no final"*).
- `[DOC]` `Aula_09_Algoritmos.pdf` p. 3, 22 (anúncio explícito da estrutura `do-while`).
- `[DOC]` `Aula_10_Algoritmos.pdf` p. 19, 22 (menção a `do`).
- `[DOC]` `Trabalho_Algoritmos.pdf` p. 3–4 (menu repetido até a escolha de saída).
- `[INF]` `00_inventario_fontes.md` Lacuna `L2` e Conflito `C1` (inclusão dedicada de `C04` para cobertura integral da ementa vigente).
- Casos de teste e soluções verificáveis: [C04_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/gabaritos/C04_gabarito.md) e [C04_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/C04_testes.md).
