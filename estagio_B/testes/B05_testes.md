# Especificação de Testes — Bloco `B05`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99** (`[DOC]` `Aula_00` p. 3; `Aula_10` p. 18).
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Critério de comparação e tolerância numérica:**
  - Comparação textual exata linha a linha após normalização de `\r\n` → `\n`.
  - Para os valores monetários formatados com `%.2f`, tolerância numérica de **`1e-2`** (`0.01`) na validação por oráculo caso haja variação de arredondamento binário de última casa; nos casos de teste abaixo, todos os valores decimais exatos foram escolhidos para evitar ambiguidade de ponto médio binário.
- **Status de execução no ambiente atual (`19/11/2026`):**
  - **Executado:** verificação estática C99 + checagem de não-antecipação (ausência de `&&`, `||`, `!`, `switch`, `while`, `for`) + **oráculo matemático em Python** sobre todos os **34 casos** de [casos_B05.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/casos_B05.json).
  - **Pendente:** compilação e execução binária em GCC (`gcc` não instalado no Windows nem no WSL2 Ubuntu desta máquina).

---

## Casos de Teste por Programa (`B05-E03` a `B05-E06`, `B05-C02`, `B05-C03`)

### 1. `B05_E03_corrigido.c` (Desconto em livraria)
- **Entradas:** `double compra` (`>= 0`).
- **Saídas:** `Desconto: R$ %.2f\nTotal: R$ %.2f\n`.
- **Casos (normais e bordas):**
  - `50.00` (normal faixa 1) → `Desconto: R$ 0.00` / `Total: R$ 50.00`
  - `99.99` (borda inferior à fronteira `100.0`) → `Desconto: R$ 0.00` / `Total: R$ 99.99`
  - `100.00` (fronteira exata 5%) → `Desconto: R$ 5.00` / `Total: R$ 95.00`
  - `199.995` (borda crítica da lacuna `<= 199.99`, permanece 5%) → `Desconto: R$ 10.00` / `Total: R$ 190.00`
  - `200.00` (fronteira exata 10%) → `Desconto: R$ 20.00` / `Total: R$ 180.00`
  - `300.00` (fronteira exata 15%) → `Desconto: R$ 45.00` / `Total: R$ 255.00`
  - `400.00` (normal faixa 4) → `Desconto: R$ 60.00` / `Total: R$ 340.00`

### 2. `B05_E04.c` (Consumo de energia elétrica)
- **Casos:**
  - `0.0` (borda zero) → `Total: R$ 0.00`
  - `80.0` (normal faixa 1) → `Total: R$ 40.00`
  - `100.0` (fronteira exata 100) → `Total: R$ 50.00`
  - `200.0` (normal faixa 2) → `Total: R$ 130.00`
  - `250.0` (fronteira exata 250) → `Total: R$ 162.50`
  - `300.0` (normal faixa 3) → `Total: R$ 240.00`

### 3. `B05_E05.c` (Taxa de bagagem)
- **Casos:**
  - `0.0` (borda zero) → `Taxa: R$ 0.00`
  - `10.0` (fronteira exata 10) → `Taxa: R$ 0.00`
  - `20.0` (fronteira exata 20) → `Taxa: R$ 40.00`
  - `30.0` (fronteira exata 30) → `Taxa: R$ 75.00`
  - `34.0` (normal faixa excedente) → `Taxa: R$ 109.00`

### 4. `B05_E06.c` (Taxa de entrega por distância)
- **Casos:**
  - `5.0` (fronteira exata 5) → `Taxa: R$ 10.00`
  - `15.0` (fronteira exata 15) → `Taxa: R$ 18.00`
  - `30.0` (fronteira exata 30) → `Taxa: R$ 28.00`
  - `34.0` (normal faixa excedente) → `Taxa: R$ 37.00`
  - `0.5` (borda mínima positiva) → `Taxa: R$ 10.00`

### 5. `B05_C02_corrigido.c` (Planos de internet)
- **Casos:**
  - `15.0` (faixa 1) → `Plano: R$ 79.90`
  - `20.0` (fronteira exata 20) → `Plano: R$ 79.90`
  - `50.0` (caso que falhava no código bugado!) → `Plano: R$ 109.90`
  - `100.0` (fronteira exata 100) → `Plano: R$ 109.90`
  - `300.0` (fronteira exata 300) → `Plano: R$ 149.90`
  - `500.0` (faixa 4) → `Plano: R$ 199.90`

### 6. `B05_C03.c` (Estacionamento)
- **Casos:**
  - `0.5` (borda < 1h) → `Total: R$ 8.00`
  - `1.0` (fronteira exata 1) → `Total: R$ 8.00`
  - `3.0` (fronteira exata 3) → `Total: R$ 15.00`
  - `6.0` (fronteira exata 6) → `Total: R$ 24.00`
  - `8.5` (normal excedente) → `Total: R$ 35.25`
