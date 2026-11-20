# Bloco `B04` — Desvio Condicional Composto (`if / else`) vs. `if`s Independentes

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio B — Expressões, Operadores e Estruturas Condicionais / **`B04`** |
| **Micro-habilidade foco** | Escolher e implementar corretamente `if / else` para alternativas mutuamente exclusivas vs. múltiplos `if`s independentes quando mais de uma condição pode ocorrer simultaneamente. |
| **Pré-requisitos** | `B03` *(Expressões relacionais, verdadeiro/falso em C e if simples)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão única de prática + checagem (22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Não utilize** `else if` (introduzido em `B05`), `switch` (introduzido em `B08`), operadores lógicos (`&&`, `||`, `!`), laços ou vetores. Utilize apenas a bifurcação binária `if / else` ou múltiplos `if`s independentes com variáveis de controle (*flags*). Saídas estritamente em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Exclusão Mútua com `if / else`:**  
   Quando um problema possui **duas alternativas mutuamente exclusivas** (ou acontece A, ou acontece B; nunca ambos, nunca nenhum), use a estrutura composta:
   ```c
   if (condicao) {
       /* Bloco A: executa se condicao != 0 */
   } else {
       /* Bloco B: executa se condicao == 0 */
   }
   ```
   **Garantia formal:** Exatamente um dos blocos será executado. Se o `if` executar, o `else` é sumariamente descartado sem reavaliação.
2. **Quando NÃO Usar Dois `if`s Seguidos:**  
   Evite escrever `if (x >= 0) ...` seguido de `if (x < 0) ...`. Além de desperdiçar processamento avaliando duas condições que são complementares, se o código dentro do primeiro `if` modificar a variável `x`, o segundo `if` pode ser disparado acidentalmente!
3. **Quando USAR Múltiplos `if`s Independentes:**  
   Use `if`s sequenciais e independentes quando **mais de uma condição pode ser verdadeira ao mesmo tempo** e desejamos que cada condição verdadeira execute sua respectiva ação (por exemplo: testar se um número possui múltiplos divisores simultâneos: 2, 3 e 5).
4. **Padrão de Bandeira (*Flag*) para o Caso "Nenhum":**  
   Ao usar múltiplos `if`s independentes e precisar de uma ação caso nenhuma condição seja satisfeita:
   - Crie uma variável inteira inicializada em zero: `int achou = 0;`.
   - Dentro de cada `if` que for executado, atualize a variável: `achou = 1;`.
   - Ao final da sequência de testes, verifique: `if (achou == 0) { printf("Nenhum\n"); }`.
5. **Atenção à Fronteira Exata:** Em classificações numéricas binárias (ex.: notas de corte ou temperaturas), verifique com rigor se o valor limite pertence ao `if` (usando `>=` ou `<=`) ou ao `else`.

---

## 2. Exemplos Guiados

### Exemplo 1 — Par ou Ímpar com `if / else` *(Programa completo)*
```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    if (n % 2 == 0) {
        printf("%d eh par\n", n);
    } else {
        printf("%d eh impar\n", n);
    }

    return 0;
}
```
Como todo inteiro é par ou ímpar, o `else` cobre com exatidão matemática todos os casos que não satisfazem `n % 2 == 0`.

### Exemplo 2 — Múltiplos `if`s independentes com flag *(Programa completo)*
Deseja-se avisar se uma pessoa tem direito a gratuidade por idade (`idade >= 65`) ou por ser estudante (`estudante == 1`), podendo ter direito por ambos, ou emitir "Tarifa cheia" caso não tenha nenhum:

```c
#include <stdio.h>

int main(void) {
    int idade, estudante, gratuidade = 0;
    scanf("%d %d", &idade, &estudante);

    if (idade >= 65) {
        printf("Beneficio Idoso\n");
        gratuidade = 1;
    }
    if (estudante == 1) {
        printf("Beneficio Estudante\n");
        gratuidade = 1;
    }
    if (gratuidade == 0) {
        printf("Tarifa cheia\n");
    }

    return 0;
}
```
Uma pessoa com 70 anos e estudante recebe ambos os benefícios. Alguém sem nenhum recebe `Tarifa cheia`.

---

## 3. Exercícios (`B04-E01` a `B04-E05`)

### `B04-E01` *(Teste de Mesa / Comparação Semântica — Reprodução do Modelo)*
Sem usar o computador, analise o que acontece para a entrada `x = 3` nos dois trechos abaixo e explique por que os resultados diferem:

**Trecho 1:**
```c
if (x > 0) {
    x = x - 5;
}
if (x <= 0) {
    printf("A\n");
}
```

**Trecho 2:**
```c
if (x > 0) {
    x = x - 5;
} else {
    printf("A\n");
}
```

---

### `B04-E02` *(Completar Solução — Par ou Ímpar com `if / else`)*
Complete o programa em C para que leia um número inteiro `n` e imprima `%d eh par\n` ou `%d eh impar\n`:

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    if (n % 2 == 0) {
        printf("%d eh par\n", n);
    } /* Lacuna: ramo alternativo */ {
        printf("%d eh impar\n", n);
    }

    return 0;
}
```

---

### `B04-E03` *(Caça ao Bug — Saída Duplicada em Fronteira)*
O programa a seguir deveria ler uma nota (`double nota`, de `0.0` a `10.0`) e classificar o estudante como `Aprovado\n` se a nota for maior ou igual a `6.0`, ou `Reprovado\n` se for menor que `6.0`:

```c
#include <stdio.h>

