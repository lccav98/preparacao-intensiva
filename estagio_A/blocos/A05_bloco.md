# Bloco `A05` — Saída de Variáveis, Casas Decimais e Constantes (`#define` e `const`)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio A — Fundamentos de Algoritmos, Ambiente C, Variáveis e Representação de Dados / **`A05`** |
| **Micro-habilidade foco** | Exibir valores de variáveis formatados com especificadores (`%d`/`%i`, `%f`, `%.Nf`, `%c`, `%e`) e definir constantes simbólicas (`#define` e `const`). |
| **Pré-requisitos** | `A03` *(Saída formatada com `printf` e escapes)* e `A04` *(Identificadores e declaração de variáveis)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`A05-E01`–`A05-E05`, 20 min):** `11 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`A05-C01`–`A05-C03`, 15 min):** `10 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Permitido:** inicialização na declaração (`tipo var = valor;`), especificadores `%d`/`%i`, `%f`, `%.Nf`, `%c`, `%e`, macro `#define NOME valor` (sem `;`) e qualificador `const tipo NOME = valor;`. **Proibido:** `scanf`, reatribuição de variável após declarada, operadores aritméticos (`+`, `-`, `*`, `/`, `%`), `if` ou laços. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`A05-E01`–`A05-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`A05-C01`–`A05-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Inicialização na declaração:** `tipo nome = valor;` declara e já grava o valor inicial (ex.: `int idade = 20;`, `double taxa = 3.5;`, `char letra = 'J';`). Em `char`, o caractere literal usa **aspas simples** (`'J'`).
2. **Especificadores de formato no `printf`:** cada marcador `%` na string corresponde, na mesma ordem, a um argumento após a vírgula:
   - `%d` ou `%i` → inteiro decimal (`int`).
   - `%f` → ponto flutuante (`float` ou `double`, exibindo 6 casas decimais por padrão).
   - `%.Nf` → ponto flutuante arredondado visualmente para `N` casas decimais (ex.: `%.2f`, `%.3f`).
   - `%c` → caractere único (`char`).
   - `%e` → notação científica (no padrão Linux/glibc: mantissa com 6 casas e `e+XX`, ex.: `1.500000e+02`).
3. **Duas formas de definir constantes simbólicas:**
   - **Macro `#define`:** `#define NOME valor` — diretiva do pré-processador colocada após `#include`; **não** recebe tipo, **não** usa `=` e **nunca** termina com `;`.
   - **Qualificador `const`:** `const tipo NOME = valor;` — exige tipo, `=` e `;`, e impede qualquer modificação do valor após a inicialização.
4. **Armadilha clássica:** colocar `;` no final de `#define LIMITE 100;` faz o pré-processador injetar `100;` dentro do `printf(...)`, causando erro de sintaxe! E usar `%d` em um `char` imprime o número do código ASCII, não a letra.

---

## 2. Exemplos Guiados

### Exemplo 1 — Especificadores de formato e precisão `%.Nf` *(Trecho ilustrativo)*

```c
int lote = 14;
double massa = 8.476;
char selo = 'B';

printf("Lote: %i | Selo: %c\n", lote, selo);
printf("Bruto: %f | Resumo: %.2f\n", massa, massa);
```
**Saída exata produzida:**
```text
Lote: 14 | Selo: B
Bruto: 8.476000 | Resumo: 8.48
```
Observe que `%i` equivale a `%d` no `printf`; `%f` exibe 6 casas por padrão (`8.476000`); e `%.2f` arredonda visualmente `8.476` para `8.48`.

### Exemplo 2 — Definindo e exibindo constantes com `#define` e `const` *(Programa completo)*

```c
#include <stdio.h>
#define PI 3.14159

int main(void) {
    const int TURMA = 61;
    double raio = 5.0;
    char grupo = 'A';

    printf("Turma %d - Grupo %c\n", TURMA, grupo);
    printf("PI = %.2f | Raio = %.1f\n", PI, raio);
    return 0;
}
```
**Saída exata:**
```text
Turma 61 - Grupo A
PI = 3.14 | Raio = 5.0
```
Note que `#define PI 3.14159` não leva `=` nem `;`, enquanto `const int TURMA = 61;` segue a sintaxe normal de declaração constante terminada por `;`.

---

## 3. Exercícios (`A05-E01` a `A05-E05`)

### `A05-E01` *(Previsão de saída no papel — Reprodução do modelo)*
Sem utilizar computador, escreva exatamente as 3 linhas impressas pelo trecho ilustrativo abaixo (adote a notação científica padrão Linux/glibc com 6 casas na mantissa e dois dígitos no expoente para `%e`):

```c
int cod = 7;
double val = 12.346;
double sci = 150.0;
char nivel = 'S';

printf("Cod=%d Nivel=%c\n", cod, nivel);
printf("V1=%.1f V2=%.2f\n", val, val);
printf("Sci=%e\n", sci);
```

---

### `A05-E02` *(Completar especificadores e constantes)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` no programa completo abaixo para que:
- `/* A */` defina a macro `MAX_ITENS` com valor `50` usando `#define`;
- `/* B */` declare a constante `TAXA_BASE` do tipo `double` com valor `4.5` usando `const`;
- `/* C */` e `/* D */` formatem respectivamente um inteiro e um real com 2 casas decimais, gerando a saída exata `Limite: 50 | Taxa: 4.50 | Tipo: P`:

