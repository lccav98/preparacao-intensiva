# Bloco `D10` — Revisão e Consolidação do Estágio D *(Bloco de Revisão)*

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio D — Vetores Unidimensionais e Strings / **`D10`** |
| **Micro-habilidade foco** | *(Revisão integrada de `D01` a `D09`)* Integrar manipulação de vetores 1D, busca/extremos, particionamento, histogramas, convolução, processamento de strings com `<string.h>` e linearização 1D sem violar limites de memória. |
| **Pré-requisitos** | `D08` *(Biblioteca `<string.h>` e algoritmos clássicos)*, `D09` *(Linearização de grades 2D em vetor 1D `i * C + j` e macro `INDICE`)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 22 min):** `14 min` resol. \| `5 min` corr. \| `3 min` recup.; **Sessão 2 (`E04`–`E06`, 22 min):** `14 min` resol. \| `5 min` corr. \| `3 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Conteúdo novo: NENHUM.** **É terminantemente proibido** o uso de matrizes 2D (`m[L][C]`), funções customizadas além de `int main(void)`, VLAs (`v[n]`), `struct`, alocação dinâmica ou a função obsoleta `gets`. Use estritamente C99 com saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Apto para Estágio E`)

---

## 1. Instruções Curtas (Matriz de Consolidação do Estágio D)

1. **Vetores 1D (`D01`–`D05`):**
   - Índices válidos sempre em `0 .. n - 1`; inicialize extremos com `v[0]` e índice `0` (`>` / `<` para 1ª ocorrência, `>=` / `<=` para última).
   - **Inversão *in-place*:** troque `v[i]` com `v[n - 1 - i]` apenas até `i < n / 2`.
   - **Particionamento e filtragem:** mantenha índice de escrita independente `k++` (nunca grave em `dest[i]` pulando casas).
   - **Histograma:** inicialize `int freq[K] = {0};` e garanta faixa válida antes de `freq[v[i]]++`.
   - **Subvetor com sobreposição & Convolução:** laço externo até `i <= n - m` (avançando `i++`), e na convolução discreta use kernel invertido `h[m - 1 - k]`.
2. **Strings (`D06`–`D08`):**
   - Regra `N + 1`, terminador `'\0'` (`0` vs `'0'` = `48`), `%Ns` sem `&`, `fgets` removendo `'\n'` e limpando `\n` pendente após `scanf`.
   - Percurso manual até `s[i] != '\0'`, máquina de estados `em_palavra` para espaços extras, `<ctype.h>` com `(unsigned char)`, e `<string.h>` (`strlen`, `strcpy`, `strcat`, `strcmp` — nunca `=` ou `==`).
3. **Linearização 1D (`D09`):**
   - Mapeamento *row-major*: `INDICE(i, j, cols) ((i) * (cols) + (j))` com parênteses protetores; conversão inversa `i = idx / cols` e `j = idx % cols`.

---

## 2. Exemplos Guiados

### Exemplo 1 — Subvetor com sobreposição e kernel assimétrico *(Revisão `D05`)*
Para `v = {1, 2, 1, 2, 1}` (`m = 5`) e padrão `p = {1, 2}` (`n = 2`), o laço `for (int i = 0; i <= m - n; i++)` testa `i = 0, 1, 2, 3`:
- `i = 0`: `{1, 2}` casa!
- `i = 1`: `{2, 1}` falha.
- `i = 2`: `{1, 2}` casa! *(preservado porque `i` avança de `1`, nunca `+= n`)*
- `i = 3`: `{2, 1}` falha.
Total: `2` ocorrências (`0` e `2`).

### Exemplo 2 — Histograma de vogais sobre string normalizada *(Revisão `D04` + `D07` + `D08`)*
```c
char c = (char)tolower((unsigned char)orig[i]);
if (c == 'a') vog[0]++;
else if (c == 'e') vog[1]++;
/* ... com int vog[5] = {0}; previamente zerado */
```

---

## 3. Exercícios (`D10-E01` a `D10-E06`)

### Sessão 1 (`D10-E01` a `D10-E03` — Rastreamento e Caça aos Bugs Integrados)

