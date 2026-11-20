# Gabarito Comentado — Bloco `C03` (Leituras por Sentinela e Algoritmos Iterativos com `while`)

> **Bloco de referência:** [C03_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/blocos/C03_bloco.md)  
> **Nota para Caça ao Bug:** Em `C03-E02` e `C03-C02`, os trechos originais contêm defeitos conceituais intencionais (leitura dentro do laço somando a sentinela, `maior = 0` com negativos e sobrescrita prematura de `m` antes do cálculo do resto). Apenas as versões corrigidas devem ser compiladas.

---

## 1. Gabarito dos Exercícios (`C03-E01` a `C03-E06`)

### Sessão 1 (`E01`–`E03`)

### `C03-E01` *(Teste de Mesa / Algoritmo de Euclides)*

1. **Par `m = 15, n = 25`:**

| Iteração | `m` no início | `n` no início | `resto = m % n` | Novo `m = n` | Novo `n = resto` |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 15 | 25 | $15 \pmod{25} = 15$ | 25 | 15 *(inverteu!)* |
| 2 | 25 | 15 | $25 \pmod{15} = 10$ | 15 | 10 |
| 3 | 15 | 10 | $15 \pmod{10} = 5$ | 10 | 5 |
| 4 | 10 | 5 | $10 \pmod{5} = 0$ | 5 | 0 |
| Saída | 5 | 0 | *(encerra: `n == 0`)* | `m = 5` | `n = 0` |

Resultado: $\text{MDC}(15, 25) = \mathbf{5}$.

2. **Par `m = 24, n = 9`:**

| Iteração | `m` no início | `n` no início | `resto = m % n` | Novo `m = n` | Novo `n = resto` |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 24 | 9 | $24 \pmod{9} = 6$ | 9 | 6 |
| 2 | 9 | 6 | $9 \pmod{6} = 3$ | 6 | 3 |
| 3 | 6 | 3 | $6 \pmod{3} = 0$ | 3 | 0 |
| Saída | 3 | 0 | *(encerra: `n == 0`)* | `m = 3` | `n = 0` |

Resultado: $\text{MDC}(24, 9) = \mathbf{3}$.

---

### `C03-E02` *(Caça ao Bug — Sentinela Somada e Máximo com Negativos)*

1. **Por que `maior = 0` falha com temperaturas negativas:** Se todas as temperaturas informadas forem negativas (ex.: `-10, -5, -8`), a condição `temp > maior` (`temp > 0`) será sempre falsa. Ao final, o programa imprimirá `Maior: 0`, um valor artificial que nunca fez parte dos dados lidos (o maior real seria `-5`). *(Observação adicional: no código original, `temp` também é testada no `while (temp != -999)` antes de ser lida ou inicializada, causando comportamento indefinido na primeira verificação.)*
2. **Por que a leitura no início do `while` soma a sentinela `-999`:** Quando `scanf("%d", &temp);` ocorre dentro do corpo antes do processamento, a condição `temp != -999` já foi testada na volta anterior. Ao digitar `-999`, o valor é lido e imediatamente acumulado por `soma += temp;` antes de o fluxo retornar ao cabeçalho do `while` para encerrar o laço.
3. **Versão corrigida completa com *priming read*:** [C03_E02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C03_E02_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int temp;
    int soma = 0;
    int maior;

    scanf("%d", &temp);
    if (temp != -999) {
        maior = temp;
        while (temp != -999) {
            soma += temp;
            if (temp > maior) {
                maior = temp;
            }
            scanf("%d", &temp);
        }
        printf("Soma: %d\n", soma);
        printf("Maior: %d\n", maior);
    }

    return 0;
}
```

---

### `C03-E03` *(Completar Solução — Contagem e Soma com Sentinela 0)*
- **Lacuna `/* A */`:** `scanf("%d", &x);` *(já fornecida como leitura prévia antes do laço)*.
- **Lacuna `/* B */`:** `x != 0`
- **Lacuna `/* C */`:** `conta++`
- **Lacuna `/* D */`:** `scanf("%d", &x)`
- **Código completo:** [C03_E03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C03_E03.c)
```c
#include <stdio.h>

int main(void) {
    int x;
    int conta = 0;
    int soma = 0;

    scanf("%d", &x);

    while (x != 0) {
        soma += x;
        conta++;
        scanf("%d", &x);
    }

    printf("Quantidade: %d\n", conta);
    printf("Soma: %d\n", soma);
    return 0;
}
```

---

### Sessão 2 (`E04`–`E06`)

### `C03-E04` *(Completar Solução — Média Real com Sentinela Negativa)*
- **Lacuna 1 (condição para positivos):** `valor > 0.0` *(ou `valor > 0`)*
- **Lacuna 2 (releitura de `valor`):** `scanf("%lf", &valor)`
- **Lacuna 3 (teste se houve leitura):** `qtd > 0`
- **Código completo:** [C03_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C03_E04.c)
```c
#include <stdio.h>

