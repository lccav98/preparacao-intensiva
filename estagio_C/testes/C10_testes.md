# Especificação de Testes — Bloco `C10`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99** (`gcc -std=c99 -Wall -Wextra`).
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Critério de comparação:**
  - Comparação textual exata linha a linha após normalização de `\r\n` $\rightarrow$ `\n`.
  - Tolerância numérica para saídas reais (`double`): `0.01`.
  - Saídas estritamente em ASCII puro com `\n` final.
- **Status de execução e fronteiras:**
  - Ausência total de vetores/arrays (`v[i]`), strings (`char[]`), funções próprias além de `int main(void)`, structs e ponteiros.
  - Cobertura integrada de todas as bordas do Estágio C: entrada vazia em sentinela, todos os valores negativos, múltiplos filtrados, $\varepsilon$ violado no primeiro termo, $n \le 1$ e $n = 2$ em primalidade, intervalos inválidos e formatação tabular `%4d`.

---

## Casos de Teste por Programa

### 1. `C10_E02_corrigido.c` (Sentinela `-1`, Filtro de Múltiplos de 5 e Máximo Seguro)
- **Entradas:** Sequência de inteiros terminada por `-1`.
- **Casos:**
  - `4 10 7 3 -1` (normal com múltiplo de 5 ignorado) $\rightarrow$ `Soma = 14\nMaior = 7`
  - `-10 -3 -5 -1` (borda crítica: apenas negativos, múltiplos ignorados) $\rightarrow$ `Soma = -3\nMaior = -3`
  - `-1` (borda vazia imediata) $\rightarrow$ `Nenhum valor valido`
  - `5 15 20 -1` (borda: todos os elementos antes da sentinela filtrados) $\rightarrow$ `Nenhum valor valido`

---

### 2. `C10_E03_corrigido.c` (Série Alternada $S = \sum_{k=0}^{n-1} \frac{(-1)^k}{(n-k)^2}$ sem Divisão Inteira/Zero)
- **Entradas:** `int n`.
- **Casos:**
  - `3` (normal: $1/9 - 1/4 + 1/1$) $\rightarrow$ `S = 0.861111`
  - `1` (borda unitária: $1/1$) $\rightarrow$ `S = 1.000000`
  - `0` (borda inválida) $\rightarrow$ `Entrada Invalida`
  - `10` (extremo) $\rightarrow$ `S = -0.817962`

---

### 3. `C10_E04.c` (Menu `do-while` + `switch`: Euclides e Primalidade)
- **Entradas:** Opções `1`, `2`, `0` e argumentos correspondentes.
- **Casos:**
  - `1 12 18 2 17 0` (normal: MDC com $a < b$ + primo + saída) $\rightarrow$ `MDC = 6\nPrimo\nEncerrando`
  - `0` (borda: saída imediata na 1ª execução do `do-while`) $\rightarrow$ `Encerrando`
  - `9 1 0 5 2 1 0` (borda: opção inválida, MDC inválido, primalidade de `1`) $\rightarrow$ `Opcao Invalida\nEntrada Invalida\nNao Primo\nEncerrando`
  - `1 1071 462 2 2 2 4 0` (extremo: Euclides maior + primo `2` + composto `4`) $\rightarrow$ `MDC = 21\nPrimo\nNao Primo\nEncerrando`

---

### 4. `C10_E05.c` (Sentinela `0` com Estatísticas e Contagem de Primos)
- **Entradas:** Sequência de inteiros (`long long`) terminada por `0`.
- **Casos:**
  - `7 4 13 1 2 0` (normal) $\rightarrow$ `Qtd: 5\nPrimos: 3\nMaior: 13\nMedia: 5.40`
  - `0` (borda vazia) $\rightarrow$ `Nenhum numero valido`
  - `-5 -2 1 0` (borda: negativos e `1`, 0 primos) $\rightarrow$ `Qtd: 3\nPrimos: 0\nMaior: 1\nMedia: -2.00`
  - `29 31 37 100 0` (extremo) $\rightarrow$ `Qtd: 4\nPrimos: 3\nMaior: 100\nMedia: 49.25`

---

### 5. `C10_E06.c` (Série Alternada de $\sin(x)$ por Tolerância $\varepsilon$)
- **Entradas:** `double x, eps`.
- **Casos:**
  - `1.0 0.001` (normal: 3 termos) $\rightarrow$ `sen(x) aprox: 0.841667\nTermos = 3`
  - `0.0 0.01` (borda: $\sin(0) = 0$, 0 termos) $\rightarrow$ `sen(x) aprox: 0.000000\nTermos = 0`
  - `0.5 1.0` (borda: $|x| < \varepsilon$, 0 termos somados) $\rightarrow$ `sen(x) aprox: 0.000000\nTermos = 0`
  - `1.0 0.0` (borda inválida) $\rightarrow$ `Entrada Invalida`
  - `-1.570796 1e-6` (extremo negativo: $\approx -\pi/2$) $\rightarrow$ `sen(x) aprox: -1.000000\nTermos = 6`

---

### 6. `C10_C02.c` (Contagem e Soma de Primos em Intervalo $[a, b]$)
- **Entradas:** `long long a, b`.
- **Casos:**
  - `1 10` (normal: primos 2, 3, 5, 7) $\rightarrow$ `Qtd Primos: 4\nSoma Primos: 17`
  - `-3 5` (borda: negativos, 0 e 1 ignorados; primos 2, 3, 5) $\rightarrow$ `Qtd Primos: 3\nSoma Primos: 10`
  - `10 5` (borda invertida inválida) $\rightarrow$ `Intervalo Invalido`
  - `7 7` (borda unitária prima) $\rightarrow$ `Qtd Primos: 1\nSoma Primos: 7`
  - `1 50` (extremo: 15 primos somando 328) $\rightarrow$ `Qtd Primos: 15\nSoma Primos: 328`

---

### 7. `C10_C03.c` (Tabela Triangular de Multiplicação `%4d`)
- **Entradas:** `int n`.
- **Casos:**
  - `4` (normal do enunciado) $\rightarrow$ 4 linhas triangulares
  - `1` (borda unitária) $\rightarrow$ `   1`
  - `0` (borda inválida) $\rightarrow$ `Entrada Invalida`
  - `6` (extremo até `36`) $\rightarrow$ 6 linhas triangulares
