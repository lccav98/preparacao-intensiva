# Bloco `F01` — Introdução a Funções: `void`, `return`, Parâmetros e Argumentos (Definição Antes de `main`)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio F — Modularização, Funções, Ponteiros e Compilação Multi-Arquivo / **`F01`** |
| **Micro-habilidade foco** | Definir e chamar funções próprias (`void` e com retorno tipado) posicionadas antes de `main`, distinguindo parâmetro formal, argumento e uso do valor retornado. |
| **Pré-requisitos** | `E08` *(Revisão e Consolidação do Estágio E — Matrizes Bidimensionais)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão única de prática + checagem (22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Não utilize** protótipos antes de `main` com definição após `main` (`F02`), ponteiros (`int *`, `F04`–`F05`) nem passagem de `&var` como argumento de função (use `&` apenas em `scanf`), vetores/matrizes/strings como parâmetros (`F06`–`F07`), múltiplos arquivos `.h`/`.c` (`F08`), recursividade (`G01`), `struct`, `malloc`/`free` ou VLAs. Defina todas as funções auxiliares **antes de `main`**, usando apenas parâmetros escalares (`int`, `double`, `char`) e saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Anatomia e posição antes de `main`:** Em C, uma função tem a forma `tipo_retorno nome(tipo1 p1, tipo2 p2) { ... }`. Quando todas as funções auxiliares são definidas **antes de `main`**, o compilador já conhece cada função no ponto em que `main` a chama.
2. **Papel do `void`:**
   - Como **tipo de retorno** (`void linha(void)`): a função executa uma tarefa (como imprimir) e **não devolve valor**. É chamada como instrução isolada (`linha();`), **nunca** dentro de `printf` ou atribuição (`x = linha();`).
   - Como **lista de parâmetros** (`(void)`): indica explicitamente que a função **não recebe argumentos**.
3. **Parâmetros formais vs. Argumentos (passagem por valor):**
   - Na definição `int somar(int a, int b)`, `a` e `b` são **parâmetros formais**. Todo parâmetro exige seu **próprio tipo** (`int a, int b` — nunca `int a, b`).
   - Na chamada `somar(x, 10)`, `x` e `10` são **argumentos**, cujos valores são **copiados por valor** para `a` e `b` no momento da chamada.
4. **Uso obrigatório do `return` em funções tipadas:** Uma função com retorno (`int`, `double`) deve devolver um valor compatível com `return expr;` em **todos os caminhos de execução** possíveis (incluindo ramos `if`/`else`). Quem chama a função deve **armazenar ou usar** o valor retornado (`r = somar(x, 10);` ou `printf("%d", somar(x, 10));`); chamar `somar(x, 10);` isoladamente descarta o resultado.
5. **Proibição de recursividade:** Uma função não deve chamar a si mesma neste estágio (use laços `for`/`while` quando precisar repetir).

---

## 2. Exemplos Guiados

### Exemplo 1 — `void linha(void)`, parâmetros individuais e retorno tipado *(Trecho ilustrativo)*
```c
void linha(void) {
    printf("----------\n");
}

int somar(int a, int b) { /* 'a' e 'b' sao parametros; cada um declara seu tipo */
    return a + b;         /* devolve o resultado ao chamador */
}

/* Em main:
   linha();                      // chamada de funcao void (nao retorna valor)
   int total = somar(7, 5);      // 7 e 5 sao argumentos copiados por valor -> total = 12
*/
```

### Exemplo 2 — Função iterativa com laço definida antes de `main` *(Programa completo)*
```c
#include <stdio.h>

void imprimir_cabecalho(void) {
    printf("=== Contador de Digitos ===\n");
}

int contar_digitos(int n) {
    if (n == 0) {
        return 1; /* caminho especifico para n == 0 */
    }
    int cont = 0;
    while (n > 0) {
        cont++;
        n /= 10;
    }
    return cont;  /* retorno garantido no caminho restante */
}

int main(void) {
    int num;
    scanf("%d", &num);
    imprimir_cabecalho();
    int qtd = contar_digitos(num);
    printf("Digitos: %d\n", qtd);
    return 0;
}
```
Observe que `contar_digitos` garante um `return` tanto quando `n == 0` quanto após o laço `while`, e `main` captura o retorno em `qtd`.

---

## 3. Exercícios (`F01-E01` a `F01-E05`)

### `F01-E01` *(Leitura e Teste de Mesa — Reprodução do modelo)*
Sem utilizar computador, acompanhe passo a passo o programa completo abaixo:

```c
#include <stdio.h>

void separador(void) {
    printf("---\n");
}

int calcular(int a, int b) {
    return a * 2 + b;
}

int main(void) {
    separador();
    int r = calcular(3, 4) + calcular(2, 5);
    printf("R = %d\n", r);
    separador();
    return 0;
}
```
**(a)** Escreva a saída exata impressa no terminal, linha por linha.  
**(b)** Na primeira chamada `calcular(3, 4)`, quais são os **parâmetros formais** e quais são os **argumentos**? Por que a instrução `printf("%d", separador());` seria inválida em C?

---

### `F01-E02` *(Completar solução)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` para que o programa exiba um título sem parâmetros e imprima o maior entre dois inteiros lidos:

```c
#include <stdio.h>

/* A */ exibir_titulo(void) {
    printf("Comparador\n");
}

int maior2(int a, /* B */ ) {
    if (a > b) {
        return a;
    }
    /* C */
}

int main(void) {
    int x, y;
    scanf("%d %d", &x, &y);
    exibir_titulo();
    int m = /* D */ ;
    printf("Maior: %d\n", m);
    return 0;
}
```

---

### `F01-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler dois inteiros `x` e `y`, determinar o maior usando `maior_de_dois` e imprimir `Maior: M`. Identifique os **3 bugs intencionais** (no papel ou em comentários `//` diretamente no código) e escreva a versão corrigida completa:

```c
#include <stdio.h>

int maior_de_dois(int a, b) {
    if (a >= b) {
        return a;
    }
}

int main(void) {
    int x, y, m = 0;
    scanf("%d %d", &x, &y);
    maior_de_dois(x, y);
    printf("Maior: %d\n", m);
    return 0;
}
```

---

### `F01-E04` *(Variação controlada com pistas)*
Escreva um **programa completo** em C definindo **antes de `main`** duas funções:
- `void exibir_faixa(int ini, int fim)` — imprime em uma linha os inteiros de `ini` até `fim` separados por espaço simples; se `ini > fim`, imprime `Intervalo vazio\n`.
- `int soma_intervalo(int ini, int fim)` — retorna a soma dos inteiros de `ini` até `fim` (ou `0` se `ini > fim`).

No `main`, leia dois inteiros `a` e `b`, chame `exibir_faixa(a, b);` e imprima exatamente:
```text
Soma: S
```
*Pista:* para evitar espaço sobrando ao final da linha em `exibir_faixa`, use `if (i > ini) printf(" ");` antes de `printf("%d", i);`.

---

### `F01-E05` *(Resolução independente)*
Escreva um **programa completo** em C definindo **antes de `main`** duas funções iterativas (sem recursão):
- `int contar_digitos(int n)` — dado `n >= 0`, retorna a quantidade de dígitos decimais de `n` (note que `0` possui `1` dígito).
- `int soma_digitos(int n)` — dado `n >= 0`, retorna a soma dos dígitos decimais de `n`.

No `main`, leia um inteiro `n` (`n >= 0`) e imprima exatamente:
```text
Digitos: D
Soma dos digitos: S
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `F01-C01` *(Teste de Mesa)*
Sem usar computador, execute o rastreamento do programa abaixo e responda:

```c
#include <stdio.h>

void marca(void) {
    printf("*\n");
}

int passo(int k) {
    if (k % 2 == 0) {
        return k / 2;
    }
    return k * 3 + 1;
}

int main(void) {
    int v = 5;
    marca();
    v = passo(v);
    printf("%d\n", v);
    printf("%d\n", passo(v));
    marca();
    return 0;
}
```
**(a)** Qual é a saída exata impressa linha por linha?  
**(b)** Qual é o parâmetro formal de `passo` e quais argumentos são passados na 1ª e na 2ª chamadas de `passo` em `main`?

### `F01-C02` *(Caça ao Bug — Programa completo)*
O programa abaixo lê `double preco` e `int qtd`, calcula o subtotal com `calcular_subtotal`, calcula `10%` de desconto caso o subtotal seja `>= 200.0` (ou `0.0` caso contrário) com `calcular_desconto`, e imprime `Total: X.XX`. Corrija todos os erros presentes no programa completo:

```c
#include <stdio.h>

double calcular_subtotal(double preco, qtd) {
    return preco * qtd;
}

double calcular_desconto(double total) {
    if (total >= 200.0) {
        return total * 0.10;
    }
}

int main(void) {
    double preco, subtotal, desc = 0.0;
    int qtd;
    scanf("%lf %d", &preco, &qtd);
    subtotal = calcular_subtotal(preco, qtd);
    calcular_desconto(subtotal);
    printf("Total: %.2f\n", subtotal - desc);
    return 0;
}
```

### `F01-C03` *(Programa completo independente)*
Defina **antes de `main`** duas funções:
- `void imprimir_linha(int n, char ch)` — imprime o caractere `ch` repetido `n` vezes na mesma linha (se `n <= 0`, imprime apenas a quebra de linha `\n`).
- `int fatorial(int n)` — calcula e retorna `n!` de forma iterativa (`n >= 0`, com `0! = 1`).

No `main`, leia `n` (`int`) e `ch` (`char`) com `scanf("%d %c", &n, &ch);`, chame `imprimir_linha(n, ch);` e imprima exatamente:
```text
Fatorial: F
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `F02` (`Protótipos de Funções, Escopo Local e Tempo de Vida`):** somente após autocorreção de `F01-E01..E05` e **100% (3/3)** em `F01-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** revisar a declaração individual de tipo por parâmetro (`int a, int b`), a exigência de `return` em todos os ramos de funções não-`void` e o uso do valor retornado pelo chamador; aplicar variante `V2` de `F01`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`E08`** / **`C05`** (laços `for`/`while` dentro do fluxo sequencial) e **`B04`** (caminhos mutuamente exclusivos em `if/else`).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 9 — procedimentos, funções, parâmetros e argumentos).
- `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 4 (27/10).
- `[DOC]` `Aula_16_Algoritmos.pdf` p. 3–24.
- `[DOC]` `Lista10_Algoritmos.pdf` p. 1 (Ex. 1 — versão iterativa de `contar_digitos`).
- Casos de teste e soluções verificáveis: [F01_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/gabaritos/F01_gabarito.md) e [F01_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/F01_testes.md).
