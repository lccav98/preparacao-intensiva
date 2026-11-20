# Bloco `D02` — Acumulação, Contagem Condicional e Busca de Extremos com Índices em Vetores

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio D — Vetores Unidimensionais e Strings / **`D02`** |
| **Micro-habilidade foco** | Calcular soma, contagem condicional e maior/menor elemento com seus índices em único percurso, aplicando desempate correto (`>` vs `<=` / `>=`). |
| **Pré-requisitos** | `D01` *(Vetores 1D: declaração, índices base 0, inicialização e limites de memória)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Sessão 2 (`E04`–`E06`, 24 min):** `15 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Não utilize** funções próprias além de `main`, strings (`char[]`/`<string.h>`), matrizes 2D ou VLAs (vetores de tamanho variável). Use `#define MAX 100` e `int v[MAX];` lendo `n` (`1 <= n <= MAX`). |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Nunca inicialize `maior` ou `menor` com `0` ou `999`:** se todos os elementos forem negativos (`{-8, -3}`), `maior = 0` falha; se todos forem grandes (`{1200, 1500}`), `menor = 999` falha. **Sempre inicialize com `v[0]` e índice `0`** (assumindo `n >= 1`).
2. **Regra de desempate pelo operador:**
   - **Primeira ocorrência** (menor índice): use comparação **estrita** (`v[i] > maior` ou `v[i] < menor`).
   - **Última ocorrência** (maior índice): use comparação **inclusiva** (`v[i] >= maior` ou `v[i] <= menor`).
3. **Maior e menor no mesmo laço (`i = 0` vs `i = 1`):** use **dois `if`s independentes** (`if (v[i] > maior)` e `if (v[i] <= menor)`), e **nunca** `else if`. Embora valores distintos não possam superar o máximo e ficar abaixo do mínimo simultaneamente, acoplá-los em `else if` falha em comparações `>=`/`<=` na posição `0` (ou com `n = 1`, onde `maior == menor`) e quebra a independência ao incluir somas/contagens no mesmo laço. Além disso: quando o laço calcula **apenas** extremos, pode iniciar em `i = 1`; quando **também** acumula `soma` ou conta elementos no mesmo percurso, **inicie obrigatoriamente em `i = 0`** para não excluir `v[0]`.
4. **Média real de vetor inteiro:** converta a soma antes de dividir: `double media = (double)soma / n;`.

---

## 2. Exemplos Guiados

### Exemplo 1 — Maior elemento e primeira ocorrência com negativos *(Trecho ilustrativo)*
Para `int v[5] = {-10, -4, -9, -4, -7};` (`n = 5`):
```c
int maior = v[0];      /* maior = -10 */
int pos_maior = 0;     /* indice 0 */

for (int i = 1; i < n; i++) {
    if (v[i] > maior) {        /* estrito '>' preserva a 1a ocorrencia */
        maior = v[i];
        pos_maior = i;
    }
}
/* Resultado: maior = -4, pos_maior = 1 (nao atualiza em i = 3 porque -4 > -4 eh falso) */
```

### Exemplo 2 — Soma, média real e extremos em um único percurso *(Programa completo)*
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
    int maior = v[0], pos_maior = 0;
    int pares = 0;

    for (int i = 0; i < n; i++) {
        soma += v[i];
        if (v[i] % 2 == 0) {
            pares++;
        }
        if (v[i] > maior) {
            maior = v[i];
            pos_maior = i;
        }
    }

    double media = (double)soma / n;
    printf("Media: %.2f\nPares: %d\nMaior: %d (indice %d)\n",
           media, pares, maior, pos_maior);
    return 0;
}
```

---

## 3. Exercícios (`D02-E01` a `D02-E06`)

### Sessão 1 (`D02-E01` a `D02-E03` — Leitura, Lacunas e Depuração)

### `D02-E01` *(Leitura e Teste de Mesa — Reprodução do modelo)*
Considere `int v[6] = {-8, -3, -12, -3, -12, -5};` (`n = 6`), inicializado com `maior = v[0]; pos_maior = 0; menor = v[0]; pos_menor = 0;`.
Sem usar computador, preencha o rastreamento de `i = 1` até `5` e indique os valores finais para:
1. Maior usando `if (v[i] > maior)` vs. usando `if (v[i] >= maior)`;
2. Menor usando `if (v[i] < menor)` vs. usando `if (v[i] <= menor)`.

---

### `D02-E02` *(Completar solução)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` do trecho ilustrativo abaixo (com `int v[MAX]` já preenchido com `n >= 1` elementos) para calcular soma, média real e índice da **última ocorrência** do maior valor em um único percurso:

```c
int soma = /* A */;
int maior = /* B */, pos_maior = 0;

for (int i = 0; i < n; i++) {
    soma += v[i];
    if ( /* C */ ) {
        maior = v[i];
        pos_maior = i;
    }
}
double media = /* D */ ;
```

---

### `D02-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler `n` (`1 <= n <= 100`) inteiros e calcular, **em um único percurso após a leitura**, a média real (2 casas), o maior valor (1ª ocorrência) e o menor valor (1ª ocorrência), imprimindo `Media: %.2f\nMaior: %d\nMenor: %d\n`. Identifique os **3 bugs intencionais** (no papel ou em comentários `//`) e escreva a versão corrigida completa:

