# Bloco `D08` — Biblioteca `<string.h>` e Algoritmos Clássicos de Strings (Inversão e Palíndromo *In-Place*)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio D — Vetores Unidimensionais e Strings / **`D08`** |
| **Micro-habilidade foco** | Empregar funções de `<string.h>` (`strlen`, `strcpy`, `strcat`, `strcmp`) compreendendo por que `=` e `==` falham em strings, e implementar inversão e verificação de palíndromo *in-place*. |
| **Pré-requisitos** | `D03` *(Inversão in-place até `N / 2`)*, `D07` *(Percurso manual até `'\0'` e caixa ASCII/`<ctype.h>`)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão única de prática + checagem (24 min):** `14 min` resol. \| `6 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Não utilize** matrizes 2D, funções próprias além de `int main(void)` ou VLAs. Use `#define MAX ...`, `<string.h>` (`strlen`, `strcpy`, `strcat`, `strcmp`), `<ctype.h>`, índices convergentes, nunca use `gets`, e mantenha saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **`strlen(s)`:** Devolve o número de caracteres antes do primeiro `'\0'` (**não conta** o `'\0'`). Guarde em `int len = (int)strlen(s);` antes de laços — chamar `strlen(s)` dentro da condição do `for` torna o percurso quadrático $O(n^2)$.
2. **Por que `=` e `==` falham em strings:**
   - **Nunca faça `dest = orig;`:** em C, vetores não podem receber atribuição direta (erro de compilação). Use `strcpy(dest, orig);`.
   - **Nunca faça `a == b`:** compara os **endereços de memória** dos dois vetores (quase sempre falso, mesmo com conteúdo igual!). Use `strcmp(a, b) == 0`.
3. **`strcpy(dest, orig)` e `strcat(dest, orig)`:**
   - `strcpy` copia `orig` (incluindo `'\0'`) para `dest`, sobrescrevendo o conteúdo anterior.
   - `strcat` anexa `orig` ao final da string já existente em `dest` (substituindo o `'\0'` de `dest` e gravando novo `'\0'` ao fim). **Garanta** que `dest` já esteja inicializado como string válida e possua capacidade `>= strlen(dest) + strlen(orig) + 1`.
4. **`strcmp(a, b)` (Comparação Lexicográfica / ASCII):**
   - Retorna **`0`** se `a` e `b` são idênticas.
   - Retorna **`< 0`** se `a` vem antes de `b` na tabela ASCII (lembre-se: `'Z'` (`90`) < `'a'` (`97`)!).
   - Retorna **`> 0`** se `a` vem depois de `b`.
5. **Inversão manual e Palíndromo *in-place*:**
   - **Para nova string `inv`:** `for (int i = 0; i < len; i++) inv[i] = s[len - 1 - i]; inv[len] = '\0';`.
   - **Palíndromo *in-place* (sem segundo vetor):** use dois índices convergentes `i = 0` e `j = len - 1` (`while (i < j)`), comparando `tolower((unsigned char)s[i]) != tolower((unsigned char)s[j])` e avançando `i++`, `j--`.

---

## 2. Exemplos Guiados

### Exemplo 1 — `strcmp` e rastreamento *in-place* de `"Arara"` *(Rastreamento)*
- `strcmp("Ana", "ana")`: compara `'A'` (`65`) com `'a'` (`97`). Como `65 < 97`, retorna valor **negativo** (`< 0`).
- Palíndromo *in-place* em `"Arara"` (`len = 5`):
  - `i = 0, j = 4`: `tolower('A') == tolower('a')` (`'a' == 'a'`) → avança `i = 1, j = 3`
  - `i = 1, j = 3`: `'r' == 'r'` → avança `i = 2, j = 2`
  - `i < j` (`2 < 2`) é falso → encerra com **`eh_pal = 1`**.

### Exemplo 2 — Ordenação lexicográfica, concatenação e palíndromo *(Programa completo)*
```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define MAX 41

int main(void) {
    char s1[MAX], s2[MAX], aux[MAX];

    scanf("%40s %40s", s1, s2);

    if (strcmp(s1, s2) > 0) {
        strcpy(aux, s1);
        strcpy(s1, s2);
        strcpy(s2, aux);
    }

    int len = (int)strlen(s1);
    int i = 0, j = len - 1, eh_pal = 1;
    while (i < j) {
        if (tolower((unsigned char)s1[i]) != tolower((unsigned char)s1[j])) {
            eh_pal = 0;
            break;
        }
        i++;
        j--;
    }

    printf("Ordem: %s <= %s\nPalindromo menor: %s\n",
           s1, s2, eh_pal ? "Sim" : "Nao");
    return 0;
}
```

---

## 3. Exercícios (`D08-E01` a `D08-E05`)

### Sessão Única (`D08-E01` a `D08-E05`)

### `D08-E01` *(Leitura e Teste de Mesa — `strcmp` e Dois Índices)*
Sem usar computador:
1. Indique o sinal do retorno (`< 0`, `== 0` ou `> 0`) para cada chamada:
   - `strcmp("Bola", "bola")`
   - `strcmp("casa", "casaco")`
   - `strcmp("abc", "abc")`
2. Rastreie passo a passo os índices `i`, `j` e `eh_pal` no verificador de palíndromo *in-place* (case-insensitive) para `"Radar"` e `"cama"`.

---

### `D08-E02` *(Completar solução — Última ocorrência de `'.'` / Extensão)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` do trecho abaixo que recebe `char arq[81]` (já lida sem `'\n'`) e extrai em `char ext[21]` a extensão após o **último** ponto `'.'` (ou `"Sem extensao"` se não houver ponto):

