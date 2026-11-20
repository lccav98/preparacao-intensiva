# Bloco `A09` — Tamanhos de Tipos, Modificadores (`sizeof`) e Precisão de Ponto Flutuante (`float` vs `double`)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio A — Fundamentos, Ambiente C, Variáveis e Representação / **`A09`** |
| **Micro-habilidade foco** | Selecionar tipos inteiros com modificadores (`short`, `long`, `signed`, `unsigned`) ou reais (`float` vs `double`) avaliando tamanhos em bytes (`sizeof` com `%zu`) e erros de aproximação binária em ponto flutuante. |
| **Pré-requisitos** | `A05` *(Especificadores e constantes)* e `A08` *(Bits, bytes e $2^n$)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática (20 min) + checagem (15 min)** — **Sessão (`E01`–`E05`, 20 min):** `11 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** declarações com `short`, `long`, `signed`, `unsigned`, `char`, `int`, `float`, `double`, operador `sizeof` com `%zu`, sufixo `f` (`0.1f`) e soma simples `+` apenas para o experimento `0.1f + 0.2f` vs `0.1 + 0.2`. **Não utilize** `if`, laços, divisão `/`, resto `%`, `<math.h>` ou vetores. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Modificadores de tipos inteiros (`Aula_02` p. 19; `Aula_04` p. 10):**
   - `short` (típico: `2 bytes` = `16 bits`) e `long` (`8 bytes` no Linux x86-64 LP64; `4 bytes` no Windows LLP64).
   - `signed` (padrão em `short`, `int`, `long`): armazena negativos e não negativos, cobrindo $[-2^{n-1},\; 2^{n-1}-1]$.
   - `unsigned`: armazena apenas valores $\ge 0$, dobrando o limite positivo máximo para $[0,\; 2^n - 1]$.
2. **Operador `sizeof` e especificador `%zu` (`Aula_04` p. 11):**
   `sizeof(tipo)` retorna a quantidade de **bytes** ocupada pelo tipo na arquitetura atual (tipo `size_t`). Imprima **sempre com `%zu`** (padrão C99); usar `%d` causa aviso em `-Wall -Wextra`.
   Tamanhos típicos no alvo do curso (**Linux x86-64 / LP64**): `char = 1`, `short = 2`, `int = 4`, `long = 8`, `float = 4`, `double = 8` bytes.
3. **Por que números reais sofrem aproximação (`Aula_04` p. 12–14):**
   Entre quaisquer dois números reais há infinitos valores, mas `float` (32 bits) e `double` (64 bits) têm bits finitos. Valores como `0.1` não têm representação binária exata finita, sendo guardados como **aproximação**.
4. **`float` vs `double` (`Aula_04` p. 15–18):**
   - `float` (`4 bytes`): precisão aproximada de **6–7 dígitos** decimais; literais usam sufixo `f` (ex.: `0.1f`).
   - `double` (`8 bytes`): precisão aproximada de **15–16 dígitos** decimais; é a escolha padrão recomendada para cálculos reais confiáveis.

---

## 2. Exemplos Guiados

### Exemplo 1 — Faixas `signed` vs `unsigned` *(Trecho ilustrativo)*
Para um tipo inteiro de **1 byte** (`8 bits`, $2^8 = 256$ valores) e de **2 bytes** (`16 bits`, $2^{16} = 65\,536$ valores):
```c
signed char temp_sensor = -10;     /* faixa: -128 a 127 */
unsigned char brilho_pixel = 255;  /* faixa: 0 a 255 */
short altitude = -400;             /* faixa: -32768 a 32767 */
unsigned short portas = 65535;     /* faixa: 0 a 65535 */
```
Note que a **quantidade de bits** (e de valores distintos $2^n$) não muda entre `signed` e `unsigned`; o que muda é o deslocamento da faixa para incluir ou não negativos.

### Exemplo 2 — Inspecionando `sizeof` com `%zu` e aproximação de `0.1f` *(Programa completo)*
```c
#include <stdio.h>

int main(void) {
    float x = 0.1f;

    printf("int: %zu bytes\n", sizeof(int));
    printf("double: %zu bytes\n", sizeof(double));
    printf("0.1f com 2 casas: %.2f\n", x);
    printf("0.1f com 10 casas: %.10f\n", x);
    printf("0.1f com 20 casas: %.20f\n", x);
    return 0;
}
```
Saída em Linux x86-64 (IEEE-754):
- `int: 4 bytes` / `double: 8 bytes`
- `0.1f` com `%.2f` = `0.10` (mascara o erro!)
- `0.1f` com `%.10f` = `0.1000000015`
- `0.1f` com `%.20f` = `0.10000000149011611938`

---

## 3. Exercícios (`A09-E01` a `A09-E05`)

### `A09-E01` *(Cálculo de faixas `signed`/`unsigned` no papel)*
Sem usar computador, responda com base em $2^n$:
- **(a)** Qual é o menor e o maior valor representável por um inteiro `unsigned` de `1 byte` (`8 bits`) e por um `signed` de `1 byte`?
- **(b)** Qual é o intervalo exato de `unsigned short` (`2 bytes`) e de `short` (`signed`, `2 bytes`)?
- **(c)** Em Linux x86-64, um `int` de `4 bytes` (`32 bits`) representa de $-2^{31}$ a $2^{31}-1$ ($\approx \pm 2{,}14 \times 10^9$). Qual é o limite aproximado de `unsigned int` e por que ele dobra o positivo máximo?

---

### `A09-E02` *(Completar solução — `sizeof` com `%zu` e `0.1f` com `%.20f` — Programa completo)*
Complete as lacunas `/* A */` a `/* D */` no programa abaixo:

```c
#include <stdio.h>

