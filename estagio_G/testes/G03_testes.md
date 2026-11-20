# Especificação de Testes — Bloco `G03`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, protótipos antes de `main`, funções recursivas lineares sobre inteiros **estritamente sem `for`/`while`/`do-while`**, sem vetores/strings, sem `struct`, sem `malloc`/`free`, sem VLAs e saídas em ASCII puro.
- **Comparação de saídas e tolerância:** correspondência textual exata de saída (`stdout`).
- **Casos de teste registrados:** **25 casos** (5 por arquivo `.c`) em [casos_G03.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/casos_G03.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`G03_E03_corrigido.c` (`contar_digitos` + `potencia`):**
   - `5832 2 5` (normal 4 dígitos, potência positiva) → `Digitos: 4` / `Potencia: 32`
   - `0 7 0` (borda `n = 0` e expoente `0`) → `Digitos: 1` / `Potencia: 1`
   - `7 3 0` (borda 1 dígito e expoente `0`) → `Digitos: 1` / `Potencia: 1`
   - `1000 -2 3` (base negativa, expoente ímpar) → `Digitos: 4` / `Potencia: -8`
   - `909 5 4` (zeros intercalados) → `Digitos: 3` / `Potencia: 625`

2. **`G03_E04.c` (`contar_digitos` + `soma_digitos_pares`):**
   - `4832` (mistura de dígitos pares e ímpares) → `Digitos: 4` / `Soma digitos pares: 14`
   - `0` (borda `n = 0`) → `Digitos: 1` / `Soma digitos pares: 0`
   - `1357` (somente dígitos ímpares) → `Digitos: 4` / `Soma digitos pares: 0`
   - `2040` (pares com zeros) → `Digitos: 4` / `Soma digitos pares: 6`
   - `8` (borda 1 dígito par) → `Digitos: 1` / `Soma digitos pares: 8`

3. **`G03_E05.c` (`produto_digitos` + `maior_digito`):**
   - `234` (normal sem zeros) → `Produto: 24` / `Maior digito: 4`
   - `0` (borda `n = 0`) → `Produto: 0` / `Maior digito: 0`
   - `7` (borda 1 dígito) → `Produto: 7` / `Maior digito: 7`
   - `508` (dígito zero no meio) → `Produto: 0` / `Maior digito: 8`
   - `919` (maior dígito repetido nas pontas) → `Produto: 81` / `Maior digito: 9`

4. **`G03_C02_corrigido.c` (`contar_zeros`):**
   - `1050` (normal com dois zeros) → `Zeros: 2`
   - `0` (borda `n = 0` — exige `1` zero) → `Zeros: 1`
   - `5` (borda 1 dígito não-zero) → `Zeros: 0`
   - `1000` (múltiplos zeros à direita) → `Zeros: 3`
   - `999` (sem zeros) → `Zeros: 0`

5. **`G03_C03.c` (`contar_digitos_maiores` + `potencia`):**
   - `5832 4 3 4` (normal) → `Maiores que lim: 2` / `Potencia: 81`
   - `0 0 5 0` (borda `n = 0`, `lim = 0`, `e = 0`) → `Maiores que lim: 0` / `Potencia: 1`
   - `0 -1 2 3` (borda `n = 0`, `lim = -1`) → `Maiores que lim: 1` / `Potencia: 8`
   - `999 8 -3 3` (todos acima de `lim`, base negativa) → `Maiores que lim: 3` / `Potencia: -27`
   - `1234 4 10 2` (nenhum estritamente maior que `4`) → `Maiores que lim: 0` / `Potencia: 100`
