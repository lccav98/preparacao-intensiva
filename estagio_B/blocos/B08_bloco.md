# Bloco `B08` — Múltipla Escolha com `switch / case`, `break`, `default` e *Fall-Through*

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio B — Expressões, Operadores e Estruturas Condicionais / **`B08`** |
| **Micro-habilidade foco** | Implementar desvios de múltipla escolha discretos sobre variáveis inteiras ou caracteres usando `switch / case`, `break`, `default` e agrupamento intencional por *fall-through*. |
| **Pré-requisitos** | `B04` *(Desvio condicional composto `if / else`)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão Única (`E01`–`E05`, 22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Não utilize** tipos reais (`float` ou `double`) nem variáveis dentro do `switch` ou dos rótulos `case`. É **estritamente proibido** o uso de laços, vetores e funções além de `main`. Saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Sintaxe e Tipos Válidos:**
   - O comando `switch (expressao)` avalia uma expressão que **deve ser obrigatoriamente de tipo integral** (`int`, `char`, `short`, `long`).
   - É **proibido** usar `float`, `double`, `string` ou ponteiros no `switch`.
2. **Restrições Estritas dos Rótulos `case`:**
   - Cada `case <valor>:` deve conter uma **constante literal ou inteira conhecida em tempo de compilação** (ex.: `case 1:`, `case 'A':`, `case '+' :`).
   - É **proibido usar variáveis** (ex.: `case x:` é erro de compilação) e **intervalos** (ex.: `case 1..5:` não existe em C padrão).
   - Rótulos duplicados (ex.: dois `case 1:` no mesmo `switch`) geram erro de compilação.
3. **O Comando `break`:**
   - O `break` encerra imediatamente a execução do `switch`, saltando para fora de suas chaves `{ }`.
   - Na ausência do `break`, o fluxo continua executando **todos os comandos dos `case`s subsequentes** (fenômeno conhecido como *fall-through*).
4. **Agrupamento Intencional de `case`s (*Fall-Through* Útil):**
   - Quando vários valores discretos devem disparar o mesmo bloco de comandos, empilham-se os rótulos `case` consecutivamente sem `break` entre eles.
5. **A Cláusula `default`:**
   - Executada quando nenhum dos rótulos `case` for igual ao valor da expressão avaliada. Funciona como o `else` final de uma cadeia `else if`.

---

## 2. Exemplos Guiados

### Exemplo 1 — O Efeito *Fall-Through* Acidental *(Trecho ilustrativo)*
Observe o que acontece quando o programador esquece o `break`:

```c
int num = 1;

switch (num) {
    case 1:
        printf("Um ");
        /* FALTAL O break AQUI! */
    case 2:
        printf("Dois ");
        break;
    default:
        printf("Outro ");
}
```
Como não há `break` no `case 1`, a execução "cai" para o `case 2` e imprime `Um Dois `.

### Exemplo 2 — Agrupamento Intencional para Classificar Dias do Mês *(Programa completo)*
Mapeamento de quantos dias tem determinado mês em ano não-bissexto usando agrupamento de rótulos `case`:

```c
#include <stdio.h>

int main(void) {
    int mes;
    scanf("%d", &mes);

    switch (mes) {
        /* Meses com 31 dias agrupados intencionalmente */
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12:
            printf("31 dias\n");
            break;

        /* Meses com 30 dias agrupados */
        case 4:
        case 6:
        case 9:
        case 11:
            printf("30 dias\n");
            break;

        /* Fevereiro em ano comum */
        case 2:
            printf("28 dias\n");
            break;

        default:
            printf("Mes Invalido\n");
            break;
    }

    return 0;
}
```

---

## 3. Exercícios (`B08-E01` a `B08-E05`)

### `B08-E01` *(Teste de Mesa — Rastreamento de Fall-Through sem break)*
Sem usar computador, analise o trecho abaixo:

```c
int cod = 2;

switch (cod) {
    case 1:
        printf("A");
    case 2:
        printf("B");
    case 3:
        printf("C");
        break;
    case 4:
        printf("D");
    default:
        printf("E");
}
printf("\n");
```
1. Qual será a saída impressa se `cod = 2`?
2. Qual será a saída se `cod = 4`?
3. Qual será a saída se `cod = 9`?

---

### `B08-E02` *(Caça ao Bug — Proibição de float e variáveis no case)*
Um estudante tentou escrever uma tabela de tarifas utilizando `switch`:

```c
#include <stdio.h>

int main(void) {
    double peso = 2.5;
    double limite = 5.0;

    /* ERRO: switch e case com double e variavel */
    switch (peso) {
        case 1.0:
            printf("Tarifa A\n");
            break;
        case limite:
            printf("Tarifa B\n");
            break;
        default:
            printf("Tarifa Padrao\n");
            break;
    }

    return 0;
}
```
1. Identifique os **3 motivos** pelos quais o código acima não compila em C padrão C99.
2. Escreva uma versão corrigida em C ([B08_E02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B08_E02_corrigido.c)) que leia um código inteiro de pacote (`int tipo`) onde `1` é `Tarifa A\n`, `2` é `Tarifa B\n` e qualquer outro valor é `Tarifa Padrao\n`.

---

### `B08-E03` *(Completar Solução — Classificador de Vogal ou Consoante)*
Complete o trecho de código abaixo para ler um único caractere `char c;` e informar se ele é uma vogal minúscula (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`) ou outra letra:

```c
char c;
scanf(" %c", &c);

switch (c) {
    /* Complete com os cases agrupados das 5 vogais minusculas */
    /* A */
        printf("Vogal\n");
        break;
    default:
        printf("Outro Caractere\n");
        break;
}
```

---

### `B08-E04` *(Variação controlada — Calculadora Básica com char de Operador)*
Escreva um **programa completo** em C que leia dois operandos reais (`double a, b`) e um operador aritmético (`char op`), lidos na ordem: `scanf("%lf %lf %c", &a, &b, &op);`.
Usando um `switch (op)`:
- `case '+':` calcule e imprima `Resultado: %.2f\n` da soma ($a + b$).
- `case '-':` calcule e imprima `Resultado: %.2f\n` da subtração ($a - b$).
- `case '*':` calcule e imprima `Resultado: %.2f\n` da multiplicação ($a \cdot b$).
- `case '/':` se `b == 0.0`, imprima `Erro: Divisao por Zero\n`; caso contrário, imprima `Resultado: %.2f\n` da divisão ($a / b$).
- `default:` imprima `Operador Invalido\n`.

Arquivo correspondente: [B08_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B08_E04.c).

---

### `B08-E05` *(Resolução independente — Conversor de Dias da Semana)*
Escreva um **programa completo** em C que leia um número inteiro de 1 a 7 (`int dia`).
Utilizando a estrutura `switch (dia)` com `break` obrigatório em todos os ramos:
- `1` $\rightarrow$ imprima `Domingo\n`
- `2` $\rightarrow$ imprima `Segunda\n`
- `3` $\rightarrow$ imprima `Terca\n`
- `4` $\rightarrow$ imprima `Quarta\n`
- `5` $\rightarrow$ imprima `Quinta\n`
- `6` $\rightarrow$ imprima `Sexta\n`
- `7` $\rightarrow$ imprima `Sabado\n`
- Qualquer outro valor $\rightarrow$ imprima `Dia Invalido\n`

Arquivo correspondente: [B08_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B08_E05.c).

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `B08-C01` *(Teste de Mesa — Fall-Through com default fora do final)*
Em C, a cláusula `default` pode aparecer em qualquer posição dentro do `switch`. Considere o seguinte código:

```c
int n = 3;

switch (n) {
    case 1:
        printf("Um ");
        break;
    default:
        printf("Zero ");
    case 2:
        printf("Dois ");
        break;
    case 3:
        printf("Tres ");
        /* Sem break */
    case 4:
        printf("Quatro ");
        break;
}
printf("\n");
```
1. Qual será a saída para `n = 3`?
2. Qual será a saída para `n = 5` (valor que cai no `default` intermediário)?
3. Qual será a saída para `n = 1`?

---

### `B08-C02` *(Caça ao Bug — Break ausente e rótulos duplicados)*
O programa abaixo deveria receber um código de operação bancária (`int op`) e imprimir uma única mensagem correspondente.

```c
#include <stdio.h>

int main(void) {
    int op;
    scanf("%d", &op);

    switch (op) {
        case 1:
            printf("Saldo\n");
        case 2:
            printf("Extrato\n");
            break;
        case 1:
            printf("Saque\n");
            break;
        default:
            printf("Opcao Invalida\n");
    }

    return 0;
}
```
1. Identifique os **2 erros graves** (um que impede a compilação e outro de lógica que causaria *fall-through* indevido).
2. Escreva o programa corrigido completo em C ([B08_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B08_C02_corrigido.c)), onde `1` é `Saldo\n`, `2` é `Extrato\n`, `3` é `Saque\n` e qualquer outro valor é `Opcao Invalida\n`.

---

### `B08-C03` *(Programa completo — Categorização de Produtos por Código)*
Escreva um programa completo em C que leia um código inteiro (`int cod`) referente a uma mercadoria de supermercado.
Utilize `switch` com **agrupamento de rótulos `case`**:
- Códigos `1`, `2` ou `3`: imprima `Alimento Nao-Perecivel\n`
- Códigos `4`, `5` ou `6`: imprima `Alimento Perecivel\n`
- Código `7`: imprima `Vestuario\n`
- Códigos `8`, `9` ou `10`: imprima `Limpeza\n`
- Para qualquer outro código: imprima `Codigo Invalido\n`

Arquivo correspondente: [B08_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B08_C03.c).

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `B09` (`Combinação de switch com if e switch Aninhado`):** somente após autocorreção dos exercícios `B08-E01..E05` **e** **100% (3/3)** na Checagem Independente `B08-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** revisar a necessidade do comando `break` ao final de cada ramo que não deve sofrer *fall-through*, conferindo se os tipos dos `case`s são estritamente inteiros ou caracteres.
- **Após 2 tentativas malsucedidas:** retornar a **`B04`** e **`B05`** (estruturas de seleção mútua com `if/else if`).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 6 — Estrutura de seleção de múltipla escolha `switch`).
- `[DOC]` `Aula_08_Algoritmos_v2.pdf` p. 3–10 (sintaxe do `switch`, `case`, `break`, `default` e *fall-through*).
- `[DOC]` `Lista3_Algoritmos.pdf` p. 1–2 (Ex. 1 e 2 — menu de opções e calculadora com `switch`).
- Casos de teste e soluções verificáveis: [B08_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/gabaritos/B08_gabarito.md) e [B08_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/B08_testes.md).
