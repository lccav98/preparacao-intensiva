# Bloco `F10` — Revisão e Consolidação do Estágio F *(Bloco de Revisão)*

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio F — Modularização, Funções, Ponteiros e Compilação Multi-Arquivo / **`F10`** |
| **Micro-habilidade foco** | *(Revisão integrada de `F01` a `F09`)* Combinar protótipos, escopo local, passagem de escalares e endereços por valor (`&`/`*`), funções com `const` em vetores/matrizes/strings, composição e organização multi-arquivo `.h`/`.c` no GCC. |
| **Pré-requisitos** | `F09` *(Pré-processamento, etapas de compilação e compilação vs. interpretação)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 22 min):** `14 min` resol. \| `5 min` corr. \| `3 min` recup.; **Sessão 2 (`E04`–`E06`, 23 min):** `14 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Conteúdo novo: NENHUM.** **É terminantemente proibido** o uso de recursividade (tópico exclusivo do Estágio G), `struct`, alocação dinâmica (`malloc`/`free`) ou VLAs. Utilize estritamente C99 com capacidades fixas e saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Apto para Estágio G`)

---

## 1. Instruções Curtas (Matriz de Consolidação do Estágio F)

1. **Funções, protótipos e escopo (`F01`–`F03`):**
   - Protótipos antes de `main` permitem posicionar as implementações após `main`.
   - Toda passagem de argumento em C é **por valor** (cópia). Variáveis locais com mesmo nome em funções diferentes ocupam espaços independentes na memória.
2. **Ponteiros e parâmetros de saída (`F04`–`F05`):**
   - Para alterar variáveis do chamador ou devolver 2+ resultados, passe **endereços por valor** (`&var` → `int *p`).
   - `*p` acessa/altera o alvo; `p` altera apenas a cópia local do endereço. Ao repassar um ponteiro `p` para outra função `aux(p)`, **não** use `&`.
3. **Vetores 1D, matrizes 2D, strings e `const` (`F06`–`F07`):**
   - `int v[]` decai para o endereço do 1º elemento (`&v[0]`) e exige `int n`. Use `const` sempre que a função for somente leitura.
   - Matrizes 2D exigem a dimensão das colunas (`const int m[][COL], int linhas`).
   - Strings dispensam `n` graças a `'\0'`; alterações *in-place* com 2 índices exigem `s[j] = '\0';` ao final.
4. **Multi-arquivo e etapas GCC (`F08`–`F09`):**
   - `.h` (guardas `#ifndef`/`#define`/`#endif`, `#define` e protótipos) × `.c` (implementações + `#include "mod.h"`).
   - Pré-processamento (`#include`, `#define`) → Compilação (`-c`, `.o`) → Ligação (`gcc main.c mod.c -o prog`, nunca passar `.h`).

---

## 2. Exemplos Guiados

### Exemplo 1 — Ponteiros, `const` em vetor e repasse *(Trecho ilustrativo)*
```c
void ajustar_alvo(int *q, int delta) {
    *q += delta;
}

void processar(const int v[], int n, int *total) {
    *total = 0;
    for (int i = 0; i < n; i++) {
        ajustar_alvo(total, v[i]); /* total ja eh int *, repassa sem '&' */
    }
}
```

### Exemplo 2 — Cabeçalho modular protegido + comando GCC *(Trecho ilustrativo)*
```c
#ifndef MOD_EXEMPLO_H
#define MOD_EXEMPLO_H

#define COL 3
int soma_linha(const int m[][COL], int linha);

#endif
```
Compilação: `gcc -std=c99 -Wall -Wextra main.c mod_exemplo.c -o prog`.

---

## 3. Exercícios (`F10-E01` a `F10-E06`)

### Sessão 1 (`F10-E01` a `F10-E03` — Rastreamento, Diagnóstico e Caça ao Bug)

### `F10-E01` *(Teste de Mesa Integrado — Ponteiros, Escopo e Vetores)*
Sem usar computador, execute o rastreamento completo do programa abaixo:

```c
#include <stdio.h>

void alterar(int x, int *p, int v[], int n);

int main(void) {
    int x = 10, y = 20;
    int v[3] = {1, 2, 3};

    alterar(x, &y, v, 3);
    printf("x=%d y=%d v0=%d\n", x, y, v[0]);
    return 0;
}

void alterar(int x, int *p, int v[], int n) {
    int k = 99;
    x = 50;
    *p = *p + 5;
    p = &k;
    *p = 77;
    if (n > 0) {
        v[0] += 10;
    }
}
```
**(a)** Qual linha exata é impressa por `main`?  
**(b)** Explique por que `x` em `main` continuou `10`, por que `y` passou para `25` (e não `77`) e por que `v[0]` mudou para `11`.

