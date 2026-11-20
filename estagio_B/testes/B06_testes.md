# Especificação de Testes — Bloco `B06`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99** (`[DOC]` `Aula_00` p. 3; `Aula_10` p. 18).
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Critério de comparação:**
  - Comparação textual exata linha a linha após normalização de `\r\n` $\rightarrow$ `\n`.
  - Saídas formatadas com quebra de linha final `\n`.
- **Status de execução:**
  - Verificação de não-antecipação (ausência total de laços `while`/`for`/`do-while`, vetores/strings `char[]` e funções adicionais).
  - Todos os casos testados e validados contra os códigos C99 em `testes/solucoes/`.

---

## Casos de Teste por Programa (`B06-E03` a `B06-E06`, `B06-C02` a `B06-C04`)

### 1. `B06_E03_corrigido.c` (Faixa de idade para concurso)
- **Entradas:** `int idade`.
- **Saídas:** `Apto\n` ou `Inapto\n`.
- **Casos:**
  - `17` (borda inferior fora) $\rightarrow$ `Inapto`
  - `18` (fronteira exata inferior) $\rightarrow$ `Apto`
  - `25` (caso normal interno) $\rightarrow$ `Apto`
  - `35` (fronteira exata superior) $\rightarrow$ `Apto`
  - `36` (borda superior fora) $\rightarrow$ `Inapto`
  - `50` (caso clássico que falhava no bug `18 <= idade <= 35`) $\rightarrow$ `Inapto`

### 2. `B06_E04.c` (Montanha-russa do parque)
- **Entradas:** `double alt` e `int idade`.
- **Saídas:** `Acesso Permitido\n` ou `Acesso Negado\n`.
- **Casos:**
  - `1.50 12` (fronteiras exatas regra 1) $\rightarrow$ `Acesso Permitido`
  - `1.49 12` (altura insuficiente para regra 1) $\rightarrow$ `Acesso Negado`
  - `1.55 11` (idade insuficiente para regra 1) $\rightarrow$ `Acesso Negado`
  - `1.40 16` (fronteiras exatas regra 2) $\rightarrow$ `Acesso Permitido`
  - `1.39 17` (altura insuficiente para regra 2) $\rightarrow$ `Acesso Negado`
  - `1.75 25` (caso pleno dentro de ambas as regras) $\rightarrow$ `Acesso Permitido`

### 3. `B06_E05.c` (Condição de existência de triângulo)
- **Entradas:** `double a, b, c`.
- **Saídas:** `Triangulo Valido\n` ou `Triangulo Invalido\n`.
- **Casos:**
  - `3.0 4.0 5.0` (triângulo retângulo clássico) $\rightarrow$ `Triangulo Valido`
  - `5.0 5.0 5.0` (equilátero) $\rightarrow$ `Triangulo Valido`
  - `1.0 2.0 3.0` (degenerado: soma de dois é igual ao terceiro) $\rightarrow$ `Triangulo Invalido`
  - `10.0 2.0 3.0` (comprimento excessivo de um lado) $\rightarrow$ `Triangulo Invalido`
  - `5.0 12.0 13.0` (triângulo escaleno válido) $\rightarrow$ `Triangulo Valido`

### 4. `B06_E06.c` (Concessão de empréstimo bancário)
- **Entradas:** `int idade, double renda, int correntista`.
- **Saídas:** `Emprestimo Aprovado\n` ou `Emprestimo Negado\n`.
- **Casos:**
  - `21 2500.00 0` (fronteira exata cliente comum) $\rightarrow$ `Emprestimo Aprovado`
  - `20 3000.00 0` (idade insuficiente para cliente comum) $\rightarrow$ `Emprestimo Negado`
  - `65 2500.00 0` (idade limite máxima comum) $\rightarrow$ `Emprestimo Aprovado`
  - `66 5000.00 0` (idade além do limite comum) $\rightarrow$ `Emprestimo Negado`
  - `18 1500.00 1` (fronteiras exatas cliente especial VIP) $\rightarrow$ `Emprestimo Aprovado`
  - `17 2000.00 1` (idade insuficiente mesmo sendo VIP) $\rightarrow$ `Emprestimo Negado`
  - `30 1499.00 1` (renda insuficiente para VIP) $\rightarrow$ `Emprestimo Negado`

### 5. `B06_C02_corrigido.c` (Aprovação por nota e frequência)
- **Entradas:** `double nota, int freq`.
- **Saídas:** `Aprovado\n` ou `Reprovado\n`.
- **Casos:**
  - `6.0 75` (fronteiras exatas de aprovação) $\rightarrow$ `Aprovado`
  - `5.9 80` (nota abaixo da mínima) $\rightarrow$ `Reprovado`
  - `2.0 80` (caso clássico que falhava no bug) $\rightarrow$ `Reprovado`
  - `8.5 74` (frequência insuficiente) $\rightarrow$ `Reprovado`
  - `10.0 100` (valores máximos) $\rightarrow$ `Aprovado`

### 6. `B06_C03.c` (Validação de data)
- **Entradas:** `int dia, int mes`.
- **Saídas:** `Data Valida\n` ou `Data Invalida\n`.
- **Casos:**
  - `28 2` (fevereiro borda máxima ano comum) $\rightarrow$ `Data Valida`
  - `29 2` (fevereiro além do limite em ano comum) $\rightarrow$ `Data Invalida`
  - `30 4` (abril borda de 30 dias) $\rightarrow$ `Data Valida`
  - `31 4` (abril com 31 dias inválido) $\rightarrow$ `Data Invalida`
  - `31 12` (dezembro borda de 31 dias) $\rightarrow$ `Data Valida`
  - `0 5` (dia zero inexistente) $\rightarrow$ `Data Invalida`
  - `15 13` (mês 13 inexistente) $\rightarrow$ `Data Invalida`

### 7. `B06_C04.c` (Bolsa de Iniciação Científica)
- **Entradas:** `double cra, double renda`.
- **Saídas:** `Bolsa Concedida\n` ou `Bolsa Nao Concedida\n`.
- **Casos:**
  - `8.5 1800.00` (fronteiras exatas regra 1) $\rightarrow$ `Bolsa Concedida`
  - `8.4 1500.00` (CRA abaixo da regra 1) $\rightarrow$ `Bolsa Nao Concedida`
  - `9.0 1800.01` (renda acima da regra 1) $\rightarrow$ `Bolsa Nao Concedida`
  - `9.5 5000.00` (mérito excepcional independente de renda) $\rightarrow$ `Bolsa Concedida`
  - `9.4 3000.00` (CRA abaixo de 9.5 e renda alta) $\rightarrow$ `Bolsa Nao Concedida`
