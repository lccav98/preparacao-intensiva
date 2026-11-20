# Bloco `G02` — Ordem de Execução na Pilha: Pré-Recursão vs. Pós-Recursão

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio G — Recursividade e Pilha de Execução / **`G02`** |
| **Micro-habilidade foco** | Prever exatamente a saída de funções recursivas `void` diferenciando instruções executadas na descida (pré-recursão) e na subida/retorno (pós-recursão), comparando recursão com iteração e implementando pequenas funções recursivas sem laços. |
| **Pré-requisitos** | `G01` *(Conceito de Recursividade e Pilha de Execução)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem (20 min):** `12 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 15 min):** `10 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Proibição absoluta de laços (`for`, `while`, `do-while`) dentro de funções recursivas.** Utilize apenas funções `void` recursivas sobre inteiros simples, sem decomposição decimal `% 10` / `/ 10` (`G03`), sem vetores (`G04`), sem strings (`G06`), sem recursão múltipla (`G08`), sem `struct`, `malloc`/`free` ou VLAs. Saídas estritamente em ASCII puro. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Execução pré-recursiva (descida / ida):** Toda instrução colocada **antes** da chamada recursiva executa **imediatamente** antes de empilhar a próxima chamada. Como `n` vai diminuindo (`3, 2, 1`), a saída sai em ordem **decrescente** (da primeira chamada até o caso base).
2. **Execução pós-recursiva (subida / volta):** Toda instrução colocada **depois** da chamada recursiva fica **suspensa** no quadro da pilha enquanto as chamadas mais internas executam. Ela só roda quando a chamada interna retorna, desempilhando na ordem **inversa** (`1, 2, 3`, do caso base de volta à chamada inicial).
3. **Dupla saída (pré + pós):** Quando uma função `void` possui `printf` antes **e** depois da chamada recursiva, ela produz um efeito espelhado: primeiro todas as impressões de ida, depois o caso base, e por fim todas as impressões de volta (ex.: `A3 A2 A1 B1 B2 B3` ou `3 2 1 1 2 3`).
4. **Iteração × Recursão:**
   - **Iteração (`for`/`while`):** mantém um único quadro de memória e altera uma variável contadora até a condição do laço falhar.
   - **Recursão:** cria um novo quadro na pilha por chamada e encerra no caso base. Para imprimir em ordem invertida (ex.: `1..n` a partir de `n`), a **pós-recursão** aproveita a própria pilha de execução sem exigir vetor auxiliar.

---

## 2. Exemplos Guiados

### Exemplo 1 — Dupla saída pré-recursiva e pós-recursiva *(Trecho ilustrativo)*
```c
void mostrar(int n) {
    if (n <= 0) {
        return;             /* caso base: interrompe a descida */
    }
    printf("A%d ", n);      /* pre-recursao: executa na descida */
    mostrar(n - 1);         /* chamada recursiva */
    printf("B%d ", n);      /* pos-recursao: executa na subida */
}
```
Rastreando `mostrar(3)`:
- **Descida:** imprime `A3 `, empilha `mostrar(2)` → imprime `A2 `, empilha `mostrar(1)` → imprime `A1 `, empilha `mostrar(0)` → caso base retorna.
- **Subida:** `mostrar(1)` retoma e imprime `B1 ` → `mostrar(2)` retoma e imprime `B2 ` → `mostrar(3)` retoma e imprime `B3 `.
- **Saída exata:** `A3 A2 A1 B1 B2 B3 `

### Exemplo 2 — Iteração × Recursão para imprimir `1 2 3 4` *(Programa completo)*
```c
#include <stdio.h>

void imprimir_crescente(int n);

int main(void) {
    int n;
    scanf("%d", &n);
    imprimir_crescente(n);
    printf("\n");
    return 0;
}

void imprimir_crescente(int n) {
    if (n <= 0) {
        return;
    }
    imprimir_crescente(n - 1);
    if (n > 1) {
        printf(" ");
    }
    printf("%d", n);
}
```
Observe: para `n = 4`, as chamadas descem `4 -> 3 -> 2 -> 1 -> 0` sem imprimir nada. Na volta da pilha, `n = 1` imprime `1`, `n = 2` imprime ` 2`, `n = 3` imprime ` 3` e `n = 4` imprime ` 4`, sem nenhum laço `for`/`while` e sem espaço extra no final.

---

## 3. Exercícios (`G02-E01` a `G02-E05`)

### `G02-E01` *(Teste de mesa — Pré, Pós e Dupla Saída — Papel)*
Sem utilizar computador, determine a saída exata de cada chamada considerando as 3 funções abaixo:
```c
void f_pre(int n) {
    if (n <= 0) return;
    printf("%d ", n);
    f_pre(n - 1);
}

void f_pos(int n) {
    if (n <= 0) return;
    f_pos(n - 1);
    printf("%d ", n);
}

void f_dupla(int n) {
    if (n <= 0) return;
    printf("%d ", n);
    f_dupla(n - 1);
    printf("%d ", n);
}
```
**(a)** `f_pre(4);`  
**(b)** `f_pos(4);`  
**(c)** `f_dupla(3);` *(indique em que momento `f_dupla(0)` retorna e qual `printf` executa logo em seguida).*

---

### `G02-E02` *(Comparação Iteração × Recursão — Papel)*
Considere duas maneiras de exibir os inteiros de `1` até `n` (`n >= 1`):
- **Versão A (iterativa):** `for (int i = 1; i <= n; i++) printf("%d ", i);`
- **Versão B (recursiva):** `imprimir_crescente(n)` do Exemplo 2.

