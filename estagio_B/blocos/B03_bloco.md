# Bloco `B03` — Expressões Relacionais, Verdadeiro/Falso em C (`<stdbool.h>`) e `if` Simples

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio B — Expressões, Operadores e Estruturas Condicionais / **`B03`** |
| **Micro-habilidade foco** | Formular comparações relacionais (`==`, `!=`, `<`, `>`, `<=`, `>=`), compreender o modelo lógico de C (`0` falso / não-zero verdadeiro e `<stdbool.h>`) e controlar desvios simples com `if (...) { ... }`. |
| **Pré-requisitos** | `B02` *(Precedência aritmética, cast, `<math.h>` e atribuições compostas)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão única de prática + checagem (22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Não utilize** `else`, `else if`, `switch`, operadores lógicos (`&&`, `||`, `!`), laços (`while`, `for`) ou vetores neste bloco. Resolva problemas exclusivamente com `if` simples e operadores relacionais unitários (`==`, `!=`, `<`, `>`, `<=`, `>=`). Saídas estritamente em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Os 6 Operadores Relacionais:**  
   `==` (igual a), `!=` (diferente de), `<` (menor que), `>` (maior que), `<=` (menor ou igual a), `>=` (maior ou igual a).
2. **Modelo Booleano de C:** Em C clássico, não há tipo booleano nativo: **`0` é falso** e **qualquer valor diferente de zero é verdadeiro**. O C99 fornece o cabeçalho `<stdbool.h>`, que define o tipo `bool` e as constantes `true` (`1`) e `false` (`0`). Toda comparação relacional resulta numericamente em `1` (verdadeiro) ou `0` (falso).
3. **Sintaxe do `if` Simples:**  
   ```c
   if (condicao) {
       /* instrucoes executadas APENAS se a condicao for verdadeira (!= 0) */
   }
   ```
   Se a condição for falsa (`0`), o bloco delimitado por `{ }` é simplesmente ignorado e a execução prossegue sequencialmente.
4. **A Armadilha do `=` vs. `==`:**  
   - `x == 5` compara se `x` é igual a 5 (produz `1` ou `0`).  
   - `x = 5` **atribui** 5 à variável `x` e avalia o resultado da atribuição (`5`), que é não-zero (verdadeiro)! O `if (x = 5)` executa sempre e ainda altera o valor de `x`.
5. **A Armadilha do Ponto e Vírgula (`;`):**  
   Escrever `if (x > 0); { ... }` encerra a instrução do `if` em um comando nulo antes das chaves. O bloco `{ ... }` será executado **incondicionalmente**, mesmo quando `x <= 0`. **Nunca** coloque ponto e vírgula logo após o fecha-parêntese do `if`!
6. **Uso Obrigatório de Chaves `{ }`:** Embora o C permita omitir chaves quando há uma única instrução, adotamos o padrão defensivo de **sempre utilizar chaves** em todos os blocos `if`.

---

## 2. Exemplos Guiados

### Exemplo 1 — Teste de paridade com `%` e `==` *(Programa completo)*
Verificar se um número inteiro lido é par e emitir aviso:

```c
#include <stdio.h>

int main(void) {
    int num;
    scanf("%d", &num);

    if (num % 2 == 0) {
        printf("Numero par detectado\n");
    }

    printf("Fim\n");
    return 0;
}
```
Se a entrada for `8`: `8 % 2` é `0`, `0 == 0` é verdadeiro (`1`), imprime `Numero par detectado` e depois `Fim`.  
Se a entrada for `7`: `7 % 2` é `1`, `1 == 0` é falso (`0`), o bloco é ignorado e imprime apenas `Fim`.

### Exemplo 2 — Armadilha do `=` vs `==` *(Trecho ilustrativo)*
```c
int status = 0;

/* FORMA ERRADA: status recebe 1 e a condicao avalia para 1 (verdadeiro) */
if (status = 1) {
    printf("Ativo\n");   /* EXECUTA INDEVIDAMENTE! */
}

/* FORMA CORRETA: apenas compara sem alterar a variavel */
if (status == 1) {
    printf("Ativo\n");   /* Nao executa, pois status eh 0 */
}
```

---

## 3. Exercícios (`B03-E01` a `B03-E05`)

### `B03-E01` *(Tabela-Verdade de Expressões Relacionais)*
Considerando as variáveis inteiras `int a = 5, b = 8;`, determine o resultado numérico (`0` ou `1`) e o valor lógico (`false` ou `true`) de cada comparação em C:
1. `a == b`
2. `a != b`
3. `a < b`
4. `b <= 8`
5. `a > 5`
6. `a >= 5`
7. `b - a == 3`

---

### `B03-E02` *(Teste de Mesa — Múltiplos ifs Independentes)*
Sem usar o computador, analise o trecho a seguir para as duas entradas independentes `x = 12` e `x = 7`:

```c
if (x > 10) {
    printf("Maior que 10\n");
}
if (x % 2 == 0) {
    printf("Par\n");
}
if (x > 20) {
    printf("Maior que 20\n");
}
printf("Fim\n");
```
Para cada valor de `x`, escreva exatamente todas as linhas que serão impressas na tela.

---

### `B03-E03` *(Caça ao Bug — 4 Erros Clássicos de Sintaxe)*
Um estudante escreveu o seguinte código que apresenta múltiplos erros de sintaxe e de semântica lógica em C:

```c
#include <stdio.h>

int main(void) {
    int x;
    scanf("%d", &x);

    if x > 0;
        printf("Positivo\n");

    if (x = 10) {
        printf("Numero igual a 10\n");
    }

    printf("Fim\n");
    return 0;
}
```
Identifique os **4 erros** presentes (ausência de parênteses, ponto e vírgula após `if`, operador de atribuição `=` em vez de comparação `==` e bloco sem chaves) e escreva o programa corrigido completo.

---

### `B03-E04` *(Completar Solução — Verificação de Paridade)*
Complete o programa abaixo para que leia um inteiro `n` e, caso seja par, imprima `O numero %d eh par\n`. O programa deve sempre imprimir `Fim do programa\n` ao final.

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    if ( /* Lacuna: teste de paridade */ ) {
        printf("O numero %d eh par\n", n);
    }

    printf("Fim do programa\n");
    return 0;
}
```

---

### `B03-E05` *(Resolução Independente — Radar de Velocidade)*
Escreva um programa completo em C que leia a velocidade de um automóvel em km/h (`double vel`). Se a velocidade for estritamente superior a `80.0` km/h, o programa deve calcular e exibir o valor da multa, sabendo que cada km/h acima do limite custa R$ 5,00:
$$\text{multa} = (\text{vel} - 80.0) \times 5.0$$
Formato de saída da multa: `Multa: R$ %.2f\n`.  
Em qualquer situação (multado ou não), o programa deve imprimir ao final a mensagem: `Boa viagem\n`.

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `B03-C01` *(Teste de Mesa — Limiar Estrito `>` vs. Inclusivo `>=`)*
Considere `double nota = 7.0;` e o trecho de código abaixo:
```c
if (nota > 7.0) {
    printf("Aprovado direto\n");
}
if (nota >= 7.0) {
    printf("Atingiu a media\n");
}
```
Indique exatamente qual texto será impresso na tela e explique a diferença entre `>` e `>=` para o valor de fronteira `7.0`.

---

### `B03-C02` *(Caça ao Bug — `;` após `if` e `=` vs `==`)*
Corrija todos os erros do programa completo abaixo:

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    if (n > 0); {
        printf("Positivo\n");
    }

    if (n = 100) {
        printf("Cem\n");
    }

    printf("Fim\n");
    return 0;
}
```

