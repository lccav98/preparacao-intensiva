# Especificação de Testes — Bloco `E04`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, `int main(void)` sem funções extras, matrizes quadradas 2D com `#define` (sem VLAs, `struct` ou `malloc`/`free`), saídas em ASCII puro.
- **Comparação de saídas e tolerância:**
  - Saída inteira e texto (`SIM`/`NAO`) com correspondência exata.
- **Casos de teste registrados:** 25 casos (5 por arquivo `.c`) em [casos_E04.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/casos_E04.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`E04_E03_corrigido.c` (`3 x 3`: diagonal secundária e identidade):**
   - Identidade `3 x 3` → `Diag secundaria: 0 1 0`, `Identidade: SIM`
   - Matriz só de `1`s (testa falha `i != j`) → `Diag secundaria: 1 1 1`, `Identidade: NAO`
   - Erro no início com `m[2][2] == 1` (`0 0 0 / 0 1 0 / 0 0 1`, testa `else`) → `Diag secundaria: 0 1 0`, `Identidade: NAO`
   - Diagonal principal ok e `(0, 2) = 5` → `Diag secundaria: 5 1 0`, `Identidade: NAO`
   - Valores mistos e negativos → `Diag secundaria: 7 0 9`, `Identidade: NAO`

2. **`E04_E04.c` (`4 x 4`: diagonais $O(N)$ e somas acima/abaixo):**
   - Matriz da errata (`soma_acima == 10`) → Principal `1 5 9 4`, Secundaria `1 2 8 3`, Acima `10`, Abaixo `29`
   - Identidade `4 x 4` → Principal `1 1 1 1`, Secundaria `0 0 0 0`, Acima `0`, Abaixo `0`
   - Sequência `1..16` → Principal `1 6 11 16`, Secundaria `4 7 10 13`, Acima `36`, Abaixo `66`
   - Todos zeros → Principal `0 0 0 0`, Secundaria `0 0 0 0`, Acima `0`, Abaixo `0`
   - Negativos e positivos → Principal `-1 2 -7 8`, Secundaria `-4 3 -6 2`, Acima `-10`, Abaixo `2`

3. **`E04_E05.c` (`n x n`: diagonais e identidade):**
   - Normal `3 x 3` identidade → `Diag principal: 1 1 1`, `Diag secundaria: 0 1 0`, `Identidade: SIM`
   - Borda `1 x 1` identidade (`1`) → `Diag principal: 1`, `Diag secundaria: 1`, `Identidade: SIM`
   - Borda `1 x 1` não-identidade (`5`) → `Diag principal: 5`, `Diag secundaria: 5`, `Identidade: NAO`
   - Borda `2 x 2` antidiagonal de `1`s → `Diag principal: 0 0`, `Diag secundaria: 1 1`, `Identidade: NAO`
   - Normal `4 x 4` → `Diag principal: 10 20 30 40`, `Diag secundaria: 4 7 10 13`, `Identidade: NAO`

4. **`E04_C02_corrigido.c` (`4 x 4`: soma secundária, soma abaixo e identidade):**
   - Identidade `4 x 4` → `Soma sec: 0`, `Soma abaixo: 0`, `Identidade: SIM`
   - Falso positivo com `m[3][3] == 1` (`m[1][0] = 2`) → `Soma sec: 0`, `Soma abaixo: 2`, `Identidade: NAO`
   - Sequência `1..16` → `Soma sec: 34`, `Soma abaixo: 66`, `Identidade: NAO`
   - Secundária e abaixo preenchidas → `Soma sec: 26`, `Soma abaixo: 15`, `Identidade: NAO`
   - Negativos e positivos → `Soma sec: -7`, `Soma abaixo: -27`, `Identidade: NAO`

5. **`E04_C03.c` (`n x n`: somas principal/secundária/acima/abaixo e identidade):**
   - Identidade `3 x 3` → Principal `3`, Secundaria `1`, Acima `0`, Abaixo `0`, `Identidade: SIM`
   - Borda `1 x 1` (`1`) → Principal `1`, Secundaria `1`, Acima `0`, Abaixo `0`, `Identidade: SIM`
   - Borda `1 x 1` (`0`) → Principal `0`, Secundaria `0`, Acima `0`, Abaixo `0`, `Identidade: NAO`
   - `4 x 4` com `soma_acima = 10` → Principal `19`, Secundaria `14`, Acima `10`, Abaixo `29`, `Identidade: NAO`
   - `2 x 2` mista → Principal `-7`, Secundaria `10`, Acima `3`, Abaixo `7`, `Identidade: NAO`
