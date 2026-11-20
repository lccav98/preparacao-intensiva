# Especificação de Testes — Bloco `C04`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99** (`[DOC]` `Aula_00` p. 3; `Aula_10` p. 18).
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Critério de comparação e tolerância numérica:**
  - Comparação textual exata linha a linha após normalização de `\r\n` $\rightarrow$ `\n`.
  - Saídas inteiras devem ter coincidência exata; saídas reais (`%.2f`) tolerância numérica `0.01`.
  - Saídas `printf` estritamente em ASCII puro (sem acentos).
- **Checagem estática de não-antecipação:**
  - Proibido o uso de laço `for`.
  - Proibido o uso de `break` em laços ou `continue` (`break` permitido exclusivamente dentro de `switch`).
  - Proibido o uso de vetores (`char[]`, `int[]`, `v[i]`) ou funções customizadas além de `int main(void)`.
- **Casos de teste registrados:** 24 casos em [casos_C04.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/casos_C04.json).

---

## Casos de Teste por Programa

### 1. `C04_E02_corrigido.c` (Validação de Nota `[0, 10]` com `do-while`)
- **Entrada:** Sequência de inteiros até o primeiro valor no intervalo `[0, 10]`.
- **Saída:** `Nota invalida\n` para cada tentativa fora do intervalo, seguido de `Nota registrada: %d\n`.
- **Casos:**
  - `C04-E02-T1` (borda válido de primeira, limite inferior `0`): `0` $\rightarrow$ `Nota registrada: 0\n`.
  - `C04-E02-T2` (borda válido de primeira, limite superior `10`): `10` $\rightarrow$ `Nota registrada: 10\n`.
  - `C04-E02-T3` (normal válido direto): `8` $\rightarrow$ `Nota registrada: 8\n`.
  - `C04-E02-T4` (normal múltiplas tentativas inválidas): `-2 11 7` $\rightarrow$ `Nota invalida\nNota invalida\nNota registrada: 7\n`.

### 2. `C04_E03.c` (Validação de Divisor Não-Nulo com `do-while`)
- **Entrada:** `double numerador`, seguido de tentativas `double divisor` até `divisor != 0.0`.
- **Saída:** `Divisor invalido\n` para cada `0.0`, e `Resultado: %.2f\n`.
- **Casos:**
  - `C04-E03-T1` (normal válido na 1ª tentativa): `15.0 3.0` $\rightarrow$ `Resultado: 5.00\n`.
  - `C04-E03-T2` (borda divisor zero antes de válido): `10.0 0 0.0 4.0` $\rightarrow$ `Divisor invalido\nDivisor invalido\nResultado: 2.50\n`.
  - `C04-E03-T3` (borda numerador zero e divisor negativo): `0.0 -2.0` $\rightarrow$ `Resultado: -0.00\n` *(ou `0.00` — vamos usar `12.0 -3.0` para evitar sinal `-0.00` em C: `Resultado: -4.00\n`, e `0.0 5.0` $\rightarrow$ `Resultado: 0.00\n`)*.
  - `C04-E03-T4` (borda divisor negativo): `12.0 -3.0` $\rightarrow$ `Resultado: -4.00\n`.

### 3. `C04_E04.c` (Menu Interativo de Caixa Eletrônico com `do-while` + `switch`)
- **Entrada:** Opções `1` (depósito + valor), `2` (saque + valor), `3` (saldo), `0` (sair), ou inválidas.
- **Saída:** Mensagens conforme operação.
- **Casos:**
  - `C04-E04-T1` (borda sair imediato): `0` $\rightarrow$ `Encerrando\n`.
  - `C04-E04-T2` (normal depósito, consulta e saque): `1 50.0 3 2 30.0 0` $\rightarrow$ `Saldo: 150.00\nSaldo: 150.00\nSaldo: 120.00\nEncerrando\n`.
  - `C04-E04-T3` (borda saque igual ao saldo e saque maior que saldo): `2 100.0 2 1.0 0` $\rightarrow$ `Saldo: 0.00\nOperacao invalida\nEncerrando\n`.
  - `C04-E04-T4` (borda valor depósito negativo e opção inválida): `1 -10.0 9 0` $\rightarrow$ `Valor invalido\nOpcao invalida\nEncerrando\n`.

### 4. `C04_E05.c` (Menu Acumulador de Total com `do-while` + `switch`)
- **Entrada:** Opções `1` (+v), `2` (-v), `3` (zerar), `0` (sair), ou inválidas.
- **Saída:** `Total: %d\n`, `Opcao invalida\n`, `Final: %d\n`.
- **Casos:**
  - `C04-E05-T1` (borda sair imediato): `0` $\rightarrow$ `Final: 0\n`.
  - `C04-E05-T2` (normal somar, subtrair e opção inválida): `1 50 2 15 9 0` $\rightarrow$ `Total: 50\nTotal: 35\nOpcao invalida\nFinal: 35\n`.
  - `C04-E05-T3` (normal zerar acumulador e resultado negativo): `1 20 3 2 10 0` $\rightarrow$ `Total: 20\nTotal: 0\nTotal: -10\nFinal: -10\n`.
  - `C04-E05-T4` (extremo múltiplas operações): `1 100 1 200 2 50 3 1 7 0` $\rightarrow$ `Total: 100\nTotal: 300\nTotal: 250\nTotal: 0\nTotal: 7\nFinal: 7\n`.

### 5. `C04_C02_corrigido.c` (Menu Contador de Itens Corrigido)
- **Entrada:** Opções `1` (adicionar item), `0` (sair), ou inválidas.
- **Saída:** `Item adicionado\n`, `Opcao invalida\n`, `Total: %d\n`.
- **Casos:**
  - `C04-C02-T1` (borda sair imediato): `0` $\rightarrow$ `Total: 0\n`.
  - `C04-C02-T2` (normal sequência `1 0`): `1 0` $\rightarrow$ `Item adicionado\nTotal: 1\n`.
  - `C04-C02-T3` (normal com opções inválidas): `5 1 1 -2 1 0` $\rightarrow$ `Opcao invalida\nItem adicionado\nItem adicionado\nOpcao invalida\nItem adicionado\nTotal: 3\n`.

### 6. `C04_C03.c` (Menu Calculadora com Validação Interna de Divisor)
- **Entrada:** Opções `1` (a+b), `2` (a*b), `3` (a/b com validação `b != 0`), `0` (sair), ou inválidas.
- **Saída:** `Resultado: %d\n`, `Divisor invalido\n`, `Opcao invalida\n`, `Saindo\n`.
- **Casos:**
  - `C04-C03-T1` (borda sair imediato): `0` $\rightarrow$ `Saindo\n`.
  - `C04-C03-T2` (normal soma e produto): `1 7 5 2 4 6 0` $\rightarrow$ `Resultado: 12\nResultado: 24\nSaindo\n`.
  - `C04-C03-T3` (borda divisão com tentativas nulas): `3 20 0 0 4 0` $\rightarrow$ `Divisor invalido\nDivisor invalido\nResultado: 5\nSaindo\n`.
  - `C04-C03-T4` (normal opção inválida e divisão inteira com sinal): `8 3 -15 3 0` $\rightarrow$ `Opcao invalida\nResultado: -5\nSaindo\n`.
  - `C04-C03-T5` (extremo múltiplas operações encadeadas): `1 10 20 2 -3 4 3 100 0 25 0` $\rightarrow$ `Resultado: 30\nResultado: -12\nDivisor invalido\nResultado: 4\nSaindo\n`.
