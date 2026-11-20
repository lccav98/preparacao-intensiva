# Especificação de Testes — Bloco `G07`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, proibição estrita de laços (`for`, `while`, `do-while`) dentro de funções recursivas, modificação *in-place* sem vetores auxiliares e sem `<string.h>`, caso base `i >= j`, sem `struct`, sem `malloc`/`free`, sem `gets(`, sem VLAs e saídas em ASCII puro.
- **Comparação de saídas e tolerância:**
  - Inteiros e strings: correspondência textual exata (`tolerancia_numerica: 0.01` mantida por padrão no JSON).
- **Casos de teste registrados:** **30 casos** (5 por arquivo `.c`) em [casos_G07.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/casos_G07.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`G07_E03_corrigido.c` (`eh_palindromo` + `inverter`):**
   - `"ABBA"` (par palíndromo) → `Palindromo: Sim` / `Invertida: ABBA`
   - `"ARARA"` (ímpar palíndromo) → `Palindromo: Sim` / `Invertida: ARARA`
   - `"CASA"` (par não-palíndromo) → `Palindromo: Nao` / `Invertida: ASAC`
   - `""` (borda string vazia) → `Palindromo: Sim` / `Invertida: `
   - `"X"` (borda 1 caractere) → `Palindromo: Sim` / `Invertida: X`

2. **`G07_E04.c` (`eh_palindromo`):**
   - `"osso"` → `Palindromo: Sim`
   - `"radar"` → `Palindromo: Sim`
   - `"arara azul"` → `Palindromo: Nao`
   - `""` → `Palindromo: Sim`
   - `"ab"` → `Palindromo: Nao`

3. **`G07_E05.c` (`inverter` *in-place*):**
   - `"ALGORITMOS"` → `Invertida: SOMTIROGLA`
   - `"C 99"` → `Invertida: 99 C`
   - `"ab"` (par de 2 caracteres) → `Invertida: ba`
   - `"a"` (1 caractere) → `Invertida: a`
   - `""` (string vazia) → `Invertida: `

4. **`G07_E06.c` (`remover_caractere` *in-place*):**
   - `"BANANA"` / `'A'` → `Resultado: BNN`
   - `"AAA"` / `'A'` → `Resultado: ` (ocorrências adjacentes removendo tudo)
   - `"AABAA"` / `'A'` → `Resultado: B` (adjacentes nas duas pontas)
   - `"teste"` / `'z'` → `Resultado: teste` (caractere ausente)
   - `"a b a c"` / `'a'` → `Resultado:  b  c` (preserva espaços)

5. **`G07_C02.c` (`eh_palindromo` + `inverter`):**
   - `"anilina"` → `Palindromo: Sim` / `Invertida: anilina`
   - `"muum"` → `Palindromo: Sim` / `Invertida: muum`
   - `"codigo"` → `Palindromo: Nao` / `Invertida: ogidoc`
   - `"k"` → `Palindromo: Sim` / `Invertida: k`
   - `"abca"` → `Palindromo: Nao` / `Invertida: acba`

6. **`G07_C03.c` (`remover_espacos` *in-place* + `comprimento`):**
   - `"C 99 e recursao"` → `Sem espacos: C99erecursao` / `Comprimento: 12`
   - `"   "` (apenas espaços adjacentes) → `Sem espacos: ` / `Comprimento: 0`
   - `"UTFPR"` (sem espaços) → `Sem espacos: UTFPR` / `Comprimento: 5`
   - `"  a  b  "` (espaços múltiplos nas extremidades e meio) → `Sem espacos: ab` / `Comprimento: 2`
   - `""` (string vazia) → `Sem espacos: ` / `Comprimento: 0`
