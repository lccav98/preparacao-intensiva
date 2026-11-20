# Bloco `D05` — Laços Aninhados em Vetores 1D: Subsequência com Sobreposição e Convolução Discreta

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio D — Vetores Unidimensionais e Strings / **`D05`** |
| **Micro-habilidade foco** | Implementar casamento de padrão consecutivo com sobreposição e convolução discreta 1D sobre múltiplos vetores usando indexação deslocada e reversa (`v[i + k]`, `h[m - 1 - k]`) com limites seguros (`i <= n - m`). |
| **Pré-requisitos** | `D03` *(Busca Linear, Inversão In-Place e Particionamento)* e `D04` *(Vetores de Frequência e Deduplicação)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Sessão 2 (`E04`–`E06`, 23 min):** `14 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Não utilize** funções próprias além de `main`, strings (`char[]`/`<string.h>`), matrizes 2D ou VLAs (vetores de tamanho variável). Use `#define MAX 100` e vetores de capacidade fixa. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Limite seguro da janela deslizante (`0 <= i <= n - m`):**
   - Ao alinhar um subvetor ou kernel de tamanho `m` a partir da posição `i` de um vetor `v` de tamanho `n`, o laço interno `k` (`0 .. m - 1`) acessa `v[i + k]`.
   - O maior índice acessado é `i + (m - 1)`. Para garantir `i + m - 1 < n`, o laço externo deve ir até **`i <= n - m`** (inclusivo!). Se `m > n`, `n - m < 0` e o laço executa `0` vezes com segurança.
2. **Casamento de subvetor com sobreposição *(Prova UFPR 2017)*:**
   - Para cada início `i` (`0 <= i <= n - m`), inicialize `int casou = 1;` **dentro** do laço externo `i` e teste no laço interno `if (v[i + k] != p[k]) { casou = 0; break; }`.
   - Para preservar **sobreposições** (ex.: `{1, 2, 1}` ocorre nos índices `0` e `2` de `{1, 2, 1, 2, 1}`), avance o laço externo sempre de **`1` em `1` (`i++`)** — nunca pule `i += m`!
3. **Convolução discreta 1D (modo válido) e kernel assimétrico:**
   - Dado o sinal `v` (tamanho `n`) e o kernel `h` (tamanho `m <= n`), o resultado `r` tem tamanho **`n - m + 1`**, com:
     `r[i] = soma_{k=0..m-1} (v[i + k] * h[m - 1 - k])`
   - **Atenção crítica ao kernel assimétrico:** na convolução, o kernel é percorrido de trás para frente (`h[m - 1 - k]`), diferente de `h[k]` (correlação). Se testar apenas com kernel simétrico (como `{1, 2, 1}`), esse erro passa despercebido! Sempre valide com um kernel assimétrico (ex.: `{1, 2, 3}`) e lembre-se de zerar `soma = 0;` a cada `i`.

---

## 2. Exemplos Guiados

### Exemplo 1 — Casamento de padrão com sobreposição *(Trecho ilustrativo)*
Para `int v[5] = {1, 2, 1, 2, 1};` (`n = 5`) e `int p[3] = {1, 2, 1};` (`m = 3`):
```c
int ocorrencias = 0;
for (int i = 0; i <= n - m; i++) {   /* i = 0, 1, 2 */
    int casou = 1;
    for (int k = 0; k < m; k++) {
        if (v[i + k] != p[k]) {
            casou = 0;
            break;
        }
    }
    if (casou) {
        ocorrencias++;
    }
}
/* Casa em i = 0 (v[0..2]) e em i = 2 (v[2..4]): ocorrencias = 2 */
```

### Exemplo 2 — Convolução discreta 1D com kernel assimétrico *(Programa completo)*
```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, m, v[MAX], h[MAX], r[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &m);
    for (int k = 0; k < m; k++) {
        scanf("%d", &h[k]);
    }

    int tam_r = n - m + 1;
    for (int i = 0; i <= n - m; i++) {
        int soma = 0;
        for (int k = 0; k < m; k++) {
            soma += v[i + k] * h[m - 1 - k];
        }
        r[i] = soma;
    }

    printf("Convolucao (%d):", tam_r);
    for (int i = 0; i < tam_r; i++) {
        printf(" %d", r[i]);
    }
    printf("\n");
    return 0;
}
```
*Traço com `v = {2, 4, 1, 3}` (`n = 4`) e `h = {1, 2, 3}` (`m = 3`):*  
`r[0] = 2*3 + 4*2 + 1*1 = 15`; `r[1] = 4*3 + 1*2 + 3*1 = 17`.