### `D10-E01` *(Teste de Mesa Integrado — Convolução Assimétrica + Macro `INDICE`)*
Sem usar computador:
1. Calcule o vetor resultante da convolução válida $r[i] = \sum_{k=0}^{2} v[i + k] \cdot h[2 - k]$ para `v = {2, 0, 1, 3, 2}` (`n = 5`) e kernel assimétrico `h = {1, 2, 4}` (`m = 3`), mostrando os produtos somados em `r[0]`, `r[1]` e `r[2]`.
2. Para uma grade `3 × 4` linearizada com `#define IND_OK(i, j) ((i) * 4 + (j))` vs. `#define IND_BUG(i, j) i * 4 + j`, compare o valor obtido em `IND_OK(1 + 1, 2)` e `IND_BUG(1 + 1, 2)`.

---

### `D10-E02` *(Caça ao Bug 1 — Histograma `0..9` e Particionamento em Vetor 1D)*
O programa completo abaixo deveria ler `n` (`1 <= n <= 100`) notas inteiras de `0` a `9`, armazenar em `aprov` as notas `>= 6`, imprimir `Aprovadas:` seguido das notas (ou ` Nenhuma`), e imprimir `Nota d: Q` para cada nota que ocorreu ao menos uma vez. Identifique os **3 bugs intencionais** e escreva a versão corrigida completa:

```c
#include <stdio.h>
#define MAX 100

int main(void) {
    int n;
    int v[MAX], aprov[MAX];
    int freq[10];

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int k = 0;
    for (int i = 0; i <= n; i++) {
        if (v[i] >= 0 && v[i] <= 9) {
            freq[v[i]]++;
        }
        if (v[i] >= 6) {
            aprov[i] = v[i];
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

### `D10-E03` *(Caça ao Bug 2 — Normalização de Espaços e `<string.h>`)*
O programa completo abaixo deveria ler uma linha (`MAX 101`), remover espaços extras (iniciais, finais e múltiplos internos) em `norm`, e imprimir `Encerrando\n` se `norm` for igual a `"SAIR"`, ou `[<norm>] (<comprimento>)\n` caso contrário. Identifique os **3 bugs intencionais** e escreva a versão corrigida completa:

```c
#include <stdio.h>
#include <string.h>
#define MAX 101