int main(void) {
    double valor;
    double soma = 0.0;
    int qtd = 0;

    scanf("%lf", &valor);

    while (valor > 0.0) {
        soma += valor;
        qtd++;
        scanf("%lf", &valor);
    }

    if (qtd > 0) {
        printf("Media: %.2f\n", soma / qtd);
    } else {
        printf("Nenhum positivo lido\n");
    }

    return 0;
}
```

---

### `C03-E05` *(Programa Completo Independente — MDC de Euclides Iterativo)*
Arquivo: [C03_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C03_E05.c)
```c
#include <stdio.h>

int main(void) {
    int a, b;
    int m, n, resto;

    scanf("%d %d", &a, &b);

    m = a;
    n = b;

    while (n != 0) {
        resto = m % n;
        m = n;
        n = resto;
    }

    printf("MDC: %d\n", m);
    return 0;
}
```
*Comentário:* O uso das variáveis auxiliares `m` e `n` preserva os valores originais de `a` e `b` caso sejam necessários posteriormente. Se `a < b`, a primeira iteração realiza automaticamente a troca via `resto = a % b = a`, `m = b`, `n = a`.

---

### `C03-E06` *(Programa Completo Independente — Maior e Menor com Sentinela)*
Arquivo: [C03_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C03_E06.c)
```c
#include <stdio.h>

int main(void) {
    int valor;
    int maior, menor;

    scanf("%d", &valor);

    if (valor == -1) {
        printf("Nenhum dado informado\n");
    } else {
        maior = valor;
        menor = valor;

        while (valor != -1) {
            if (valor > maior) {
                maior = valor;
            }
            if (valor < menor) {
                menor = valor;
            }
            scanf("%d", &valor);
        }

        printf("Maior: %d\n", maior);
        printf("Menor: %d\n", menor);
    }

    return 0;
}
```
*Comentário:* Inicializar `maior` e `menor` com o primeiro valor válido lido garante funcionamento correto para qualquer escala numérica e protege o programa contra o caso de borda em que `-1` é digitado logo na entrada.

---

## 2. Gabarito da Checagem Independente (`C03-C01` a `C03-C03`)

### `C03-C01` *(Teste de Mesa / Entrada Vazia no Priming Read)*
1. **Entrada `0`:** O laço executa **0 iterações**, pois após o `scanf` prévio (`val = 0`), a condição `val != 0` já é falsa na primeira avaliação. O programa imprime exatamente: `Contagem: 0`.
2. **Entrada `4 7 0`:** O laço executa 2 iterações (para `4` e `7`) e para quando `val` recebe `0`. Imprime exatamente: `Contagem: 2`.
3. **O número `0` é contado?** **Não**, em nenhuma das duas situações. Pelo padrão *priming read*, o teste `while (val != 0)` sempre precede o incremento `cont++`: quando `0` é lido antes do laço (caso 1) ou ao final da última iteração válida (caso 2), a condição `val != 0` falha imediatamente antes de entrar novamente no corpo.

---

### `C03-C02` *(Teste de Mesa / Ordem das Atribuições em Euclides)*
1. **Explicação do bug:** Ao executar `m = n;` na Linha 1 primeiro, o valor anterior de `m` é sobrescrito e perdido, passando `m` e `n` a terem exatamente o mesmo valor. Em seguida, na Linha 2, o cálculo `m % n` equivale a `n % n`, que é sempre **`0`**. Assim, `n` torna-se `0` logo na 1ª iteração e o laço encerra prematuramente devolvendo o `n` original como se fosse o MDC (ex.: para `m = 12, n = 8`, retornaria incorretamente `8` em vez de `4`).
2. **Sequência correta de 3 atribuições:**
   ```c
   resto = m % n;
   m = n;
   n = resto;
   ```

---

### `C03-C03` *(Programa Completo Independente — Estatísticas de Fluxo com Sentinela)*
Arquivo: [C03_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C03_C03.c)
```c
#include <stdio.h>

int main(void) {
    int valor;
    int conta = 0;
    int soma = 0;
    int maior;

    scanf("%d", &valor);

    if (valor == 0) {
        printf("Nenhum valor valido\n");
    } else {
        maior = valor;
        while (valor != 0) {
            conta++;
            soma += valor;
            if (valor > maior) {
                maior = valor;
            }
            scanf("%d", &valor);
        }

        printf("Quantidade: %d\n", conta);
        printf("Soma: %d\n", soma);
        printf("Media: %.2f\n", (double)soma / conta);
        printf("Maior: %d\n", maior);
    }

    return 0;
}
```
*Comentário:* O *cast* `(double)soma / conta` evita a divisão inteira truncada, e o ramo `if (valor == 0)` impede tanto a divisão por zero quanto a impressão de uma variável `maior` não inicializada.
