# Bloco `C08` — Séries Numéricas, Atualização Incremental e Convergência por Tolerância ($\varepsilon$)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio C — Estruturas de Repetição e Rastreamento de Laços / **`C08`** |
| **Micro-habilidade foco** | Calcular somatórios e séries matemáticas atualizando numerador, denominador, sinal ou fatorial incrementalmente a cada iteração ($O(n)$) e interrompendo por critério de tolerância ($\varepsilon$) sem somar o termo que viola $< \varepsilon$. |
| **Pré-requisitos** | `C03` *(Laços com Sentinela)*, `C05` *(Laço Contado `for`)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Sessão 2 (`E04`–`E06`, 20 min):** `12 min` resol. \| `5 min` corr. \| `3 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Não utilize** vetores ou strings (`char[]`, `int[]` ou qualquer array `v[i]`), funções customizadas além de `int main(void)`, `struct` ou alocação dinâmica. Cálculos de ponto flutuante devem usar estritamente `double`. Saídas de programas C devem ser em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Atualização Incremental ($O(n)$ vs $O(n^2)$):**
   - Ao calcular somatórios do tipo $\sum \frac{x^k}{k!}$, nunca recalcule potências ou fatoriais a partir do zero em cada iteração com laços aninhados ou bibliotecas pesadas.
   - Observe a relação matemática de recorrência entre termos consecutivos:
     $$\text{termo}_k = \text{termo}_{k-1} \times \frac{x}{k}$$
   - Uma única multiplicação e divisão em ponto flutuante a cada iteração mantém o algoritmo estritamente linear em tempo e previne estouros de capacidade (*overflow*).

2. **Prevenção de *Overflow* com `double`:**
   - Em inteiros de 32 bits com sinal (`int`), o fatorial estoura em $13!$ ($13! = 6.227.020.800 > 2^{31}-1 = 2.147.483.647$).
   - O tipo `double` suporta valores até aproximadamente $10^{308}$ com 53 bits de precisão de mantissa (~15 a 17 dígitos significativos decimais), sendo o tipo mandatório para denominadores e termos de séries numéricas.

3. **A Armadilha da Divisão Inteira (`1 / fat`):**
   - Se `fat` for uma variável inteira ou se você escrever o numerador como `1` em vez de `1.0`, o compilador executa a divisão truncada inteira. Para qualquer `fat >= 2`, o resultado de `1 / fat` é **`0`**, zerando todos os termos seguintes da série!
   - Escreva sempre com literal de ponto flutuante: `1.0 / fat` ou faça conversão explícita `(double)num / den`.

4. **Alternância de Sinal Elegante:**
   - Para séries alternadas do tipo $\sum (-1)^k \cdot a_k$, utilize uma variável escalar de sinal multiplicativo:
     ```c
     double sinal = 1.0;
     // ... a cada passo:
     sinal = -sinal;
     ```
   - Isso evita calcular $(-1)^k$ e custa apenas uma inversão aritmética de sinal por iteração.

5. **Critério de Tolerância ($\varepsilon$) sem Somar o Violador:**
   - Em aproximações numéricas infinitas, o laço deve somar apenas termos cuja magnitude seja maior ou igual à tolerância estipulada ($\text{termo} \ge \varepsilon$).
   - A estrutura canônica correta avalia o termo **antes** de somá-lo ao acumulador:
     ```c
     double soma = 0.0;
     double termo = 1.0; // Primeiro termo (k = 0)
     int k = 0;
     while (termo >= eps) {
         soma += termo;
         k++;
         termo = termo / k; // Proximo termo
     }
     ```
   - Quando `termo` cai abaixo de `eps`, o laço encerra imediatamente **sem somar** esse termo violador.

6. **Prevenção de Divisão por Zero (*Off-by-One* em Denominadores):**
   - Em séries com denominador $(n - k)^2$, atente para os limites exatos da variável de controle. Se o laço for até $k \le n$, na iteração $k = n$ o denominador será $(n - n)^2 = 0$, gerando uma exceção fatal de ponto flutuante (*Crash / Floating Point Exception*). O limite superior correto deve ser $k < n$ ($k$ de $0$ a $n-1$).

---

## 2. Exemplos Guiados

### Exemplo 1 — Série do Número $e$ com $N$ Termos por `for` Incremental

A constante de Euler $e$ é dada por:
$$e = \sum_{k=0}^{n-1} \frac{1}{k!} = \frac{1}{0!} + \frac{1}{1!} + \frac{1}{2!} + \frac{1}{3!} + \dots$$

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    double soma = 0.0;
    double termo = 1.0; // Termo para k = 0 (1 / 0! = 1.0)

    for (int k = 0; k < n; k++) {
        soma += termo;
        termo = termo / (k + 1); // Atualizacao incremental O(1) do proximo termo
    }

    printf("e aprox: %.8f\n", soma);
    return 0;
}
```

