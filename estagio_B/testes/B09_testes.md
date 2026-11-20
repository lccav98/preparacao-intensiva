# Especificação de Testes — Bloco `B09`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99** (`[DOC]` `Aula_00` p. 3; `Aula_10` p. 18).
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Critério de comparação:**
  - Comparação textual exata linha a linha após normalização de `\r\n` $\rightarrow$ `\n`.
  - Saídas formatadas com quebra de linha final `\n`.
- **Status de execução:**
  - Verificação de não-antecipação (ausência total de laços, vetores e funções extras).
  - Casos testados e validados contra os códigos C99 em `testes/solucoes/`.

---

## Casos de Teste por Programa (`B09-E03` a `B09-E06`, `B09-C02` e `B09-C03`)

### 1. `B09_E03_corrigido.c` (Cardápio com refeição e bebida)
- **Entradas:** `int prato, int bebida`.
- **Saídas:** Nome do prato e bebida ou mensagem de erro.
- **Casos:**
  - `1 1` $\rightarrow$ `Prato: Peixe\nBebida: Suco\n`
  - `1 2` $\rightarrow$ `Prato: Peixe\nBebida: Agua\n`
  - `1 3` $\rightarrow$ `Prato: Peixe\nBebida Invalida\n`
  - `2 1` $\rightarrow$ `Prato: Frango\nBebida: Suco\n`
  - `2 2` $\rightarrow$ `Prato: Frango\nBebida: Agua\n`
  - `3 1` $\rightarrow$ `Prato Invalido\n`

### 2. `B09_E04.c` (Terminal bancário com validação de saldo e valores)
- **Entradas:** `int op` e, para operações 1 e 2, `double valor`.
- **Saídas:** `Saldo Atual: R$ %.2f\n`, `Saldo Insuficiente\n`, `Valor Invalido\n` ou `Operacao Invalida\n`.
- **Casos:**
  - `1 250.00` $\rightarrow$ `Saldo Atual: R$ 750.00`
  - `1 1000.00` (saque de todo o saldo) $\rightarrow$ `Saldo Atual: R$ 0.00`
  - `1 1000.01` (saque excede saldo) $\rightarrow$ `Saldo Insuficiente`
  - `1 0.00` (valor zero inválido) $\rightarrow$ `Valor Invalido`
  - `2 500.00` $\rightarrow$ `Saldo Atual: R$ 1500.00`
  - `2 -50.00` (depósito negativo) $\rightarrow$ `Valor Invalido`
  - `3` (consulta saldo) $\rightarrow$ `Saldo Atual: R$ 1000.00`
  - `4` (opção inválida) $\rightarrow$ `Operacao Invalida`

### 3. `B09_E05.c` (Conceitos A-F com `nota / 10`)
- **Entradas:** `int nota`.
- **Saídas:** Conceito correspondente ou `Nota Invalida\n`.
- **Casos:**
  - `100` $\rightarrow$ `Conceito A`
  - `95` $\rightarrow$ `Conceito A`
  - `90` $\rightarrow$ `Conceito A`
  - `89` $\rightarrow$ `Conceito B`
  - `80` $\rightarrow$ `Conceito B`
  - `75` $\rightarrow$ `Conceito C`
  - `70` $\rightarrow$ `Conceito C`
  - `65` $\rightarrow$ `Conceito D`
  - `60` $\rightarrow$ `Conceito D`
  - `59` $\rightarrow$ `Conceito F`
  - `0` $\rightarrow$ `Conceito F`
  - `-1` (borda negativa) $\rightarrow$ `Nota Invalida`
  - `101` (borda positiva acima) $\rightarrow$ `Nota Invalida`

### 4. `B09_E06.c` (Totem de autoatendimento)
- **Entradas:** `int categoria, int item`.
- **Saídas:** Nome do produto e preço ou erro.
- **Casos:**
  - `1 1` $\rightarrow$ `Suco Natural: R$ 7.00`
  - `1 2` $\rightarrow$ `Refrigerante: R$ 5.00`
  - `1 3` $\rightarrow$ `Item Invalido`
  - `2 1` $\rightarrow$ `Sanduiche: R$ 12.00`
  - `2 2` $\rightarrow$ `Hamburguer: R$ 18.00`
  - `2 0` $\rightarrow$ `Item Invalido`
  - `3 1` $\rightarrow$ `Categoria Invalida`

### 5. `B09_C02.c` (Faixas etárias decimais)
- **Entradas:** `int idade`.
- **Saídas:** Nome da faixa etária ou `Idade Invalida\n`.
- **Casos:**
  - `5` $\rightarrow$ `Crianca`
  - `9` $\rightarrow$ `Crianca`
  - `10` $\rightarrow$ `Jovem`
  - `19` $\rightarrow$ `Jovem`
  - `20` $\rightarrow$ `Adulto`
  - `59` $\rightarrow$ `Adulto`
  - `60` $\rightarrow$ `Idoso`
  - `120` $\rightarrow$ `Idoso`
  - `-1` $\rightarrow$ `Idade Invalida`
  - `121` $\rightarrow$ `Idade Invalida`

### 6. `B09_C03.c` (Central telefônica com ramais)
- **Entradas:** `int setor, int ramal`.
- **Saídas:** Nome do departamento ou erro.
- **Casos:**
  - `1 1` $\rightarrow$ `Hardware`
  - `1 2` $\rightarrow$ `Software`
  - `1 3` $\rightarrow$ `Ramal Invalido`
  - `2 1` $\rightarrow$ `Contas a Pagar`
  - `2 2` $\rightarrow$ `Contas a Receber`
  - `2 0` $\rightarrow$ `Ramal Invalido`
  - `3 1` $\rightarrow$ `Setor Invalido`