```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int soma = 0, maior = 0, menor = 0;
    for (int i = 0; i < n; i++) {
        soma += v[i];
        if (v[i] > maior) {
            maior = v[i];
        } else if (v[i] < menor) {
            menor = v[i];
        }
    }

    double media = soma / n;
    printf("Media: %.2f\nMaior: %d\nMenor: %d\n", media, maior, menor);
    return 0;
}
```

---

### Sessão 2 (`D02-E04` a `D02-E06` — Escrita Guiada → Independente)

### `D02-E04` *(Variação controlada com pistas)*
Escreva um **programa completo** em C que leia `n` (`1 <= n <= 100`) e depois `n` inteiros para um vetor `v[MAX]`. Calcule e imprima:
```text
Soma: X
Media: Y.YY
Acima da media: Z
```
onde `Acima da media` é a quantidade de elementos **estritamente maiores (`>`)** que a média real calculada.  
*Pista:* Como o valor da média só fica pronto após somar todos os elementos, faça a contagem `v[i] > media` em um segundo `for` após calcular `media = (double)soma / n;`.

---

### `D02-E05` *(Variação controlada com pistas)*
Escreva um **programa completo** em C que leia `n` (`1 <= n <= 100`) e `n` inteiros em `v[MAX]`. Encontre o **menor valor** armazenado e o índice da **última ocorrência** desse menor valor (base 0). Imprima exatamente:
```text
Menor: X
Indice: Y
```
*Pista:* Inicialize `menor = v[0]` e `pos_menor = 0`, e pense se o teste no laço deve ser `<` ou `<=`.

---

### `D02-E06` *(Resolução independente)*
Escreva um **programa completo** em C que leia `n` (`1 <= n <= 100`) e `n` inteiros para um vetor `v[MAX]`. **Em apenas um percurso pelo vetor após a leitura**, determine:
1. O **maior valor** e o índice da sua **primeira ocorrência**;
2. O **menor valor** e o índice da sua **última ocorrência**.

Imprima exatamente neste formato:
```text
Maior: X (indice P1)
Menor: Y (indice P2)
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `D02-C01` *(Teste de Mesa)*
Dado `int v[6] = {-4, -4, -9, -1, -9, -1};` (`n = 6`), inicializado com `maior = v[0]; pos_maior = 0; menor = v[0]; pos_menor = 0;`, faça o teste de mesa do laço `for (int i = 1; i < 6; i++)` usando `if (v[i] > maior)` e `if (v[i] <= menor)`. Informe os valores finais de `maior`, `pos_maior`, `menor` e `pos_menor`.

### `D02-C02` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler `n` (`1 <= n <= 100`) e `n` inteiros, contar quantos são **estritamente positivos (`> 0`)** e achar o **menor valor** com o índice da sua **primeira ocorrência**, imprimindo `Positivos: X\nMenor: Y (indice Z)\n`. Corrija todos os defeitos presentes:

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
    int menor = 999, pos_menor = 1;
    for (int i = 1; i < n; i++) {
        if (v[i] > 0) {
            positivos++;
        }
        if (v[i] <= menor) {
            menor = v[i];
            pos_menor = i;
        }
    }

    printf("Positivos: %d\nMenor: %d (indice %d)\n", positivos, menor, pos_menor);
    return 0;
}
```

### `D02-C03` *(Programa completo independente)*
Escreva um programa completo em C que leia `n` (`1 <= n <= 100`) e `n` inteiros em `v[MAX]`. **Em apenas um percurso após a leitura**, calcule e imprima exatamente:
```text
Soma: S
Media: M.MM
Negativos: Q
Maior: X (indice P1)
Menor: Y (indice P2)
```
onde `Negativos` conta elementos `< 0`, `Maior` registra o índice da **1ª ocorrência** e `Menor` registra o índice da **última ocorrência**.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `D03` (`Busca Linear, Inversão In-Place e Particionamento`):** somente após autocorreção de `D02-E01..E06` e **100% (3/3)** em `D02-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** refazer teste de mesa com vetor só de negativos e empates nas extremidades `0` e `n - 1`; aplicar variante `V2` de `D02`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`D01`** (indexação base 0 e limites `0..n-1`), **`B04`** (dois `if`s independentes vs. `else if`) e **`B02`** (cast `(double)`).

---

## 6. Referências do Orientador
- `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 3 (09/10).
- `[DOC]` `Aula_11_Algoritmos.pdf` p. 26 (soma de vetor); `Aula_12_Algoritmos.pdf` p. 4–13, 25 (maior/menor, negativos, 1 percurso, desempates).
- `[DOC]` `Lista6_Algoritmos.pdf` p. 1 (Ex. 1 — maior 1ª ocorr. / menor última ocorr. em 1 percurso); `Lista8_Algoritmos_Revisao.pdf` p. 3 (Ex. 6).
- Casos de teste e soluções verificáveis: [D02_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/gabaritos/D02_gabarito.md) e [D02_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/D02_testes.md).
