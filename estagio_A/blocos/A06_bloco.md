# Bloco `A06` — Entrada de Dados com `scanf` e Operador `&`

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio A — Fundamentos, Ambiente C, Variáveis e Representação / **`A06`** |
| **Micro-habilidade foco** | Ler dados digitados pelo usuário com `scanf` usando o especificador compatível (`%d`, `%f`, `%lf`, `%c`) e o operador de endereço `&`, incluindo leitura múltipla e leitura segura de `char` com `" %c"`. |
| **Pré-requisitos** | `A05` *(Saída de variáveis com especificadores, casas decimais e constantes `#define`/`const`)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática (20 min) + checagem (15 min)** — **Sessão (`E01`–`E05`, 20 min):** `11 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** estrutura mínima C99 (`#include <stdio.h>`, `int main(void)`, `return 0;`), declarações (`char`, `int`, `float`, `double`), constantes (`#define`, `const`), `printf` (com escapes e `%.Nf`) e `scanf` (`%d`, `%f`, `%lf`, `" %c"`, leitura múltipla) com `&`. **Não utilize** reatribuição/troca com `aux` (`A07`), operadores aritméticos (`+`, `-`, `*`, `/`, `%`), `if`, laços, `%s` ou vetores. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Declare antes de ler:** Toda variável precisa estar declarada antes de ser usada no `scanf` (`Aula_03` p. 3).
2. **O operador `&` é obrigatório:** `scanf` precisa saber **onde, na memória**, guardar o valor digitado (`Aula_03` p. 6). Escreva sempre `scanf("%d", &idade);` — esquecer `&` gera erro ou comportamento indefinido.
3. **Regra crítica `float` vs `double` no `scanf` (`Aula_03` p. 7):**
   - Para `float x;` → use **`%f`**: `scanf("%f", &x);`
   - Para `double y;` → use obrigatoriamente **`%lf`** (*long float*): `scanf("%lf", &y);` (usar `%f` em `double` no `scanf` lê formato errado na memória!).
   - No `printf`, ambos aceitam `%.2f` (saídas sempre com ponto `.` e sem acentos).
4. **Leitura múltipla:** É possível ler vários valores em uma chamada separando especificadores por espaço: `scanf("%d %lf", &codigo, &valor);` e listando todos os endereços `&` na mesma ordem.
5. **Espaço antes de `%c` (`" %c"`):** Quando ler um caractere após números ou `Enter`, `%c` sem espaço capturaria o caractere em branco (`'\n'` ou `' '`) deixado no teclado. Escreva **`" %c"`** (com um espaço antes de `%c`) para ignorar espaços e quebras de linha pendentes.

---

## 2. Exemplos Guiados

### Exemplo 1 — Anatomia do `scanf`, operador `&` e erro `%f` vs `%lf` *(Trecho ilustrativo)*
Compare chamadas corretas e incorretas para as variáveis abaixo:

```c
int idade;
float taxa;
double saldo;
char grupo;

scanf("%d", idade);      /* ERRADO: faltou '&' antes de idade */
scanf("%d", &idade);     /* CORRETO */

scanf("%f", &taxa);      /* CORRETO para float */
scanf("%f", &saldo);     /* ERRADO: saldo eh double, exige %lf no scanf */
scanf("%lf", &saldo);    /* CORRETO para double */

scanf(" %c", &grupo);    /* CORRETO: espaco antes de %c ignora '\n' anterior */
```

### Exemplo 2 — Leitura múltipla e eco formatado *(Programa completo)*
O programa lê um inteiro (`matricula`), um `double` (`media`) e um caractere (`turno`), exibindo-os em formato padronizado:

```c
#include <stdio.h>

int main(void) {
    int matricula;
    double media;
    char turno;

    scanf("%d %lf %c", &matricula, &media, &turno);

    printf("Matricula: %d\n", matricula);
    printf("Media: %.2f\n", media);
    printf("Turno: %c\n", turno);
    return 0;
}
```
Para a entrada `1042 8.75 M`, o espaço antes de `%c` descarta o espaço após `8.75`, lendo exatamente `'M'`.

---

## 3. Exercícios (`A06-E01` a `A06-E05`)

### `A06-E01` *(Leitura e Diagnóstico de Código — Reprodução do modelo)*
Sem utilizar computador, analise o trecho ilustrativo abaixo e liste **todos os 3 erros** nas chamadas `scanf`, escrevendo a linha corrigida de cada um:

```c
int alunos;
double nota_corte;
char turma;

scanf("%d", alunos);
scanf("%f", &nota_corte);
scanf("%c", &turma);
```

---

### `A06-E02` *(Completar solução — Trecho ilustrativo)*
Complete as lacunas `/* A */`, `/* B */` e `/* C */` no trecho abaixo para ler:
1. dois inteiros (`codigo` e `lote`) em uma única chamada `scanf`;
2. um `double` (`peso`) e um `char` (`categoria`) na segunda chamada `scanf`, ignorando quebras de linha anteriores ao caractere.