---

### Exemplo 2 — Série por Tolerância $\varepsilon$ com `while`

Deseja-se aproximar $e$ somando todos os termos que satisfazem $\frac{1}{k!} \ge \varepsilon$:

```c
#include <stdio.h>

int main(void) {
    double eps;
    scanf("%lf", &eps);

    double soma = 0.0;
    double termo = 1.0;
    int k = 0;

    while (termo >= eps) {
        soma += termo;
        k++;
        termo = termo / k;
    }

    printf("Soma: %.8f\n", soma);
    printf("Termos somados: %d\n", k);
    return 0;
}
```
*Se a entrada for `0.01`, termos $< 0.01$ não entram na soma e o número de termos somados reflete exatamente as parcelas adicionadas.*

---

## 3. Exercícios (`C08-E01` a `C08-E06`)

### Sessão 1 (`C08-E01` a `C08-E03` — Rastreamento de Séries e Caça aos Bugs Numéricos)

### `C08-E01` *(Teste de Mesa dos 4 Primeiros Termos de Série Incremental)*
Considere a série que aproxima o valor de $\frac{\pi}{4}$ através da fórmula de Leibniz:
$$\frac{\pi}{4} = \sum_{k=0}^{\infty} \frac{(-1)^k}{2k + 1} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \dots$$

Sem usar computador, elabore a tabela de teste de mesa para os 4 primeiros termos ($k = 0, 1, 2, 3$), contendo:
1. Índice $k$.
2. Valor de `sinal` ($+1.0$ ou $-1.0$).
3. Denominador $2k + 1$.
4. Valor do termo atual $\text{termo} = \frac{\text{sinal}}{2k + 1}$ em fração e decimal com 4 casas.
5. Valor acumulado em `soma`.

---

### `C08-E02` *(Caça ao Bug 1 — Divisão Inteira Destrutiva em Denominador)*
O programa abaixo deveria calcular a soma dos $n$ primeiros termos da série harmônica inversa de fatoriais $S = \sum_{k=1}^{n} \frac{1}{k!}$:

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    double soma = 0.0;
    int fat = 1;

    for (int k = 1; k <= n; k++) {
        fat *= k;
        soma += 1 / fat; // <-- ONDE ESTA O ERRO?
    }

    printf("Soma = %.6f\n", soma);
    return 0;
}
```

1. Quando o programa é executado para `n = 5`, o resultado impresso é `Soma = 1.000000`, em vez do valor correto aproximado $1.716667$. Explique analiticamente por que todas as parcelas a partir de $k = 2$ foram computadas como zero.
2. Escreva o programa corrigido completo em C99 ([C08_E02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C08_E02_corrigido.c)).

---

### `C08-E03` *(Caça ao Bug 2 — Somar o Termo Violador que Falha em $< \varepsilon$)*
Um programador tentou implementar um laço de tolerância $\varepsilon$ usando `do-while`:

```c
#include <stdio.h>

