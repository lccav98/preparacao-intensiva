# Especificação de Testes — Bloco `G02`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, protótipos antes de `main`, funções recursivas `void` **estritamente sem `for`/`while`/`do-while`**, sem decomposição decimal, sem vetores/strings, sem `struct`, sem `malloc`/`free`, sem VLAs e saídas em ASCII puro.
- **Comparação de saídas e tolerância:** correspondência textual exata de saída (`stdout`).
- **Casos de teste registrados:** **20 casos** (5 por arquivo `.c`) em [casos_G02.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/casos_G02.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`G02_E03_corrigido.c` (`espelho`):**
   - `3` (normal) → `3 2 1 1 2 3`
   - `1` (borda mínima positiva) → `1 1`
   - `0` (borda zero) → linha vazia (`\n`)
   - `-4` (borda negativa) → linha vazia (`\n`)
   - `5` (normal maior) → `5 4 3 2 1 1 2 3 4 5`

2. **`G02_E04.c` (`sequencia_ab`):**
   - `3` (normal) → `A3 A2 A1 B1 B2 B3`
   - `1` (borda mínima positiva) → `A1 B1`
   - `0` (borda zero) → linha vazia (`\n`)
   - `-2` (borda negativa) → linha vazia (`\n`)
   - `4` (normal 4 níveis) → `A4 A3 A2 A1 B1 B2 B3 B4`

3. **`G02_E05.c` (`contar_regressivo` + `contar_progressivo`):**
   - `4` (normal) → `Regressivo: 4 3 2 1` / `Progressivo: 1 2 3 4`
   - `1` (borda unitária) → `Regressivo: 1` / `Progressivo: 1`
   - `0` (borda zero) → `Regressivo:` / `Progressivo:`
   - `-3` (borda negativa) → `Regressivo:` / `Progressivo:`
   - `6` (normal 6 níveis) → `Regressivo: 6 5 4 3 2 1` / `Progressivo: 1 2 3 4 5 6`

4. **`G02_C03.c` (`pulso`):**
   - `3` (normal) → `3 2 1 0 1 2 3`
   - `0` (borda zero) → `0`
   - `1` (borda unitária) → `1 0 1`
   - `-5` (borda negativa) → `0`
   - `5` (normal 5 níveis) → `5 4 3 2 1 0 1 2 3 4 5`
