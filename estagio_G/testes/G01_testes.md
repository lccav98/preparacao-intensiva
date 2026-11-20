# Rubrica e Gabarito Verificável — Bloco `G01`

- **Natureza do bloco:** **100% leitura, identificação e teste de mesa no papel** (tripé recursivo, pilha de execução e *stack overflow* por caso base inalcançável). **Não há arquivos `.c` nem `casos_G01.json` neste bloco.**
- **Status de verificação:**
  - **Executado:** revisão conceitual, rastreamento passo a passo de todas as chamadas/retornos e alinhamento terminológico com `Aula_21_Algoritmos.pdf` (p. 3–20) e `Aula_22_Algoritmos.pdf` (p. 3–14).
  - **Pendente:** não aplicável para GCC (`G01` não possui programas `.c` executáveis).

---

## Rubrica de Correção e Chaves Verificáveis

### Exercícios (`G01-E01` a `G01-E05`)
| Item | Critério de Acerto Integral (100% no item) | Chave Verificável |
|---|---|---|
| **`G01-E01`** | Identifica corretamente os 3 elementos do tripé em `fat` e rastreia todas as 5 chamadas e os 5 retornos na ordem inversa. | Caso base: `n == 0 -> 1`; passo: `n * fat(n - 1)`; progresso: `n - 1`; retornos: `1, 1, 2, 6, 24`. |
| **`G01-E02`** | Preenche as 4 lacunas da tabela respeitando empilhamento descendente e retorno ascendente. | `/* A */`: `soma_pares(4) = 4 + soma_pares(2)`; `/* B */`: `soma_pares(0)`; `/* C */`: `6`; `/* D */`: `12`. |
| **`G01-E03`** | Lista 4 chamadas iniciais de `f(3)` e `g(4)`, explica o *stack overflow* e propõe correção válida para cada função. | `f(3)->f(4)->f(5)->f(6)` (afasta-se de `0`, corrigir com `n - 1`); `g(4)->g(2)->g(0)->g(-2)` (pula `1`, corrigir com `n <= 1`). |
| **`G01-E04`** | Rastreia os 4 quadros `(a, b)` de `misterio(4, 3)` com retorno `0, 4, 8, 12` e identifica a multiplicação `a * b`. | Quadros `(4,3)->(4,2)->(4,1)->(4,0)`; soma final `12`; operação `a * b`. |
| **`G01-E05`** | Registra `k = 8, 6, 4, 2` separados por quadro e calcula retorno final `19`, explicando isolamento de quadros na pilha. | Retornos: `calc(1)=1`, `calc(2)=5`, `calc(3)=11`, `calc(4)=19`; cada chamada tem cópia local própria de `k`. |

### Checagem Independente (`G01-C01` a `G01-C03` — Exige 3/3 = 100%)
| Item | Habilidade Avaliada | Critério de Correção |
|---|---|---|
| **`G01-C01`** | Empilhamento e desempilhamento completo (`pot2(4)`) | Lista `pot2(4)->pot2(3)->pot2(2)->pot2(1)->pot2(0)`, informa **5 quadros** no pico e retornos `1, 2, 4, 8, 16`. |
| **`G01-C02`** | Rastreamento com passo `n - 2` (`seq(6)`) | Identifica `seq(0)` atingindo `n <= 1` com retorno `2` e desempilha `5 -> 8 -> 11`. |
| **`G01-C03`** | Diagnóstico de caso base inalcançável (`contar(5)`) | Mostra sequência `5, 3, 1, -1, -3...` pulando `0` (*stack overflow*) e corrige para `if (n <= 0) return 0;`. |
