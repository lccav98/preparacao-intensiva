# Gabarito Comentado — Bloco `G09` (Revisão e Consolidação do Estágio G)

> **Bloco de referência:** [G09_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/blocos/G09_bloco.md)  
> **Nota para Caça ao Bug:** `G09-E03` no bloco do aluno contém **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`G09-E01` a `G09-E06`)

### `G09-E01` *(Teste de Mesa Integrado)*
- **(a)** Saída exata de `eco(3)`:
  ```text
  3 2 1 0
  1 2 3 
  ```
  *(Detalhe: `3 `, `2 `, `1 ` na descida; `0\n` no caso base `n == 0`; depois `1 `, `2 `, `3 ` no retorno das chamadas.)*
- **(b)** Árvore de `f(4)`: `f(4)` chama `f(3)` (que chama `f(2)` e `f(1)`) e `f(2)` (que chama `f(1)` e `f(0)`).
  - Valores: `f(0)=1`, `f(1)=2`, `f(2)=3`, `f(3)=5`, `f(4)=` **`8`**.
  - Total de chamadas: **`9`** (`f(4)` 1x, `f(3)` 1x, `f(2)` 2x, `f(1)` 3x, `f(0)` 2x).

### `G09-E02` *(Diagnóstico de Armadilhas Recursivas)*
1. **Dupla chamada exponencial em `maior`:** chama `maior(v, n - 1)` duas vezes na mesma execução (custo $O(2^n)$). Correção: guardar em variável local `int m = maior(v, n - 1);` e comparar `v[n - 1] > m`.
2. **Acesso antes do caso base:** calcula `v[n - 1]` **antes** de testar `if (n == 0) return 0;`, acessando `v[-1]` quando `n == 0`. Correção: colocar `if (n == 0) return 0;` como primeira instrução da função.
3. **Uso de laço em função que deveria ser recursiva:** usa `for` em vez de recursão por índice crescente (`i + 1`). Correção: testar `if (s[i] == '\0') return 0;` e retornar `(s[i] == c) + contar_letra(s, i + 1, c);`.

### `G09-E03` *(Caça ao Bug Integrada — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `soma_digitos` retorna `1` no caso base `n == 0`, adicionando `+1` indevido a toda soma. Deve retornar `0`.
  2. `maior_vetor` usa `if (n == 0) return 0;` (retorna `0` mesmo se todos os elementos forem negativos!) e ainda faz dupla chamada `maior_vetor(v, n - 1)`. Deve usar caso base `if (n == 1) return v[0];` e variável local `m`.
  3. `inverter` usa `if (i == j) return;`, falhando para strings de tamanho par ou vazias. Deve usar `if (i >= j) return;`.
- **Solução corrigida completa:** [G09_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G09_E03_corrigido.c)
```c
#include <stdio.h>

int soma_digitos(int n);
int maior_vetor(const int v[], int n);
int comprimento(const char s[], int i);
void inverter(char s[], int i, int j);

int main(void) {
    char s[100];
    int num, n, v[50];

    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }
    scanf("%d %d", &num, &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int len = comprimento(s, 0);
    inverter(s, 0, len - 1);

    printf("Soma digitos: %d\n", soma_digitos(num));
    printf("Maior: %d\n", maior_vetor(v, n));
    printf("Invertida: %s\n", s);
    return 0;
}

int soma_digitos(int n) {
    // Erro original 1: retornava 1 no caso base n == 0, somando 1 a mais.
    // Correcao: retornar 0 quando n == 0.
    if (n == 0) {
        return 0;
    }
    return (n % 10) + soma_digitos(n / 10);
}

int maior_vetor(const int v[], int n) {
    // Erro original 2: usava caso base n == 0 retornando 0 (falha com todos negativos) e fazia dupla chamada.
    // Correcao: caso base n == 1 retornando v[0] e chamada unica em variavel local m.
    if (n == 1) {
        return v[0];
    }
    int m = maior_vetor(v, n - 1);
    if (v[n - 1] > m) {
        return v[n - 1];
    }
    return m;
}

int comprimento(const char s[], int i) {
    if (s[i] == '\0') {
        return 0;
    }
    return 1 + comprimento(s, i + 1);
}

void inverter(char s[], int i, int j) {
    // Erro original 3: usava if (i == j), falhando para strings de tamanho par ou vazias.
    // Correcao: usar if (i >= j) return;.
    if (i >= j) {
        return;
    }
    char aux = s[i];
    s[i] = s[j];
    s[j] = aux;
    inverter(s, i + 1, j - 1);
}
```

### `G09-E04` *(Integração 1 — Vetores `const`, chamada única e média)*
Arquivo: [G09_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G09_E04.c)
```c
#include <stdio.h>

int maior_vetor(const int v[], int n);
double media_vetor(const int v[], int n);
int contar_acima(const int v[], int n, double lim);

int main(void) {
    int n, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    double med = media_vetor(v, n);
    printf("Maior: %d\n", maior_vetor(v, n));
    printf("Media: %.2f\n", med);
    printf("Acima da media: %d\n", contar_acima(v, n, med));
    return 0;
}

int maior_vetor(const int v[], int n) {
    if (n == 1) {
        return v[0];
    }
    int m = maior_vetor(v, n - 1);
    if (v[n - 1] > m) {
        return v[n - 1];
    }
    return m;
}

double media_vetor(const int v[], int n) {
    if (n == 1) {
        return (double)v[0];
    }
    return ((n - 1) * media_vetor(v, n - 1) + v[n - 1]) / n;
}

int contar_acima(const int v[], int n, double lim) {
    if (n == 0) {
        return 0;
    }
    return (v[n - 1] > lim) + contar_acima(v, n - 1, lim);
}
```