---

## 3. Exercícios (`D05-E01` a `D05-E06`)

### Sessão 1 (`D05-E01` a `D05-E03` — Leitura, Lacunas e Depuração)

### `D05-E01` *(Teste de Mesa — Sobreposição e Kernel Assimétrico)*
Sem usar computador, resolva:
1. Para `int v[6] = {2, 2, 2, 1, 2, 2};` (`n = 6`) e `int p[2] = {2, 2};` (`m = 2`), rastreie cada janela `i = 0 .. 4`, indicando em quais índices ocorre casamento (com sobreposição) e o total de ocorrências.
2. Para `int v[4] = {4, 1, 3, 2};` (`n = 4`) e o kernel assimétrico `int h[3] = {1, 2, 5};` (`m = 3`), calcule `r[0]` e `r[1]` usando a fórmula da convolução `sum(v[i + k] * h[m - 1 - k])` e mostre quais valores errados surgiriam se alguém escrevesse `h[k]` no lugar de `h[m - 1 - k]`.

---

### `D05-E02` *(Completar solução)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` do trecho abaixo (com `v[MAX]` de tamanho `n` e `p[MAX]` de tamanho `m`, onde `1 <= m <= n`) para contar todas as ocorrências de `p` em `v` **permitindo sobreposição**:

```c
int ocorrencias = 0;
for (int i = 0; /* A */ ; i++) {
    int casou = /* B */;
    for (int k = 0; k < m; k++) {
        if ( /* C */ != p[k]) {
            casou = 0;
            break;
        }
    }
    if (casou) {
        /* D */;
    }
}
```

---

### `D05-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler `n`, `v[MAX]`, `m` e `h[MAX]` (`1 <= m <= n <= 100`), calcular a convolução discreta 1D e imprimir `Convolucao: r0 r1 ...`. Identifique os **3 bugs intencionais** e escreva a versão corrigida completa:

```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, m, v[MAX], h[MAX], r[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &m);
    for (int k = 0; k < m; k++) {
        scanf("%d", &h[k]);
    }

    int soma = 0;
    for (int i = 0; i < n; i++) {
        for (int k = 0; k < m; k++) {
            soma += v[i + k] * h[k];
        }
        r[i] = soma;
    }

    printf("Convolucao:");
    for (int i = 0; i < n - m + 1; i++) {
        printf(" %d", r[i]);
    }
    printf("\n");
    return 0;
}
```

---

### Sessão 2 (`D05-E04` a `D05-E06` — Escrita Guiada → Independente)

### `D05-E04` *(Variação controlada com pistas)*
Escreva um **programa completo** em C *(inspirado na Prova UFPR 2017 / Lista 6 Ex. 5)* que leia `n` (`1 <= n <= 100`), `n` inteiros em `v[MAX]`, depois `m` (`1 <= m <= n`) e `m` inteiros em `p[MAX]`. Encontre **todas as posições iniciais** em que `p` aparece como subvetor consecutivo de `v` (com sobreposição). Imprima exatamente:
```text
Ocorrencias: Q
Indices: i0 i1 ...
```
*(Se `Q == 0`, imprima `Indices: nenhum`).*  
*Pista:* Guarde os índices encontrados em um vetor `pos[MAX]` usando um contador independente `qtd = 0`.

---

### `D05-E05` *(Variação controlada com pistas)*
Escreva um **programa completo** em C que leia `n` (`1 <= n <= 100`), `v[MAX]`, `m` (`1 <= m <= n`) e o kernel `h[MAX]`. Calcule a convolução discreta 1D `r` de tamanho `tam_r = n - m + 1` e também encontre o **maior valor** obtido em `r` e o índice de sua **1ª ocorrência** em `r`. Imprima exatamente:
```text
Resultado (K): r0 r1 ...
Maior convolucao: V (indice P)
```
*Pista:* Após preencher `r[0 .. tam_r - 1]`, inicialize `maior = r[0]; pos_maior = 0;` e use comparação estrita `r[i] > maior`.

