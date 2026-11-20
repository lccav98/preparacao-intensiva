# Especificação de Testes — Bloco `H02`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comandos de compilação 5-arquivos (nunca passar `.h` ao `gcc`):**
  - `H02_E03_corrigido`: `gcc -std=c99 -Wall -Wextra solucoes/H02_E03_corrigido/main.c solucoes/H02_E03_corrigido/imagem.c solucoes/H02_E03_corrigido/funcoes.c -o processador`
  - `H02_E04`: `gcc -std=c99 -Wall -Wextra solucoes/H02_E04/main.c solucoes/H02_E04/imagem.c solucoes/H02_E04/funcoes.c -o processador`
  - `H02_E05`: `gcc -std=c99 -Wall -Wextra solucoes/H02_E05/main.c solucoes/H02_E05/imagem.c solucoes/H02_E05/funcoes.c -o processador`
  - `H02_C02_corrigido`: `gcc -std=c99 -Wall -Wextra solucoes/H02_C02_corrigido/main.c solucoes/H02_C02_corrigido/imagem.c solucoes/H02_C02_corrigido/funcoes.c -o processador`
  - `H02_C03`: `gcc -std=c99 -Wall -Wextra solucoes/H02_C03/main.c solucoes/H02_C03/imagem.c solucoes/H02_C03/funcoes.c -o processador`
- **Restrições verificadas nos projetos de 5 arquivos:** saturação `[0, 255]` por condicionais (sem `% 256`), fronteira exata `>= limiar -> 255`, assinatura idêntica `.h`/`.c`, `static int img[ALTURA][LARGURA]` em `main.c`, sem `struct`, sem `malloc`/`free`, sem VLAs, sem recursividade e saídas em ASCII puro.
- **Comparação de saídas:** correspondência textual exata.
- **Casos de teste registrados:** **25 casos** (5 por projeto 5-arquivos) em [casos_H02.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/casos_H02.json).

---

## Casos de Teste por Projeto 5-Arquivos (5 casos cada: normal + bordas)

1. **`H02_E03_corrigido` (`3 x 3`, `ajustarBrilho`):**
   - `T1` (normal): `b = +30` com saturação em `240` e `255`.
   - `T2` (borda): `b = -30` com saturação em `10` e `0`.
   - `T3` (borda): `b = 0` (identidade).
   - `T4` (borda): `b = +300` (saturação total em `255`).
   - `T5` (borda): `b = -300` (saturação total em `0`).

2. **`H02_E04` (`3 x 3`, `ajustarBrilho` + `contarExtremos`):**
   - `T1` (normal): `b = +30` resultando em `Extremos (0 ou 255): 3`.
   - `T2` (normal): `b = -30` resultando em `Extremos (0 ou 255): 4`.
   - `T3` (borda): nenhum extremo após ajuste (`Extremos (0 ou 255): 0`).
   - `T4` (borda): todos os 9 pixels saturam em `255` (`Extremos (0 ou 255): 9`).
   - `T5` (borda): PGM inválido (`P5`) → `Erro ao ler imagem.`.

3. **`H02_E05` (`3 x 4`, `ajustarBrilho` seguido de `limiarizar`):**
   - `T1` (normal): `b = 30`, `limiar = 128` (fronteira exata `97 + 30 = 127 < 128` vs `98 + 30 = 128 >= 128`).
   - `T2` (borda): `b = 100`, `limiar = 255` (testando pixels saturados em `255`).
   - `T3` (borda): `b = -40`, `limiar = 100` (pixels `140 - 40 = 100` e `141 - 40 = 101`).
   - `T4` (borda): `b = -200` (todos viram `0`) com `limiar = 0` (`0 >= 0` → todos `255`).
   - `T5` (borda): dimensões invertidas `3 4` em vez de `4 3` → `Erro ao ler imagem.`.

4. **`H02_C02_corrigido` (`3 x 3`, `limiarizar`):**
   - `T1` (normal): fronteira `99`, `100`, `101` com `L = 100`.
   - `T2` (borda): todos os pixels exatamente iguais a `L = 50` → todos `255`.
   - `T3` (borda): `L = 255` (apenas `255` permanece `255`).
   - `T4` (normal): `L = 0` (todos `255`).
   - `T5` (borda): `maxval = 128` inválido → `Erro ao ler imagem.`.

5. **`H02_C03` (`3 x 3`, `ajustarBrilho` independente):**
   - `T1` (normal): `b = +40` com saturações superiores.
   - `T2` (normal): `b = -40` com saturações inferiores.
   - `T3` (borda): `b = -255` zerando até `255`.
   - `T4` (borda): `b = +255` saturando `0` em `255`.
   - `T5` (borda): `b = 0` preservando todos os valores.
