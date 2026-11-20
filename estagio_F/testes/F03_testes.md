# Especificação de Testes — Bloco `F03`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, protótipos antes de `main`, parâmetros escalares copiados **por valor** (sem ponteiros `*`, sem passagem de `&var` para funções próprias, sem vetores/matrizes/strings em parâmetros e sem recursão), saídas em ASCII puro.
- **Comparação de saídas e tolerância:**
  - Inteiros: correspondência exata.
  - Valores reais (`%.2f` em `F03_E03_corrigido.c` e `F03_E05.c`): correspondência textual exata e tolerância numérica de **`1e-2`**.
- **Casos de teste registrados:** 20 casos (5 por arquivo `.c`) em [casos_F03.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/casos_F03.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`F03_E03_corrigido.c` (`reajustar` com `return`):**
   - `1000.00 10.0` (aumento normal de 10%) → `Novo salario: 1100.00`
   - `2500.00 0.0` (percentual zero) → `Novo salario: 2500.00`
   - `1200.00 15.0` (aumento de 15%) → `Novo salario: 1380.00`
   - `800.00 -10.0` (redução de 10%) → `Novo salario: 720.00`
   - `0.00 25.0` (base zero) → `Novo salario: 0.00`

2. **`F03_E04.c` (`processar_saque`):**
   - `500 120` (saque válido) → `Original: 500` / `Atualizado: 380`
   - `200 200` (saque exato do saldo → `0`) → `Original: 200` / `Atualizado: 0`
   - `150 200` (saldo insuficiente → inalterado) → `Original: 150` / `Atualizado: 150`
   - `300 0` (saque zero → inalterado) → `Original: 300` / `Atualizado: 300`
   - `300 -50` (saque negativo → inalterado) → `Original: 300` / `Atualizado: 300`

3. **`F03_E05.c` (`converter_celsius_para_kelvin` + `limitar_intervalo`):**
   - `25.0` (temperatura normal) → `Kelvin limitado: 298.15`
   - `-300.0` (abaixo do zero absoluto → saturado em `0.00`) → `Kelvin limitado: 0.00`
   - `-273.15` (borda exata `0.00 K`) → `Kelvin limitado: 0.00`
   - `800.0` (acima do teto `1000.00 K` → saturado) → `Kelvin limitado: 1000.00`
   - `726.85` (borda exata `1000.00 K`) → `Kelvin limitado: 1000.00`

4. **`F03_C03.c` (`aplicar_multa` convertido para `return`):**
   - `12 5` (multa positiva) → `Total de pontos: 17`
   - `0 7` (início zerado) → `Total de pontos: 7`
   - `10 0` (infração zero → mantém `10`) → `Total de pontos: 10`
   - `10 -3` (infração negativa → mantém `10`) → `Total de pontos: 10`
   - `20 1` (incremento unitário) → `Total de pontos: 21`
