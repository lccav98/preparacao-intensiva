# Especificação de Testes — Bloco `B01`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99** (`[DOC]` `Aula_00` p. 3; `Aula_10` p. 18).
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Critério de comparação e tolerância numérica:**
  - Comparação textual exata linha a linha após normalização de `\r\n` → `\n`.
  - Para saídas monetárias com `%.2f` (`B01_C02_corrigido.c`), tolerância de `1e-2` (`0.01`).
- **Status de execução no ambiente atual (`19/11/2026`):**
  - **Executado:** verificação estática C99 + checagem de não-antecipação (ausência de `&&`, `||`, `!`, `switch`, `while`, `for`, `char[]`) + **oráculo matemático em Python** sobre todos os **35 casos** de [casos_B01.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/casos_B01.json).
  - **Pendente:** compilação e execução binária em GCC (`gcc` não instalado no Windows nem no WSL2 Ubuntu desta máquina).

---

## Casos de Teste por Programa (`B01_E02.c`, `B01_E03.c`, `B01_E04.c`, `B01_E05.c`, `B01_C02_corrigido.c`, `B01_C03.c`)

### 1. `B01_E02.c` (Decomposição em notas de 20 e moedas de 1)
- **Entradas:** `int valor` (`>= 0`).
- **Saídas:** `Notas de 20: %d\nMoedas de 1: %d\n`.
- **Casos (normais e bordas):**
  - `0` (borda zero) → `Notas de 20: 0` / `Moedas de 1: 0`
  - `19` (borda imediatamente inferior a 20) → `Notas de 20: 0` / `Moedas de 1: 19`
  - `20` (fronteira exata de 1 nota) → `Notas de 20: 1` / `Moedas de 1: 0`
  - `25` (normal com resto positivo) → `Notas de 20: 1` / `Moedas de 1: 5`
  - `60` (múltiplo exato de 20) → `Notas de 20: 3` / `Moedas de 1: 0`
  - `97` (normal composto) → `Notas de 20: 4` / `Moedas de 1: 17`

### 2. `B01_E03.c` (Conversão de segundos em minutos e segundos)
- **Entradas:** `int total_seg` (`>= 0`).
- **Saídas:** `Minutos: %d\nSegundos: %d\n`.
- **Casos:**
  - `0` (borda zero) → `Minutos: 0` / `Segundos: 0`
  - `45` (menos de um minuto) → `Minutos: 0` / `Segundos: 45`
  - `60` (fronteira exata de 1 minuto) → `Minutos: 1` / `Segundos: 0`
  - `135` (normal: 2 min e 15 s) → `Minutos: 2` / `Segundos: 15`
  - `3600` (exatamente 1 hora em segundos) → `Minutos: 60` / `Segundos: 0`

### 3. `B01_E04.c` (Decomposição em horas, minutos e segundos formato compacto)
- **Entradas:** `int seg_totais` (`>= 0`).
- **Saídas:** `%d h %d m %d s\n`.
- **Casos:**
  - `0` (borda zero) → `0 h 0 m 0 s`
  - `59` (borda inferior a 1 minuto) → `0 h 0 m 59 s`
  - `60` (borda exata 1 minuto) → `0 h 1 m 0 s`
  - `3600` (borda exata 1 hora) → `1 h 0 m 0 s`
  - `3661` (1h 1m 1s) → `1 h 1 m 1 s`
  - `7322` (2h 2m 2s) → `2 h 2 m 2 s`

### 4. `B01_E05.c` (Decomposição horária independente)
- **Entradas:** `int tempo_seg` (`>= 0`).
- **Saídas:** `Horas: %d\nMinutos: %d\nSegundos: %d\n`.
- **Casos:**
  - `0` (borda zero) → `Horas: 0` / `Minutos: 0` / `Segundos: 0`
  - `45` (normal apenas segundos) → `Horas: 0` / `Minutos: 0` / `Segundos: 45`
  - `125` (normal minutos e segundos) → `Horas: 0` / `Minutos: 2` / `Segundos: 5`
  - `3600` (fronteira 1 hora) → `Horas: 1` / `Minutos: 0` / `Segundos: 0`
  - `4000` (normal 1h 6m 40s) → `Horas: 1` / `Minutos: 6` / `Segundos: 40`

### 5. `B01_C02_corrigido.c` (Correção de desconto percentual)
- **Entradas:** `int valor` (`>= 0`).
- **Saídas:** `Desconto: R$ %.2f\n`.
- **Casos:**
  - `0` (borda zero) → `Desconto: R$ 0.00`
  - `50` (normal) → `Desconto: R$ 5.00`
  - `100` (borda base 100) → `Desconto: R$ 10.00`
  - `250` (normal) → `Desconto: R$ 25.00`
  - `1000` (normal grande) → `Desconto: R$ 100.00`

### 6. `B01_C03.c` (Caixa eletrônico: 50, 20, 10 e 1)
- **Entradas:** `int quantia` (`>= 0`).
- **Saídas:** `Cedulas de 50: %d\nCedulas de 20: %d\nCedulas de 10: %d\nCedulas de 1: %d\n`.
- **Casos:**
  - `0` (borda zero) → `50: 0` / `20: 0` / `10: 0` / `1: 0`
  - `8` (apenas notas de 1) → `50: 0` / `20: 0` / `10: 0` / `1: 8`
  - `10` (fronteira exata de 10) → `50: 0` / `20: 0` / `10: 1` / `1: 0`
  - `37` (20 + 10 + 7) → `50: 0` / `20: 1` / `10: 1` / `1: 7`
  - `50` (fronteira exata de 50) → `50: 1` / `20: 0` / `10: 0` / `1: 0`
  - `88` (50 + 20 + 10 + 8) → `50: 1` / `20: 1` / `10: 1` / `1: 8`
  - `189` (3x50 + 20 + 10 + 9) → `50: 3` / `20: 1` / `10: 1` / `1: 9`
