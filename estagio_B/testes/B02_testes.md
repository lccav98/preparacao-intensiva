# Especificação de Testes — Bloco `B02`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99** (`[DOC]` `Aula_00` p. 3; `Aula_10` p. 18).
- **Comando de compilação padrão (com inclusão de `<math.h>` exigindo `-lm`):**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -lm -o programa
  ```
- **Critério de comparação e tolerância numérica:**
  - Comparação textual exata linha a linha após normalização de `\r\n` → `\n`.
  - Tolerância numérica de `1e-2` (`0.01`) para saídas em ponto flutuante `%.2f`.
- **Status de execução no ambiente atual (`19/11/2026`):**
  - **Executado:** verificação estática C99 + checagem de não-antecipação (ausência de `&&`, `||`, `!`, `switch`, `while`, `for`, `char[]`) + **oráculo matemático em Python** sobre todos os **27 casos** de [casos_B02.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/casos_B02.json).
  - **Pendente:** compilação e execução binária em GCC (`gcc` não instalado no Windows nem no WSL2 Ubuntu desta máquina).

---

## Casos de Teste por Programa (`B02_E02_corrigido.c`, `B02_E03.c`, `B02_E04.c`, `B02_E05.c`, `B02_C02_corrigido.c`, `B02_C03.c`)

### 1. `B02_E02_corrigido.c` (Raiz quadrática com precedência correta)
- **Entradas:** `double a, b, c` (com `a != 0` e `delta >= 0`).
- **Saídas:** `x1 = %.2f\n`.
- **Casos:**
  - `1.0 -5.0 6.0` (raízes inteiras 3 e 2) → `x1 = 3.00`
  - `1.0 -2.0 1.0` (raiz dupla: delta = 0) → `x1 = 1.00`
  - `2.0 -8.0 6.0` (`a = 2.0`, testa divisor `2.0 * a = 4.0`) → `x1 = 3.00`
  - `1.0 -7.0 12.0` (raízes 4 e 3) → `x1 = 4.00`

### 2. `B02_E03.c` (Cálculo completo de Bhaskara para delta >= 0)
- **Entradas:** `double a, b, c`.
- **Saídas:** `x1 = %.2f\nx2 = %.2f\n`.
- **Casos:**
  - `1.0 -5.0 6.0` → `x1 = 3.00` / `x2 = 2.00`
  - `1.0 -4.0 4.0` (delta zero) → `x1 = 2.00` / `x2 = 2.00`
  - `2.0 -10.0 8.0` → `x1 = 4.00` / `x2 = 1.00`
  - `1.0 0.0 -9.0` (b = 0) → `x1 = 3.00` / `x2 = -3.00`

### 3. `B02_E04.c` (Atribuições compostas e incremento)
- **Entradas:** `int saldo, bonus, taxa`.
- **Saídas:** `Saldo final: %d\n`.
- **Casos:**
  - `100 50 30` → `100 + 50 = 150` → `150 - 30 = 120` → `120 * 2 = 240` → `240 + 1 = 241`
  - `0 10 5` → `0 + 10 = 10` → `5` → `10` → `11`
  - `50 0 0` → `50` → `50` → `100` → `101`
  - `20 30 50` → `50` → `0` → `0` → `1`

### 4. `B02_E05.c` (Distância euclidiana entre dois pontos)
- **Entradas:** `double x1, y1, x2, y2`.
- **Saídas:** `Distancia: %.2f\n`.
- **Casos:**
  - `0.0 0.0 3.0 4.0` (triângulo 3-4-5) → `Distancia: 5.00`
  - `1.0 1.0 1.0 1.0` (pontos coincidentes: distância zero) → `Distancia: 0.00`
  - `0.0 0.0 0.0 5.0` (alinhado no eixo Y) → `Distancia: 5.00`
  - `-2.0 -3.0 2.0 0.0` (coordenadas negativas) → `Distancia: 5.00`
  - `1.0 2.0 4.0 6.0` (deslocamento delta_x=3, delta_y=4) → `Distancia: 5.00`

### 5. `B02_C02_corrigido.c` (Média ponderada com cast e parênteses)
- **Entradas:** `int n1, n2, n3`.
- **Saídas:** `Media: %.2f\n`.
- **Casos:**
  - `10 10 10` (nota máxima) → `Media: 10.00`
  - `5 7 8` (`(10 + 21 + 40) / 10 = 7.10`) → `Media: 7.10`
  - `0 0 0` (nota zero) → `Media: 0.00`
  - `6 8 9` (`(12 + 24 + 45) / 10 = 8.10`) → `Media: 8.10`
  - `4 5 6` (`(8 + 15 + 30) / 10 = 5.30`) → `Media: 5.30`

### 6. `B02_C03.c` (Hipotenusa de triângulo retângulo com `-lm`)
- **Entradas:** `int a, b`.
- **Saídas:** `Hipotenusa: %.2f\n`.
- **Casos:**
  - `3 4` (terna pitagórica 3-4-5) → `Hipotenusa: 5.00`
  - `5 12` (terna 5-12-13) → `Hipotenusa: 13.00`
  - `6 8` (terna 6-8-10) → `Hipotenusa: 10.00`
  - `8 15` (terna 8-15-17) → `Hipotenusa: 17.00`
  - `1 1` (caso irracional: sqrt(2)) → `Hipotenusa: 1.41`
