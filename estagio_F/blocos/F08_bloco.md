# Bloco `F08` — Organização Multi-Arquivo (`.h` e `.c`), Guardas `#ifndef`, Ligação no GCC e Diagnóstico de Erros

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio F — Modularização, Funções, Ponteiros e Compilação Multi-Arquivo / **`F08`** |
| **Micro-habilidade foco** | Separar um programa em interface (`.h` com guardas `#ifndef`/`#define`/`#endif`), implementação (`.c`) e consumidor (`main.c`), compilar múltiplos `.c` no GCC e diagnosticar os 4 erros clássicos de cabeçalho e ligação. |
| **Pré-requisitos** | `F07` *(Funções com matrizes 2D `m[][COL]`, strings in-place e composição de funções)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Sessão 2 (`E04`–`E06`, 23 min):** `14 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Não utilize** recursividade (`G01`), `struct`, alocação dinâmica (`malloc`/`free`) ou VLAs. Mantenha no `.h` apenas constantes `#define` e protótipos (nunca corpos de função), e nunca passe arquivos `.h` diretamente ao comando `gcc`. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Separação Interface × Implementação:**
   - **Arquivo `.h` (cabeçalho / interface):** contém **apenas** `#define`s compartilhados e **protótipos** das funções públicas do módulo. **Nunca** coloque implementações (corpos `{ ... }`) de funções comuns no `.h`.
   - **Arquivo `.c` do módulo (implementação):** inclui seu próprio cabeçalho (`#include "mod.h"`) e implementa o código de cada função declarada no `.h`.
   - **Arquivo `main.c` (consumidor):** inclui `<stdio.h>` e `"mod.h"` para poder chamar as funções do módulo.
2. **`#include <...>` vs. `#include "..."`:**
   - `<stdio.h>` (sinais `< >`): busca nos diretórios padrão do compilador/sistema.
   - `"mod.h"` (aspas duplas `" "`): busca primeiro no diretório do projeto (cabeçalhos locais).
3. **Guardas de inclusão (`#ifndef` / `#define` / `#endif`):** Todo `.h` deve começar e terminar com:
   ```c
   #ifndef NOME_MODULO_H
   #define NOME_MODULO_H
   /* constantes e prototipos */
   #endif
   ```
   Isso impede inclusões duplicadas caso vários arquivos incluam o mesmo `.h`.
4. **Compilação multi-arquivo no GCC:** `#include "mod.h"` faz apenas colagem textual de **protótipos**, **não** compila nem liga `mod.c`! Você deve listar **todos os `.c`** no comando GCC e **nunca** listar `.h`:
   ```bash
   gcc -std=c99 -Wall -Wextra main.c mod.c -o prog
   ```
5. **Diagnóstico dos 4 erros clássicos:**
   - `No such file or directory`: nome do `.h` errado ou uso de `<mod.h>` em vez de `"mod.h"`.
   - `undefined reference to '...'`: erro de ligação — esqueceu de passar `mod.c` ao `gcc` (ou o nome da função no `.c` diverge do protótipo).
   - `multiple definition of '...'`: corpo de função implementado dentro do `.h` (incluído em dois `.c`), ou duas implementações em `.c` distintos.
   - `conflicting types for '...'`: assinatura (tipo de retorno ou parâmetros) no `.h` difere da definição no `.c`.

---

## 2. Exemplos Guiados

### Exemplo 1 — Estrutura mínima de módulo em 3 arquivos *(Trecho ilustrativo)*

**`math_util.h`**
```c
#ifndef MATH_UTIL_H
#define MATH_UTIL_H

int dobro(int x);
int quadrado(int x);

#endif
```

**`math_util.c`**
```c
#include "math_util.h"

int dobro(int x) {
    return 2 * x;
}

int quadrado(int x) {
    return x * x;
}
```

**`main.c`**
```c
#include <stdio.h>
#include "math_util.h"

int main(void) {
    int n;
    scanf("%d", &n);
    printf("Dobro: %d\nQuadrado: %d\n", dobro(n), quadrado(n));
    return 0;
}
```
**Comando de compilação e execução:**
```bash
gcc -std=c99 -Wall -Wextra main.c math_util.c -o prog && ./prog
```

---

## 3. Exercícios (`F08-E01` a `F08-E06`)

### Sessão 1 (`F08-E01` a `F08-E03` — Diagnóstico, Lacunas e Caça ao Bug)

