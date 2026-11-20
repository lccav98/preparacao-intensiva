# Especificação de Testes — Bloco `F06`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, protótipos antes de `main`, vetores 1D com capacidade fixa (`50`), uso de `const` em parâmetros somente leitura, sem matrizes 2D, sem multi-arquivo, sem VLAs, sem `struct`, sem `malloc`/`free`, sem recursividade e saídas em ASCII puro.
- **Comparação de saídas e tolerância:**
  - Inteiros e sequências de inteiros: correspondência exata.
  - Valores reais (`%.2f` em `F06_C03.c`): correspondência textual exata e tolerância numérica de **`1e-2`**.
- **Casos de teste registrados:** **25 casos** (5 por arquivo `.c`) em [casos_F06.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/casos_F06.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`F06_E03_corrigido.c` (`contar_acima`):**
   - `5` / `10 3 15 8 20` / `limite = 8` → `Acima: 3` (ignora igual a `8`)
   - `4` / `5 5 5 5` / `limite = 5` → `Acima: 0` (fronteira estrita `>`)
   - `3` / `-10 -5 -1` / `limite = -6` → `Acima: 2` (negativos)
   - `1` / `12` / `limite = 10` → `Acima: 1` (borda `n = 1` positivo)
   - `1` / `10` / `limite = 10` → `Acima: 0` (borda `n = 1` empate)

2. **`F06_E04.c` (`produto_interno`):**
   - `3` / `1 2 3` / `4 5 6` → `Produto interno: 32`
   - `3` / `2 -1 4` / `-3 5 0` → `Produto interno: -11`
   - `2` / `1 -1` / `1 1` → `Produto interno: 0` (ortogonais)
   - `4` / `0 0 0 0` / `9 -8 7 6` → `Produto interno: 0`
   - `1` / `-4` / `-5` → `Produto interno: 20` (borda `n = 1`)

3. **`F06_E05.c` (`substituir_negativos` + `imprimir_vetor`):**
   - `5` / `3 -2 0 -7 8` → `3 0 0 0 8`
   - `4` / `-1 -2 -3 -4` → `0 0 0 0` (todos negativos)
   - `3` / `5 10 15` → `5 10 15` (nenhum negativo)
   - `1` / `-9` → `0` (borda `n = 1` negativo)
   - `1` / `0` → `0` (borda `n = 1` zero)

4. **`F06_C02_corrigido.c` (`soma_pares`):**
   - `5` / `2 3 4 5 6` → `Soma pares: 12`
   - `4` / `1 3 5 7` → `Soma pares: 0` (apenas ímpares)
   - `4` / `-4 3 -2 0` → `Soma pares: -6` (pares negativos e zero)
   - `1` / `8` → `Soma pares: 8` (borda `n = 1` par)
   - `1` / `-3` → `Soma pares: 0` (borda `n = 1` ímpar negativo)

5. **`F06_C03.c` (`estatisticas_vetor`):**
   - `3` / `10 20 30` → `Menor: 10` / `Maior: 30` / `Media: 20.00`
   - `4` / `-5 -2 -9 -4` → `Menor: -9` / `Maior: -2` / `Media: -5.00`
   - `1` / `7` → `Menor: 7` / `Maior: 7` / `Media: 7.00`
   - `3` / `1 2 4` → `Menor: 1` / `Maior: 4` / `Media: 2.33`
   - `4` / `5 5 5 5` → `Menor: 5` / `Maior: 5` / `Media: 5.00`
