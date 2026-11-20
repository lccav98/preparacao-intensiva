# Gabarito Comentado — Bloco `G01` (Conceito de Recursividade e Pilha de Execução)

> **Bloco de referência:** [G01_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/blocos/G01_bloco.md)  
> **Nota:** Bloco 100% de leitura, identificação e teste de mesa no papel; não há arquivos `.c` nem `casos_G01.json`.

---

## 1. Gabarito dos Exercícios (`G01-E01` a `G01-E05`)

### `G01-E01` *(Identificação do tripé e teste de mesa)*
- **(a)** Tripé em `fat(n)`:
  - **Caso base:** `if (n == 0) { return 1; }` (interrompe a recursão sem nova chamada).
  - **Passo recursivo:** `return n * fat(n - 1);` (delega o cálculo de `(n - 1)!`).
  - **Progresso:** para `n > 0`, o argumento passa de `n` para `n - 1`, diminuindo `1` unidade a cada chamada até atingir exatamente `0`.
- **(b)** Empilhamento e desempilhamento de `fat(4)`:
  - **Descida:** `fat(4) -> 4 * fat(3)` → `fat(3) -> 3 * fat(2)` → `fat(2) -> 2 * fat(1)` → `fat(1) -> 1 * fat(0)` → `fat(0)` retorna `1`.
  - **Subida:** `fat(0) = 1` → `fat(1) = 1 * 1 = 1` → `fat(2) = 2 * 1 = 2` → `fat(3) = 3 * 2 = 6` → `fat(4) = 4 * 6 = 24`.

### `G01-E02` *(Completar tabela de pilha de execução)*
- **`/* A */`:** `soma_pares(4) = 4 + soma_pares(2)`
- **`/* B */`:** `soma_pares(0)` (atinge caso base `n <= 0`)
- **`/* C */`:** `4 + 2 = 6`
- **`/* D */`:** `6 + 6 = 12`

### `G01-E03` *(Caça ao Caso Base Inalcançável — Stack Overflow)*
- **(1) Função `f(3)`:**
  - **Primeiras 4 chamadas:** `f(3)` → `f(4)` → `f(5)` → `f(6)`.
  - **Motivo da falha:** O argumento cresce (`n + 1`) afastando-se cada vez mais do caso base `n == 0`; o caso base nunca é atingido e a pilha estoura (*stack overflow*).
  - **Correção mínima:** Alterar o passo para `return n * f(n - 1);` (ou assumir `n >= 0` com `n - 1`).
- **(2) Função `g(4)`:**
  - **Primeiras 4 chamadas:** `g(4)` → `g(2)` → `g(0)` → `g(-2)`.
  - **Motivo da falha:** Partindo de um número par (`4`), subtrair `2` só gera números pares (`4, 2, 0, -2, ...`), pulando o caso base `n == 1`. A condição nunca se torna verdadeira e ocorre *stack overflow*.
  - **Correção mínima:** Trocar o caso base para `if (n <= 1) { return 1; }` (ou `if (n <= 0) { return 0; }` se a intenção for não somar no limite `0`, mantendo parada segura para pares e negativos).

### `G01-E04` *(Pilha com dois parâmetros — `misterio(4, 3)`)*
- **(a)** Rastreamento:
  - **Descida:**
    1. `misterio(a=4, b=3)` aguarda `4 + misterio(4, 2)`
    2. `misterio(a=4, b=2)` aguarda `4 + misterio(4, 1)`
    3. `misterio(a=4, b=1)` aguarda `4 + misterio(4, 0)`
    4. `misterio(a=4, b=0)` atinge `b == 0` e retorna `0`
  - **Subida:** `misterio(4,0) -> 0`, `misterio(4,1) -> 4 + 0 = 4`, `misterio(4,2) -> 4 + 4 = 8`, `misterio(4,3) -> 4 + 8 = 12`.
- **(b)** Para `b >= 0`, `misterio(a, b)` calcula a multiplicação **`a * b`** por somas sucessivas.

### `G01-E05` *(Variáveis locais independentes por quadro — `calc(4)`)*
- **(a)** Rastreamento na pilha:
  - `calc(4)`: `n = 4`, `k = 8` → aguarda `8 + calc(3)`
  - `calc(3)`: `n = 3`, `k = 6` → aguarda `6 + calc(2)`
  - `calc(2)`: `n = 2`, `k = 4` → aguarda `4 + calc(1)`
  - `calc(1)`: `n = 1`, `k = 2` → atinge `n <= 1`, **retorna `1`**
  - Retorno para `calc(2)`: `4 + 1 = 5`
  - Retorno para `calc(3)`: `6 + 5 = 11`
  - Retorno para `calc(4)`: `8 + 11 = 19`
- **(b)** Cada chamada recursiva cria um **novo quadro de ativação isolado** na pilha de execução, com sua própria variável local `k` em um endereço de memória distinto. Assim, `k` de `calc(1)` não altera o `k` guardado no quadro de `calc(4)`.

---

## 2. Gabarito da Checagem Independente (`G01-C01` a `G01-C03`)

### `G01-C01` *(Rastreamento de `pot2(4)`)*
1. **Chamadas empilhadas (base → topo):** `pot2(4)` → `pot2(3)` → `pot2(2)` → `pot2(1)` → `pot2(0)`.
2. **Pico de quadros simultâneos na pilha:** **5 quadros** (quando `pot2(0)` está executando).
3. **Ordem de retorno (topo → base):**
   - `pot2(0)` retorna `1`
   - `pot2(1)` retorna `2 * 1 = 2`
   - `pot2(2)` retorna `2 * 2 = 4`
   - `pot2(3)` retorna `2 * 4 = 8`
   - `pot2(4)` retorna `2 * 8 = 16`

### `G01-C02` *(Rastreamento de `seq(6)`)*
- **Descida:**
  - `seq(6)` aguarda `3 + seq(4)`
  - `seq(4)` aguarda `3 + seq(2)`
  - `seq(2)` aguarda `3 + seq(0)`
  - `seq(0)` satisfaz `n <= 1` (caso base atingido com `n = 0`) e retorna `2`.
- **Subida:**
  - `seq(2)` retorna `3 + 2 = 5`
  - `seq(4)` retorna `3 + 5 = 8`
  - `seq(6)` retorna `3 + 8 = 11`
- **Resultado final:** **`11`**.

### `G01-C03` *(Caso base inalcançável em `contar(5)`)*
- **(a)** Sequência empilhada: `contar(5)` → `contar(3)` → `contar(1)` → `contar(-1)` → `contar(-3)` → `...`. Como `5` é ímpar e o passo subtrai `2`, `n` permanece sempre ímpar, passa direto de `1` para `-1` sem nunca valer `0`, tornando o caso base `n == 0` inalcançável e provocando *stack overflow*.
- **(b)** Alterar o caso base para **`if (n <= 0) { return 0; }`** (parada por desigualdade), garantindo encerramento seguro tanto para entradas pares quanto ímpares (inclusive negativas).
