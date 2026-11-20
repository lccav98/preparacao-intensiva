# Bloco `G03` — Recursão Linear sobre Inteiros (Sem Laços) e Decomposição Decimal

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio G — Recursividade e Pilha de Execução / **`G03`** |
| **Micro-habilidade foco** | Projetar e implementar funções recursivas lineares sobre inteiros **sem qualquer estrutura de repetição**, tratando corretamente decomposição decimal (`% 10`, `/ 10`), casos base (`n < 10` vs. `n == 0`) e argumento de terminação. |
| **Pré-requisitos** | `G02` *(Ordem de Execução na Pilha: Pré-Recursão vs. Pós-Recursão)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem (22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 16 min):** `11 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Proibição estrita de `for`, `while` e `do-while` em qualquer função recursiva.** Utilize apenas recursão linear sobre inteiros (`int`), sem vetores (`G04`), sem strings (`G06`), sem recursão múltipla ou divisão pela metade (`G08`), sem `struct`, `malloc`/`free` ou VLAs. Saídas estritamente em ASCII puro. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Proibição de laços em funções recursivas:** Toda repetição deve ocorrer por meio de chamadas recursivas com argumento menor. **Nunca** utilize `for`, `while` ou `do-while` dentro de uma função recursiva.
2. **Recorrência matemática → Código C (`potencia(x, n)` para $n \ge 0$):**
   - Caso base: $P(x, 0) = 1 \implies$ `if (n == 0) return 1;`
   - Passo recursivo: $P(x, n) = x \cdot P(x, n - 1) \implies$ `return x * potencia(x, n - 1);`
3. **Decomposição decimal recursiva (`% 10` e `/ 10`):**
   - `n % 10` isola o dígito das unidades; `n / 10` remove o último dígito.
   - **Cuidado crítico com a entrada `0` (`n < 10` vs. `n == 0`):**
     - Ao **contar dígitos**, o número `0` possui **1 dígito**. Usar `if (n == 0) return 0;` gera resposta `0` errada para a entrada `0`! O caso base correto é **`if (n < 10) return 1;`** (todo inteiro `0..9` tem 1 dígito, e `10..` cai nele após divisões por `10`).
     - Ao **contar ocorrências de um dígito específico** (ex.: contar zeros), testar `if (n == 0) return 1;` faria `15 / 10 -> 1 / 10 -> 0` somar um zero fantasma à esquerda! Por isso, use também **`if (n < 10)`** para distinguir `n == 0` dos dígitos `1..9`.
4. **Justificativa de terminação para todo $n \ge 0$:**
   - Para `n - 1`: se `n > 0`, o novo argumento `n - 1` é inteiro não-negativo estritamente menor que `n`; em passos finitos atinge `0` (caso base).
   - Para `n / 10`: se `n >= 10`, então $1 \le \lfloor n / 10 \rfloor < n$; logo a sequência decresce estritamente até entrar no caso base `0 <= n < 10`.

---

## 2. Exemplos Guiados

### Exemplo 1 — Soma recursiva de dígitos e prova de terminação *(Trecho ilustrativo)*
```c
int soma_digitos(int n) {
    if (n < 10) {
        return n;
    }
    return (n % 10) + soma_digitos(n / 10);
}
```
- Rastreamento para `soma_digitos(5832)`:
  - `5832` (`>= 10`): `2 + soma_digitos(583)`
  - `583` (`>= 10`): `3 + soma_digitos(58)`
  - `58` (`>= 10`): `8 + soma_digitos(5)`
  - `5` (`< 10`): retorna `5` → `8 + 5 = 13` → `3 + 13 = 16` → `2 + 16 = 18`.
- Terminação ($n \ge 0$): enquanto $n \ge 10$, o passo chama `n / 10`, que satisfaz $0 < \lfloor n / 10 \rfloor < n$; em número finito de divisões entra no intervalo $0 \le n < 10$ e para no caso base.

### Exemplo 2 — Contagem segura de dígitos tratando `n = 0` *(Programa completo)*
```c
#include <stdio.h>

int contar_digitos(int n);

int main(void) {
    int n;
    scanf("%d", &n);
    printf("Digitos: %d\n", contar_digitos(n));
    return 0;
}

int contar_digitos(int n) {
    if (n < 10) {
        return 1;
    }
    return 1 + contar_digitos(n / 10);
}
```
Observe: para `n = 0`, `0 < 10` é verdadeiro e devolve `1` imediatamente; para `n = 407`, desce `407 -> 40 -> 4` (retorna `1`) e soma `1 + 1 + 1 = 3`.

---

## 3. Exercícios (`G03-E01` a `G03-E05`)

### `G03-E01` *(Rastreamento e justificativa de terminação — Papel)*
Sem utilizar computador, analise a função abaixo:
```c
int misterio(int n) {
    if (n < 10) {
        return n;
    }
    return (n % 10) + misterio(n / 10);
}
```
**(a)** Rastreie `misterio(5832)` mostrando cada chamada empilhada e cada valor retornado na subida.  
**(b)** Escreva uma justificativa curta explicando por que `misterio(n)` sempre termina para qualquer inteiro `n >= 0`.

---

### `G03-E02` *(Completar solução — Potência recursiva `P(x, n)` — Papel)*
Complete as lacunas `/* A */`, `/* B */` e `/* C */` na função recursiva abaixo para calcular $x^n$ ($n \ge 0$) sem laços:
```c
int potencia(int x, int n) {
    if ( /* A */ ) {
        return /* B */ ;
    }
    return /* C */ ;
}
```

---

### `G03-E03` *(Caça ao Bug — Programa completo `.c`)*
O programa abaixo deveria ler `n` (`n >= 0`), `x` e `e` (`e >= 0`) e imprimir a quantidade de dígitos de `n` e o valor de $x^e$ usando **apenas recursão (sem laços)**. Identifique os **2 erros** (um erro de caso base para entrada `0` e uma violação da regra sem laços), comente-os com `//` e apresente o programa corrigido:

```c
#include <stdio.h>

int contar_digitos(int n);
int potencia(int x, int e);

int main(void) {
    int n, x, e;
    scanf("%d %d %d", &n, &x, &e);
    printf("Digitos: %d\n", contar_digitos(n));
    printf("Potencia: %d\n", potencia(x, e));
    return 0;
}

int contar_digitos(int n) {
    if (n == 0) {
        return 0;
    }
    return 1 + contar_digitos(n / 10);
}

int potencia(int x, int e) {
    int res = 1;
    while (e > 0) {
        res = res * x;
        e--;
    }
    return res;
}
```

---

### `G03-E04` *(Variação controlada com pistas — Programa completo `.c`)*
Escreva um **programa completo** em C (sem laços em nenhuma função) definindo protótipos antes de `main` para:
- `int contar_digitos(int n)` — retorna a quantidade de dígitos de `n` (`n >= 0`).
- `int soma_digitos_pares(int n)` — retorna a soma apenas dos dígitos pares de `n` (`n >= 0`).

No `main`, leia `n` (`n >= 0`) e imprima exatamente:
```text
Digitos: D
Soma digitos pares: S
```
*Pista:* Em `soma_digitos_pares`, teste `int d = n % 10;`: se `n < 10`, devolva `d` quando `d % 2 == 0` ou `0` caso contrário; se `n >= 10`, some `d` (quando par) com `soma_digitos_pares(n / 10)`.

---

### `G03-E05` *(Resolução independente — Programa completo `.c`)*
Escreva um **programa completo** em C (sem qualquer laço `for`, `while` ou `do-while`) implementando duas funções recursivas sobre `n >= 0`:
- `int produto_digitos(int n)` — retorna o produto dos dígitos decimais de `n` (para `n = 0`, retorna `0`).
- `int maior_digito(int n)` — retorna o maior dígito decimal de `n` (faça apenas **uma** chamada recursiva por ativação guardando `maior_digito(n / 10)` em variável local).

No `main`, leia `n` (`n >= 0`) e imprima exatamente:
```text
Produto: P
Maior digito: M
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `G03-C01` *(Rastreamento e prova de terminação — Papel)*
Sem usar computador, rastreie `contar_altos(7409)` e justifique formalmente por que a função termina para todo inteiro `n >= 0`:
```c
int contar_altos(int n) {
    if (n < 10) {
        if (n >= 5) return 1;
        return 0;
    }
    if (n % 10 >= 5) {
        return 1 + contar_altos(n / 10);
    }
    return contar_altos(n / 10);
}
```

### `G03-C02` *(Correção de caso base `n == 0` vs. `n < 10` — Programa completo `.c`)*
O programa abaixo deveria contar quantos dígitos iguais a `0` existem em `n` (`n >= 0`), sabendo que o número `0` possui `1` dígito zero, mas falha para a entrada `0` (e retornaria um zero extra se alguém apenas trocasse `return 0;` por `return 1;` no caso base `n == 0`!). Corrija `contar_zeros` usando caso base `n < 10`:
```c
#include <stdio.h>

int contar_zeros(int n);

int main(void) {
    int n;
    scanf("%d", &n);
    printf("Zeros: %d\n", contar_zeros(n));
    return 0;
}

int contar_zeros(int n) {
    if (n == 0) {
        return 0;
    }
    if (n % 10 == 0) {
        return 1 + contar_zeros(n / 10);
    }
    return contar_zeros(n / 10);
}
```

### `G03-C03` *(Funções recursivas compiladas sem laços — Programa completo `.c`)*
Escreva um **programa completo** em C (sem `for`, `while` ou `do-while`) com protótipos antes de `main` para:
- `int contar_digitos_maiores(int n, int lim)` — retorna quantos dígitos decimais de `n` (`n >= 0`) são estritamente maiores que `lim`.
- `int potencia(int x, int e)` — retorna $x^e$ para `e >= 0`.

No `main`, leia `n`, `lim`, `x` e `e`, e imprima exatamente:
```text
Maiores que lim: K
Potencia: P
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `G04` (`Recursão Linear em Vetores 1D: Redução por Tamanho (n - 1)`):** somente após autocorreção de `G03-E01..E05` e **100% (3/3)** na Checagem Independente `G03-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** testar manualmente as entradas `n = 0`, `n = 5` e `n = 10` em `if (n == 0)` vs. `if (n < 10)`, reescrever a relação de recorrência antes do código C e aplicar variante `V2` de `G03`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`G02`** (ordem de execução na pilha) e **`B01` / `F01`** (decomposição decimal `% 10` e `/ 10` e retorno de funções tipadas).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 10 — recursão: definições e exemplos).
- `[DOC]` `Aula_21_Algoritmos.pdf` p. 25–26 (Ex. 2 — `potencia` recursiva e decomposição).
- `[DOC]` `Lista11_Algoritmos.pdf` p. 1–2 (Ex. 3 — `misterio(5832)` e justificativa de terminação; Ex. 4 — entrega `contar_digitos` sem laços).
- Casos de teste e soluções verificáveis: [G03_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/gabaritos/G03_gabarito.md) e [G03_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/G03_testes.md).
