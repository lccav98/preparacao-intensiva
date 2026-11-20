# Especificação de Testes — Bloco `F04`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, ponteiros manipulados exclusivamente dentro de `main` (sem ponteiros como parâmetros de função — tópico de `F05`, sem vetores/matrizes/strings em funções, sem aritmética de ponteiros, sem `struct`, sem `malloc`/`free`, sem VLAs e sem recursão), saídas determinísticas em ASCII puro.
- **Comparação de saídas e tolerância:**
  - Inteiros e texto: correspondência exata.
  - Valores reais (`%.2f` em `F04_E06.c`): correspondência textual exata e tolerância numérica de **`1e-2`**.
- **Casos de teste registrados:** 25 casos (5 por arquivo `.c`) em [casos_F04.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/casos_F04.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`F04_E03_corrigido.c` (`p = &x` e guarda `q != NULL`):**
   - `10 5` (`y > 0`, `q = &y`) → `25`
   - `10 0` (borda `y == 0`, `q == NULL`) → `20`
   - `10 -3` (`y < 0`, `q == NULL`) → `20`
   - `0 7` (`x == 0`, `y > 0`) → `7`
   - `-4 2` (`x < 0`, `y > 0`) → `-6`

2. **`F04_E04.c` (`p_menor` e `p_maior` por redirecionamento):**
   - `8 2 14` (normal: menor em `b`, maior em `c`) → `Valores: 8 12 14` / `Apontado por p_maior: 14`
   - `5 5 5` (todos iguais: `p_menor` e `p_maior` compartilham `&a`) → `Valores: 15 5 5` / `Apontado por p_maior: 15`
   - `-10 -3 -20` (todos negativos) → `Valores: -10 -3 -10` / `Apontado por p_maior: -3`
   - `1 2 3` (crescente: `a` vira `11`, mas `p_maior` segue apontando para `c`) → `Valores: 11 2 3` / `Apontado por p_maior: 3`
   - `0 -5 10` (zero, negativo e positivo) → `Valores: 0 5 10` / `Apontado por p_maior: 10`

3. **`F04_E05.c` (ordenação e igualdade via `*px` e `*py`):**
   - `15 4` (fora de ordem) → `Iguais: 0` / `Ordenados: 4 15`
   - `4 15` (já ordenados) → `Iguais: 0` / `Ordenados: 4 15`
   - `7 7` (iguais) → `Iguais: 1` / `Ordenados: 7 7`
   - `0 -9` (zero e negativo) → `Iguais: 0` / `Ordenados: -9 0`
   - `-12 -12` (iguais negativos) → `Iguais: 1` / `Ordenados: -12 -12`

4. **`F04_E06.c` (seleção condicional de ponteiro com `NULL`):**
   - `100.00 50.00 1` (aponta `a`) → `Atualizado: 110.00` / `Valores: 110.00 50.00`
   - `100.00 200.00 2` (aponta `b`) → `Atualizado: 220.00` / `Valores: 100.00 220.00`
   - `40.00 80.00 0` (borda `escolha = 0`, `NULL`) → `Ponteiro nulo` / `Valores: 40.00 80.00`
   - `40.00 80.00 3` (`escolha` fora de `1..2`, `NULL`) → `Ponteiro nulo` / `Valores: 40.00 80.00`
   - `15.20 30.40 2` (decimais) → `Atualizado: 33.44` / `Valores: 15.20 33.44`

5. **`F04_C03_corrigido.c` (diagnóstico de ponteiro não inicializado / `NULL`):**
   - `10 20 1` (`cod == 1`, `q = &a`) → `35 25`
   - `10 20 0` (`cod != 1`, `q == NULL`) → `10 25`
   - `0 -5 1` (borda resultante `0 0`) → `0 0`
   - `0 -5 2` (`cod != 1`, `q == NULL`) → `0 0`
   - `-8 3 1` (soma anula `a`) → `0 8`
