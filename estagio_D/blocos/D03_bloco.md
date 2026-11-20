# Bloco `D03` — Busca Linear, Inversão *In-Place* e Particionamento em Múltiplos Vetores

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio D — Vetores Unidimensionais e Strings / **`D03`** |
| **Micro-habilidade foco** | Executar busca linear (com `-1` e `break`), inverter um vetor *in-place* até `N / 2` e construir múltiplos vetores filtrados com índices de escrita independentes. |
| **Pré-requisitos** | `D02` *(Acumulação, Contagem Condicional e Busca de Extremos com Índices em Vetores)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 20 min):** `12 min` resol. \| `5 min` corr. \| `3 min` recup.; **Sessão 2 (`E04`–`E06`, 22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Não utilize** funções próprias além de `main`, strings (`char[]`/`<string.h>`), matrizes 2D ou VLAs (vetores de tamanho variável). Use `#define MAX 100` e vetores de capacidade fixa `int v[MAX];` lendo `n` (`1 <= n <= MAX`). |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Busca linear (sentinela `-1` e `break`):**
   - Para localizar a **1ª ocorrência** de `x`, inicialize `int pos = -1;` (nunca `0`, pois `0` é um índice válido!). Ao encontrar `v[i] == x`, faça `pos = i; break;`.
   - Para a **última ocorrência**, remova o `break` (ou percorra de `n - 1` até `0` com `break`).
   - Para **listar todas as ocorrências** ou contar repetições, percorra todo o vetor sem `break`.
2. **Inversão *in-place* até `n / 2`:**
   - Para inverter o próprio vetor `v` na memória sem criar outro vetor, troque `v[i]` com `v[n - 1 - i]` usando uma variável auxiliar `aux`, com o laço indo somente até **`i < n / 2`**.
   - **Erro clássico:** usar `i < n` troca cada par duas vezes, devolvendo o vetor à ordem original! Quando `n` é ímpar, a divisão inteira `n / 2` deixa o elemento central intacto, como esperado.
3. **Particionamento em múltiplos vetores (contadores independentes):**
   - Ao separar elementos de `v` em dois vetores (ex.: `pares` e `impares`), mantenha um **índice de escrita próprio** para cada destino (`int k_par = 0, k_imp = 0;`) e incremente somente o contador do vetor que recebeu o elemento (`pares[k_par++] = v[i];`).
   - **Nunca** escreva em `pares[i]` usando o índice `i` de `v` — isso deixa lixo de memória nas posições puladas! Sempre trate o caso em que algum vetor resultante termine vazio (`k == 0`).
4. **Busca pelo mais próximo (distância absoluta):**
   - Calcule a distância até `x` com `abs(v[i] - x)` (de `#include <stdlib.h>`) ou condicional (`d = v[i] - x; if (d < 0) d = -d;`).
   - Inicialize `melhor_dist` e `pos_melhor = 0` a partir de `v[0]`. Use `<` para preferir a **1ª ocorrência** em empate (ou `<=` para a última).

---

## 2. Exemplos Guiados

### Exemplo 1 — Busca linear da 1ª ocorrência e distância mínima *(Trecho ilustrativo)*
Para `int v[5] = {12, 5, 8, 5, 20};` (`n = 5`) e `x = 5`:
```c
int pos = -1;
for (int i = 0; i < n; i++) {
    if (v[i] == x) {
        pos = i;
        break;   /* interrompe na 1a ocorrencia: pos = 1 */
    }
}
```
Se buscarmos o elemento mais próximo de `alvo = 10`:
```c
int melhor_dist = v[0] - alvo;
if (melhor_dist < 0) melhor_dist = -melhor_dist;
int pos_melhor = 0;

for (int i = 1; i < n; i++) {
    int d = v[i] - alvo;
    if (d < 0) d = -d;
    if (d < melhor_dist) {   /* '<' mantem menor indice em empate (12 vs 8 -> fica 12 no indice 0) */
        melhor_dist = d;
        pos_melhor = i;
    }
}
```

### Exemplo 2 — Inversão *in-place* e particionamento em dois vetores *(Programa completo)*
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    for (int i = 0; i < n / 2; i++) {
        int aux = v[i];
        v[i] = v[n - 1 - i];
        v[n - 1 - i] = aux;
    }

    int neg[MAX], nao_neg[MAX];
    int k_neg = 0, k_nneg = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] < 0) {
            neg[k_neg++] = v[i];
        } else {
            nao_neg[k_nneg++] = v[i];
        }
    }

    printf("Negativos (%d):", k_neg);
    for (int i = 0; i < k_neg; i++) {
        printf(" %d", neg[i]);
    }
    printf("\nNao negativos (%d):", k_nneg);
    for (int i = 0; i < k_nneg; i++) {
        printf(" %d", nao_neg[i]);
    }
    printf("\n");
    return 0;
}
```

---

## 3. Exercícios (`D03-E01` a `D03-E06`)

### Sessão 1 (`D03-E01` a `D03-E03` — Leitura, Lacunas e Depuração)

### `D03-E01` *(Teste de Mesa — Inversão `n / 2` vs `n`)*
Sem usar computador, rastreie a troca `aux = v[i]; v[i] = v[n - 1 - i]; v[n - 1 - i] = aux;`:
1. Para `int v[5] = {10, 20, 30, 40, 50};` (`n = 5`):
   - **(a)** Estado final de `v` quando o laço usa `i < n / 2` (`i = 0, 1`);
   - **(b)** Estado passo a passo de `v` (`i = 0, 1, 2, 3, 4`) quando o laço usa erroneamente `i < n`.
2. Para `int u[4] = {1, 2, 3, 4};` (`n = 4`): estado final com `i < n / 2` (`i = 0, 1`).

---

### `D03-E02` *(Completar solução)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` para particionar um vetor `v[MAX]` (com `n` inteiros e `media` já calculada) em dois vetores `menores[MAX]` (`< media`) e `maiores_ig[MAX]` (`>= media`), sem deixar lixo em posições puladas:

```c
int menores[MAX], maiores_ig[MAX];
int k1 = /* A */, k2 = 0;

for (int i = 0; i < n; i++) {
    if (v[i] < media) {
        menores[ /* B */ ] = v[i];
    } else {
        maiores_ig[ /* C */ ] = v[i];
    }
}

printf("Menores (%d):", k1);
for (int i = 0; i < /* D */ ; i++) {
    printf(" %d", menores[i]);
}
```

---

### `D03-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler `n` (`1 <= n <= 100`), `n` inteiros em `v[MAX]` e uma chave `x`, buscar o índice da **1ª ocorrência** de `x` (ou `-1` se não existir), depois **inverter `v` *in-place*** e imprimir `Indice: P\nInvertido: ...\n`. Identifique os **3 bugs intencionais** e escreva a versão corrigida completa:

```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, x, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &x);

    int pos = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] == x) {
            pos = i;
        }
    }

    for (int i = 0; i < n; i++) {
        int aux = v[i];
        v[i] = v[n - 1 - i];
        v[n - 1 - i] = aux;
    }

    printf("Indice: %d\nInvertido:", pos);
    for (int i = 0; i < n; i++) {
        printf(" %d", v[i]);
    }
    printf("\n");
    return 0;
}
```

---

### Sessão 2 (`D03-E04` a `D03-E06` — Escrita Guiada → Independente)

### `D03-E04` *(Variação controlada com pistas)*
Escreva um **programa completo** em C que leia `n` (`1 <= n <= 100`), `n` inteiros em `v[MAX]` e um inteiro `x`. Encontre o elemento de `v` **mais próximo de `x`** (menor distância absoluta `|v[i] - x|`; em caso de empate, escolha a **1ª ocorrência**, isto é, o menor índice). Imprima exatamente:
```text
Mais proximo: V (indice P, distancia D)
```
*Pista:* Inclua `<stdlib.h>` para usar `abs(v[i] - x)` (ou calcule com condicional), inicialize `melhor_dist` com a distância de `v[0]` e `pos_melhor = 0`, e compare com `<` estrito.

---

### `D03-E05` *(Variação controlada com pistas)*
Escreva um **programa completo** em C *(estilo Prova UFPR 2017)* que leia `n` (`1 <= n <= 100`) e `n` inteiros em `v[MAX]`. Particione os elementos preservando a ordem relativa em dois vetores: `pares[MAX]` e `impares[MAX]`. Imprima exatamente:
```text
Pares (K1): ...
Impares (K2): ...
```
Se algum dos vetores resultar vazio (`K1 == 0` ou `K2 == 0`), imprima ` nenhum` após os dois-pontos (ex.: `Pares (0): nenhum`).  
*Pista:* Para incluir ímpares negativos corretamente, teste `v[i] % 2 == 0` para par e `else` para ímpar (nunca use `v[i] % 2 == 1`).

