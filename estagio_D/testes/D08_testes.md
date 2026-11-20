# Especificação de Testes — Bloco `D08`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, `#include <string.h>` e `#include <ctype.h>`, sem `gets`, sem VLAs, sem funções extras e sem matrizes 2D. Saídas em ASCII puro.
- **Comparação de saídas:** correspondência textual exata linha a linha.
- **Status de execução no ambiente atual (`19/11/2026`):**
  - **Executado:** verificação estática C99 + checagem de não-antecipação + **oráculo Python** sobre todos os **25 casos** de [casos_D08.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/casos_D08.json).
  - **Pendente:** compilação e execução binária em GCC (`gcc` ausente no ambiente local).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`D08_E03_corrigido.c`:**
   - Palavras distintas (`utfpr` `c99`) → `Iguais: Nao`, `Uniao: utfpr-c99`, `Invertida: 99c-rpf tu` (sem espaço: `99c-rpftu`)
   - Palavras iguais (`aba` `aba`) → `Iguais: Sim`, `Uniao: aba-aba`, `Invertida: aba-aba`
   - Diferença só de caixa (`Ana` `ana`) → `Iguais: Nao`, `Uniao: Ana-ana`, `Invertida: ana-anA`
   - 1 caractere cada (`x` `y`) → `Iguais: Nao`, `Uniao: x-y`, `Invertida: y-x`
   - Limite de 30 chars? (`abcde` `12345`) → `Iguais: Nao`, `Uniao: abcde-12345`, `Invertida: 54321-edcba`

2. **`D08_E04.c`:**
   - Não palíndromo (`Algoritmo`) → `Original: Algoritmo`, `Invertida: omtiroglA`, `Identicas: Nao`
   - Palíndromo exato (`arara`) → `Original: arara`, `Invertida: arara`, `Identicas: Sim`
   - Palíndromo com caixa diferente (`Arara`) → `Identicas: Nao` (`strcmp` diferencia `'A'` de `'a'`)
   - String vazia (`\n`) → `Original: `, `Invertida: `, `Identicas: Sim`
   - Com espaços (`a b a`) → `Original: a b a`, `Invertida: a b a`, `Identicas: Sim`

3. **`D08_E05.c`:**
   - Frase palíndroma (`A base do teto desaba`) → `Palindromo`
   - Palavra com caixa mista (`Radar`) → `Palindromo`
   - Não palíndromo (`Computacao`) → `Nao palindromo`
   - Espaços assimétricos (`  o   m o `) → `Palindromo`
   - Só espaços (`     `) → `Palindromo`

4. **`D08_C02_corrigido.c`:**
   - Fora de ordem, menor palíndromo com caixa (`zebra` `Arara`) → `Ordem: Arara <= zebra`, `Palindromo menor: Sim`
   - Em ordem, menor não palíndromo (`casa` `dado`) → `Ordem: casa <= dado`, `Palindromo menor: Nao`
   - Palavras iguais (`Omo` `Omo`) → `Ordem: Omo <= Omo`, `Palindromo menor: Sim`
   - Maiúscula vs minúscula (`ana` `Zebra`) → `Ordem: Zebra <= ana`, `Palindromo menor: Nao`
   - Prefixo (`a` `ab`) → `Ordem: a <= ab`, `Palindromo menor: Sim`

5. **`D08_C03.c`:**
   - Normal (`4`: `casa Arara ovo dados`) → `Menor: Arara`, `Maior: ovo`, `Palindromos: 2`
   - `n = 1` palíndromo (`1`: `Radar`) → `Menor: Radar`, `Maior: Radar`, `Palindromos: 1`
   - Sem palíndromos (`3`: `sol lua mar`) → `Menor: lua`, `Maior: sol`, `Palindromos: 0`
   - Todas iguais (`3`: `Ana Ana Ana`) → `Menor: Ana`, `Maior: Ana`, `Palindromos: 3`
   - Prefixo e caixa (`4`: `Z a aa A`) → `Menor: A`, `Maior: aa`, `Palindromos: 4`