```c
int len = (int) /* A */ (arq);
int pos = -1;
for (int i = len - 1; i >= 0; i--) {
    if (arq[i] == /* B */) {
        pos = i;
        break;
    }
}
if (pos == /* C */) {
    strcpy(ext, "Sem extensao");
} else {
    /* D */ (ext, &arq[pos + 1]);
}
```

---

### `D08-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler duas palavras `a` e `b` (até `30` chars cada), informar se são idênticas (`Iguais: Sim` / `Nao`), montar `res` no formato `"a-b"` e construir a versão invertida `inv`, imprimindo `Uniao: <res>\nInvertida: <inv>\n`. Identifique os **3 bugs intencionais** e escreva a versão corrigida completa:

```c
#include <stdio.h>
#include <string.h>
#define MAX 31
#define MAX_RES 65

int main(void) {
    char a[MAX], b[MAX];
    char res[MAX_RES], inv[MAX_RES];

    scanf("%30s %30s", a, b);

    if (a == b) {
        printf("Iguais: Sim\n");
    } else {
        printf("Iguais: Nao\n");
    }

    strcat(res, a);
    strcat(res, "-");
    strcat(res, b);

    int len = (int)strlen(res);
    for (int i = 0; i < len; i++) {
        inv[i] = res[len - 1 - i];
    }

    printf("Uniao: %s\nInvertida: %s\n", res, inv);
    return 0;
}
```

---

### `D08-E04` *(Variação controlada com pistas)*
Escreva um **programa completo** em C que leia uma linha (`MAX 81`) com `fgets`, remova eventual `'\n'` usando `strlen`, construa manualmente sua versão invertida em `char inv[MAX]` (sem usar função não-padrão como `strrev`), e imprima exatamente:
```text
Original: <orig>
Invertida: <inv>
Identicas: Sim   (ou Nao, comparando via strcmp)
```
*Pista:* Percorra `i` de `0` até `len - 1` gravando `orig[len - 1 - i]` em `inv[i]`, e coloque `inv[len] = '\0';`.

---

### `D08-E05` *(Resolução independente)*
Escreva um **programa completo** em C que leia uma frase (`MAX 101`) com `fgets`, remova eventual `'\n'`, e verifique **in-place** (sem criar segunda string) se a frase é um palíndromo **ignorando espaços `' '` e diferenças entre maiúsculas e minúsculas** (ex.: `"A base do teto desaba"` é palíndromo). Imprima exatamente:
```text
Palindromo
```
ou
```text
Nao palindromo
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `D08-C01` *(Teste de Mesa e Análise)*
Sem usar computador:
1. Dado `char x[10] = "teste"; char y[10] = "teste";`, o que a expressão `x == y` resulta (`1` ou `0`)? Por quê?
2. Qual o sinal retornado por `strcmp("Zebra", "abacaxi")`? Justifique com base na tabela ASCII.
3. Rastreie `i` e `j` no algoritmo de palíndromo *in-place* para `"Omo"` e `"abca"`.

---

### `D08-C02` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler duas palavras (`MAX 41`), ordená-las lexicograficamente (`s1 <= s2`) e verificar se a menor delas (`s1`) é um palíndromo *in-place* (ignorando maiúsculas/minúsculas). Corrija todos os **3 defeitos** presentes:

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define MAX 41

int main(void) {
    char s1[MAX], s2[MAX], aux[MAX];

    scanf("%40s %40s", s1, s2);

    if (s1 > s2) {
        aux = s1;
        s1 = s2;
        s2 = aux;
    }

    int len = (int)strlen(s1);
    int i = 0, j = len - 1, eh_pal = 1;
    while (i < j) {
        if (s1[i] != s1[j]) {
            eh_pal = 0;
            break;
        }
        i++;
        j--;
    }

    printf("Ordem: %s <= %s\nPalindromo menor: %s\n",
           s1, s2, eh_pal ? "Sim" : "Nao");
    return 0;
}
```

---

### `D08-C03` *(Programa completo independente)*
Escreva um programa completo em C que leia `n` (`1 <= n <= 20`) e depois `n` palavras (cada uma com até `30` caracteres úteis, lidas com `%30s`). Determine e imprima exatamente:
```text
Menor: <menor lexicograficamente via strcmp>
Maior: <maior lexicograficamente via strcmp>
Palindromos: <quantidade de palavras que sao palindromos case-insensitive>
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `D09` (`Linearização de Grades 2D em Vetor 1D`):** somente após autocorreção de `D08-E01..E05` e **100% (3/3)** em `D08-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** revisar a diferença entre `=`/`strcpy` e `==`/`strcmp`, o sinal de `strcmp` com maiúsculas vs. minúsculas e o rastreamento de dois índices convergentes `i < j`; aplicar variante `V2` de `D08`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`D03`** (inversão com dois índices até `n / 2`) e **`D07`** (percurso manual até `'\0'` e `<ctype.h>`).

---

## 6. Referências do Orientador
- `[DOC]` `Aula_13_Algoritmos.pdf` p. 20–23, 25 (`<string.h>`: `strlen`, `strcpy`, `strcat`, `strcmp`, inversão e palíndromo).
- `[DOC]` `Lista7_Algoritmos.pdf` p. 1–2 (Ex. 1, 4 — extensão de arquivo, inversão e palíndromo).
- `[DOC]` `Lista8_Algoritmos_Revisao.pdf` p. 3 (Ex. 8).
- Casos de teste e soluções verificáveis: [D08_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/gabaritos/D08_gabarito.md) e [D08_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/D08_testes.md).
