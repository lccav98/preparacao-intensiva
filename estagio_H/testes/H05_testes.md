# Especificação de Testes — Bloco `H05`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comandos de compilação multi-arquivo (5 arquivos por projeto; nunca passar `.h` ao `gcc`):**
  - `H05_E03_corrigido`: `gcc -std=c99 -Wall -Wextra solucoes/H05_E03_corrigido/main.c solucoes/H05_E03_corrigido/imagem.c solucoes/H05_E03_corrigido/funcoes.c -o prog`
  - `H05_E04`: `gcc -std=c99 -Wall -Wextra solucoes/H05_E04/main.c solucoes/H05_E04/imagem.c solucoes/H05_E04/funcoes.c -o prog`
  - `H05_E05`: `gcc -std=c99 -Wall -Wextra solucoes/H05_E05/main.c solucoes/H05_E05/imagem.c solucoes/H05_E05/funcoes.c -o prog`
  - `H05_E06`: `gcc -std=c99 -Wall -Wextra solucoes/H05_E06/main.c solucoes/H05_E06/imagem.c solucoes/H05_E06/funcoes.c -o prog`
  - `H05_C03`: `gcc -std=c99 -Wall -Wextra solucoes/H05_C03/main.c solucoes/H05_C03/imagem.c solucoes/H05_C03/funcoes.c -o prog`
- **Restrições verificadas nos projetos:** leitura única de `lerImagem(img)` antes do `do-while` com retorno de erro (`return 1;`), somente `main` em `main.c`, validação `t in {3, 5, 7}`, `break` em todos os `case`, preservação de bordas no `blur` e `mediana`, sem `struct`, sem `malloc`/`free`, sem VLAs e saídas em ASCII puro.
- **Comparação de saídas:** correspondência textual exata de prompts do menu, mensagens de erro, contadores e matriz `P2` `7 x 7` gravada ao sair.
- **Casos de teste registrados:** **25 casos** (5 por projeto 5-arquivos) em [casos_H05.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/casos_H05.json).

---

## Casos de Teste por Projeto 5-Arquivos (5 casos por projeto: encadeamento + validação + falhas)

1. **`H05_E03_corrigido` (`main.c` corrigido com `do-while` + `switch`):**
   - `T1` (normal): `1 20 -> 3 -> 0` sobre `A` $\rightarrow$ mediana opera sobre a imagem com brilho ajustado.
   - `T2` (normal): `2 5 -> 1 -30 -> 0` sobre `B` $\rightarrow$ blur `5 x 5` seguido de brilho negativo com saturação em `0`.
   - `T3` (borda): `2 4 -> 9 -> 3 -> 0` sobre `C` $\rightarrow$ rejeita `t = 4` e opção `9`, aplica mediana e salva.
   - `T4` (borda): cabeçalho inválido `P3` $\rightarrow$ encerra imediatamente antes do menu com `Erro ao ler imagem.`.
   - `T5` (borda): `2 7 -> 0` sobre `B` $\rightarrow$ blur `7 x 7` altera apenas o pixel central `(3, 3)`.

2. **`H05_E04` (Menu padrão completo em `7 x 7`):**
   - `T1` (normal): cadeia de 3 operações `1 30 -> 2 3 -> 3 -> 0`.
   - `T2` (normal): `3 -> 1 20 -> 0` (mediana seguida de brilho).
   - `T3` (borda): `2 7 -> 0` sobre `C`.
   - `T4` (borda): rejeições sucessivas `t = 2`, `t = 6`, opção `8`, depois `0` (imagem preservada).
   - `T5` (borda): dimensão `5 5` incompatível com `7 x 7` $\rightarrow$ `Erro ao ler imagem.`.

3. **`H05_E05` (Menu com `Operacoes aplicadas: K`):**
   - `T1` (normal): `1 15 -> 3 -> 0` $\rightarrow$ `Operacoes aplicadas: 2`.
   - `T2` (borda): saída imediata `0` $\rightarrow$ `Operacoes aplicadas: 0` e imagem intacta.
   - `T3` (borda): `9` (inválida) + `2 4` (inválido) + `1 -10` + `2 3` + `0` $\rightarrow$ `Operacoes aplicadas: 2` (erros não contam!).
   - `T4` (normal): `2 5 -> 3 -> 1 -50 -> 0` $\rightarrow$ `Operacoes aplicadas: 3`.
   - `T5` (borda): `maxval = 100 != 255` $\rightarrow$ `Erro ao ler imagem.`.

4. **`H05_E06` (Menu estendido com opção `4 - Aplicar limiarizacao`):**
   - `T1` (normal): `3 -> 4 30 -> 0`.
   - `T2` (normal): `1 20 -> 4 120 -> 0`.
   - `T3` (borda): `4 -5` e `4 300` rejeitados (`Limiar invalido. Use 0 a 255.`), seguidos de `2 3 -> 4 100 -> 0`.
   - `T4` (borda): opção `7` e `t = 9` rejeitados antes de `0`.
   - `T5` (normal): `3 -> 1 55 -> 4 255 -> 0` (fronteira máxima `255`).

5. **`H05_C03` (Checagem independente — 5 arquivos completo):**
   - `T1` (normal): `1 -10 -> 2 3 -> 0`.
   - `T2` (normal): `3 -> 2 5 -> 1 25 -> 0`.
   - `T3` (borda): `2 7 -> 1 -200 -> 0`.
   - `T4` (borda): opção `5` e `t = 4` rejeitados antes de `0`.
   - `T5` (borda): cabeçalho `P3` rejeitado com `Erro ao ler imagem.`.
