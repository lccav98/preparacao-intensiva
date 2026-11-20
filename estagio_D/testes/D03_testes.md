# Especificação de Testes — Bloco `D03`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>` (e `#include <stdlib.h>` para `abs()`), `#define MAX 100`, vetores 1D fixos (sem VLAs, funções extras, strings ou matrizes 2D), saídas em ASCII puro.
- **Comparação de saídas e tolerância:**
  - Inteiros e textos: correspondência exata.
  - Médias (`%.2f`): tolerância numérica de **`1e-2`**.
- **Casos de teste registrados:** 30 casos (5 por arquivo `.c`) em [casos_D03.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/casos_D03.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`D03_E03_corrigido.c`:**
   - Normal com repetição (`5`: `4 7 9 7 2`, chave `7`) → `Indice: 1\nInvertido: 2 7 9 7 4\n`
   - Não encontrado (`4`: `10 20 30 40`, chave `5`) → `Indice: -1\nInvertido: 40 30 20 10\n`
   - Chave na posição `0` com `n` par (`4`: `8 3 1 9`, chave `8`) → `Indice: 0\nInvertido: 9 1 3 8\n`
   - `n = 1` encontrado (`1`: `-6`, chave `-6`) → `Indice: 0\nInvertido: -6\n`
   - `n = 1` ausente (`1`: `-6`, chave `0`) → `Indice: -1\nInvertido: -6\n`

2. **`D03_E04.c`:**
   - Normal sem empate (`5`: `3 12 7 19 15`, `x = 10`) → `Mais proximo: 12 (indice 1, distancia 2)`
   - Empate escolhendo 1ª ocorrência (`4`: `12 5 8 15`, `x = 10`) → `Mais proximo: 12 (indice 0, distancia 2)`
   - Exato negativo (`4`: `-10 -3 4 8`, `x = -3`) → `Mais proximo: -3 (indice 1, distancia 0)`
   - `n = 1` (`1`: `-7`, `x = 5`) → `Mais proximo: -7 (indice 0, distancia 12)`
   - Todos abaixo de `x` (`3`: `-20 -10 -5`, `x = 0`) → `Mais proximo: -5 (indice 2, distancia 5)`

3. **`D03_E05.c`:**
   - Normal misto (`6`: `3 8 -4 7 0 -5`) → `Pares (3): 8 -4 0` / `Impares (3): 3 7 -5`
   - Apenas pares (`3`: `2 -6 0`) → `Pares (3): 2 -6 0` / `Impares (0): nenhum`
   - Apenas ímpares negativos (`3`: `-1 -3 -7`) → `Pares (0): nenhum` / `Impares (3): -1 -3 -7`
   - `n = 1` par (`1`: `0`) → `Pares (1): 0` / `Impares (0): nenhum`
   - `n = 1` ímpar negativo (`1`: `-9`) → `Pares (0): nenhum` / `Impares (1): -9`

4. **`D03_E06.c`:**
   - Normal (`4`: `10 20 30 40`) → `Invertido: 40 30 20 10`, `Media: 25.00`, `Abaixo (2): 20 10`, `Acima ou igual (2): 40 30`
   - Todos iguais (`3`: `5 5 5`) → `Invertido: 5 5 5`, `Media: 5.00`, `Abaixo (0): nenhum`, `Acima ou igual (3): 5 5 5`
   - `n = 1` (`1`: `-4`) → `Invertido: -4`, `Media: -4.00`, `Abaixo (0): nenhum`, `Acima ou igual (1): -4`
   - `n = 5` ímpar (`5`: `1 2 3 4 5`) → `Invertido: 5 4 3 2 1`, `Media: 3.00`, `Abaixo (2): 2 1`, `Acima ou igual (3): 5 4 3`
   - Negativos (`4`: `-10 0 2 4`) → `Invertido: 4 2 0 -10`, `Media: -1.00`, `Abaixo (1): -10`, `Acima ou igual (3): 4 2 0`

5. **`D03_C02_corrigido.c`:**
   - Múltiplas ocorrências (`6`: `5 2 5 8 5 1`, `alvo = 5`) → `Ocorrencias: 0 2 4`, `Mais proximo: 5 (indice 0)`
   - Nenhuma ocorrência com negativos (`4`: `-10 2 12 18`, `alvo = 10`) → `Ocorrencias: nenhuma`, `Mais proximo: 12 (indice 2)`
   - Empate na distância (`4`: `7 13 7 13`, `alvo = 10`) → `Ocorrencias: nenhuma`, `Mais proximo: 7 (indice 0)`
   - `n = 1` encontrado (`1`: `0`, `alvo = 0`) → `Ocorrencias: 0`, `Mais proximo: 0 (indice 0)`
   - `n = 1` ausente (`1`: `-5`, `alvo = 5`) → `Ocorrencias: nenhuma`, `Mais proximo: -5 (indice 0)`

6. **`D03_C03.c`:**
   - Normal (`6`: `2 9 4 12 1 8`, `L = 6`) → `Menores invertidos (3): 1 4 2`, `Maiores ou iguais (3): 9 12 8`
   - `menores` vazio (`3`: `10 20 30`, `L = 10`) → `Menores invertidos (0): nenhum`, `Maiores ou iguais (3): 10 20 30`
   - `maiores_ig` vazio (`4`: `-5 -1 0 3`, `L = 5`) → `Menores invertidos (4): 3 0 -1 -5`, `Maiores ou iguais (0): nenhum`
   - `n = 1` menor (`1`: `-2`, `L = 0`) → `Menores invertidos (1): -2`, `Maiores ou iguais (0): nenhum`
   - `menores` com tamanho par (`5`: `1 2 10 3 4`, `L = 5`) → `Menores invertidos (4): 4 3 2 1`, `Maiores ou iguais (1): 10`
