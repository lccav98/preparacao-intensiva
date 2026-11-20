# Especificação de Testes — Bloco `A03`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99** (`[DOC]` `Aula_00` p. 3; `Aula_10` p. 18).
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas estaticamente nos arquivos `.c`:** apenas `#include <stdio.h>`, `int main(void)`, `return 0;`, `;`, comentários `//`/`/* */` e `printf` com strings literais estritamente ASCII usando apenas `\n`, `\t`, `\"` e `\\` (sem variáveis, `#define`/`const`, `%d`/`%f`/`%c`, `scanf`, operadores, `if` ou laços).
- **Critério de comparação:** correspondência exata byte a byte das quebras de linha `\n`, tabulações literais `\t` (`0x09`), aspas `"` e barras invertidas `\` após normalização de `\r\n` → `\n` (`tolerancia_numerica: 0`).
- **Status de execução no ambiente atual (`19/11/2026`):**
  - **Executado:** validação estática C99 + checagem de não-antecipação + sincronia literal `.c` ↔ `A03_gabarito.md` + simulação exata das sequências de escape em Python sobre todos os **5 casos** de [casos_A03.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/casos_A03.json).
  - **Pendente:** compilação e execução binária em GCC (`gcc` ausente no ambiente local).

---

## Casos de Teste por Programa (`A03-E03` a `A03-E05`, `A03-C02`, `A03-C03`)

1. **`A03_E03_corrigido.c` (`A03-E03-T1`):**
   - `stdin`: vazio (`""`)
   - `stdout` esperado (com quebras `\n`):
     - Linha 1: `Diretorio: C:\usuarios\aluno`
     - Linha 2: `Mensagem: "Compilado!"`

2. **`A03_E04.c` (`A03-E04-T1`):**
   - `stdin`: vazio (`""`)
   - `stdout` esperado (única chamada `printf`):
     - Linha 1: `UTFPR - Campus Ponta Grossa`
     - Linha 2: `Disciplina: Algoritmos`
     - Linha 3: `Padrao: "C99"`

3. **`A03_E05.c` (`A03-E05-T1`):**
   - `stdin`: vazio (`""`)
   - `stdout` esperado (tabulações `\t` reais entre colunas):
     - Linha 1: `Comando\tFuncao`
     - Linha 2: `"gcc"\tCompila C`
     - Linha 3: `\n\tNova linha`
     - Linha 4: `\\\tBarra literal` *(duas barras `\\` seguidas de `\t` e `Barra literal`)*

4. **`A03_C02_corrigido.c` (`A03-C02-T1`):**
   - `stdin`: vazio (`""`)
   - `stdout` esperado (tabulações `\t` reais):
     - Linha 1: `Codigo:\t100`
     - Linha 2: `Rota:\tC:\projetos\teste`
     - Linha 3: `Nota:\t"Aprovado"`

5. **`A03_C03.c` (`A03-C03-T1`):**
   - `stdin`: vazio (`""`)
   - `stdout` esperado (única chamada `printf` + tabulações `\t` reais):
     - Linha 1: `Relatorio\t"Final"`
     - Linha 2: `Pasta:\tD:\aulas\c`
     - Linha 3: `Situacao:\tOK`
