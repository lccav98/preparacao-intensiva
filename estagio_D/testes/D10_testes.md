# Especificação de Testes — Bloco `D10`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** nenhuma matriz 2D, nenhuma função além de `int main(void)`, sem VLAs, sem `gets`, sem `struct` ou alocação dinâmica. Saídas em ASCII puro.
- **Comparação de saídas:** correspondência textual exata linha a linha.
- **Status de execução no ambiente atual (`19/11/2026`):**
  - **Executado:** verificação estática C99 + checagem de não-antecipação + **oráculo Python** sobre todos os **35 casos** de [casos_D10.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/casos_D10.json).
  - **Pendente:** compilação e execução binária em GCC (`gcc` ausente no ambiente local).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`D10_E02_corrigido.c`:**
   - Normal (`6`: `4 7 6 4 9 2`) → `Aprovadas: 7 6 9`, `Nota 2: 1`, `Nota 4: 2`, `Nota 6: 1`, `Nota 7: 1`, `Nota 9: 1`
   - Nenhuma aprovada (`4`: `0 3 5 2`) → `Aprovadas: Nenhuma` + contagens
   - Todas aprovadas e iguais (`3`: `8 8 8`) → `Aprovadas: 8 8 8`, `Nota 8: 3`
   - Limite `n = 1` nota `6` (`1`: `6`) → `Aprovadas: 6`, `Nota 6: 1`
   - Limites `0` e `9` (`4`: `0 9 0 9`) → `Aprovadas: 9 9`, `Nota 0: 2`, `Nota 9: 2`

2. **`D10_E03_corrigido.c`:**
   - Normal com espaços (`  Ola   C99  `) → `[Ola C99] (7)`
   - Comando `SAIR` com espaços extras (`   SAIR   `) → `Encerrando`
   - Case-sensitive `"sair"` (`sair`) → `[sair] (4)`
   - Só espaços (`     `) → `[] (0)`
   - Linha vazia (`\n`) → `[] (0)`

3. **`D10_E04.c`:**
   - Normal com kernel assimétrico (`5`: `2 0 1 3 2`, `3`: `1 2 4`) → `Convolucao: 9 5 12`
   - `n == m` (`3`: `1 2 3`, `3`: `4 5 6`) → `Convolucao: 28` (`1*6 + 2*5 + 3*4`)
   - `m = 1` (`4`: `-2 5 0 3`, `1`: `-3`) → `Convolucao: 6 -15 0 -9`
   - Kernel com zeros (`4`: `10 20 30 40`, `2`: `0 1`) → `Convolucao: 10 20 30`
   - Negativos (`4`: `-1 2 -3 4`, `2`: `2 -1`) → `Convolucao: 5 -8 11`

4. **`D10_E05.c`:**
   - Normal (`  Algoritmos   em C  `) → `[Algoritmos em C]`, `a:1 e:1 i:1 o:2 u:0`
   - Todas as vogais em caixa mista (`AEIOU aeiou`) → `[AEIOU aeiou]`, `a:2 e:2 i:2 o:2 u:2`
   - Sem vogais (`bcdf 123`) → `[bcdf 123]`, `a:0 e:0 i:0 o:0 u:0`
   - Só espaços (`    `) → `[]`, `a:0 e:0 i:0 o:0 u:0`
   - Linha vazia (`\n`) → `[]`, `a:0 e:0 i:0 o:0 u:0`

5. **`D10_E06.c`:**
   - Normal `2 x 3` (`1 2 3 / 4 5 6`) → Transposta `3 x 2`, `Maior: 6 em (1, 2)`, `Menor: 1 em (0, 0)`
   - Empates negativos `2 x 2` (`-5 -1 / -1 -5`) → Transposta `2 x 2`, `Maior: -1 em (0, 1)`, `Menor: -5 em (1, 1)`
   - Grade `1 x 1` (`42`) → `Transposta:\n42`, `Maior: 42 em (0, 0)`, `Menor: 42 em (0, 0)`
   - Todos iguais `2 x 3` (`7 ... 7`) → `Maior: 7 em (0, 0)`, `Menor: 7 em (1, 2)`
   - Vetor coluna `3 x 1` (`10 / 20 / 5`) → `Transposta:\n10 20 5`, `Maior: 20 em (1, 0)`, `Menor: 5 em (2, 0)`

6. **`D10_C02.c`:**
   - Sobreposição múltipla (`5`: `1 2 1 2 1`, `2`: `1 2`) → `Ocorrencias: 2`, `Posicoes: 0 2`
   - Sobreposição de iguais (`5`: `3 3 3 3 3`, `3`: `3 3 3`) → `Ocorrencias: 3`, `Posicoes: 0 1 2`
   - Sem ocorrência (`4`: `1 2 3 4`, `2`: `2 4`) → `Ocorrencias: 0`, `Posicoes: Nenhuma`
   - `m == n` igual (`3`: `9 8 7`, `3`: `9 8 7`) → `Ocorrencias: 1`, `Posicoes: 0`
   - Padrão unitário no fim (`4`: `1 2 3 9`, `1`: `9`) → `Ocorrencias: 1`, `Posicoes: 3`

7. **`D10_C03.c`:**
   - Palíndromo com espaços e caixa (`Arara`) → `Palindromo: Sim`, `a: 3`, `r: 2`
   - Frase palíndroma (`A base do teto desaba`) → `Palindromo: Sim` + frequências
   - Não palíndromo (`Casa 99!`) → `Palindromo: Nao`, `a: 2`, `c: 1`, `s: 1`
   - Sem letras (`123 321`) → `Palindromo: Sim`, `Sem letras`
   - Só espaços (`   `) → `Palindromo: Sim`, `Sem letras`
