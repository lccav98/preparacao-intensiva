# Especificação de Testes — Bloco `A02`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99** (`[DOC]` `Aula_00` p. 3; `Aula_02` p. 4; `Aula_10` p. 18).
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas estaticamente nos arquivos `.c`:** apenas `#include <stdio.h>`, `int main(void)`, `return 0;`, `;`, comentários `//`/`/* */` e `printf` simples com strings literais estritamente ASCII usando no máximo `\n` (sem variáveis, `scanf`, `\t`, `\"`, `\\`, `%d`, `%f`, `%c`, operadores, `if` ou laços).
- **Critério de comparação:** correspondência textual exata byte a byte após normalização de `\r\n` → `\n` (`tolerancia_numerica: 0`).
- **Status de execução no ambiente atual (`19/11/2026`):**
  - **Executado:** validação estática C99 + checagem de não-antecipação + sincronia literal `.c` ↔ `A02_gabarito.md` + simulação textual da saída esperada sobre os **5 casos** de [casos_A02.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/casos_A02.json).
  - **Pendente:** compilação e execução binária em GCC (`gcc` ausente no ambiente local).

---

## Casos de Teste por Programa (`A02-E03` a `A02-E05`, `A02-C02`, `A02-C03`)

1. **`A02_E03_corrigido.c` (`A02-E03-T1`):**
   - `stdin`: vazio (`""`)
   - `stdout` esperado:
     ```text
     UTFPR Ponta Grossa
     Laboratorio GCC
     ```

2. **`A02_E04.c` (`A02-E04-T1`):**
   - `stdin`: vazio (`""`)
   - `stdout` esperado:
     ```text
     Passo 1: Editar codigo
     Passo 2: Compilar com gcc
     Passo 3: Executar no Linux
     ```

3. **`A02_E05.c` (`A02-E05-T1`):**
   - `stdin`: vazio (`""`)
   - `stdout` esperado:
     ```text
     Curso: Algoritmos CC61A
     Padrao: C99
     Compilador: GCC Linux
     ```

4. **`A02_C02_corrigido.c` (`A02-C02-T1`):**
   - `stdin`: vazio (`""`)
   - `stdout` esperado:
     ```text
     Sistema pronto
     Status: OK
     ```

5. **`A02_C03.c` (`A02-C03-T1`):**
   - `stdin`: vazio (`""`)
   - `stdout` esperado:
     ```text
     Compilacao limpa
     Execucao concluida
     ```
