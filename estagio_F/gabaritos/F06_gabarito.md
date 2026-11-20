# Gabarito Comentado — Bloco `F06` (Funções com Vetores 1D e Modificador `const`)

> **Bloco de referência:** [F06_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/blocos/F06_bloco.md)  
> **Nota para Caça ao Bug:** `F06-E03` e `F06-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`F06-E01` a `F06-E05`)

### `F06-E01` *(Análise Comparativa e Teste de Mesa)*
- **(a)** Saída exata:
  ```text
  a = 10
  vet = 4 8 12
  ```
- **(b)** Em C, toda passagem de argumento é **por valor**:
  - `tentar_dobrar(a)` recebe uma **cópia do valor `10`** no parâmetro local `x`; dobrar `x` não altera `a` em `main`.
  - Em `dobrar_vetor(vet, 3)`, o nome `vet` decai para o endereço do primeiro elemento (`&vet[0]`), e uma **cópia desse endereço** é passada por valor para o parâmetro `v`. Assim, `v[i]` acessa diretamente os elementos originais de `vet` na memória, dobrando-os para `4 8 12`.
  - A linha `v = NULL;` altera apenas a variável ponteiro local `v` dentro de `dobrar_vetor`, sem afetar `vet` em `main`.

### `F06-E02` *(Completar solução)*
- **`/* A */`:** `const int v[]`
- **`/* B */`:** `int *soma, double *media`
- **`/* C */`:** `&s, &m`
- **`/* D */`:**
```c
    for (int i = 0; i < n; i++) {
        total += v[i];
    }
    *soma = total;
    *media = (double)total / n;
```

### `F06-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. Em `main`, `contar_acima(v, n + 1, lim)` passa `n + 1` como tamanho, fazendo o laço ler `v[n]` (fora da faixa válida `0..n-1`, comportamento indefinido).
  2. Em `contar_acima`, o parâmetro é `const int v[]` (somente leitura), mas a linha `v[i] = 0;` tenta modificar o vetor, causando erro de compilação.
- **Solução corrigida completa:** [F06_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F06_E03_corrigido.c)
```c
#include <stdio.h>

int contar_acima(const int v[], int n, int limite);

int main(void) {
    int n, lim, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &lim);
    // Erro original 1: passava n + 1, lendo posicao invalida v[n] fora dos limites.
    // Correcao: passar exatamente n.
    printf("Acima: %d\n", contar_acima(v, n, lim));
    return 0;
}

int contar_acima(const int v[], int n, int limite) {
    int cont = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] > limite) {
            cont++;
        }
        // Erro original 2: tentava executar v[i] = 0; dentro de parametro const int v[].
        // Correcao: remover a escrita em v[i], preservando o contrato de somente leitura.
    }
    return cont;
}
```

### `F06-E04` *(Programa completo — Produto interno)*
Arquivo: [F06_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F06_E04.c)
```c
#include <stdio.h>

int produto_interno(const int a[], const int b[], int n);

int main(void) {
    int n, a[50], b[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    for (int i = 0; i < n; i++) {
        scanf("%d", &b[i]);
    }
    printf("Produto interno: %d\n", produto_interno(a, b, n));
    return 0;
}

int produto_interno(const int a[], const int b[], int n) {
    int soma = 0;
    for (int i = 0; i < n; i++) {
        soma += a[i] * b[i];
    }
    return soma;
}
```

### `F06-E05` *(Programa completo — Substituir negativos e imprimir)*
Arquivo: [F06_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F06_E05.c)
```c
#include <stdio.h>

void substituir_negativos(int v[], int n);
void imprimir_vetor(const int v[], int n);

int main(void) {
    int n, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    substituir_negativos(v, n);
    imprimir_vetor(v, n);
    return 0;
}

void substituir_negativos(int v[], int n) {
    for (int i = 0; i < n; i++) {
        if (v[i] < 0) {
            v[i] = 0;
        }
    }
}

void imprimir_vetor(const int v[], int n) {
    for (int i = 0; i < n; i++) {
        if (i > 0) {
            printf(" ");
        }
        printf("%d", v[i]);
    }
    printf("\n");
}
```

---

## 2. Gabarito da Checagem Independente (`F06-C01` a `F06-C03`)

### `F06-C01` *(Teste de Mesa e Análise)*
- **(a)** Saída impressa: **`x=5 v[0]=99`**
- **(b)** `x` é um `int` passado por valor (cópia do número `5`), logo `x = 99` altera apenas o parâmetro local. Já `v` decai para o endereço de `v[0]`, passado por valor ao ponteiro local `v` de `ajustar`; assim, `v[0] = 99` escreve no primeiro elemento do vetor original em `main`. A linha `v = NULL;` modifica somente a cópia local do ponteiro, não alterando `v` em `main`. Trocar `int v[]` por `int *v` no protótipo e na definição **não muda nada**, pois em parâmetros de função `int v[]` e `int *v` são equivalentes.

### `F06-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. Condição do laço `i <= n` lê `v[n]` além do último índice válido (`n - 1`). Deve ser `i < n`.
  2. Tentativa de alterar `v[i] = 0;` em parâmetro `const int v[]` (erro de compilação) para ignorar ímpares; basta somar somente quando `v[i] % 2 == 0`.
- **Solução corrigida completa:** [F06_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F06_C02_corrigido.c)
```c
#include <stdio.h>

int soma_pares(const int v[], int n);

int main(void) {
    int n, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    printf("Soma pares: %d\n", soma_pares(v, n));
    return 0;
}

int soma_pares(const int v[], int n) {
    int soma = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] % 2 == 0) {
            soma += v[i];
        }
    }
    return soma;
}
```

### `F06-C03` *(Programa completo — Estatísticas do vetor)*
Arquivo: [F06_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F06_C03.c)
```c
#include <stdio.h>

void estatisticas_vetor(const int v[], int n, int *menor, int *maior, double *media);

int main(void) {
    int n, v[50], menor, maior;
    double media;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    estatisticas_vetor(v, n, &menor, &maior, &media);
    printf("Menor: %d\nMaior: %d\nMedia: %.2f\n", menor, maior, media);
    return 0;
}

void estatisticas_vetor(const int v[], int n, int *menor, int *maior, double *media) {
    int soma = v[0];
    *menor = v[0];
    *maior = v[0];
    for (int i = 1; i < n; i++) {
        soma += v[i];
        if (v[i] < *menor) {
            *menor = v[i];
        }
        if (v[i] > *maior) {
            *maior = v[i];
        }
    }
    *media = (double)soma / n;
}
```
