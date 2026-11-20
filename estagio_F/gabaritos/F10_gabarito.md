# Gabarito Comentado — Bloco `F10` (Revisão e Consolidação do Estágio F)

> **Bloco de referência:** [F10_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/blocos/F10_bloco.md)  
> **Nota para Caça ao Bug:** `F10-E03` no bloco do aluno contém **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`F10-E01` a `F10-E06`)

### `F10-E01` *(Teste de Mesa Integrado)*
- **(a)** Saída impressa: **`x=10 y=25 v0=11`**
- **(b)**
  - `x` em `alterar` é uma cópia local do valor `10` (variável independente da `x` de `main`), logo `x = 50;` não altera `main`.
  - `p` recebe inicialmente o endereço de `y` (passado por valor), portanto `*p = *p + 5;` soma `5` a `y` (`20 -> 25`). Depois `p = &k;` redireciona apenas o ponteiro local `p` para `k`, e `*p = 77;` altera `k`, deixando `y = 25`.
  - `v` decai para `&v[0]`, logo `v[0] += 10;` modifica diretamente o primeiro elemento do vetor de `main` (`1 -> 11`).

### `F10-E02` *(Diagnóstico Multi-Arquivo e Etapas GCC)*
1. **Etapa:** Ligação | **Erro:** `undefined reference to 'limpar_texto'` | **Correção:** incluir `texto.c` no comando: `gcc -std=c99 -Wall -Wextra main.c texto.c -o prog`.
2. **Etapa:** Compilação | **Erro:** `array type has incomplete element type` | **Correção:** informar a dimensão constante das colunas no parâmetro 2D, ex.: `void zerar(int m[][COL]);`.
3. **Etapa:** Ligação | **Erro:** `multiple definition of 'triplo'` | **Correção:** deixar apenas o protótipo `int triplo(int x);` em `calc.h` (com guardas `#ifndef`) e mover o corpo `{ return 3 * x; }` para `calc.c`.

### `F10-E03` *(Caça ao Bug Integrada — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. Em `main`, `resumo(v, n, soma, &maior);` passa o `int` `soma` (não inicializado) em vez do endereço `&soma`.
  2. Em `resumo`, `soma = 0;` altera apenas o ponteiro local para `NULL` em vez de zerar o alvo `*soma = 0;`.
  3. Em `limpar_espacos`, falta `s[j] = '\0';` após o laço, deixando caracteres antigos no fim da string.
- **Solução corrigida completa:** [F10_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F10_E03_corrigido.c)
```c
#include <stdio.h>

void resumo(const int v[], int n, int *soma, int *maior);
void limpar_espacos(char s[]);

int main(void) {
    char s[100];
    int n, v[50], soma, maior;

    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    // Erro original 1: passava soma (int) em vez de &soma (int *).
    // Correcao: passar o endereco &soma por valor.
    resumo(v, n, &soma, &maior);
    limpar_espacos(s);

    printf("Soma: %d\n", soma);
    printf("Maior: %d\n", maior);
    printf("Sem espacos: %s\n", s);
    return 0;
}

void resumo(const int v[], int n, int *soma, int *maior) {
    // Erro original 2: fazia soma = 0; (anulando a copia local do ponteiro) em vez de *soma = 0;.
    // Correcao: desreferenciar *soma para inicializar a variavel de main.
    *soma = 0;
    *maior = v[0];
    for (int i = 0; i < n; i++) {
        *soma += v[i];
        if (v[i] > *maior) {
            *maior = v[i];
        }
    }
}

void limpar_espacos(char s[]) {
    int j = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] != ' ') {
            s[j] = s[i];
            j++;
        }
    }
    // Erro original 3: nao gravava '\0' ao final da string modificada in-place.
    // Correcao: encerrar a string com s[j] = '\0';.
    s[j] = '\0';
}
```

### `F10-E04` *(Integração 1 — Composição, `const` e ponteiros de saída)*
Arquivo: [F10_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F10_E04.c)
```c
#include <stdio.h>

double media_vetor(const int v[], int n);
void analisar_vetor(const int v[], int n, int lim, int *acima_lim, double *media);

int main(void) {
    int n, v[50], lim, acima;
    double media;

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &lim);

    analisar_vetor(v, n, lim, &acima, &media);
    printf("Media: %.2f\n", media);
    printf("Acima do limite: %d\n", acima);
    return 0;
}

double media_vetor(const int v[], int n) {
    int soma = 0;
    for (int i = 0; i < n; i++) {
        soma += v[i];
    }
    return (double)soma / n;
}

void analisar_vetor(const int v[], int n, int lim, int *acima_lim, double *media) {
    *media = media_vetor(v, n);
    int cont = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] > lim) {
            cont++;
        }
    }
    *acima_lim = cont;
}
```

### `F10-E05` *(Integração 2 — Projeto Multi-Arquivo `matriz_ops`)*
Arquivos: [matriz_ops.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F10_E05/matriz_ops.h) | [matriz_ops.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F10_E05/matriz_ops.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F10_E05/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/F10_E05/main.c solucoes/F10_E05/matriz_ops.c -o prog
```

**`matriz_ops.h`:**
```c
#ifndef MATRIZ_OPS_H
#define MATRIZ_OPS_H

#define COL 3

int soma_diagonal_principal(const int m[][COL]);
void extremos_matriz(const int m[][COL], int linhas, int *menor, int *maior);

#endif
```

**`matriz_ops.c`:**
```c
#include "matriz_ops.h"

int soma_diagonal_principal(const int m[][COL]) {
    int soma = 0;
    for (int i = 0; i < COL; i++) {
        soma += m[i][i];
    }
    return soma;
}

void extremos_matriz(const int m[][COL], int linhas, int *menor, int *maior) {
    *menor = m[0][0];
    *maior = m[0][0];
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < COL; j++) {
            if (m[i][j] < *menor) {
                *menor = m[i][j];
            }
            if (m[i][j] > *maior) {
                *maior = m[i][j];
            }
        }
    }
}
```

**`main.c`:**
```c
#include <stdio.h>
#include "matriz_ops.h"