int main(void) {
    double nota;
    scanf("%lf", &nota);

    if (nota >= 6.0) {
        printf("Aprovado\n");
    }
    if (nota <= 6.0) {
        printf("Reprovado\n");
    }

    return 0;
}
```
1. Qual erro grave acontece quando a entrada é exatamente `6.0`?
2. Escreva o programa corrigido utilizando a estrutura `if / else`.

---

### `B04-E04` *(Completar Solução — Múltiplos Divisores e Flag 'Nenhum')*
Complete o programa que lê um número inteiro `n` e verifica de forma não-excludente se ele é divisível por 2, por 3 e por 5. Caso não seja divisível por nenhum desses três, imprima `Nenhum divisor encontrado\n`:

```c
#include <stdio.h>

int main(void) {
    int n, achou = 0;
    scanf("%d", &n);

    if (n % 2 == 0) {
        printf("Divisivel por 2\n");
        achou = 1;
    }
    if ( /* A: divisivel por 3 */ ) {
        printf("Divisivel por 3\n");
        achou = 1;
    }
    if ( /* B: divisivel por 5 */ ) {
        printf("Divisivel por 5\n");
        achou = 1;
    }
    if ( /* C: nenhum divisor encontrado */ ) {
        printf("Nenhum divisor encontrado\n");
    }

    return 0;
}
```

---

### `B04-E05` *(Resolução Independente — Crédito Especial)*
Um banco concederá um crédito especial aos seus clientes conforme o saldo médio do último ano (`double saldo_medio`, com `saldo_medio >= 0`):
- Clientes com saldo médio estritamente superior a R$ 1.000,00 recebem um crédito de 30% do saldo médio;
- Clientes com saldo médio menor ou igual a R$ 1.000,00 recebem um crédito de 15% do saldo médio.

Escreva um programa completo em C que leia o saldo médio e imprima:
```text
Saldo medio: R$ %.2f\n
Credito especial: R$ %.2f\n
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `B04-C01` *(Análise Conceitual — `if`+`if` vs. `if/else`)*
Explique detalhadamente:
1. Por que a construção `if (condicao) ... else ...` é computacionalmente e logicamente superior a dois `if`s com condições complementares (ex.: `if (x >= 0)` e `if (x < 0)`);
2. Em que circunstância da vida real ou de um algoritmo é **obrigatório** usar `if`s independentes em vez de `if/else`.

---

### `B04-C02` *(Programa Completo — Termômetro Febril)*
Escreva um programa completo em C que leia a temperatura corporal em graus Celsius de um paciente (`double temp`).  
Se a temperatura for igual ou superior a `37.8` °C, imprima: `Estado febril: %.1f C\n`.  
Caso contrário, imprima: `Temperatura normal: %.1f C\n`.  
Utilize a estrutura composta `if / else`.

---

### `B04-C03` *(Programa Completo — Permissões Múltiplas e Flag de Controle)*
Um sistema operacional atribui permissões a um usuário segundo seu código numérico inteiro (`int codigo`):
- Se o código for múltiplo de 2, imprime `Permissao de Leitura\n`;
- Se o código for múltiplo de 3, imprime `Permissao de Escrita\n`;
- Se o código for múltiplo de 5, imprime `Permissao de Execucao\n`.

O usuário pode receber uma, duas ou todas as três permissões simultaneamente. Caso não receba nenhuma das três permissões, o programa deve imprimir obrigatoriamente: `Sem permissoes especiais\n`.  
Escreva o programa completo em C utilizando múltiplos `if`s e uma variável inteira de controle (*flag*).

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `B05` (`Múltiplas Alternativas com else if e Ordem das Condições`):** somente após autocorreção dos exercícios `B04-E01..E05` **e** **100% (3/3)** na Checagem Independente `B04-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** revisar o conceito de exclusão mútua (`if/else`) vs. eventos simultâneos (múltiplos `if`s) e o uso da flag inteira para o caso alternativo abrangente.
- **Após 2 tentativas malsucedidas:** retornar para **`B03`** (operadores relacionais e sintaxe do `if`).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 6 — Estrutura de seleção: composta `if/else`).
- `[DOC]` `Aula_07_Algoritmos.pdf` p. 3–9 (Desvio condicional composto `if/else`, fluxo de controle e bifurcação binária).
- `[DOC]` `Lista2_Algoritmos.pdf` p. 1–2 (Ex. 2, 3, 5 — decisões compostas e regras de negócio com `if/else`).
- Casos de teste e soluções verificáveis: [B04_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/gabaritos/B04_gabarito.md) e [B04_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/B04_testes.md).
