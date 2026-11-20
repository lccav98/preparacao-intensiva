# Bloco `C07` — Controle de Fluxo em Laços (`break`, `continue`, `for (;;)` / `while (1)`) e Primalidade

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio C — Estruturas de Repetição e Rastreamento de Laços / **`C07`** |
| **Micro-habilidade foco** | Controlar saída antecipada (`break`) e salto de iteração (`continue`) em laços (incluindo `for (;;)` / `while (1)`) e implementar algoritmo de verificação de primalidade com tratamento de borda (`n <= 1`). |
| **Pré-requisitos** | `C03` *(Laços com Sentinela)*, `C05` *(Laço Contado `for`)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão 1 (`E01`–`E05`, 22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Não utilize** vetores ou strings (`char[]`, `int[]` ou qualquer array `v[i]`), funções customizadas além de `int main(void)`, `struct` ou alocação dinâmica. Saídas de programas C devem ser estritamente em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **O Comando `break` em Laços:**
   - Interrompe **imediatamente** o laço mais interno (`while`, `for` ou `do-while`) no qual está contido.
   - O fluxo de execução salta diretamente para a primeira linha após o fechamento `}` do laço.
   - Se houver laços aninhados, o `break` sai **apenas** do laço atual em que se encontra, não afetando os laços mais externos.

2. **O Comando `continue`:**
   - Interrompe **apenas a iteração corrente**, saltando as instruções restantes do corpo e passando para a próxima iteração.
   - **Comportamento no `for`:** Salta diretamente para a expressão de atualização (`expr3`), e em seguida avalia a condição (`expr2`).
   - **Comportamento no `while` e `do-while`:** Salta diretamente para o teste da condição.

3. **A Armadilha do `continue` no `while`:**
   ```c
   int i = 0;
   while (i < 5) {
       if (i == 2) {
           continue; // <-- PULA O INCREMENTO! LACO INFINITO!
       }
       printf("%d ", i);
       i++; // <-- NUNCA SERA EXECUTADO QUANDO i == 2
   }
   ```
   No `while`, como o incremento geralmente fica no final do corpo, um `continue` mal posicionado pula a linha `i++`. A variável `i` permanece congelada em `2` e o laço entra em **loop infinito**. Para evitar isso no `while`, o incremento deve ocorrer antes do `continue` ou deve-se preferir a estrutura `for`.

4. **Laços com Saída no Meio (`while (1)` ou `for (;;)`):**
   - São laços com condição propositalmente sempre verdadeira.
   - A saída ocorre obrigatoriamente através de um comando `break` condicionado a uma leitura de sentinela ou critério de convergência.
   - Evita a duplicação de chamadas de leitura antes e dentro do laço (*priming read*).

5. **`break` em Laço que Contém `switch`:**
   - O comando `break` dentro de um bloco `switch` pertence ao `switch`, e **não** ao laço! Ele apenas impede o *fall-through* dos casos do `switch`, sem interromper o laço externo. Para encerrar o laço a partir de um `case`, é necessário usar uma variável de sinalização (*flag*).

6. **Algoritmo de Primalidade e Casos Borda:**
   - **Definição:** Um número inteiro positivo $n$ é primo se possuir exatamente dois divisores positivos distintos: $1$ e o próprio $n$.
   - **Bordas Obrigatórias:**
     - Números menores ou iguais a 1 ($n \le 1$): **NÃO são primos**.
     - Número $2$: é o **único primo par**.
     - Números pares maiores que 2 ($n > 2$ e $n \% 2 == 0$): **NÃO são primos**.
   - **Eficiência de parada antecipada:** Para verificar se $n \ge 3$ é primo, basta testar divisores ímpares $d = 3, 5, 7, \dots$ até $d \times d \le n$. Se encontrar um divisor exato ($n \% d == 0$), executa-se um `break` imediatamente, pois o número é composto.

---

## 2. Exemplos Guiados

### Exemplo 1 — Diferença entre `break` e `continue` em `for`

```c
#include <stdio.h>

int main(void) {
    printf("Com continue: ");
    for (int i = 1; i <= 6; i++) {
        if (i == 4) {
            continue; // Pula apenas o numero 4
        }
        printf("%d ", i);
    }
    printf("\n");

    printf("Com break:    ");
    for (int i = 1; i <= 6; i++) {
        if (i == 4) {
            break; // Aborta todo o laco ao atingir 4
        }
        printf("%d ", i);
    }
    printf("\n");

    return 0;
}
```

**Saída Produzida:**
```text
Com continue: 1 2 3 5 6 
Com break:    1 2 3 
```

---

### Exemplo 2 — Verificador de Primalidade com Saída Antecipada

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    int primo = 1; // 1 = verdadeiro, 0 = falso

    if (n <= 1) {
        primo = 0; // 0 e 1 nao sao primos
    } else if (n == 2) {
        primo = 1; // 2 e primo
    } else if (n % 2 == 0) {
        primo = 0; // pares > 2 nao sao primos
    } else {
        /* Testa apenas divisores impares */
        for (int d = 3; d * d <= n; d += 2) {
            if (n % d == 0) {
                primo = 0;
                break; // divisor encontrado, encerra a busca
            }
        }
    }

    if (primo) {
        printf("Primo\n");
    } else {
        printf("Nao Primo\n");
    }

    return 0;
}
```

---

## 3. Exercícios (`C07-E01` a `C07-E05`)

### Sessão 1 (`C07-E01` a `C07-E05` — Controle de Fluxo, Depuração e Primalidade)

### `C07-E01` *(Rastreamento de `break` e `continue` em `for`)*
Sem usar computador, analise o trecho de código abaixo e elabore o teste de mesa completo:

```c
int soma = 0;
for (int i = 1; i <= 10; i++) {
    if (i % 3 == 0) {
        continue;
    }
    if (i > 7) {
        break;
    }
    printf("%d ", i);
    soma += i;
}
printf("\nSoma = %d\n", soma);
```

1. Para cada iteração de `i` de 1 a 10, informe se a instrução `continue` foi acionada, se o `break` foi acionado, o que foi impresso e o valor acumulado em `soma`.
2. Qual é a saída exata impressa pelo programa?

---

### `C07-E02` *(Caça ao Bug — Armadilha do `continue` em `while`)*
O programa abaixo deveria ler valores inteiros positivos e imprimir a contagem regressiva de `n` até `1`, pulando o número 3:

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    int i = n;
    while (i >= 1) {
        if (i == 3) {
            continue;
        }
        printf("%d ", i);
        i--;
    }
    printf("\n");
    return 0;
}
```

