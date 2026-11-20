# Especificação de Testes — Bloco `F05`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, protótipos declarados antes de `main`, parâmetros escalares e ponteiros para escalares (sem passagem de vetores/matrizes/strings, multi-arquivo ou recursão).
- **Comparação de saídas e tolerância:**
  - Inteiros: correspondência exata.
  - Valores reais (`%.2f` em `F05_C03.c`): correspondência textual exata e tolerância numérica de **`1e-2`**.
- **Status de execução no ambiente atual (`19/11/2026`):**
  - **Executado:** verificação estática C99 + checagem de não-antecipação + **oráculo matemático Python** sobre todos os **30 casos** de [casos_F05.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/casos_F05.json).
  - **Pendente:** compilação e execução binária em GCC (`gcc` ausente no ambiente local).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`F05_E03_corrigido.c` (`trocar`):**
   - `10 20` (normais distintos) → `20 10`
   - `-5 12` (negativo e positivo) → `12 -5`
   - `7 7` (iguais) → `7 7`
   - `0 -9` (zero e negativo) → `-9 0`
   - `100 -100` (opostos) → `-100 100`

2. **`F05_E04.c` (`soma_e_diferenca`):**
   - `15 4` (normais) → `Soma: 19` / `Diferenca: 11`
   - `4 15` (diferença negativa) → `Soma: 19` / `Diferenca: -11`
   - `-8 -3` (dois negativos) → `Soma: -11` / `Diferenca: -5`
   - `0 0` (zeros) → `Soma: 0` / `Diferenca: 0`
   - `-7 7` (opostos) → `Soma: 0` / `Diferenca: -14`

3. **`F05_E05.c` (`extremos_tres`):**
   - `8 2 14` (normais) → `Menor: 2` / `Maior: 14`
   - `-10 -3 -25` (todos negativos) → `Menor: -25` / `Maior: -3`
   - `5 5 5` (todos iguais) → `Menor: 5` / `Maior: 5`
   - `9 9 1` (empate de maior) → `Menor: 1` / `Maior: 9`
   - `0 -5 0` (empate com zero) → `Menor: -5` / `Maior: 0`

4. **`F05_E06.c` (`decompor_tempo`):**
   - `7384` (normal composto) → `2 h, 3 min, 4 s`
   - `0` (borda zero) → `0 h, 0 min, 0 s`
   - `59` (borda abaixo de 1 minuto) → `0 h, 0 min, 59 s`
   - `3599` (borda abaixo de 1 hora) → `0 h, 59 min, 59 s`
   - `3600` (borda exatamente 1 hora) → `1 h, 0 min, 0 s`

5. **`F05_C02_corrigido.c` (`acumular` a partir de `100`):**
   - `25 40` (dois positivos) → `Saldo: 165`
   - `-30 10` (saque e depósito) → `Saldo: 80`
   - `0 0` (neutro) → `Saldo: 100`
   - `-100 0` (zera saldo) → `Saldo: 0`
   - `-150 20` (saldo negativo) → `Saldo: -30`

6. **`F05_C03.c` (`retangulo`):**
   - `5.0 3.0` (inteiros como reais) → `Area: 15.00` / `Perimetro: 16.00`
   - `2.5 4.2` (decimais) → `Area: 10.50` / `Perimetro: 13.40`
   - `1.0 1.0` (quadrado unitário) → `Area: 1.00` / `Perimetro: 4.00`
   - `0.5 0.5` (menor que 1) → `Area: 0.25` / `Perimetro: 2.00`
   - `12.34 5.60` (duas casas decimais) → `Area: 69.10` / `Perimetro: 35.88`