---

### `F10-E02` *(Diagnóstico Multi-Arquivo e Etapas GCC)*
Identifique em qual etapa (`Pré-processamento`, `Compilação` ou `Ligação`) cada erro ocorre, nomeie a mensagem típica do GCC e dê a correção exata:
1. `gcc -std=c99 -Wall -Wextra main.c -o prog`, onde `main.c` chama `limpar_texto(s)` definida em `texto.c` (incluindo `"texto.h"`).
2. `matriz.h` declara `void zerar(int m[][]);` (faltando `COL`).
3. `calc.h` define `int triplo(int x) { return 3 * x; }` e é incluído tanto por `main.c` quanto por `calc.c`.

---

### `F10-E03` *(Caça ao Bug Integrada — Ponteiros, `const` e String in-place)*
O programa completo abaixo lê uma linha de texto `s`, um inteiro `n` (`1 <= n <= 50`) e `n` inteiros em `v`, devendo exibir `Soma: S`, `Maior: M` e `Sem espacos: <s_sem_espacos>`. Identifique os **3 bugs intencionais**, corrija o programa completo e documente cada correção com **comentários `//` no código**:

```c
#include <stdio.h>

void resumo(const int v[], int n, int *soma, int *maior);
void limpar_espacos(char s[]);

int main(void) {
    char s[100];
    int n, v[50], soma, maior;

    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    resumo(v, n, soma, &maior);
    limpar_espacos(s);

    printf("Soma: %d\n", soma);
    printf("Maior: %d\n", maior);
    printf("Sem espacos: %s\n", s);
    return 0;
}

void resumo(const int v[], int n, int *soma, int *maior) {
    soma = 0;
    *maior = v[0];
    for (int i = 0; i < n; i++) {
        *soma += v[i];
        if (v[i] > *maior) {
            *maior = v[i];
        }
    }
}

void limpar_espacos(char s[]) {
    int j = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] != ' ') {
            s[j] = s[i];
            j++;
        }
    }
}
```

---

### Sessão 2 (`F10-E04` a `F10-E06` — Implementação Integrada Independente)

### `F10-E04` *(Integração 1 — Composição, Vetor `const` e Ponteiros de Saída)*
Escreva um **programa completo** em C99 com protótipos antes de `main` contendo:
```c
double media_vetor(const int v[], int n);
void analisar_vetor(const int v[], int n, int lim, int *acima_lim, double *media);
```
Onde `analisar_vetor` chama `media_vetor` para gravar `*media` e conta em `*acima_lim` quantos elementos de `v` são estritamente maiores que `lim`. No `main`, leia `n` (`1 <= n <= 50`), `n` inteiros e `lim`, chame `analisar_vetor` e imprima:
```text
Media: M.MM
Acima do limite: K
```

---

### `F10-E05` *(Integração 2 — Projeto Multi-Arquivo `matriz_ops`)*
Implemente em **3 arquivos** (`matriz_ops.h`, `matriz_ops.c`, `main.c`):
- `matriz_ops.h` (guardas `MATRIZ_OPS_H`, `#define COL 3`):
  - `int soma_diagonal_principal(const int m[][COL]);` *(matriz `3 x 3`)*
  - `void extremos_matriz(const int m[][COL], int linhas, int *menor, int *maior);`
- `matriz_ops.c`: implementa as duas funções.
- `main.c`: lê os `9` inteiros da matriz `3 x 3`, chama as funções e imprime:
  ```text
  Diagonal principal: DP
  Menor: MN
  Maior: MX
  ```

---

### `F10-E06` *(Integração 3 — Projeto Multi-Arquivo `texto_ops`)*
Implemente em **3 arquivos** (`texto_ops.h`, `texto_ops.c`, `main.c`):
- `texto_ops.h` (guardas `TEXTO_OPS_H`):
  - `int contar_letras(const char s[]);` *(conta `'a'..'z'` e `'A'..'Z'`)*
  - `void substituir_caractere(char s[], char antigo, char novo);` *(in-place)*
