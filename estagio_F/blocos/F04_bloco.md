# Bloco `F04` — Introdução a Ponteiros: `&`, `*`, `NULL`, Desreferenciamento e Rastreamento de Memória

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio F — Modularização, Funções, Ponteiros e Compilação Multi-Arquivo / **`F04`** |
| **Micro-habilidade foco** | Declarar ponteiros tipados (`int *p`), obter endereços com `&` (`%p`), inicializar com `&var` ou `NULL`, ler/modificar alvos via `*p` e rastrear passo a passo mudanças de alvo em memória. |
| **Pré-requisitos** | `F03` *(Passagem por valor em C e limites da cópia local)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 20 min):** `12 min` resol. \| `5 min` corr. \| `3 min` recup.; **Sessão 2 (`E04`–`E06`, 20 min):** `12 min` resol. \| `5 min` corr. \| `3 min` recup.; **Checagem (`C01`–`C03`, 16 min):** `11 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Não utilize** ponteiros como parâmetros de função (`F05`), vetores/matrizes/strings em funções (`F06`–`F07`), aritmética de ponteiros (`p + 1`, `p++`), múltiplos arquivos `.h`/`.c` (`F08`), recursividade (`G01`), `struct`, `malloc`/`free` ou VLAs. Todo o uso de ponteiros (`&`, `*`, `NULL`) ocorre localmente em `main` com escalares (`int`, `double`) e saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Operador de endereço (`&`) e `%p`:** Toda variável ocupa um endereço único na memória. `&a` obtém o endereço de `a`. Para imprimi-lo com `printf`, use `%p` e conversão `(void *)&a` (ou `(void *)p`).
2. **O que é um ponteiro:** É uma variável que armazena o **endereço de memória** de outra variável do tipo compatível (`int *p;` guarda endereço de `int`; `double *q;` guarda endereço de `double`).
3. **Dois usos distintos do símbolo `*`:**
   - **Na declaração** (`int *p;` ou `int *p = &a;`): indica que `p` é um **ponteiro para `int`**. Em `int *p = &a;`, quem recebe `&a` é **`p`**, não `*p`.
   - **Em expressões/atribuições** (`*p = 25;`, `y = *p;`): é o **operador de desreferenciamento** ("acesse o conteúdo no endereço guardado em `p`").
4. **Diferença crítica `p` vs. `*p` vs. `&p`:**
   - `p`: o **endereço** armazenado dentro do ponteiro (ex.: `0x100`).
   - `*p`: o **valor** guardado na variável alvo apontada por `p`.
   - `&p`: o **endereço próprio** onde o ponteiro `p` reside na memória (ex.: `0x200`).
   - Mudar `p = &b;` **redireciona** o ponteiro; mudar `*p = 99;` **altera o valor** da variável apontada.
5. **Declaração ≠ Inicialização (`NULL` e ponteiros não inicializados):** `int *p;` contém **lixo de memória** (endereço indefinido). Desreferenciar (`*p = 5;`) um ponteiro não inicializado ou `NULL` (`<stdio.h>`) gera **comportamento indefinido** (*segmentation fault*). Sempre inicialize com `&var` ou `NULL`, e teste `if (p != NULL)` antes de desreferenciar quando o ponteiro puder ser nulo.

---

## 2. Exemplos Guiados

### Exemplo 1 — Rastreamento de memória com endereços simbólicos *(Trecho ilustrativo)*
Suponha `a` no endereço `0x100`, `b` em `0x104` e `p` em `0x200`:
```c
int a = 10, b = 20;
int *p = &a;
*p = 25;
p = &b;
*p = *p + a;
```

| Passo | `a` (`0x100`) | `b` (`0x104`) | `p` (`0x200`) | `*p` | Observação |
|---|---:|---:|---|---:|---|
| `int a = 10, b = 20;` | `10` | `20` | `?` | — | `p` ainda não existe |
| `int *p = &a;` | `10` | `20` | `0x100` (`&a`) | `10` | `p` aponta para `a` |
| `*p = 25;` | **`25`** | `20` | `0x100` (`&a`) | `25` | Escreve em `a` via `*p` |
| `p = &b;` | `25` | `20` | **`0x104`** (`&b`) | `20` | Redireciona `p` para `b` |
| `*p = *p + a;` | `25` | **`45`** | `0x104` (`&b`) | `45` | `b = 20 + 25 = 45`; `&p` segue `0x200` |

### Exemplo 2 — Inicialização segura com `NULL`, `%p` e verificação antes de `*p` *(Programa completo)*
```c
#include <stdio.h>

