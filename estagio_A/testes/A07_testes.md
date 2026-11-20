# Especificação de Testes — Bloco `A07`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, `int main(void)`, `return 0;`, `scanf`/`printf` e atribuição/troca com `aux`; **ausência** de `/`, `%`, `<math.h>`, `if`, laços e vetores.
- **Critério de comparação e tolerância:**
  - Inteiros: correspondência textual exata.
  - Valores `double` em `A07_E05.c` (`%.2f`): correspondência textual exata e tolerância numérica de **`1e-2`**.
- **Status de execução no ambiente atual (`19/11/2026`):**
  - **Executado:** verificação estática C99 + checagem de não-antecipação + sincronia literal com [A07_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/gabaritos/A07_gabarito.md) + **simulação/oráculo em Python** sobre todos os **18 casos** de [casos_A07.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/casos_A07.json).
  - **Pendente:** compilação e execução binária em GCC (`gcc` ausente no ambiente local).

---

## Casos de Teste por Programa (mínimo 4 casos por arquivo: normais, iguais, negativos e zeros)

### 1. `A07_E04_corrigido.c` (Troca de dois inteiros)
- `A07-E04-T1` (normal): `10 20\n` → `x = 20, y = 10`
- `A07-E04-T2` (negativos): `-8 -3\n` → `x = -3, y = -8`
- `A07-E04-T3` (zeros): `0 0\n` → `x = 0, y = 0`
- `A07-E04-T4` (iguais): `7 7\n` → `x = 7, y = 7`
- `A07-E04-T5` (zero e negativo): `0 -15\n` → `x = -15, y = 0`

### 2. `A07_E05.c` (Troca de dois `double` exibindo antes e depois)
- `A07-E05-T1` (normal): `3.50 8.25\n` → `Antes: a = 3.50, b = 8.25` / `Depois: a = 8.25, b = 3.50`
- `A07-E05-T2` (negativos): `-4.75 -1.25\n` → `Antes: a = -4.75, b = -1.25` / `Depois: a = -1.25, b = -4.75`
- `A07-E05-T3` (zeros): `0.0 0.0\n` → `Antes: a = 0.00, b = 0.00` / `Depois: a = 0.00, b = 0.00`
- `A07-E05-T4` (iguais): `5.50 5.50\n` → `Antes: a = 5.50, b = 5.50` / `Depois: a = 5.50, b = 5.50`

### 3. `A07_E06.c` (Rotação cíclica à direita de 3 inteiros)
- `A07-E06-T1` (normal): `10 20 30\n` → `Antes: 10 20 30` / `Depois: 30 10 20`
- `A07-E06-T2` (negativos): `-5 -2 -9\n` → `Antes: -5 -2 -9` / `Depois: -9 -5 -2`
- `A07-E06-T3` (zeros): `0 0 0\n` → `Antes: 0 0 0` / `Depois: 0 0 0`
- `A07-E06-T4` (iguais + zero): `4 4 0\n` → `Antes: 4 4 0` / `Depois: 0 4 4`

### 4. `A07_C03.c` (Rotação cíclica à esquerda de 3 inteiros)
- `A07-C03-T1` (normal): `1 2 3\n` → `Resultado: 2 3 1`
- `A07-C03-T2` (negativos): `-10 -20 -30\n` → `Resultado: -20 -30 -10`
- `A07-C03-T3` (zeros): `0 0 0\n` → `Resultado: 0 0 0`
- `A07-C03-T4` (iguais): `9 9 9\n` → `Resultado: 9 9 9`
- `A07-C03-T5` (negativo, zero e positivo): `-4 0 8\n` → `Resultado: 0 8 -4`