- `texto_ops.c`: implementa as duas funções.
- `main.c`: lê uma linha em `char s[100]` com `fgets` (removendo `'\n'`/`'\r'`), lê dois caracteres não-espaço `antigo` e `novo` com `scanf(" %c %c", &antigo, &novo)`, aplica `substituir_caractere` e imprime:
  ```text
  Texto: <s_modificada>
  Letras: L
  ```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `F10-C01` *(Teste de Mesa Integrado — Ponteiros, Repasse e `const`)*
Sem usar computador, analise o programa abaixo:
```c
#include <stdio.h>

void ajustar(int *q);
void aplicar(int *p, int v[], int n);
int somar(const int v[], int n);

int main(void) {
    int a = 5;
    int v[3] = {2, 4, 6};
    aplicar(&a, v, 3);
    printf("a=%d soma=%d\n", a, somar(v, 3));
    return 0;
}

void ajustar(int *q) {
    *q += 10;
}

void aplicar(int *p, int v[], int n) {
    ajustar(p);
    if (n > 0) {
        v[0] += *p;
    }
}

int somar(const int v[], int n) {
    int s = 0;
    for (int i = 0; i < n; i++) {
        s += v[i];
    }
    return s;
}
```
**(a)** Qual linha é impressa por `main`?  
**(b)** Por que `aplicar` chama `ajustar(p)` sem `&` e qual a função do modificador `const` em `somar`?

### `F10-C02` *(Diagnóstico Multi-Arquivo e Etapas GCC)*
Dado um projeto com `main.c`, `oper.h` e `oper.c`, diagnostique os 3 defeitos abaixo (etapa + erro + correção):
1. `gcc -std=c99 -Wall -Wextra main.c -o app` quando `main.c` chama `oper_media(v, n)` de `oper.c`.
2. `oper.h` sem guardas `#ifndef` e contendo `int dobro(int x) { return 2 * x; }`, incluído em `main.c` e `oper.c`.
3. `oper.h` declara `double oper_media(const int v[], int n);` e `oper.c` define `int oper_media(const int v[], int n)`.

### `F10-C03` *(Projeto Multi-Arquivo Independente — `analise`)*
Crie os **3 arquivos** `analise.h` (guardas `ANALISE_H`, `#define COL 3`), `analise.c` e `main.c`:
- `void linha_extremos(const int m[][COL], int linha, int *menor, int *maior);`
- `int contar_ocorrencias_str(const char s[], char ch);`

No `main.c`, leia `linhas` (`1 <= linhas <= 10`), leia os `linhas x 3` inteiros de `m[10][COL]`, leia o índice `idx` (`0 <= idx < linhas`), leia uma palavra `s` (`scanf("%49s", s)`) e um caractere `ch` (`scanf(" %c", &ch)`). Imprima exatamente:
```text
Linha <idx>: menor=<MN> maior=<MX>
Ocorrencias: <K>
```
Compile limpo com `gcc -std=c99 -Wall -Wextra main.c analise.c -o prog`.

---

## 5. Orientação de Avanço ou Recuperação (Conclusão do Estágio F)

- **Avançar para o Estágio G (`G01 — Conceito de Recursividade e Pilha de Execução`):** somente após autocorreção de `F10-E01..E06` **e** **100% de acerto (3/3)** na Checagem Independente `F10-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada por sub-habilidade (1ª falha):**
  - Falha em protótipos, escopo local ou passagem por valor $\rightarrow$ revisar **`F01`–`F03`**.
  - Falha em `&`/`*`, parâmetros de saída ou repasse de ponteiros $\rightarrow$ revisar **`F04`–`F05`**.
  - Falha em `const`, matrizes `m[][COL]` ou strings *in-place* $\rightarrow$ revisar **`F06`–`F07`**.
  - Falha em `.h`/`.c`, `#ifndef`, erros do GCC ou pré-processamento $\rightarrow$ revisar **`F08`–`F09`**.
- **Após 2 tentativas malsucedidas:** interromper novas tentativas em `F10`, diagnosticar qual pré-requisito (`F01`–`F09`) falhou e reabilitá-lo integralmente antes de refazer a checagem de conclusão do Estágio F.

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (itens 9 e 11).
- `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 4 (27/10 a 10/11).
- `[DOC]` `Aula_16`–`Aula_20` e `Lista10_Algoritmos.pdf` completa.
- Casos de teste e soluções verificáveis: [F10_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/gabaritos/F10_gabarito.md) e [F10_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/F10_testes.md).
