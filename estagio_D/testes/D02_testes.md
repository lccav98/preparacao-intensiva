# Especificação de Testes — Bloco `D02`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, `#define MAX 100`, `int v[MAX]` (sem VLAs, funções extras, strings ou matrizes 2D).
- **Comparação de saídas e tolerância:**
  - Inteiros e índices: correspondência exata.
  - Médias (`%.2f`): comparação textual e tolerância numérica de **`1e-2`**.
- **Status de execução no ambiente atual (`19/11/2026`):**
  - **Executado:** verificação estática C99 + checagem de não-antecipação + **oráculo matemático Python** sobre todos os **30 casos** de [casos_D02.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/casos_D02.json).
  - **Pendente:** compilação e execução binária em GCC (`gcc` ausente no ambiente local).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`D02_E03_corrigido.c`:**
   - Normal misto (`5`: `4 7 2 9 3`) → `Media: 5.00`, `Maior: 9`, `Menor: 2`
   - Todos negativos (`4`: `-10 -3 -8 -20`) → `Media: -10.25`, `Maior: -3`, `Menor: -20`
   - Todos positivos grandes (`3`: `1200 1500 1100`) → `Media: 1266.67`, `Maior: 1500`, `Menor: 1100`
   - `n = 1` negativo (`1`: `-7`) → `Media: -7.00`, `Maior: -7`, `Menor: -7`
   - Empates iguais (`4`: `5 5 5 5`) → `Media: 5.00`, `Maior: 5`, `Menor: 5`

2. **`D02_E04.c`:**
   - Normal (`5`: `10 20 30 40 50`) → `Soma: 150`, `Media: 30.00`, `Acima da media: 2`
   - Todos iguais (`4`: `6 6 6 6`) → `Soma: 24`, `Media: 6.00`, `Acima da media: 0` (testa `>` estrito)
   - `n = 1` (`1`: `-5`) → `Soma: -5`, `Media: -5.00`, `Acima da media: 0`
   - Média fracionária (`4`: `1 2 2 5`) → `Soma: 10`, `Media: 2.50`, `Acima da media: 1`
   - Negativos e positivos (`4`: `-4 -2 2 4`) → `Soma: 0`, `Media: 0.00`, `Acima da media: 2`

3. **`D02_E05.c`:**
   - Normal com empate (`6`: `8 3 5 3 9 7`) → `Menor: 3`, `Indice: 3`
   - Menor na posição `0` (`4`: `-10 0 5 2`) → `Menor: -10`, `Indice: 0`
   - Todos iguais (`5`: `4 4 4 4 4`) → `Menor: 4`, `Indice: 4` (último índice!)
   - `n = 1` (`1`: `42`) → `Menor: 42`, `Indice: 0`
   - Negativos empatados (`4`: `-2 -9 -5 -9`) → `Menor: -9`, `Indice: 3`

4. **`D02_E06.c`:**
   - Normal com empates duplos (`7`: `4 9 2 9 5 2 7`) → `Maior: 9 (indice 1)`, `Menor: 2 (indice 5)`
   - Todos iguais negativos (`4`: `-3 -3 -3 -3`) → `Maior: -3 (indice 0)`, `Menor: -3 (indice 3)`
   - `n = 1` (`1`: `0`) → `Maior: 0 (indice 0)`, `Menor: 0 (indice 0)`
   - Crescente (`4`: `1 2 3 4`) → `Maior: 4 (indice 3)`, `Menor: 1 (indice 0)`
   - Decrescente negativos (`4`: `-1 -2 -3 -4`) → `Maior: -1 (indice 0)`, `Menor: -4 (indice 3)`

5. **`D02_C02_corrigido.c`:**
   - `v[0]` positivo e valores `> 999` (`4`: `1200 1050 1050 1500`) → `Positivos: 4`, `Menor: 1050 (indice 1)`
   - `v[0]` positivo e empate de menor (`5`: `5 -3 8 -3 2`) → `Positivos: 3`, `Menor: -3 (indice 1)` (1ª ocorrência)
   - Zero não é positivo (`4`: `0 -2 0 3`) → `Positivos: 1`, `Menor: -2 (indice 1)`
   - `n = 1` positivo (`1`: `2000`) → `Positivos: 1`, `Menor: 2000 (indice 0)`
   - Todos negativos (`3`: `-5 -1 -5`) → `Positivos: 0`, `Menor: -5 (indice 0)`

6. **`D02_C03.c`:**
   - Normal completo (`6`: `-4 8 -9 8 -9 0`) → `Soma: -6`, `Media: -1.00`, `Negativos: 3`, `Maior: 8 (indice 1)`, `Menor: -9 (indice 4)`
   - `n = 1` negativo (`1`: `-15`) → `Soma: -15`, `Media: -15.00`, `Negativos: 1`, `Maior: -15 (indice 0)`, `Menor: -15 (indice 0)`
   - Todos iguais zero (`3`: `0 0 0`) → `Soma: 0`, `Media: 0.00`, `Negativos: 0`, `Maior: 0 (indice 0)`, `Menor: 0 (indice 2)`
   - Todos negativos (`4`: `-1 -5 -1 -5`) → `Soma: -12`, `Media: -3.00`, `Negativos: 4`, `Maior: -1 (indice 0)`, `Menor: -5 (indice 3)`
   - Positivos grandes (`3`: `1000 1001 1000`) → `Soma: 3001`, `Media: 1000.33`, `Negativos: 0`, `Maior: 1001 (indice 1)`, `Menor: 1000 (indice 2)`
