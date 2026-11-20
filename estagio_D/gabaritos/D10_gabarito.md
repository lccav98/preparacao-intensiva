# Gabarito Comentado — Bloco `D10` (Revisão e Consolidação do Estágio D)

> **Bloco de referência:** [D10_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/blocos/D10_bloco.md)  
> **Nota de Consolidação:** Este bloco integra todas as micro-habilidades de `D01` a `D09` sem conteúdo novo, sem matrizes 2D e sem funções auxiliares além de `int main(void)`.

---

## 1. Gabarito dos Exercícios (`D10-E01` a `D10-E06`)

### `D10-E01` *(Teste de Mesa Integrado)*
1. **Convolução válida** com kernel invertido `h_inv = {h[2], h[1], h[0]} = {4, 2, 1}` sobre `v = {2, 0, 1, 3, 2}`:
   - `r[0]` (`i = 0`): `2*4 + 0*2 + 1*1 = 8 + 0 + 1 = 9`
   - `r[1]` (`i = 1`): `0*4 + 1*2 + 3*1 = 0 + 2 + 3 = 5`
   - `r[2]` (`i = 2`): `1*4 + 3*2 + 2*1 = 4 + 6 + 2 = 12`
   - **Resultado:** `r = {9, 5, 12}`.
2. **Macro `INDICE`:**
   - `IND_OK(1 + 1, 2)` → `((1 + 1) * 4 + (2))` = **`10`** *(correto)*.
   - `IND_BUG(1 + 1, 2)` → `1 + 1 * 4 + 2` = **`7`** *(errado por precedência de `*` antes de `+`)*.

---

### `D10-E02` *(Caça ao Bug 1 — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `int freq[10];` não foi inicializado com `{0}`, acumulando lixo de memória. Correto: `int freq[10] = {0};`.
  2. `for (int i = 0; i <= n; i++)` lê `v[n]` (erro *off-by-one* fora dos limites do vetor). Correto: `i < n`.
  3. `aprov[i] = v[i];` grava na posição de leitura `i` em vez do índice independente `k`, deixando lixo nas posições puladas. Correto: `aprov[k] = v[i];`.
- **Solução corrigida completa:** [D10_E02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D10_E02_corrigido.c)
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n;
    int v[MAX], aprov[MAX];
    int freq[10] = {0};

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int k = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] >= 0 && v[i] <= 9) {
            freq[v[i]]++;
        }
        if (v[i] >= 6) {
            aprov[k] = v[i];
            k++;
        }
    }

    printf("Aprovadas:");
    if (k == 0) {
        printf(" Nenhuma\n");
    } else {
        for (int i = 0; i < k; i++) {
            printf(" %d", aprov[i]);
        }
        printf("\n");
    }

    for (int d = 0; d < 10; d++) {
        if (freq[d] > 0) {
            printf("Nota %d: %d\n", d, freq[d]);
        }
    }
    return 0;
}
```

---

### `D10-E03` *(Caça ao Bug 2 — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `orig[len - 1] = '0';` coloca o dígito `'0'` (`48`) em vez do terminador nulo `'\0'` (`0`). Correto: `orig[len - 1] = '\0';`.
  2. Falta fechar `norm[j] = '\0';` após o laço de remoção de espaços extras.
  3. `if (norm == "SAIR")` compara endereços de memória em vez de conteúdo. Correto: `if (strcmp(norm, "SAIR") == 0)`.
- **Solução corrigida completa:** [D10_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D10_E03_corrigido.c)
```c
#include <stdio.h>
#include <string.h>
#define MAX 101

int main(void) {
    char orig[MAX], norm[MAX];

    fgets(orig, MAX, stdin);
    int len = (int)strlen(orig);
    if (len > 0 && orig[len - 1] == '\n') {
        orig[len - 1] = '\0';
    }

    int j = 0, em_palavra = 0;
    for (int i = 0; orig[i] != '\0'; i++) {
        if (orig[i] != ' ') {
            if (j > 0 && !em_palavra) {
                norm[j++] = ' ';
            }
            norm[j++] = orig[i];
            em_palavra = 1;
        } else {
            em_palavra = 0;
        }
    }
    norm[j] = '\0';

    if (strcmp(norm, "SAIR") == 0) {
        printf("Encerrando\n");
    } else {
        printf("[%s] (%d)\n", norm, (int)strlen(norm));
    }
    return 0;
}
```

---

### `D10-E04` *(Programa completo — Convolução discreta 1D)*
Arquivo: [D10_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D10_E04.c)
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, m;
    int v[MAX], h[MAX], r[MAX];

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &m);
    for (int k = 0; k < m; k++) {
        scanf("%d", &h[k]);
    }

    int tam_r = n - m + 1;
    for (int i = 0; i < tam_r; i++) {
        int soma = 0;
        for (int k = 0; k < m; k++) {
            soma += v[i + k] * h[m - 1 - k];
        }
        r[i] = soma;
    }

    printf("Convolucao:");
    for (int i = 0; i < tam_r; i++) {
        printf(" %d", r[i]);
    }
    printf("\n");
    return 0;
}
```

---

