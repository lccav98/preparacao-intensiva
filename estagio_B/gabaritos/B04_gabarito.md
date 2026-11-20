# Gabarito Comentado — Bloco `B04` (`if / else` vs. `if`s Independentes)

> **Bloco de referência:** [B04_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/blocos/B04_bloco.md)  
> **Nota para Caça ao Bug:** O código em `B04-E03` no bloco do aluno contém **erro intencional** de condições sobrepostas em dois `if`s independentes. Apenas a versão corrigida deve ser compilada.

---

## 1. Gabarito dos Exercícios (`B04-E01` a `B04-E05`)

### `B04-E01` *(Teste de Mesa / Comparação Semântica)*
Considere `x = 3` avaliado nos dois trechos:

- **Trecho 1 (Dois `if`s independentes com mutação de estado):**
  ```c
  if (x > 0) {
      x = x - 5;
  }
  if (x <= 0) {
      printf("A\n");
  }
  ```
  1. `x > 0` ($3 > 0$) é verdadeiro $\to x$ passa a valer $3 - 5 = -2$.
  2. O segundo `if` é avaliado de forma independente: `x <= 0` ($-2 \le 0$) agora é verdadeiro!
  3. Imprime: **`A`**.

- **Trecho 2 (Desvio composto `if / else`):**
  ```c
  if (x > 0) {
      x = x - 5;
  } else {
      printf("A\n");
  }
  ```
  1. `x > 0` ($3 > 0$) é verdadeiro $\to x$ passa a valer $-2$.
  2. Como o ramo `if` foi executado, o ramo `else` é **automaticamente ignorado**.
  3. **Nada é impresso**.

*Conclusão pedagógica:* `if / else` garante exclusão mútua mesmo que o bloco execute alterações nas variáveis testadas. Dois `if`s independentes reavaliam a segunda condição sobre o novo estado da variável!

---

### `B04-E02` *(Completar Solução — Par ou Ímpar com `if / else`)*
Arquivo: [B04_E02.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B04_E02.c)
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

---

### `B04-E03` *(Caça ao Bug — Saída Duplicada em Fronteira)*
- **Erro intencional:** Dois `if`s independentes testando `nota >= 6.0` e `nota <= 6.0`. Quando `nota == 6.0`, **ambas as condições são verdadeiras**, imprimindo `Aprovado` e `Reprovado` ao mesmo tempo!
- **Correção:** Utilizar a estrutura composta `if / else`. Se `nota >= 6.0` for verdadeira, executa o `if`; caso contrário, o `else` captura estritamente as notas `< 6.0`.
- **Solução corrigida completa:** [B04_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B04_E03_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    double nota;
    scanf("%lf", &nota);

    if (nota >= 6.0) {
        printf("Aprovado\n");
    } else {
        printf("Reprovado\n");
    }

    return 0;
}
```

---

### `B04-E04` *(Completar Solução — Múltiplos Divisores e Flag 'Nenhum')*
Arquivo: [B04_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B04_E04.c)
```c
#include <stdio.h>

int main(void) {
    int n, achou = 0;
    scanf("%d", &n);

    if (n % 2 == 0) {
        printf("Divisivel por 2\n");
        achou = 1;
    }
    if (n % 3 == 0) {
        printf("Divisivel por 3\n");
        achou = 1;
    }
    if (n % 5 == 0) {
        printf("Divisivel por 5\n");
        achou = 1;
    }
    if (achou == 0) {
        printf("Nenhum divisor encontrado\n");
    }

    return 0;
}
```

---

### `B04-E05` *(Resolução Independente — Crédito Especial)*
Arquivo: [B04_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B04_E05.c)
```c
#include <stdio.h>

int main(void) {
    double saldo_medio, credito;
    scanf("%lf", &saldo_medio);

    if (saldo_medio > 1000.0) {
        credito = saldo_medio * 0.30;
    } else {
        credito = saldo_medio * 0.15;
    }

    printf("Saldo medio: R$ %.2f\n", saldo_medio);
    printf("Credito especial: R$ %.2f\n", credito);
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`B04-C01` a `B04-C03`)

### `B04-C01` *(Análise Conceitual — `if`+`if` vs. `if/else`)*
1. **Exclusão mútua garantida:** No `if/else`, a arquitetura da linguagem garante que **exatamente um** dos blocos será executado. Se a condição do `if` for verdadeira, o `else` é sumariamente descartado. Em dois `if`s independentes, se a lógica não for estritamente disjunta ou se uma variável for alterada, ambos os blocos podem ser executados (ou ambos podem falhar).
2. **Eficiência computacional:** No `if/else`, quando a condição inicial é verdadeira, o compilador não gasta ciclos de processador avaliando uma segunda condição.
3. **Legibilidade e prevenção de bugs:** Dois `if`s sugerem ao leitor que são eventos independentes que podem ocorrer simultaneamente; `if/else` expressa com clareza matemática que se trata de uma bifurcação binária complementar.

---

### `B04-C02` *(Programa Completo — Termômetro Febril)*
Arquivo: [B04_C02.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B04_C02.c)
```c
#include <stdio.h>

int main(void) {
    double temp;
    scanf("%lf", &temp);

    if (temp >= 37.8) {
        printf("Estado febril: %.1f C\n", temp);
    } else {
        printf("Temperatura normal: %.1f C\n", temp);
    }

    return 0;
}
```

---

### `B04-C03` *(Programa Completo — Permissões Múltiplas e Flag de Controle)*
Arquivo: [B04_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B04_C03.c)
```c
#include <stdio.h>

int main(void) {
    int codigo, permissoes = 0;
    scanf("%d", &codigo);

    if (codigo % 2 == 0) {
        printf("Permissao de Leitura\n");
        permissoes = 1;
    }
    if (codigo % 3 == 0) {
        printf("Permissao de Escrita\n");
        permissoes = 1;
    }
    if (codigo % 5 == 0) {
        printf("Permissao de Execucao\n");
        permissoes = 1;
    }
    if (permissoes == 0) {
        printf("Sem permissoes especiais\n");
    }

    return 0;
}
```
