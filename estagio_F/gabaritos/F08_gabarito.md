# Gabarito Comentado — Bloco `F08` (Organização Multi-Arquivo `.h` e `.c`)

> **Bloco de referência:** [F08_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/blocos/F08_bloco.md)  
> **Nota para Caça ao Bug:** `F08-E03` no bloco do aluno contém **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`F08-E01` a `F08-E06`)

### `F08-E01` *(Diagnóstico sem Compilar — Os 4 erros clássicos)*
- **(a)** **`undefined reference to 'soma_vetor'`** (erro de ligação). O `.h` forneceu apenas o protótipo; faltou incluir `vetor.c` no comando de compilação: `gcc -std=c99 -Wall -Wextra main.c vetor.c -o prog`.
- **(b)** **`vetor.h: No such file or directory`** (erro de pré-processamento). `<...>` busca apenas nos diretórios padrão do sistema; cabeçalhos locais do projeto exigem aspas duplas: `#include "vetor.h"`.
- **(c)** **`multiple definition of 'dobro'`** (erro de ligação). Ao incluir `calc.h` em `main.c` e `calc.c`, ambos os arquivos `.o` geram o código compilado de `dobro`. Correção: manter no `calc.h` apenas o protótipo `int dobro(int x);` (com guardas `#ifndef`) e mover a implementação para `calc.c`.
- **(d)** **`conflicting types for 'media'`** (erro de compilação). O tipo de retorno no protótipo de `vetor.h` (`double`) diverge da definição em `vetor.c` (`int`). Correção: uniformizar ambas as assinaturas com `double`.

### `F08-E02` *(Completar cabeçalho `.h` e comando GCC)*
- **`/* A */`:** `#ifndef`
- **`/* B */`:** `#define`
- **`/* C */`:** `#endif`
- **(d)** Comando GCC:
  ```bash
  gcc -std=c99 -Wall -Wextra main.c stats.c -o app
  ```

### `F08-E03` *(Caça ao Bug Multi-Arquivo — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `calc.h` não possui guardas (`#ifndef CALC_H` / `#define CALC_H` / `#endif`) e contém o corpo completo de `soma_intervalo`, gerando `multiple definition` quando incluído por `main.c` e `calc.c`. Deve conter apenas os protótipos; a implementação vai para `calc.c`.
  2. `calc.h` declara `double contar_pares(int a, int b);`, mas `calc.c` define `int contar_pares(int a, int b)`, gerando `conflicting types`. Ambos devem retornar `int`.
  3. `main.c` usa `#include <calc.h>` em vez de `#include "calc.h"`, gerando `No such file or directory`.
- **Solução corrigida em 3 arquivos:** [calc.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F08_E03_corrigido/calc.h) | [calc.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F08_E03_corrigido/calc.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F08_E03_corrigido/main.c)
- **Comando GCC:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/F08_E03_corrigido/main.c solucoes/F08_E03_corrigido/calc.c -o prog
  ```

**`calc.h`:**
```c
#ifndef CALC_H
#define CALC_H

int soma_intervalo(int a, int b);
int contar_pares(int a, int b);

#endif
```

**`calc.c`:**
```c
#include "calc.h"

int soma_intervalo(int a, int b) {
    if (a > b) {
        int aux = a;
        a = b;
        b = aux;
    }
    int soma = 0;
    for (int i = a; i <= b; i++) {
        soma += i;
    }
    return soma;
}

int contar_pares(int a, int b) {
    if (a > b) {
        int aux = a;
        a = b;
        b = aux;
    }
    int cont = 0;
    for (int i = a; i <= b; i++) {
        if (i % 2 == 0) {
            cont++;
        }
    }
    return cont;
}
```

**`main.c`:**
```c
#include <stdio.h>
#include "calc.h"

int main(void) {
    int a, b;
    scanf("%d %d", &a, &b);
    printf("Soma: %d\n", soma_intervalo(a, b));
    printf("Pares: %d\n", contar_pares(a, b));
    return 0;
}
```

### `F08-E04` *(Projeto 3-arquivos — Módulo `vetor`)*
Arquivos: [vetor.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F08_E04/vetor.h) | [vetor.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F08_E04/vetor.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F08_E04/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/F08_E04/main.c solucoes/F08_E04/vetor.c -o prog
```

**`vetor.h`:**
```c
#ifndef VETOR_H
#define VETOR_H

void ler_vetor(int v[], int n);
int soma_vetor(const int v[], int n);
int maior_vetor(const int v[], int n);

#endif
```

**`vetor.c`:**
```c
#include <stdio.h>
#include "vetor.h"

void ler_vetor(int v[], int n) {
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
}

int soma_vetor(const int v[], int n) {
    int soma = 0;
    for (int i = 0; i < n; i++) {
        soma += v[i];
    }
    return soma;
}

int maior_vetor(const int v[], int n) {
    int maior = v[0];
    for (int i = 1; i < n; i++) {
        if (v[i] > maior) {
            maior = v[i];
        }
    }
    return maior;
}
```

**`main.c`:**
```c
#include <stdio.h>
#include "vetor.h"

int main(void) {
    int n, v[50];
    scanf("%d", &n);
    ler_vetor(v, n);
    printf("Soma: %d\n", soma_vetor(v, n));
    printf("Maior: %d\n", maior_vetor(v, n));
    return 0;
}
```

