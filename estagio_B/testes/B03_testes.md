# Especificação de Testes — Bloco `B03`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99** (`[DOC]` `Aula_00` p. 3; `Aula_10` p. 18).
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Critério de comparação e tolerância numérica:**
  - Comparação textual exata linha a linha após normalização de `\r\n` → `\n`.
  - Tolerância de `1e-2` (`0.01`) para saídas com `%.2f`.
- **Status de execução no ambiente atual (`19/11/2026`):**
  - **Executado:** verificação estática C99 + checagem de não-antecipação (ausência de `else`, `else if`, `switch`, `&&`, `||`, `!`, `while`, `for`, `char[]`) + **oráculo lógico/matemático em Python** sobre todos os **24 casos** de [casos_B03.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/casos_B03.json).
  - **Pendente:** compilação e execução binária em GCC (`gcc` não instalado no Windows nem no WSL2 Ubuntu desta máquina).

---

## Casos de Teste por Programa (`B03_E03_corrigido.c`, `B03_E04.c`, `B03_E05.c`, `B03_C02_corrigido.c`, `B03_C03.c`)

### 1. `B03_E03_corrigido.c` (ifs simples independentes)
- **Entradas:** `int x`.
- **Saídas:** Mensagens condicionais e `Fim\n`.
- **Casos:**
  - `-5` (negativo: nenhum if executa) → `Fim\n`
  - `0` (zero: fronteira estrita `x > 0` não executa) → `Fim\n`
  - `7` (positivo diferente de 10) → `Positivo\nFim\n`
  - `10` (fronteira exata de ambos os ifs) → `Positivo\nNumero igual a 10\nFim\n`
  - `15` (positivo maior que 10) → `Positivo\nFim\n`

### 2. `B03_E04.c` (Verificação de paridade com `if` simples)
- **Entradas:** `int n`.
- **Saídas:** Se par, `O numero %d eh par\n`; sempre finaliza com `Fim do programa\n`.
- **Casos:**
  - `4` (par positivo) → `O numero 4 eh par\nFim do programa\n`
  - `7` (ímpar positivo) → `Fim do programa\n`
  - `0` (zero: par) → `O numero 0 eh par\nFim do programa\n`
  - `11` (ímpar) → `Fim do programa\n`
  - `100` (par grande) → `O numero 100 eh par\nFim do programa\n`

### 3. `B03_E05.c` (Radar de velocidade com multa acima de 80 km/h)
- **Entradas:** `double vel`.
- **Saídas:** Se `vel > 80.0`, imprime `Multa: R$ %.2f\n`; sempre finaliza com `Boa viagem\n`.
- **Casos:**
  - `60.0` (abaixo do limite) → `Boa viagem\n`
  - `80.0` (fronteira exata: limite permitido, não multa) → `Boa viagem\n`
  - `80.1` (borda imediatamente acima da fronteira) → `Multa: R$ 0.50\nBoa viagem\n`
  - `90.0` (excedente de 10 km/h: 10 * 5 = 50.00) → `Multa: R$ 50.00\nBoa viagem\n`
  - `110.0` (excedente de 30 km/h: 30 * 5 = 150.00) → `Multa: R$ 150.00\nBoa viagem\n`

### 4. `B03_C02_corrigido.c` (Correção de `;` após `if` e `=` vs `==`)
- **Entradas:** `int n`.
- **Saídas:** Mensagens condicionais e `Fim\n`.
- **Casos:**
  - `-10` (negativo) → `Fim\n`
  - `0` (zero) → `Fim\n`
  - `50` (positivo != 100) → `Positivo\nFim\n`
  - `100` (positivo e igual a 100) → `Positivo\nCem\nFim\n`

### 5. `B03_C03.c` (Desconto simples se valor >= 100.0)
- **Entradas:** `double valor`.
- **Saídas:** `Valor final: R$ %.2f\n`.
- **Casos:**
  - `50.00` (sem desconto) → `Valor final: R$ 50.00\n`
  - `99.99` (fronteira inferior: sem desconto) → `Valor final: R$ 99.99\n`
  - `100.00` (fronteira exata: 10% de desconto) → `Valor final: R$ 90.00\n`
  - `150.00` (com desconto: 150 - 15 = 135) → `Valor final: R$ 135.00\n`
  - `200.00` (com desconto: 200 - 20 = 180) → `Valor final: R$ 180.00\n`