int main(void) {
    float x = /* A */;
    printf("int: /* B */ bytes\n", sizeof(int));
    printf("double: /* C */ bytes\n", /* D */);
    printf("0.1f: %.20f\n", x);
    return 0;
}
```

---

### `A09-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria exibir o tamanho em bytes de `float` e `double` (sem warnings no `gcc -std=c99 -Wall -Wextra`) e comparar com alta precisão (`%.10f` e `%.20f`) o valor `0.1` armazenado em `float` e em `double`. Identifique os **2 defeitos intencionais** no código (no papel ou em comentários `//`) e escreva a **versão corrigida completa**:

```c
#include <stdio.h>

int main(void) {
    float a = 0.1f;
    double b = 0.1;

    printf("float: %d bytes\n", sizeof(float));
    printf("double: %d bytes\n", sizeof(double));
    printf("float 0.1f (10 casas): %.2f\n", a);
    printf("float 0.1f (20 casas): %.2f\n", a);
    printf("double 0.1 (10 casas): %.2f\n", b);
    printf("double 0.1 (20 casas): %.2f\n", b);
    return 0;
}
```

---

### `A09-E04` *(Escolha justificada de tipo — Papel)*
Para cada dado abaixo, escolha o tipo em C mais adequado entre `unsigned char`, `short`, `unsigned short`, `int`, `unsigned int`, `long`, `float` e `double`, justificando pelo tamanho em bytes (Linux x86-64), faixa ou precisão:
1. Intensidade de pixel em imagem PGM P2 (`0` a `255`).
2. Altitude geográfica em metros (`-430` m a `8850` m).
3. População mundial estimada (`8.200.000.000` habitantes — atenção ao limite de 4 bytes!).
4. Coeficiente físico que exige `12` dígitos decimais significativos após o ponto.

---

### `A09-E05` *(Experimento `float` vs `double` — Programa completo)*
Escreva um **programa completo** em C que declare:
- `float af = 0.1f, bf = 0.2f, sf = af + bf;`
- `double ad = 0.1, bd = 0.2, sd = ad + bd;`

e imprima os resultados das duas somas com **10** e **20** casas decimais exatamente no formato:
```text
float 10 casas: <sf com %.10f>
float 20 casas: <sf com %.20f>
double 10 casas: <sd com %.10f>
double 20 casas: <sd com %.20f>
```
*Pista:* Observe por que `float` já diverge na 8ª casa decimal (`0.3000000119...`), enquanto `double` mantém `0.3000000000` até 10 casas e só exibe ruído na 17ª casa (`...04441`).

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `A09-C01` *(Faixa `unsigned`/`signed` de $k$ bytes)*
Considere um tipo inteiro de $k = 2$ bytes (`16` bits):
1. Quantos valores distintos ele representa? Indique a faixa exata para `unsigned` e para `signed`.
2. Um contador de eventos varia de `0` a `40.000`. Um `short` (`signed`) de `2` bytes consegue armazená-lo sem transbordar? Qual modificador resolve mantendo `2` bytes?

### `A09-C02` *(Diagnóstico de perda de precisão)*
Um estudante escreveu `float a = 0.1f; float b = 0.2f; float s = a + b;` e imprimiu `%.2f`, obtendo `0.30`. Com base nisso, afirmou que *"float guarda 0.1 e 0.3 sem erro algum"*. Explique tecnicamente:
1. Por que a conclusão está incorreta e o que `%.2f` escondeu;
2. Qual valor aparece ao imprimir `0.1f` e `0.1f + 0.2f` com `%.10f`;
3. Qual tipo primitivo reduz esse erro de aproximação e quantos dígitos aproximados ele preserva.

### `A09-C03` *(Programa completo com `sizeof` e `%zu`)*
Escreva um **programa completo** em C que imprima o tamanho em bytes (`sizeof` com `%zu`) dos 6 tipos fundamentais da `Aula_04` p. 11, exatamente uma linha por tipo:
```text
char: <n> bytes
short: <n> bytes
int: <n> bytes
long: <n> bytes
float: <n> bytes
double: <n> bytes
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `A10` (`Revisão e Consolidação do Estágio A`):** somente após autocorreção de `A09-E01`..`E05` **e** **100% (3/3)** na Checagem Independente `A09-C01`..`C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** revisar a relação entre $n$ bits, faixas `unsigned`/`signed` ($2^n$) e o motivo de `0.1` em binário ser aproximado (`Aula_04` p. 14–17); aplicar variante `V2` de `A09`.
- **Regra das 2 tentativas malsucedidas:** após **2 reprovações** neste bloco, parar repetições e investigar os pré-requisitos **`A08`** ($2^n$ e quantidade de bits) e **`A05`** (especificadores `printf`).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (itens 2 e 3 — Tipos primitivos e precisão numérica).
- `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 1 (31/08 — Representação de dados e precisão numérica; `float` e `double`).
- `[DOC]` `Aula_02_Algoritmos.pdf` p. 19 (Modificadores de tipo: `short`, `long`, `signed`, `unsigned`).
- `[DOC]` `Aula_04_Algoritmos.pdf` p. 10–19 (tamanhos de tipos, `sizeof`/`%zu`, reais em bits finitos, `float` vs `double` e experimento `0.1f + 0.2f`).
- `[INF]` Padrão alvo Linux x86-64 (LP64: `long` = 8 bytes) vs. Windows (LLP64: `long` = 4 bytes) documentado para interpretação portátil de `sizeof(long)`.
- Gabarito e especificação de testes: [A09_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/gabaritos/A09_gabarito.md) e [A09_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/A09_testes.md).
