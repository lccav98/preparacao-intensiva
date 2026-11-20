# Bloco `F03` — Passagem por Valor em C e Limites da Cópia Local

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio F — Modularização, Funções, Ponteiros e Compilação Multi-Arquivo / **`F03`** |
| **Micro-habilidade foco** | Compreender que argumentos escalares em C são sempre copiados para os parâmetros (**passagem por valor**) e que modificar o parâmetro não altera a variável original do chamador. |
| **Pré-requisitos** | `F02` *(Protótipos de funções, escopo local e tempo de vida)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão única de prática + checagem (18 min):** `10 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Não utilize** ponteiros (`int *`, `double *`), operador `&` como argumento de função própria (use `&` apenas em `scanf`), vetores/matrizes/strings como parâmetros (`F06`–`F07`), múltiplos arquivos `.h`/`.c` (`F08`), recursividade (`G01`), `struct`, `malloc`/`free` ou VLAs. Utilize protótipos antes de `main`, variáveis escalares (`int`, `double`), **passagem por valor** e `return`. Saídas de programas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Passagem por valor (regra fundamental em C):** Quando uma função é chamada com argumentos escalares (`f(x, y)`), C avalia cada argumento e **copia seu valor** para o parâmetro correspondente da função chamada.
2. **Quadros de memória separados:** Cada chamada cria um quadro próprio na memória para os parâmetros e variáveis locais da função. Alterar um parâmetro dentro da função modifica **apenas a cópia local**; a variável original no chamador permanece intacta.
3. **Por que `void trocar(int x, int y)` falha:** Mesmo que `x` e `y` troquem de valor dentro do quadro de `trocar`, esse quadro é destruído no retorno. As variáveis originais `a` e `b` de `main` jamais são alteradas.
4. **Paralelo com `scanf`:** Para ler um inteiro, escrevemos `scanf("%d", &x);` e não `scanf("%d", x);`. Sem `&`, `scanf` receberia apenas uma cópia do valor de `x` e não conseguiria alterar a variável original de `main` *(veremos como fazer isso em funções próprias usando ponteiros em `F04`–`F05`)*.
5. **Quando `return` resolve vs. quando não basta:**
   - Para calcular **1 único resultado** e atualizar uma variável do chamador, substitua a função `void` falha por uma função com retorno (`int` ou `double`) e atribua o retorno em `main` (`x = dobrar(x);`).
   - Quando a tarefa exige modificar **2 ou mais variáveis** do chamador ao mesmo tempo (como `trocar`), apenas um `return` não é suficiente.

---

## 2. Exemplos Guiados

### Exemplo 1 — Cópia local vs. retorno útil com `return` *(Trecho ilustrativo)*
```c
void tentar_dobrar(int n) {
    n = n * 2; /* modifica apenas a copia local 'n' */
}

int dobrar(int n) {
    return n * 2; /* devolve o novo valor ao chamador */
}
```
Rastreamento de memória para `int x = 5;` em `main`:
- Ao chamar `tentar_dobrar(x);`:
  - Quadro `main`: `x = 5`
  - Quadro `tentar_dobrar`: `n = 5` → `n = 10` *(destruído ao retornar)*
  - Após o retorno, em `main`: `x` **continua `5`**.
- Ao chamar `x = dobrar(x);`:
  - `dobrar(5)` calcula `10` e devolve `10` pelo `return`; `main` grava `10` em `x`.

### Exemplo 2 — Falha de `swap` por valor vs. atualização com `return` *(Programa completo)*
```c
#include <stdio.h>

void trocar_falho(int x, int y);
int atualizar_saldo(int saldo, int delta);

int main(void) {
    int a = 10, b = 20, saldo = 100;
    trocar_falho(a, b);
    saldo = atualizar_saldo(saldo, 35);
    printf("a=%d b=%d saldo=%d\n", a, b, saldo);
    return 0;
}

void trocar_falho(int x, int y) {
    int aux = x;
    x = y;
    y = aux; /* trocou apenas as copias locais x e y */
}

int atualizar_saldo(int saldo, int delta) {
    return saldo + delta;
}
```
Saída produzida: `a=10 b=20 saldo=135`. `a` e `b` não trocaram, enquanto `saldo` foi atualizado graças ao `return`.

---

## 3. Exercícios (`F03-E01` a `F03-E05`)

### `F03-E01` *(Teste de Mesa de Memória — Papel)*
Sem usar computador, acompanhe os quadros de memória do programa abaixo:

```c
#include <stdio.h>

void ajusta(int a, int b);

int main(void) {
    int x = 4, y = 7;
    printf("Antes: %d %d\n", x, y);
    ajusta(x, y);
    printf("Depois: %d %d\n", x, y);
    return 0;
}

void ajusta(int a, int b) {
    a += 10;
    b *= 2;
    printf("Dentro: %d %d\n", a, b);
}
```
**(a)** Desenhe o conteúdo dos quadros de `main` e `ajusta` durante a execução de `ajusta(x, y);` e após o retorno.  
**(b)** Escreva as 3 linhas exatas impressas no terminal.

---

### `F03-E02` *(Análise Conceitual e Lacunas)*
Observe os dois trechos abaixo:

```c
void trocar(int x, int y) {
    int aux = x;
    x = y;
    y = aux;
}
```
```c
/* Objetivo: retornar preco com pct% de desconto */
/* A */ aplicar_desconto(double preco, double pct) {
    double novo = preco * (1.0 - pct / 100.0);
    /* B */
}
/* Em main: double p = 100.0; /* C */ */
```
**(a)** Explique por que chamar `trocar(u, v);` em `main` deixa `u` e `v` inalterados.  
**(b)** Preencha as lacunas `/* A */`, `/* B */` e `/* C */` para converter `aplicar_desconto` em uma função com retorno útil e atualizar `p` em `main`.

---

### `F03-E03` *(Caça ao Bug — Programa completo)*
O programa abaixo lê `double salario` e `double percentual`, deveria aplicar o aumento percentual por meio da função `reajustar` e imprimir `Novo salario: X.XX`. Porém, devido a um erro de passagem por valor, o valor impresso permanece igual ao salário original. Identifique o erro (em comentários `//`) e corrija o programa completo convertendo `reajustar` para retornar o novo salário via `return`:

```c
#include <stdio.h>

void reajustar(double sal, double pct);

int main(void) {
    double salario, percentual;
    scanf("%lf %lf", &salario, &percentual);
    reajustar(salario, percentual);
    printf("Novo salario: %.2f\n", salario);
    return 0;
}

void reajustar(double sal, double pct) {
    sal = sal * (1.0 + pct / 100.0);
}
```

---

### `F03-E04` *(Variação controlada com pistas)*
Escreva um **programa completo** em C com protótipo antes de `main` para a função:
```c
int processar_saque(int saldo, int valor);
```
Se `valor > 0 && valor <= saldo`, a função deve subtrair `valor` de sua cópia local `saldo` e retornar o novo valor; caso contrário, retorna `saldo` inalterado. No `main`, leia `saldo` e `saque`, armazene o retorno em `novo_saldo` e imprima exatamente:
```text
Original: X
Atualizado: Y
```
*Pista:* como `saldo` é passado por valor, a variável `saldo` de `main` continua preservada para impressão na linha `Original:`.

---

### `F03-E05` *(Resolução independente)*
Escreva um **programa completo** em C com protótipos antes de `main` para:
- `double converter_celsius_para_kelvin(double c);` — retorna `c + 273.15`.
- `double limitar_intervalo(double val, double min, double max);` — retorna `min` se `val < min`, `max` se `val > max`, ou `val` caso contrário.

No `main`, leia uma temperatura `double t`, converta-a para Kelvin chamando `converter_celsius_para_kelvin`, restrinja o resultado ao intervalo `[0.0, 1000.0]` chamando `limitar_intervalo` (atualizando via `return`) e imprima exatamente:
```text
Kelvin limitado: K.KK
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `F03-C01` *(Teste de Mesa sem compilador)*
Sem usar computador, execute o rastreamento do programa abaixo e escreva a saída exata linha por linha:

```c
#include <stdio.h>

int misturar(int a, int b);

int main(void) {
    int x = 6, y = 2, z;
    z = misturar(x, y);
    printf("main: x=%d y=%d z=%d\n", x, y, z);
    return 0;
}

int misturar(int a, int b) {
    a = a * 3;
    b = b + 5;
    printf("func: a=%d b=%d\n", a, b);
    return a + b;
}
```

### `F03-C02` *(Análise Conceitual sem compilador)*
Considere a tentativa de ordenação abaixo:

```c
#include <stdio.h>

void ordenar_par(int a, int b);

int main(void) {
    int x = 15, y = 4;
    ordenar_par(x, y);
    printf("%d %d\n", x, y);
    return 0;
}

void ordenar_par(int a, int b) {
    if (a > b) {
        int aux = a;
        a = b;
        b = aux;
    }
}
```
**(a)** O que é impresso no terminal?  
**(b)** Explique, em termos de **passagem por valor** e **quadros de memória separados**, por que `ordenar_par` falha em ordenar `x` e `y` em `main` e por que um único comando `return` não resolveria a atualização simultânea dessas duas variáveis no chamador.

### `F03-C03` *(Conversão de `void` falho para `return` útil — Programa completo)*
Um estudante escreveu a função abaixo esperando atualizar os pontos de um jogador em `main`, mas ela falha por usar `void` com passagem por valor:
```c
void aplicar_multa(int pontos, int infracao) {
    if (infracao > 0) {
        pontos = pontos + infracao;
    }
}
```
Escreva um **programa completo** em C (com protótipo antes de `main`) que corrija `aplicar_multa` para retornar `int`, leia `pontos` e `infracao` no `main`, atualize `pontos` usando o retorno da função (`pontos = aplicar_multa(pontos, infracao);`) e imprima exatamente:
```text
Total de pontos: P
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `F04` (`Introdução a Ponteiros: &, *, NULL, Desreferenciamento e Rastreamento de Memória`):** somente após autocorreção de `F03-E01..E05` e **100% (3/3)** em `F03-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** desenhar duas caixas separadas no papel (`Quadro main` vs `Quadro funcao`), rastreando a cópia inicial dos argumentos e mostrando que o quadro da função desaparece ao retornar; aplicar variante `V2` de `F03`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`F02`** (escopo local e tempo de vida) e **`A07`** (atribuição e troca com variável auxiliar).

---

## 6. Referências do Orientador
- `[DOC]` `Aula_17_Algoritmos.pdf` p. 12–17.
- `[DOC]` `Aula_18_Algoritmos.pdf` p. 4–7.
- `[DOC]` `Lista10_Algoritmos.pdf` p. 1–2 (Ex. 2 — parte escalar `func1`).
- Casos de teste e soluções verificáveis: [F03_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/gabaritos/F03_gabarito.md) e [F03_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/F03_testes.md).
