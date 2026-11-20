# Especificação de Testes — Bloco `E05`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, `#define MAX 20`, matrizes 2D fixas (sem VLAs, funções customizadas, `struct` ou alocação dinâmica), saídas em ASCII puro.
- **Comparação de saídas:** correspondência textual e numérica exata linha a linha.
- **Casos de teste registrados:** 25 casos (5 por arquivo `.c`) em [casos_E05.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/casos_E05.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`E05_E03_corrigido.c`:**
   - Retangular `2 x 3` → transposta `3 x 2` e `Simetrica: Nao`
   - Quadrada simétrica `3 x 3` → transposta `3 x 3` e `Simetrica: Sim`
   - Quadrada não simétrica com falha na última linha (`(1, 2) != (2, 1)`) → `Simetrica: Nao`
   - Borda `1 x 4` (linha única → coluna única `4 x 1`) → `Simetrica: Nao`
   - Borda `1 x 1` (`42`) → transposta `1 x 1` e `Simetrica: Sim`

2. **`E05_E04.c`:**
   - Retangular `2 x 3` com positivos e negativos → soma `2 x 3` e transposta `3 x 2`
   - Quadrada `2 x 2` anulando para zeros → soma nula e transposta nula
   - Borda `3 x 1` (vetor coluna → vetor linha `1 x 3`)
   - Borda `1 x 3` (vetor linha → vetor coluna `3 x 1`)
   - Borda `1 x 1` (`-7 + 12 = 5`)

3. **`E05_E05.c`:**
   - Quadrada não simétrica `3 x 3` → `Simetrica A: Nao`, `A + A^T`, `Simetrica A + A^T: Sim`
   - Quadrada já simétrica `2 x 2` → `Simetrica A: Sim`, `A + A^T = 2A`, `Simetrica A + A^T: Sim`
   - Antissimétrica `3 x 3` (`A^T = -A`) → `Simetrica A: Nao`, `A + A^T` toda nula, `Simetrica A + A^T: Sim`
   - Borda `1 x 1` (`-5`) → `Simetrica A: Sim`, `-10`, `Simetrica A + A^T: Sim`
   - Quadrada `3 x 3` falhando na borda superior direita `(0, 2)` → `Simetrica A: Nao`, `Simetrica A + A^T: Sim`

4. **`E05_C02_corrigido.c`:**
   - Normal compatível `2 x 3` + `2 x 3` → `Soma:`
   - Incompatível apenas nas colunas (`2 x 3` vs `2 x 4`) → `Soma impossivel`
   - Incompatível apenas nas linhas (`3 x 2` vs `2 x 2`) → `Soma impossivel`
   - Incompatível em ambos (`2 x 3` vs `3 x 2`) → `Soma impossivel`
   - Borda `1 x 1` compatível (`-3 + 8 = 5`) → `Soma:`

5. **`E05_C03.c`:**
   - Soma de duas matrizes não simétricas que resulta em matriz simétrica `2 x 2` → `Simetrica (A + B): Sim`
   - Soma que resulta em matriz não simétrica `3 x 3` → `Simetrica (A + B): Nao`
   - Soma de `A` com `-A` (matriz nula) `2 x 2` → `Simetrica (A + B): Sim`
   - Borda `1 x 1` (`10 + -4 = 6`) → `Simetrica (A + B): Sim`
   - Falha de simetria apenas no último par `(1, 2)` de `3 x 3` → `Simetrica (A + B): Nao`