---

### `D03-E06` *(Resolução independente)*
Escreva um **programa completo** em C que leia `n` (`1 <= n <= 100`) e `n` inteiros para `v[MAX]`. Faça em sequência:
1. Inverta `v` *in-place*;
2. Calcule a média real (`double`) dos elementos;
3. Particione o vetor **já invertido** em `abaixo[MAX]` (`v[i] < media`) e `acima_ig[MAX]` (`v[i] >= media`).

Imprima exatamente neste formato (imprimindo ` nenhum` após os dois-pontos se algum vetor particionado ficar vazio):
```text
Invertido: ...
Media: M.MM
Abaixo (K1): ...
Acima ou igual (K2): ...
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `D03-C01` *(Teste de Mesa)*
Dado `int v[4] = {9, 7, 5, 3};` (`n = 4`), rastreie a execução do laço **incorreto** abaixo passo a passo (`i = 0, 1, 2, 3`), registrando o vetor `v` ao final de cada iteração, e explique por que o limite correto deve ser `i < n / 2`:
```c
for (int i = 0; i < 4; i++) {
    int aux = v[i];
    v[i] = v[3 - i];
    v[3 - i] = aux;
}
```

### `D03-C02` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler `n` (`1 <= n <= 100`), `n` inteiros em `v[MAX]` e um inteiro `alvo`, listar **todos** os índices onde `v[i] == alvo` (ou ` nenhuma` se não ocorrer) e informar o elemento **mais próximo** de `alvo` (em empate, a **1ª ocorrência**). Corrija todos os defeitos presentes:

```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, alvo, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &alvo);

    int qtd = 0;
    printf("Ocorrencias:");
    for (int i = 0; i < n; i++) {
        if (v[i] == alvo) {
            printf(" %d", i);
            qtd++;
            break;
        }
    }
    if (qtd == 0) {
        printf(" nenhuma");
    }
    printf("\n");

    int melhor_dist = v[0] - alvo;
    int pos_melhor = 0;
    for (int i = 1; i < n; i++) {
        int d = v[i] - alvo;
        if (d <= melhor_dist) {
            melhor_dist = d;
            pos_melhor = i;
        }
    }

    printf("Mais proximo: %d (indice %d)\n", v[pos_melhor], pos_melhor);
    return 0;
}
```

### `D03-C03` *(Programa completo independente)*
Escreva um programa completo em C que leia `n` (`1 <= n <= 100`), `n` inteiros em `v[MAX]` e um limiar inteiro `L`. Particione `v` em `menores[MAX]` (`v[i] < L`) e `maiores_ig[MAX]` (`v[i] >= L`). Em seguida, inverta *in-place* apenas o vetor `menores` e imprima exatamente (usando ` nenhum` se o vetor correspondente tiver 0 elementos):
```text
Menores invertidos (K1): ...
Maiores ou iguais (K2): ...
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `D04` (`Vetores de Frequência e Deduplicação`):** somente após autocorreção de `D03-E01..E06` e **100% (3/3)** em `D03-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** refazer teste de mesa de inversão com `n` par e `n` ímpar (`i < n / 2`), verificar contadores independentes em particionamento com caso vazio (`0` elementos) e aplicar variante `V2` de `D03`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`A07`** (troca com `aux`), **`C07`** (`break` em laços), **`D01`** (limites `0..n-1`) e **`D02`** (desempate `<` vs `<=` e média real).

---

## 6. Referências do Orientador
- `[DOC]` `Aula_12_Algoritmos.pdf` p. 14–20, 26 (busca linear, inversão *in-place* até `N / 2`, particionamento em vetores separados).
- `[DOC]` `Lista6_Algoritmos.pdf` p. 1–2 (Ex. 2 — **Prova UFPR 2017** — e Ex. 4).
- Casos de teste e soluções verificáveis: [D03_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/gabaritos/D03_gabarito.md) e [D03_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/D03_testes.md).
