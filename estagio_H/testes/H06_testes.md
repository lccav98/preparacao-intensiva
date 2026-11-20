# Especificação de Testes — Bloco `H06`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comandos de compilação multi-arquivo (nunca passar `.h` ao `gcc`):**
  - `H06_E03_corrigido`: `gcc -std=c99 -Wall -Wextra solucoes/H06_E03_corrigido/main.c solucoes/H06_E03_corrigido/imagem.c solucoes/H06_E03_corrigido/funcoes.c -o prog`
  - `H06_E04`: `gcc -std=c99 -Wall -Wextra solucoes/H06_E04/main.c solucoes/H06_E04/imagem.c solucoes/H06_E04/funcoes.c -o prog`
  - `H06_E05`: `gcc -std=c99 -Wall -Wextra solucoes/H06_E05/main.c solucoes/H06_E05/imagem.c solucoes/H06_E05/funcoes.c -o prog`
  - `H06_E06`: `gcc -std=c99 -Wall -Wextra solucoes/H06_E06/main.c solucoes/H06_E06/imagem.c solucoes/H06_E06/funcoes.c -o prog`
  - `H06_C03`: `gcc -std=c99 -Wall -Wextra solucoes/H06_C03/main.c solucoes/H06_C03/imagem.c solucoes/H06_C03/funcoes.c -o prog`
  - `H06_OP1_opcional` *(não bloqueante)*: `gcc -std=c99 -Wall -Wextra solucoes/H06_OP1_opcional/main.c solucoes/H06_OP1_opcional/imagem.c solucoes/H06_OP1_opcional/funcoes.c -o prog`
  - `H06_OP2_opcional` *(não bloqueante, 7 arquivos)*: `gcc -std=c99 -Wall -Wextra solucoes/H06_OP2_opcional/main.c solucoes/H06_OP2_opcional/imagem.c solucoes/H06_OP2_opcional/funcoes.c solucoes/H06_OP2_opcional/estatisticas.c -o prog`
- **Restrições verificadas:** guardas `#ifndef` em todos os `.h`, `const` em funções somente leitura, ponteiros de saída em `resumoImagem` (`H06_E06`), recursão pura por linhas sem laço externo em `H06_OP1_opcional`, sem `struct`, sem `malloc`/`free`, sem VLAs, sem `gets(` e saídas em ASCII puro.
- **Comparação de saídas e tolerância:**
  - Inteiros, mensagens do menu e matrizes PGM P2: correspondência textual exata.
  - Médias (`%.2f` em `H06_E06` e `H06_OP2_opcional`): correspondência textual exata e tolerância numérica de **`1e-2`**.
- **Casos de teste registrados:** **35 casos** (**25 obrigatórios** + **10 `[OPCIONAIS]`**, 5 por projeto) em [casos_H06.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/casos_H06.json).

---

## Casos de Teste por Projeto (5 casos por projeto: normal + bordas críticas)

1. **`H06_E03_corrigido` (`inverterCores` corrigido):**
   - `T1` (normal): `4 -> 0` sobre `A`.
   - `T2` (normal): `1 20 -> 4 -> 0` sobre `B`.
   - `T3` (borda): dupla inversão `4 -> 4 -> 0` restaura imagem original `C`.
   - `T4` (borda): opção `9` e `t = 4` rejeitados antes de `4 -> 3 -> 0`.
   - `T5` (borda): cabeçalho inválido `P3` rejeitado com `Erro ao ler imagem.`.

2. **`H06_E04` (Modificação ao vivo 1 — `limiarizar`):**
   - `T1` (normal): `4 30 -> 0`.
   - `T2` (normal): `1 -20 -> 3 -> 4 128 -> 0`.
   - `T3` (borda): rejeita `-1` e `256`, aceita fronteira `255`.
   - `T4` (borda): `2 5 -> 4 100 -> 0`.
   - `T5` (borda): dimensão `3 3` rejeitada com `Erro ao ler imagem.`.

3. **`H06_E05` (Modificação ao vivo 2 — `espelharHorizontal`):**
   - `T1` (normal): `4 -> 0` sobre `D` (linhas espelhadas).
   - `T2` (borda): duplo espelhamento `4 -> 4 -> 0` restaura `D` original.
   - `T3` (normal): `1 15 -> 4 -> 3 -> 0`.
   - `T4` (borda): `2 3 -> 4 -> 9 -> 0` (rejeita `9`).
   - `T5` (borda): `4 -> 2 7 -> 0`.

4. **`H06_E06` (Simulado final — `resumoImagem` com ponteiros ao sair):**
   - `T1` (normal): `1 20 -> 3 -> 0` $\rightarrow$ `Minimo` / `Maximo` / `Media` + PGM P2.
   - `T2` (normal): `2 3 -> 4 100 -> 0` $\rightarrow$ mínimo `0`, máximo `255` e média binarizada.
   - `T3` (borda): saída imediata `0` sobre `B`.
   - `T4` (borda): `4 260` rejeitado antes de `2 7 -> 0`.
   - `T5` (borda): imagem toda preta `0` com `1 -10 -> 0` $\rightarrow$ `Minimo: 0`, `Maximo: 0`, `Media: 0.00`.

5. **`H06_C03` (Checagem independente — `aplicarNegativo`):**
   - `T1` (normal): `4 -> 1 -20 -> 0`.
   - `T2` (normal): `3 -> 4 -> 0`.
   - `T3` (borda): dupla aplicação `4 -> 4 -> 0`.
   - `T4` (borda): opção `8` e `t = 2` rejeitados entre filtros válidos.
   - `T5` (borda): cabeçalho `P3` rejeitado com `Erro ao ler imagem.`.

6. **`H06_OP1_opcional` *(Opcional não bloqueante — `ajustarBrilhoLinhaRec`)*:**
   - `T1`–`T5`: deltas `+30`, `-40`, `0`, `+300` (satura tudo em `255`) e `-300` (satura tudo em `0`).

7. **`H06_OP2_opcional` *(Opcional não bloqueante — módulo `estatisticas.h/.c`)*:**
   - `T1`–`T5`: consulta estatística antes/depois de brilho, mediana e blur `7 x 7`, além de imagem constante `255` (`Media: 255.00`).
