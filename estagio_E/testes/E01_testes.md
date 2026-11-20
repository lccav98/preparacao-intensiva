# Especificação de Testes — Bloco `E01`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, `int main(void)` sem funções extras, matrizes 2D com dimensões fixas por `#define` (sem VLAs, sem `struct`, sem `malloc`/`free`), saídas em ASCII puro.
- **Comparação de saídas e tolerância:**
  - Saída inteira e formatação tabular com correspondência exata.
- **Casos de teste registrados:** 25 casos (5 por arquivo `.c`) em [casos_E01.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/casos_E01.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`E01_E03_corrigido.c` (grade `2 x 3`):**
   - Normal (`1 2 3 4 5 6`) → 2 linhas: `1 2 3` / `4 5 6`
   - Negativos e zero (`-5 0 7 -2 9 -1`) → `-5 0 7` / `-2 9 -1`
   - Todos zeros (`0 0 0 0 0 0`) → `0 0 0` / `0 0 0`
   - Constante (`8 8 8 8 8 8`) → `8 8 8` / `8 8 8`
   - Extremos (`-100 50 0 99 -1 42`) → `-100 50 0` / `99 -1 42`

2. **`E01_E04.c` (grade `3 x 3` com linhas invertidas):**
   - Normal (`1 2 3 4 5 6 7 8 9`) → `7 8 9` / `4 5 6` / `1 2 3`
   - Negativos (`-1 -2 -3 0 0 0 1 2 3`) → `1 2 3` / `0 0 0` / `-1 -2 -3`
   - Todos zeros (`0 0 0 0 0 0 0 0 0`) → `0 0 0` / `0 0 0` / `0 0 0`
   - Linhas iguais (`5 5 5 5 5 5 5 5 5`) → `5 5 5` / `5 5 5` / `5 5 5`
   - Simétrica nas linhas (`10 20 30 40 50 60 10 20 30`) → `10 20 30` / `40 50 60` / `10 20 30`

3. **`E01_E05.c` (grade `l x c` e cantos `m[0][0]` e `m[l-1][c-1]`):**
   - Normal `2 x 3` (`2 3` / `10 20 30 40 50 60`) → `Cantos: 10 60` + 2 linhas
   - Borda `1 x 1` (`1 1` / `-42`) → `Cantos: -42 -42` + `-42`
   - Borda `1 x 4` (vetor-linha) (`1 4` / `5 6 7 8`) → `Cantos: 5 8` + `5 6 7 8`
   - Borda `4 x 1` (vetor-coluna) (`4 1` / `9 -1 0 3`) → `Cantos: 9 3` + 4 linhas
   - Retangular `3 x 2` com negativos (`3 2` / `-7 0 4 -2 8 -9`) → `Cantos: -7 -9` + 3 linhas

4. **`E01_C02_corrigido.c` (grade `l x c` tabular):**
   - Normal `2 x 2` (`2 2` / `1 2 3 4`) → `1 2` / `3 4`
   - Borda `1 x 1` (`1 1` / `99`) → `99`
   - Borda `1 x 3` (`1 3` / `-1 0 1`) → `-1 0 1`
   - Borda `3 x 1` (`3 1` / `10 20 30`) → `10` / `20` / `30`
   - Retangular `3 x 4` (`3 4` / `1 2 3 4 5 6 7 8 9 10 11 12`) → 3 linhas de 4 valores

5. **`E01_C03.c` (grade `3 x 4` original e inversa total):**
   - Normal (`1..12`) → `Matriz:` (`1 2 3 4` / `5 6 7 8` / `9 10 11 12`) + `Inversa:` (`12 11 10 9` / `8 7 6 5` / `4 3 2 1`)
   - Zeros (`0` x 12) → ambas matrizes zeradas
   - Negativos (`-12..-1`) → `Matriz:` + `Inversa:`
   - Palíndromo de grade (`1 2 3 4 5 6 6 5 4 3 2 1`) → `Matriz:` e `Inversa:` idênticas
   - Misto (`10 0 -5 3 8 -2 7 1 -9 4 0 6`) → `Matriz:` + `Inversa:`
