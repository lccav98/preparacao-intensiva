# Gabarito Comentado — Bloco `D02` (Acumulação, Contagem e Extremos em Vetores)

> **Bloco de referência:** [D02_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/blocos/D02_bloco.md)  
> **Nota para Caça ao Bug:** `D02-E03` e `D02-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`D02-E01` a `D02-E06`)

### `D02-E01` *(Teste de Mesa)*
Para `v = {-8, -3, -12, -3, -12, -5}` (`maior = -8, pos_maior = 0, menor = -8, pos_menor = 0`):
- **`i = 1` (`v[1] = -3`):** `-3 > -8` (V) → `maior = -3, pos_maior = 1`. Menor não muda.
- **`i = 2` (`v[2] = -12`):** Maior não muda. `-12 < -8` (V) → `menor = -12, pos_menor = 2`.
- **`i = 3` (`v[3] = -3`):** Com `>` → `-3 > -3` (F, mantém `pos_maior = 1`); com `>=` → `-3 >= -3` (V, atualiza `pos_maior = 3`).
- **`i = 4` (`v[4] = -12`):** Com `<` → `-12 < -12` (F, mantém `pos_menor = 2`); com `<=` → `-12 <= -12` (V, atualiza `pos_menor = 4`).
- **`i = 5` (`v[5] = -5`):** Nenhum extremo muda.
- **Resumo final:** Maior `= -3` (`1` com `>`, `3` com `>=`); Menor `= -12` (`2` com `<`, `4` com `<=`).

### `D02-E02` *(Completar solução)*
- **`/* A */`:** `0`
- **`/* B */`:** `v[0]`
- **`/* C */`:** `v[i] >= maior` *(usa `>=` para última ocorrência)*
- **`/* D */`:** `(double)soma / n`

### `D02-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `maior = 0, menor = 0;` falha se todos os valores forem negativos (`maior` fica `0`) ou todos positivos (`menor` fica `0`). Correto: `maior = v[0]; menor = v[0];`.
  2. `else if (v[i] < menor)` impede testar `menor` quando o `if (v[i] > maior)` é verdadeiro (erro conceitual de acoplamento). Correto: dois `if`s independentes.
  3. `double media = soma / n;` executa divisão inteira antes de converter para `double`. Correto: `(double)soma / n;`.
- **Solução corrigida completa:** [D02_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D02_E03_corrigido.c)
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int soma = 0, maior = v[0], menor = v[0];
    for (int i = 0; i < n; i++) {
        soma += v[i];
        if (v[i] > maior) {
            maior = v[i];
        }
        if (v[i] < menor) {
            menor = v[i];
        }
    }

    double media = (double)soma / n;
    printf("Media: %.2f\nMaior: %d\nMenor: %d\n", media, maior, menor);
    return 0;
}
```

### `D02-E04` *(Programa completo — Soma, média e acima da média)*
Arquivo: [D02_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D02_E04.c)
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int soma = 0;
    for (int i = 0; i < n; i++) {
        soma += v[i];
    }

    double media = (double)soma / n;
    int acima = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] > media) {
            acima++;
        }
    }

    printf("Soma: %d\nMedia: %.2f\nAcima da media: %d\n", soma, media, acima);
    return 0;
}
```

### `D02-E05` *(Programa completo — Menor e última ocorrência)*
Arquivo: [D02_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D02_E05.c)
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int menor = v[0], pos_menor = 0;
    for (int i = 1; i < n; i++) {
        if (v[i] <= menor) {
            menor = v[i];
            pos_menor = i;
        }
    }

    printf("Menor: %d\nIndice: %d\n", menor, pos_menor);
    return 0;
}
```

### `D02-E06` *(Programa completo — Maior 1ª ocorr. e menor última ocorr. em 1 percurso)*
Arquivo: [D02_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D02_E06.c)
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int maior = v[0], pos_maior = 0;
    int menor = v[0], pos_menor = 0;
    for (int i = 1; i < n; i++) {
        if (v[i] > maior) {
            maior = v[i];
            pos_maior = i;
        }
        if (v[i] <= menor) {
            menor = v[i];
            pos_menor = i;
        }
    }

    printf("Maior: %d (indice %d)\nMenor: %d (indice %d)\n",
           maior, pos_maior, menor, pos_menor);
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`D02-C01` a `D02-C03`)

### `D02-C01` *(Teste de Mesa)*
Para `v = {-4, -4, -9, -1, -9, -1}` (início: `maior = -4, pos_maior = 0, menor = -4, pos_menor = 0`):
- `i = 1 (-4)`: `-4 > -4` (F); `-4 <= -4` (V) → `menor = -4, pos_menor = 1`
- `i = 2 (-9)`: `-9 > -4` (F); `-9 <= -4` (V) → `menor = -9, pos_menor = 2`
- `i = 3 (-1)`: `-1 > -4` (V) → `maior = -1, pos_maior = 3`; `-1 <= -9` (F)
- `i = 4 (-9)`: `-9 > -1` (F); `-9 <= -9` (V) → `menor = -9, pos_menor = 4`
- `i = 5 (-1)`: `-1 > -1` (F); `-1 <= -9` (F)
- **Resultado final:** `maior = -1`, `pos_maior = 3`; `menor = -9`, `pos_menor = 4`.

### `D02-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `menor = 999, pos_menor = 1;` falha se todos os elementos forem `>= 1000` (e assume índice inicial `1` inválido se `n == 1` ou se o menor estiver em `0`). Correto: `menor = v[0], pos_menor = 0;`.
  2. O laço inicia em `i = 1`, deixando **`v[0]` de fora da contagem de `positivos`**! Correto: iniciar `for (int i = 0; i < n; i++)` (como `<` é estrito, `v[0] < v[0]` na 1ª iteração não altera `pos_menor`).
  3. Usa `v[i] <= menor`, registrando a **última** ocorrência em vez da **primeira**. Correto: `if (v[i] < menor)`.
- **Solução corrigida completa:** [D02_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D02_C02_corrigido.c)
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int positivos = 0;
    int menor = v[0], pos_menor = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] > 0) {
            positivos++;
        }
        if (v[i] < menor) {
            menor = v[i];
            pos_menor = i;
        }
    }

    printf("Positivos: %d\nMenor: %d (indice %d)\n", positivos, menor, pos_menor);
    return 0;
}
```

### `D02-C03` *(Programa completo — Percurso único completo)*
Arquivo: [D02_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D02_C03.c)
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int soma = 0, negativos = 0;
    int maior = v[0], pos_maior = 0;
    int menor = v[0], pos_menor = 0;

    for (int i = 0; i < n; i++) {
        soma += v[i];
        if (v[i] < 0) {
            negativos++;
        }
        if (v[i] > maior) {
            maior = v[i];
            pos_maior = i;
        }
        if (v[i] <= menor) {
            menor = v[i];
            pos_menor = i;
        }
    }

    double media = (double)soma / n;
    printf("Soma: %d\nMedia: %.2f\nNegativos: %d\nMaior: %d (indice %d)\nMenor: %d (indice %d)\n",
           soma, media, negativos, maior, pos_maior, menor, pos_menor);
    return 0;
}
```
