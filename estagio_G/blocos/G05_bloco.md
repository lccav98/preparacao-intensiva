# Bloco `G05` — Recursão em Vetores: Parada Antecipada, Máximo Sem Dupla Chamada e Média Recursiva

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio G — Recursividade e Pilha de Execução / **`G05`** |
| **Micro-habilidade foco** | Formular recursões sobre vetores (`const int v[]`) com parada antecipada (`contem` / busca), escolha correta do caso base `n == 1`, cálculo de extremos com **chamada recursiva única** (evitando explosão $O(2^n)$) e média aritmética recursiva `double`. |
| **Pré-requisitos** | `G04` *(Recursão Linear em Vetores 1D: Redução por Tamanho `n - 1`)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 20 min):** `12 min` resol. \| `5 min` corr. \| `3 min` recup.; **Sessão 2 (`E04`–`E06`, 22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `12 min` resol. \| `6 min` conf. |
| **Restrição de escopo** | **Proibição estrita de `for`, `while` e `do-while` em qualquer função recursiva** (laços permitidos apenas em `main` para ler os elementos do vetor). Use capacidade fixa (`int v[50]`), `const int v[]` e redução `n - 1`. **Não utilize** strings (`G06`–`G07`), recursão múltipla Fibonacci/potenciação rápida (`G08`), `struct`, `malloc`/`free` ou VLAs. Saídas estritamente em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Busca com parada antecipada (`contem`):** Possui **dois casos de parada** (sempre testando `n <= 0` antes de ler `v[n - 1]`):
   - Se `n <= 0`: retorna `0` (percorreu todo o subvetor e não encontrou).
   - Se `v[n - 1] == x`: retorna `1` **imediatamente**, interrompendo a descida antes de atingir `n == 0`.
   - Caso contrário: `return contem(v, n - 1, x);`.
2. **Quando usar caso base `n == 1` (e não `n == 0`):** Para **máximo**, **mínimo** e **média**, um vetor vazio (`n == 0`) não tem elemento neutro válido (usar `return 0;` quebraria vetores apenas negativos ou dividiria por zero). Assume-se `n >= 1` com caso base **`if (n == 1) return v[0];`** (em `media`, `(double)v[0]`).
3. **Máximo sem dupla chamada (evitar explosão exponencial $O(2^n)$):**
   - **Erro grave:** escrever `if (v[n - 1] > maior(v, n - 1)) return v[n - 1]; return maior(v, n - 1);` dispara **duas** chamadas recursivas idênticas sempre que `v[n - 1]` não é o maior, podendo gerar $2^n - 1$ chamadas em vetor decrescente!
   - **Forma correta ($O(n)$, exatamente `n` chamadas):** guarde o retorno recursivo em uma **variável local**:
     ```c
     int m = maior(v, n - 1);
     if (v[n - 1] > m) return v[n - 1];
     return m;
     ```
4. **Média aritmética recursiva `double`:** Como a média dos `n - 1` primeiros elementos vale `media(v, n - 1)`, a soma deles é `(n - 1) * media(v, n - 1)`. Somando `v[n - 1]` e dividindo por `n`:
   ```c
   double media(const int v[], int n) {
       if (n == 1) return (double)v[0];
       return ((n - 1) * media(v, n - 1) + v[n - 1]) / n;
   }
   ```
   *(Alternativa igualmente válida: usar uma função auxiliar recursiva `soma(v, n)` e retornar `(double)soma(v, n) / n`.)*

---

## 2. Exemplos Guiados

### Exemplo 1 — Parada antecipada em `contem` vs. chamada única em `maior` *(Trecho ilustrativo)*
```c
int contem(const int v[], int n, int x) {
    if (n <= 0) {
        return 0;                   /* parada 1: esgotou sem achar */
    }
    if (v[n - 1] == x) {
        return 1;                   /* parada 2 (antecipada): achou! */
    }
    return contem(v, n - 1, x);
}

int maior(const int v[], int n) {
    if (n == 1) {
        return v[0];                /* caso base seguro para negativos */
    }
    int m = maior(v, n - 1);        /* UMA unica chamada recursiva */
    if (v[n - 1] > m) {
        return v[n - 1];
    }
    return m;
}
```
Observe: em `maior(v, 4)` sobre `{8, 3, 12, 5}`, ocorrem apenas **4 chamadas** (`n = 4 -> 3 -> 2 -> 1`). Se chamássemos `maior(v, n - 1)` duas vezes, ocorreria uma árvore de chamadas repetidas.

### Exemplo 2 — Média recursiva `double` sem função auxiliar *(Programa completo)*
```c
#include <stdio.h>

double media_vetor(const int v[], int n);

int main(void) {
    int n, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    printf("Media: %.2f\n", media_vetor(v, n));
    return 0;
}

double media_vetor(const int v[], int n) {
    if (n == 1) {
        return (double)v[0];
    }
    return ((n - 1) * media_vetor(v, n - 1) + v[n - 1]) / n;
}
```
Rastreando `v = {10, 20, 30}` (`n = 3`): `media(v, 1) = 10.0` → `media(v, 2) = (1 * 10.0 + 20) / 2 = 15.0` → `media(v, 3) = (2 * 15.0 + 30) / 3 = 20.0`.

---

## 3. Exercícios (`G05-E01` a `G05-E06`)

### Sessão 1 (`G05-E01` a `G05-E03` — Rastreamento, Desempenho e Depuração)

### `G05-E01` *(Teste de mesa — Parada antecipada em `contem` — Papel)*
Sem utilizar computador, considere `int v[5] = {4, 9, 12, 7, 3};` e a função `contem` do Exemplo 1:
- **(a)** Rastreie `contem(v, 5, 12)`, listando cada chamada empilhada, o valor retornado e o **número total de chamadas** executadas.
- **(b)** Rastreie `contem(v, 5, 15)` e compare o número total de chamadas com o item **(a)**.

---

### `G05-E02` *(Análise de explosão de chamadas — 1 vs. 2 chamadas em `maior` — Papel)*
Compare as duas versões abaixo aplicadas ao vetor estritamente decrescente `int v[4] = {40, 30, 20, 10};`:
```c
int maior_A(const int v[], int n) {
    if (n == 1) return v[0];
    int m = maior_A(v, n - 1);
    if (v[n - 1] > m) return v[n - 1];
    return m;
}

int maior_B(const int v[], int n) {
    if (n == 1) return v[0];
    if (v[n - 1] > maior_B(v, n - 1)) return v[n - 1];
    return maior_B(v, n - 1);
}
```
**(a)** Quantas chamadas ocorrem ao todo em `maior_A(v, 4)` e em `maior_B(v, 4)`? *(Desenhe ou conte por nível: `n = 4, 3, 2, 1`).*  
**(b)** Para `n = 20` em um vetor decrescente, quantas chamadas `maior_A` e `maior_B` executam ($2^n - 1$)?

---

### `G05-E03` *(Caça ao Bug — Programa completo `.c`)*
O programa abaixo lê `n` (`1 <= n <= 50`), `n` inteiros e um alvo `x`, e deveria imprimir o maior elemento do vetor e `1`/`0` indicando se `x` ocorre no vetor. Identifique os **bugs** em `maior_vetor` (caso base incorreto para negativos + dupla chamada exponencial) e em `contem` (ordem de teste causando leitura fora dos limites), comente-os com `//` e escreva a versão corrigida completa:

```c
#include <stdio.h>

int maior_vetor(const int v[], int n);
int contem(const int v[], int n, int x);

int main(void) {
    int n, x, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &x);
    printf("Maior: %d\n", maior_vetor(v, n));
    printf("Contem: %d\n", contem(v, n, x));
    return 0;
}

int maior_vetor(const int v[], int n) {
    if (n == 0) {
        return 0;
    }
    if (v[n - 1] > maior_vetor(v, n - 1)) {
        return v[n - 1];
    }
    return maior_vetor(v, n - 1);
}

int contem(const int v[], int n, int x) {
    if (v[n - 1] == x) {
        return 1;
    }
    if (n <= 0) {
        return 0;
    }
    return contem(v, n - 1, x);
}
```

---

### Sessão 2 (`G05-E04` a `G05-E06` — Completar, Variação e Escrita Independente)

### `G05-E04` *(Completar solução e compilar — Média recursiva `.c`)*
Complete as lacunas `/* A */`, `/* B */` e `/* C */` para que o programa leia `n` (`1 <= n <= 50`) e `n` inteiros e calcule a média aritmética `double` de forma puramente recursiva:

```c
#include <stdio.h>

double media_vetor(const int v[], int n);

int main(void) {
    int n, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    printf("Media: %.2f\n", media_vetor(v, n));
    return 0;
}

double media_vetor(const int v[], int n) {
    if ( /* A */ ) {
        return /* B */ ;
    }
    return ( /* C */ ) / n;
}
```

---

### `G05-E05` *(Variação controlada com pistas — Programa completo `.c`)*
Escreva um **programa completo** em C (sem laços nas funções recursivas) com protótipos antes de `main` para:
- `int menor_vetor(const int v[], int n)` — retorna o menor elemento de `v[0..n-1]` (`n >= 1`), usando caso base `n == 1` e **uma única chamada recursiva** armazenada em variável local.
- `int contem(const int v[], int n, int x)` — retorna `1` se `x` estiver em `v[0..n-1]` (com parada antecipada) ou `0` caso contrário.

No `main`, leia `n` (`1 <= n <= 50`), os `n` inteiros e `x`, e imprima exatamente:
```text
Menor: M
Encontrado: Sim
```
(ou `Encontrado: Nao` quando `contem` retornar `0`).  
*Pista:* No `main`, use `if (contem(v, n, x))` para decidir entre `"Sim"` e `"Nao"`.

---

### `G05-E06` *(Resolução independente — Máximo e média recursiva sem laços `.c`)*
Escreva um **programa completo** em C (sem qualquer `for`, `while` ou `do-while` nas funções auxiliares) definindo e implementando:
- `int maior_vetor(const int v[], int n)` — com caso base `n == 1` e chamada recursiva única ($O(n)$).
- `double media_vetor(const int v[], int n)` — média aritmética `double` recursiva.

No `main`, leia `n` (`1 <= n <= 50`) e os `n` inteiros de `v`, e imprima exatamente:
```text
Maior: M
Media: X.XX
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `G05-C01` *(Análise comparativa de custo 1 vs. 2 chamadas — Papel)*
Considere duas implementações para encontrar o menor elemento de `v[0..n-1]` (`n >= 1`) sobre um vetor estritamente **crescente** (pior caso para o teste `<`):
- **Versão 1:** guarda `int m = menor1(v, n - 1);` e depois compara `v[n - 1] < m`.
- **Versão 2:** testa `if (v[n - 1] < menor2(v, n - 1)) return v[n - 1]; return menor2(v, n - 1);`.

**(a)** Quantas chamadas realiza cada versão para `n = 5` e para `n = 10` nesse pior caso?  
**(b)** Por que o caso base deve ser `if (n == 1) return v[0];` em vez de `if (n == 0) return 0;`?

### `G05-C02` *(Busca com parada antecipada — Programa completo `.c`)*
Escreva um **programa completo** em C (sem laços na função recursiva) implementando:
```c
int indice_ultimo(const int v[], int n, int x);
```
que retorna o **maior índice** (`0 <= i < n`) em que `v[i] == x` usando **parada antecipada** a partir do final `v[n - 1]`, ou `-1` caso `x` não esteja presente (ou `n <= 0`). No `main`, leia `n` (`0 <= n <= 50`), os `n` inteiros e `x`, e imprima exatamente:
```text
Indice: I
```

### `G05-C03` *(Média recursiva e contagem filtrada sem laços — Programa completo `.c`)*
Escreva um **programa completo** em C (sem laços nas funções recursivas) implementando:
- `double media_vetor(const int v[], int n)` — média aritmética recursiva para `n >= 1`.
- `int contar_acima(const int v[], int n, double lim)` — conta recursivamente quantos elementos de `v[0..n-1]` são estritamente maiores que `lim`.

No `main`, leia `n` (`1 <= n <= 50`) e os `n` inteiros de `v`, calcule `double m = media_vetor(v, n);` e imprima exatamente:
```text
Media: X.XX
Acima da media: K
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `G06` (`Recursão em Strings por Índice Crescente e Impressão no Retorno`):** somente após autocorreção de `G05-E01..E06` e **100% (3/3)** na Checagem Independente `G05-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** desenhar a árvore de chamadas da dupla chamada em `maior` para `n = 4` destacando as subárvores duplicadas, revisar a derivação algébrica da média ponderada `((n - 1) * media(v, n - 1) + v[n - 1]) / n` e aplicar variante `V2` de `G05`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`G04`** (redução `n - 1` e ordem do caso base antes de `v[n - 1]`) e **`B01`–`B02`** (conversão explícita `(double)` para evitar divisão inteira).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 10 — recursão: definições e exemplos).
- `[DOC]` `Aula_22_Algoritmos.pdf` p. 29–32 (`contem` com parada antecipada e busca/máximo em vetores).
- `[DOC]` `Lista11_Algoritmos.pdf` p. 2–3 (Ex. 7 — `maior` evitando dupla chamada exponencial; Ex. 8 — entrega `media` recursiva, adaptada de K. N. King, Cap. 9, Ex. 10).
- Casos de teste e soluções verificáveis: [G05_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/gabaritos/G05_gabarito.md) e [G05_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/G05_testes.md).