1. Ao executar com entrada `5`, o programa imprime `5 4 ` e congela em tela preta (laço infinito). Explique detalhadamente por que isso ocorreu.
2. Escreva o programa corrigido completo em C99 ([C07_E02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C07_E02_corrigido.c)).

---

### `C07-E03` *(Completar Laço `while (1)` com `break` Condicional)*
Complete o programa abaixo ([C07_E03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C07_E03.c)) que lê notas inteiras de provas (de 0 a 100).
- A entrada é interrompida imediatamente quando o usuário digita um valor negativo (sentinela `< 0`).
- O programa calcula a quantidade de notas válidas lidas e a média aritmética das notas válidas com duas casas decimais (`%.2f`).
- Se nenhuma nota válida for digitada antes do sentinela, imprima: `Nenhuma nota valida\n`.
- *Restrição:* Proibido usar vetores. Utilize a estrutura `while (1)` com `break`.

*Exemplo de entrada:* `80 90 70 -1`  
*Saída esperada:*
```text
Qtd: 3
Media: 80.00
```

---

### `C07-E04` *(Detector de Número Primo com Tratamento Rigoroso de Bordas)*
Escreva um programa completo em C99 ([C07_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C07_E04.c)) que leia um número inteiro `n` qualquer e informe se ele é primo ou não.
- Se `n` for primo, imprima: `Primo\n`.
- Se não for primo, imprima: `Nao Primo\n`.
- *Casos de teste obrigatórios que devem funcionar corretamente:*
  - `n = -5` $\rightarrow$ `Nao Primo`
  - `n = 0` $\rightarrow$ `Nao Primo`
  - `n = 1` $\rightarrow$ `Nao Primo`
  - `n = 2` $\rightarrow$ `Primo`
  - `n = 4` $\rightarrow$ `Nao Primo`
  - `n = 13` $\rightarrow$ `Primo`

---

### `C07-E05` *(Programa Completo — Contagem de Primos em Sequência com Sentinela)*
Escreva um programa completo em C99 ([C07_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C07_E05.c)) que leia números inteiros positivos fornecidos pelo usuário, um a um, até que o número `0` (sentinela de parada) seja digitado.
Para cada número lido (exceto o 0):
- Verifique se ele é primo.
- Mantenha a contagem de quantos números primos foram identificados.
- Ao final, imprima:
  ```text
  Total Primos: %d
  ```