### `D10-E05` *(Programa completo — Normalização de frase e histograma de vogais)*
Arquivo: [D10_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D10_E05.c)
```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define MAX 101

int main(void) {
    char orig[MAX], norm[MAX];
    int vog[5] = {0};

    fgets(orig, MAX, stdin);
    int len = (int)strlen(orig);
    if (len > 0 && orig[len - 1] == '\n') {
        orig[len - 1] = '\0';
    }

    int j = 0, em_palavra = 0;
    for (int i = 0; orig[i] != '\0'; i++) {
        if (orig[i] != ' ') {
            if (j > 0 && !em_palavra) {
                norm[j++] = ' ';
            }
            norm[j++] = orig[i];
            em_palavra = 1;

            char c = (char)tolower((unsigned char)orig[i]);
            if (c == 'a') {
                vog[0]++;
            } else if (c == 'e') {
                vog[1]++;
            } else if (c == 'i') {
                vog[2]++;
            } else if (c == 'o') {
                vog[3]++;
            } else if (c == 'u') {
                vog[4]++;
            }
        } else {
            em_palavra = 0;
        }
    }
    norm[j] = '\0';

    printf("[%s]\na:%d e:%d i:%d o:%d u:%d\n",
           norm, vog[0], vog[1], vog[2], vog[3], vog[4]);
    return 0;
}
```

---

### `D10-E06` *(Programa completo — Linearização 1D: transposta impressa e extremos)*
Arquivo: [D10_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D10_E06.c)
```c
#include <stdio.h>
#define MAX 225
#define INDICE(i, j, cols) ((i) * (cols) + (j))

int main(void) {
    int l, c;
    int v[MAX];

    scanf("%d %d", &l, &c);
    for (int i = 0; i < l; i++) {
        for (int j = 0; j < c; j++) {
            scanf("%d", &v[INDICE(i, j, c)]);
        }
    }

    printf("Transposta:\n");
    for (int j = 0; j < c; j++) {
        for (int i = 0; i < l; i++) {
            if (i > 0) {
                printf(" ");
            }
            printf("%d", v[INDICE(i, j, c)]);
        }
        printf("\n");
    }

    int maior = v[0], idx_maior = 0;
    int menor = v[0], idx_menor = 0;
    for (int idx = 1; idx < l * c; idx++) {
        if (v[idx] > maior) {
            maior = v[idx];
            idx_maior = idx;
        }
        if (v[idx] <= menor) {
            menor = v[idx];
            idx_menor = idx;
        }
    }

    printf("Maior: %d em (%d, %d)\n", maior, idx_maior / c, idx_maior % c);
    printf("Menor: %d em (%d, %d)\n", menor, idx_menor / c, idx_menor % c);
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`D10-C01` a `D10-C03`)

### `D10-C01` *(Teste de Mesa Integrado)*
1. **Inversão *in-place* de `{10, 20, 30, 40, 50}` (`5 / 2 = 2` iterações):**
   - `i = 0`: troca `v[0]` e `v[4]` → `{50, 20, 30, 40, 10}`.
   - `i = 1`: troca `v[1]` e `v[3]` → `{50, 40, 30, 20, 10}`.
   - **Vetor final:** `{50, 40, 30, 20, 10}`.
2. `strcmp("Algo", "algo")` retorna **`< 0`** (`'A'` = `65` < `'a'` = `97`). Já `((2) * 4 + (1))` e `2 * 4 + 1` valem ambos **`9`** (mas sem parênteses quebraria com expressões compostas como `1 + 1`).

---

### `D10-C02` *(Programa completo — Subvetor com sobreposição)*
Arquivo: [D10_C02.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D10_C02.c)
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int m, n;
    int v[MAX], p[MAX], pos[MAX];

    scanf("%d", &m);
    for (int i = 0; i < m; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &n);
    for (int k = 0; k < n; k++) {
        scanf("%d", &p[k]);
    }

    int qtd = 0;
    for (int i = 0; i <= m - n; i++) {
        int casa = 1;
        for (int k = 0; k < n; k++) {
            if (v[i + k] != p[k]) {
                casa = 0;
                break;
            }
        }
        if (casa) {
            pos[qtd++] = i;
        }
    }

    printf("Ocorrencias: %d\nPosicoes:", qtd);
    if (qtd == 0) {
        printf(" Nenhuma\n");
    } else {
        for (int i = 0; i < qtd; i++) {
            printf(" %d", pos[i]);
        }
        printf("\n");
    }
    return 0;
}
```

---

### `D10-C03` *(Programa completo — Palíndromo in-place + histograma de letras)*
Arquivo: [D10_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D10_C03.c)
```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define MAX 101

int main(void) {
    char s[MAX];
    int freq[26] = {0};

    fgets(s, MAX, stdin);
    int len = (int)strlen(s);
    if (len > 0 && s[len - 1] == '\n') {
        s[len - 1] = '\0';
        len--;
    }

    int i = 0, j = len - 1, eh_pal = 1;
    while (i < j) {
        while (i < j && s[i] == ' ') {
            i++;
        }
        while (i < j && s[j] == ' ') {
            j--;
        }
        if (tolower((unsigned char)s[i]) != tolower((unsigned char)s[j])) {
            eh_pal = 0;
            break;
        }
        i++;
        j--;
    }

    int tem_letra = 0;
    for (int k = 0; k < len; k++) {
        char c = (char)tolower((unsigned char)s[k]);
        if (c >= 'a' && c <= 'z') {
            freq[c - 'a']++;
            tem_letra = 1;
        }
    }

    printf("Palindromo: %s\n", eh_pal ? "Sim" : "Nao");
    if (!tem_letra) {
        printf("Sem letras\n");
    } else {
        for (int k = 0; k < 26; k++) {
            if (freq[k] > 0) {
                printf("%c: %d\n", 'a' + k, freq[k]);
            }
        }
    }
    return 0;
}
```
