# Especificação de Testes — Bloco `B08`

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

## Casos de Teste por Programa (`B08-E02`, `B08-E04`, `B08-E05`, `B08-C02` e `B08-C03`)

### 1. `B08_E02_corrigido.c` (Tarifas discretas por código)
- **Entradas:** `int tipo`.
- **Saídas:** `Tarifa A\n`, `Tarifa B\n` ou `Tarifa Padrao\n`.
- **Casos:**
  - `1` $\rightarrow$ `Tarifa A`
  - `2` $\rightarrow$ `Tarifa B`
  - `3` $\rightarrow$ `Tarifa Padrao`
  - `0` $\rightarrow$ `Tarifa Padrao`

### 2. `B08_E04.c` (Calculadora básica com operador `char`)
- **Entradas:** `double a, double b, char op`.
- **Saídas:** `Resultado: %.2f\n`, `Erro: Divisao por Zero\n` ou `Operador Invalido\n`.
- **Casos:**
  - `10.0 5.0 +` $\rightarrow$ `Resultado: 15.00`
  - `10.0 5.0 -` $\rightarrow$ `Resultado: 5.00`
  - `10.0 5.0 *` $\rightarrow$ `Resultado: 50.00`
  - `10.0 5.0 /` $\rightarrow$ `Resultado: 2.00`
  - `10.0 0.0 /` (divisão por zero) $\rightarrow$ `Erro: Divisao por Zero`
  - `10.0 5.0 %` (operador não suportado) $\rightarrow$ `Operador Invalido`

### 3. `B08_E05.c` (Conversor de dias da semana)
- **Entradas:** `int dia`.
- **Saídas:** Nome do dia em ASCII ou `Dia Invalido\n`.
- **Casos:**
  - `1` $\rightarrow$ `Domingo`
  - `2` $\rightarrow$ `Segunda`
  - `3` $\rightarrow$ `Terca`
  - `4` $\rightarrow$ `Quarta`
  - `5` $\rightarrow$ `Quinta`
  - `6` $\rightarrow$ `Sexta`
  - `7` $\rightarrow$ `Sabado`
  - `0` $\rightarrow$ `Dia Invalido`
  - `8` $\rightarrow$ `Dia Invalido`

### 4. `B08_C02_corrigido.c` (Menu bancário)
- **Entradas:** `int op`.
- **Saídas:** `Saldo\n`, `Extrato\n`, `Saque\n` ou `Opcao Invalida\n`.
- **Casos:**
  - `1` $\rightarrow$ `Saldo`
  - `2` $\rightarrow$ `Extrato`
  - `3` $\rightarrow$ `Saque`
  - `4` $\rightarrow$ `Opcao Invalida`
  - `0` $\rightarrow$ `Opcao Invalida`

### 5. `B08_C03.c` (Categorização de produtos de supermercado)
- **Entradas:** `int cod`.
- **Saídas:** Nome da categoria ou `Codigo Invalido\n`.
- **Casos:**
  - `1` $\rightarrow$ `Alimento Nao-Perecivel`
  - `3` $\rightarrow$ `Alimento Nao-Perecivel`
  - `4` $\rightarrow$ `Alimento Perecivel`
  - `6` $\rightarrow$ `Alimento Perecivel`
  - `7` $\rightarrow$ `Vestuario`
  - `8` $\rightarrow$ `Limpeza`
  - `10` $\rightarrow$ `Limpeza`
  - `0` $\rightarrow$ `Codigo Invalido`
  - `11` $\rightarrow$ `Codigo Invalido`
