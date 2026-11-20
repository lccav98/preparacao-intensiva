# Bloco `F07` — Funções com Matrizes 2D (`m[][COL]`), Strings *In-Place* e Composição de Funções

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio F — Modularização, Funções, Ponteiros e Compilação Multi-Arquivo / **`F07`** |
| **Micro-habilidade foco** | Implementar funções que recebem matrizes 2D (informando obrigatoriamente a dimensão das colunas `m[][COL]`), manipular strings (`const char s[]` vs. `char s[]` *in-place* até `'\0'`) e compor funções onde uma função chama outra. |
| **Pré-requisitos** | `F06` *(Funções com vetores 1D e modificador `const`)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Sessão 2 (`E04`–`E06`, 22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Não utilize** organização multi-arquivo `.h`/`.c` (`F08`), recursividade (`G01`), `struct`, alocação dinâmica (`malloc`/`free`) ou VLAs. Utilize constantes `#define` para a dimensão de colunas, manipulação *in-place* em strings sem vetor auxiliar quando solicitado e protótipos antes de `main`. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Obrigatoriedade das colunas em matrizes 2D (`m[][COL]`):** Matrizes são armazenadas de forma linear (*row-major*: linha após linha). Para localizar `m[i][j]` a partir do endereço inicial, o compilador calcula o deslocamento `i * COL + j`. Por isso:
   - O número de linhas pode ficar vazio (`m[][COL]`), mas o número de **colunas (`COL`) é obrigatório** no protótipo e na definição! Escrever `int m[][]` gera erro de compilação.
   - Use `#define COL ...` e informe `int linhas` quando a quantidade de linhas for variável (até a capacidade máxima).
   - Se a função apenas lê a matriz, use **`const int m[][COL]`**.
2. **Strings em funções dispensam `n`:** Como uma string C termina sempre no marcador `'\0'`, funções como `int contar(const char s[])` ou `void limpar(char s[])` não precisam receber o tamanho `n`; basta percorrer até `s[i] != '\0'`.
3. **Transformação *in-place* em strings com 2 índices:** Para remover ou filtrar caracteres sem criar uma segunda string, use:
   - `i` para **leitura** (`0` até `s[i] != '\0'`);
   - `j` para **escrita** dos caracteres mantidos (`s[j] = s[i]; j++;`);
   - Ao final do laço, grave obrigatoriamente **`s[j] = '\0';`** (esquecer `'\0'` deixa "lixo" residual do texto antigo!).
4. **Composição de funções:** Uma função pode (e deve) chamar outra função auxiliar declarada anteriormente por protótipo (ex.: `media_matriz` chama `soma_matriz(m, linhas)`). Na chamada interna, repasse `m` e `linhas` diretamente pelos nomes dos parâmetros (sem colchetes `[]` nem `&`).

---

## 2. Exemplos Guiados

### Exemplo 1 — Matriz 2D com `const` e composição de funções *(Trecho ilustrativo)*
```c
#define COL 3

int soma_linha(const int m[][COL], int linha) {
    int s = 0;
    for (int j = 0; j < COL; j++) {
        s += m[linha][j];
    }
    return s;
}

double media_linha(const int m[][COL], int linha) {
    /* Composicao: media_linha reutiliza soma_linha */
    return (double)soma_linha(m, linha) / COL;
}
```

### Exemplo 2 — Remoção *in-place* em string com 2 índices *(Programa completo)*
```c
#include <stdio.h>

void remover_hifens(char s[]);

int main(void) {
    char codigo[50];
    scanf("%49s", codigo);
    remover_hifens(codigo);
    printf("%s\n", codigo);
    return 0;
}

void remover_hifens(char s[]) {
    int j = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] != '-') {
            s[j] = s[i];
            j++;
        }
    }
    s[j] = '\0';
}
```
Observe: para `"12-34-5"`, `i` percorre os `7` caracteres, `j` grava `'1','2','3','4','5'` nos índices `0..4` e `s[5] = '\0'` encerra a nova string `"12345"`.

---

## 3. Exercícios (`F07-E01` a `F07-E06`)

### Sessão 1 (`F07-E01` a `F07-E03` — Rastreamento, Lacunas e Depuração)

### `F07-E01` *(Teste de Mesa e Composição — Reprodução do modelo)*
Sem utilizar computador, acompanhe o programa completo abaixo:

```c
#include <stdio.h>
#define COL 3

int soma_linha(const int m[][COL], int linha);
double media_linha(const int m[][COL], int linha);

int main(void) {
    int mat[2][COL] = {
        {3, 6, 9},
        {1, 2, 3}
    };
    printf("L0: %.2f\n", media_linha(mat, 0));
    printf("L1: %.2f\n", media_linha(mat, 1));
    return 0;
}

int soma_linha(const int m[][COL], int linha) {
    int s = 0;
    for (int j = 0; j < COL; j++) {
        s += m[linha][j];
    }
    return s;
}

double media_linha(const int m[][COL], int linha) {
    return (double)soma_linha(m, linha) / COL;
}
```
**(a)** Qual é a saída exata impressa por `main`?  
**(b)** Descreva a cadeia de chamadas da 1ª linha impressa (`main -> ... -> ...`) e explique por que `COL` é obrigatório em `const int m[][COL]`.

---

### `F07-E02` *(Completar solução — Remoção de espaços in-place)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` para remover todos os espaços `' '` de `s` *in-place*:

```c
#include <stdio.h>

void remover_espacos( /* A */ );

int main(void) {
    char frase[60] = "C e modular";
    remover_espacos(frase);
    printf("%s\n", frase);
    return 0;
}

void remover_espacos( /* A */ ) {
    int j = 0;
    for (int i = 0; /* B */ ; i++) {
        if (s[i] != ' ') {
            /* C */
        }
    }
    /* D */
}
```

---

### `F07-E03` *(Caça ao Bug — Programa completo)*
O programa abaixo deveria ler `linhas` (`1 <= linhas <= 10`), ler uma matriz `linhas x 3`, ler uma palavra `texto` (até 49 caracteres) e imprimir a soma da matriz (`Soma: S`) e o texto sem dígitos `'0'..'9'` (`Texto: ...`). Identifique os **2 erros intencionais**, corrija o programa completo e explique cada erro com **comentários `//` diretamente no código**:

```c
#include <stdio.h>

#define COL 3

int somar_matriz(const int m[][], int linhas);
void remover_digitos(char s[]);

int main(void) {
    int linhas, m[10][COL];
    char texto[50];

    scanf("%d", &linhas);
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < COL; j++) {
            scanf("%d", &m[i][j]);
        }
    }
    scanf("%49s", texto);

    printf("Soma: %d\n", somar_matriz(m, linhas));
    remover_digitos(texto);
    printf("Texto: %s\n", texto);
    return 0;
}

int somar_matriz(const int m[][], int linhas) {
    int soma = 0;
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < COL; j++) {
            soma += m[i][j];
        }
    }
    return soma;
}

void remover_digitos(char s[]) {
    int j = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] < '0' || s[i] > '9') {
            s[j] = s[i];
            j++;
        }
    }
}
```

---

### Sessão 2 (`F07-E04` a `F07-E06` — Escrita Guiada → Independente)

### `F07-E04` *(Variação controlada com pistas — Simetria em matriz `3 x 3`)*
Defina `#define N 3` e escreva um **programa completo** em C com o protótipo e a implementação da função:
```c
int eh_simetrica(const int m[][N]);
```
A função deve retornar `1` se `m[i][j] == m[j][i]` para todos os elementos e `0` caso contrário. No `main`, leia os `9` inteiros da matriz `3 x 3` e imprima `Simetrica: Sim` ou `Simetrica: Nao`.  
*Pista:* Basta testar `j` variando de `i + 1` até `N - 1` e retornar `0` assim que encontrar `m[i][j] != m[j][i]`.

---

### `F07-E05` *(Variação controlada com pistas — Composição em matriz `m[][4]`)*
Defina `#define COL 4` e escreva um **programa completo** em C que implemente as três funções abaixo utilizando **composição**:
```c
int soma_matriz(const int m[][COL], int linhas);
double media_matriz(const int m[][COL], int linhas);
int contar_acima_media(const int m[][COL], int linhas);
```
`media_matriz` deve chamar `soma_matriz`, e `contar_acima_media` deve chamar `media_matriz`. No `main`, leia `linhas` (`1 <= linhas <= 10`), leia os elementos da matriz `linhas x 4` e imprima exatamente:
```text
Soma: S
Media: M.MM
Acima da media: K
```
*Pista:* Em `media_matriz`, o total de elementos da matriz é `linhas * COL`. Use `(double)soma_matriz(m, linhas) / (linhas * COL)`.

---

### `F07-E06` *(Resolução independente — Remoção in-place em string)*
Escreva um **programa completo** em C com protótipo e implementação da função:
```c
void remover_caractere(char s[], char c);
```
A função deve remover todas as ocorrências do caractere `c` da string `s` **diretamente no vetor `s` (*in-place*)**, sem declarar uma segunda string auxiliar. No `main`, leia uma linha em `char s[100]` com `fgets` (removendo o `'\n'`/`'\r'` final), leia um caractere não-espaço `c` com `scanf(" %c", &c)`, chame `remover_caractere(s, c)` e imprima exatamente:
```text
Resultado: <string_resultante>
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `F07-C01` *(Análise Conceitual e Rastreamento)*
Sem usar computador:
1. Explique por que o cabeçalho `void f(int m[][])` não compila em C, enquanto `void f(int m[][4], int linhas)` compila corretamente.
2. Explique por que funções que recebem strings (`const char s[]`) normalmente dispensam o parâmetro de tamanho `n`, diferentemente de `const int v[]`.
3. Dado `int g(const int v[], int n)` que retorna a soma de `v`, e `double h(const int v[], int n)` que retorna `(double)g(v, n) / n`, qual é o retorno de `h(a, 4)` para `a = {2, 4, 6, 8}` e em que ordem as funções iniciam e terminam?

### `F07-C02` *(Programa completo — Diagonais e composição em `3 x 3`)*
Defina `#define N 3` e implemente um programa completo com as funções:
```c
int soma_diagonal_principal(const int m[][N]);
int soma_diagonal_secundaria(const int m[][N]);
void resumo_diagonais(const int m[][N], int *dp, int *ds);
```
Onde `resumo_diagonais` compõe as duas funções anteriores gravando os resultados em `*dp` e `*ds`. No `main`, leia a matriz `3 x 3`, chame `resumo_diagonais` e imprima:
```text
Diagonal principal: DP
Diagonal secundaria: DS
```

### `F07-C03` *(Programa completo — Remoção de vogais in-place e comprimento)*
Implemente um programa completo (sem `<string.h>`) com as funções:
```c
void remover_vogais(char s[]);
int tamanho_string(const char s[]);
```
`remover_vogais` deve remover `'a','e','i','o','u'` e `'A','E','I','O','U'` *in-place* (sem vetor auxiliar). `tamanho_string` deve contar os caracteres até `'\0'`. No `main`, leia uma linha com `fgets` em `char s[100]` (removendo `'\n'`/`'\r'`), chame `remover_vogais(s)` e imprima:
```text
Sem vogais: <string_modificada>
Comprimento: L
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `F08` (`Organização Multi-Arquivo .h/.c, Guardas #ifndef e Ligação no GCC`):** somente após autocorreção de `F07-E01..E06` e **100% (3/3)** em `F07-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** revisar a fórmula de endereçamento *row-major* (`i * COL + j`), praticar o padrão de 2 índices + `s[j] = '\0';` no papel e aplicar variante `V2` de `F07`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`F06`** (`const` e passagem de arranjos por valor de endereço), **`E01`/`E04`** (matrizes 2D e diagonais) e **`D07`/`D08`** (percurso de strings até `'\0'`).

---

## 6. Referências do Orientador
- `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 4 (03/11 e 09/11 — Strings e matrizes em funções).
- `[DOC]` `Aula_18_Algoritmos_parte2.pdf` p. 3–10 (passagem de matrizes 2D e strings em funções).
- `[DOC]` `Lista10_Algoritmos.pdf` p. 3 (Ex. 6 — entrega, Ex. 7 — composição e strings/matrizes).
- Casos de teste e soluções verificáveis: [F07_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/gabaritos/F07_gabarito.md) e [F07_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/F07_testes.md).
