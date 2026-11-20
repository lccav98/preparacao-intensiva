# Bloco `F05` — Ponteiros como Parâmetros, Múltiplos Resultados e Depuração de Ponteiros

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio F — Modularização, Funções, Ponteiros e Compilação Multi-Arquivo / **`F05`** |
| **Micro-habilidade foco** | Passar endereços por valor (`func(&x)`) para modificar variáveis do chamador ou devolver múltiplos resultados por parâmetros de saída, além de repassar e depurar ponteiros entre funções. |
| **Pré-requisitos** | `F04` *(Introdução a ponteiros: `&`, `*`, `NULL`, desreferenciamento e rastreamento de memória)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Sessão 2 (`E04`–`E06`, 24 min):** `15 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Não utilize** vetores, matrizes ou strings como parâmetros de função (tópicos de `F06`–`F07`), múltiplos arquivos `.h`/`.c` (`F08`) ou recursividade (`G01`). Utilize apenas escalares (`int`, `double`) e ponteiros para escalares (`int *`, `double *`) com protótipos antes de `main`. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Regra fundamental em C:** Todos os argumentos são passados **por valor** (cópia). Quando uma função recebe `int *p`, ela recebe uma **cópia do endereço** da variável original (`&var`).
2. **Alterar `p` vs. alterar `*p`:**
   - Alterar `p` (`p = NULL;`) modifica **apenas a cópia local** do ponteiro dentro da função; o chamador não é afetado.
   - Alterar `*p` (`*p = 20;`) escreve diretamente **na variável original** no endereço apontado.
3. **Repasse entre funções:** Se `funcA(int *p)` chama `funcB(int *q)` passando o mesmo alvo, `p` **já armazena um endereço**. Portanto `funcA` chama `funcB(p);` (**sem `&`**!). Usar `&p` passaria o endereço do próprio ponteiro `p` (`int **`), o que é erro de tipo.
4. **Quando usar retorno vs. ponteiro de saída:**
   - 1 resultado calculado sem alterar variáveis externas → prefira `return`.
   - 2 ou mais resultados simultâneos (ou troca/atualização *in-place*) → use **parâmetros de saída** (`int *`, `double *`).
5. **Erro clássico em `trocar`:** `int *aux; *aux = *a;` tenta gravar em endereço indeterminado (**comportamento indefinido**). A variável temporária guarda um **valor**, logo deve ser `int aux = *a;`.

---

## 2. Exemplos Guiados

### Exemplo 1 — Repasse de ponteiros e alteração de `*p` vs `p` *(Trecho ilustrativo)*
```c
void somar_bonus(int *nota, int extra) {
    *nota = *nota + extra;   /* altera a variavel original no chamador */
    nota = NULL;             /* altera apenas a copia local do ponteiro */
}

void aplicar(int *alvo) {
    somar_bonus(alvo, 15);   /* alvo JA eh int *, nao usa '&' */
}
/* Em main: int pts = 70; aplicar(&pts); -> pts passa a valer 85 */
```

### Exemplo 2 — Devolvendo múltiplos resultados via parâmetros de saída *(Programa completo)*
```c
#include <stdio.h>

void quadrado_e_cubo(int n, int *quad, int *cubo);

int main(void) {
    int x, q, c;
    scanf("%d", &x);

    quadrado_e_cubo(x, &q, &c);
    printf("Quadrado: %d\nCubo: %d\n", q, c);
    return 0;
}

void quadrado_e_cubo(int n, int *quad, int *cubo) {
    *quad = n * n;
    *cubo = n * n * n;
}
```
Observe: `x` entra por valor (leitura), enquanto `&q` e `&c` fornecem os endereços onde a função grava os dois resultados.

---

## 3. Exercícios (`F05-E01` a `F05-E06`)

### Sessão 1 (`F05-E01` a `F05-E03` — Leitura, Lacunas e Depuração)

### `F05-E01` *(Leitura e Teste de Mesa — Reprodução do modelo)*
Sem utilizar computador, acompanhe o programa completo abaixo:

```c
#include <stdio.h>

void trocar(int *a, int *b);
void ordenar_par(int *x, int *y);

int main(void) {
    int u, v;
    scanf("%d %d", &u, &v);
    ordenar_par(&u, &v);
    printf("%d %d\n", u, v);
    return 0;
}

void trocar(int *a, int *b) {
    int aux = *a;
    *a = *b;
    *b = aux;
}

void ordenar_par(int *x, int *y) {
    if (*x > *y) {
        trocar(x, y);
    }
}
```
**(a)** Qual é a saída impressa para as entradas `12 5` e `4 9`?  
**(b)** Por que `main` chama `ordenar_par(&u, &v)` usando `&`, enquanto `ordenar_par` chama `trocar(x, y)` **sem `&`**?

---

### `F05-E02` *(Completar solução)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` para que a função `dividir_inteiro` grave o quociente e o resto de `a / b` (`b != 0`) nas variáveis de `main`:

```c
#include <stdio.h>

void dividir_inteiro(int a, int b, /* A */ , /* B */ );

int main(void) {
    int x = 23, y = 5, q, r;
    dividir_inteiro(x, y, /* C */ );
    printf("Quociente: %d\nResto: %d\n", q, r);
    return 0;
}

void dividir_inteiro(int a, int b, int *quoc, int *resto) {
    /* D */
}
```

