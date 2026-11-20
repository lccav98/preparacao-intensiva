# Especificação de Testes — Bloco `D01`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, tamanho fixo com `#define` (`N` ou `MAX`), sem VLAs, sem funções extras, sem strings ou matrizes 2D, saídas em ASCII puro.
- **Comparação de saídas e tolerância:**
  - Saída inteira e formatação textual com correspondência exata.
- **Casos de teste registrados:** 25 casos (5 por arquivo `.c`) em [casos_D01.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/casos_D01.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`D01_E03_corrigido.c`:**
   - Normal (`10 20 30 40 50`) → `Direta: 10 20 30 40 50\nInversa: 50 40 30 20 10\n`
   - Negativos e zero (`-5 0 7 -2 9`) → `Direta: -5 0 7 -2 9\nInversa: 9 -2 7 0 -5\n`
   - Todos iguais (`4 4 4 4 4`) → `Direta: 4 4 4 4 4\nInversa: 4 4 4 4 4\n`
   - Decrescente (`5 4 3 2 1`) → `Direta: 5 4 3 2 1\nInversa: 1 2 3 4 5\n`
   - Zeros e extremos (`0 -100 100 0 -1`) → `Direta: 0 -100 100 0 -1\nInversa: -1 0 100 -100 0\n`

2. **`D01_E04.c`:**
   - Normal (`1 2 3 4 5 6`) → `Metade 2: 4 5 6\nMetade 1: 1 2 3\n`
   - Negativos (`-10 -20 -30 40 50 60`) → `Metade 2: 40 50 60\nMetade 1: -10 -20 -30\n`
   - Todos zeros (`0 0 0 0 0 0`) → `Metade 2: 0 0 0\nMetade 1: 0 0 0\n`
   - Espelhado (`9 8 7 7 8 9`) → `Metade 2: 7 8 9\nMetade 1: 9 8 7\n`
   - Misto (`100 -1 50 25 0 -7`) → `Metade 2: 25 0 -7\nMetade 1: 100 -1 50\n`

3. **`D01_E05.c`:**
   - Normal (`4`: `11 22 33 44`) → `Direta: 11 22 33 44\nInversa: 44 33 22 11\n`
   - Borda `n = 1` (`1`: `-9`) → `Direta: -9\nInversa: -9\n`
   - Borda `n = 2` (`2`: `5 10`) → `Direta: 5 10\nInversa: 10 5\n`
   - Palíndromo numérico (`5`: `1 2 3 2 1`) → `Direta: 1 2 3 2 1\nInversa: 1 2 3 2 1\n`
   - Negativos (`3`: `-3 -2 -1`) → `Direta: -3 -2 -1\nInversa: -1 -2 -3\n`

4. **`D01_C02_corrigido.c`:**
   - Normal `n = 5` (`5`: `10 20 30 40 50`) → `Impares: 20 40\nInverso: 50 40 30 20 10\n`
   - Borda `n = 1` (`1`: `77`) → `Impares:\nInverso: 77\n`
   - Borda `n = 2` (`2`: `8 9`) → `Impares: 9\nInverso: 9 8\n`
   - Negativos `n = 4` (`4`: `-1 -2 -3 -4`) → `Impares: -2 -4\nInverso: -4 -3 -2 -1\n`
   - Todos zeros `n = 3` (`3`: `0 0 0`) → `Impares: 0\nInverso: 0 0 0\n`

5. **`D01_C03.c`:**
   - Normal (`4`: `10 20 30 40`) → `Primeiro: 10 | Ultimo: 40\nInverso: 40 30 20 10\n`
   - Borda `n = 1` (`1`: `-42`) → `Primeiro: -42 | Ultimo: -42\nInverso: -42\n`
   - Borda `n = 2` (`2`: `0 100`) → `Primeiro: 0 | Ultimo: 100\nInverso: 100 0\n`
   - Negativos (`5`: `-5 -4 -3 -2 -1`) → `Primeiro: -5 | Ultimo: -1\nInverso: -1 -2 -3 -4 -5\n`
   - Iguais (`3`: `7 7 7`) → `Primeiro: 7 | Ultimo: 7\nInverso: 7 7 7\n`
