# Especificação de Testes — Bloco `H04`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comandos de compilação multi-arquivo (5 arquivos por projeto; nunca passar `.h` ao `gcc`):**
  - `H04_E03_corrigido`: `gcc -std=c99 -Wall -Wextra solucoes/H04_E03_corrigido/main.c solucoes/H04_E03_corrigido/imagem.c solucoes/H04_E03_corrigido/funcoes.c -o prog`
  - `H04_E04`: `gcc -std=c99 -Wall -Wextra solucoes/H04_E04/main.c solucoes/H04_E04/imagem.c solucoes/H04_E04/funcoes.c -o prog`
  - `H04_E05`: `gcc -std=c99 -Wall -Wextra solucoes/H04_E05/main.c solucoes/H04_E05/imagem.c solucoes/H04_E05/funcoes.c -o prog`
  - `H04_E06`: `gcc -std=c99 -Wall -Wextra solucoes/H04_E06/main.c solucoes/H04_E06/imagem.c solucoes/H04_E06/funcoes.c -o prog`
  - `H04_C03`: `gcc -std=c99 -Wall -Wextra solucoes/H04_C03/main.c solucoes/H04_C03/imagem.c solucoes/H04_C03/funcoes.c -o prog`
- **Nota sobre E/S PGM P2 nos testes automatizados:** Em `solucoes/`, `imagem.c` implementa `lerImagem` e `salvarImagem` lendo/gravando o formato PGM P2 (`5 x 5`) via `stdin`/`stdout`, permitindo executar todos os casos determinísticos sem arquivos externos em disco e mantendo `main.c` livre de `FILE*`.
- **Restrições verificadas nos projetos:** guardas `#ifndef` em `imagem.h` e `funcoes.h`, inclusão `"imagem.h"` em `funcoes.h`, matriz auxiliar `static int aux[ALTURA][LARGURA]`, reinício `int k = 0;` por pixel interno, uso da função `ordenar(v, 9)` fornecida e seleção de `v[4]`, bordas preservadas, sem `struct`, sem `malloc`/`free`, sem VLAs e saídas em ASCII puro.
- **Comparação de saídas:** correspondência textual exata de cabeçalho `P2`, matriz de pixels e contadores.
- **Casos de teste registrados:** **25 casos** (5 por projeto 5-arquivos) em [casos_H04.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/casos_H04.json).

---

## Casos de Teste por Projeto 5-Arquivos (5 casos por projeto: normal + bordas críticas)

1. **`H04_E03_corrigido` e `H04_E04` (`aplicarMediana` em `5 x 5`):**
   - `T1` (normal): imagem `5 x 5` com ruídos sal (`255`) e pimenta (`0`) internos $\rightarrow$ ruídos removidos e bordas preservadas.
   - `T2` (borda): imagem `5 x 5` com ruídos `0` e `255` alternados na borda externa e `20` isolado no centro `(2, 2)` $\rightarrow$ toda a borda permanece intacta e o centro torna-se `10`.
   - `T3` (borda): imagem uniforme (`100` em todas as posições) $\rightarrow$ matriz resultante idêntica.
   - `T4` (normal): imagem com risco de contaminação cruzada entre `(1, 1)` e `(1, 2)` $\rightarrow$ valida leitura exclusiva da matriz original antes da cópia final.
   - `T5` (normal): quadrado `3 x 3` de intensidade `200` com buraco `0` no centro $\rightarrow$ centro preenchido para `200` e cantos do quadrado suavizados para `20`.

2. **`H04_E05` (`passos` aplicações sucessivas da mediana):**
   - `T1`: `passos = 1` sobre `M1` $\rightarrow$ resultado após 1 mediana.
   - `T2`: `passos = 2` sobre `M2` $\rightarrow$ bordas `0`/`255` preservadas mesmo após 2 passagens.
   - `T3`: `passos = 0` sobre `M3` (borda de repetição nula) $\rightarrow$ imagem original intacta.
   - `T4`: `passos = 2` sobre `M4` $\rightarrow$ 2ª passada opera sobre o resultado da 1ª.
   - `T5`: `passos = 3` sobre `M5` $\rightarrow$ convergência após 3 passagens mantendo `(2, 2) = 20` na 3ª passagem.

3. **`H04_E06` (`mediana` + `Pixels alterados: K`):**
   - `T1`: `M1` $\rightarrow$ `Pixels alterados: 7`.
   - `T2`: `M2` $\rightarrow$ `Pixels alterados: 1`.
   - `T3`: `M3` (uniforme) $\rightarrow$ `Pixels alterados: 0`.
   - `T4`: `M4` $\rightarrow$ `Pixels alterados: 8`.
   - `T5`: `M5` $\rightarrow$ `Pixels alterados: 5`.

4. **`H04_C03` (`aplicarMediana` seguida de `limiarizar`):**
   - `T1`: `M1`, `limiar = 13` $\rightarrow$ mediana elimina `255`/`0` antes da binarização.
   - `T2`: `M2`, `limiar = 15` $\rightarrow$ ruídos de borda `255` preservados; interior todo `0`.
   - `T3`: `M3`, `limiar = 100` (fronteira exata `>= limiar`) $\rightarrow$ todos os pixels viram `255`.
   - `T4`: `M4`, `limiar = 40` $\rightarrow$ binarização coerente sobre a imagem filtrada.
   - `T5`: `M5`, `limiar = 200` (fronteira exata `>= 200`) $\rightarrow$ cruz central permanece `255`.