int main(void) {
    double eps;
    scanf("%lf", &eps);

    double soma = 0.0;
    double termo = 1.0;
    int k = 1;

    do {
        soma += termo;
        termo = 1.0 / (k * k);
        k++;
    } while (termo >= eps);

    printf("Soma = %.6f\n", soma);
    return 0;
}
```

1. Demonstre por que a estrutura `do-while` acima soma indevidamente uma parcela que viola o critério de tolerância ($< \varepsilon$).
2. Escreva o programa corrigido completo em C99 ([C08_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C08_E03_corrigido.c)), garantindo que apenas termos estritamente maiores ou iguais a $\varepsilon$ sejam somados.

---

### Sessão 2 (`C08-E04` a `C08-E06` — Implementação de Séries Contadas e por Tolerância)

### `C08-E04` *(Completar Série Exponencial $e^x$ com Atualização Incremental $O(n)$)*
A série de Taylor para a função exponencial $e^x$ em torno de zero é dada por:
$$e^x = \sum_{k=0}^{n-1} \frac{x^k}{k!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots + \frac{x^{n-1}}{(n-1)!}$$

Escreva um programa completo em C99 ([C08_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C08_E04.c)) que leia um valor real `double x` e um inteiro positivo `int n` ($n \ge 1$), calcule a soma dos $n$ primeiros termos utilizando atualização incremental $\text{termo}_k = \text{termo}_{k-1} \times \frac{x}{k}$ sem recalcular potência ou fatorial do zero, e imprima o resultado no formato:
```text
e^x aprox: %.6f
```

*Exemplo de entrada:* `1.0 10`  
*Saída esperada:* `e^x aprox: 2.718282`

---

### `C08-E05` *(Série Contada da Lista 5 Ex. 5 — Prova AED I UFPR 2017)*
Adaptação da questão 5 da Lista de Exercícios 5 da UTFPR:
Dado um número inteiro positivo $n$ ($n \ge 1$), calcule o valor do somatório $S$:
$$S = \sum_{k=0}^{n-1} \frac{2^k}{(n - k)^2} = \frac{2^0}{n^2} + \frac{2^1}{(n-1)^2} + \frac{2^2}{(n-2)^2} + \dots + \frac{2^{n-1}}{1^2}$$

Escreva um programa completo em C99 ([C08_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C08_E05.c)) que:
1. Leia o inteiro `n`. Se `n <= 0`, imprima: `Entrada Invalida\n` e encerre.
2. Calcule o somatório acumulando em uma variável `double soma`. Atualize a potência de 2 incrementalmente (`pot2 *= 2.0;`).
3. Imprima o resultado final com 6 casas decimais: `S = %.6f\n`.

*Exemplo de entrada:* `3`  
*Cálculo:* $\frac{2^0}{3^2} + \frac{2^1}{2^2} + \frac{2^2}{1^2} = \frac{1}{9} + \frac{2}{4} + \frac{4}{1} = 0.111111 + 0.5 + 4.0 = 4.611111$  
*Saída esperada:* `S = 4.611111`

---

### `C08-E06` *(Série por Tolerância com Contagem Exata de Termos)*
Escreva um programa completo em C99 ([C08_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C08_E06.c)) que aproxime a constante de Euler $e = \sum_{k=0}^{\infty} \frac{1}{k!}$ utilizando critério de tolerância $\varepsilon$:
1. Leia um valor real positivo `double eps` ($0 < \varepsilon \le 1$). Se a entrada for inválida ($\varepsilon \le 0$), imprima `Tolerancia Invalida\n`.
2. Some termos consecutivos $\frac{1}{k!}$ enquanto o termo for maior ou igual a $\varepsilon$ ($\text{termo} \ge \varepsilon$).
3. Ao término, imprima:
   ```text
   Soma = %.8f
   Termos = %d
   ```

*Exemplo de entrada:* `0.001`  
*Saída esperada:*
```text
Soma = 2.71825397
Termos = 7
```
*(Termos somados de $k=0$ até $k=6$, pois $\frac{1}{6!} = \frac{1}{720} \approx 0.001389 \ge 0.001$, enquanto $\frac{1}{7!} \approx 0.000198 < 0.001$).*

---

## 4. Checagem Independente de Domínio (`C08-C01` a `C08-C03`)

> **Instruções:** Resolva estas 3 questões sem consulta a materiais ou gabaritos. Tempo limite: 18 minutos.

### `C08-C01` *(Identificação de Bug Numérico e Divisão por Zero)*
Considere o seguinte trecho proposto para calcular uma variação da série de Taylor:

```c
double soma = 0.0;
for (int k = 0; k <= n; k++) {
    double termo = (1 / (k + 1)) * (n / (n - k));
    soma += termo;
}
```

Identifique **dois erros conceituais graves** no cálculo de `termo`:
1. Um erro de perda de precisão aritmética em tempo de compilação.
2. Um erro que causará pane (*crash*) por divisão por zero na última iteração.

---

### `C08-C02` *(Programa Completo — Série Alternada do Logaritmo Natural $\ln(1+x)$)*
Conforme a questão 4 da `Lista8_Algoritmos_Revisao.pdf` da UTFPR, para $|x| < 1$, o logaritmo natural de $(1+x)$ é dado pela série:
$$\ln(1 + x) = \sum_{k=1}^{n} (-1)^{k+1} \frac{x^k}{k} = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \dots$$

Escreva um programa completo em C99 ([C08_C02.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C08_C02.c)) que leia `double x` (onde $-1 < x \le 1$) e um número inteiro de termos `int n` ($n \ge 1$), calcule o somatório acumulado utilizando alternância de sinal e potência incremental (`pot_x *= x;`), e imprima o resultado no formato:
```text
ln(1+x) aprox: %.6f
```

*Exemplo de entrada:* `0.5 5`  
*Saída esperada:* `ln(1+x) aprox: 0.407292`

---

### `C08-C03` *(Programa Completo — Série com Tolerância e Borda $\varepsilon > 1$)*
Escreva um programa completo em C99 ([C08_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C08_C03.c)) que calcule a aproximação de:
$$S = \sum_{k=1}^{\infty} \frac{1}{k^2}$$
somando todos os termos enquanto $\frac{1}{k^2} \ge \varepsilon$.
- Se o usuário digitar $\varepsilon > 1.0$, o primeiro termo já viola a tolerância ($\frac{1}{1^2} = 1.0 < \varepsilon$). Nesse caso, o programa não deve somar nenhum termo e imprimir:
  ```text
  Soma = 0.000000
  Termos = 0
  ```
- Para entradas válidas com $\varepsilon \le 1.0$, imprima:
  ```text
  Soma = %.6f
  Termos = %d
  ```

*Exemplo de entrada:* `0.1`  
*Saída esperada:*
```text
Soma = 1.361111
Termos = 3
```
*(Termos somados: $\frac{1}{1} + \frac{1}{4} + \frac{1}{9} = 1 + 0.25 + 0.111111 = 1.361111$, pois $\frac{1}{16} = 0.0625 < 0.1$).*

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `C09` (`Laços Aninhados e Formatação Tabular`):** somente após autocorreção dos exercícios `C08-E01..E06` **e** **100% de acerto (3/3)** na Checagem Independente `C08-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** revisar a regra de ouro de atualização incremental $\text{termo} \times \frac{x}{k}$ e o teste preventivo de tolerância `while (termo >= eps)` antes do acumulador.
- **Após 2 tentativas malsucedidas:** retornar a **`C02`** (acumuladores e contadores) e **`A09`** (precisão de tipos e literais reais).

---

## 6. Referências do Orientador
- `[DOC]` `Lista5_Algoritmos.pdf` p. 1–2 (Ex. 3, 4: cálculo de série de $e$ incremental e tolerância $\varepsilon$; Ex. 5: somatório $S = \sum 2^k / (n-k)^2$ adaptado da **Prova AED I UFPR 2017**).
- `[DOC]` `Lista8_Algoritmos_Revisao.pdf` p. 2 (Ex. 4: série de Taylor do logaritmo natural $\ln(1+x)$).
- `[DOC]` `00_inventario_fontes.md` Conflito C14 (precisão numérica e uso mandatório de `double` em fronteiras e séries).
- Casos de teste e soluções verificáveis: [C08_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/gabaritos/C08_gabarito.md) e [C08_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/C08_testes.md).