**(a)** Compare as duas versões quanto a: (1) mecanismo que gera repetição, (2) condição de parada e (3) uso de memória em quadros de ativação.  
**(b)** Na Versão B, se trocarmos a ordem das linhas colocando `printf("%d", n);` **antes** de `imprimir_crescente(n - 1);`, o que muda na saída para `n = 4`?

---

### `G02-E03` *(Caça ao Bug — Programa completo `.c`)*
O programa completo abaixo deveria ler `n` e imprimir a sequência espelhada `n ... 1 1 ... n` (ex.: para `n = 3`, imprimir `3 2 1 1 2 3`). Identifique os **2 bugs intencionais** em `espelho`, explique-os em comentários `//` diretamente no código e apresente o programa corrigido sem laços:

```c
#include <stdio.h>

void espelho(int n);

int main(void) {
    int n;
    scanf("%d", &n);
    espelho(n);
    printf("\n");
    return 0;
}

void espelho(int n) {
    printf("%d ", n);
    if (n > 1) {
        printf(" ");
    }
    printf("%d", n);
    espelho(n - 1);
}
```

---

### `G02-E04` *(Completar solução e compilar — Programa completo `.c`)*
Complete as lacunas `/* A */`, `/* B */` e `/* C */` para que o programa leia `n` (`n >= 0`) e imprima o padrão `A<n> ... A1 B1 ... B<n>` (ex.: para `n = 3`, imprime `A3 A2 A1 B1 B2 B3`; para `n <= 0`, imprime apenas a quebra de linha):

```c
#include <stdio.h>

void sequencia_ab(int n);

int main(void) {
    int n;
    scanf("%d", &n);
    sequencia_ab(n);
    printf("\n");
    return 0;
}

void sequencia_ab(int n) {
    /* A */
    printf("A%d ", n);
    /* B */
    if (n > 1) {
        printf(" ");
    }
    /* C */
}
```

---

### `G02-E05` *(Resolução independente — Programa completo `.c`)*
Escreva um **programa completo** em C (sem qualquer `for`, `while` ou `do-while` nas funções auxiliares) com protótipos antes de `main` para duas funções recursivas:
- `void contar_regressivo(int n)` — imprime de `n` até `1` separados por espaço simples (sem espaço extra ao final).
- `void contar_progressivo(int n)` — imprime de `1` até `n` separados por espaço simples (sem espaço extra ao final).

No `main`, leia `n` (`n >= 0`) e imprima exatamente (se `n <= 0`, não imprima números após os dois-pontos):
```text
Regressivo: 4 3 2 1
Progressivo: 1 2 3 4
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `G02-C01` *(Teste de mesa — Só pré-recursão e só pós-recursão, 4 níveis)*
Sem usar computador, escreva a saída exata de cada chamada:
```c
void ida(int n) {
    if (n <= 0) return;
    printf("I%d ", n);
    ida(n - 1);
}

void volta(int n) {
    if (n <= 0) return;
    volta(n - 1);
    printf("V%d ", n);
}
```
**(a)** `ida(4);`  
**(b)** `volta(4);`

### `G02-C02` *(Teste de mesa — Dupla saída pré+pós com 4 níveis)*
Sem usar computador, rastreie `eco(4)` mostrando a pilha na descida e na subida, e escreva a saída exata gerada pela função abaixo:
```c
void eco(int n) {
    if (n <= 0) {
        printf("|");
        return;
    }
    printf("%d ", n);
    eco(n - 1);
    printf(" %d", n);
}
```

### `G02-C03` *(Pequena função `.c` — Dupla saída recursiva sem laços)*
Escreva um **programa completo** em C (sem laços) com protótipo e implementação da função:
```c
void pulso(int n);
```
Dado um inteiro `n` (`n >= 0`), `pulso(n)` deve imprimir em uma única linha (com `\n` em `main`) os valores descendo de `n` até `0` e subindo de `1` até `n`, separados por espaço simples. Exemplos:
- Para `n = 3`: `3 2 1 0 1 2 3`
- Para `n = 0`: `0`
- Para `n <= 0`: imprime `0` (caso base `if (n <= 0) { printf("0"); return; }`).

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `G03` (`Recursão Linear sobre Inteiros e Decomposição Decimal`):** somente após autocorreção de `G02-E01..E05` e **100% (3/3)** na Checagem Independente `G02-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** marcar com setas `↓` (antes da chamada) e `↑` (depois da chamada) no código de cada função, simular passo a passo com fichas na mesa e aplicar variante `V2` de `G02`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar o pré-requisito **`G01`** (empilhamento de quadros e regra *"a chamada mais recente termina primeiro"*).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 10 — recursão: definições e exemplos).
- `[DOC]` `Aula_21_Algoritmos.pdf` p. 21–24, 27 (`mostrar`, execução antes vs. depois da chamada recursiva).
- `[DOC]` `Aula_22_Algoritmos.pdf` p. 15–22 (revisão da pilha com `mostrar` e comparação iteração × recursão).
- `[DOC]` `Lista11_Algoritmos.pdf` p. 1 (Ex. 1 — rastreamento de saída pré e pós-recursão).
- Casos de teste e soluções verificáveis: [G02_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/gabaritos/G02_gabarito.md) e [G02_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/G02_testes.md).
