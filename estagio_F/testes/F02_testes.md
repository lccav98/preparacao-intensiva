# Especificação de Testes — Bloco `F02`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, protótipos declarados antes de `main` com definições após `main`, parâmetros escalares copiados por valor (sem ponteiros `*`, sem passagem de `&var`, sem vetores/matrizes/strings em parâmetros e sem recursão), saídas em ASCII puro.
- **Comparação de saídas e tolerância:** correspondência textual e inteira exata.
- **Casos de teste registrados:** 25 casos (5 por arquivo `.c`) em [casos_F02.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/casos_F02.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`F02_E03_corrigido.c` (`quadrado` + `soma_quadrados`):**
   - `3 4` (normal) → `Soma dos quadrados: 25`
   - `0 0` (zeros) → `Soma dos quadrados: 0`
   - `-3 4` (negativo e positivo) → `Soma dos quadrados: 25`
   - `-5 -2` (dois negativos) → `Soma dos quadrados: 29`
   - `10 0` (um zero) → `Soma dos quadrados: 100`

2. **`F02_E04.c` (`eh_bissexto` + `dias_no_mes`):**
   - `2 2024` (fevereiro bissexto divisível por 4) → `Dias: 29`
   - `2 1900` (borda secular não-bissexto, divisível por 100) → `Dias: 28`
   - `2 2000` (borda secular bissexto, divisível por 400) → `Dias: 29`
   - `4 2025` (mês de 30 dias) → `Dias: 30`
   - `13 2025` (mês inválido) → `Mes invalido`

3. **`F02_E05.c` (`soma_divisores_proprios` + `eh_perfeito`):**
   - `1 30` (normal contendo `6` e `28`) → `Perfeitos: 2`
   - `6 6` (borda unitária em perfeito) → `Perfeitos: 1`
   - `7 27` (intervalo sem perfeitos) → `Perfeitos: 0`
   - `1 500` (contém `6`, `28`, `496`) → `Perfeitos: 3`
   - `-5 5` (contém negativos e `0`, `1`) → `Perfeitos: 0`

4. **`F02_C02_corrigido.c` (`mdc` + `mmc`):**
   - `12 18` (normal) → `MDC: 6` / `MMC: 36`
   - `7 13` (primos entre si) → `MDC: 1` / `MMC: 91`
   - `5 5` (iguais) → `MDC: 5` / `MMC: 5`
   - `24 6` (um múltiplo do outro) → `MDC: 6` / `MMC: 24`
   - `1 9` (borda com `1`) → `MDC: 1` / `MMC: 9`

5. **`F02_C03.c` (`eh_primo` + `contar_primos`):**
   - `1 10` (contém `1` não-primo e `2, 3, 5, 7`) → `Primos: 4`
   - `2 2` (borda menor primo) → `Primos: 1`
   - `-10 1` (negativos até `1`, nenhum primo) → `Primos: 0`
   - `14 16` (intervalo composto) → `Primos: 0`
   - `10 30` (normal: `11, 13, 17, 19, 23, 29`) → `Primos: 6`
