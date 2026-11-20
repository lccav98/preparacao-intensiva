# Especificação de Testes — Bloco `G09`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, proibição estrita de laços (`for`, `while`, `do-while`) dentro de funções recursivas, uso de `const` em leituras, chamada única em `maior_vetor` e `potencia_rapida`, modificação *in-place* em strings sem vetor auxiliar, sem `struct`, sem `malloc`/`free`, sem `gets(`, sem VLAs e saídas em ASCII puro.
- **Comparação de saídas e tolerância:**
  - Inteiros e strings: correspondência textual exata.
  - Valores reais (`%.2f` em `G09_E04.c`, `G09_E06.c` e `G09_C02.c`): correspondência textual exata e tolerância numérica de **`1e-2`**.
- **Casos de teste registrados:** **30 casos** (5 por arquivo `.c`) em [casos_G09.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/casos_G09.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`G09_E03_corrigido.c` (`soma_digitos` + `maior_vetor` + `inverter`):**
   - `"ABBA"` / `5832` / `4` (`10 25 7 18`) → `Soma digitos: 18` / `Maior: 25` / `Invertida: ABBA`
   - `"CASA"` / `0` / `3` (`-9 -2 -5`) → `Soma digitos: 0` / `Maior: -2` / `Invertida: ASAC` (todos negativos + `0` + par)
   - `""` / `9` / `1` (`-42`) → `Soma digitos: 9` / `Maior: -42` / `Invertida: ` (string vazia + `n = 1`)
   - `"C99"` / `1000` / `5` (`0 0 0 0 0`) → `Soma digitos: 1` / `Maior: 0` / `Invertida: 99C`
   - `"X"` / `90909` / `2` (`-1 1`) → `Soma digitos: 27` / `Maior: 1` / `Invertida: X`

2. **`G09_E04.c` (`maior_vetor` + `media_vetor` + `contar_acima`):**
   - `4` (`10 20 30 40`) → `Maior: 40` / `Media: 25.00` / `Acima da media: 2`
   - `3` (`1 2 4`) → `Maior: 4` / `Media: 2.33` / `Acima da media: 1`
   - `4` (`-8 -4 -2 -6`) → `Maior: -2` / `Media: -5.00` / `Acima da media: 2`
   - `3` (`5 5 5`) → `Maior: 5` / `Media: 5.00` / `Acima da media: 0`
   - `1` (`-7`) → `Maior: -7` / `Media: -7.00` / `Acima da media: 0`

3. **`G09_E05.c` (`remover_char` + `comprimento` + `eh_palindromo`):**
   - `"a-r-a-r-a"` / `'-'` → `Limpa: arara` / `Comprimento: 5` / `Palindromo: Sim`
   - `"ab_ba"` / `'_'` → `Limpa: abba` / `Comprimento: 4` / `Palindromo: Sim`
   - `"AAA"` / `'A'` → `Limpa: ` / `Comprimento: 0` / `Palindromo: Sim`
   - `"casa"` / `'z'` → `Limpa: casa` / `Comprimento: 4` / `Palindromo: Nao`
   - `"xaxbx"` / `'x'` → `Limpa: ab` / `Comprimento: 2` / `Palindromo: Nao`

4. **`G09_E06.c` (`contar_digitos` + `soma_digitos` + `potencia_rapida`):**
   - `5832 2.0 8` → `Digitos: 4` / `Soma digitos: 18` / `Potencia: 256.00`
   - `0 5.0 0` → `Digitos: 1` / `Soma digitos: 0` / `Potencia: 1.00`
   - `7 3.0 5` → `Digitos: 1` / `Soma digitos: 7` / `Potencia: 243.00`
   - `1005 2.5 1` → `Digitos: 4` / `Soma digitos: 6` / `Potencia: 2.50`
   - `909 -2.0 3` → `Digitos: 3` / `Soma digitos: 18` / `Potencia: -8.00`

5. **`G09_C02.c` (`soma_pares` + `media_vetor` + `contem`):**
   - `5` (`1 2 3 4 5`) / `4` → `Soma pares: 6` / `Media: 3.00` / `Contem: Sim`
   - `4` (`1 3 5 7`) / `2` → `Soma pares: 0` / `Media: 4.00` / `Contem: Nao`
   - `3` (`-4 -2 6`) / `-4` → `Soma pares: 0` / `Media: 0.00` / `Contem: Sim`
   - `1` (`8`) / `8` → `Soma pares: 8` / `Media: 8.00` / `Contem: Sim`
   - `4` (`-3 -5 -2 1`) / `0` → `Soma pares: -2` / `Media: -2.25` / `Contem: Nao`

6. **`G09_C03.c` (`remover_vogais` *in-place* + `imprimir_inversa`):**
   - `"Algoritmos"` → `Sem vogais: lgrtms` / `Inversa: smtrgl`
   - `"AEIOUaeiou"` → `Sem vogais: ` / `Inversa: `
   - `"C99 GCC"` → `Sem vogais: C99 GCC` / `Inversa: CCG 99C`
   - `"Educacao"` → `Sem vogais: dcc` / `Inversa: ccd`
   - `""` → `Sem vogais: ` / `Inversa: `
