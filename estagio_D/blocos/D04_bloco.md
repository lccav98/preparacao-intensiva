# Bloco `D04` — Vetores de Frequência (Histograma) e Deduplicação Preservando Ordem

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio D — Vetores Unidimensionais e Strings / **`D04`** |
| **Micro-habilidade foco** | Usar um vetor de frequências por indexação indireta (`freq[v[i]]++`) para contagem/comparação de histogramas e filtrar duplicatas em faixa arbitrária preservando a ordem original. |
| **Pré-requisitos** | `D03` *(Busca Linear, Inversão In-Place e Particionamento em Múltiplos Vetores)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão única de prática + checagem (24 min):** `14 min` resol. \| `6 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Não utilize** funções próprias além de `main`, strings (`char[]`/`<string.h>`), matrizes 2D ou VLAs (vetores de tamanho variável). Use `#define MAX 100` e vetores de capacidade fixa. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Indexação indireta (`freq[v[i]]++`):**
   - Quando os valores pertencem a uma faixa pequena e inteira não-negativa (ex.: dígitos `0..9` ou notas `0..5`), use o próprio valor `v[i]` como índice no vetor contador: `freq[v[i]]++;`.
   - **Atenção:** o valor `v[i]` deve estar dentro dos limites do vetor `freq` (ex.: `0 <= v[i] && v[i] < 10`). Nunca use `freq[i]++` (isso contaria posições, não valores!).
2. **Inicialização obrigatória com `{0}`:**
   - Sempre declare `int freq[10] = {0};`. Sem `{0}`, `freq` começa com lixo de memória e `freq[v[i]]++` soma sobre valores arbitrários.
3. **Comparação de histogramas:**
   - Dois vetores `a` e `b` de mesmo tamanho contêm exatamente os mesmos valores com as mesmas multiplicidades (em qualquer ordem) se e somente se `fa[k] == fb[k]` para **todo** `k` da faixa.
4. **Impressão de histograma com `*`:**
   - Para cada valor `k` com `freq[k] > 0`, imprima `k:` seguido de um laço interno de `0` até `freq[k] - 1` imprimindo `'*'`.
5. **Deduplicação em faixa arbitrária (busca no prefixo `0 .. i - 1`):**
   - Quando os valores podem ser negativos ou grandes (onde não cabe `freq[]`), mantenha a ordem original testando se `v[i]` já apareceu antes (`for (int j = 0; j < i; j++)`).
   - Reinicie `int repetido = 0;` **dentro** do laço externo `i` e pare o laço interno com `j < i` (nunca `j <= i`, senão `v[i]` compara consigo mesmo!).

---

## 2. Exemplos Guiados

### Exemplo 1 — Contagem de frequência e impressão com `*` *(Trecho ilustrativo)*
Para `int v[6] = {2, 0, 2, 4, 2, 1};` (valores em `0..4`):
```c
int freq[5] = {0};
for (int i = 0; i < 6; i++) {
    freq[v[i]]++;
}
/* freq = {1, 1, 3, 0, 1} */

for (int d = 0; d < 5; d++) {
    if (freq[d] > 0) {
        printf("%d: ", d);
        for (int c = 0; c < freq[d]; c++) {
            printf("*");
        }
        printf("\n");
    }
}
/* Saida:
0: *
1: *
2: ***
4: *
*/
```

### Exemplo 2 — Deduplicação preservando ordem em faixa arbitrária *(Programa completo)*
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int unicos[MAX], k = 0;
    for (int i = 0; i < n; i++) {
        int repetido = 0;
        for (int j = 0; j < i; j++) {
            if (v[j] == v[i]) {
                repetido = 1;
                break;
            }
        }
        if (repetido == 0) {
            unicos[k++] = v[i];
        }
    }

    printf("Unicos (%d):", k);
    for (int i = 0; i < k; i++) {
        printf(" %d", unicos[i]);
    }
    printf("\n");
    return 0;
}
```

---

## 3. Exercícios (`D04-E01` a `D04-E05`)

### `D04-E01` *(Teste de Mesa — Histograma e Prefixo `0 .. i - 1`)*
Sem usar computador, responda:
1. Dado `int v[7] = {3, 0, 3, 2, 0, 3, 1};` e `int freq[4] = {0};`, escreva o conteúdo final de `freq[0]`, `freq[1]`, `freq[2]` e `freq[3]` após executar `for (int i = 0; i < 7; i++) freq[v[i]]++;`.
2. Dado `int u[5] = {-4, 10, -4, 7, 10};`, rastreie a busca no prefixo `0 .. i - 1` preenchendo para cada `i` (`0..4`) quais `j` são testados, se `repetido` fica `0` ou `1`, e qual é o vetor `unicos` final.

---

### `D04-E02` *(Completar solução)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` para verificar se dois vetores `a[MAX]` e `b[MAX]` de tamanho `n` (com valores garantidos em `0..9`) possuem exatamente o mesmo histograma:

