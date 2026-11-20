# Especificação de Testes — Bloco `D04`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, `#define MAX 100`, vetores 1D fixos (sem VLAs, funções extras, strings ou matrizes 2D), saídas em ASCII puro.
- **Comparação de saídas e tolerância:**
  - Correspondência textual e numérica exata.
- **Casos de teste registrados:** 25 casos (5 por arquivo `.c`) em [casos_D04.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/casos_D04.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`D04_E03_corrigido.c`:**
   - Normal com negativos (`6`: `-4 10 -4 7 10 0`) → `Unicos (4): -4 10 7 0`
   - Todos iguais (`4`: `5 5 5 5`) → `Unicos (1): 5`
   - Todos distintos (`4`: `100 -200 300 0`) → `Unicos (4): 100 -200 300 0`
   - `n = 1` (`1`: `-9`) → `Unicos (1): -9`
   - Repetidos consecutivos e nas pontas (`6`: `1 1 2 3 3 1`) → `Unicos (3): 1 2 3`

2. **`D04_E04.c`:**
   - Normal (`6`: `2 0 2 9 2 1`) → `0: *\n1: *\n2: ***\n9: *\n`
   - Todos zero (`3`: `0 0 0`) → `0: ***\n`
   - Extremos `0` e `9` (`4`: `9 0 9 0`) → `0: **\n9: **\n`
   - `n = 1` (`1`: `5`) → `5: *\n`
   - Todos os dígitos `0..9` (`10`: `9 8 7 6 5 4 3 2 1 0`) → uma linha `*` para cada dígito de `0` a `9`

3. **`D04_E05.c`:**
   - Mesmo histograma permutado (`5`: `1 3 3 0 2` e `3 0 2 1 3`) → `Mesmo histograma\nMais frequente: 3 (total 4)\n`
   - Histogramas diferentes (`4`: `1 1 2 3` e `1 2 2 3`) → `Histogramas diferentes\nMais frequente: 1 (total 3)\n` (empate `1` e `2` com total `3`, vence menor `1`)
   - Empate total no dígito `0` (`2`: `0 5` e `5 0`) → `Mesmo histograma\nMais frequente: 0 (total 2)\n`
   - `n = 1` diferente (`1`: `9` e `4`) → `Histogramas diferentes\nMais frequente: 4 (total 1)\n`
   - Todos iguais no dígito `9` (`3`: `9 9 9` e `9 9 9`) → `Mesmo histograma\nMais frequente: 9 (total 6)\n`

4. **`D04_C02_corrigido.c`:**
   - Normal incluindo `0` e `5` (`7`: `5 0 3 5 2 5 1`) → `Nota 0: 1\nNota 1: 1\nNota 2: 1\nNota 3: 1\nNota 4: 0\nNota 5: 3\n`
   - Todas notas `5` (`3`: `5 5 5`) → `Nota 0..4: 0`, `Nota 5: 3`
   - Todas notas `0` (`2`: `0 0`) → `Nota 0: 2`, `Nota 1..5: 0`
   - `n = 1` nota `4` (`1`: `4`) → `Nota 4: 1`, demais `0`
   - Uma de cada nota (`6`: `5 4 3 2 1 0`) → todas `1`

5. **`D04_C03.c`:**
   - Normal (`7`: `8 -3 8 0 -3 12 8`) → `Unicos (4): 8 -3 0 12\nRepetidos removidos: 3\n`
   - Sem repetidos (`4`: `-1 -2 -3 -4`) → `Unicos (4): -1 -2 -3 -4\nRepetidos removidos: 0\n`
   - Todos iguais (`5`: `0 0 0 0 0`) → `Unicos (1): 0\nRepetidos removidos: 4\n`
   - `n = 1` (`1`: `999`) → `Unicos (1): 999\nRepetidos removidos: 0\n`
   - Valores grandes e negativos (`5`: `10000 -5000 10000 42 -5000`) → `Unicos (3): 10000 -5000 42\nRepetidos removidos: 2\n`
