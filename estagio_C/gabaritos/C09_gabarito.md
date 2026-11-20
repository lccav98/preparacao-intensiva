# Gabarito Comentado — Bloco `C09` (Laços Aninhados e Formatação Tabular)

> **Bloco de referência:** [C09_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/blocos/C09_bloco.md)  
> **Nota para Caça ao Bug:** Os códigos em `C09-E02` e `C09-C02` ilustram erros clássicos de posicionamento de `\n`, limite independente onde deveria ser dependente e ausência de largura fixa. As versões corrigidas compiláveis encontram-se em `testes/solucoes/`.

---

## 1. Gabarito dos Exercícios (`C09-E01` a `C09-E06`)

### `C09-E01` *(Teste de Mesa — Laços Aninhados Dependentes)*
Código:
```c
for (int i = 1; i <= 4; i++) {
    for (int j = 1; j <= i; j++) {
        printf("%3d", i * j);
    }
    printf("\n");
}
```

1. **Lista de pares `(i, j)` executados:**
   - `i = 1`: `(1, 1)` $\rightarrow$ 1 iteração
   - `i = 2`: `(2, 1), (2, 2)` $\rightarrow$ 2 iterações
   - `i = 3`: `(3, 1), (3, 2), (3, 3)` $\rightarrow$ 3 iterações
   - `i = 4`: `(4, 1), (4, 2), (4, 3), (4, 4)` $\rightarrow$ 4 iterações
   - **Total de iterações do laço interno:** $1 + 2 + 3 + 4 = 10$.

2. **Saída exata impressa (`%3d`):**
```text
  1
  2  4
  3  6  9
  4  8 12 16
```

---

### `C09-E02` *(Caça ao Bug — `printf("\n")` Mal Posicionado e Limite Invertido)*
1. **Explicação dos 2 bugs para `n = 3`:**
   - **Bug 1 (`j <= n` em vez de `j <= i`):** O laço interno não depende de `i`, imprimindo sempre todos os números de `1` até `n` em toda linha (formando um quadrado $3 \times 3$ em vez de um triângulo).
   - **Bug 2 (`printf("\n");` dentro do laço interno):** Faz com que cada número impresso pule imediatamente para uma nova linha, transformando as 9 impressões em uma única coluna vertical (`1`, `2`, `3`, `1`, `2`, `3`, `1`, `2`, `3`).
2. **Solução completa corrigida:** [C09_E02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C09_E02_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int n;
    if (scanf("%d", &n) != 1) {
        return 1;
    }

    if (n <= 0) {
        printf("Entrada Invalida\n");
        return 0;
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%3d", j);
        }
        printf("\n");
    }

    return 0;
}
```

---

### `C09-E03` *(Grade de Tabuada Formatada $L \times C$)*
Solução completa: [C09_E03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C09_E03.c)
```c
#include <stdio.h>

int main(void) {
    int linhas, cols;
    if (scanf("%d %d", &linhas, &cols) != 2) {
        return 1;
    }

    if (linhas <= 0 || cols <= 0) {
        printf("Entrada Invalida\n");
        return 0;
    }

    for (int i = 1; i <= linhas; i++) {
        for (int j = 1; j <= cols; j++) {
            printf("%4d", i * j);
        }
        printf("\n");
    }

    return 0;
}
```

---

### `C09-E04` *(Triângulo Numérico Invertido)*
Solução completa: [C09_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C09_E04.c)
```c
#include <stdio.h>

int main(void) {
    int n;
    if (scanf("%d", &n) != 1) {
        return 1;
    }

    if (n <= 0) {
        printf("Entrada Invalida\n");
        return 0;
    }

    for (int i = n; i >= 1; i--) {
        for (int j = 1; j <= i; j++) {
            printf("%3d", j);
        }
        printf("\n");
    }

    return 0;
}
```

---

### `C09-E05` *(Calendário Mensal Formatado — Lista 5 Ex. 6 UTFPR)*
Solução completa: [C09_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C09_E05.c)
```c
#include <stdio.h>

