# Especificação de Testes — Bloco `D09`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, vetores estritamente **1D**, macro `INDICE` com parênteses protetores, **nenhuma matriz 2D**, sem VLAs e sem funções extras além de `int main(void)`. Saídas em ASCII puro.
- **Comparação de saídas:** correspondência textual exata linha a linha.
- **Status de execução no ambiente atual (`19/11/2026`):**
  - **Executado:** verificação estática C99 + checagem de não-antecipação (zero matrizes 2D) + **oráculo Python** sobre todos os **25 casos** de [casos_D09.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/casos_D09.json).
  - **Pendente:** compilação e execução binária em GCC (`gcc` ausente no ambiente local).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`D09_E03_corrigido.c`:**
   - Normal (`1..12`, consulta `(2, 3)`) → grade `3x4` e `Consulta: 7`
   - Canto superior esquerdo `(1, 1)` → `Consulta: 1`
   - Canto inferior direito `(3, 4)` → `Consulta: 120`
   - Valores negativos (`-1..-12`, consulta `(2, 1)`) → `Consulta: -5`
   - Todos iguais (`7`, consulta `(3, 2)`) → `Consulta: 7`

2. **`D09_E04.c`:**
   - Normal `2 x 3` (`1 2 3 / 4 5 6`) → `Linha 0: 6`, `Linha 1: 15`, `Maior: 6 em (1, 2)`
   - Grade `1 x 1` (`-9`) → `Linha 0: -9`, `Maior: -9 em (0, 0)`
   - Todos negativos com empate (`2 x 2`: `-5 -2 / -2 -8`) → `Maior: -2 em (0, 1)` (1ª ocorrência)
   - Vetor coluna `3 x 1` (`10 / 30 / 20`) → `Linha 0: 10`, `Linha 1: 30`, `Linha 2: 20`, `Maior: 30 em (1, 0)`
   - Vetor linha `1 x 4` (`4 4 4 4`) → `Linha 0: 16`, `Maior: 4 em (0, 0)`

3. **`D09_E05.c`:**
   - Normal `2 x 3` (`abc` `def`, 3 consultas `(0,2)`, `(1,0)`, `(2,0)`) → `c`, `d`, `Invalido`, `Linear: abcdef`
   - Grade `1 x 1` (`Z`, 2 consultas `(0,0)`, `(-1,0)`) → `Z`, `Invalido`, `Linear: Z`
   - `0` consultas (`2 x 2`, `q = 0`) → `Linear: 1234`
   - Limite negativo de coluna (`2 x 2`, consulta `(0, -1)` e `(0, 2)`) → `Invalido`, `Invalido`, `Linear: abcd`
   - Retangular `3 x 2` (`12` `34` `56`, consulta `(2, 1)`) → `6`, `Linear: 123456`

4. **`D09_C02_corrigido.c`:**
   - Normal `3 x 5` (`abcde` `fghij` `klmno`, `lin1=2, col=1`) → `Celula: g`, `Coluna: b g l`, `Linear: abcdefghijklmno`
   - Primeira linha e primeira coluna (`lin1=1, col=0`) → `Celula: a`, `Coluna: a f k`
   - Última linha e última coluna (`lin1=3, col=4`) → `Celula: o`, `Coluna: e j o`
   - Dígitos na grade (`12345` `67890` `ABCDE`, `lin1=2, col=4`) → `Celula: 0`, `Coluna: 5 0 E`
   - Símbolos iguais (`.....` `..X..` `.....`, `lin1=2, col=2`) → `Celula: X`, `Coluna: . X .`

5. **`D09_C03.c`:**
   - Normal `2 x 3` (`1 5 2 / 5 3 5`, alvo `5`) → `Coluna 0: 6`, `Coluna 1: 8`, `Coluna 2: 7`, `Ocorrencias: 3`, `Primeira: (0, 1)`
   - Alvo ausente (`2 x 2`, alvo `9`) → `Ocorrencias: 0`, `Primeira: Nao encontrado`
   - Grade `1 x 1` igual ao alvo (`4`, alvo `4`) → `Coluna 0: 4`, `Ocorrencias: 1`, `Primeira: (0, 0)`
   - Negativos (`3 x 2`, alvo `-3`) → `Coluna 0: -5`, `Coluna 1: -6`, `Ocorrencias: 1`, `Primeira: (1, 0)`
   - Matriz `1 x 4` (`7 8 7 9`, alvo `7`) → `Ocorrencias: 2`, `Primeira: (0, 0)`