int main(void) {
    int x = 10, y = 30, op;
    int *p = NULL; /* inicializado com NULL (nao aponta para lugar valido ainda) */

    scanf("%d", &op);
    if (op == 1) {
        p = &x;
    } else if (op == 2) {
        p = &y;
    }

    if (p != NULL) {
        *p = *p + 5;
        printf("Endereco: %p | Valor: %d\n", (void *)p, *p);
    } else {
        printf("Ponteiro NULL: nenhum alvo selecionado\n");
    }
    return 0;
}
```

---

## 3. Exercícios (`F04-E01` a `F04-E06`)

### Sessão 1 (`F04-E01` a `F04-E03` — Rastreamento Simbólico, Lacunas e Caça ao Bug)

### `F04-E01` *(Teste de Mesa Intensivo com Endereços Simbólicos — Reprodução do modelo)*
Considere os endereços simbólicos: `a` em `0x100`, `b` em `0x104`, `c` em `0x108`, `p` em `0x200` e `q` em `0x204`. Sem usar computador, acompanhe cada linha abaixo:

```c
int a = 5, b = 12, c = 30;
int *p = &a;
int *q = &b;
p = q;
*p = 40;
q = &c;
*q = *q - *p;
a = *p + *q;
```
Preencha os valores finais de todas as expressões:  
- `a = ___`, `&a = ___`  
- `b = ___`, `&b = ___`  
- `c = ___`, `&c = ___`  
- `p = ___`, `*p = ___`, `&p = ___`  
- `q = ___`, `*q = ___`, `&q = ___`

---

### `F04-E02` *(Completar solução)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` para declarar ponteiros `p` e `q` apontando para `x` e `y`, trocar os conteúdos de `x` e `y` **indiretamente via `*p` e `*q`** e aterrar `p` ao final:

```c
#include <stdio.h>

int main(void) {
    int x = 14, y = 29;
    int /* A */ = &x;
    int *q = /* B */ ;

    int aux = *p;
    *p = /* C */ ;
    *q = aux;

    /* D */ ; /* redireciona p para NULL */
    printf("x=%d y=%d\n", x, y);
    return 0;
}
```

---

### `F04-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler `x` e `y`, dobrar `x` usando o ponteiro `p`, apontar `q` para `y` somente quando `y > 0` (mantendo `NULL` caso contrário) e, se `q` não for nulo, somar `*q` em `*p`, imprimindo o valor final de `x`. Identifique os **3 bugs intencionais** (no papel ou em comentários `//`) e escreva a versão corrigida completa:

```c
#include <stdio.h>

int main(void) {
    int x, y;
    scanf("%d %d", &x, &y);

    int *p;
    *p = x * 2;

    int *q = NULL;
    if (y > 0) {
        q = y;
    }

    *p = *p + *q;

    printf("%d\n", x);
    return 0;
}
```

---

### Sessão 2 (`F04-E04` a `F04-E06` — Escrita Guiada → Independente em `main`)

### `F04-E04` *(Variação controlada com pistas)*
Escreva um **programa completo** em C que leia três inteiros `a`, `b` e `c` em `main`, declare dois ponteiros `int *p_menor = &a;` e `int *p_maior = &a;` e **redirecione** `p_menor` e `p_maior` (sem alterar valores ainda) para que apontem para a variável de menor e maior valor entre `a`, `b` e `c`. Em seguida, some `10` ao menor valor por meio de `*p_menor = *p_menor + 10;` e imprima exatamente:
```text
Valores: A B C
Apontado por p_maior: M
```
*Pista:* para atualizar um ponteiro, compare `b < *p_menor` e redirecione com `p_menor = &b;` (use `if`s independentes para `b` e `c`).

---