---

### `F05-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler dois inteiros `x` e `y`, trocá-los usando `trocar` e exibir `x` e `y` trocados. Identifique o bug fatal dentro de `trocar`, corrija o programa completo e explique o erro e a correção usando **comentários `//` diretamente no código**:

```c
#include <stdio.h>

void trocar(int *a, int *b);

int main(void) {
    int x, y;
    scanf("%d %d", &x, &y);
    trocar(&x, &y);
    printf("%d %d\n", x, y);
    return 0;
}

void trocar(int *a, int *b) {
    int *aux;
    *aux = *a;
    *a = *b;
    *b = *aux;
}
```

---

### Sessão 2 (`F05-E04` a `F05-E06` — Escrita Guiada → Independente)

### `F05-E04` *(Variação controlada com pistas)*
Escreva um **programa completo** em C com protótipo antes de `main` para a função:
```c
void soma_e_diferenca(int a, int b, int *soma, int *dif);
```
No `main`, leia dois inteiros `a` e `b`, chame `soma_e_diferenca` para armazenar `a + b` em `*soma` e `a - b` em `*dif`, e imprima exatamente:
```text
Soma: X
Diferenca: Y
```
*Pista:* Em `main`, passe as variáveis de saída com `&` (`&s, &d`).

---

### `F05-E05` *(Variação controlada com pistas)*
Escreva um **programa completo** em C que declare e implemente a função:
```c
void extremos_tres(int a, int b, int c, int *menor, int *maior);
```
A função deve determinar o menor e o maior entre os três inteiros `a`, `b` e `c` e gravá-los em `*menor` e `*maior`. No `main`, leia os três inteiros e imprima:
```text
Menor: X
Maior: Y
```
*Pista:* Inicialize `*menor = a;` e `*maior = a;` dentro da função e compare `b` e `c` usando `if`s independentes.

---

### `F05-E06` *(Resolução independente)*
Escreva um **programa completo** em C contendo o protótipo e a implementação da função:
```c
void decompor_tempo(int total_seg, int *h, int *m, int *s);
```
Dado um total não-negativo de segundos `total_seg`, a função deve calcular as horas inteiras (`*h`), minutos restantes (`*m`, `0..59`) e segundos restantes (`*s`, `0..59`). No `main`, leia `total_seg`, chame a função e imprima exatamente:
```text
H h, M min, S s
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `F05-C01` *(Teste de Mesa)*
Sem usar computador, execute o rastreamento do programa abaixo e responda:

```c
#include <stdio.h>

void atualizar(int *p, int k);
void aplicar_dobro(int *q);

int main(void) {
    int saldo = 15;
    aplicar_dobro(&saldo);
    printf("%d\n", saldo);
    return 0;
}

void atualizar(int *p, int k) {
    *p = *p + k;
    p = NULL;
}

void aplicar_dobro(int *q) {
    int val = *q;
    atualizar(q, val);
}
```
**(a)** Qual valor é impresso por `main`?  
**(b)** Por que `atualizar(q, val)` não usa `&q` e por que a linha `p = NULL;` dentro de `atualizar` não zera `q` nem `saldo`?

### `F05-C02` *(Caça ao Bug — Programa completo)*
O programa abaixo parte de `saldo = 100`, lê dois valores inteiros `x` e `y` e deveria somar ambos a `saldo` por meio de duas chamadas a `acumular`, exibindo `Saldo: S`. Corrija todos os erros presentes:

```c
#include <stdio.h>

void acumular(int *total, int valor);

int main(void) {
    int saldo = 100, x, y;
    scanf("%d %d", &x, &y);
    acumular(saldo, x);
    acumular(saldo, y);
    printf("Saldo: %d\n", saldo);
    return 0;
}

void acumular(int *total, int valor) {
    total = total + valor;
}
```

### `F05-C03` *(Programa completo independente)*
Declare e implemente a função:
```c
void retangulo(double base, double altura, double *area, double *perimetro);
```
No `main`, leia dois valores reais (`double`) representando `base` e `altura`, chame `retangulo` e imprima exatamente:
```text
Area: A.AA
Perimetro: P.PP
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `F06` (`Funções com Vetores 1D e const`):** somente após autocorreção de `F05-E01..E06` e **100% (3/3)** em `F05-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** desenhar caixas de memória com endereços simbólicos (`0x100`, `0x104`, `0x200`) diferenciando `p` (endereço) de `*p` (conteúdo apontado) e aplicar variante `V2` de `F05`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`F04`** (declaração/desreferenciamento de ponteiros e inicialização) e **`F03`** (cópia local na passagem por valor).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 9 — parâmetros, argumentos, desvio de chamada).
- `[DOC]` `Aula_17_Algoritmos.pdf` p. 24, 35–36, 39; `Aula_18_Algoritmos.pdf` p. 3–14, 32–35 (Ex. 1, 3, 4).
- `[DOC]` `Lista10_Algoritmos.pdf` p. 2 (Ex. 3 — entrega comentada, Ex. 4 — repasse de ponteiros).
- Casos de teste e soluções verificáveis: [F05_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/gabaritos/F05_gabarito.md) e [F05_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/F05_testes.md).
