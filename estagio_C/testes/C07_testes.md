# Especificação de Testes — Bloco `C07`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99** (`gcc -std=c99 -Wall -Wextra`).
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Critério de comparação:**
  - Comparação textual exata linha a linha após normalização de `\r\n` $\rightarrow$ `\n`.
  - Saídas formatadas com quebra de linha final `\n`.
  - Tolerância numérica para médias reais: `0.01`.
- **Status de execução e fronteiras:**
  - Ausência total de vetores/arrays (`v[i]`), strings (`char[]`), funções próprias adicionais e ponteiros.
  - Testes cobrindo exaustivamente casos normais, bordas críticas de sentinela e bordas de primalidade ($n \le 1$, $n = 2$, pares e ímpares).

---

## Casos de Teste por Programa

### 1. `C07_E02_corrigido.c` (Contagem Regressiva Pulando o 3 sem Laço Infinito)
- **Entradas:** `int n`.
- **Saídas esperadas:** Números em contagem regressiva separados por espaço, com `\n` final.
- **Casos:**
  - `5` (caso normal atravessando o 3) $\rightarrow$ `5 4 2 1 `
  - `3` (início exatamente no valor de salto) $\rightarrow$ `2 1 `
  - `1` (fronteira inferior sem alcançar o 3) $\rightarrow$ `1 `
  - `0` (borda nula) $\rightarrow$ linha vazia

---

### 2. `C07_E03.c` (Média de Notas com Saída Antecipada `while (1)`)
- **Entradas:** Sequência de notas inteiras terminada por valor negativo.
- **Saídas esperadas:** `Qtd: %d\nMedia: %.2f\n` ou `Nenhuma nota valida\n`.
- **Casos:**
  - `80 90 70 -1` (caso normal com 3 notas) $\rightarrow$ `Qtd: 3\nMedia: 80.00`
  - `-1` (parada imediata sem notas) $\rightarrow$ `Nenhuma nota valida`
  - `100 100 -5` (duas notas máximas) $\rightarrow$ `Qtd: 2\nMedia: 100.00`
  - `55 -2` (única nota válida) $\rightarrow$ `Qtd: 1\nMedia: 55.00`

---

### 3. `C07_E04.c` (Detector de Primalidade com Bordas)
- **Entradas:** `long long n`.
- **Saídas esperadas:** `Primo\n` ou `Nao Primo\n`.
- **Casos:**
  - `1` (fronteira crítica: 1 não é primo) $\rightarrow$ `Nao Primo`
  - `2` (único primo par) $\rightarrow$ `Primo`
  - `4` (menor número par composto) $\rightarrow$ `Nao Primo`
  - `13` (primo clássico) $\rightarrow$ `Primo`
  - `0` (borda zero) $\rightarrow$ `Nao Primo`
  - `-7` (número negativo) $\rightarrow$ `Nao Primo`
  - `29` (primo maior) $\rightarrow$ `Primo`

---

### 4. `C07_E05.c` (Contagem de Primos até Sentinela 0)
- **Entradas:** Sequência de inteiros positivos terminada por 0.
- **Saídas esperadas:** `Total Primos: %d\n`.
- **Casos:**
  - `7 10 13 1 4 17 0` (3 primos: 7, 13, 17) $\rightarrow$ `Total Primos: 3`
  - `0` (parada imediata) $\rightarrow$ `Total Primos: 0`
  - `2 3 5 0` (todos primos) $\rightarrow$ `Total Primos: 3`
  - `4 6 8 9 0` (nenhum primo) $\rightarrow$ `Total Primos: 0`

---

### 5. `C07_C02_corrigido.c` (Menu Interativo e `break` em `switch`)
- **Entradas:** Sequência de opções inteiras terminada por 0.
- **Saídas esperadas:** Linhas correspondentes a cada opção, seguidas de `Saindo\nFim do Programa\n`.
- **Casos:**
  - `1 0` $\rightarrow$ `Opcao 1 Executada\nSaindo\nFim do Programa`
  - `0` $\rightarrow$ `Saindo\nFim do Programa`
  - `3 1 0` $\rightarrow$ `Opcao Invalida\nOpcao 1 Executada\nSaindo\nFim do Programa`

---

### 6. `C07_C03.c` (Classificador em Lote e Resumo de Primalidade)
- **Entradas:** `int k` seguido de `k` números inteiros.
- **Saídas esperadas:** Para cada número: `Numero %lld: Primo\n` ou `Numero %lld: Nao Primo\n`. Linha final: `Resumo: %d primos de %d numeros\n`.
- **Casos:**
  - `4` com `1 2 4 13` $\rightarrow$ `Resumo: 2 primos de 4 numeros`
  - `1` com `7` $\rightarrow$ `Resumo: 1 primos de 1 numeros`
  - `2` com `0 -5` $\rightarrow$ `Resumo: 0 primos de 2 numeros`
