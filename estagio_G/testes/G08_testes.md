# Especificação de Testes — Bloco `G08`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, proibição estrita de laços (`for`, `while`, `do-while`) dentro de funções recursivas, dois casos base (`n == 0` e `n == 1`) em `fib` e `potencia_rapida`, variável local `p` evitando dupla chamada em `n / 2`, sem `struct`, sem `malloc`/`free`, sem `gets(`, sem VLAs e saídas em ASCII puro.
- **Comparação de saídas e tolerância:**
  - Inteiros: correspondência textual exata.
  - Valores reais (`%.2f`): correspondência textual exata e tolerância numérica de **`1e-2`**.
- **Casos de teste registrados:** **25 casos** (5 por arquivo `.c`) em [casos_G08.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/casos_G08.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`G08_E03_corrigido.c` (`fib` + `potencia_rapida` com contador):**
   - `2.0 8 5` → `Potencia: 256.00` / `Chamadas: 4` / `Fib: 5`
   - `3.0 5 6` → `Potencia: 243.00` / `Chamadas: 3` / `Fib: 8`
   - `5.0 0 0` (borda `n=0, k=0`) → `Potencia: 1.00` / `Chamadas: 1` / `Fib: 0`
   - `2.5 1 1` (borda `n=1, k=1`) → `Potencia: 2.50` / `Chamadas: 1` / `Fib: 1`
   - `-2.0 3 7` (base negativa + expoente ímpar) → `Potencia: -8.00` / `Chamadas: 2` / `Fib: 13`

2. **`G08_E04.c` (`fib_contado`):**
   - `5` → `Fib: 5` / `Chamadas: 15`
   - `0` (caso base 0) → `Fib: 0` / `Chamadas: 1`
   - `1` (caso base 1) → `Fib: 1` / `Chamadas: 1`
   - `4` → `Fib: 3` / `Chamadas: 9`
   - `8` (crescimento exponencial) → `Fib: 21` / `Chamadas: 67`

3. **`G08_E05.c` (`pot_linear` vs. `pot_rapida`):**
   - `2.0 8` → `Resultado: 256.00` / `Chamadas linear: 8` / `Chamadas rapida: 4`
   - `2.0 7` → `Resultado: 128.00` / `Chamadas linear: 7` / `Chamadas rapida: 3`
   - `5.0 0` (borda `n=0`) → `Resultado: 1.00` / `Chamadas linear: 1` / `Chamadas rapida: 1`
   - `3.5 1` (borda `n=1`) → `Resultado: 3.50` / `Chamadas linear: 1` / `Chamadas rapida: 1`
   - `1.0 32` (`n = 32`: 32 vs 6 chamadas) → `Resultado: 1.00` / `Chamadas linear: 32` / `Chamadas rapida: 6`

4. **`G08_E06.c` (`potencia_rapida` com negativos/positivos e contagem de multiplicações):**
   - `2.0 8` → `Potencia: 256.00` / `Multiplicacoes: 3`
   - `3.0 5` → `Potencia: 243.00` / `Multiplicacoes: 3`
   - `2.0 -2` (expoente negativo par) → `Potencia: 0.25` / `Multiplicacoes: 1`
   - `5.0 0` (borda `n=0`) → `Potencia: 1.00` / `Multiplicacoes: 0`
   - `2.0 -1` (expoente negativo `-1`) → `Potencia: 0.50` / `Multiplicacoes: 0`

5. **`G08_C03.c` (`fib` + `potencia_rapida`):**
   - `2.0 10 6` → `Potencia: 1024.00` / `Chamadas: 4` / `Fib(K): 8`
   - `2.0 0 0` → `Potencia: 1.00` / `Chamadas: 1` / `Fib(K): 0`
   - `4.0 1 1` → `Potencia: 4.00` / `Chamadas: 1` / `Fib(K): 1`
   - `1.5 4 4` → `Potencia: 5.06` / `Chamadas: 3` / `Fib(K): 3`
   - `-3.0 3 7` → `Potencia: -27.00` / `Chamadas: 2` / `Fib(K): 13`
