# Especificação de Testes — Bloco `C01`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99** (`[DOC]` `Aula_00` p. 3; `Aula_10` p. 18).
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Critério de comparação e tolerância numérica:**
  - Comparação textual exata linha a linha após normalização de `\r\n` $\rightarrow$ `\n`.
  - Saídas inteiras devem ter coincidência exata.
- **Checagem estática de não-antecipação:**
  - Proibido o uso de `do-while` ou `for` neste bloco.
  - Proibido o uso de `break` ou `continue`.
  - Proibido o uso de vetores (`char[]`, `int[]`, etc.) ou ponteiros/funções além de `main`.
- **Casos de teste registrados:** 21 casos em [casos_C01.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/casos_C01.json).

---

## Casos de Teste por Programa

### 1. `C01_E02_corrigido.c` (Contagem simples de 1 a 5)
- **Entrada:** Nenhuma (sem leitura).
- **Saída:** `1\n2\n3\n4\n5\n`
- **Casos:**
  - `C01-E02-T1` (normal): Execução completa do laço com 5 iterações.

### 2. `C01_E03.c` (Contagem progressiva de 1 a N)
- **Entrada:** `int n`
- **Saída:** Números de `1` a `n`, um por linha.
- **Casos:**
  - `C01-E03-T1` (borda zero): `0` $\rightarrow$ saída vazia (0 iterações).
  - `C01-E03-T2` (borda negativo): `-5` $\rightarrow$ saída vazia (0 iterações).
  - `C01-E03-T3` (borda unitária): `1` $\rightarrow$ `1\n`.
  - `C01-E03-T4` (normal): `4` $\rightarrow$ `1\n2\n3\n4\n`.
  - `C01-E03-T5` (normal): `7` $\rightarrow$ `1\n2\n3\n4\n5\n6\n7\n`.

### 3. `C01_E04.c` (Contagem regressiva par até 0)
- **Entrada:** `int n`
- **Saída:** Números pares de `n` (ou `n-1` se ímpar) decrescendo de 2 em 2 até `0`.
- **Casos:**
  - `C01-E04-T1` (borda zero): `0` $\rightarrow$ `0\n`.
  - `C01-E04-T2` (borda ímpar 1): `1` $\rightarrow$ `0\n`.
  - `C01-E04-T3` (normal par): `6` $\rightarrow$ `6\n4\n2\n0\n`.
  - `C01-E04-T4` (normal ímpar): `7` $\rightarrow$ `6\n4\n2\n0\n`.
  - `C01-E04-T5` (normal par maior): `10` $\rightarrow$ `10\n8\n6\n4\n2\n0\n`.

### 4. `C01_E05.c` (Intervalo fechado [A, B])
- **Entrada:** `int a, b`
- **Saída:** Inteiros de `a` até `b`, um por linha.
- **Casos:**
  - `C01-E05-T1` (borda intervalo unitário): `5 5` $\rightarrow$ `5\n`.
  - `C01-E05-T2` (borda invertido): `6 4` $\rightarrow$ saída vazia.
  - `C01-E05-T3` (normal): `3 7` $\rightarrow$ `3\n4\n5\n6\n7\n`.
  - `C01-E05-T4` (normal com negativos): `-2 2` $\rightarrow$ `-2\n-1\n0\n1\n2\n`.
  - `C01-E05-T5` (normal): `100 103` $\rightarrow$ `100\n101\n102\n103\n`.

### 5. `C01_C03.c` (Intervalo com passo personalizado)
- **Entrada:** `int inicio, fim, passo`
- **Saída:** Valores de `inicio` incrementando de `passo` enquanto `<= fim`.
- **Casos:**
  - `C01-C03-T1` (borda inicio > fim): `10 5 2` $\rightarrow$ saída vazia.
  - `C01-C03-T2` (borda inicio == fim): `5 5 1` $\rightarrow$ `5\n`.
  - `C01-C03-T3` (normal): `2 11 3` $\rightarrow$ `2\n5\n8\n11\n`.
  - `C01-C03-T4` (normal): `1 10 2` $\rightarrow$ `1\n3\n5\n7\n9\n`.
  - `C01-C03-T5` (normal com passo 5): `0 20 5` $\rightarrow$ `0\n5\n10\n15\n20\n`.