int main(void) {
    int dias, inicio;
    if (scanf("%d %d", &dias, &inicio) != 2) {
        return 1;
    }

    if (dias < 28 || dias > 31 || inicio < 1 || inicio > 7) {
        printf("Entrada Invalida\n");
        return 0;
    }

    printf("Dom Seg Ter Qua Qui Sex Sab\n");

    for (int i = 1; i < inicio; i++) {
        printf("    ");
    }

    for (int d = 1; d <= dias; d++) {
        printf("%3d", d);
        if ((inicio - 1 + d) % 7 == 0 || d == dias) {
            printf("\n");
        } else {
            printf(" ");
        }
    }

    return 0;
}
```
*Comentário:* Cada dia ocupa 3 colunas (`%3d`) mais 1 espaço separador (`" "` ou `"\n"`), totalizando 4 caracteres por coluna — exatamente a mesma largura de `"Dom "` ou `"    "` no recuo inicial.

---

### `C09-E06` *(Moldura Retangular Oca com Laços Aninhados)*
Solução completa: [C09_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C09_E06.c)
```c
#include <stdio.h>

int main(void) {
    int linhas, cols;
    if (scanf("%d %d", &linhas, &cols) != 2) {
        return 1;
    }

    if (linhas < 2 || cols < 2) {
        printf("Entrada Invalida\n");
        return 0;
    }

    for (int i = 1; i <= linhas; i++) {
        for (int j = 1; j <= cols; j++) {
            if (i == 1 || i == linhas || j == 1 || j == cols) {
                printf("#");
            } else {
                printf(" ");
            }
        }
        printf("\n");
    }

    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`C09-C01` a `C09-C03`)

### `C09-C01` *(Teste de Mesa — Pares `(i, j)` Dependentes)*
1. **Pares `(i, j)` executados:**
   - `i = 1`: `(1, 1), (1, 2), (1, 3), (1, 4)` (valores `i+j`: `2, 3, 4, 5`)
   - `i = 2`: `(2, 2), (2, 3), (2, 4)` (valores `i+j`: `4, 5, 6`)
   - `i = 3`: `(3, 3), (3, 4)` (valores `i+j`: `6, 7`)
   - `i = 4`: `(4, 4)` (valor `i+j`: `8`)
   - **Total de chamadas a `printf("%2d", i + j)`:** $4 + 3 + 2 + 1 = 10$.

2. **Saída exata impressa (`%2d`):**
```text
 2 3 4 5
 4 5 6
 6 7
 8
```

---

### `C09-C02` *(Caça ao Bug — Grade Sequencial com Quebra e Largura Incorretas)*
1. **Explicação dos erros:**
   - **Erro 1 (`%d` sem largura fixa):** Sem especificador de largura (como `%3d`), os números ficam colados uns aos outros sem separação e colunas com 1 e 2 dígitos perdem o alinhamento vertical.
   - **Erro 2 (`printf("\n");` dentro do laço interno):** Quebra a linha após cada único número em vez de quebrar somente ao término das `cols` colunas da linha `i`.
2. **Solução completa corrigida:** [C09_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C09_C02_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int linhas, cols;
    if (scanf("%d %d", &linhas, &cols) != 2) {
        return 1;
    }

    if (linhas <= 0 || cols <= 0) {
        printf("Entrada Invalida\n");
        return 0;
    }

    int num = 1;
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%3d", num++);
        }
        printf("\n");
    }

    return 0;
}
```

---

### `C09-C03` *(Programa Completo — Triângulo de Floyd com Largura Fixa)*
Solução completa: [C09_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C09_C03.c)
```c
#include <stdio.h>

int main(void) {
    int n;
    if (scanf("%d", &n) != 1) {
        return 1;
    }

    if (n <= 0) {
        printf("Entrada Invalida\n");
        return 0;
    }

    int num = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%3d", num++);
        }
        printf("\n");
    }

    return 0;
}
```
