# Especificação de Testes — Bloco `G05`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, protótipos antes de `main`, capacidade fixa (`int v[50]`), `const int v[]`, funções recursivas **estritamente sem `for`/`while`/`do-while`** (laço apenas em `main` para leitura de entrada), chamada recursiva única em `maior`/`menor`, caso base `n == 1` para extremos/média, sem strings, sem `struct`, sem `malloc`/`free`, sem VLAs e saídas em ASCII puro.
- **Comparação de saídas e tolerância:**
  - Inteiros e texto: correspondência exata.
  - Valores reais (`%.2f` em `G05_E04.c`, `G05_E06.c` e `G05_C03.c`): correspondência textual exata e tolerância numérica de **`1e-2`**.
- **Casos de teste registrados:** **30 casos** (5 por arquivo `.c`) em [casos_G05.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/casos_G05.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`G05_E03_corrigido.c` (`maior_vetor` + `contem`):**
   - `5` / `4 9 12 7 3` / `x = 12` (parada antecipada no meio) → `Maior: 12` / `Contem: 1`
   - `4` / `-10 -3 -25 -8` / `x = -3` (todos negativos, encontrado) → `Maior: -3` / `Contem: 1`
   - `4` / `-10 -3 -25 -8` / `x = 0` (todos negativos, ausente — testa `n <= 0` antes de `v[n - 1]`) → `Maior: -3` / `Contem: 0`
   - `1` / `-7` / `x = -7` (borda `n = 1` encontrado) → `Maior: -7` / `Contem: 1`
   - `1` / `5` / `x = 9` (borda `n = 1` ausente) → `Maior: 5` / `Contem: 0`

2. **`G05_E04.c` (`media_vetor`):**
   - `4` / `10 20 30 40` (média exata) → `Media: 25.00`
   - `3` / `1 2 4` (dízima `2.333...`) → `Media: 2.33`
   - `1` / `7` (borda `n = 1`) → `Media: 7.00`
   - `4` / `-5 -2 -9 -4` (todos negativos) → `Media: -5.00`
   - `3` / `5 6 6` (arredondamento `5.666...`) → `Media: 5.67`

3. **`G05_E05.c` (`menor_vetor` + `contem`):**
   - `5` / `8 3 15 2 9` / `x = 15` (normal encontrado) → `Menor: 2` / `Encontrado: Sim`
   - `4` / `10 20 30 40` / `x = 25` (crescente ausente) → `Menor: 10` / `Encontrado: Nao`
   - `4` / `-5 -12 -3 -8` / `x = -12` (todos negativos) → `Menor: -12` / `Encontrado: Sim`
   - `1` / `4` / `x = 4` (borda `n = 1` encontrado) → `Menor: 4` / `Encontrado: Sim`
   - `1` / `-1` / `x = 0` (borda `n = 1` ausente) → `Menor: -1` / `Encontrado: Nao`

4. **`G05_E06.c` (`maior_vetor` + `media_vetor`):**
   - `5` / `10 20 30 40 50` (crescente) → `Maior: 50` / `Media: 30.00`
   - `3` / `2 5 7` (dízima `4.666...`) → `Maior: 7` / `Media: 4.67`
   - `4` / `-8 -3 -12 -5` (todos negativos) → `Maior: -3` / `Media: -7.00`
   - `1` / `-4` (borda `n = 1` negativo) → `Maior: -4` / `Media: -4.00`
   - `4` / `0 0 0 5` (fração `.25`) → `Maior: 5` / `Media: 1.25`

5. **`G05_C02.c` (`indice_ultimo`):**
   - `5` / `4 7 2 7 9` / `x = 7` (múltiplas ocorrências → último índice) → `Indice: 3`
   - `4` / `10 20 30 40` / `x = 10` (no índice `0`) → `Indice: 0`
   - `4` / `10 20 30 40` / `x = 99` (ausente) → `Indice: -1`
   - `0` / `x = 5` (borda vetor vazio `n = 0`) → `Indice: -1`
   - `1` / `-3` / `x = -3` (borda `n = 1` encontrado) → `Indice: 0`

6. **`G05_C03.c` (`media_vetor` + `contar_acima`):**
   - `4` / `10 20 30 40` (média `25.00`, 2 acima) → `Media: 25.00` / `Acima da media: 2`
   - `3` / `1 2 4` (média `2.33`, 1 acima) → `Media: 2.33` / `Acima da media: 1`
   - `4` / `5 5 5 5` (todos iguais à média) → `Media: 5.00` / `Acima da media: 0`
   - `4` / `-10 -4 -2 0` (negativos e zero, `-4` igual não conta) → `Media: -4.00` / `Acima da media: 2`
   - `1` / `12` (borda `n = 1`) → `Media: 12.00` / `Acima da media: 0`
