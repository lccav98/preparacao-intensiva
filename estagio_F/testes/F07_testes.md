# Especificação de Testes — Bloco `F07`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, protótipos antes de `main`, matrizes 2D com dimensão das colunas informada via `#define`, strings processadas *in-place* até `'\0'`, composição entre funções, sem multi-arquivo, sem VLAs, sem `struct`, sem `malloc`/`free`, sem recursividade e saídas em ASCII puro.
- **Comparação de saídas e tolerância:**
  - Inteiros e strings: correspondência textual exata.
  - Valores reais (`%.2f` em `F07_E05.c`): correspondência textual exata e tolerância numérica de **`1e-2`**.
- **Casos de teste registrados:** **30 casos** (5 por arquivo `.c`) em [casos_F07.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/casos_F07.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`F07_E03_corrigido.c` (`somar_matriz` + `remover_digitos`):**
   - `2` linhas (`1 2 3` / `4 5 6`) + `"a1b2c3"` → `Soma: 21` / `Texto: abc`
   - `1` linha (`-5 10 -5`) + `"999"` → `Soma: 0` / `Texto: ` (string vazia após remover tudo)
   - `2` linhas (`0 0 0` / `0 0 0`) + `"utfpr"` → `Soma: 0` / `Texto: utfpr` (sem dígitos)
   - `3` linhas (`1 1 1` / `2 2 2` / `3 3 3`) + `"0a0"` → `Soma: 18` / `Texto: a`
   - `1` linha (`-1 -2 -3`) + `"c99"` → `Soma: -6` / `Texto: c`

2. **`F07_E04.c` (`eh_simetrica` `3 x 3`):**
   - Simétrica geral (`1 2 3` / `2 4 5` / `3 5 6`) → `Simetrica: Sim`
   - Assimétrica na borda `[0][2] != [2][0]` (`1 2 9` / `2 4 5` / `3 5 6`) → `Simetrica: Nao`
   - Identidade `3 x 3` → `Simetrica: Sim`
   - Antissimétrica não-nula (`0 1 -2` / `-1 0 3` / `2 -3 0`) → `Simetrica: Nao`
   - Simétrica com negativos (`-3 0 -1` / `0 7 4` / `-1 4 -2`) → `Simetrica: Sim`

3. **`F07_E05.c` (`soma_matriz`, `media_matriz`, `contar_acima_media`):**
   - `2 x 4` (`1 2 3 4` / `5 6 7 8`) → `Soma: 36` / `Media: 4.50` / `Acima da media: 4`
   - `1 x 4` iguais (`10 10 10 10`) → `Soma: 40` / `Media: 10.00` / `Acima da media: 0`
   - `2 x 4` com negativos (`-2 -4 -6 -8` / `0 2 4 6`) → `Soma: -8` / `Media: -1.00` / `Acima da media: 4`
   - `1 x 4` decimal (`1 2 3 5`) → `Soma: 11` / `Media: 2.75` / `Acima da media: 2`
   - `3 x 4` esparsa (`0..0` e `12`) → `Soma: 12` / `Media: 1.00` / `Acima da media: 1`

4. **`F07_E06.c` (`remover_caractere` *in-place*):**
   - `"banana"` removendo `'a'` → `Resultado: bnn`
   - `"arara azul"` removendo `'a'` → `Resultado: rr zul` (preserva espaço)
   - `"xxxx"` removendo `'x'` → `Resultado: ` (tudo removido)
   - `"teste"` removendo `'z'` → `Resultado: teste` (caractere ausente)
   - `"Aba"` removendo `'a'` → `Resultado: Ab` (sensível a maiúscula/minúscula)

5. **`F07_C02.c` (`resumo_diagonais` `3 x 3`):**
   - `1..9` (`1 2 3` / `4 5 6` / `7 8 9`) → `Diagonal principal: 15` / `Diagonal secundaria: 15`
   - Identidade `3 x 3` → `Diagonal principal: 3` / `Diagonal secundaria: 1`
   - Negativos (`-1 2 -3` / `4 -5 6` / `-7 8 -9`) → `Diagonal principal: -15` / `Diagonal secundaria: -15`
   - Zeros nas diagonais (`0 9 0` / `9 0 9` / `0 9 0`) → `Diagonal principal: 0` / `Diagonal secundaria: 0`
   - Assimétrica (`10 0 2` / `0 20 0` / `4 0 30`) → `Diagonal principal: 60` / `Diagonal secundaria: 26`

6. **`F07_C03.c` (`remover_vogais` + `tamanho_string`):**
   - `"Algoritmos"` → `Sem vogais: lgrtms` / `Comprimento: 6`
   - `"AEIOUaeiou"` → `Sem vogais: ` / `Comprimento: 0` (apenas vogais)
   - `"C99 GCC"` → `Sem vogais: C99 GCC` / `Comprimento: 7` (sem vogais, preserva espaço/dígitos)
   - `"Educacao"` → `Sem vogais: dcc` / `Comprimento: 3`
   - `"a"` → `Sem vogais: ` / `Comprimento: 0` (borda 1 caractere vogal)