### `F04-E05` *(Variação controlada com pistas)*
Escreva um **programa completo** em C que leia dois inteiros `x` e `y` em `main` e declare `int *px = &x;` e `int *py = &y;`. Se `*px > *py`, troque os conteúdos de `x` e `y` **exclusivamente por meio de `*px` e `*py`** (usando `int aux = *px;`). Em seguida, verifique se `*px == *py` (gravando `1` ou `0` em `int iguais`) e imprima exatamente:
```text
Iguais: I
Ordenados: X Y
```
*Pista:* a variável auxiliar `aux` armazena um **valor inteiro** (`int`), não um endereço.

---

### `F04-E06` *(Resolução independente)*
Escreva um **programa completo** em C que leia dois números reais `double a, b;` e um inteiro `escolha`. Declare `double *alvo = NULL;`. Se `escolha == 1`, aponte `alvo` para `a`; se `escolha == 2`, aponte `alvo` para `b`; para qualquer outro valor, mantenha `alvo` como `NULL`.
- Se `alvo != NULL`, aumente em `10%` o valor apontado (`*alvo = (*alvo) * 1.10;`) e imprima `Atualizado: X.XX`.
- Caso contrário, imprima `Ponteiro nulo`.
- Ao final (em qualquer caso), imprima `Valores: A.AA B.BB`.

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `F04-C01` *(Teste de Mesa 1 — Redirecionamento de ponteiro)*
Considere `a` no endereço `0x100`, `b` em `0x104` e `p` em `0x200`. Sem usar computador, rastreie o trecho abaixo e informe os valores finais de `a`, `&a`, `b`, `&b`, `p`, `*p` e `&p`:

```c
int a = 8, b = 15;
int *p = &a;
*p = 20;
p = &b;
*p = *p + a;
a = *p - 10;
```

### `F04-C02` *(Teste de Mesa 2 — Dois ponteiros compartilhando o mesmo alvo)*
Considere `x` no endereço `0x100`, `y` em `0x104`, `p` em `0x200` e `q` em `0x204`. Sem usar computador, rastreie o trecho abaixo e informe os valores finais de `x`, `y`, `p`, `*p`, `&p`, `q`, `*q` e `&q`:

```c
int x = 10, y = 4;
int *p = &x;
int *q = &x;
*p = *p + 6;
*q = *q * 2;
q = &y;
*q = *p - *q;
```

### `F04-C03` *(Diagnóstico de Ponteiro Não Inicializado / `NULL` — Caça ao Bug)*
O programa completo abaixo deveria ler `a`, `b` e `cod`, somar `5` a `b` por meio de `p`, apontar `q` para `a` apenas quando `cod == 1` (`NULL` caso contrário) e, quando `q` não for nulo, somar `*p` em `*q`, exibindo `a` e `b`. Identifique os **2 bugs críticos de ponteiro** usando **comentários `//` no código** e escreva o programa corrigido completo:

```c
#include <stdio.h>

int main(void) {
    int a, b, cod;
    scanf("%d %d %d", &a, &b, &cod);

    int *p;
    *p = b + 5;

    int *q = NULL;
    if (cod == 1) {
        q = &a;
    }

    *q = *q + *p;
    printf("%d %d\n", a, b);
    return 0;
}
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `F05` (`Ponteiros como Parâmetros, Múltiplos Resultados e Depuração de Ponteiros`):** somente após autocorreção de `F04-E01..E06` e **100% (3/3)** em `F04-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** refazer tabelas de memória linha a linha com endereços simbólicos (`0x100`, `0x104`, `0x200`), separando explicitamente `p` (endereço guardado), `*p` (valor no alvo) e `&p` (endereço do próprio ponteiro); aplicar variante `V2` de `F04`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`F03`** (cópia local na passagem por valor), **`A07`** (modelo de memória e troca com `aux`) e **`A06`** (operador `&` no `scanf`).

---

## 6. Referências do Orientador
- `[DOC]` `Aula_17_Algoritmos.pdf` p. 18–35, 37–38 (Ex. 1, Ex. 2).
- `[DOC]` `Lista10_Algoritmos.pdf` p. 2 (base conceitual de Ex. 3).
- Casos de teste e soluções verificáveis: [F04_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/gabaritos/F04_gabarito.md) e [F04_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/F04_testes.md).
