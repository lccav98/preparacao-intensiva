# Especificação de Testes — Bloco `D07`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>` e `#include <ctype.h>`, sem `<string.h>`, sem `gets`, sem VLAs, sem funções extras e sem matrizes 2D. Saídas em ASCII puro.
- **Comparação de saídas e tolerância:**
  - Strings e contagens: correspondência textual exata.
  - Médias (`%.2f`): tolerância numérica de **`1e-2`**.
- **Status de execução no ambiente atual (`19/11/2026`):**
  - **Executado:** verificação estática C99 + checagem de não-antecipação + **oráculo Python** sobre todos os **30 casos** de [casos_D07.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/casos_D07.json).
  - **Pendente:** compilação e execução binária em GCC (`gcc` ausente no ambiente local).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`D07_E03_corrigido.c`:**
   - Normal (`Sala 101 bloco B2`) → `Palavras: 4`, `Limpa: [Sala  bloco B]`
   - Espaços múltiplos nas bordas (`  teste   123  `) → `Palavras: 2`, `Limpa: [  teste     ]`
   - Só dígitos (`987654`) → `Palavras: 1`, `Limpa: []`
   - Só espaços (`    `) → `Palavras: 0`, `Limpa: [    ]`
   - Linha vazia (`\n`) → `Palavras: 0`, `Limpa: []`

2. **`D07_E04.c`:**
   - Normal (`Algoritmos C99`) → `Comprimento: 14`, `Vogais: 4`, `Digitos: 2`, `Palavras: 2`
   - Múltiplos espaços e maiúsculas (`  AEIOU   01  `) → `Comprimento: 14`, `Vogais: 5`, `Digitos: 2`, `Palavras: 2`
   - Só espaços (`     `) → `Comprimento: 5`, `Vogais: 0`, `Digitos: 0`, `Palavras: 0`
   - Linha vazia (`\n`) → `Comprimento: 0`, `Vogais: 0`, `Digitos: 0`, `Palavras: 0`
   - Sem vogais (`bcdf 42!`) → `Comprimento: 8`, `Vogais: 0`, `Digitos: 2`, `Palavras: 2`

3. **`D07_E05.c`:**
   - Normal com espaços extras (`  ola   mundo   C  `) → `[ola mundo C]`
   - Palavra única sem espaços (`UTFPR`) → `[UTFPR]`
   - Só espaços (`      `) → `[]`
   - Linha vazia (`\n`) → `[]`
   - Espaço único interno (`um dois tres`) → `[um dois tres]`

4. **`D07_E06.c`:**
   - Deslocamento positivo com wrap (`3` / `Luz 9!`) → `Cifrada: Oxc 9!`
   - Deslocamento negativo (`-3` / `Abc Xyz!`) → `Cifrada: Xyz Uvw!`
   - Deslocamento maior que 26 (`29` / `aZ 0`) → `Cifrada: dC 0`
   - Deslocamento múltiplo de 26 (`52` / `Teste 123`) → `Cifrada: Teste 123`
   - Sem letras (`123 !@#`) → `Cifrada: 123 !@#`

5. **`D07_C02_corrigido.c`:**
   - Normal (`ola mundo`) → `Maiuscula: OLA MUNDO`, `Media palavra: 4.00`
   - Espaços extras e pontuação (`  c99   ok! `) → `Maiuscula:   C99   OK! `, `Media palavra: 3.00`
   - Só espaços (`    `) → `Maiuscula:     `, `Media palavra: 0.00`
   - Linha vazia (`\n`) → `Maiuscula: `, `Media palavra: 0.00`
   - Já em maiúsculas (`ABC DE`) → `Maiuscula: ABC DE`, `Media palavra: 2.50`

6. **`D07_C03.c`:**
   - Normal (`C99: Aula-07!`) → `Limpa: [c99aula07]`, `Removidos: 4`
   - Só pontuação e espaços (`--- !!!   `) → `Limpa: []`, `Removidos: 10`
   - Apenas alfanuméricos (`AbC123`) → `Limpa: [abc123]`, `Removidos: 0`
   - Linha vazia (`\n`) → `Limpa: []`, `Removidos: 0`
   - Mistura completa (`A1, b2; C3.`) → `Limpa: [a1b2c3]`, `Removidos: 5`
