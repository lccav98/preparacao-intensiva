# Especificação de Testes — Bloco `E02`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, `int main(void)` sem funções extras, matrizes 2D com `#define` (sem VLAs, `struct` ou `malloc`/`free`), saídas em ASCII puro.
- **Comparação de saídas e tolerância:**
  - Inteiros e texto: correspondência exata.
  - Valores reais (`%.2f` em `E02_E04.c`): correspondência textual exata e tolerância numérica de **`1e-2`**.
- **Casos de teste registrados:** 25 casos (5 por arquivo `.c`) em [casos_E02.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/casos_E02.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`E02_E03_corrigido.c` (`3 x 3`: soma, maior 1ª ocorrência, busca 2D):**
   - Normal com alvo repetido (`1 5 3 / 5 9 2 / 9 4 5`, `alvo=5`) → `Soma: 43`, `Maior: 9 (1, 1)`, `Alvo: (0, 1)`
   - Todos negativos (`-8 -3 -9 / -2 -7 -2 / -10 -2 -5`, `alvo=-2`) → `Soma: -48`, `Maior: -2 (1, 0)`, `Alvo: (1, 0)`
   - Alvo ausente (`1 2 3 / 4 5 6 / 7 8 9`, `alvo=10`) → `Soma: 45`, `Maior: 9 (2, 2)`, `Alvo: nao encontrado`
   - Todos zeros (`0` x 9, `alvo=0`) → `Soma: 0`, `Maior: 0 (0, 0)`, `Alvo: (0, 0)`
   - Alvo na última posição (`2 4 6 / 8 10 12 / 14 16 18`, `alvo=18`) → `Soma: 90`, `Maior: 18 (2, 2)`, `Alvo: (2, 2)`

2. **`E02_E04.c` (`3 x 4`: média real e contagem estritamente acima):**
   - Normal `1..12` → `Media: 6.50`, `Acima da media: 6`
   - Todos iguais (`5` x 12) → `Media: 5.00`, `Acima da media: 0`
   - Média exata presente na matriz (`2 2 2 2 / 4 4 4 4 / 6 6 6 6`, média `4.00`) → `Media: 4.00`, `Acima da media: 4`
   - Negativos (`-10 -20 -30 -40 / -10 -20 -30 -40 / -10 -20 -30 -40`) → `Media: -25.00`, `Acima da media: 6`
   - Um outlier positivo (`0` x 11 + `12`) → `Media: 1.00`, `Acima da media: 1`

3. **`E02_E05.c` (`4 x 5`: soma, maior e menor 1ª ocorrência):**
   - Normal `1..20` → `Soma: 210`, `Maior: 20 (3, 4)`, `Menor: 1 (0, 0)`
   - Todos negativos com empates (`-5`..`-1`) → `Soma: -60`, `Maior: -1 (0, 4)`, `Menor: -5 (0, 0)`
   - Todos iguais (`7` x 20) → `Soma: 140`, `Maior: 7 (0, 0)`, `Menor: 7 (0, 0)`
   - Grandes valores (`1000..1019`) → `Soma: 20190`, `Maior: 1019 (3, 4)`, `Menor: 1000 (0, 0)`
   - Extremos repetidos em linhas distintas (`10 20 30 40 50` x 4) → `Soma: 600`, `Maior: 50 (0, 4)`, `Menor: 10 (0, 0)`

4. **`E02_C02_corrigido.c` (`l x c`: menor 1ª ocorrência e busca 2D):**
   - Normal `2 x 3` (`5 2 8 / 2 9 1`, `alvo=2`) → `Menor: 1 (1, 2)`, `Posicao: (0, 1)`
   - Todos >= 999 (`1200 1500 / 1000 1200`, `alvo=1200`) → `Menor: 1000 (1, 0)`, `Posicao: (0, 0)`
   - Borda `1 x 1` (`1 1`, `-7`, `alvo=-7`) → `Menor: -7 (0, 0)`, `Posicao: (0, 0)`
   - Alvo não encontrado (`2 2`, `-3 -1 / -3 -9`, `alvo=0`) → `Menor: -9 (1, 1)`, `Posicao: nao encontrada`
   - Empate de menor (`3 2`, `4 1 / 1 5 / 1 2`, `alvo=1`) → `Menor: 1 (0, 1)`, `Posicao: (0, 1)`

5. **`E02_C03.c` (`l x c`: soma, maior e busca 2D):**
   - Normal `2 x 3` (`1 9 3 / 9 2 4`, `alvo=9`) → `Soma: 28`, `Maior: 9 (0, 1)`, `Busca: (0, 1)`
   - Borda `1 x 1` (`1 1`, `-15`, `alvo=5`) → `Soma: -15`, `Maior: -15 (0, 0)`, `Busca: nao encontrado`
   - Todos negativos `3 x 2` (`-9 -4 / -4 -8 / -12 -4`, `alvo=-4`) → `Soma: -41`, `Maior: -4 (0, 1)`, `Busca: (0, 1)`
   - Linha única `1 x 4` (`1 4`, `0 0 0 0`, `alvo=0`) → `Soma: 0`, `Maior: 0 (0, 0)`, `Busca: (0, 0)`
   - Coluna única `4 x 1` (`4 1`, `3 / 7 / 7 / 2`, `alvo=7`) → `Soma: 19`, `Maior: 7 (1, 0)`, `Busca: (1, 0)`
