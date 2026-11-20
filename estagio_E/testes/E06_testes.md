# Especificação de Testes — Bloco `E06`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, `#define MAX 20`, matrizes 2D fixas (sem VLAs, funções customizadas, `struct` ou alocação dinâmica), saídas em ASCII puro.
- **Comparação de saídas:** correspondência textual e numérica exata linha a linha.
- **Casos de teste registrados:** 30 casos (5 por arquivo `.c`) em [casos_E06.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/casos_E06.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`E06_E03_corrigido.c`:**
   - Produto clássico `2 x 3` por `3 x 2` (`1..6` × `7..12`) → `58 64 / 139 154`
   - Incompatível `2 x 3` por `2 x 2` (pegando `LA == LB` mas `CA != LB`) → `Multiplicacao impossivel`
   - Vetor linha × vetor coluna (`1 x 3` por `3 x 1`) → produto escalar `1 x 1` (`24`)
   - Vetor coluna × vetor linha (`3 x 1` por `1 x 2`) → matriz `3 x 2`
   - Quadrada `2 x 2` com negativos → `7 12 / 3 -6`

2. **`E06_E04.c`:**
   - Normal `2 x 3` por `3 x 2` → `Maior: 154 em (1, 1)`
   - Produto com todos os elementos negativos → `Maior: -5 em (0, 0)`
   - Empate no maior elemento (1ª ocorrência *row-major*) → `Maior: 3 em (0, 0)`
   - Retangular `3 x 2` por `2 x 2` → `Maior: 16 em (2, 1)`
   - Borda `1 x 1` negativo → `Maior: -20 em (0, 0)`

3. **`E06_E05.c`:**
   - Ambos `A*B` (`2 x 2`) e `B*A` (`3 x 3`) possíveis com dimensões distintas
   - `A*B` possível (`2 x 3` por `3 x 3` identidade), `B*A` impossível
   - `A*B` impossível, `B*A` possível (`2 x 2` por `3 x 2`)
   - Não comutatividade `2 x 2` (`A*B != B*A`)
   - Ambos `A*B` e `B*A` impossíveis (`2 x 3` e `2 x 3`)

4. **`E06_E06.c`:**
   - Normal `2 x 2` (`1 2 / 3 4`) → `7 10 / 15 22`, `Traco de A^2: 29`
   - Matriz identidade `3 x 3` → `I_3`, `Traco de A^2: 3`
   - Matriz de rotação `90°` (`0 1 / -1 0`) → `-I_2`, `Traco de A^2: -2`
   - Matriz `3 x 3` com negativos e zeros → `Traco de A^2: 9`
   - Borda `1 x 1` (`-3`) → `9`, `Traco de A^2: 9`

5. **`E06_C02_corrigido.c`:**
   - Retangular `2 x 3` por `3 x 2` (`LA != CB`, pegando bug `j < CA` e `k < LA`)
   - Retangular `2 x 2` por `2 x 3` (`CB > CA`)
   - `1 x 2` por `2 x 1` → `1 x 1` (`2`)
   - `3 x 1` por `1 x 3` → `3 x 3`
   - Borda `1 x 1` com zero → `0`

6. **`E06_C03.c`:**
   - Retangular `2 x 3` (`1 2 3 / 4 5 6`) → `14 32 / 32 77`
   - Identidade `2 x 2` → `1 0 / 0 1`
   - Linha única `1 x 4` → `14` (`1 x 1`)
   - Coluna única `3 x 1` → matriz `3 x 3` simétrica
   - Borda `1 x 1` (`-5`) → `25`
