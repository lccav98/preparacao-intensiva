# Especificação de Testes — Bloco `G04`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, protótipos antes de `main`, capacidade fixa (`int v[50]`), `const int v[]`, funções recursivas **estritamente sem `for`/`while`/`do-while`** (laço apenas em `main` para leitura de entrada), verificação `n <= 0` antes de acessar `v[n - 1]`, sem aritmética de ponteiros, sem `struct`, sem `malloc`/`free`, sem VLAs e saídas em ASCII puro.
- **Comparação de saídas e tolerância:** correspondência textual exata de saída (`stdout`).
- **Casos de teste registrados:** **25 casos** (5 por arquivo `.c`) em [casos_G04.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/casos_G04.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`G04_E03_corrigido.c` (`soma_positivos`):**
   - `5` / `3 -2 7 0 4` (mistura positivos, zero e negativo) → `Soma positivos: 14`
   - `4` / `-5 -1 -8 -2` (todos negativos) → `Soma positivos: 0`
   - `0` (borda vetor vazio `n = 0`) → `Soma positivos: 0`
   - `1` / `-9` (borda `n = 1` negativo) → `Soma positivos: 0`
   - `1` / `12` (borda `n = 1` positivo) → `Soma positivos: 12`

2. **`G04_E04.c` (`contar_positivos` + `soma_pares`):**
   - `5` / `4 -3 2 0 7` (mistura positivos, zero e negativos) → `Positivos: 3` / `Soma pares: 6`
   - `0` (borda vetor vazio `n = 0`) → `Positivos: 0` / `Soma pares: 0`
   - `4` / `-4 -3 -2 -1` (todos negativos) → `Positivos: 0` / `Soma pares: -6`
   - `3` / `1 3 5` (todos ímpares positivos) → `Positivos: 3` / `Soma pares: 0`
   - `1` / `8` (borda `n = 1` par positivo) → `Positivos: 1` / `Soma pares: 8`

3. **`G04_E05.c` (`contar_ocorrencias`):**
   - `6` / `3 7 3 2 3 9` / `x = 3` (múltiplas ocorrências) → `Ocorrencias: 3`
   - `4` / `1 2 3 4` / `x = 5` (nenhuma ocorrência) → `Ocorrencias: 0`
   - `0` / `x = 7` (borda vetor vazio `n = 0`) → `Ocorrencias: 0`
   - `5` / `-2 -2 -2 -2 -2` / `x = -2` (todos iguais ao alvo) → `Ocorrencias: 5`
   - `1` / `10` / `x = 10` (borda `n = 1` encontrado) → `Ocorrencias: 1`

4. **`G04_C02_corrigido.c` (`contar_acima`):**
   - `5` / `10 3 15 8 20` / `lim = 8` (ignora igual a `8`) → `Acima: 3`
   - `4` / `5 5 5 5` / `lim = 5` (todos iguais ao limite) → `Acima: 0`
   - `0` / `lim = 10` (borda vetor vazio `n = 0`) → `Acima: 0`
   - `3` / `-10 -5 -1` / `lim = -6` (negativos) → `Acima: 2`
   - `1` / `12` / `lim = 10` (borda `n = 1` acima) → `Acima: 1`

5. **`G04_C03.c` (`soma_intervalo_vetor`):**
   - `5` / `2 8 15 10 20` / `[8, 15]` (bordas inclusivas) → `Soma no intervalo: 33`
   - `4` / `1 2 3 4` / `[10, 20]` (nenhum no intervalo) → `Soma no intervalo: 0`
   - `0` / `[0, 10]` (borda vetor vazio `n = 0`) → `Soma no intervalo: 0`
   - `4` / `-5 -2 0 4` / `[-3, 0]` (negativos e zero) → `Soma no intervalo: -2`
   - `1` / `7` / `[7, 7]` (borda `n = 1`, intervalo unitário) → `Soma no intervalo: 7`
