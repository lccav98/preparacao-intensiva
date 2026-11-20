# Bloco `F06` — Funções com Vetores 1D e Modificador `const`

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio F — Modularização, Funções, Ponteiros e Compilação Multi-Arquivo / **`F06`** |
| **Micro-habilidade foco** | Passar vetores 1D (`int v[], int n`) para funções compreendendo o decaimento para o endereço do 1º elemento (sem cópia integral), protegendo leituras com `const` e combinando com parâmetros de saída por ponteiro. |
| **Pré-requisitos** | `F05` *(Ponteiros como parâmetros, múltiplos resultados e depuração de ponteiros)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão (`E01`–`E05`, 24 min):** `14 min` resol. \| `6 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Não utilize** matrizes 2D em parâmetros (`m[][COL]`), funções *in-place* em strings (`F07`), organização multi-arquivo `.h`/`.c` (`F08`), recursividade (`G01`), `struct`, alocação dinâmica (`malloc`/`free`) ou VLAs. Utilize vetores 1D de capacidade fixa e protótipos antes de `main`. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Decaimento do vetor na chamada:** Quando você passa o nome de um vetor (`func(v, n);`), C **não copia** todos os elementos. O nome `v` decai para o **endereço do primeiro elemento** (`&v[0]`), e esse endereço é passado **por valor** (cópia do endereço) para a função.
2. **Equivalência de parâmetros (`int v[]` ≡ `int *v`):** Na lista de parâmetros de uma função, `int v[]` e `int *v` significam exatamente a mesma coisa para o compilador: um ponteiro local que recebe a cópia do endereço inicial do vetor.
   - Alterar `v[i]` dentro da função **modifica o vetor original** no chamador.
   - Alterar o próprio ponteiro `v` (`v = NULL;`) modifica **apenas a cópia local** do ponteiro; o vetor do chamador permanece intacto.
3. **Passagem obrigatória do tamanho `n`:** Como a função recebe apenas o endereço inicial (e `sizeof(v)` dentro da função mede o tamanho de um ponteiro, não do vetor!), você **sempre** deve passar o número de elementos válidos `n` como parâmetro (`int n`). Passar `n` maior que a quantidade real de elementos gera leitura fora dos limites (*comportamento indefinido*).
4. **Contrato de somente leitura (`const int v[]`):** Se a função apenas consulta os elementos do vetor (ex.: soma, média, busca, impressão), declare o parâmetro como **`const int v[]`**. Qualquer tentativa de alterar `v[i]` dentro dessa função será barrada pelo compilador.
5. **Combinação com parâmetros de saída:** Para devolver múltiplos resumos de um vetor (ex.: soma, menor, maior e média), passe o vetor como `const int v[], int n` e os resultados por ponteiros de saída (`int *`, `double *`).

---

## 2. Exemplos Guiados

### Exemplo 1 — Escalar vs. vetor 1D e uso de `const` *(Trecho ilustrativo)*
```c
void tentar_alterar(int x) {
    x = 99; /* altera apenas a copia local de x */
}

void zerar_primeiro(int v[], int n) {
    if (n > 0) {
        v[0] = 0; /* altera o vetor original via copia do endereco */
    }
    v = NULL;     /* altera apenas o ponteiro local v */
}

int somar_elementos(const int v[], int n) {
    int s = 0;
    for (int i = 0; i < n; i++) {
        s += v[i];
    }
    /* v[0] = 10; -> ERRO de compilacao por causa de const! */
    return s;
}
```

### Exemplo 2 — Vetor com `const` e múltiplos resultados por ponteiro *(Programa completo)*
```c
#include <stdio.h>

void extremos_vetor(const int v[], int n, int *menor, int *maior);

int main(void) {
    int n, v[50], mn, mx;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    extremos_vetor(v, n, &mn, &mx);
    printf("Menor: %d\nMaior: %d\n", mn, mx);
    return 0;
}

void extremos_vetor(const int v[], int n, int *menor, int *maior) {
    *menor = v[0];
    *maior = v[0];
    for (int i = 1; i < n; i++) {
        if (v[i] < *menor) *menor = v[i];
        if (v[i] > *maior) *maior = v[i];
    }
}
```
Observe: `v` entra sem `&` (decaimento para `&v[0]`) protegido por `const`, enquanto `mn` e `mx` precisam de `&` porque são variáveis escalares de saída.

---

## 3. Exercícios (`F06-E01` a `F06-E05`)

### `F06-E01` *(Análise Comparativa e Teste de Mesa — Reprodução do modelo)*
Sem utilizar computador, acompanhe o programa completo abaixo:

```c
#include <stdio.h>

void tentar_dobrar(int x);
void dobrar_vetor(int v[], int n);

int main(void) {
    int a = 10;
    int vet[3] = {2, 4, 6};

    tentar_dobrar(a);
    dobrar_vetor(vet, 3);

    printf("a = %d\n", a);
    printf("vet = %d %d %d\n", vet[0], vet[1], vet[2]);
    return 0;
}

void tentar_dobrar(int x) {
    x = x * 2;
}

void dobrar_vetor(int v[], int n) {
    for (int i = 0; i < n; i++) {
        v[i] = v[i] * 2;
    }
    v = NULL;
}
```
**(a)** Qual é a saída exata impressa por `main`?  
**(b)** Explique por que `a` permaneceu inalterado enquanto `vet` foi modificado, mesmo sabendo que em C toda passagem de argumento é **por valor**, e por que `v = NULL;` não apagou `vet` em `main`.

---

### `F06-E02` *(Completar solução — `const` e parâmetros de saída)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` para que a função `estatisticas` leia o vetor com proteção `const` e grave a soma e a média real em `main`:

