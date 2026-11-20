# Especificação de Testes — Bloco `C02`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99** (`[DOC]` `Aula_00` p. 3; `Aula_10` p. 18).
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Critério de comparação e tolerância numérica:**
  - Comparação textual exata linha a linha após normalização de `\r\n` $\rightarrow$ `\n`.
  - Saídas inteiras devem ter coincidência exata.
- **Checagem estática de não-antecipação:**
  - Proibido o uso de `do-while` ou `for`.
  - Proibido o uso de `break` ou `continue`.
  - Proibido o uso de vetores (`char[]`, `int[]`, etc.) ou ponteiros/funções além de `main`.
- **Casos de teste registrados:** 30 casos em [casos_C02.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/casos_C02.json).

---

## Casos de Teste por Programa

### 1. `C02_E02_corrigido.c` (Divisão inteira por subtrações sucessivas com correção de bug)
- **Entrada:** `int a, b`
- **Saída:** `Quociente: %d\nResto: %d\n`
- **Casos:**
  - `C02-E02-T1` (borda dividendo zero): `0 5` $\rightarrow$ `Quociente: 0\nResto: 0\n`.
  - `C02-E02-T2` (borda a == b): `5 5` $\rightarrow$ `Quociente: 1\nResto: 0\n`.
  - `C02-E02-T3` (borda a < b): `4 5` $\rightarrow$ `Quociente: 0\nResto: 4\n`.
  - `C02-E02-T4` (múltiplo exato - ponto crítico do bug): `15 5` $\rightarrow$ `Quociente: 3\nResto: 0\n`.
  - `C02-E02-T5` (normal com resto): `14 4` $\rightarrow$ `Quociente: 3\nResto: 2\n`.
  - `C02-E02-T6` (normal com resto): `23 7` $\rightarrow$ `Quociente: 3\nResto: 2\n`.

### 2. `C02_E03.c` (Tabuada de 1 a 10 com while)
- **Entrada:** `int n`
- **Saída:** 10 linhas no formato `%d x %d = %d\n`.
- **Casos:**
  - `C02-E03-T1` (borda zero): `0` $\rightarrow$ tabuada do zero (todos resultados 0).
  - `C02-E03-T2` (borda unitária): `1` $\rightarrow$ tabuada do 1.
  - `C02-E03-T3` (normal): `5` $\rightarrow$ tabuada do 5.
  - `C02-E03-T4` (normal): `7` $\rightarrow$ tabuada do 7.

### 3. `C02_E04.c` (Divisão e resto por subtrações sucessivas)
- **Entrada:** `int dividendo, divisor`
- **Saída:** `Quociente: %d\nResto: %d\n`
- **Casos:**
  - `C02-E04-T1` (borda zero): `0 8` $\rightarrow$ `Quociente: 0\nResto: 0\n`.
  - `C02-E04-T2` (borda divisor == dividendo): `8 8` $\rightarrow$ `Quociente: 1\nResto: 0\n`.
  - `C02-E04-T3` (borda dividendo < divisor): `3 8` $\rightarrow$ `Quociente: 0\nResto: 3\n`.
  - `C02-E04-T4` (normal múltiplo exato): `20 4` $\rightarrow$ `Quociente: 5\nResto: 0\n`.
  - `C02-E04-T5` (normal com resto): `29 6` $\rightarrow$ `Quociente: 4\nResto: 5\n`.

### 4. `C02_E05.c` (Soma e contagem de pares em intervalo)
- **Entrada:** `int a, b`
- **Saída:** `Quantidade: %d\nSoma: %d\n`
- **Casos:**
  - `C02-E05-T1` (borda sem pares, intervalo unitário ímpar): `3 3` $\rightarrow$ `Quantidade: 0\nSoma: 0\n`.
  - `C02-E05-T2` (borda 1 par, intervalo unitário par): `4 4` $\rightarrow$ `Quantidade: 1\nSoma: 4\n`.
  - `C02-E05-T3` (normal): `1 6` $\rightarrow$ pares: 2, 4, 6 $\rightarrow$ `Quantidade: 3\nSoma: 12\n`.
  - `C02-E05-T4` (normal): `2 8` $\rightarrow$ pares: 2, 4, 6, 8 $\rightarrow$ `Quantidade: 4\nSoma: 20\n`.
  - `C02-E05-T5` (normal): `7 11` $\rightarrow$ pares: 8, 10 $\rightarrow$ `Quantidade: 2\nSoma: 18\n`.

### 5. `C02_C02_corrigido.c` (Resto por subtrações sucessivas corrigido)
- **Entrada:** `int a, b`
- **Saída:** `Resto: %d\n`
- **Casos:**
  - `C02-C02-T1` (borda a = 0): `0 4` $\rightarrow$ `Resto: 0\n`.
  - `C02-C02-T2` (borda a == b): `4 4` $\rightarrow$ `Resto: 0\n`.
  - `C02-C02-T3` (borda múltiplo exato): `12 4` $\rightarrow$ `Resto: 0\n`.
  - `C02-C02-T4` (normal com resto): `13 4` $\rightarrow$ `Resto: 1\n`.
  - `C02-C02-T5` (normal a < b): `3 5` $\rightarrow$ `Resto: 3\n`.

### 6. `C02_C03.c` (Estatísticas de intervalo com while e filtros)
- **Entrada:** `int inicio, fim`
- **Saída:** `Impares: %d\nSoma mult 3: %d\n`
- **Casos:**
  - `C02-C03-T1` (borda unitário par não mult 3): `2 2` $\rightarrow$ `Impares: 0\nSoma mult 3: 0\n`.
  - `C02-C03-T2` (borda unitário ímpar mult 3): `3 3` $\rightarrow$ `Impares: 1\nSoma mult 3: 3\n`.
  - `C02-C03-T3` (normal): `1 6` $\rightarrow$ `Impares: 3\nSoma mult 3: 9\n`.
  - `C02-C03-T4` (normal): `1 10` $\rightarrow$ `Impares: 5\nSoma mult 3: 18\n`.
  - `C02-C03-T5` (normal): `6 12` $\rightarrow$ `Impares: 3\nSoma mult 3: 27\n`.