### `G09-E05` *(Integração 2 — Strings *in-place* e palíndromo)*
Arquivo: [G09_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G09_E05.c)
```c
#include <stdio.h>

void remover_char(char s[], int i, int j, char c);
int comprimento(const char s[], int i);
int eh_palindromo(const char s[], int i, int j);

int main(void) {
    char s[100], c;
    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }
    scanf(" %c", &c);

    remover_char(s, 0, 0, c);
    int len = comprimento(s, 0);

    printf("Limpa: %s\n", s);
    printf("Comprimento: %d\n", len);
    if (eh_palindromo(s, 0, len - 1)) {
        printf("Palindromo: Sim\n");
    } else {
        printf("Palindromo: Nao\n");
    }
    return 0;
}

void remover_char(char s[], int i, int j, char c) {
    if (s[i] == '\0') {
        s[j] = '\0';
        return;
    }
    if (s[i] != c) {
        s[j] = s[i];
        remover_char(s, i + 1, j + 1, c);
    } else {
        remover_char(s, i + 1, j, c);
    }
}

int comprimento(const char s[], int i) {
    if (s[i] == '\0') {
        return 0;
    }
    return 1 + comprimento(s, i + 1);
}

int eh_palindromo(const char s[], int i, int j) {
    if (i >= j) {
        return 1;
    }
    if (s[i] != s[j]) {
        return 0;
    }
    return eh_palindromo(s, i + 1, j - 1);
}
```

### `G09-E06` *(Integração 3 — Decomposição decimal e potenciação rápida)*
Arquivo: [G09_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G09_E06.c)
```c
#include <stdio.h>

int contar_digitos(int n);
int soma_digitos(int n);
double potencia_rapida(double x, int n);

int main(void) {
    int num, exp;
    double x;
    scanf("%d %lf %d", &num, &x, &exp);

    printf("Digitos: %d\n", contar_digitos(num));
    printf("Soma digitos: %d\n", soma_digitos(num));
    printf("Potencia: %.2f\n", potencia_rapida(x, exp));
    return 0;
}

int contar_digitos(int n) {
    if (n < 10) {
        return 1;
    }
    return 1 + contar_digitos(n / 10);
}

int soma_digitos(int n) {
    if (n == 0) {
        return 0;
    }
    return (n % 10) + soma_digitos(n / 10);
}

double potencia_rapida(double x, int n) {
    if (n == 0) {
        return 1.0;
    }
    if (n == 1) {
        return x;
    }
    double p = potencia_rapida(x, n / 2);
    if (n % 2 == 0) {
        return p * p;
    }
    return x * p * p;
}
```

---

## 2. Gabarito da Checagem Independente (`G09-C01` a `G09-C03`)

### `G09-C01` *(Teste de Mesa Integrado)*
1. Saída exata de `traco(4)`:
   ```text
   [4 [3 [2 [1 |
   1] 2] 3] 4] 
   ```
2. Chamar `potencia_rapida(x, n / 2)` duas vezes na mesma expressão faz com que cada chamada gere duas subchamadas idênticas, resultando em ~$n$ chamadas (árvore exponencial) em vez de $\approx \log_2 n$. Forma correta:
   ```c
   double p = potencia_rapida(x, n / 2);
   return p * p; /* ou x * p * p quando impar */
   ```

### `G09-C02` *(Implementação Integrada — Vetor `const` sem laços)*
Arquivo: [G09_C02.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G09_C02.c)
```c
#include <stdio.h>

int soma_pares(const int v[], int n);
int contem(const int v[], int n, int x);
double media_vetor(const int v[], int n);

int main(void) {
    int n, v[50], x;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &x);

    printf("Soma pares: %d\n", soma_pares(v, n));
    printf("Media: %.2f\n", media_vetor(v, n));
    if (contem(v, n, x)) {
        printf("Contem: Sim\n");
    } else {
        printf("Contem: Nao\n");
    }
    return 0;
}

int soma_pares(const int v[], int n) {
    if (n == 0) {
        return 0;
    }
    int termo = (v[n - 1] % 2 == 0) ? v[n - 1] : 0;
    return termo + soma_pares(v, n - 1);
}

int contem(const int v[], int n, int x) {
    if (n == 0) {
        return 0;
    }
    if (v[n - 1] == x) {
        return 1;
    }
    return contem(v, n - 1, x);
}

double media_vetor(const int v[], int n) {
    if (n == 1) {
        return (double)v[0];
    }
    return ((n - 1) * media_vetor(v, n - 1) + v[n - 1]) / n;
}
```

### `G09-C03` *(Implementação Integrada — String *in-place* + impressão no retorno)*
Arquivo: [G09_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G09_C03.c)
```c
#include <stdio.h>

void remover_vogais(char s[], int i, int j);
void imprimir_inversa(const char s[], int i);

int main(void) {
    char s[100];
    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }

    remover_vogais(s, 0, 0);
    printf("Sem vogais: %s\n", s);
    printf("Inversa: ");
    imprimir_inversa(s, 0);
    printf("\n");
    return 0;
}

void remover_vogais(char s[], int i, int j) {
    if (s[i] == '\0') {
        s[j] = '\0';
        return;
    }
    char c = s[i];
    int vogal = (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
                 c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
    if (!vogal) {
        s[j] = s[i];
        remover_vogais(s, i + 1, j + 1);
    } else {
        remover_vogais(s, i + 1, j);
    }
}

void imprimir_inversa(const char s[], int i) {
    if (s[i] == '\0') {
        return;
    }
    imprimir_inversa(s, i + 1);
    printf("%c", s[i]);
}
```