```c
#include <stdio.h>

void estatisticas( /* A */ , int n, /* B */ );

int main(void) {
    int dados[4] = {10, 15, 20, 25};
    int s;
    double m;

    estatisticas(dados, 4, /* C */ );
    printf("Soma: %d\nMedia: %.2f\n", s, m);
    return 0;
}

void estatisticas( /* A */ , int n, /* B */ ) {
    int total = 0;
    /* D */
}
```

---

### `F06-E03` *(Caça ao Bug — Programa completo)*
O programa abaixo deveria ler `n` (`1 <= n <= 50`), ler `n` inteiros para `v`, ler `lim` e contar quantos elementos de `v` são estritamente maiores que `lim`, imprimindo `Acima: K`. Identifique os **2 erros intencionais** (`const` e limite `n`), corrija o programa completo e explique cada erro usando **comentários `//` diretamente no código**:

```c
#include <stdio.h>

int contar_acima(const int v[], int n, int limite);

int main(void) {
    int n, lim, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &lim);
    printf("Acima: %d\n", contar_acima(v, n + 1, lim));
    return 0;
}

int contar_acima(const int v[], int n, int limite) {
    int cont = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] > limite) {
            cont++;
        }
        v[i] = 0;
    }
    return cont;
}
```

---

### `F06-E04` *(Variação controlada com pistas)*
Escreva um **programa completo** em C com protótipo antes de `main` para a função:
```c
int produto_interno(const int a[], const int b[], int n);
```
A função deve calcular e retornar o produto interno $\sum_{i=0}^{n-1} a[i] \cdot b[i]$. No `main`, leia `n` (`1 <= n <= 50`), os `n` inteiros de `a` e os `n` inteiros de `b`, chame `produto_interno` e imprima exatamente:
```text
Produto interno: P
```
*Pista:* Ambos os vetores são somente leitura (`const int []`). Inicialize `int soma = 0;` dentro da função e acumule `a[i] * b[i]`.

---

### `F06-E05` *(Resolução independente)*
Escreva um **programa completo** em C contendo os protótipos e as implementações de duas funções:
1. `void substituir_negativos(int v[], int n);` — substitui por `0` todos os elementos negativos de `v` (*in-place*).
2. `void imprimir_vetor(const int v[], int n);` — imprime os `n` elementos de `v` em uma única linha separados por espaço simples, finalizando com `\n`.

No `main`, leia `n` (`1 <= n <= 50`) e `n` inteiros em `v[50]`, chame `substituir_negativos(v, n)` e em seguida `imprimir_vetor(v, n)`.

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `F06-C01` *(Teste de Mesa e Análise)*
Sem usar computador, analise o trecho abaixo:
```c
#include <stdio.h>

void ajustar(int x, int v[], int n);

int main(void) {
    int x = 5;
    int v[3] = {10, 20, 30};
    ajustar(x, v, 3);
    printf("x=%d v[0]=%d\n", x, v[0]);
    return 0;
}

void ajustar(int x, int v[], int n) {
    if (n > 0) {
        x = 99;
        v[0] = 99;
    }
    v = NULL;
}
```
**(a)** Qual linha é impressa por `main`?  
**(b)** Explique por que `v[0]` mudou e `x` não mudou, por que `v = NULL;` não afetou `main` e se substituir `int v[]` por `int *v` no protótipo e na definição mudaria o comportamento do programa.

### `F06-C02` *(Caça ao Bug — Programa completo)*
O programa abaixo deveria ler `n` (`1 <= n <= 50`) e `n` inteiros e imprimir `Soma pares: S`. Identifique e corrija todos os bugs presentes:

```c
#include <stdio.h>

int soma_pares(const int v[], int n);

int main(void) {
    int n, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    printf("Soma pares: %d\n", soma_pares(v, n));
    return 0;
}

int soma_pares(const int v[], int n) {
    int soma = 0;
    for (int i = 0; i <= n; i++) {
        if (v[i] % 2 != 0) {
            v[i] = 0;
        }
        soma += v[i];
    }
    return soma;
}
```

### `F06-C03` *(Programa completo independente)*
Declare e implemente a função:
```c
void estatisticas_vetor(const int v[], int n, int *menor, int *maior, double *media);
```
No `main`, leia `n` (`1 <= n <= 50`) e `n` inteiros em `v[50]`, chame `estatisticas_vetor` e imprima exatamente:
```text
Menor: X
Maior: Y
Media: M.MM
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `F07` (`Funções com Matrizes 2D, Strings In-Place e Composição`):** somente após autocorreção de `F06-E01..E05` e **100% (3/3)** em `F06-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** revisar a diferença entre copiar um escalar e passar o endereço de `v[0]` por valor, praticar declarações com `const int v[]` e aplicar variante `V2` de `F06`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`F05`** (passagem de endereços por valor e parâmetros de saída) e **`D02`** (acumulação e extremos em vetores 1D).

---

## 6. Referências do Orientador
- `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 4 (09/11 — Passagem de vetores e matrizes por parâmetro).
- `[DOC]` `Aula_18_Algoritmos.pdf` p. 15–31, 33 (Ex. 2 — vetores como parâmetros, decaimento e `const`).
- `[DOC]` `Lista10_Algoritmos.pdf` p. 1–2 (Ex. 2 — escalar vs. vetor, Ex. 5 — `estatisticas`).
- Casos de teste e soluções verificáveis: [F06_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/gabaritos/F06_gabarito.md) e [F06_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/F06_testes.md).
