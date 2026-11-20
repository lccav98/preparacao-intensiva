# Especificação de Testes — Bloco `C03`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99** (`[DOC]` `Aula_00` p. 3; `Aula_10` p. 18).
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Critério de comparação e tolerância numérica:**
  - Comparação textual exata linha a linha após normalização de `\r\n` $\rightarrow$ `\n`.
  - Saídas inteiras devem ter coincidência exata; saídas reais (`%.2f`) tolerância numérica `0.01`.
  - Saídas `printf` estritamente em ASCII puro (sem acentos).
- **Checagem estática de não-antecipação:**
  - Proibido o uso de `do-while` ou `for`.
  - Proibido o uso de `break` ou `continue`.
  - Proibido o uso de vetores (`char[]`, `int[]`, `v[i]`) ou funções customizadas além de `int main(void)`.
- **Casos de teste registrados:** 31 casos em [casos_C03.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/casos_C03.json).

---

## Casos de Teste por Programa

### 1. `C03_E02_corrigido.c` (Soma e Maior Temperatura com Sentinela `-999`)
- **Entrada:** Sequência de inteiros terminada pela sentinela `-999`.
- **Saída:** `Soma: %d\nMaior: %d\n` (ou saída vazia caso `-999` seja o primeiro valor).
- **Casos:**
  - `C03-E02-T1` (normal com todos negativos — ponto crítico do bug `maior = 0`): `-10 -5 -8 -999` $\rightarrow$ `Soma: -23\nMaior: -5\n`.
  - `C03-E02-T2` (borda única temperatura zero): `0 -999` $\rightarrow$ `Soma: 0\nMaior: 0\n`.
  - `C03-E02-T3` (normal misto positivo/negativo): `12 -3 25 8 -999` $\rightarrow$ `Soma: 42\nMaior: 25\n`.
  - `C03-E02-T4` (borda única temperatura negativa): `-50 -999` $\rightarrow$ `Soma: -50\nMaior: -50\n`.
  - `C03-E02-T5` (borda entrada vazia imediata): `-999` $\rightarrow$ *(saída vazia)*.

### 2. `C03_E03.c` (Contagem e Soma com Sentinela `0`)
- **Entrada:** Sequência de inteiros positivos terminada por `0`.
- **Saída:** `Quantidade: %d\nSoma: %d\n`.
- **Casos:**
  - `C03-E03-T1` (borda entrada vazia): `0` $\rightarrow$ `Quantidade: 0\nSoma: 0\n`.
  - `C03-E03-T2` (borda unitário): `7 0` $\rightarrow$ `Quantidade: 1\nSoma: 7\n`.
  - `C03-E03-T3` (normal): `10 20 30 0` $\rightarrow$ `Quantidade: 3\nSoma: 60\n`.
  - `C03-E03-T4` (normal valores repetidos): `5 5 5 5 0` $\rightarrow$ `Quantidade: 4\nSoma: 20\n`.
  - `C03-E03-T5` (extremo valores maiores): `100 250 150 0` $\rightarrow$ `Quantidade: 3\nSoma: 500\n`.

### 3. `C03_E04.c` (Média Real com Sentinela `<= 0`)
- **Entrada:** Sequência de `double` positivos terminada por valor `<= 0.0`.
- **Saída:** `Media: %.2f\n` ou `Nenhum positivo lido\n`.
- **Casos:**
  - `C03-E04-T1` (borda sentinela zero): `0` $\rightarrow$ `Nenhum positivo lido\n`.
  - `C03-E04-T2` (borda sentinela negativa): `-3.5` $\rightarrow$ `Nenhum positivo lido\n`.
  - `C03-E04-T3` (borda unitário): `8.5 -1` $\rightarrow$ `Media: 8.50\n`.
  - `C03-E04-T4` (normal inteiros): `5.0 7.0 9.0 0` $\rightarrow$ `Media: 7.00\n`.
  - `C03-E04-T5` (normal decimais): `2.5 3.75 4.25 -10` $\rightarrow$ `Media: 3.50\n`.

### 4. `C03_E05.c` (MDC de Euclides Iterativo)
- **Entrada:** `int a, b` positivos.
- **Saída:** `MDC: %d\n`.
- **Casos:**
  - `C03-E05-T1` (normal `a > b`): `48 18` $\rightarrow$ `MDC: 6\n`.
  - `C03-E05-T2` (borda `a < b` com auto-inversão): `15 25` $\rightarrow$ `MDC: 5\n`.
  - `C03-E05-T3` (borda primos entre si): `17 13` $\rightarrow$ `MDC: 1\n`.
  - `C03-E05-T4` (borda iguais): `9 9` $\rightarrow$ `MDC: 9\n`.
  - `C03-E05-T5` (normal divisor exato): `24 6` $\rightarrow$ `MDC: 6\n`.
  - `C03-E05-T6` (extremo clássico de Euclides): `1071 462` $\rightarrow$ `MDC: 21\n`.

### 5. `C03_E06.c` (Maior e Menor com Sentinela `-1`)
- **Entrada:** Sequência de inteiros positivos terminada por `-1`.
- **Saída:** `Maior: %d\nMenor: %d\n` ou `Nenhum dado informado\n`.
- **Casos:**
  - `C03-E06-T1` (borda entrada vazia): `-1` $\rightarrow$ `Nenhum dado informado\n`.
  - `C03-E06-T2` (borda unitário): `42 -1` $\rightarrow$ `Maior: 42\nMenor: 42\n`.
  - `C03-E06-T3` (borda todos iguais): `10 10 10 -1` $\rightarrow$ `Maior: 10\nMenor: 10\n`.
  - `C03-E06-T4` (normal): `8 3 15 2 9 -1` $\rightarrow$ `Maior: 15\nMenor: 2\n`.
  - `C03-E06-T5` (normal extremo nos limites): `100 50 200 1 -1` $\rightarrow$ `Maior: 200\nMenor: 1\n`.

### 6. `C03_C03.c` (Estatísticas de Fluxo com Sentinela `0`)
- **Entrada:** Sequência de inteiros positivos terminada por `0`.
- **Saída:** `Quantidade: %d\nSoma: %d\nMedia: %.2f\nMaior: %d\n` ou `Nenhum valor valido\n`.
- **Casos:**
  - `C03-C03-T1` (borda entrada vazia): `0` $\rightarrow$ `Nenhum valor valido\n`.
  - `C03-C03-T2` (borda unitário): `9 0` $\rightarrow$ `Quantidade: 1\nSoma: 9\nMedia: 9.00\nMaior: 9\n`.
  - `C03-C03-T3` (normal média inteira): `4 8 6 0` $\rightarrow$ `Quantidade: 3\nSoma: 18\nMedia: 6.00\nMaior: 8\n`.
  - `C03-C03-T4` (normal média decimal): `10 5 12 7 0` $\rightarrow$ `Quantidade: 4\nSoma: 34\nMedia: 8.50\nMaior: 12\n`.
  - `C03-C03-T5` (extremo valores maiores): `100 200 50 150 0` $\rightarrow$ `Quantidade: 4\nSoma: 500\nMedia: 125.00\nMaior: 200\n`.
