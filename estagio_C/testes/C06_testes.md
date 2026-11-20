# Especificação de Testes — Bloco `C06`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99** (`gcc -std=c99 -Wall -Wextra`).
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Critério de comparação:**
  - Comparação textual exata linha a linha após normalização de quebras de linha (`\r\n` $\rightarrow$ `\n`).
  - Saídas formatadas com quebra de linha final `\n`.
  - Ausência total de caracteres acentuados nas mensagens de `printf`.
- **Status de execução e fronteiras:**
  - Verificação de não-antecipação: ausência estrita de vetores/strings (`char[]`, `int[]`, `v[i]`), funções além de `main`, structs e ponteiros.
  - Todas as soluções compiláveis em C99 sem advertências (*warnings*).

---

## Casos de Teste por Programa (`C06-E04`, `C06-E05`, `C06-C03`)

### 1. `C06_E04_corrigido.c` (Soma de Ímpares até `n` sem Laço Infinito)
- **Entradas:** `int n`.
- **Saídas esperadas:** `Soma = %d\n`.
- **Casos:**
  - `5` (ímpar: soma 1 + 3 + 5) $\rightarrow$ `Soma = 9`
  - `6` (par: clássico bug que travava com `i != n`, soma 1 + 3 + 5) $\rightarrow$ `Soma = 9`
  - `1` (fronteira exata inferior de ímpar positivo) $\rightarrow$ `Soma = 1`
  - `2` (fronteira par inferior) $\rightarrow$ `Soma = 1`
  - `10` (par maior: 1 + 3 + 5 + 7 + 9) $\rightarrow$ `Soma = 25`
  - `0` (borda não positiva: 0 iterações) $\rightarrow$ `Soma = 0`

---

### 2. `C06_E05.c` (Sequência de Collatz / $3n+1$)
- **Entradas:** `long long n`.
- **Saídas esperadas:** Linha 1 com os termos separados por espaço; Linha 2 com `Passos: %d\n` (ou `Entrada Invalida\n`).
- **Casos:**
  - `6` (caso normal demonstrativo) $\rightarrow$ `6 3 10 5 16 8 4 2 1\nPassos: 8`
  - `1` (fronteira imediata de parada: 0 passos) $\rightarrow$ `1\nPassos: 0`
  - `2` (par elementar: 1 passo) $\rightarrow$ `2 1\nPassos: 1`
  - `3` (ímpar inicial: 7 passos) $\rightarrow$ `3 10 5 16 8 4 2 1\nPassos: 7`
  - `0` (borda inválida) $\rightarrow$ `Entrada Invalida`
  - `-5` (borda negativa) $\rightarrow$ `Entrada Invalida`

---

### 3. `C06_C03.c` (Redução Numérica, Soma e Contagem de Dígitos)
- **Entradas:** `long long n`.
- **Saídas esperadas:** `Soma = %d\nDigitos = %d\n` (ou `Valor Invalido\n`).
- **Casos:**
  - `4096` (caso normal multicomponente) $\rightarrow$ `Soma = 19\nDigitos = 4`
  - `7` (fronteira de 1 único dígito) $\rightarrow$ `Soma = 7\nDigitos = 1`
  - `1000` (número com múltiplos zeros internos) $\rightarrow$ `Soma = 1\nDigitos = 4`
  - `123456789` (grande número com todos os dígitos) $\rightarrow$ `Soma = 45\nDigitos = 9`
  - `0` (borda inválida) $\rightarrow$ `Valor Invalido`
  - `-10` (borda negativa) $\rightarrow$ `Valor Invalido`
