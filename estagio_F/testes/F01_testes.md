# Especificação de Testes — Bloco `F01`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, funções auxiliares definidas **antes de `main`** (sem protótipos separados), parâmetros escalares copiados por valor (sem ponteiros `*`, sem passagem de `&var`, sem vetores/matrizes/strings em parâmetros e sem recursão), saídas em ASCII puro.
- **Comparação de saídas e tolerância:**
  - Inteiros e texto: correspondência exata.
  - Valores reais (`%.2f` em `F01_C02_corrigido.c`): correspondência textual exata e tolerância numérica de **`1e-2`**.
- **Casos de teste registrados:** 25 casos (5 por arquivo `.c`) em [casos_F01.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/casos_F01.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`F01_E03_corrigido.c` (`maior_de_dois`):**
   - `10 25` (segundo maior) → `Maior: 25`
   - `30 12` (primeiro maior) → `Maior: 30`
   - `7 7` (empate) → `Maior: 7`
   - `-5 -12` (dois negativos) → `Maior: -5`
   - `0 -3` (zero e negativo) → `Maior: 0`

2. **`F01_E04.c` (`exibir_faixa` + `soma_intervalo`):**
   - `3 7` (intervalo normal) → `3 4 5 6 7` / `Soma: 25`
   - `5 5` (intervalo unitário) → `5` / `Soma: 5`
   - `8 4` (intervalo invertido/vazio) → `Intervalo vazio` / `Soma: 0`
   - `-2 2` (simétrico em torno de zero) → `-2 -1 0 1 2` / `Soma: 0`
   - `-4 -1` (todos negativos) → `-4 -3 -2 -1` / `Soma: -10`

3. **`F01_E05.c` (`contar_digitos` + `soma_digitos`):**
   - `5832` (normal 4 dígitos) → `Digitos: 4` / `Soma dos digitos: 18`
   - `0` (borda zero) → `Digitos: 1` / `Soma dos digitos: 0`
   - `7` (borda 1 dígito) → `Digitos: 1` / `Soma dos digitos: 7`
   - `1000` (potência de 10 com zeros) → `Digitos: 4` / `Soma dos digitos: 1`
   - `90909` (zeros intercalados) → `Digitos: 5` / `Soma dos digitos: 27`

4. **`F01_C02_corrigido.c` (`calcular_subtotal` + `calcular_desconto`):**
   - `10.50 4` (abaixo do limiar `200.0`) → `Total: 42.00`
   - `50.00 4` (exatamente no limiar `200.00`, 10% de desconto) → `Total: 180.00`
   - `49.99 4` (logo abaixo do limiar: `199.96`) → `Total: 199.96`
   - `120.00 3` (acima do limiar: `360.00` - `36.00`) → `Total: 324.00`
   - `0.00 5` (borda zero) → `Total: 0.00`

5. **`F01_C03.c` (`imprimir_linha` + `fatorial`):**
   - `5 *` (normal) → `*****` / `Fatorial: 120`
   - `0 #` (borda `n = 0`) → linha vazia (`\n`) / `Fatorial: 1`
   - `1 A` (borda `n = 1`) → `A` / `Fatorial: 1`
   - `6 -` (normal) → `------` / `Fatorial: 720`
   - `4 +` (normal) → `++++` / `Fatorial: 24`
