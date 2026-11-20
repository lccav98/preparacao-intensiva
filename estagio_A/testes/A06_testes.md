# Especificação de Testes — Bloco `A06`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99** (`[DOC]` `Aula_00` p. 3; `Aula_10` p. 18).
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** apenas `#include <stdio.h>`, `int main(void)`, `return 0;`, `scanf` (`%d`, `%f`, `%lf`, `" %c"`) com `&` e `printf` estritamente ASCII; **ausência** de reatribuição/troca `aux`, operadores aritméticos (`+`, `-`, `*`, `/`, `%`), `if`, laços, `%s` e vetores.
- **Critério de comparação e tolerância:**
  - Comparação textual exata linha a linha após normalização `\r\n` → `\n`.
  - Valores formatados com `%.1f` / `%.2f`: correspondência textual exata e tolerância numérica de **`1e-2`**.
- **Status de execução no ambiente atual (`19/11/2026`):**
  - **Executado:** verificação estática C99 + checagem de não-antecipação + sincronia literal com [A06_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/gabaritos/A06_gabarito.md) + **simulação/oráculo em Python** sobre todos os **20 casos** de [casos_A06.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/casos_A06.json).
  - **Pendente:** compilação e execução binária em GCC (`gcc` ausente no ambiente local).

---

## Casos de Teste por Programa (4 casos por arquivo: normal, negativos, zero e bordas)

### 1. `A06_E03_corrigido.c` (`int item; double preco; char setor;`)
- `A06-E03-T1` (normal): `105\n42.50\nB\n` → `Item: 105\nPreco: R$ 42.50\nSetor: B`
- `A06-E03-T2` (zero): `0\n0.0\nZ\n` → `Item: 0\nPreco: R$ 0.00\nSetor: Z`
- `A06-E03-T3` (negativo + espaços antes de `" %c"`): `-12\n-5.75   \n  A\n` → `Item: -12\nPreco: R$ -5.75\nSetor: A`
- `A06-E03-T4` (borda decimal): `999\n1234.80\nC\n` → `Item: 999\nPreco: R$ 1234.80\nSetor: C`

### 2. `A06_E04.c` (Leitura dupla `int` e `double`)
- `A06-E04-T1` (normal): `10 20\n1.50 9.75\n` → `IDs: 10 e 20\nLimites: 1.50 a 9.75`
- `A06-E04-T2` (zeros): `0 0\n0.0 0.0\n` → `IDs: 0 e 0\nLimites: 0.00 a 0.00`
- `A06-E04-T3` (negativos): `-5 -1\n-10.25 -0.50\n` → `IDs: -5 e -1\nLimites: -10.25 a -0.50`
- `A06-E04-T4` (tabulação e quebras de linha): `7\t8\n-100.00\n100.00\n` → `IDs: 7 e 8\nLimites: -100.00 a 100.00`

### 3. `A06_E05.c` (`int codigo; double temperatura; char escala;`)
- `A06-E05-T1` (normal): `12 24.5 C\n` → `Sensor 12: 24.5 C`
- `A06-E05-T2` (negativo): `3 -40.0 C\n` → `Sensor 3: -40.0 C`
- `A06-E05-T3` (zero com Enter antes de `char`): `0\n0.0\nK\n` → `Sensor 0: 0.0 K`
- `A06-E05-T4` (escala Fahrenheit): `99 212.0 F\n` → `Sensor 99: 212.0 F`

### 4. `A06_C01_corrigido.c` (`int sala; double area;`)
- `A06-C01-T1` (normal): `204\n48.50\n` → `Sala: 204\nArea: 48.50 m2`
- `A06-C01-T2` (zero): `0\n0.0\n` → `Sala: 0\nArea: 0.00 m2`
- `A06-C01-T3` (negativo): `-1\n-12.25\n` → `Sala: -1\nArea: -12.25 m2`
- `A06-C01-T4` (fração): `1\n0.75\n` → `Sala: 1\nArea: 0.75 m2`

### 5. `A06_C03.c` (`int id; double valor; char situacao;`)
- `A06-C03-T1` (normal): `42 150.25 A\n` → `ID: 42\nValor: R$ 150.25\nSituacao: A`
- `A06-C03-T2` (zero): `0 0.0 I\n` → `ID: 0\nValor: R$ 0.00\nSituacao: I`
- `A06-C03-T3` (negativo + quebra de linha): `-7\n-89.50\nP\n` → `ID: -7\nValor: R$ -89.50\nSituacao: P`
- `A06-C03-T4` (inteiro digitado para `%lf`): `500 300 F\n` → `ID: 500\nValor: R$ 300.00\nSituacao: F`
