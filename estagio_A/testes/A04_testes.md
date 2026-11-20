# Especificação e Rubrica de Verificação — Bloco `A04`

- **Natureza do bloco:** validação sintática e conceitual de identificadores, palavras reservadas e declarações de variáveis (`char`, `int`, `float`, `double`), sem operações de E/S formatada (`%d`, `%f`, `%c`), sem `scanf`, sem constantes (`#define`/`const`) e sem operadores. Não utiliza casos binários `casos_A04.json` nem arquivos `.c` em `solucoes/`.
- **Critério de validação estática:** conformidade C99 das declarações apresentadas no gabarito e ausência de antecipações proibidas (`printf`/`scanf` de variáveis, `=`, `#define`, `const`, operadores) em [A04_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/blocos/A04_bloco.md) e [A04_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/gabaritos/A04_gabarito.md).
- **Status de execução:**
  - **Executado:** auditoria estática de sintaxe C99 nas declarações, checagem de não-antecipação e verificação da rubrica dos 10 itens (`A04-E01`–`A04-E06` e `A04-C01`–`A04-C04`).
  - **Pendente / Não aplicável:** compilação e execução binária em GCC não aplicáveis a entregas individuais de `solucoes/` em `A04` (bloco sem `.c` em `solucoes/`, e `gcc` ausente no ambiente local).

---

## Rubrica Objetiva de Correção (`A04-E01` a `A04-E06` e `A04-C01` a `A04-C04`)

| Item | Critérios Obrigatórios para Acerto Integral (`1/1`) | Erro Típico que Reprova o Item |
|---|---|---|
| **`A04-E01`** | Classifica exatamente `idadeAluno`, `taxa_juros` e `_indice` como válidos, e `1semestre` (dígito inicial), `while` (reservada) e `saldo-atual` (hífen `-`) como inválidos com justificativa correta. | Marcar `_indice` como inválido ou `saldo-atual` como válido. |
| **`A04-E02`** | Preenche respectivamente `int`, `char`, `double`, `float`. | Trocar `double` por `float` quando o enunciado exige dupla precisão. |
| **`A04-E03`** | Identifica os **4 defeitos** (`3notas`, `preco produto`, `int`, `taxa%`) e reescreve 4 declarações válidas com `;`. | Esquecer `;` ao reescrever ou usar caractere com acento/espaço na correção. |
| **`A04-E04`** | **(a)** Lista exatamente `char`, `sizeof`, `return`; **(b)** aponta `média` pelo acento; **(c)** cita *case-sensitivity* para `media_1` vs `Media_1`. | Incluir `Char` ou `Return` como palavras reservadas. |
| **`A04-E05`** | **(a)** Declara `int`, `double` e `char` com nomes válidos sem `=`; **(b)** indica que o conteúdo inicial na memória é indeterminado. | Responder que `int` começa automaticamente com `0` ou inicializar com `=`. |
| **`A04-E06`** | Escreve `#include <stdio.h>`, `int main(void)`, declara `int`, `char`, `double` e `float` com nomes válidos e termina com `return 0;` (sem `=` ou `printf`). | Usar `void` como tipo de variável ou antecipar `scanf`/`printf`. |
| **`A04-C01`** | Classifica exatamente `nota2`, `valor_final`, `_total` (válidos) e `2nota`, `valor final`, `custo$` (inválidos com motivo). | Classificar `nota2` como inválido por conter dígito no final. |
| **`A04-C02`** | **(a)** Aponta apenas `void`, `switch`, `for`; **(b)** explica *case-sensitivity* (`Void` ≠ `void`) e idioma das palavras reservadas (`caso` ≠ `case`). | Marcar `For` ou `caso` como palavras reservadas. |
| **`A04-C03`** | Escolhe `int` (passageiros), `double` (coeficiente de alta precisão) e `char` (turno único) com justificativa coerente. | Escolher `float` para alta precisão ou `void` para turno. |
| **`A04-C04`** | Escreve 4 declarações válidas em `int`, `char`, `float`, `double` com identificadores mnemônicos corretos e `;` sem `=`. | Omitir `;`, usar espaços/acentos no nome ou inverter `float` e `double`. |
