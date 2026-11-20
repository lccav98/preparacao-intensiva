# Especificação de Testes — Bloco `A05`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99** (`[DOC]` `Aula_00` p. 3; `Aula_10` p. 18).
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas estaticamente nos arquivos `.c`:** apenas `#include <stdio.h>`, `#define NOME valor` (sem `;`), `const tipo NOME = valor;`, inicialização na declaração (`int`, `double`, `char`), e `printf` com especificadores `%d`, `%i`, `%.Nf`, `%c` em texto estritamente ASCII (sem `scanf`, sem `%e` nos binários para independência de plataforma, sem reatribuição pós-declaração, sem operadores aritméticos `+ - * / %`, `if` ou laços).
- **Critério de comparação e tolerância numérica:**
  - Correspondência textual exata após normalização de `\r\n` → `\n` e tolerância numérica de **`1e-2`** (`0.01`) nos campos reais. Todos os valores literais (`72.453`, `3.14159`, `4.5`, `49.876`, `7.2`, `12.50`, `6.258`) foram escolhidos fora de pontos médios decimais ambíguos para garantir arredondamento determinístico em IEEE-754.
- **Status de execução no ambiente atual (`19/11/2026`):**
  - **Executado:** validação estática C99 + checagem de não-antecipação + sincronia literal `.c` ↔ `A05_gabarito.md` + **oráculo matemático e de formatação em Python** sobre todos os **5 casos** de [casos_A05.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/casos_A05.json).
  - **Pendente:** compilação e execução binária em GCC (`gcc` ausente no ambiente local).

---

## Casos de Teste por Programa (`A05-E03` a `A05-E05`, `A05-C02`, `A05-C03`)

1. **`A05_E03_corrigido.c` (`A05-E03-T1`):**
   - `stdin`: vazio (`""`)
   - `stdout` esperado: `Limite: 100 | Peso: 72.45 kg | Classe: A`

2. **`A05_E04.c` (`A05-E04-T1`):**
   - `stdin`: vazio (`""`)
   - `stdout` esperado:
     - Linha 1: `PI aproximado: 3.1416`
     - Linha 2: `Escala: 2`
     - Linha 3: `Raio: 4.50 m`

3. **`A05_E05.c` (`A05-E05-T1`):**
   - `stdin`: vazio (`""`)
   - `stdout` esperado:
     - Linha 1: `Ficha 2026 - Setor E`
     - Linha 2: `Codigo: 308`
     - Linha 3: `Valor: R$ 49.88`
     - Linha 4: `Peso: 7.2 kg`

4. **`A05_C02_corrigido.c` (`A05-C02-T1`):**
   - `stdin`: vazio (`""`)
   - `stdout` esperado: `Max: 40 | Taxa: 12.50`

5. **`A05_C03.c` (`A05-C03-T1`):**
   - `stdin`: vazio (`""`)
   - `stdout` esperado:
     - Linha 1: `Sistema v3`
     - Linha 2: `Sala 102 - Bloco C`
     - Linha 3: `Tarifa: R$ 6.26`
