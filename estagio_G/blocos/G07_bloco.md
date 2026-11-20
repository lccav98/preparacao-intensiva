# Bloco `G07` — Recursão em Strings com Dois Índices (`i`, `j`) e Modificação *In-Place* Sem Laços

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio G — Recursividade e Pilha de Execução / **`G07`** |
| **Micro-habilidade foco** | Implementar algoritmos recursivos sobre strings com dois índices convergentes (`i`, `j`) e modificação *in-place* (inversão e remoção de caractere) sem estruturas de repetição e sem vetores auxiliares. |
| **Pré-requisitos** | `G06` *(Recursão em strings por índice crescente `i + 1` até `'\0'`)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Sessão 2 (`E04`–`E06`, 24 min):** `14 min` resol. \| `6 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **PROIBIÇÃO DE LAÇOS EM FUNÇÕES RECURSIVAS:** nenhuma função recursiva pode conter `for`, `while` ou `do-while` (laços são permitidos apenas na `main` para leitura/limpeza de `fgets`). **É proibido** usar vetor auxiliar (segunda string), `<string.h>`, recursão múltipla (`G08`), `struct`, `malloc`/`free`, `gets(` ou VLAs. Toda modificação deve ocorrer *in-place* em `char s[]` com saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Dois índices convergentes (`i`, `j`) e o caso base `i >= j`:**
   - `i` começa em `0` (início) e `j` começa em `comprimento(s, 0) - 1` (último caractere válido antes de `'\0'`).
   - A cada chamada recursiva, `i` avança (`i + 1`) e `j` recua (`j - 1`).
   - **Regra crítica do caso base (`i >= j` vs. `i == j`):**
     - Em string de tamanho **ímpar** (`"ARARA"`, índices `0..4`), `(i, j)` passa por `(0,4) -> (1,3) -> (2,2)`, atingindo `i == j`.
     - Em string de tamanho **par** (`"ABBA"`, índices `0..3`), `(i, j)` passa de `(1,2)` direto para **`(2,1)`** (`i > j`), **sem nunca passar por `i == j`**! Em string vazia `""`, já inicia com `i = 0, j = -1` (`i > j`).
     - Portanto, o caso base **sempre** deve testar **`if (i >= j)`**! Usar `i == j` causa acesso inválido e *stack overflow* em strings pares e vazias.
2. **Remoção recursiva *in-place* sem laço e sem vetor auxiliar:**
   - **Padrão com dois índices (leitura `i`, escrita `j`) — recomendado:**
     - Caso base: quando `s[i] == '\0'`, grave **`s[j] = '\0';`** e retorne.
     - Se `s[i] != c`: copie `s[j] = s[i];` e chame `remover(s, i + 1, j + 1, c);`.
     - Se `s[i] == c`: não escreva e avance apenas a leitura: `remover(s, i + 1, j, c);`.
   - **Alternativa por deslocamento recursivo à esquerda (sem laço):** ao encontrar `s[i] == c`, uma função auxiliar recursiva desloca `s[k] = s[k + 1]` até `'\0'`, e a função principal **reavalia o mesmo índice `i`** (`remover(s, i, c)`), para não pular ocorrências adjacentes como `"AAA"` → `'A'`.

---

## 2. Exemplos Guiados

### Exemplo 1 — Palíndromo e inversão *in-place* com `i >= j` *(Trecho ilustrativo)*
```c
int eh_palindromo(const char s[], int i, int j) {
    if (i >= j) {
        return 1;
    }
    if (s[i] != s[j]) {
        return 0;
    }
    return eh_palindromo(s, i + 1, j - 1);
}

void inverter(char s[], int i, int j) {
    if (i >= j) {
        return;
    }
    char aux = s[i];
    s[i] = s[j];
    s[j] = aux;
    inverter(s, i + 1, j - 1);
}
```
Rastreamento de `inverter("ABBA", 0, 3)` / `eh_palindromo("ABBA", 0, 3)`:
- `(i=0, j=3)`: `'A' == 'A'` → chama `(1, 2)`
- `(i=1, j=2)`: `'B' == 'B'` → chama `(2, 1)`
- `(i=2, j=1)`: `i >= j` verdadeiro → retorna `1` (palíndromo).

### Exemplo 2 — Remoção *in-place* com dois índices (tratando adjacentes) *(Programa parcial)*
```c
void remover_caractere(char s[], int i, int j, char c) {
    if (s[i] == '\0') {
        s[j] = '\0';
        return;
    }
    if (s[i] != c) {
        s[j] = s[i];
        remover_caractere(s, i + 1, j + 1, c);
    } else {
        remover_caractere(s, i + 1, j, c);
    }
}
```
Rastreamento de `remover_caractere("AAA", 0, 0, 'A')`:
- `(i=0, j=0)`: `s[0]=='A'` → descarta, chama `(1, 0)`
- `(i=1, j=0)`: `s[1]=='A'` → descarta, chama `(2, 0)`
- `(i=2, j=0)`: `s[2]=='A'` → descarta, chama `(3, 0)`
- `(i=3, j=0)`: `s[3]=='\0'` → grava `s[0] = '\0'` → resultado `""`.

---

## 3. Exercícios (`G07-E01` a `G07-E06`)

### Sessão 1 (`G07-E01` a `G07-E03` — Teste de Mesa, Lacunas e Caça ao Bug)

### `G07-E01` *(Teste de Mesa — Par vs. Ímpar e Ocorrências Adjacentes)*
Sem usar computador:
- **(a)** Liste todos os pares `(i, j)` percorridos por `eh_palindromo(s, 0, len - 1)` para `"ARARA"` e para `"ABBA"`. Explique por que o caso base `if (i == j)` funcionaria em `"ARARA"`, mas falharia em `"ABBA"`.
- **(b)** Rastreie `remover_caractere(s, 0, 0, 'A')` do Exemplo 2 para `"BANANA"`, listando cada chamada `(i, j, s[i])` e o conteúdo final de `s`.
- **(c)** Se um aluno usar deslocamento à esquerda recursivo e, após remover `s[i] == 'A'`, chamar `remover(s, i + 1, 'A')` em vez de `remover(s, i, 'A')`, o que acontece com a string `"AAA"`? Qual string sobra no final?

---

### `G07-E02` *(Completar solução — Inversão *in-place*)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` para que o programa inverta `s` *in-place* sem usar laços nas funções recursivas:

```c
#include <stdio.h>

int comprimento(const char s[], int i);
void inverter(char s[], int i, int j);

int main(void) {
    char s[100];
    scanf("%99s", s);
    int len = comprimento(s, 0);
    inverter(s, 0, /* D */);
    printf("Invertida: %s\n", s);
    return 0;
}

int comprimento(const char s[], int i) {
    if (s[i] == '\0') {
        return 0;
    }
    return 1 + comprimento(s, i + 1);
}

void inverter(char s[], int i, int j) {
    if (/* A */) {
        return;
    }
    /* B */
    inverter(s, /* C */);
}
```

---

### `G07-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler uma linha `s`, verificar se é palíndromo, invertê-la *in-place* e imprimir `Palindromo: Sim/Nao` e `Invertida: <s>`. Identifique os **3 bugs intencionais**, corrija o programa completo e explique cada correção com **comentários `//`**:

```c
#include <stdio.h>

int comprimento(const char s[], int i);
int eh_palindromo(const char s[], int i, int j);
void inverter(char s[], int i, int j);

int main(void) {
    char s[100];
    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }

    int len = comprimento(s, 0);
    if (eh_palindromo(s, 0, len - 1)) {
        printf("Palindromo: Sim\n");
    } else {
        printf("Palindromo: Nao\n");
    }

    inverter(s, 0, len);
    printf("Invertida: %s\n", s);
    return 0;
}

int comprimento(const char s[], int i) {
    if (s[i] == '\0') {
        return 0;
    }
    return 1 + comprimento(s, i + 1);
}

int eh_palindromo(const char s[], int i, int j) {
    if (i == j) {
        return 1;
    }
    if (s[i] != s[j]) {
        return 0;
    }
    return eh_palindromo(s, i + 1, j - 1);
}

void inverter(char s[], int i, int j) {
    if (i >= j) {
        return;
    }
    char aux = s[i];
    s[i] = s[j];
    s[j] = aux;
    inverter(s, i + 1, j);
}
```

---

### Sessão 2 (`G07-E04` a `G07-E06` — Implementação *In-Place* Sem Laços)

### `G07-E04` *(Variação controlada com pistas — Palíndromo recursivo)*
Escreva um **programa completo** em C99 (sem laços nas funções recursivas e sem `<string.h>`) com:
- `int comprimento(const char s[], int i);`
- `int eh_palindromo(const char s[], int i, int j);`

No `main`, leia uma linha em `char s[100]` com `fgets` (removendo `'\n'`/`'\r'`) e imprima exatamente:
```text
Palindromo: Sim
```
*(ou `Palindromo: Nao`). Considere comparação exata caractere a caractere e string vazia `""` como palíndromo.*  
*Pista:* chame `eh_palindromo(s, 0, comprimento(s, 0) - 1)` e use `if (i >= j) return 1;`.

---

### `G07-E05` *(Variação controlada com pistas — Inversão *in-place*)*
Escreva um **programa completo** em C99 (sem laços nas funções recursivas) com:
- `int comprimento(const char s[], int i);`
- `void inverter(char s[], int i, int j);` *(altera `s` diretamente no próprio vetor, sem criar segunda string)*

No `main`, leia uma linha em `char s[100]` com `fgets` (removendo `'\n'`/`'\r'`), inverta `s` e imprima exatamente:
```text
Invertida: <string_invertida>
```
*Pista:* para string vazia (`len == 0`), `len - 1 == -1`, e `if (i >= j) return;` protege contra acesso inválido.

---

### `G07-E06` *(Resolução independente — Remoção *in-place* sem laço e sem auxiliar)*
Projete a assinatura e implemente uma função recursiva `remover_caractere` que remova **in-place** todas as ocorrências de um caractere `c` em uma string `char s[]`, **sem usar laços (`for`/`while`/`do-while`) nem vetor auxiliar**, tratando corretamente ocorrências adjacentes (como `"AAA"` → `'A'`) e gravando `'\0'` na nova posição final.

No `main`, leia uma linha em `char s[100]` com `fgets` (removendo `'\n'`/`'\r'`) e um caractere não-espaço `c` com `scanf(" %c", &c);`. Imprima exatamente:
```text
Resultado: <string_modificada>
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `G07-C01` *(Teste de Mesa e Análise de Borda)*
Sem usar computador:
1. Rastreie `remover_caractere("AABAA", 0, 0, 'A')` (com índices de leitura `i` e escrita `j`), indicando todas as chamadas `(i, j)` até `s[j] = '\0'` e a string final obtida.
2. Explique qual erro exato acontece ao chamar `inverter(s, 0, comprimento(s, 0) - 1)` para `s = "CASA"` se o caso base for escrito erroneamente como `if (i == j) return;`.

### `G07-C02` *(Implementação independente — Palíndromo + Inversão *in-place*)*
Escreva um **programa completo** em C99 (sem laços nas funções recursivas e sem `<string.h>`) com `comprimento`, `eh_palindromo` e `inverter` *in-place*. No `main`, leia uma palavra `char s[100]` com `scanf("%99s", s);`, verifique se é palíndromo, inverta `s` e imprima exatamente:
```text
Palindromo: Sim
Invertida: <string_invertida>
```
*(ou `Palindromo: Nao`).*

### `G07-C03` *(Implementação independente — Remoção *in-place* de espaços)*
Escreva um **programa completo** em C99 (sem laços nas funções recursivas e sem vetor auxiliar) com:
- `void remover_espacos(char s[], int i, int j);` *(remove todos os `' '` in-place e grava `'\0'`)*
- `int comprimento(const char s[], int i);`

No `main`, leia uma linha em `char s[100]` com `fgets` (removendo `'\n'`/`'\r'`), remova os espaços e imprima exatamente:
```text
Sem espacos: <string_sem_espacos>
Comprimento: L
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `G08` (`Recursão Múltipla vs. Divisão pela Metade`):** somente após autocorreção de `G07-E01..E06` e **100% (3/3)** na Checagem Independente `G07-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** revisar a diferença entre tamanho par e ímpar no caso base `i >= j`, traçar no papel a tabela `(i, j)` da remoção com `"AAA"` e aplicar variante `V2` de `G07`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`G06`** (índice crescente até `'\0'`) e **`D08`** / **`F07`** (conceito de algoritmo *in-place* com dois índices).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (itens 9 e 10 — modularização e recursão).
- `[DOC]` `Aula_23_Algoritmos.pdf` p. 9–14 (palíndromo, inversão com dois índices e remoção recursiva *in-place*).
- `[DOC]` `Lista12_Algoritmos.pdf` p. 1–2 (Ex. 4, Ex. 5 — entrega).
- Casos de teste e soluções verificáveis: [G07_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/gabaritos/G07_gabarito.md) e [G07_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/G07_testes.md).