### `F08-E05` *(Projeto 3-arquivos — Módulo `matriz` 2D)*
Arquivos: [matriz.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F08_E05/matriz.h) | [matriz.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F08_E05/matriz.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F08_E05/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/F08_E05/main.c solucoes/F08_E05/matriz.c -o prog
```

**`matriz.h`:**
```c
#ifndef MATRIZ_H
#define MATRIZ_H

#define COL 3

void ler_matriz(int m[][COL], int linhas);
int soma_coluna(const int m[][COL], int linhas, int col);
int maior_matriz(const int m[][COL], int linhas);

#endif
```

**`matriz.c`:**
```c
#include <stdio.h>
#include "matriz.h"

void ler_matriz(int m[][COL], int linhas) {
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < COL; j++) {
            scanf("%d", &m[i][j]);
        }
    }
}

int soma_coluna(const int m[][COL], int linhas, int col) {
    int soma = 0;
    for (int i = 0; i < linhas; i++) {
        soma += m[i][col];
    }
    return soma;
}

int maior_matriz(const int m[][COL], int linhas) {
    int maior = m[0][0];
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < COL; j++) {
            if (m[i][j] > maior) {
                maior = m[i][j];
            }
        }
    }
    return maior;
}
```

**`main.c`:**
```c
#include <stdio.h>
#include "matriz.h"

int main(void) {
    int linhas, c, m[10][COL];
    scanf("%d %d", &linhas, &c);
    ler_matriz(m, linhas);
    printf("Soma coluna %d: %d\n", c, soma_coluna(m, linhas, c));
    printf("Maior: %d\n", maior_matriz(m, linhas));
    return 0;
}
```

### `F08-E06` *(Projeto 3-arquivos — Módulo `texto`)*
Arquivos: [texto.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F08_E06/texto.h) | [texto.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F08_E06/texto.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F08_E06/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/F08_E06/main.c solucoes/F08_E06/texto.c -o prog
```

**`texto.h`:**
```c
#ifndef TEXTO_H
#define TEXTO_H

int contar_ocorrencias(const char s[], char ch);
void para_maiusculas(char s[]);

#endif
```

**`texto.c`:**
```c
#include "texto.h"

int contar_ocorrencias(const char s[], char ch) {
    int cont = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == ch) {
            cont++;
        }
    }
    return cont;
}

void para_maiusculas(char s[]) {
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] >= 'a' && s[i] <= 'z') {
            s[i] = (char)(s[i] - 'a' + 'A');
        }
    }
}
```

**`main.c`:**
```c
#include <stdio.h>
#include "texto.h"

int main(void) {
    char s[100], ch;
    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }
    scanf(" %c", &ch);
    printf("Ocorrencias: %d\n", contar_ocorrencias(s, ch));
    para_maiusculas(s);
    printf("Maiusculas: %s\n", s);
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`F08-C01` a `F08-C03`)

### `F08-C01` *(Diagnóstico sem Compilar)*
1. **`undefined reference to 'calc_media'`:** faltou informar `mod.c` ao ligador no comando GCC (`gcc -std=c99 -Wall -Wextra main.c mod.c -o prog`).
2. **`multiple definition of 'f'`:** o corpo de `f` foi escrito no `.h`, sendo compilado tanto em `main.c` quanto em `mod.c`. Correção: deixar apenas `int f(int x);` em `mod.h` e mover a implementação para `mod.c`.
3. **`conflicting types for 'f'`:** o protótipo em `mod.h` retorna `void`, mas a definição em `mod.c` retorna `int`. Correção: alinhar o tipo de retorno entre `.h` e `.c`.

### `F08-C02` *(Escrita de `.h` válido)*
```c
#ifndef GEOMETRIA_H
#define GEOMETRIA_H

double area_retangulo(double base, double altura);
void retangulo_info(double base, double altura, double *area, double *perimetro);

#endif
```

### `F08-C03` *(Projeto 3-arquivos independente — Módulo `estatistica`)*
Arquivos: [estatistica.h](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F08_C03/estatistica.h) | [estatistica.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F08_C03/estatistica.c) | [main.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F08_C03/main.c)
```bash
gcc -std=c99 -Wall -Wextra solucoes/F08_C03/main.c solucoes/F08_C03/estatistica.c -o prog
```

**`estatistica.h`:**
```c
#ifndef ESTATISTICA_H
#define ESTATISTICA_H

double media_vetor(const int v[], int n);
int contar_no_intervalo(const int v[], int n, int min, int max);

#endif
```

**`estatistica.c`:**
```c
#include "estatistica.h"

double media_vetor(const int v[], int n) {
    int soma = 0;
    for (int i = 0; i < n; i++) {
        soma += v[i];
    }
    return (double)soma / n;
}

int contar_no_intervalo(const int v[], int n, int min, int max) {
    int cont = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] >= min && v[i] <= max) {
            cont++;
        }
    }
    return cont;
}
```

**`main.c`:**
```c
#include <stdio.h>
#include "estatistica.h"

int main(void) {
    int n, v[50], min, max;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d %d", &min, &max);
    printf("Media: %.2f\n", media_vetor(v, n));
    printf("No intervalo: %d\n", contar_no_intervalo(v, n, min, max));
    return 0;
}
```