```c
int fa[10] = /* A */;
int fb[10] = {0};

for (int i = 0; i < n; i++) {
    fa[ /* B */ ]++;
    fb[ /* C */ ]++;
}

int iguais = 1;
for (int d = 0; d < 10; d++) {
    if ( /* D */ ) {
        iguais = 0;
        break;
    }
}
```

---

### `D04-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler `n` (`1 <= n <= 100`) e `n` inteiros quaisquer em `v[MAX]`, copiar os elementos **sem repetições** para `unicos[MAX]` na ordem da 1ª ocorrência e imprimir `Unicos (K): ...`. Identifique os **3 bugs intencionais** e escreva a versão corrigida completa:

```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int unicos[MAX], k = 0;
    int repetido = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            if (v[j] == v[i]) {
                repetido = 1;
                break;
            }
        }
        if (repetido == 0) {
            unicos[i] = v[i];
            k++;
        }
    }

    printf("Unicos (%d):", k);
    for (int i = 0; i < k; i++) {
        printf(" %d", unicos[i]);
    }
    printf("\n");
    return 0;
}
```

---

### `D04-E04` *(Variação controlada com pistas)*
Escreva um **programa completo** em C que leia `n` (`1 <= n <= 100`) e `n` dígitos inteiros no intervalo `0..9` para `v[MAX]`. Usando um vetor de frequências `int freq[10] = {0};`, imprima o histograma em ordem crescente de `0` a `9`, exibindo **apenas os dígitos com frequência `> 0`**, no formato exato:
```text
D: ***
```
*(onde a quantidade de `*` corresponde a `freq[D]`).*  
*Pista:* Após contar com `freq[v[i]]++;`, faça um `for (int d = 0; d < 10; d++)` com `if (freq[d] > 0)` e um laço interno para os asteriscos.

---

### `D04-E05` *(Resolução independente)*
Escreva um **programa completo** em C que leia `n` (`1 <= n <= 100`), depois `n` inteiros (`0..9`) para o vetor `a[MAX]` e mais `n` inteiros (`0..9`) para o vetor `b[MAX]`. Usando vetores de frequência `fa[10]` e `fb[10]`:
1. Verifique se `a` e `b` possuem as mesmas frequências (`Mesmo histograma` ou `Histogramas diferentes`);
2. Encontre qual valor `0..9` possui a **maior soma de ocorrências** nos dois vetores juntos (`fa[d] + fb[d]`; em caso de empate, escolha o **menor** valor `0..9`).

Imprima exatamente:
```text
Mesmo histograma
Mais frequente: V (total T)
```
*(ou `Histogramas diferentes` na primeira linha).*

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `D04-C01` *(Teste de Mesa)*
Dado `int v[6] = {4, 1, 4, 0, 1, 4};` e `int freq[5] = {0};`, mostre os valores finais de `freq[0..4]` após o laço `for (int i = 0; i < 6; i++) { freq[v[i]]++; }` e informe qual valor ocorreu mais vezes.

### `D04-C02` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler `n` (`1 <= n <= 100`) e `n` notas inteiras de `0` a `5`, contar quantas vezes cada nota ocorreu e imprimir todas de `0` a `5` no formato `Nota K: Q`. Corrija todos os defeitos presentes:

```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int freq[6];
    for (int i = 0; i < n; i++) {
        freq[i]++;
    }

    for (int k = 0; k < 5; k++) {
        printf("Nota %d: %d\n", k, freq[k]);
    }
    return 0;
}
```

### `D04-C03` *(Programa completo independente)*
Escreva um programa completo em C que leia `n` (`1 <= n <= 100`) e `n` inteiros quaisquer (positivos, zero ou negativos) em `v[MAX]`. Deduplique mantendo a ordem da **1ª ocorrência** por busca no prefixo `0 .. i - 1` e imprima exatamente:
```text
Unicos (K): x1 x2 ...
Repetidos removidos: R
```
onde `R = n - K`.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `D05` (`Laços Aninhados em Vetores 1D: Subsequência e Convolução`):** somente após autocorreção de `D04-E01..E05` e **100% (3/3)** em `D04-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** revisar indexação indireta `freq[v[i]]++` com `{0}` e o limite `j < i` com reset de `repetido = 0` dentro do laço externo; aplicar variante `V2` de `D04`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`D01`** (inicialização `{0}` e limites), **`D03`** (busca linear e contadores independentes de escrita) e **`C09`** (laços aninhados).

---

## 6. Referências do Orientador
- `[DOC]` `Aula_11_Algoritmos.pdf` p. 31 (Ex. Fixação 1 — contagem/frequência).
- `[DOC]` `Lista6_Algoritmos.pdf` p. 2 (Ex. 3 — comparação de histogramas e deduplicação).
- `[DOC]` `Lista8_Algoritmos_Revisao.pdf` p. 3 (Ex. 7 — frequência e repetidos).
- Casos de teste e soluções verificáveis: [D04_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/gabaritos/D04_gabarito.md) e [D04_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/D04_testes.md).
