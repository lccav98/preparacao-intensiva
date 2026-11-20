# Gabarito Comentado — Bloco `C01` (Repetição com Pré-Condição `while`)

> **Bloco de referência:** [C01_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/blocos/C01_bloco.md)  
> **Nota pedagógica:** Erros intencionais apresentados em `C01-E02` (falta de incremento e `;` após cabeçalho) ilustram causas comuns de laço infinito. Apenas a versão corrigida deve ser compilada e testada.

---

## 1. Gabarito dos Exercícios (`C01-E01` a `C01-E05`)

### `C01-E01` *(Teste de Mesa / Previsão Mental)*

**Trecho A:**
- `k = 1`: `1 < 5` (V) $\rightarrow$ imprime `2 ` $\rightarrow$ `k` vira `2`.
- `k = 2`: `2 < 5` (V) $\rightarrow$ imprime `4 ` $\rightarrow$ `k` vira `3`.
- `k = 3`: `3 < 5` (V) $\rightarrow$ imprime `6 ` $\rightarrow$ `k` vira `4`.
- `k = 4`: `4 < 5` (V) $\rightarrow$ imprime `8 ` $\rightarrow$ `k` vira `5`.
- `k = 5`: `5 < 5` (F) $\rightarrow$ encerra o laço.
- **Saída exata na tela:** `2 4 6 8 `
- **Número de iterações:** 4
- **Valor final de `k`:** 5

**Trecho B:**
- `w = 10`: teste `10 < 4` resulta em **Falso** imediatamente.
- **Saída exata na tela:** *(nenhuma saída gerada)*
- **Número de iterações:** 0
- **Valor final de `w`:** 10

---

### `C01-E02` *(Caça ao Bug — Laço Infinito e Comando Nulo)*
1. **Erro no Aluno 1:** A variável de controle `i` inicia em 1 e nunca é modificada no corpo do laço. Como `1 <= 5` permanece indefinidamente verdadeiro, o laço imprime `1` infinitas vezes e nunca encerra.
2. **Erro no Aluno 2:** O caractere `;` após `while (i <= 5)` fecha imediatamente a estrutura do laço, associando a ele uma instrução vazia (comando nulo). O programa entra em loop infinito executando apenas essa instrução vazia com `i = 1`, e o bloco entre chaves `{ printf("%d\n", i); i++; }` jamais é alcançado.
3. **Versão corrigida:** [C01_E02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C01_E02_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int i = 1;
    while (i <= 5) {
        printf("%d\n", i);
        i++;
    }
    return 0;
}
```

---

### `C01-E03` *(Completar Solução — Contagem Progressiva de 1 a N)*
- **Lacuna `/* A */`:** `1` (inicialização da contagem).
- **Lacuna `/* B */`:** `i <= n` (condição de continuação até `n` inclusive).
- **Lacuna `/* C */`:** `i++` ou `i = i + 1` (passo unitário).
- **Código completo:** [C01_E03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C01_E03.c)
```c
#include <stdio.h>

int main(void) {
    int n, i;
    scanf("%d", &n);

    i = 1;
    while (i <= n) {
        printf("%d\n", i);
        i++;
    }

    return 0;
}
```

---

### `C01-E04` *(Completar Solução — Contagem Regressiva Par com Passo 2)*
- **Lacuna 1 (condição):** `atual >= 0`
- **Lacuna 2 (atualização):** `atual -= 2` ou `atual = atual - 2`
- **Código completo:** [C01_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C01_E04.c)
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

    while (atual >= 0) {
        printf("%d\n", atual);
        atual -= 2;
    }

    return 0;
}
```

---

### `C01-E05` *(Resolução Independente — Intervalo Fechado [A, B])*
Arquivo: [C01_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C01_E05.c)
```c
#include <stdio.h>

int main(void) {
    int a, b;
    scanf("%d %d", &a, &b);

    while (a <= b) {
        printf("%d\n", a);
        a++;
    }

    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`C01-C01` a `C01-C03`)

### `C01-C01` *(Teste de Mesa / Avaliação de Iterações com Pré-Teste)*
1. **Valores impressos:**
   ```text
   2
   5
   8
   ```
   *(Nota: quando `x = 8 + 3 = 11`, o teste `11 <= 10` torna-se falso, então 11 não é impresso).*
2. **Número de iterações:** 3 iterações (para `x = 2`, `x = 5` e `x = 8`).
3. **Valor final armazenado em `x`:** `11`.
4. **Com valor inicial `x = 12`:** Como `12 <= 10` é falso de início, são executadas **0 iterações**.

---

### `C01-C02` *(Teste de Mesa / Laço Regressivo com Condição Estrita)*
- Início com `c = 10`.
  - Iteração 1: `10 > 3` (V) $\rightarrow$ `c` decrementa para `8` $\rightarrow$ imprime `8`.
  - Iteração 2: `8 > 3` (V) $\rightarrow$ `c` decrementa para `6` $\rightarrow$ imprime `6`.
  - Iteração 3: `6 > 3` (V) $\rightarrow$ `c` decrementa para `4` $\rightarrow$ imprime `4`.
  - Iteração 4: `4 > 3` (V) $\rightarrow$ `c` decrementa para `2` $\rightarrow$ imprime `2`.
  - Teste pós-iteração 4: `2 > 3` (F) $\rightarrow$ encerra.
1. **Números impressos:** `8`, `6`, `4`, `2` (um por linha).
2. **Número de iterações:** 4 iterações.
3. **Valor final de `c`:** `2`.

---

### `C01-C03` *(Programa Completo Independente — Intervalo com Passo Personalizado)*
Arquivo: [C01_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C01_C03.c)
```c
#include <stdio.h>

int main(void) {
    int inicio, fim, passo;
    scanf("%d %d %d", &inicio, &fim, &passo);

    while (inicio <= fim) {
        printf("%d\n", inicio);
        inicio += passo;
    }

    return 0;
}
```
