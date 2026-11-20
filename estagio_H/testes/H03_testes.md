# Especificação de Testes — Bloco `H03`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comandos de compilação 5-arquivos (nunca passar `.h` ao `gcc`):**
  - `H03_E03_corrigido`: `gcc -std=c99 -Wall -Wextra solucoes/H03_E03_corrigido/main.c solucoes/H03_E03_corrigido/imagem.c solucoes/H03_E03_corrigido/funcoes.c -o processador`
  - `H03_E04`: `gcc -std=c99 -Wall -Wextra solucoes/H03_E04/main.c solucoes/H03_E04/imagem.c solucoes/H03_E04/funcoes.c -o processador`
  - `H03_E05`: `gcc -std=c99 -Wall -Wextra solucoes/H03_E05/main.c solucoes/H03_E05/imagem.c solucoes/H03_E05/funcoes.c -o processador`
  - `H03_E06`: `gcc -std=c99 -Wall -Wextra solucoes/H03_E06/main.c solucoes/H03_E06/imagem.c solucoes/H03_E06/funcoes.c -o processador`
  - `H03_C02_corrigido`: `gcc -std=c99 -Wall -Wextra solucoes/H03_C02_corrigido/main.c solucoes/H03_C02_corrigido/imagem.c solucoes/H03_C02_corrigido/funcoes.c -o processador`
  - `H03_C03`: `gcc -std=c99 -Wall -Wextra solucoes/H03_C03/main.c solucoes/H03_C03/imagem.c solucoes/H03_C03/funcoes.c -o processador`
- **Restrições verificadas nos projetos de 5 arquivos:** parâmetro `int t` em `aplicarBlur(int img[ALTURA][LARGURA], int t)`, matriz auxiliar `static int aux[ALTURA][LARGURA];` copiada de `img` antes do cálculo, preservação de bordas (`r <= i < ALTURA - r` e `r <= j < LARGURA - r`), divisão inteira por `t * t`, `static int img[ALTURA][LARGURA];` em `main.c`, sem `struct`, sem `malloc`/`free`, sem VLAs, sem recursividade e saídas em ASCII puro.
- **Comparação de saídas:** correspondência textual exata.
- **Casos de teste registrados:** **30 casos** (5 por projeto 5-arquivos) em [casos_H03.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/casos_H03.json).

---

## Casos de Teste por Projeto 5-Arquivos (5 casos cada: normal + bordas)

1. **`H03_E03_corrigido` (`5 x 5`, `aplicarBlur` corrigido):**
   - `T1` (normal): matriz cruz `90/0` com `t = 3` (`r = 1`).
   - `T2` (borda): mesma matriz com `t = 5` (`r = 2`, apenas `(2,2) = 75` recalculado).
   - `T3` (normal): matriz assimétrica `5 x 5` com picos `200` e `220` (`t = 3`), detectando reutilização sem `aux`.
   - `T4` (borda): impulso central `255` com `t = 5` → `(2,2) = 10` (`255 / 25`).
   - `T5` (borda): `t = 4` inválido → `Tamanho t invalido.`.

2. **`H03_E04` (`5 x 5`, blur fixo `t = 3`):**
   - `T1` (normal): matriz `90/0` (`70/60/50` internos, bordas `90`).
   - `T2` (normal): matriz assimétrica `5 x 5`.
   - `T3` (borda): impulso central `255` cercado de `0`s → bloco `3 x 3` interno vira `28` (`255 / 9`).
   - `T4` (borda): matriz uniforme `255` inalterada.
   - `T5` (borda): assinatura `P5` inválida → `Erro ao ler imagem.`.

3. **`H03_E05` (`7 x 7`, blur parametrizável `t` em `{3, 5, 7}`):**
   - `T1` (normal): matriz assimétrica `7 x 7` com `t = 3` (`25` pixels internos).
   - `T2` (normal): matriz assimétrica `7 x 7` com `t = 5` (`9` pixels internos, `2` linhas/colunas de borda preservadas).
   - `T3` (borda): matriz assimétrica `7 x 7` com `t = 7` (apenas `(3,3) = 92` recalculado).
   - `T4` (borda): pico central `247` sobre fundo `100` com `t = 7` → `(3,3) = 103`.
   - `T5` (borda): `t = 1` inválido → `Tamanho t invalido.`.

4. **`H03_E06` (`7 x 7`, `aplicarBlur` + `ajustarBrilho` encadeados):**
   - `T1` (normal): quadrado interno `50` sobre fundo `200`, `t = 3` seguido de `b = +20`.
   - `T2` (borda): mesma matriz com `t = 5` e `b = -180` (pixels internos saturam em `0`, bordas caem para `20`).
   - `T3` (borda): dois picos `255` (`(0,0)` e `(3,3)`), `t = 7` seguido de `b = +250` (saturação em `255`).
   - `T4` (borda): `t = 9` inválido → `Tamanho t invalido.`.
   - `T5` (borda): dimensões inválidas `5 7` → `Erro ao ler imagem.`.

5. **`H03_C02_corrigido` (`5 x 5`, `aplicarBlur` corrigido):**
   - `T1` (normal): matriz `90/0` com `t = 3`.
   - `T2` (normal): matriz assimétrica `5 x 5` com `t = 5` (`(2,2) = 58`).
   - `T3` (borda): impulso central `255` com `t = 3`.
   - `T4` (borda): matriz uniforme `255` com `t = 5`.
   - `T5` (borda): `t = 6` inválido → `Tamanho t invalido.`.

6. **`H03_C03` (`7 x 7`, `aplicarBlur` independente):**
   - `T1` (normal): matriz assimétrica `7 x 7` com `t = 3`.
   - `T2` (normal): pico central `247` sobre fundo `100` com `t = 5` (bloco `3 x 3` interno `= 105`).
   - `T3` (borda): matriz assimétrica `7 x 7` com `t = 5`.
   - `T4` (borda): matriz uniforme `10` com `t = 7`.
   - `T5` (borda): `t = 2` inválido → `Tamanho t invalido.`.