```c
int codigo, lote;
double peso;
char categoria;

scanf("/* A */", /* B */);
scanf("/* C */", &peso, &categoria);
```

---

### `A06-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler o número inteiro de um `item`, seu `preco` (`double`) e o caractere do `setor` (`char`), imprimindo:
```text
Item: <item>
Preco: R$ <preco com 2 casas>
Setor: <setor>
```
Identifique os **4 bugs intencionais** (entre `scanf` e `printf` — anotando no papel ou em comentários `//`) e escreva a **versão corrigida completa**:

```c
#include <stdio.h>

int main(void) {
    int item;
    double preco;
    char setor;

    scanf("%d", item);
    scanf("%f", &preco);
    scanf("%c", &setor);

    printf("Item: %d\n", item);
    printf("Preco: R$ %.2f\n", &preco);
    printf("Setor: %c\n", setor);
    return 0;
}
```

---

### `A06-E04` *(Variação controlada com pistas — Programa completo)*
Escreva um **programa completo** em C que leia:
1. dois números inteiros (`id_a` e `id_b`) usando **uma única chamada `scanf`** (leitura dupla);
2. dois números reais `double` (`min_val` e `max_val`) usando **uma única chamada `scanf`**.

Em seguida, imprima exatamente no formato ASCII abaixo (2 casas decimais para os reais):
```text
IDs: <id_a> e <id_b>
Limites: <min_val> a <max_val>
```
*Pistas:* Use `"%d %d"` com `&id_a, &id_b` na primeira leitura e `"%lf %lf"` com `&min_val, &max_val` na segunda. Não use operadores aritméticos.

---

### `A06-E05` *(Resolução independente — Programa completo)*
Escreva um **programa completo** em C que leia, em **uma única chamada `scanf`** (tratando adequadamente o espaço antes de `%c`), um código inteiro (`codigo`), uma temperatura real em `double` (`temperatura`) e uma letra de escala (`escala`, tipo `char` — por exemplo `'C'`, `'F'` ou `'K'`), e imprima exatamente (com 1 casa decimal na temperatura):
```text
Sensor <codigo>: <temperatura> <escala>
```
Exemplo para entrada `12 24.5 C`:
`Sensor 12: 24.5 C`

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `A06-C01` *(Caça ao Bug — Programa completo)*
Identifique e corrija os **2 defeitos** do programa completo abaixo, que lê o número inteiro de uma `sala` e sua `area` em `double`:
```c
#include <stdio.h>

int main(void) {
    int sala;
    double area;

    scanf("%d", sala);
    scanf("%f", &area);

    printf("Sala: %d\n", sala);
    printf("Area: %.2f m2\n", area);
    return 0;
}
```

### `A06-C02` *(Completar leitura múltipla no papel — Trecho ilustrativo)*
Complete no papel as duas chamadas `scanf` do trecho ilustrativo abaixo:
```c
int dia, mes, ano;
double indice;
char classe;

/* 1. Leia dia, mes e ano em uma unica chamada scanf: */
scanf( /* complete */ );

/* 2. Leia indice e classe na mesma chamada, evitando capturar '\n' no char: */
scanf( /* complete */ );
```

### `A06-C03` *(Programa completo de entrada e eco formatado)*
Escreva um **programa completo** em C que leia um identificador inteiro (`id`), um valor monetário em `double` (`valor`) e um caractere de situação (`situacao`), e imprima exatamente:
```text
ID: <id>
Valor: R$ <valor com 2 casas>
Situacao: <situacao>
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `A07` (`Atribuição, Modelo de Memória e Troca com aux`):** somente após autocorreção de `A06-E01`..`E05` **e** **100% (3/3)** na Checagem Independente `A06-C01`..`C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** revisar a correspondência `double` ↔ `%lf`, a necessidade do `&` antes de cada variável no `scanf` e o espaço em `" %c"`; aplicar variante equivalente `V2` de `A06`.
- **Regra das 2 tentativas malsucedidas:** após **2 reprovações** neste bloco, parar repetições mecânicas e investigar o pré-requisito **`A05`** (especificadores de formato) e **`A04`** (declaração e tipos primitivos).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 4 — Instruções de entrada, saída e atribuição).
- `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 1 (28/08 — Uso das funções `scanf()` e `printf()`).
- `[DOC]` `Aula_03_Algoritmos.pdf` p. 3–8 (`scanf`, operador `&`, especificadores `%d`/`%i`/`%f`/`%lf`/`%c`) e p. 13–14 (programas completos de entrada).
- `[INF]` Uso de `" %c"` para ignorar *whitespace* (`'\n'`, `' '`) residual após leitura numérica no `scanf`.
- Gabarito e especificação de testes: [A06_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/gabaritos/A06_gabarito.md) e [A06_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/A06_testes.md).