---

### `B03-C03` *(Programa Completo Independente — Desconto Simples sem else)*
Escreva um programa completo em C que leia o valor de uma compra (`double valor`, com `valor >= 0`). Se o valor for maior ou igual a `100.00`, aplique um desconto de 10% diretamente sobre a variável (`valor = valor * 0.90;`).  
Não utilize `else`.  
Ao final, imprima sempre o valor a pagar no formato exato: `Valor final: R$ %.2f\n`.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `B04` (`Desvio Condicional Composto if / else vs. ifs Independentes`):** somente após autocorreção dos exercícios `B03-E01..E05` **e** **100% (3/3)** na Checagem Independente `B03-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** revisar os 6 operadores relacionais, a distinção `=` vs `==` e a armadilha do `;` após `if`. Aplicar a variante `V2` do bloco.
- **Após 2 tentativas malsucedidas:** retornar para **`B01`** (operador `%` e paridade) e **`A06`** (comandos sequenciais em C).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 2 e item 6 — Estrutura de seleção: simples `if`).
- `[DOC]` `Aula_06_Algoritmos.pdf` p. 4–28 (Expressões relacionais, tabela-verdade em C, estrutura `if`, sintaxe e armadilhas).
- `[DOC]` `Lista1_Algoritmos.pdf` p. 2 (Ex. 3, 4, 5 — condições e limiares simples).
- Casos de teste e soluções verificáveis: [B03_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/gabaritos/B03_gabarito.md) e [B03_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/B03_testes.md).