### `F08-E01` *(Diagnóstico sem Compilar — Os 4 erros clássicos)*
Para cada situação abaixo, identifique qual dos 4 erros ocorre (`No such file or directory`, `undefined reference`, `multiple definition` ou `conflicting types`) e explique como corrigi-lo:
- **(a)** `main.c` inclui `"vetor.h"` e chama `soma_vetor(v, n)`, mas o aluno executa `gcc -std=c99 -Wall -Wextra main.c -o prog`.
- **(b)** `main.c` escreve `#include <vetor.h>` para um arquivo local na mesma pasta.
- **(c)** O arquivo `calc.h` contém a implementação completa `int dobro(int x) { return 2 * x; }` e é incluído por `main.c` e `calc.c`.
- **(d)** `vetor.h` declara `double media(const int v[], int n);`, mas `vetor.c` define `int media(const int v[], int n) { ... }`.

---

### `F08-E02` *(Completar cabeçalho `.h` com guardas e comando GCC)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` para o arquivo `stats.h` e indique o comando de compilação correto:

```c
/* A */ STATS_H
/* B */ STATS_H

int maximo(const int v[], int n);
double media(const int v[], int n);

/* C */
```
**(d)** Escreva o comando `gcc -std=c99 -Wall -Wextra ...` correto para compilar `main.c` e `stats.c` gerando o executável `app` (sem passar `.h`).

---

### `F08-E03` *(Caça ao Bug Multi-Arquivo — Correção em 3 arquivos)*
O projeto de 3 arquivos abaixo deveria ler dois inteiros `a` e `b` e imprimir `Soma: S` e `Pares: P` (quantidade de pares no intervalo fechado `[min(a,b), max(a,b)]`). Identifique os **3 bugs intencionais** espalhados entre `calc.h`, `calc.c` e `main.c`, corrija os 3 arquivos e explique os bugs usando **comentários `//` diretamente no código**:

**`calc.h` (com erro):**
```c
int soma_intervalo(int a, int b) {
    if (a > b) { int aux = a; a = b; b = aux; }
    int s = 0;
    for (int i = a; i <= b; i++) s += i;
    return s;
}
double contar_pares(int a, int b);
```

**`calc.c` (com erro):**
```c
#include "calc.h"

int contar_pares(int a, int b) {
    if (a > b) { int aux = a; a = b; b = aux; }
    int cont = 0;
    for (int i = a; i <= b; i++) {
        if (i % 2 == 0) cont++;
    }
    return cont;
}
```

**`main.c` (com erro):**
```c
#include <stdio.h>
#include <calc.h>

int main(void) {
    int a, b;
    scanf("%d %d", &a, &b);
    printf("Soma: %d\n", soma_intervalo(a, b));
    printf("Pares: %d\n", contar_pares(a, b));
    return 0;
}
```

---

### Sessão 2 (`F08-E04` a `F08-E06` — Refatoração e Construção Multi-Arquivo)

### `F08-E04` *(Variação controlada com pistas — Módulo `vetor` em 3 arquivos)*
Organize em **3 arquivos** (`vetor.h`, `vetor.c`, `main.c`) um programa que leia `n` (`1 <= n <= 50`) e `n` inteiros em `v[50]`, exibindo `Soma: S` e `Maior: M`:
- `vetor.h` (com guardas `VETOR_H`): protótipos de `void ler_vetor(int v[], int n);`, `int soma_vetor(const int v[], int n);` e `int maior_vetor(const int v[], int n);`.
- `vetor.c`: inclui `<stdio.h>` e `"vetor.h"` e implementa as 3 funções.
- `main.c`: inclui `<stdio.h>` e `"vetor.h"`, lê `n`, chama as funções e imprime:
  ```text
  Soma: S
  Maior: M
  ```
*Pista:* Compile com `gcc -std=c99 -Wall -Wextra main.c vetor.c -o prog`.

---

### `F08-E05` *(Variação controlada com pistas — Módulo `matriz` 2D em 3 arquivos)*
Crie os **3 arquivos** `matriz.h`, `matriz.c` e `main.c`:
- `matriz.h` (com guardas `MATRIZ_H`): defina `#define COL 3` e os protótipos:
  - `void ler_matriz(int m[][COL], int linhas);`
  - `int soma_coluna(const int m[][COL], int linhas, int col);`
  - `int maior_matriz(const int m[][COL], int linhas);`
