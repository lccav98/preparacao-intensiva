# Gabarito Comentado — Bloco `G02` (Ordem de Execução na Pilha: Pré-Recursão vs. Pós-Recursão)

> **Bloco de referência:** [G02_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/blocos/G02_bloco.md)  
> **Nota para Caça ao Bug:** `G02-E03` no bloco do aluno contém **2 erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`G02-E01` a `G02-E05`)

### `G02-E01` *(Teste de mesa — Pré, Pós e Dupla Saída)*
- **(a) `f_pre(4)`:** `4 3 2 1 ` *(cada `printf` ocorre antes da chamada, na descida da pilha).*
- **(b) `f_pos(4)`:** `1 2 3 4 ` *(todos os `printf` aguardam na pilha e executam somente na subida, do topo `n = 1` até `n = 4`).*
- **(c) `f_dupla(3)`:** `3 2 1 1 2 3 `
  - Na descida, `f_dupla(3)`, `f_dupla(2)` e `f_dupla(1)` imprimem `3 `, `2 ` e `1 `.
  - `f_dupla(0)` atinge o caso base `n <= 0` e **retorna sem imprimir nada** para o quadro de `f_dupla(1)`.
  - Logo em seguida, o segundo `printf` de `f_dupla(1)` executa e imprime `1 `, iniciando a subida (`1 `, depois `2 `, depois `3 `).

### `G02-E02` *(Comparação Iteração × Recursão)*
- **(a)** Comparação:
  1. **Mecanismo de repetição:** a Versão A repete usando um laço `for` controlado pelo índice `i`; a Versão B repete por chamadas sucessivas da própria função com argumento `n - 1`.
  2. **Condição de parada:** a Versão A para quando `i <= n` se torna falso; a Versão B para ao atingir o caso base `if (n <= 0) return;`.
  3. **Uso de memória:** a Versão A mantém um único quadro na pilha durante todo o laço; a Versão B aloca `n + 1` quadros simultâneos na pilha de execução (um para cada valor de `n` até `0`).
- **(b)** Se `printf("%d", n);` for colocado **antes** de `imprimir_crescente(n - 1);`, a impressão passa a ocorrer na descida (pré-recursão), mudando a saída de `1 2 3 4` para a ordem decrescente `4 3 2 1` (ajustando o espaçamento).

### `G02-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. Falta o caso base `if (n <= 0) { return; }`: sem condição de parada, `espelho` chama `espelho(n - 1)` indefinidamente até causar *stack overflow*.
  2. Os dois blocos de impressão estão colocados **antes** da chamada recursiva (ambos pré-recursivos), imprimindo `3 32 21 1...` em vez de descer `3 2 1` e só então subir `1 2 3`.
- **Solução corrigida completa:** [G02_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G02_E03_corrigido.c)
```c
#include <stdio.h>

void espelho(int n);

int main(void) {
    int n;
    scanf("%d", &n);
    espelho(n);
    printf("\n");
    return 0;
}

void espelho(int n) {
    // Bug 1 original: faltava caso base (if (n <= 0) return;), causando stack overflow.
    if (n <= 0) {
        return;
    }
    // Pre-recursao (descida): imprime de n ate 1.
    printf("%d ", n);
    espelho(n - 1);
    // Bug 2 original: o segundo bloco de impressao estava antes da chamada recursiva.
    // Pos-recursao (subida): imprime de 1 ate n na volta da pilha.
    if (n > 1) {
        printf(" ");
    }
    printf("%d", n);
}
```

### `G02-E04` *(Completar solução — `sequencia_ab`)*
- **`/* A */`:** `if (n <= 0) { return; }`
- **`/* B */`:** `sequencia_ab(n - 1);`
- **`/* C */`:** `printf("B%d", n);`
- **Programa completo:** [G02_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G02_E04.c)
```c
#include <stdio.h>

void sequencia_ab(int n);

int main(void) {
    int n;
    scanf("%d", &n);
    sequencia_ab(n);
    printf("\n");
    return 0;
}

void sequencia_ab(int n) {
    if (n <= 0) {
        return;
    }
    printf("A%d ", n);
    sequencia_ab(n - 1);
    if (n > 1) {
        printf(" ");
    }
    printf("B%d", n);
}
```

### `G02-E05` *(Programa completo — Contagens regressiva e progressiva sem laços)*
Arquivo: [G02_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G02_E05.c)
```c
#include <stdio.h>

void contar_regressivo(int n);
void contar_progressivo(int n);

int main(void) {
    int n;
    scanf("%d", &n);

    printf("Regressivo:");
    if (n > 0) {
        printf(" ");
        contar_regressivo(n);
    }
    printf("\n");

    printf("Progressivo:");
    if (n > 0) {
        printf(" ");
        contar_progressivo(n);
    }
    printf("\n");
    return 0;
}

void contar_regressivo(int n) {
    if (n <= 0) {
        return;
    }
    printf("%d", n);
    if (n > 1) {
        printf(" ");
    }
    contar_regressivo(n - 1);
}

void contar_progressivo(int n) {
    if (n <= 0) {
        return;
    }
    contar_progressivo(n - 1);
    if (n > 1) {
        printf(" ");
    }
    printf("%d", n);
}
```

---

## 2. Gabarito da Checagem Independente (`G02-C01` a `G02-C03`)

### `G02-C01` *(Teste de mesa — 4 níveis)*
- **(a) `ida(4)`:** `I4 I3 I2 I1 `
- **(b) `volta(4)`:** `V1 V2 V3 V4 `

### `G02-C02` *(Teste de mesa — Dupla saída `eco(4)`)*
- **Descida:** `eco(4)` imprime `"4 "` → `eco(3)` imprime `"3 "` → `eco(2)` imprime `"2 "` → `eco(1)` imprime `"1 "` → `eco(0)` atinge `n <= 0`, imprime `"|"` e retorna.
- **Subida:** `eco(1)` imprime `" 1"` → `eco(2)` imprime `" 2"` → `eco(3)` imprime `" 3"` → `eco(4)` imprime `" 4"`.
- **Saída exata:**
```text
4 3 2 1 | 1 2 3 4
```

### `G02-C03` *(Programa completo — `pulso(n)`)*
Arquivo: [G02_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G02_C03.c)
```c
#include <stdio.h>

void pulso(int n);

int main(void) {
    int n;
    scanf("%d", &n);
    pulso(n);
    printf("\n");
    return 0;
}

void pulso(int n) {
    if (n <= 0) {
        printf("0");
        return;
    }
    printf("%d ", n);
    pulso(n - 1);
    printf(" %d", n);
}
```