- Se nenhum número primo tiver sido digitado na sequência, a saída deve ser:
  ```text
  Total Primos: 0
  ```

*Exemplo de entrada:* `7 10 13 1 4 17 0`  
*Saída esperada:*
```text
Total Primos: 3
```
*(Os primos da sequência foram 7, 13 e 17; 1, 4 e 10 não são primos).*

---

## 4. Checagem Independente de Domínio (`C07-C01` a `C07-C03`)

> **Instruções:** Resolva estas 3 questões sem consulta a materiais ou gabaritos. Tempo limite: 18 minutos.

### `C07-C01` *(Teste de Mesa — `continue` vs `break` em Laços)*
Analise os dois trechos de código abaixo e determine sem computador o que cada um imprime:

**Trecho A:**
```c
int a = 0;
for (int i = 1; i <= 5; i++) {
    if (i == 3) continue;
    a += i;
}
printf("A = %d\n", a);
```

**Trecho B:**
```c
int b = 0;
for (int i = 1; i <= 5; i++) {
    if (i == 3) break;
    b += i;
}
printf("B = %d\n", b);
```

Apresente os valores finais de `A` e `B` com a justificativa de quais termos foram somados em cada um.

---

### `C07-C02` *(Caça ao Bug — `break` em Laço Contendo `switch`)*
Um estudante tentou escrever um menu simples que fica repetindo até que a opção 0 seja escolhida para sair:

```c
#include <stdio.h>

int main(void) {
    int opcao;
    while (1) {
        scanf("%d", &opcao);
        switch (opcao) {
            case 1:
                printf("Opcao 1 Executada\n");
                break;
            case 0:
                printf("Saindo\n");
                break; // O aluno pretendia encerrar o while aqui!
            default:
                printf("Opcao Invalida\n");
                break;
        }
    }
    printf("Fim do Programa\n");
    return 0;
}
```

1. Explique por que a digitação de `0` imprime `Saindo` mas o laço `while (1)` **continua rodando indefinidamente**, sem nunca alcançar `printf("Fim do Programa\n");`.
2. Escreva a versão corrigida completa em C99 ([C07_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C07_C02_corrigido.c)), utilizando uma variável de controle (*flag*) ou condição estruturada no laço.

---

### `C07-C03` *(Programa Completo — Classificador e Estatísticas de Primalidade)*
Escreva um programa completo em C99 ([C07_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C07_C03.c)) que leia um número inteiro positivo `k` (`k >= 1`) representando a quantidade de números a serem analisados.
Em seguida, leia `k` números inteiros.
Para cada número:
- Se for primo, imprima: `Numero %d: Primo\n`.
- Se não for primo, imprima: `Numero %d: Nao Primo\n`.

Ao final, imprima a linha de resumo:
```text
Resumo: %d primos de %d numeros
```

*Exemplo de entrada:*
```text
4
1
2
4
13
```
*Saída esperada:*
```text
Numero 1: Nao Primo
Numero 2: Primo
Numero 4: Nao Primo
Numero 13: Primo
Resumo: 2 primos de 4 numeros
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `C08` (`Séries Numéricas, Atualização Incremental e Convergência por Tolerância`):** somente após autocorreção dos exercícios `C07-E01..E05` **e** **100% de acerto (3/3)** na Checagem Independente `C07-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** revisar a diferença entre o escopo do `break` em `switch` vs laço e reescrever manualmente a lógica de primalidade isolando os casos $n \le 1$.
- **Após 2 tentativas malsucedidas:** retornar a **`C03`** (laços com sentinela) e **`B08`** (estrutura de seleção múltipla `switch`).

---

## 6. Referências do Orientador
- `[DOC]` `Aula_10_Algoritmos.pdf` p. 17, 19–25 (`break`, `continue`, laços com saída intermediária).
- `[DOC]` `Lista8_Algoritmos_Revisao.pdf` p. 2 (Ex. 5: algoritmo de primalidade e tratamento de $n = 1$).
- `[DOC]` `00_inventario_fontes.md` Seção 2.1 e 2.2 (especificação dos padrões de repetição e controle de fluxo).
- Casos de teste e soluções verificáveis: [C07_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/gabaritos/C07_gabarito.md) e [C07_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/C07_testes.md).
