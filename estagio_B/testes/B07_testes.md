# Especificação de Testes — Bloco `B07`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99** (`[DOC]` `Aula_00` p. 3; `Aula_10` p. 18).
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Critério de comparação:**
  - Comparação textual exata linha a linha após normalização de `\r\n` $\rightarrow$ `\n`.
  - Saídas formatadas com quebra de linha final `\n`.
- **Status de execução:**
  - Verificação de não-antecipação (ausência de `switch`, laços, vetores e funções extras).
  - Casos testados e validados contra os códigos C99 em `testes/solucoes/`.

---

## Casos de Teste por Programa (`B07-E03` a `B07-E06`, `B07-C02` e `B07-C03`)

### 1. `B07_E03_corrigido.c` (Controle de acesso à sala de servidores)
- **Entradas:** `int cracha, int biometria`.
- **Saídas:** `Acesso Liberado\n`, `Biometria Obrigatoria\n` ou `Cracha Invalido\n`.
- **Casos:**
  - `1 1` $\rightarrow$ `Acesso Liberado`
  - `1 0` (caso que falhava na associação errada do `else`) $\rightarrow$ `Biometria Obrigatoria`
  - `0 1` $\rightarrow$ `Cracha Invalido`
  - `0 0` $\rightarrow$ `Cracha Invalido`

### 2. `B07_E04.c` (Classificação hierárquica de triângulos)
- **Entradas:** `double a, b, c`.
- **Saídas:** `Equilatero\n`, `Isosceles\n`, `Escaleno\n` ou `Nao Forma Triangulo\n`.
- **Casos:**
  - `5.0 5.0 5.0` (todos iguais) $\rightarrow$ `Equilatero`
  - `5.0 5.0 8.0` (dois iguais válidos) $\rightarrow$ `Isosceles`
  - `3.0 4.0 5.0` (três distintos válidos) $\rightarrow$ `Escaleno`
  - `1.0 2.0 10.0` (não fecha polígono) $\rightarrow$ `Nao Forma Triangulo`
  - `2.0 3.0 5.0` (degenerado: $2+3=5$) $\rightarrow$ `Nao Forma Triangulo`

### 3. `B07_E05.c` (Sistema acadêmico com prioridade à frequência)
- **Entradas:** `int freq, double nota`.
- **Saídas:** `Reprovado por Falta\n`, `Aprovado\n`, `Exame Final\n` ou `Reprovado por Nota\n`.
- **Casos:**
  - `70 9.5` (falta reprova direto mesmo com nota 9.5) $\rightarrow$ `Reprovado por Falta`
  - `75 7.0` (fronteiras exatas de aprovação) $\rightarrow$ `Aprovado`
  - `80 6.9` (nota em exame final) $\rightarrow$ `Exame Final`
  - `80 4.0` (fronteira inferior de exame) $\rightarrow$ `Exame Final`
  - `80 3.9` (nota insuficiente para exame) $\rightarrow$ `Reprovado por Nota`
  - `74 10.0` (falta absoluta) $\rightarrow$ `Reprovado por Falta`

### 4. `B07_E06.c` (Crédito habitacional)
- **Entradas:** `double renda_mensal, double valor_parcela, int restricoes_spc`.
- **Saídas:** `Credito Recusado: Restricao Cadastral\n`, `Credito Recusado: Parcela Excede Margem\n` ou `Credito Aprovado\n`.
- **Casos:**
  - `5000.00 1200.00 0` (24% da renda, sem restrição) $\rightarrow$ `Credito Aprovado`
  - `5000.00 1500.00 0` (exatamente 30% da renda) $\rightarrow$ `Credito Aprovado`
  - `5000.00 1500.01 0` (ultrapassa margem) $\rightarrow$ `Credito Recusado: Parcela Excede Margem`
  - `10000.00 1000.00 1` (restrição cadastral bloqueia imediatamente) $\rightarrow$ `Credito Recusado: Restricao Cadastral`

### 5. `B07_C02_corrigido.c` (Classificação com validação de existência)
- **Entradas:** `double a, b, c`.
- **Saídas:** `Equilatero\n`, `Isosceles\n`, `Escaleno\n` ou `Nao Forma Triangulo\n`.
- **Casos:**
  - `6.0 6.0 6.0` $\rightarrow$ `Equilatero`
  - `7.0 7.0 4.0` $\rightarrow$ `Isosceles`
  - `6.0 8.0 10.0` $\rightarrow$ `Escaleno`
  - `1.0 2.0 10.0` (armadilha clássica: seria escaleno se não testasse existência) $\rightarrow$ `Nao Forma Triangulo`
  - `3.0 3.0 8.0` (dois lados iguais mas $3+3 < 8$) $\rightarrow$ `Nao Forma Triangulo`

### 6. `B07_C03.c` (Triagem de doação de sangue)
- **Entradas:** `int idade, double peso, int jejum_horas`.
- **Saídas:** `Impedimento: Idade Fora da Faixa\n`, `Impedimento: Peso Insuficiente\n`, `Impedimento: Jejum Inadequado\n` ou `Apto para Doacao\n`.
- **Casos:**
  - `25 65.0 4` (apto pleno) $\rightarrow$ `Apto para Doacao`
  - `15 70.0 4` (idade menor que 16) $\rightarrow$ `Impedimento: Idade Fora da Faixa`
  - `70 70.0 4` (idade maior que 69) $\rightarrow$ `Impedimento: Idade Fora da Faixa`
  - `25 49.9 4` (peso menor que 50.0 kg) $\rightarrow$ `Impedimento: Peso Insuficiente`
  - `25 65.0 1` (jejum menor que 2 horas) $\rightarrow$ `Impedimento: Jejum Inadequado`
  - `25 65.0 13` (jejum excessivo acima de 12 horas) $\rightarrow$ `Impedimento: Jejum Inadequado`
  - `16 50.0 2` (fronteiras mínimas válidas) $\rightarrow$ `Apto para Doacao`
  - `69 50.0 12` (fronteiras máximas válidas) $\rightarrow$ `Apto para Doacao`
