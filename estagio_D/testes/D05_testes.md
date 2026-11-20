# Especificação de Testes — Bloco `D05`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, `#define MAX 100`, vetores 1D fixos (sem VLAs, funções extras, strings ou matrizes 2D), saídas em ASCII puro.
- **Comparação de saídas e tolerância:**
  - Correspondência textual e numérica exata.
- **Casos de teste registrados:** 30 casos (5 por arquivo `.c`) em [casos_D05.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/casos_D05.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`D05_E03_corrigido.c`:**
   - Kernel assimétrico (`4`: `2 4 1 3`, `3`: `1 2 3`) → `Convolucao: 15 17\n`
   - Kernel assimétrico (`4`: `4 1 3 2`, `3`: `1 2 5`) → `Convolucao: 25 13\n`
   - Borda `m == n` (`3`: `10 20 30`, `3`: `1 0 -1`) → `Convolucao: 20\n`
   - Borda `m = 1` (`4`: `2 -3 4 0`, `1`: `3`) → `Convolucao: 6 -9 12 0\n`
   - Borda `n = 1, m = 1` (`1`: `-5`, `1`: `-2`) → `Convolucao: 10\n`

2. **`D05_E04.c`:**
   - Sobreposição clássica (`5`: `1 2 1 2 1`, `3`: `1 2 1`) → `Ocorrencias: 2\nIndices: 0 2\n`
   - Todos iguais sobrepostos (`4`: `7 7 7 7`, `2`: `7 7`) → `Ocorrencias: 3\nIndices: 0 1 2\n`
   - Nenhuma ocorrência (`5`: `1 2 3 4 5`, `2`: `3 5`) → `Ocorrencias: 0\nIndices: nenhum\n`
   - Casamento apenas na última janela (`4`: `9 8 1 2`, `2`: `1 2`) → `Ocorrencias: 1\nIndices: 2\n`
   - Borda `m == n` (`3`: `-1 0 1`, `3`: `-1 0 1`) → `Ocorrencias: 1\nIndices: 0\n`

3. **`D05_E05.c`:**
   - Normal com kernel assimétrico (`5`: `1 3 2 5 4`, `3`: `1 0 2`) → `Resultado (3): 4 11 8\nMaior convolucao: 11 (indice 1)\n`
   - Empate no maior valor (1ª ocorrência) (`5`: `1 2 1 2 1`, `2`: `1 2`) → `Resultado (4): 4 5 4 5\nMaior convolucao: 5 (indice 1)\n`
   - Todos negativos (`4`: `-5 -2 -8 -1`, `2`: `1 3`) → `Resultado (3): -17 -14 -25\nMaior convolucao: -14 (indice 1)\n`
   - Borda `m == n` (`3`: `2 5 1`, `3`: `4 1 2`) → `Resultado (1): 13\nMaior convolucao: 13 (indice 0)\n`
   - Kernel de 1 elemento negativo (`3`: `3 -4 2`, `1`: `-2`) → `Resultado (3): -6 8 -4\nMaior convolucao: 8 (indice 1)\n`

4. **`D05_E06.c`:**
   - Sobreposição + convolução (`5`: `1 2 1 2 1`, `2`: `1 2`) → `Ocorrencias: 2\nConvolucao: 4 5 4 5\n`
   - Borda `m > n` (`2`: `5 6`, `3`: `5 6 7`) → `Ocorrencias: 0\nConvolucao: vazia\n`
   - Borda `m == n` igual (`3`: `4 5 6`, `3`: `4 5 6`) → `Ocorrencias: 1\nConvolucao: 73\n`
   - Borda `m = 1` (`4`: `3 1 3 3`, `1`: `3`) → `Ocorrencias: 3\nConvolucao: 9 3 9 9\n`
   - Sem ocorrência com negativos (`4`: `-1 2 -3 4`, `2`: `-2 1`) → `Ocorrencias: 0\nConvolucao: -5 8 -11\n`

5. **`D05_C02_corrigido.c`:**
   - Sobreposição (`3`: `1 1 1`, `2`: `1 1`) → `Ocorrencias: 2\n`
   - Falha antes de casar no final (`5`: `9 0 1 2 3`, `2`: `2 3`) → `Ocorrencias: 1\n` (pega os 3 bugs: reset de `casou` e `i <= n - m`)
   - Sem ocorrência (`4`: `1 2 1 3`, `2`: `2 2`) → `Ocorrencias: 0\n`
   - Borda `m == n` (`2`: `5 5`, `2`: `5 5`) → `Ocorrencias: 1\n`
   - Sobreposição longa (`6`: `1 0 1 0 1 0`, `3`: `1 0 1`) → `Ocorrencias: 2\n`

6. **`D05_C03.c`:**
   - Normal kernel assimétrico (`5`: `1 2 3 4 5`, `3`: `1 2 4`) → `Tamanho: 3\nValores: 11 18 25\nSoma total: 54\n`
   - Negativos (`4`: `-2 3 -1 4`, `2`: `2 -3`) → `Tamanho: 3\nValores: 12 -11 11\nSoma total: 12\n`
   - Borda `m == n` (`3`: `2 0 -1`, `3`: `5 3 1`) → `Tamanho: 1\nValores: -3\nSoma total: -3\n`
   - Borda `m = 1` (`3`: `4 -1 2`, `1`: `10`) → `Tamanho: 3\nValores: 40 -10 20\nSoma total: 50\n`
   - Tudo zero (`4`: `0 0 0 0`, `2`: `3 7`) → `Tamanho: 3\nValores: 0 0 0\nSoma total: 0\n`