---

### `D05-E06` *(Resolução independente)*
Escreva um **programa completo** em C que leia `n` (`1 <= n <= 100`), `n` inteiros em `v[MAX]`, depois `m` (`1 <= m <= 100`, **podendo ocorrer `m > n`**) e `m` inteiros em `p[MAX]`.
1. Conte quantas vezes `p` ocorre em `v` como subvetor consecutivo com sobreposição (se `m > n`, o resultado deve ser `0` sem acesso inválido à memória).
2. Se `m <= n`, calcule e imprima a convolução discreta de `v` com `p` (`Convolucao: r0 r1 ...`); se `m > n`, imprima `Convolucao: vazia`.

Formato exato:
```text
Ocorrencias: Q
Convolucao: ...
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `D05-C01` *(Análise de Limite e Casos de Borda)*
Para um vetor `v` de tamanho `n` e um padrão `p` de tamanho `m`, considere o laço externo `for (int i = 0; i <= n - m; i++)` com acesso interno `v[i + k]` (`0 <= k < m`):
1. Qual é o maior índice acessado em `v` quando `i = n - m` e `k = m - 1`? Por que `i <= n - m` é seguro e `i < n` causa invasão de memória para `m >= 2`?
2. Quantas iterações executa o laço externo quando `m == n`?
3. Quantas iterações executa o laço externo quando `m > n`?

### `D05-C02` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler `n`, `v[MAX]`, `m` e `p[MAX]` (`1 <= m <= n <= 100`), contar quantas vezes `p` ocorre em `v` **permitindo sobreposição** e imprimir `Ocorrencias: Q`. Corrija todos os defeitos presentes:

```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n, m, v[MAX], p[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &m);
    for (int k = 0; k < m; k++) {
        scanf("%d", &p[k]);
    }

    int ocorrencias = 0;
    int casou = 1;
    for (int i = 0; i < n - m; i++) {
        for (int k = 0; k < m; k++) {
            if (v[i + k] != p[k]) {
                casou = 0;
                break;
            }
        }
        if (casou) {
            ocorrencias++;
            i += m - 1;
        }
    }

    printf("Ocorrencias: %d\n", ocorrencias);
    return 0;
}
```

### `D05-C03` *(Programa completo independente)*
Escreva um programa completo em C que leia `n` (`1 <= n <= 100`), `n` inteiros em `v[MAX]`, depois `m` (`1 <= m <= n`) e `m` inteiros do kernel `h[MAX]`. Calcule a convolução discreta 1D `r[i] = sum(v[i + k] * h[m - 1 - k])` para `0 <= i <= n - m`, some todos os elementos de `r` e imprima exatamente:
```text
Tamanho: K
Valores: r0 r1 ...
Soma total: S
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `D06` (`Strings em C: Vetor de char, Terminador '\0' e E/S Segura`):** somente após autocorreção de `D05-E01..E06` e **100% (3/3)** em `D05-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** refazer teste de mesa com padrão sobreposto (`{1, 1}` em `{1, 1, 1}`) e kernel assimétrico (`{1, 2, 5}`); verificar os limites `i <= n - m` e a borda `m == n`; aplicar variante `V2` de `D05`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`C09`** (laços aninhados e reset do acumulador/flag), **`D03`** (busca linear com `break`) e **`D04`** (laços aninhados com prefixo e indexação segura).

---

## 6. Referências do Orientador
- `[DOC]` `Aula_11_Algoritmos.pdf` p. 32 (Ex. Fixação 2 — busca de subvetor).
- `[DOC]` `Aula_12_Algoritmos.pdf` p. 21–24 (casamento de padrão e convolução discreta).
- `[DOC]` `Lista6_Algoritmos.pdf` p. 2–3 (Ex. 5 — **Prova UFPR 2017** — e Ex. 6).
- Casos de teste e soluções verificáveis: [D05_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/gabaritos/D05_gabarito.md) e [D05_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/D05_testes.md).
