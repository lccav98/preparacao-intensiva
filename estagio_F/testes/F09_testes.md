# Rubrica e Gabarito Verificável — Bloco `F09`

- **Natureza do bloco:** **100% papel e análise conceitual** (pré-processamento, etapas de compilação e compilação vs. interpretação). **Não há arquivos `.c` nem `casos_F09.json` neste bloco.**
- **Status de verificação:**
  - **Executado:** revisão conceitual e consistência terminológica contra `Aula_20_Algoritmos_Roteiro_Atividade_Assíncrona.pdf`, `ementa_algoritmos.pdf` (item 11) e os conceitos de ligação de `F08`.
  - **Pendente:** não aplicável para GCC (`F09` não possui programas `.c` executáveis).

---

## Rubrica de Correção e Chaves Verificáveis

### Exercícios (`F09-E01` a `F09-E05`)
| Item | Critério de Acerto Integral (100% no item) | Chave Verificável |
|---|---|---|
| **`F09-E01`** | Remove o 2º `#include`, elimina comentário e expande `LIMITE` para `50`. | Código final contém apenas `int dobrar(int x);` e `return dobrar(50);` dentro de `main`. |
| **`F09-E02`** | Acerta ordem exata das 3 etapas, flag `-c` e atribui `undefined reference` à ligação. | `Pré-processamento` → `Compilação` → `Ligação`; flag `-c`; `Ligação`. |
| **`F09-E03`** | Corrige as 3 afirmações distinguindo texto (`#`), sintaxe/tipos (`.c -> .o`) e ligação. | (1) Tipos são checados na compilação; (2) `#define` não leva `;`; (3) `gcc -c` usa apenas o `.h` e a ligação ocorre depois. |
| **`F09-E04`** | Contrasta binário nativo dependente de CPU/SO vs. código/bytecode em VM e custo de tradução em execução. | C gera código de máquina nativo; Python/Java dependem de interpretador/JVM na máquina destino. |
| **`F09-E05`** | Identifica sucesso de `gcc -c`, falha de ligação sem `math_ops.o` e diferença C vs. Python em `if (0)`. | (a) Gera `main.o`; (b) `undefined reference` na ligação; (c) C barra na compilação, Python não executa o ramo falso. |

### Checagem Independente (`F09-C01` a `F09-C04` — Exige 4/4)
| Item | Habilidade Avaliada | Critério de Correção |
|---|---|---|
| **`F09-C01`** | Etapas C → executável | Descreve corretamente `Pré-processamento` (texto/`#`) → `Compilação` (`.o`) → `Ligação` (executável). |
| **`F09-C02`** | `#include`, `#define` e `#ifndef` | Explica colagem textual, substituição de macro e prevenção de inclusão múltipla com `#ifndef`. |
| **`F09-C03`** | Compilação vs. Interpretação | Contrasta momento da tradução, dependência de ambiente no usuário final e detecção de erros. |
| **`F09-C04`** | Portabilidade e compilação separada | Compara binário nativo C vs. bytecode JVM (`.class`) e explica por que `gcc -c a.c` precisa apenas de `b.h`, mas o executável precisa de `b.o`. |
