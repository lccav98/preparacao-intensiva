# Especificação de Testes — Bloco `D06`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, `#define` para tamanhos fixos (regra `N + 1`), sem `<string.h>`, sem `<ctype.h>`, sem `gets`, sem VLAs, sem funções extras e sem matrizes 2D. Saídas em ASCII puro.
- **Comparação de saídas:** correspondência textual exata linha a linha (`\n` final preservado).
- **Status de execução no ambiente atual (`19/11/2026`):**
  - **Executado:** verificação estática C99 + checagem de não-antecipação + **oráculo Python** sobre todos os **25 casos** de [casos_D06.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/casos_D06.json).
  - **Pendente:** compilação e execução binária em GCC (`gcc` ausente no ambiente local).

---

## Casos de Teste por Programa (5 casos por arquivo: normal + bordas críticas)

1. **`D06_E03_corrigido.c`:**
   - Normal com espaços na descrição (`C101` / `Introducao a Programacao C`) → `Codigo: C101` / `Desc: [Introducao a Programacao C]`
   - Código no limite exato de 15 chars (`ABCDEFGHIJKLMNO` / `Teste limite 15`) → `Codigo: ABCDEFGHIJKLMNO` / `Desc: [Teste limite 15]`
   - Descrição vazia (`X1` / `\n`) → `Codigo: X1` / `Desc: []`
   - Descrição com espaços múltiplos e dígitos (`A0` / `  123  456  `) → `Codigo: A0` / `Desc: [  123  456  ]`
   - Código com dígitos `'0'` no meio (`007` / `Agente Zero`) → `Codigo: 007` / `Desc: [Agente Zero]`

2. **`D06_E04.c`:**
   - Normal (`INFO` / `Algoritmos e Estruturas`) → `Tag: INFO` / `Titulo: [Algoritmos e Estruturas]`
   - Tag de 20 chars exatos (`12345678901234567890` / `Limite exato da tag`) → `Tag: 12345678901234567890` / `Titulo: [Limite exato da tag]`
   - Título com 1 caractere (`T` / `A`) → `Tag: T` / `Titulo: [A]`
   - Título vazio (`EMPTY` / `\n`) → `Tag: EMPTY` / `Titulo: []`
   - Espaços após a tag antes da quebra de linha (`TAG1   ` / `Linha limpa`) → `Tag: TAG1` / `Titulo: [Linha limpa]`

3. **`D06_E05.c`:**
   - Truncamento no meio (`Algoritmos em C` / `e`) → `Resultado: [Algoritmos ]`
   - Caractere no índice `0` (`Banana` / `B`) → `Resultado: []`
   - Caractere ausente (`Linguagem C` / `z`) → `Resultado: [Linguagem C]`
   - Múltiplas ocorrências (para na 1ª: `a-b-c-d` / `-`) → `Resultado: [a]`
   - Caractere no último índice útil (`UTFPR` / `R`) → `Resultado: [UTFP]`

4. **`D06_C02_corrigido.c`:**
   - Normal (`UTFPR` / `Ponta Grossa`) → `Sigla: UTFPR | Cidade: Ponta Grossa`
   - Sigla no limite de 10 chars (`PARANA2026` / `Curitiba Sul`) → `Sigla: PARANA2026 | Cidade: Curitiba Sul`
   - Cidade de palavra única (`USP` / `SaoPaulo`) → `Sigla: USP | Cidade: SaoPaulo`
   - Cidade vazia (`TEST` / `\n`) → `Sigla: TEST | Cidade: `
   - Sigla de 1 char (`C` / `Belo Horizonte`) → `Sigla: C | Cidade: Belo Horizonte`

5. **`D06_C03.c`:**
   - Normal (`20260012` / `Maria Silva` / `Algoritmos em C`) → `Matricula: 20260012`, `Nome: Maria Silva`, `Disciplina: Algoritmos em C`
   - Matrícula no limite de 12 chars (`123456789012` / `Joao Pedro` / `Calculo I`) → `Matricula: 123456789012`, `Nome: Joao Pedro`, `Disciplina: Calculo I`
   - Espaços extras na entrada (`M1   ` / `Ana` / `Fisica 1`) → `Matricula: M1`, `Nome: Ana`, `Disciplina: Fisica 1`
   - Nome simples e disciplina vazia (`A1` / `Carlos` / `\n`) → `Matricula: A1`, `Nome: Carlos`, `Disciplina: `
   - Nome com espaços internos múltiplos (`RA99` / `Luis  Souza` / `Estrutura de Dados`) → `Matricula: RA99`, `Nome: Luis  Souza`, `Disciplina: Estrutura de Dados`
