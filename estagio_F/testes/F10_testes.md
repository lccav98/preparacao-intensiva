# Especificação de Testes — Bloco `F10`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comandos de compilação:**
  - Arquivo único (`F10_E03_corrigido.c`, `F10_E04.c`):
    ```bash
    gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o prog
    ```
  - Multi-arquivo (`F10_E05`, `F10_E06`, `F10_C03` — nunca passar `.h` ao `gcc`):
    - `F10_E05`: `gcc -std=c99 -Wall -Wextra solucoes/F10_E05/main.c solucoes/F10_E05/matriz_ops.c -o prog`
    - `F10_E06`: `gcc -std=c99 -Wall -Wextra solucoes/F10_E06/main.c solucoes/F10_E06/texto_ops.c -o prog`
    - `F10_C03`: `gcc -std=c99 -Wall -Wextra solucoes/F10_C03/main.c solucoes/F10_C03/analise.c -o prog`
- **Restrições verificadas nos arquivos `.c`/`.h`:** protótipos antes de `main` ou em `.h` com guardas `#ifndef`/`#define`/`#endif`, uso de `const`, matrizes com dimensão de colunas fixa (`COL`), strings terminadas em `'\0'`, sem recursividade, sem VLAs, sem `struct`, sem `malloc`/`free` e saídas em ASCII puro.
- **Comparação de saídas e tolerância:**
  - Inteiros e strings: correspondência textual exata.
  - Valores reais (`%.2f` em `F10_E04.c`): correspondência textual exata e tolerância numérica de **`1e-2`**.
- **Casos de teste registrados:** **25 casos** (5 por solução/projeto) em [casos_F10.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/casos_F10.json).

---

## Casos de Teste por Programa / Projeto (5 casos cada: normal + bordas críticas)

1. **`F10_E03_corrigido.c` (`resumo` + `limpar_espacos`):**
   - `"C 99 e modular"` / `4` / `10 20 5 15` → `Soma: 50` / `Maior: 20` / `Sem espacos: C99emodular`
   - `"   "` / `3` / `-5 -2 -9` → `Soma: -16` / `Maior: -2` / `Sem espacos: ` (apenas espaços)
   - `"UTFPR"` / `1` / `42` → `Soma: 42` / `Maior: 42` / `Sem espacos: UTFPR` (sem espaços, `n = 1`)
   - `"a b c"` / `4` / `0 0 0 0` → `Soma: 0` / `Maior: 0` / `Sem espacos: abc`
   - `" x y "` / `2` / `-10 10` → `Soma: 0` / `Maior: 10` / `Sem espacos: xy`

2. **`F10_E04.c` (`media_vetor` + `analisar_vetor`):**
   - `4` / `10 20 30 40` / `25` → `Media: 25.00` / `Acima do limite: 2`
   - `3` / `1 2 4` / `1` → `Media: 2.33` / `Acima do limite: 2`
   - `4` / `-8 -4 -2 -6` / `-5` → `Media: -5.00` / `Acima do limite: 2`
   - `3` / `5 5 5` / `5` → `Media: 5.00` / `Acima do limite: 0` (estritamente maior que `5`)
   - `1` / `10` / `9` → `Media: 10.00` / `Acima do limite: 1` (borda `n = 1`)

3. **`F10_E05` (`matriz_ops.h` + `matriz_ops.c` + `main.c`):**
   - `1 2 3` / `4 5 6` / `7 8 9` → `Diagonal principal: 15` / `Menor: 1` / `Maior: 9`
   - `-9 -2 -3` / `-4 -5 -6` / `-7 -8 -1` → `Diagonal principal: -15` / `Menor: -9` / `Maior: -1`
   - `0 0 0` / `0 0 0` / `0 0 0` → `Diagonal principal: 0` / `Menor: 0` / `Maior: 0`
   - `10 0 0` / `0 20 0` / `0 0 30` → `Diagonal principal: 60` / `Menor: 0` / `Maior: 30`
   - `5 5 5` / `5 5 5` / `5 5 5` → `Diagonal principal: 15` / `Menor: 5` / `Maior: 5`

4. **`F10_E06` (`texto_ops.h` + `texto_ops.c` + `main.c`):**
   - `"banana"` / `a o` → `Texto: bonono` / `Letras: 6`
   - `"C-99-ok"` / `- _` → `Texto: C_99_ok` / `Letras: 3` (dígitos/símbolos não contam como letra)
   - `"1234"` / `1 9` → `Texto: 9234` / `Letras: 0`
   - `"Az"` / `x y` → `Texto: Az` / `Letras: 2` (caractere antigo ausente)
   - `"a-a"` / `- b` → `Texto: aba` / `Letras: 3` (substituição aumenta contagem de letras!)

5. **`F10_C03` (`analise.h` + `analise.c` + `main.c`):**
   - `2` linhas (`10 2 8` / `-5 0 3`) / `idx = 0` / `"algoritmos"` / `'o'` → `Linha 0: menor=2 maior=10` / `Ocorrencias: 2`
   - `2` linhas (`10 2 8` / `-5 0 -9`) / `idx = 1` / `"teste"` / `'z'` → `Linha 1: menor=-9 maior=0` / `Ocorrencias: 0`
   - `1` linha (`7 7 7`) / `idx = 0` / `"aaa"` / `'a'` → `Linha 0: menor=7 maior=7` / `Ocorrencias: 3`
   - `3` linhas (`1 2 3` / `4 5 6` / `-1 -2 -3`) / `idx = 2` / `"C99"` / `'9'` → `Linha 2: menor=-3 maior=-1` / `Ocorrencias: 2`
   - `2` linhas (`0 -1 1` / `2 3 4`) / `idx = 0` / `"x"` / `'x'` → `Linha 0: menor=-1 maior=1` / `Ocorrencias: 1`
