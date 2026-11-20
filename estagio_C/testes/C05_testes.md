# Especificação de Testes — Bloco `C05`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99** (`[DOC]` `Aula_00` p. 3; `Aula_10` p. 18).
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Critério de comparação e tolerância numérica:**
  - Comparação textual exata linha a linha após normalização de `\r\n` $\rightarrow$ `\n`.
  - Saídas inteiras devem ter coincidência exata; saídas reais (`%.2f`) tolerância numérica `0.01`.
  - Saídas `printf` estritamente em ASCII puro (sem acentos).
- **Checagem estática de não-antecipação:**
  - Proibido o uso de `break` ou `continue` em laços.
  - Proibido o uso de vetores (`char[]`, `int[]`, `v[i]`) ou funções customizadas além de `int main(void)`.
- **Casos de teste registrados:** 31 casos em [casos_C05.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/casos_C05.json).

---

## Casos de Teste por Programa

### 1. `C05_E02_corrigido.c` (Primeiros `n` Múltiplos Positivos de 3)
- **Entrada:** `int n`.
- **Saída:** `n` linhas com `3 * i\n` para `i = 1..n`.
- **Casos:**
  - `C05-E02-T1` (borda `n = 0`): `0` $\rightarrow$ *(saída vazia)*.
  - `C05-E02-T2` (borda `n < 0`): `-3` $\rightarrow$ *(saída vazia)*.
  - `C05-E02-T3` (borda unitário): `1` $\rightarrow$ `3\n`.
  - `C05-E02-T4` (normal): `4` $\rightarrow$ `3\n6\n9\n12\n`.
  - `C05-E02-T5` (normal): `6` $\rightarrow$ `3\n6\n9\n12\n15\n18\n`.

### 2. `C05_E03.c` (Fatorial Iterativo com `for`)
- **Entrada:** `int n` ($n \ge 0$).
- **Saída:** `%d! = %lld\n`.
- **Casos:**
  - `C05-E03-T1` (borda `0!`): `0` $\rightarrow$ `0! = 1\n`.
  - `C05-E03-T2` (borda `1!`): `1` $\rightarrow$ `1! = 1\n`.
  - `C05-E03-T3` (normal): `5` $\rightarrow$ `5! = 120\n`.
  - `C05-E03-T4` (normal): `7` $\rightarrow$ `7! = 5040\n`.
  - `C05-E03-T5` (normal): `12` $\rightarrow$ `12! = 479001600\n`.
  - `C05-E03-T6` (extremo `long long`): `15` $\rightarrow$ `15! = 1307674368000\n`.

### 3. `C05_E04.c` (Contagem Regressiva com Passo Variável)
- **Entrada:** `int inicio, passo` (`passo > 0`).
- **Saída:** Valores `>= 1` um por linha e `Contagem: %d\n`.
- **Casos:**
  - `C05-E04-T1` (borda 0 iterações): `0 2` $\rightarrow$ `Contagem: 0\n`.
  - `C05-E04-T2` (borda unitário): `1 5` $\rightarrow$ `1\nContagem: 1\n`.
  - `C05-E04-T3` (normal): `10 3` $\rightarrow$ `10\n7\n4\n1\nContagem: 4\n`.
  - `C05-E04-T4` (normal parada antes de `0`): `12 5` $\rightarrow$ `12\n7\n2\nContagem: 3\n`.
  - `C05-E04-T5` (normal passo `1`): `5 1` $\rightarrow$ `5\n4\n3\n2\n1\nContagem: 5\n`.

### 4. `C05_E05.c` (Múltiplos de 3 e Não-Múltiplos de 5 em `1..n`)
- **Entrada:** `int n`.
- **Saída:** Valores filtrados um por linha, seguidos de `Quantidade: %d\nSoma: %d\n`.
- **Casos:**
  - `C05-E05-T1` (borda nenhum valor): `2` $\rightarrow$ `Quantidade: 0\nSoma: 0\n`.
  - `C05-E05-T2` (borda unitário): `3` $\rightarrow$ `3\nQuantidade: 1\nSoma: 3\n`.
  - `C05-E05-T3` (borda exclui `15`): `15` $\rightarrow$ `3\n6\n9\n12\nQuantidade: 4\nSoma: 30\n`.
  - `C05-E05-T4` (normal): `20` $\rightarrow$ `3\n6\n9\n12\n18\nQuantidade: 5\nSoma: 48\n`.
  - `C05-E05-T5` (extremo exclui `15` e `30`): `30` $\rightarrow$ `3\n6\n9\n12\n18\n21\n24\n27\nQuantidade: 8\nSoma: 120\n`.

### 5. `C05_C02_corrigido.c` (Soma de Pares e Valor Pós-Laço de `i`)
- **Entrada:** `int a, b`.
- **Saída:** `Soma pares: %d\nProximo i: %d\n`.
- **Casos:**
  - `C05-C02-T1` (borda intervalo vazio `a > b`): `6 4` $\rightarrow$ `Soma pares: 0\nProximo i: 6\n`.
  - `C05-C02-T2` (borda unitário par): `4 4` $\rightarrow$ `Soma pares: 4\nProximo i: 5\n`.
  - `C05-C02-T3` (borda unitário ímpar): `3 3` $\rightarrow$ `Soma pares: 0\nProximo i: 4\n`.
  - `C05-C02-T4` (normal): `1 6` $\rightarrow$ `Soma pares: 12\nProximo i: 7\n`.
  - `C05-C02-T5` (normal com negativos): `-4 2` $\rightarrow$ `Soma pares: -4\nProximo i: 3\n`.

### 6. `C05_C03.c` (Estatísticas com `for` e Filtros Lógicos)
- **Entrada:** `int n`.
- **Saída:** `Qtd par ou mult7: %d\nSoma impares > 5: %d\nMedia total: %.2f\n` ou `Entrada invalida\n`.
- **Casos:**
  - `C05-C03-T1` (borda zero): `0` $\rightarrow$ `Entrada invalida\n`.
  - `C05-C03-T2` (borda negativo): `-5` $\rightarrow$ `Entrada invalida\n`.
  - `C05-C03-T3` (borda unitário): `1` $\rightarrow$ `Qtd par ou mult7: 0\nSoma impares > 5: 0\nMedia total: 1.00\n`.
  - `C05-C03-T4` (normal): `10` $\rightarrow$ `Qtd par ou mult7: 6\nSoma impares > 5: 16\nMedia total: 5.50\n`.
  - `C05-C03-T5` (normal interseção `14` par e mult7): `14` $\rightarrow$ `Qtd par ou mult7: 8\nSoma impares > 5: 40\nMedia total: 7.50\n`.
