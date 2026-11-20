# Especificação de Testes — Bloco `E07`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, uso obrigatório de `static` nas matrizes grandes (`500 x 500`) e no cubo `10 x 10 x 10`, sem VLAs, funções customizadas, `struct`, `malloc`/`free` ou `FILE*`, saídas em ASCII puro.
- **Comparação de saídas:** correspondência textual exata e numérica com tolerância `0.01` em médias `%.2f`.
- **Casos de teste registrados:** 25 casos (5 por arquivo `.c`) em [casos_E07.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/casos_E07.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`E07_E03_corrigido.c`:**
   - Retangular `3 x 2` (`largura = 3, altura = 2`) com `delta = +30` → saturação em `255`
   - Retangular `2 x 3` (`largura = 2, altura = 3`) com `delta = -60` → saturação em `0`
   - Linha única `4 x 1` com `delta = 0` → pixels inalterados
   - Coluna única `1 x 3` com `delta = +20` → saturação superior
   - Borda `1 x 1` (`100`) com `delta = -300` → saturado para `0`

2. **`E07_E04.c`:**
   - Normal `3 x 2`, `delta = +20`, `limiar = 128` → `Pretos: 3 Brancos: 3`
   - Fronteira exata `== limiar` (`128` com `limiar = 128`) → vira `255`
   - Tudo branco (`limiar = 0` após `delta = -100`) → `Pretos: 0 Brancos: 3`
   - Limiar máximo `255` com saturação prévia → `Pretos: 2 Brancos: 2`
   - Borda `1 x 1` (`128` com `delta = -1`, `limiar = 128`) → cai para `127 < 128` → `Pretos: 1 Brancos: 0`

3. **`E07_E05.c`:**
   - Cubo `2 x 2 x 2` com `delta = +20` → somas por camada `425` e `570`, `Saturados: 2`
   - Cubo `2 x 1 x 3` com `delta = -35` → camada `0` toda saturada em `0`
   - Cubo `1 x 2 x 2` com `delta = 0` e extremos já existentes (`0` e `255`) → `Saturados: 2`
   - Pilha `3 x 1 x 1` com `delta = +30` → `Camada 0..2`, `Saturados: 1`
   - Cubo `2 x 2 x 1` com `delta = +100` → camada `0` saturada em `255`

4. **`E07_C02_corrigido.c`:**
   - Fronteira `127 / 128 / 129` com `limiar = 128` (`3 x 2`)
   - Retangular `2 x 3` com `limiar = 100` (múltiplos pixels iguais ao limiar)
   - Limiar `0` (`4 x 1`) → todos viram `255`
   - Limiar `255` (`1 x 3`) → apenas `255` vira `255`, `254` vira `0`
   - Borda `1 x 1` (`255`, `limiar = 255`) → `255`

5. **`E07_C03.c`:**
   - Normal `3 x 2`, `delta = +20`, `limiar = 128` → `Acima: 3`, `Media: 158.33`
   - Negativo `2 x 2`, `delta = -50`, `limiar = 100` → `Acima: 1`, `Media: 69.50`
   - Todos saturados em `255` (`1 x 3`) → `Acima: 3`, `Media: 255.00`
   - Todos saturados em `0` (`2 x 1`) → `Acima: 0`, `Media: 0.00`
   - Borda `1 x 1` (`128`, `delta = 0`, `limiar = 128`) → `Acima: 1`, `Media: 128.00`