```c
#include <stdio.h>
/* A */

int main(void) {
    /* B */
    char tipo = 'P';
    printf("Limite: /* C */ | Taxa: /* D */ | Tipo: %c\n", MAX_ITENS, TAXA_BASE, tipo);
    return 0;
}
```

---

### `A05-E03` *(Caça ao Bug — `#define` e especificadores — Programa completo)*
O programa completo abaixo deveria compilar sem avisos e exibir exatamente:
```text
Limite: 100 | Peso: 72.45 kg | Classe: A
```
Identifique os **3 bugs intencionais** presentes no código (anotando no papel ou em comentários `//`) e escreva a **versão corrigida completa**:

```c
#include <stdio.h>
#define LIMITE 100;

int main(void) {
    double peso = 72.453;
    char classe = 'A';

    printf("Limite: %f | Peso: %.2f kg | Classe: %d\n", LIMITE, peso, classe);
    return 0;
}
```

---

### `A05-E04` *(Variação controlada com pistas — `#define` e `const` sem expressão aritmética)*
Escreva um **programa completo** em C para exibir os parâmetros fixos de um experimento circular *(sem realizar cálculos aritméticos ainda, pois operadores serão estudados no Estágio B)*. Defina `#define PI 3.14159`, a constante `const int ESCALA = 2;` e as variáveis inicializadas `double raio = 4.5;` e `char unidade = 'm';`, imprimindo exatamente:

```text
PI aproximado: 3.1416
Escala: 2
Raio: 4.50 m
```
*Pistas:* Use `%.4f` para `PI`, `%i` (ou `%d`) para `ESCALA`, `%.2f %c` na última linha, e não coloque `;` nem `=` na diretiva `#define`.

---

### `A05-E05` *(Resolução independente — Ficha de dados formatada)*
Escreva um **programa completo** em C que declare e inicialize diretamente na declaração:
- constante `const int ANO_BASE = 2026;`
- inteiro `codigo = 308`
- real `double valorUnitario = 49.876;`
- real `double peso = 7.2;`
- caractere `char setor = 'E';`

Sem usar operadores aritméticos nem reatribuição de variáveis, exiba exatamente a ficha formatada abaixo (sem acentos):

```text
Ficha 2026 - Setor E
Codigo: 308
Valor: R$ 49.88
Peso: 7.2 kg
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `A05-C01` *(Previsão de `%.2f` e `%c` no papel)*
Sem usar computador, escreva exatamente a linha impressa pelo programa abaixo:

```c
#include <stdio.h>
#define FATOR 10

int main(void) {
    const char GRAU = 'B';
    double nota = 8.749;
    printf("Fator %i | Grau %c | Nota %.2f\n", FATOR, GRAU, nota);
    return 0;
}
```

### `A05-C02` *(Caça ao Bug — `#define` e `const` — Programa completo)*
O programa completo abaixo deveria definir uma constante `MAX` igual a `40` e uma constante real `TAXA` igual a `12.50`, imprimindo:
```text
Max: 40 | Taxa: 12.50
```
Identifique os **2 erros intencionais** e escreva a **versão corrigida completa** (inicializando `TAXA` diretamente na declaração, sem reatribuição):

```c
#include <stdio.h>
#define MAX 40;

int main(void) {
    const double TAXA = 10.00;
    TAXA = 12.50;
    printf("Max: %d | Taxa: %.2f\n", MAX, TAXA);
    return 0;
}
```

### `A05-C03` *(Programa completo independente)*
Escreva um **programa completo** em C que defina `#define VERSAO 3` e `const double TARIFA = 6.258;`, além das variáveis inicializadas `int sala = 102;` e `char bloco = 'C';`, sem reatribuições nem expressões aritméticas, e imprima exatamente:

```text
Sistema v3
Sala 102 - Bloco C
Tarifa: R$ 6.26
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `A06` (`Entrada de Dados com scanf e Operador &`):** somente após autocorreção de `A05-E01..E05` **e** **100% (3/3)** na Checagem Independente `A05-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** revisar a correspondência posicional entre especificadores (`%d`/`%i`, `%.Nf`, `%c`) e variáveis, além das regras de `#define` (sem `=` e sem `;`) vs. `const` (imutável após inicialização), aplicando a variante `V2` de `A05`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`A03`** (formatação e escapes em `printf`) e **`A04`** (tipos primitivos `char`, `int`, `float`, `double` e sintaxe de declaração).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (itens 2 e 4 — Variáveis, constantes e instruções de saída).
- `[DOC]` `Aula_02_Algoritmos.pdf` p. 20–24 (especificadores `%d`/`%i`/`%f`/`%c`/`%e`, casas decimais `%.Nf`, inicialização na declaração, constantes `#define` e `const`).
- `[DOC]` `Aula_03_Algoritmos.pdf` p. 12 (inicialização de variáveis na declaração).
- Gabarito comentado, casos JSON e especificação de testes: [A05_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/gabaritos/A05_gabarito.md) e [A05_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/A05_testes.md).
