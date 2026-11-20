# Especificação de Testes — Bloco `F08`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comandos de compilação multi-arquivo (nunca passar `.h` ao `gcc`):**
  - `F08_E03_corrigido`: `gcc -std=c99 -Wall -Wextra solucoes/F08_E03_corrigido/main.c solucoes/F08_E03_corrigido/calc.c -o prog`
  - `F08_E04`: `gcc -std=c99 -Wall -Wextra solucoes/F08_E04/main.c solucoes/F08_E04/vetor.c -o prog`
  - `F08_E05`: `gcc -std=c99 -Wall -Wextra solucoes/F08_E05/main.c solucoes/F08_E05/matriz.c -o prog`
  - `F08_E06`: `gcc -std=c99 -Wall -Wextra solucoes/F08_E06/main.c solucoes/F08_E06/texto.c -o prog`
  - `F08_C03`: `gcc -std=c99 -Wall -Wextra solucoes/F08_C03/main.c solucoes/F08_C03/estatistica.c -o prog`
- **Restrições verificadas nos projetos `.h`/`.c`:** guardas `#ifndef`/`#define`/`#endif` em todos os `.h`, apenas `#define`s e protótipos no `.h`, `#include "..."` para cabeçalhos locais, `const` em parâmetros somente leitura, sem VLAs, sem `struct`, sem `malloc`/`free`, sem recursividade e saídas em ASCII puro.
- **Comparação de saídas e tolerância:**
  - Inteiros e strings: correspondência textual exata.
  - Valores reais (`%.2f` em `F08_C03`): correspondência textual exata e tolerância numérica de **`1e-2`**.
- **Casos de teste registrados:** **25 casos** (5 por projeto multi-arquivo) em [casos_F08.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/casos_F08.json).

---

## Casos de Teste por Projeto Multi-Arquivo (5 casos por projeto: normal + bordas críticas)

1. **`F08_E03_corrigido` (`calc.h` + `calc.c` + `main.c`):**
   - `1 6` (crescente) → `Soma: 21` / `Pares: 3`
   - `6 1` (decrescente) → `Soma: 21` / `Pares: 3`
   - `-3 3` (negativos e positivos) → `Soma: 0` / `Pares: 3` (`-2, 0, 2`)
   - `4 4` (intervalo unitário par) → `Soma: 4` / `Pares: 1`
   - `5 5` (intervalo unitário ímpar) → `Soma: 5` / `Pares: 0`

2. **`F08_E04` (`vetor.h` + `vetor.c` + `main.c`):**
   - `4` / `10 20 5 15` → `Soma: 50` / `Maior: 20`
   - `3` / `-8 -2 -15` → `Soma: -25` / `Maior: -2` (todos negativos)
   - `5` / `0 0 0 0 0` → `Soma: 0` / `Maior: 0`
   - `1` / `-7` → `Soma: -7` / `Maior: -7` (borda `n = 1`)
   - `4` / `9 9 3 9` → `Soma: 30` / `Maior: 9` (empate no máximo)

3. **`F08_E05` (`matriz.h` + `matriz.c` + `main.c`):**
   - `2 1` (`1 2 3` / `4 5 6`) → `Soma coluna 1: 7` / `Maior: 6`
   - `3 0` (`-5 1 2` / `-3 4 0` / `-2 8 -1`) → `Soma coluna 0: -10` / `Maior: 8`
   - `1 2` (`10 20 30`) → `Soma coluna 2: 30` / `Maior: 30` (borda `linhas = 1`)
   - `2 2` (`-9 -8 -7` / `-6 -5 -4`) → `Soma coluna 2: -11` / `Maior: -4` (todos negativos)
   - `2 0` (`0 0 0` / `0 0 0`) → `Soma coluna 0: 0` / `Maior: 0`

4. **`F08_E06` (`texto.h` + `texto.c` + `main.c`):**
   - `"Banana 2026"` / `'a'` → `Ocorrencias: 3` / `Maiusculas: BANANA 2026`
   - `"Aba"` / `'a'` → `Ocorrencias: 1` / `Maiusculas: ABA` (contagem antes de converter)
   - `"xyz"` / `'k'` → `Ocorrencias: 0` / `Maiusculas: XYZ` (ausente)
   - `"C99!"` / `'9'` → `Ocorrencias: 2` / `Maiusculas: C99!` (dígitos/pontuação intactos)
   - `"a"` / `'a'` → `Ocorrencias: 1` / `Maiusculas: A` (borda 1 caractere)

5. **`F08_C03` (`estatistica.h` + `estatistica.c` + `main.c`):**
   - `4` / `10 20 30 40` / `15 35` → `Media: 25.00` / `No intervalo: 2`
   - `3` / `1 2 4` / `0 5` → `Media: 2.33` / `No intervalo: 3`
   - `5` / `-5 0 5 10 15` / `0 10` → `Media: 5.00` / `No intervalo: 3` (fronteiras inclusivas)
   - `3` / `2 4 6` / `7 10` → `Media: 4.00` / `No intervalo: 0`
   - `1` / `42` / `42 42` → `Media: 42.00` / `No intervalo: 1`
