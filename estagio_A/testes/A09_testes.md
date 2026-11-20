# Especificação de Testes — Bloco `A09`

- **Ambiente alvo:** Linux (`x86-64`, modelo de dados **LP64**), compilador GCC, padrão **C99**.
- **Nota de portabilidade importante (LP64 vs. LLP64):**
  - No ambiente alvo **Linux x86-64 (LP64)**, os tamanhos em bytes são: `char = 1`, `short = 2`, `int = 4`, **`long = 8`**, `float = 4`, `double = 8`.
  - Em **Windows 64 bits (LLP64)**, `sizeof(long)` é **`4`** (e não `8`). Os casos determinísticos de [casos_A09.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/casos_A09.json) espelham o ambiente alvo **Linux x86-64 (LP64)** da disciplina (`Aula_04` p. 11).
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, `int main(void)`, `return 0;`, `sizeof` impresso exclusivamente com `%zu`, sufixo `f` para `float` e soma `+` apenas em `A09_E05.c`; **ausência** de `if`, laços, `/`, `%`, `<math.h>` e vetores.
- **Status de execução no ambiente atual (`19/11/2026`):**
  - **Executado:** verificação estática C99 + checagem de não-antecipação + sincronia literal com [A09_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/gabaritos/A09_gabarito.md) + **simulação IEEE-754 em Python (`ctypes.c_float` e `float` 64 bits)** e conferência de `sizeof` LP64 sobre os **3 casos** de [casos_A09.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/casos_A09.json).
  - **Pendente:** compilação e execução binária em GCC (`gcc` ausente no ambiente local).

---

## Casos de Teste Determinísticos (Sem `stdin` — 1 caso por arquivo)

### 1. `A09_E03_corrigido.c` (`sizeof` com `%zu` + `0.1f` vs `0.1` em `%.10f` e `%.20f`)
- **Entrada (`stdin`):** vazia (`""`)
- **Saída esperada (`stdout`):**
  ```text
  float: 4 bytes
  double: 8 bytes
  float 0.1f (10 casas): 0.1000000015
  float 0.1f (20 casas): 0.10000000149011611938
  double 0.1 (10 casas): 0.1000000000
  double 0.1 (20 casas): 0.10000000000000000555
  ```

### 2. `A09_E05.c` (Experimento `0.1f + 0.2f` vs `0.1 + 0.2`)
- **Entrada (`stdin`):** vazia (`""`)
- **Saída esperada (`stdout`):**
  ```text
  float 10 casas: 0.3000000119
  float 20 casas: 0.30000001192092895508
  double 10 casas: 0.3000000000
  double 20 casas: 0.30000000000000004441
  ```

### 3. `A09_C03.c` (`sizeof` dos 6 tipos fundamentais em Linux x86-64 LP64)
- **Entrada (`stdin`):** vazia (`""`)
- **Saída esperada (`stdout`):**
  ```text
  char: 1 bytes
  short: 2 bytes
  int: 4 bytes
  long: 8 bytes
  float: 4 bytes
  double: 8 bytes
  ```