int main(void) {
    char orig[MAX], norm[MAX];

    fgets(orig, MAX, stdin);
    int len = (int)strlen(orig);
    if (len > 0 && orig[len - 1] == '\n') {
        orig[len - 1] = '0';
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

    if (norm == "SAIR") {
        printf("Encerrando\n");
    } else {
        printf("[%s] (%d)\n", norm, (int)strlen(norm));
    }
    return 0;
}
```

---

### Sessão 2 (`D10-E04` a `D10-E06` — Implementação Integrada Independente)

### `D10-E04` *(Integração 1 — Convolução Discreta 1D com Kernel Assimétrico)*
Escreva um programa completo em C99 ([D10_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D10_E04.c)) que leia `n` (`1 <= n <= 100`) e `n` inteiros para `v[MAX]`, depois `m` (`1 <= m <= n`) e `m` inteiros para o kernel `h[MAX]`. Calcule a convolução válida `r[i] = sum_{k=0}^{m-1} v[i + k] * h[m - 1 - k]` para `0 <= i <= n - m` e imprima exatamente:
```text
Convolucao: r0 r1 ...
```

---

### `D10-E05` *(Integração 2 — Normalização de Frase e Histograma de Vogais)*
Escreva um programa completo em C99 ([D10_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D10_E05.c)) que leia uma frase (`MAX 101`) com `fgets`, remova eventual `'\n'`, produza a versão normalizada sem espaços extras em `norm[MAX]` e conte em `int vog[5] = {0};` as ocorrências das vogais `'a'`, `'e'`, `'i'`, `'o'`, `'u'` (sem distinguir maiúsculas/minúsculas). Imprima exatamente:
```text
[<norm>]
a:X e:Y i:Z o:W u:K
```

---

### `D10-E06` *(Integração 3 — Linearização 1D `L × C`: Transposta Impressa e Extremos)*
Escreva um programa completo em C99 ([D10_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D10_E06.c)) **(proibidas matrizes 2D!)** que leia `L` e `C` (`1 <= L <= 15`, `1 <= C <= 15`) e `L * C` inteiros para um único vetor 1D `int v[225]` usando `#define INDICE(i, j, cols) ((i) * (cols) + (j))`. Imprima:
1. `Transposta:\n` seguida das `C` linhas de `L` elementos separadas por espaço simples (exibindo a transposição sem usar matriz 2D);
2. `Maior: X em (i1, j1)` (**1ª ocorrência** em ordem *row-major*);
3. `Menor: Y em (i2, j2)` (**última ocorrência** em ordem *row-major*).

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `D10-C01` *(Teste de Mesa Integrado)*
Sem usar computador:
1. Rastreie o vetor `int v[5] = {10, 20, 30, 40, 50};` após executar a inversão *in-place*:
   ```c
   for (int i = 0; i < 5 / 2; i++) {
       int aux = v[i];
       v[i] = v[4 - i];
       v[4 - i] = aux;
   }
   ```
2. Indique o sinal de `strcmp("Algo", "algo")` e o resultado de `((2) * 4 + (1))` vs `2 * 4 + 1` na grade `3 × 4`.

---

### `D10-C02` *(Programa Completo — Subvetor com Sobreposição)*
Escreva um programa completo em C99 ([D10_C02.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D10_C02.c)) que leia `m` (`1 <= m <= 100`) e `m` inteiros em `v[MAX]`, depois `n` (`1 <= n <= m`) e `n` inteiros do padrão `p[MAX]`. Conte todas as ocorrências consecutivas de `p` em `v` **permitindo sobreposição**, armazene os índices iniciais em `pos[MAX]` e imprima exatamente:
```text
Ocorrencias: Q
Posicoes: i0 i1 ...   (ou "Posicoes: Nenhuma" se Q == 0)
```

---

### `D10-C03` *(Programa Completo — Palíndromo In-Place + Histograma de Letras)*
Escreva um programa completo em C99 ([D10_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D10_C03.c)) que leia uma linha (`MAX 101`) com `fgets`, remova eventual `'\n'`, verifique **in-place** se é palíndromo (ignorando espaços `' '` e caixa) e conte a frequência de cada letra `'a'..'z'` (case-insensitive) em `int freq[26] = {0};`. Imprima:
```text
Palindromo: Sim   (ou Nao)
```
seguido de uma linha `<letra>: <contagem>` em ordem alfabética para cada letra com contagem `> 0`, ou `Sem letras` caso nenhuma letra apareça.

---

## 5. Orientação de Avanço ou Recuperação (Conclusão do Estágio D)

- **Avançar para o Estágio E (`E01 — Matrizes 2D: Declaração, Armazenamento Row-Major, Acesso e Leitura/Escrita em Grade`):** somente após autocorreção dos exercícios `D10-E01..E06` **e** **100% de acerto (3/3)** na Checagem Independente `D10-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada por sub-habilidade (1ª falha):**
  - Falha em limites, extremos, busca ou particionamento $\rightarrow$ revisar **`D01`**–**`D03`**.
  - Falha em histogramas, sobreposição de subvetor ou convolução $\rightarrow$ revisar **`D04`** e **`D05`**.
  - Falha em `'\0'`, `fgets`, percurso manual ou `<string.h>` $\rightarrow$ revisar **`D06`**–**`D08`**.
  - Falha em mapeamento `i * C + j` ou macro `INDICE` $\rightarrow$ revisar **`D09`**.
- **Após 2 tentativas malsucedidas:** interromper novas tentativas em `D10`, diagnosticar qual pré-requisito (`D01`–`D09`) falhou e reabilitá-lo integralmente antes de refazer a checagem de conclusão do Estágio D.

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (itens 2 e 8 — cadeias de caracteres e vetores unidimensionais).
- `[DOC]` `Aula_11` a `Aula_14` (vetores, algoritmos 1D, strings e linearização *row-major*).
- `[DOC]` `Lista6_Algoritmos.pdf`, `Lista7_Algoritmos.pdf` e `Lista8_Algoritmos_Revisao.pdf` p. 3 (Ex. 6–8).
- Casos de teste e soluções verificáveis: [D10_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/gabaritos/D10_gabarito.md) e [D10_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/D10_testes.md).
