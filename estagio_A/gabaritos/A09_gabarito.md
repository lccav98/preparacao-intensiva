# Gabarito Comentado — Bloco `A09` (`sizeof`, Modificadores e Precisão `float` vs `double`)

> **Bloco de referência:** [A09_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/blocos/A09_bloco.md)  
> **Nota para Caça ao Bug:** O código em `A09-E03` no bloco do aluno contém **defeitos intencionais** detalhados abaixo. Apenas as versões corrigidas e válidas devem ser compiladas.

---

## 1. Gabarito dos Exercícios (`A09-E01` a `A09-E05`)

### `A09-E01` *(Faixas `signed`/`unsigned`)*
- **(a)** `1 byte` (`8 bits`, $2^8 = 256$ valores):
  - `unsigned`: **`[0, 255]`** ($0$ até $2^8 - 1$).
  - `signed`: **`[-128, 127]`** ($-2^7$ até $2^7 - 1$).
- **(b)** `2 bytes` (`16 bits`, $2^{16} = 65\,536$ valores):
  - `unsigned short`: **`[0, 65535]`**.
  - `short` (`signed`): **`[-32768, 32767]`**.
- **(c)** `unsigned int` (32 bits) representa aproximadamente **`0` a `4.294.967.295` ($\approx 4 \times 10^9$)**. Como não precisa reservar metade dos padrões ($2^{31}$) para representar números negativos, toda a capacidade de $2^{32}$ padrões fica disponível para valores não negativos, dobrando o limite positivo.

### `A09-E02` *(Completar solução — `sizeof` e `0.1f`)*
- **`/* A */`:** `0.1f`
- **`/* B */`:** `%zu`
- **`/* C */`:** `%zu`
- **`/* D */`:** `sizeof(double)`

### `A09-E03` *(Caça ao Bug — Defeitos intencionais no enunciado)*
- **Erros intencionais:**
  1. Uso de `%d` para imprimir o retorno de `sizeof(...)` (cujo tipo é `size_t`, exigindo **`%zu`** em C99 para evitar warning em `-Wall -Wextra` e incompatibilidade de tamanho em plataformas 64 bits).
  2. Uso de `%.2f` em todas as saídas de `0.1f` e `0.1` mascara o erro de aproximação binária; para revelar a diferença de precisão entre `float` (32 bits) e `double` (64 bits), deve-se usar `%.10f` e `%.20f`.
- **Solução corrigida completa:** [A09_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A09_E03_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    float a = 0.1f;
    double b = 0.1;

    printf("float: %zu bytes\n", sizeof(float));
    printf("double: %zu bytes\n", sizeof(double));
    printf("float 0.1f (10 casas): %.10f\n", a);
    printf("float 0.1f (20 casas): %.20f\n", a);
    printf("double 0.1 (10 casas): %.10f\n", b);
    printf("double 0.1 (20 casas): %.20f\n", b);
    return 0;
}
```
*(Saída exata em Linux x86-64 / IEEE-754: `float: 4 bytes`, `double: 8 bytes`, `0.1000000015`, `0.10000000149011611938`, `0.1000000000`, `0.10000000000000000555`.)*

### `A09-E04` *(Escolha justificada de tipo)*
1. Pixel PGM P2 (`0..255`): **`unsigned char`** (`1 byte`, faixa exata `[0, 255]`).
2. Altitude (`-430..8850`): **`short`** (`2 bytes`, `signed`, faixa `[-32768, 32767]`, economiza metade da memória de `int`).
3. População (`8.200.000.000`): **`long`** (ou `unsigned long`) em Linux x86-64 (`8 bytes`), pois `int` (`4 bytes`, máximo `2.147.483.647`) e `unsigned int` (máximo `4.294.967.295`) transbordariam!
4. Coeficiente com `12` dígitos significativos: **`double`** (`8 bytes`, ~15–16 dígitos decimais de precisão, enquanto `float` oferece apenas ~6–7 dígitos).

### `A09-E05` *(Programa completo — Experimento `0.1f + 0.2f` vs `0.1 + 0.2`)*
Arquivo: [A09_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A09_E05.c)
```c
#include <stdio.h>

int main(void) {
    float af = 0.1f, bf = 0.2f, sf = af + bf;
    double ad = 0.1, bd = 0.2, sd = ad + bd;

    printf("float 10 casas: %.10f\n", sf);
    printf("float 20 casas: %.20f\n", sf);
    printf("double 10 casas: %.10f\n", sd);
    printf("double 20 casas: %.20f\n", sd);
    return 0;
}
```
*(Saída exata IEEE-754: `0.3000000119`, `0.30000001192092895508`, `0.3000000000`, `0.30000000000000004441`.)*

---

## 2. Gabarito da Checagem Independente (`A09-C01` a `A09-C03`)

### `A09-C01` *(Faixa `unsigned`/`signed` de $k = 2$ bytes)*
1. $k = 2$ bytes = $16$ bits → representa **$2^{16} = 65\,536$** valores distintos.
   - `unsigned`: **`[0, 65535]`**
   - `signed`: **`[-32768, 32767]`**
2. **Não.** Um `short` (`signed`) de 2 bytes suporta apenas até `32.767`, portanto `40.000` transbordaria (*overflow*). O modificador **`unsigned short`** mantém `2 bytes` e amplia o limite superior até `65.535`.

### `A09-C02` *(Diagnóstico de perda de precisão)*
1. A conclusão é incorreta porque `0.1` e `0.2` **não possuem representação binária exata finita**; `float` armazena apenas uma aproximação em 32 bits. O especificador `%.2f` arredonda visualmente para 2 casas e **oculta o erro** já presente na memória.
2. Com `%.10f`, obtém-se **`0.1000000015`** para `0.1f` e **`0.3000000119`** para `0.1f + 0.2f`.
3. O tipo **`double`** (`8 bytes`, 64 bits) reduz drasticamente esse erro, mantendo cerca de **15–16 dígitos decimais** de precisão (`0.1000000000` e `0.3000000000` em `%.10f`).

### `A09-C03` *(Programa completo com `sizeof` e `%zu`)*
Arquivo: [A09_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A09_C03.c)
```c
#include <stdio.h>

int main(void) {
    printf("char: %zu bytes\n", sizeof(char));
    printf("short: %zu bytes\n", sizeof(short));
    printf("int: %zu bytes\n", sizeof(int));
    printf("long: %zu bytes\n", sizeof(long));
    printf("float: %zu bytes\n", sizeof(float));
    printf("double: %zu bytes\n", sizeof(double));
    return 0;
}
```
*(Saída alvo em Linux x86-64 LP64: `char: 1`, `short: 2`, `int: 4`, `long: 8`, `float: 4`, `double: 8` bytes.)*
