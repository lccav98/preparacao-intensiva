# Especificação de Testes — Bloco `G06`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, proibição estrita de laços (`for`, `while`, `do-while`) dentro de funções recursivas, uso de `const char []` nas funções de leitura, sem `<string.h>`, sem `struct`, sem `malloc`/`free`, sem `gets(`, sem VLAs e saídas em ASCII puro.
- **Comparação de saídas e tolerância:**
  - Inteiros e strings: correspondência textual exata (`tolerancia_numerica: 0.01` mantida por padrão no JSON).
- **Casos de teste registrados:** **20 casos** (5 por arquivo `.c`) em [casos_G06.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/casos_G06.json).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`G06_E03_corrigido.c` (`contar_caractere` + `imprimir_inversa`):**
   - `"banana"` / `'a'` → `Ocorrencias: 3` / `Inversa: ananab`
   - `"arara azul"` / `'a'` → `Ocorrencias: 4` / `Inversa: luza arara` (com espaço)
   - `""` (linha vazia) / `'x'` → `Ocorrencias: 0` / `Inversa: ` (borda string vazia)
   - `"Aba"` / `'a'` → `Ocorrencias: 1` / `Inversa: abA` (*case-sensitive*)
   - `"z"` / `'z'` → `Ocorrencias: 1` / `Inversa: z` (borda 1 caractere)

2. **`G06_E04.c` (`contar_vogais` + `imprimir_inversa`):**
   - `"Algoritmos"` → `Vogais: 4` / `Inversa: somtiroglA`
   - `"AEIOUaeiou"` → `Vogais: 10` / `Inversa: uoieaUOIEA`
   - `"C99 GCC"` → `Vogais: 0` / `Inversa: CCG 99C`
   - `""` (linha vazia) → `Vogais: 0` / `Inversa: ` (borda string vazia)
   - `"Casa Azul"` → `Vogais: 4` / `Inversa: luzA asaC`

3. **`G06_E05.c` (`comprimento` + `iguais`):**
   - `"casa" "casa"` → `Comp A: 4` / `Comp B: 4` / `Iguais: Sim`
   - `"SOL" "SOLAR"` → `Comp A: 3` / `Comp B: 5` / `Iguais: Nao` (prefixo com tamanhos diferentes)
   - `"SOLAR" "SOL"` → `Comp A: 5` / `Comp B: 3` / `Iguais: Nao` (ordem invertida)
   - `"Casa" "casa"` → `Comp A: 4` / `Comp B: 4` / `Iguais: Nao` (mesmo tamanho, maiúscula vs minúscula)
   - `"x" "x"` → `Comp A: 1` / `Comp B: 1` / `Iguais: Sim` (borda 1 caractere)

4. **`G06_C03.c` (`contar_digitos_str` + `tem_caractere`):**
   - `"C99 e 2026"` / `'9'` → `Digitos: 6` / `Contem: Sim`
   - `"Algoritmos"` / `'z'` → `Digitos: 0` / `Contem: Nao`
   - `"012345"` / `'5'` → `Digitos: 6` / `Contem: Sim`
   - `""` (linha vazia) / `'a'` → `Digitos: 0` / `Contem: Nao` (borda string vazia)
   - `"a1b2"` / `'1'` → `Digitos: 2` / `Contem: Sim`
