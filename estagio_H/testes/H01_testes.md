# Especificação de Testes — Bloco `H01`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comandos de compilação 5-arquivos (nunca passar `.h` ao `gcc`):**
  - `H01_E03_corrigido`: `gcc -std=c99 -Wall -Wextra solucoes/H01_E03_corrigido/main.c solucoes/H01_E03_corrigido/imagem.c solucoes/H01_E03_corrigido/funcoes.c -o processador`
  - `H01_E04`: `gcc -std=c99 -Wall -Wextra solucoes/H01_E04/main.c solucoes/H01_E04/imagem.c solucoes/H01_E04/funcoes.c -o processador`
  - `H01_E05`: `gcc -std=c99 -Wall -Wextra solucoes/H01_E05/main.c solucoes/H01_E05/imagem.c solucoes/H01_E05/funcoes.c -o processador`
  - `H01_C02_corrigido`: `gcc -std=c99 -Wall -Wextra solucoes/H01_C02_corrigido/main.c solucoes/H01_C02_corrigido/imagem.c solucoes/H01_C02_corrigido/funcoes.c -o processador`
  - `H01_C03`: `gcc -std=c99 -Wall -Wextra solucoes/H01_C03/main.c solucoes/H01_C03/imagem.c solucoes/H01_C03/funcoes.c -o processador`
- **Restrições verificadas nos projetos de 5 arquivos:** guardas `#ifndef`/`#define`/`#endif` em `imagem.h` e `funcoes.h`, `#include "imagem.h"` dentro de `funcoes.h`, `static int img[ALTURA][LARGURA]` em `main.c`, sem `struct`, sem `malloc`/`free`, sem VLAs e saídas em ASCII puro.
- **Comparação de saídas:** correspondência textual exata para cabeçalho PGM P2 (`P2`, `<largura> <altura>`, `255`), pixels e mensagens de contagem/erro.
- **Casos de teste registrados:** **25 casos** (5 por projeto 5-arquivos) em [casos_H01.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/casos_H01.json).

---

## Casos de Teste por Projeto 5-Arquivos (5 casos cada: normal + bordas)

1. **`H01_E03_corrigido` (`3 x 4`, limiarização):**
   - `T1` (normal): limiar `128` sobre valores abaixo, iguais e acima do limiar.
   - `T2` (borda): limiar `0` (todos os pixels viram `255`).
   - `T3` (borda): limiar `256` (todos os pixels viram `0`).
   - `T4` (borda): fronteira exata `99`, `100`, `101` com limiar `100`.
   - `T5` (borda): assinatura `P5` inválida → `Erro ao ler imagem.`.

2. **`H01_E04` (`3 x 3`, negativo `255 - p`):**
   - `T1` (normal): valores variados (`0, 128, 255, 55, 100, 200, 10, 245, 127`).
   - `T2` (borda): imagem totalmente preta (`0` → `255`).
   - `T3` (borda): imagem totalmente branca (`255` → `0`).
   - `T4` (normal): gradiente `1..9`.
   - `T5` (borda): dimensão divergente `4 3` → `Erro ao ler imagem.`.

3. **`H01_E05` (`2 x 4`, limiarização + `contarBrancos`):**
   - `T1` (normal): limiar `128` resultando em `Brancos: 4`.
   - `T2` (borda): nenhum pixel `>= 100` → `Brancos: 0`.
   - `T3` (borda): todos os pixels `== 100` com limiar `100` → `Brancos: 8`.
   - `T4` (normal): fronteira `126..129` e extremos `0/255`.
   - `T5` (borda): `maxval = 100` inválido → `Erro ao ler imagem.`.

4. **`H01_C02_corrigido` (`3 x 3`, `zerarBordas`):**
   - `T1` (normal): preserva apenas o pixel central `(1,1) = 150`.
   - `T2` (borda): bordas `255` e centro `0` → toda a matriz vira `0`.
   - `T3` (borda): centro `255` preservado e bordas zeradas.
   - `T4` (normal): bordas já zeradas e centro `77`.
   - `T5` (borda): assinatura `P1` inválida → `Erro ao ler imagem.`.

5. **`H01_C03` (`3 x 3`, `espelharHorizontal`):**
   - `T1` (normal): matriz assimétrica `10..90`.
   - `T2` (borda): matriz simétrica horizontalmente (inalterada).
   - `T3` (normal): extremos `0, 128, 255` rotacionados por linha.
   - `T4` (borda): matriz uniforme `42`.
   - `T5` (borda): altura divergente `3 4` → `Erro ao ler imagem.`.
