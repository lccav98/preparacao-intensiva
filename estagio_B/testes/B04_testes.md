# Especificação de Testes — Bloco `B04`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99** (`[DOC]` `Aula_00` p. 3; `Aula_10` p. 18).
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Critério de comparação e tolerância numérica:**
  - Comparação textual exata linha a linha após normalização de `\r\n` → `\n`.
  - Tolerância de `1e-2` (`0.01`) para saídas em ponto flutuante `%.2f` e `%.1f`.
- **Status de execução no ambiente atual (`19/11/2026`):**
  - **Executado:** verificação estática C99 + checagem de não-antecipação (ausência de `else if`, `switch`, `&&`, `||`, `!`, `while`, `for`, `char[]`) + **oráculo lógico/matemático em Python** sobre todos os **32 casos** de [casos_B04.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/casos_B04.json).
  - **Pendente:** compilação e execução binária em GCC (`gcc` não instalado no Windows nem no WSL2 Ubuntu desta máquina).

---

## Casos de Teste por Programa (`B04_E02.c`, `B04_E03_corrigido.c`, `B04_E04.c`, `B04_E05.c`, `B04_C02.c`, `B04_C03.c`)

### 1. `B04_E02.c` (Par ou Ímpar com `if / else`)
- **Entradas:** `int n`.
- **Saídas:** `%d eh par\n` ou `%d eh impar\n`.
- **Casos:**
  - `0` (zero: par) → `0 eh par`
  - `4` (par positivo) → `4 eh par`
  - `7` (ímpar positivo) → `7 eh impar`
  - `-3` (ímpar negativo: -3 % 2 = -1 != 0, cai no else) → `-3 eh impar`
  - `100` (par grande) → `100 eh par`

### 2. `B04_E03_corrigido.c` (Aprovação binária na fronteira 6.0)
- **Entradas:** `double nota`.
- **Saídas:** `Aprovado\n` ou `Reprovado\n`.
- **Casos:**
  - `8.5` (aprovado normal) → `Aprovado`
  - `6.0` (fronteira exata: aprovado; elimina o bug de saída dupla) → `Aprovado`
  - `5.9` (borda imediatamente inferior: reprovado) → `Reprovado`
  - `0.0` (nota mínima: reprovado) → `Reprovado`
  - `10.0` (nota máxima: aprovado) → `Aprovado`

### 3. `B04_E04.c` (Múltiplos divisores com `if`s independentes e flag)
- **Entradas:** `int n`.
- **Saídas:** Linhas indicando cada divisor encontrado (`2`, `3`, `5`) ou `Nenhum divisor encontrado\n`.
- **Casos:**
  - `30` (divisível por 2, 3 e 5 simultaneamente) → 3 linhas
  - `6` (divisível por 2 e 3) → 2 linhas
  - `10` (divisível por 2 e 5) → 2 linhas
  - `15` (divisível por 3 e 5) → 2 linhas
  - `7` (primo: nenhum dos três) → `Nenhum divisor encontrado`
  - `25` (apenas por 5) → `Divisivel por 5`

### 4. `B04_E05.c` (Crédito especial: 30% se saldo > 1000.0, senão 15%)
- **Entradas:** `double saldo_medio`.
- **Saídas:** `Saldo medio: R$ %.2f\nCredito especial: R$ %.2f\n`.
- **Casos:**
  - `500.00` (15% de 500 = 75.00) → `Saldo medio: R$ 500.00` / `Credito especial: R$ 75.00`
  - `1000.00` (fronteira inclusiva `<= 1000`: 15% de 1000 = 150.00) → `Saldo medio: R$ 1000.00` / `Credito especial: R$ 150.00`
  - `1000.01` (borda estrita `> 1000`: 30% de 1000.01 = 300.00) → `Saldo medio: R$ 1000.01` / `Credito especial: R$ 300.00`
  - `2000.00` (30% de 2000 = 600.00) → `Saldo medio: R$ 2000.00` / `Credito especial: R$ 600.00`
  - `0.00` (saldo zero) → `Saldo medio: R$ 0.00` / `Credito especial: R$ 0.00`

### 5. `B04_C02.c` (Termômetro febril na fronteira 37.8 C)
- **Entradas:** `double temp`.
- **Saídas:** `Temperatura normal: %.1f C\n` ou `Estado febril: %.1f C\n`.
- **Casos:**
  - `36.5` (normal) → `Temperatura normal: 36.5 C`
  - `37.7` (borda inferior) → `Temperatura normal: 37.7 C`
  - `37.8` (fronteira exata febril) → `Estado febril: 37.8 C`
  - `38.5` (febre moderada) → `Estado febril: 38.5 C`
  - `39.0` (febre alta) → `Estado febril: 39.0 C`

### 6. `B04_C03.c` (Privilégios de acesso múltiplos e caso nenhum)
- **Entradas:** `int codigo`.
- **Saídas:** Permissões disparadas ou `Sem permissoes especiais\n`.
- **Casos:**
  - `2` (apenas leitura) → `Permissao de Leitura`
  - `3` (apenas escrita) → `Permissao de Escrita`
  - `5` (apenas execução) → `Permissao de Execucao`
  - `6` (leitura e escrita: múltiplo de 2 e 3) → 2 linhas
  - `30` (todas as permissões: múltiplo de 2, 3 e 5) → 3 linhas
  - `7` (nenhuma permissão) → `Sem permissoes especiais`
