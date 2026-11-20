# Especificação de Testes — Bloco `B10`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99** (`[DOC]` `Aula_00` p. 3; `Aula_10` p. 18).
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -lm -o programa
  ```
- **Critério de comparação e tolerância numérica:**
  - Comparação textual exata linha a linha após normalização de `\r\n` $\rightarrow$ `\n`.
  - Tolerância de `0.01` em valores de ponto flutuante formatados com `%.2f`.
- **Status de execução:**
  - Verificação de não-antecipação (ausência total de laços, vetores e funções extras).
  - Casos testados e validados contra os códigos C99 em `testes/solucoes/`.

---

## Casos de Teste por Programa (`B10-E02`, `B10-E04` a `B10-E06`, `B10-C02` e `B10-C03`)

### 1. `B10_E02_corrigido.c` (Tributação sobre lucros)
- **Entradas:** `double lucro`.
- **Saídas:** `Imposto: R$ %.2f\n`.
- **Casos:**
  - `5000.00` $\rightarrow$ `Imposto: R$ 0.00`
  - `9999.99` $\rightarrow$ `Imposto: R$ 0.00`
  - `10000.00` $\rightarrow$ `Imposto: R$ 1000.00`
  - `24999.995` (caso que falhava na lacuna) $\rightarrow$ `Imposto: R$ 2500.00`
  - `25000.00` $\rightarrow$ `Imposto: R$ 2500.00`
  - `30000.00` $\rightarrow$ `Imposto: R$ 4500.00`

### 2. `B10_E04.c` (Equação do 2º Grau / Bhaskara)
- **Entradas:** `double a, double b, double c`.
- **Saídas:** `Raizes: %.2f e %.2f\n`, `Raiz unica: %.2f\n`, `Sem raizes reais\n` ou `Nao e equacao de segundo grau\n`.
- **Casos:**
  - `0.0 2.0 4.0` (não é segundo grau) $\rightarrow$ `Nao e equacao de segundo grau`
  - `1.0 -5.0 6.0` ($\Delta = 1 > 0$, raízes 3.00 e 2.00) $\rightarrow$ `Raizes: 3.00 e 2.00`
  - `1.0 -4.0 4.0` ($\Delta = 0$, raiz única 2.00) $\rightarrow$ `Raiz unica: 2.00`
  - `1.0 1.0 1.0` ($\Delta = -3 < 0$, sem raízes reais) $\rightarrow$ `Sem raizes reais`
  - `2.0 -10.0 8.0` ($\Delta = 36$, raízes 4.00 e 1.00) $\rightarrow$ `Raizes: 4.00 e 1.00`

### 3. `B10_E05.c` (Calendário astronômico e ano bissexto)
- **Entradas:** `int dia, int mes, int ano`.
- **Saídas:** `Data Valida: Bissexto\n`, `Data Valida: Nao Bissexto\n` ou `Data Invalida\n`.
- **Casos:**
  - `29 2 2024` (ano bissexto regular) $\rightarrow$ `Data Valida: Bissexto`
  - `29 2 1900` (ano secular não divisível por 400) $\rightarrow$ `Data Invalida`
  - `29 2 2000` (ano secular divisível por 400) $\rightarrow$ `Data Valida: Bissexto`
  - `28 2 2023` (ano comum) $\rightarrow$ `Data Valida: Nao Bissexto`
  - `31 4 2023` (abril tem 30 dias) $\rightarrow$ `Data Invalida`
  - `30 4 2023` (abril válido) $\rightarrow$ `Data Valida: Nao Bissexto`
  - `15 13 2024` (mês 13) $\rightarrow$ `Data Invalida`
  - `10 5 -5` (ano negativo) $\rightarrow$ `Data Invalida`

### 4. `B10_E06.c` (Tarifas de energia por categoria)
- **Entradas:** `int tipo, double kwh`.
- **Saídas:** Fatura da categoria ou erro.
- **Casos:**
  - `1 80.0` (residencial dentro do limite) $\rightarrow$ `Fatura Residencial: R$ 48.00`
  - `1 100.0` (residencial fronteira) $\rightarrow$ `Fatura Residencial: R$ 60.00`
  - `1 150.0` (residencial com excedente) $\rightarrow$ `Fatura Residencial: R$ 102.50`
  - `2 150.0` (comercial dentro do limite) $\rightarrow$ `Fatura Comercial: R$ 112.50`
  - `2 200.0` (comercial fronteira) $\rightarrow$ `Fatura Comercial: R$ 150.00`
  - `2 250.0` (comercial excedente) $\rightarrow$ `Fatura Comercial: R$ 197.50`
  - `3 1000.0` (industrial) $\rightarrow$ `Fatura Industrial: R$ 800.00`
  - `1 -10.0` (consumo negativo) $\rightarrow$ `Consumo Invalido`
  - `4 100.0` (tipo inexistente) $\rightarrow$ `Tipo Invalido`

### 5. `B10_C02.c` (Triângulo, classificação e área de Heron)
- **Entradas:** `double a, double b, double c`.
- **Saídas:** `<Tipo> - Area: %.2f\n` ou `Invalido\n`.
- **Casos:**
  - `3.0 4.0 5.0` $\rightarrow$ `Escaleno - Area: 6.00`
  - `6.0 6.0 6.0` $\rightarrow$ `Equilatero - Area: 15.59`
  - `5.0 5.0 6.0` $\rightarrow$ `Isosceles - Area: 12.00`
  - `1.0 2.0 10.0` $\rightarrow$ `Invalido`

### 6. `B10_C03.c` (Folha de pagamento com INSS e IRRF)
- **Entradas:** `double salario_bruto, int dependentes`.
- **Saídas:** Três linhas formatadas ou `Entrada Invalida\n`.
- **Casos:**
  - `1412.00 0` $\rightarrow$ `INSS: R$ 105.90\nIRRF: R$ 0.00\nLiquido: R$ 1306.10`
  - `2500.00 1` $\rightarrow$ `INSS: R$ 225.00\nIRRF: R$ 0.00\nLiquido: R$ 2275.00`
  - `3500.00 0` $\rightarrow$ `INSS: R$ 420.00\nIRRF: R$ 462.00\nLiquido: R$ 2618.00`
  - `5000.00 2` $\rightarrow$ `INSS: R$ 550.00\nIRRF: R$ 915.93\nLiquido: R$ 3534.07`
  - `-100.00 0` $\rightarrow$ `Entrada Invalida`