int main(void) {
    int m[COL][COL], mn, mx;
    for (int i = 0; i < COL; i++) {
        for (int j = 0; j < COL; j++) {
            scanf("%d", &m[i][j]);
        }
    }
    extremos_matriz(m, COL, &mn, &mx);
    printf("Diagonal principal: %d\n", soma_diagonal_principal(m));
    printf("Menor: %d\n", mn);
    printf("Maior: %d\n", mx);
    return 0;
}
```

### `F10-E06` *(Integração 3 — Projeto Multi-Arquivo `texto_ops`)*
Arquivos: [texto_ops.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F10_E06/texto_ops.h) | [texto_ops.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F10_E06/texto_ops.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F10_E06/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/F10_E06/main.c solucoes/F10_E06/texto_ops.c -o prog
```

**`texto_ops.h`:**
```c
#ifndef TEXTO_OPS_H
#define TEXTO_OPS_H

int contar_letras(const char s[]);
void substituir_caractere(char s[], char antigo, char novo);

#endif
```

**`texto_ops.c`:**
```c
#include "texto_ops.h"

int contar_letras(const char s[]) {
    int cont = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if ((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z')) {
            cont++;
        }
    }
    return cont;
}

void substituir_caractere(char s[], char antigo, char novo) {
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == antigo) {
            s[i] = novo;
        }
    }
}
```

**`main.c`:**
```c
#include <stdio.h>
#include "texto_ops.h"

int main(void) {
    char s[100], antigo, novo;
    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }
    scanf(" %c %c", &antigo, &novo);
    substituir_caractere(s, antigo, novo);
    printf("Texto: %s\n", s);
    printf("Letras: %d\n", contar_letras(s));
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`F10-C01` a `F10-C03`)

### `F10-C01` *(Teste de Mesa Integrado)*
- **(a)** Saída impressa: **`a=15 soma=27`** (`ajustar(p)` eleva `a` de `5` para `15`; `v[0] += *p` altera `v[0]` de `2` para `17`; `somar(v, 3)` calcula `17 + 4 + 6 = 27`).
- **(b)** Em `aplicar`, `p` já é do tipo `int *` (contém o endereço de `a`), logo é repassado como `ajustar(p)` sem `&`. Em `somar`, `const int v[]` impede que a função modifique os elementos do vetor original, garantindo leitura segura em tempo de compilação.

### `F10-C02` *(Diagnóstico Multi-Arquivo)*
1. **Ligação (`undefined reference to 'oper_media'`):** incluir `oper.c` no GCC (`gcc -std=c99 -Wall -Wextra main.c oper.c -o app`).
2. **Ligação (`multiple definition of 'dobro'`):** adicionar guardas `#ifndef OPER_H` / `#define OPER_H` / `#endif` em `oper.h`, deixar nele apenas o protótipo `int dobro(int x);` e mover o corpo para `oper.c`.
3. **Compilação (`conflicting types for 'oper_media'`):** uniformizar o tipo de retorno entre `oper.h` e `oper.c` (ambos `double`).

### `F10-C03` *(Projeto Multi-Arquivo Independente — `analise`)*
Arquivos: [analise.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F10_C03/analise.h) | [analise.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F10_C03/analise.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F10_C03/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/F10_C03/main.c solucoes/F10_C03/analise.c -o prog
```

**`analise.h`:**
```c
#ifndef ANALISE_H
#define ANALISE_H

#define COL 3

void linha_extremos(const int m[][COL], int linha, int *menor, int *maior);
int contar_ocorrencias_str(const char s[], char ch);

#endif
```

**`analise.c`:**
```c
#include "analise.h"

void linha_extremos(const int m[][COL], int linha, int *menor, int *maior) {
    *menor = m[linha][0];
    *maior = m[linha][0];
    for (int j = 1; j < COL; j++) {
        if (m[linha][j] < *menor) {
            *menor = m[linha][j];
        }
        if (m[linha][j] > *maior) {
            *maior = m[linha][j];
        }
    }
}

int contar_ocorrencias_str(const char s[], char ch) {
    int cont = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == ch) {
            cont++;
        }
    }
    return cont;
}
```

**`main.c`:**
```c
#include <stdio.h>
#include "analise.h"

int main(void) {
    int linhas, m[10][COL], idx, mn, mx;
    char s[50], ch;

    scanf("%d", &linhas);
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < COL; j++) {
            scanf("%d", &m[i][j]);
        }
    }
    scanf("%d", &idx);
    scanf("%49s", s);
    scanf(" %c", &ch);

    linha_extremos(m, idx, &mn, &mx);
    printf("Linha %d: menor=%d maior=%d\n", idx, mn, mx);
    printf("Ocorrencias: %d\n", contar_ocorrencias_str(s, ch));
    return 0;
}
```