- `matriz.c`: implemente as funções.
- `main.c`: leia `linhas` (`1 <= linhas <= 10`) e o índice da coluna `c` (`0 <= c < 3`), depois os `linhas * 3` inteiros da matriz `m[10][COL]`, e imprima exatamente:
  ```text
  Soma coluna C: S
  Maior: M
  ```
*Pista:* Como `COL` é compartilhado entre `main.c` e `matriz.c`, declare `#define COL 3` dentro de `matriz.h`.

---

### `F08-E06` *(Resolução independente — Módulo `texto` em 3 arquivos)*
Construa um projeto modular em **3 arquivos** (`texto.h`, `texto.c`, `main.c`):
- `texto.h` (com guardas `TEXTO_H`): protótipos de:
  - `int contar_ocorrencias(const char s[], char ch);`
  - `void para_maiusculas(char s[]);` *(converte `'a'..'z'` para `'A'..'Z'` in-place)*
- `texto.c`: implementa as duas funções (sem `<string.h>` ou `<ctype.h>` necessários).
- `main.c`: lê uma linha em `char s[100]` com `fgets` (removendo `'\n'`/`'\r'`), lê um caractere não-espaço `ch` com `scanf(" %c", &ch)`, conta as ocorrências de `ch` **antes** da conversão para maiúsculas, converte `s` e imprime exatamente:
  ```text
  Ocorrencias: K
  Maiusculas: <string_convertida>
  ```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `F08-C01` *(Diagnóstico sem Compilar)*
Identifique o erro exato do GCC e como corrigi-lo em cada cenário:
1. O comando `gcc -std=c99 -Wall -Wextra main.c -o prog` falha quando `main.c` chama `calc_media(v, n)` declarada em `mod.h` e definida em `mod.c`.
2. O arquivo `mod.h` define `int f(int x) { return x + 1; }` e é incluído em `main.c` e `mod.c`.
3. `mod.h` declara `void f(const int v[], int n);` e `mod.c` implementa `int f(const int v[], int n) { ... }`.

### `F08-C02` *(Escrita de `.h` válido com guardas)*
Escreva no papel o conteúdo completo e válido de um arquivo `geometria.h` protegido contra inclusão múltipla (`GEOMETRIA_H`) contendo os protótipos de:
- `double area_retangulo(double base, double altura);`
- `void retangulo_info(double base, double altura, double *area, double *perimetro);`

### `F08-C03` *(Projeto 3-arquivos independente — Módulo `estatistica`)*
Crie os **3 arquivos** `estatistica.h` (guardas `ESTATISTICA_H`), `estatistica.c` e `main.c` com:
- `double media_vetor(const int v[], int n);`
- `int contar_no_intervalo(const int v[], int n, int min, int max);` *(conta elementos no intervalo fechado `[min, max]`)*

No `main.c`, leia `n` (`1 <= n <= 50`), os `n` inteiros de `v`, e dois inteiros `min` e `max`. Imprima exatamente:
```text
Media: M.MM
No intervalo: K
```
Compile e verifique com `gcc -std=c99 -Wall -Wextra main.c estatistica.c -o prog`.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `F09` (`Pré-Processamento, Etapas de Compilação e Compilação vs. Interpretação`):** somente após autocorreção de `F08-E01..E06` e **100% (3/3)** em `F08-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** desenhar o mapa `.h` (protótipos + guardas) × `.c` (implementações) × `gcc main.c mod.c`, revisar a tabela dos 4 erros clássicos e aplicar variante `V2` de `F08`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`F07`** (funções com matrizes 2D e strings) e **`F02`** (protótipos vs. definições e escopo).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (itens 9 e 11 — modularização e compilação).
- `[DOC]` `Aula_19_Algoritmos.pdf` p. 3–20 (arquivos `.h`/`.c`, `#ifndef`, compilação multi-arquivo e diagnóstico de erros).
- `[DOC]` `Lista10_Algoritmos.pdf` p. 3 (Ex. 8 — entrega modularizada em múltiplos arquivos `questao8.zip`).
- `[DOC]` `Apresentacao_Trabalho_Algoritmos.pdf` p. 5–6 (organização em `.h` e `.c`).
- Casos de teste e soluções verificáveis: [F08_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/gabaritos/F08_gabarito.md) e [F08_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/F08_testes.md).
