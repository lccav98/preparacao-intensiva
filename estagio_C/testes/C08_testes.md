# Especificação de Testes — Bloco `C08`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99** (`gcc -std=c99 -Wall -Wextra`).
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Critério de comparação:**
  - Comparação textual exata linha a linha após normalização de `\r\n` $\rightarrow$ `\n`.
  - Tolerância numérica para saídas reais em ponto flutuante (`double`): `0.01` (embora as soluções em `double` atinjam exatidão até a última casa impressa).
  - Saídas estritamente em ASCII puro com `\n` final.
- **Status de execução e fronteiras:**
  - Ausência total de vetores/arrays (`v[i]`), strings (`char[]`), funções próprias além de `int main(void)` e alocação dinâmica.
  - Cobertura de casos normais, bordas de tolerância ($\varepsilon = 1.0$, $\varepsilon > 1.0$, $\varepsilon \le 0$), bordas $n \le 0$ e $n = 1$, além de casos extremos sem *overflow* de fatorial/denominador.

---

## Casos de Teste por Programa

### 1. `C08_E02_corrigido.c` (Série $\sum_{k=1}^{n} \frac{1}{k!}$ sem Divisão Inteira)
- **Entradas:** `int n`.
- **Saídas esperadas:** `Soma = %.6f\n`.
- **Casos:**
  - `5` (caso normal do enunciado) $\rightarrow$ `Soma = 1.716667`
  - `1` (borda inferior de 1 termo) $\rightarrow$ `Soma = 1.000000`
  - `0` (borda nula: 0 iterações) $\rightarrow$ `Soma = 0.000000`
  - `15` (extremo: $15! > 2^{31}-1$, testa ausência de *overflow* com `double`) $\rightarrow$ `Soma = 1.718282`

---

### 2. `C08_E03_corrigido.c` (Série $\sum_{k=1}^{\infty} \frac{1}{k^2}$ por Tolerância sem Somar Violador)
- **Entradas:** `double eps`.
- **Saídas esperadas:** `Soma = %.6f\n`.
- **Casos:**
  - `0.1` (normal: soma $1 + 0.25 + 1/9$) $\rightarrow$ `Soma = 1.361111`
  - `1.0` (borda exata: apenas $k=1$) $\rightarrow$ `Soma = 1.000000`
  - `1.5` (borda violadora inicial: 0 termos) $\rightarrow$ `Soma = 0.000000`
  - `0.05` (normal estendido: 4 termos, até $k=4$) $\rightarrow$ `Soma = 1.423611`

---

### 3. `C08_E04.c` (Série Exponencial $e^x$ Incremental $O(n)$)
- **Entradas:** `double x`, `int n`.
- **Saídas esperadas:** `e^x aprox: %.6f\n`.
- **Casos:**
  - `1.0 10` (normal: $e^1$ com 10 termos) $\rightarrow$ `e^x aprox: 2.718282`
  - `0.0 5` (borda: $e^0 = 1$) $\rightarrow$ `e^x aprox: 1.000000`
  - `2.0 1` (borda: apenas 1 termo $k=0$) $\rightarrow$ `e^x aprox: 1.000000`
  - `-1.0 12` (extremo negativo: $e^{-1}$) $\rightarrow$ `e^x aprox: 0.367879`

---

### 4. `C08_E05.c` (Somatório $S = \sum_{k=0}^{n-1} \frac{2^k}{(n-k)^2}$ — UFPR 2017)
- **Entradas:** `int n`.
- **Saídas esperadas:** `S = %.6f\n` ou `Entrada Invalida\n`.
- **Casos:**
  - `3` (normal do enunciado) $\rightarrow$ `S = 4.611111`
  - `1` (borda unitária: $2^0 / 1^2$) $\rightarrow$ `S = 1.000000`
  - `0` (borda inválida) $\rightarrow$ `Entrada Invalida`
  - `-2` (borda negativa inválida) $\rightarrow$ `Entrada Invalida`
  - `10` (extremo maior) $\rightarrow$ `S = 596.207123`

---

### 5. `C08_E06.c` (Série de Euler $e$ por Tolerância com Contagem)
- **Entradas:** `double eps`.
- **Saídas esperadas:** `Soma = %.8f\nTermos = %d\n` ou `Tolerancia Invalida\n`.
- **Casos:**
  - `0.001` (normal: 7 termos, $k=0..6$) $\rightarrow$ `Soma = 2.71805556\nTermos = 7`
  - `1.0` (borda exata: 2 termos, $k=0,1$) $\rightarrow$ `Soma = 2.00000000\nTermos = 2`
  - `1.5` (borda $\varepsilon > 1$: 0 termos) $\rightarrow$ `Soma = 0.00000000\nTermos = 0`
  - `0.0` (borda inválida) $\rightarrow$ `Tolerancia Invalida`
  - `-0.1` (borda negativa inválida) $\rightarrow$ `Tolerancia Invalida`
  - `1e-8` (extremo de alta precisão: 12 termos) $\rightarrow$ `Soma = 2.71828183\nTermos = 12`

---

### 6. `C08_C02.c` (Série Alternada de $\ln(1+x)$)
- **Entradas:** `double x`, `int n`.
- **Saídas esperadas:** `ln(1+x) aprox: %.6f\n`.
- **Casos:**
  - `0.5 5` (normal do enunciado) $\rightarrow$ `ln(1+x) aprox: 0.407292`
  - `0.0 4` (borda nula: $\ln(1) = 0$) $\rightarrow$ `ln(1+x) aprox: 0.000000`
  - `1.0 1` (borda unitária de 1 termo) $\rightarrow$ `ln(1+x) aprox: 1.000000`
  - `-0.5 6` (normal negativo) $\rightarrow$ `ln(1+x) aprox: -0.691146`
  - `1.0 100` (extremo de 100 termos) $\rightarrow$ `ln(1+x) aprox: 0.688172`

---

### 7. `C08_C03.c` (Série $\sum_{k=1}^{\infty} \frac{1}{k^2}$ por Tolerância com Contagem)
- **Entradas:** `double eps`.
- **Saídas esperadas:** `Soma = %.6f\nTermos = %d\n`.
- **Casos:**
  - `0.1` (normal do enunciado) $\rightarrow$ `Soma = 1.361111\nTermos = 3`
  - `1.5` (borda $\varepsilon > 1$: nenhum termo somado) $\rightarrow$ `Soma = 0.000000\nTermos = 0`
  - `1.0` (borda exata: 1 termo) $\rightarrow$ `Soma = 1.000000\nTermos = 1`
  - `0.01` (extremo de 10 termos) $\rightarrow$ `Soma = 1.549768\nTermos = 10`
