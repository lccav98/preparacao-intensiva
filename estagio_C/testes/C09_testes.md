# Especificação de Testes — Bloco `C09`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99** (`gcc -std=c99 -Wall -Wextra`).
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Critério de comparação:**
  - Comparação textual exata caractere por caractere após normalização de `\r\n` $\rightarrow$ `\n`.
  - Atenção estrita ao alinhamento por largura fixa (`%3d`, `%4d`) e ausência de espaços extras ao final das linhas.
  - Saídas estritamente em ASCII puro com `\n` final.
- **Status de execução e fronteiras:**
  - Ausência total de vetores/arrays (`v[i]`), strings (`char[]`), funções próprias além de `int main(void)` e alocação dinâmica.
  - Cobertura de casos normais, bordas unitárias (`1`, `2 2`, `28 1`, `31 7`), entradas inválidas (`<= 0`, `< 2`, calendário fora de faixa) e casos extremos maiores (números de 2 dígitos testando alinhamento).

---

## Casos de Teste por Programa

### 1. `C09_E02_corrigido.c` (Triângulo Crescente com `%3d`)
- **Entradas:** `int n`.
- **Casos:**
  - `4` (normal) $\rightarrow$ 4 linhas (`  1`, `  1  2`, `  1  2  3`, `  1  2  3  4`)
  - `1` (borda unitária) $\rightarrow$ `  1`
  - `0` (borda inválida) $\rightarrow$ `Entrada Invalida`
  - `6` (extremo) $\rightarrow$ 6 linhas

---

### 2. `C09_E03.c` (Grade de Tabuada $L \times C$ com `%4d`)
- **Entradas:** `int linhas, cols`.
- **Casos:**
  - `3 4` (normal do enunciado) $\rightarrow$ grade $3 \times 4$
  - `1 1` (borda unitária) $\rightarrow$ `   1`
  - `0 4` (borda inválida) $\rightarrow$ `Entrada Invalida`
  - `5 5` (extremo com produtos de 2 dígitos até 25) $\rightarrow$ grade $5 \times 5$

---

### 3. `C09_E04.c` (Triângulo Invertido com `%3d`)
- **Entradas:** `int n`.
- **Casos:**
  - `4` (normal do enunciado) $\rightarrow$ 4 linhas decrescentes
  - `1` (borda unitária) $\rightarrow$ `  1`
  - `-3` (borda negativa inválida) $\rightarrow$ `Entrada Invalida`
  - `6` (extremo) $\rightarrow$ 6 linhas decrescentes

---

### 4. `C09_E05.c` (Calendário Mensal Formatado)
- **Entradas:** `int dias, inicio`.
- **Casos:**
  - `30 3` (normal do enunciado: mês de 30 dias iniciando na terça)
  - `28 1` (borda exata: 4 semanas cheias, domingo a sábado)
  - `31 7` (borda extrema: mês de 31 dias iniciando no sábado, 6 semanas)
  - `27 2` (borda inválida de dias) $\rightarrow$ `Entrada Invalida`
  - `30 8` (borda inválida de dia inicial) $\rightarrow$ `Entrada Invalida`

---

### 5. `C09_E06.c` (Moldura Retangular Oca `#`)
- **Entradas:** `int linhas, cols`.
- **Casos:**
  - `4 5` (normal do enunciado)
  - `2 2` (borda mínima sem interior oco: `##\n##`)
  - `1 5` (borda inválida $< 2$) $\rightarrow$ `Entrada Invalida`
  - `5 8` (extremo maior)

---

### 6. `C09_C02_corrigido.c` (Grade Sequencial Alinhada `%3d`)
- **Entradas:** `int linhas, cols`.
- **Casos:**
  - `3 4` (normal: 1 a 12)
  - `1 5` (borda de 1 linha)
  - `3 0` (borda inválida) $\rightarrow$ `Entrada Invalida`
  - `4 5` (extremo: 1 a 20)

---

### 7. `C09_C03.c` (Triângulo de Floyd `%3d`)
- **Entradas:** `int n`.
- **Casos:**
  - `4` (normal do enunciado: 1 a 10)
  - `1` (borda unitária: `  1`)
  - `0` (borda inválida) $\rightarrow$ `Entrada Invalida`
  - `6` (extremo: 1 a 21, testando alinhamento de 1 e 2 dígitos)
