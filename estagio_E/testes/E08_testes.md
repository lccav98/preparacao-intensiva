# Especificação de Testes — Bloco `E08`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, nenhuma função além de `int main(void)`, sem VLAs, sem `struct`, sem `malloc`/`free` ou `FILE*`, uso de `static` em matrizes de imagem grandes, saídas em ASCII puro.
- **Comparação de saídas:** correspondência textual e numérica exata linha a linha.
- **Casos de teste registrados:** 35 casos (5 por arquivo `.c`) em [casos_E08.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_E/testes/casos_E08.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`E08_E02_corrigido.c`:**
   - Matriz identidade `3 x 3` → somas `1, 1, 1`, `Maior: 1 em (0, 0)`, `Identidade: Sim`
   - Matriz `2 x 2` toda de `1` (pega falso positivo na diagonal!) → `Identidade: Nao`
   - Matriz `2 x 2` toda negativa (`-5 -2 / -9 -2`) → `Maior: -2 em (0, 1)`, `Identidade: Nao`
   - Matriz `3 x 3` geral → somas por coluna `9, 10, 13`, `Maior: 9 em (2, 2)`
   - Borda `1 x 1` (`1`) → `Identidade: Sim`

2. **`E08_E03_corrigido.c`:**
   - Retangular `3 x 2` com `delta = +30` → transposta PGM P2 `2 x 3` com saturação superior
   - Retangular `2 x 3` com `delta = -60` → transposta PGM P2 `3 x 2` com saturação inferior
   - Linha `4 x 1` (`delta = 0`) → coluna `1 x 4`
   - Coluna `1 x 3` (`delta = -15`) → linha `3 x 1`
   - Borda `1 x 1` (`250`, `delta = +20`) → `255`

3. **`E08_E04.c`:**
   - Matriz `3 x 3` (`1..9`) → DP `15`, DS `15`, Acima `11`, Abaixo `19`
   - Matriz `2 x 2` com negativos → DP `-3`, DS `7`, Acima `3`, Abaixo `4`
   - Identidade `4 x 4` → DP `4`, DS `0`, Acima `0`, Abaixo `0`
   - Borda `1 x 1` (`42`) → DP `42`, DS `42`, Acima `0`, Abaixo `0`
   - Antissimétrica `3 x 3` → DP `0`, DS `0`, Acima `6`, Abaixo `-6`

4. **`E08_E05.c`:**
   - Produto `A * A^T` (`2 x 3` por `3 x 2`) → `14 32 / 32 77`, `Simetrica: Sim`, `Alvo encontrado em (0, 1)`
   - Produto `2 x 2` não simétrico e alvo ausente → `Simetrica: Nao`, `Alvo nao encontrado`
   - Dimensões incompatíveis (`2 x 3` por `2 x 2`) → `Multiplicacao impossivel`
   - Produto retangular `2 x 3` por `3 x 1` → `2 x 1`, `Simetrica: Nao`, `Alvo encontrado em (1, 0)`
   - Borda `1 x 1` (`-3 * -4 = 12`) → `Simetrica: Sim`, `Alvo encontrado em (0, 0)`

5. **`E08_E06.c`:**
   - Normal `3 x 2`, `delta = +20`, `limiar = 128` → `Minimo: 20 em (1, 0)`, `Maximo: 255 em (0, 2)`, `Pretos: 2 Brancos: 4`
   - Saturação inferior completa `2 x 2` (`delta = -100`) → `Minimo: 0 em (0, 0)`, `Maximo: 0 em (0, 0)`, `Pretos: 4 Brancos: 0`
   - Todos `>= limiar` (`2 x 2`, `limiar = 50`) → `Pretos: 0 Brancos: 4`
   - Fronteira exata `== limiar` (`127 + 1 = 128` com `limiar = 128`) → `Pretos: 1 Brancos: 2`
   - Borda `1 x 1` (`200`, `delta = +100`, `limiar = 255`) → `255`, `Pretos: 0 Brancos: 1`

6. **`E08_C02.c`:**
   - Retangular `2 x 3` → transposta `3 x 2`, alvo encontrado em `(1, 0)`
   - Empates em `T` (`2 x 2`, tudo `5`) → 1ª ocorrência `(0, 0)`
   - Soma nula `1 x 3` com alvo ausente → `Busca em T: nao encontrado`
   - Coluna `3 x 1` → linha `1 x 3`, alvo em `(0, 2)`
   - Borda `1 x 1` → `(0, 0)`

7. **`E08_C03.c`:**
   - Produto `2 x 2` com negativos saturados em `0` → `Identidade (antes de saturar): Nao`
   - Produto de matrizes inversas (`[1 2; 0 1] * [1 -2; 0 1] = I_2`) → `Identidade (antes de saturar): Sim`
   - Produto com valores `> 255` saturados em `255` → `Identidade (antes de saturar): Nao`
   - Identidade `3 x 3` → `Identidade (antes de saturar): Sim`
   - Borda `1 x 1` negativo (`-5 * 10 = -50` → saturado `0`) → `Identidade (antes de saturar): Nao`
