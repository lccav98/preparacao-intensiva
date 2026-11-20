# Especificação de Testes — Bloco `E03`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, `int main(void)` sem funções extras, matrizes 2D com `#define` (sem VLAs, `struct` ou `malloc`/`free`), saídas em ASCII puro.
- **Comparação de saídas e tolerância:**
  - Saída inteira e formatação textual com correspondência exata.
- **Casos de teste registrados:** 25 casos (5 por arquivo `.c`) em [casos_E03.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/casos_E03.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`E03_E03_corrigido.c` (`3 x 4`: soma das linhas e das colunas):**
   - Normal (`1..12`) → `Linhas: 10 26 42`, `Colunas: 15 18 21 24`
   - Todos zeros (`0` x 12) → `Linhas: 0 0 0`, `Colunas: 0 0 0 0`
   - Cancelamento positivo/negativo (`-1 -2 -3 -4 / 1 2 3 4 / 5 -5 5 -5`) → `Linhas: -10 10 0`, `Colunas: 5 -5 5 -5`
   - Esparsa (`10 0 0 0 / 0 20 0 0 / 0 0 30 40`) → `Linhas: 10 20 70`, `Colunas: 10 20 30 40`
   - Todos negativos (`-5` x 12) → `Linhas: -20 -20 -20`, `Colunas: -15 -15 -15 -15`

2. **`E03_E04.c` (`3 x 4`: fatiamento ordinal de linha e coluna):**
   - Normal (`1..12`, `lin=2, col=3`) → `Linha 2: 5 6 7 8` (`26`) e `Coluna 3: 3 7 11` (`21`)
   - Borda primeira linha e primeira coluna (`lin=1, col=1`) → `Linha 1: 10 20 30 40` (`100`) e `Coluna 1: 10 1 -5` (`6`)
   - Borda última linha e última coluna (`lin=3, col=4`) → `Linha 3: -5 -5 -5 -5` (`-20`) e `Coluna 4: 40 4 -5` (`39`)
   - Zeros (`lin=2, col=2`) → somas `0` e `0`
   - Negativos (`-1..-12`, `lin=1, col=4`) → `Linha 1: -1 -2 -3 -4` (`-10`) e `Coluna 4: -4 -8 -12` (`-24`)

3. **`E03_E05.c` (`4 x 4`: somas por linha/coluna + maior linha 1ª ocorrência):**
   - Normal King Cap. 8 → `Linhas: 20 26 39 27`, `Colunas: 28 23 35 26`, `Maior linha: 2 (39)`
   - Empate de maior linha (`10 10 0 10`) → `Maior linha: 0 (10)`
   - Todas linhas negativas → `Linhas: -11 -4 -16 -10`, `Maior linha: 1 (-4)`
   - Todos zeros → `Linhas: 0 0 0 0`, `Colunas: 0 0 0 0`, `Maior linha: 0 (0)`
   - Maior na última linha → `Linhas: 4 8 12 16`, `Colunas: 10 10 10 10`, `Maior linha: 3 (16)`

4. **`E03_C02_corrigido.c` (`3 x 5`: somas das linhas + fatiamento da coluna `k` base 0):**
   - Normal `k = 2` (`1..15`) → `Linhas: 15 40 65`, `Coluna 2: 3 8 13`
   - Borda `k = 0` → `Linhas: 11 22 33`, `Coluna 0: 10 20 30`
   - Borda `k = 4` (maior que `L = 3`, testa bug de limite) → `Linhas: 11 22 33`, `Coluna 4: 1 2 3`
   - Negativos e zeros (`k = 3`) → `Linhas: -5 -10 0`, `Coluna 3: -1 -2 0`
   - Zeros (`k = 1`) → `Linhas: 0 0 0`, `Coluna 1: 0 0 0`

5. **`E03_C03.c` (`l x c`: somas das linhas e das colunas):**
   - Normal `2 x 3` → `Linhas: 6 15`, `Colunas: 5 7 9`
   - Borda `1 x 1` (`-9`) → `Linhas: -9`, `Colunas: -9`
   - Borda `1 x 4` → `Linhas: 0`, `Colunas: 2 -3 5 -4`
   - Borda `4 x 1` → `Linhas: 10 -2 5 7`, `Colunas: 20`
   - Retangular `3 x 2` → `Linhas: 3 -4 9`, `Colunas: 9 -1`
