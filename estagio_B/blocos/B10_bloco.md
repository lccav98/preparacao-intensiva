# Bloco `B10` — Revisão e Consolidação do Estágio B *(Bloco de Revisão)*

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio B — Expressões, Operadores e Estruturas Condicionais / **`B10`** |
| **Micro-habilidade foco** | Integrar expressões aritméticas, operadores relacionais e lógicos, tabela-verdade e todas as estruturas de desvio (`if / else`, `else if`, aninhamento e `switch`) na resolução de problemas complexos com casos de borda exatos. |
| **Pré-requisitos** | `B01` a `B09` *(Conclusão integral dos blocos anteriores do Estágio B)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 22 min):** `14 min` resol. \| `5 min` corr. \| `3 min` recup.; **Sessão 2 (`E04`–`E06`, 22 min):** `14 min` resol. \| `5 min` corr. \| `3 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Conteúdo novo: NENHUM.** **É terminantemente proibido** o uso de laços (`while`, `for`, `do-while`), vetores ou cadeias de caracteres (`char[]`), ou funções além de `main`. Use estritamente C99 com saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Apto para Estágio C`)

---

## 1. Instruções Curtas (Matriz de Decisão do Estágio B)

1. **Escolha da Estrutura Condicional Adequada:**
   - **`if` Simples:** Para ações condicionais independentes (filtros ou correções pontuais).
   - **`if / else`:** Para bifurcações binárias exclusivas (ou faz A, ou faz B).
   - **Cadeia `if / else if / else`:** Para faixas numéricas contínuas ou intervalos com operadores relacionais (`<`, `<=`, `>`, `>=`), testando sempre do extremo mais restritivo para o mais geral.
   - **`if` Aninhado:** Para decisões hierárquicas dependentes (onde a 2ª pergunta só tem sentido se a 1ª for verdadeira, como validar existência antes de classificar).
   - **`switch / case`:** Para seleções discretas baseadas em valores pontuais inteiros ou caracteres (`int` ou `char`), usando `break` em todos os ramos ou agrupando *cases* intencionalmente por *fall-through*.
2. **Precedência e Defensividade:**
   - Ordem global: `( )` e `!` unário $\rightarrow$ `* / %` $\rightarrow$ `+ -` $\rightarrow$ `< <= > >=` $\rightarrow$ `== !=` $\rightarrow$ `&&` $\rightarrow$ `||` $\rightarrow$ `=`.
   - Use parênteses defensivos sempre que misturar aritmética com testes relacionais ou `&&` com `||`.
   - Lembre-se: em C, `a <= x <= b` é um bug grave! Escreva sempre `x >= a && x <= b`.
3. **Robustez em Fronteiras Contínuas:**
   - Use variáveis do tipo `double` (com `%lf` no `scanf` e `%.2f` no `printf`) para valores monetários e decimais, evitando lacunas e erros de arredondamento de `float`.
   - Garanta cobertura completa de fronteiras (ex.: `< 100.0` seguido de `<= 200.0`), sem deixar brechas abertas entre limites.

---

## 2. Exemplos Guiados de Integração

### Exemplo 1 — Rastreamento Integrado: Expressões, Lógica e Dangling Else
Considere o seguinte trecho com `int a = 14, b = 3, c = 0;`:

```c
int res = (a % b == 2) && (a / b > 3 || !c);

if (res) {
    if (b > a) {
        printf("Ramo 1\n");
    } else {
        printf("Ramo 2\n");
    }
} else {
    printf("Ramo 3\n");
}
```
**Passo a passo:**
1. `a % b` $\rightarrow$ `14 % 3` é `2`. Logo, `2 == 2` é `1` (verdadeiro).
2. Como o primeiro termo do `&&` é `1`, avalia o lado direito:
   - `a / b` $\rightarrow$ `14 / 3` é `4` (divisão inteira). `4 > 3` é `1` (verdadeiro).
   - Por curto-circuito no `||`, `!c` nem precisa ser avaliado! O parênteses da direita resulta em `1`.
3. `1 && 1` $\rightarrow$ `res = 1`.
4. O `if (res)` entra no bloco interno. Avalia `b > a` $\rightarrow$ `3 > 14`, que é falso (`0`).
5. Cai no `else` interno e imprime: **`Ramo 2\n`**.

---

## 3. Exercícios (`B10-E01` a `B10-E06`)

### Sessão 1 (`B10-E01` a `B10-E03` — Rastreio e Depuração Integrados)

### `B10-E01` *(Teste de Mesa Integrador)*
Sem utilizar computador, determine o valor final das variáveis e a saída exata impressa para o trecho abaixo:

```c
int x = 15, y = 4, z = 2;
int cond1, cond2;

cond1 = (x / y == 3) && (x % y != 0);
cond2 = !(z > y) || (x + y * z > 25);

if (cond1) {
    if (cond2) {
        printf("A-%d\n", x % z);
    } else {
        printf("B-%d\n", y / z);
    }
} else {
    printf("C\n");
}
```
1. Qual é o valor de `cond1` (`0` ou `1`)?
2. Qual é o valor de `cond2` (`0` ou `1`)?
3. Qual linha exata é impressa pelo `printf`?

---

### `B10-E02` *(Caça ao Bug — Precisão de Fronteiras e Lacunas)*
O programa abaixo deveria calcular o imposto sobre o lucro de uma empresa:
- até `10000.00`: isento (`0%`)
- de `10000.00` até `25000.00`: `10%` sobre o total
- acima de `25000.00`: `15%` sobre o total

```c
#include <stdio.h>

int main(void) {
    float lucro, imposto;
    scanf("%f", &lucro);

    /* CODIGO COM BUGS DE TIPO E LACUNA DE FRONTEIRA */
    if (lucro < 10000.0) {
        imposto = 0.0f;
    } else if (lucro >= 10000.0 && lucro <= 24999.99) {
        imposto = lucro * 0.10f;
    } else {
        imposto = lucro * 0.15f;
    }

    printf("Imposto: R$ %.2f\n", imposto);
    return 0;
}
```
1. Identifique os **2 problemas** no código (um relativo à precisão do tipo `float` e outro relativo à lacuna entre `24999.99` e `25000.00`).
2. Escreva a versão corrigida completa em C usando `double` e faixas sem lacunas ([B10_E02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B10_E02_corrigido.c)).

---

### `B10-E03` *(Teste de Mesa — Switch com Fall-Through e Aritmética Modular)*
Considere o código:

```c
int num = 17;
int chave = (num % 5); /* 17 % 5 = 2 */

switch (chave) {
    case 1:
        printf("Um ");
        break;
    case 2:
        printf("Dois ");
        /* Sem break */
    case 3:
        printf("Tres ");
        break;
    case 4:
        printf("Quatro ");
        break;
    default:
        printf("Outro ");
        break;
}
printf("\n");
```
1. Qual será a saída para `num = 17`?
2. Qual será a saída para `num = 20`?
3. Qual será a saída para `num = 14`?

---

### Sessão 2 (`B10-E04` a `B10-E06` — Programas Completos Integradores da Lista2/Lista3 UTFPR)

### `B10-E04` *(Programa completo — Resolução da Equação do 2º Grau / Bhaskara)*
Escreva um **programa completo** em C que leia os coeficientes reais `a`, `b` e `c` de uma equação quadrática ($ax^2 + bx + c = 0$): `scanf("%lf %lf %lf", &a, &b, &c);`.
Regras estritas:
1. Se `a == 0.0`, a equação não é do segundo grau: imprima `Nao e equacao de segundo grau\n`.
2. Se `a != 0.0`, calcule o discriminante $\Delta = b^2 - 4ac$:
   - Se $\Delta < 0.0$: imprima `Sem raizes reais\n`
   - Se $\Delta == 0.0$: calcule a raiz única $x = -b / (2a)$ e imprima `Raiz unica: %.2f\n`
   - Se $\Delta > 0.0$: calcule as duas raízes reais usando a função `sqrt` de `<math.h>`:
     $$x_1 = \frac{-b + \sqrt{\Delta}}{2a}, \quad x_2 = \frac{-b - \sqrt{\Delta}}{2a}$$
     Imprima exatamente: `Raizes: %.2f e %.2f\n` (exibindo $x_1$ e $x_2$ com 2 casas decimais).

Arquivo correspondente: [B10_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B10_E04.c).

---

### `B10-E05` *(Programa completo — Validação de Calendário e Ano Bissexto)*
Escreva um **programa completo** em C que leia três números inteiros: `dia`, `mes` e `ano` (`scanf("%d %d %d", &dia, &mes, &ano);`).
O programa deve validar a data considerando as regras astronômicas de ano bissexto:
- Um ano é **bissexto** se: for divisível por 4 e não for divisível por 100, OU se for divisível por 400.
- Regras de validação:
  - O ano deve ser positivo (`ano > 0`).
  - O mês deve estar entre 1 e 12 (`mes >= 1 && mes <= 12`).
  - Dias válidos:
    - Meses 1, 3, 5, 7, 8, 10, 12: de 1 a 31 dias.
    - Meses 4, 6, 9, 11: de 1 a 30 dias.
    - Mês 2 (Fevereiro): de 1 a 29 dias se o ano for bissexto; de 1 a 28 dias se o ano não for bissexto.
- Se a data for válida:
  - Se o ano for bissexto, imprima: `Data Valida: Bissexto\n`
  - Se o ano não for bissexto, imprima: `Data Valida: Nao Bissexto\n`
- Se qualquer dado for inconsistente, imprima: `Data Invalida\n`

Arquivo correspondente: [B10_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B10_E05.c).

---

### `B10-E06` *(Programa completo — Fatura de Energia Elétrica por Categoria)*
Escreva um **programa completo** em C que leia o tipo de instalação (`int tipo`) e o consumo mensal em kWh (`double kwh`): `scanf("%d %lf", &tipo, &kwh);`.
Validação inicial:
- Se `kwh < 0.0`, imprima: `Consumo Invalido\n`
- Se `kwh >= 0.0`, calcule o valor da conta usando `switch (tipo)`:
  - **Tipo 1 (Residencial):**
    - até `100.0` kWh: tarifa de `R$ 0.60` por kWh (`kwh * 0.60`);
    - acima de `100.0` kWh: valor base de `R$ 60.00` mais `R$ 0.85` por kWh excedente acima de 100.
    - Imprima: `Fatura Residencial: R$ %.2f\n`
  - **Tipo 2 (Comercial):**
    - até `200.0` kWh: tarifa de `R$ 0.75` por kWh;
    - acima de `200.0` kWh: valor base de `R$ 150.00` mais `R$ 0.95` por kWh excedente acima de 200.
    - Imprima: `Fatura Comercial: R$ %.2f\n`
  - **Tipo 3 (Industrial):**
    - taxa fixa de demanda de `R$ 300.00` mais `R$ 0.50` por todo kWh consumido (`300.00 + kwh * 0.50`).
    - Imprima: `Fatura Industrial: R$ %.2f\n`
  - **Qualquer outro tipo (`default`):**
    - Imprima: `Tipo Invalido\n`

Arquivo correspondente: [B10_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B10_E06.c).

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `B10-C01` *(Teste de Mesa Integrador)*
Considere o trecho com `int a = 10, b = 20, c = 5;`:

```c
int r1 = (a < b) && (b / c == 4);
int r2 = !(a + c == 15) || (b % c == 0);

if (r1 && r2) {
    if (b - a > c) {
        printf("Resultado Alpha\n");
    } else {
        printf("Resultado Beta\n");
    }
} else {
    printf("Resultado Gama\n");
}
```
1. Qual é o valor de `r1` (`0` ou `1`)?
2. Qual é o valor de `r2` (`0` ou `1`)?
3. Qual texto exato será impresso?

---

### `B10-C02` *(Programa completo — Triângulo, Classificação e Área de Heron)*
Escreva um programa completo em C que leia os três lados de um triângulo (`double a, b, c`).
1. Valide a existência do triângulo ($a < b + c$ e $b < a + c$ e $c < a + b$). Se não formar triângulo, imprima: `Invalido\n`.
2. Se formar triângulo:
   - Calcule o semiperímetro $s = (a + b + c) / 2.0$.
   - Calcule a área pela fórmula de Heron: $\text{area} = \sqrt{s(s - a)(s - b)(s - c)}$ (usando `sqrt` de `<math.h>`).
   - Classifique o triângulo:
     - Se $a = b$ e $b = c$: imprima `Equilatero - Area: %.2f\n`
     - Se $a = b$ ou $a = c$ ou $b = c$: imprima `Isosceles - Area: %.2f\n`
     - Se todos os lados forem distintos: imprima `Escaleno - Area: %.2f\n`

Arquivo correspondente: [B10_C02.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B10_C02.c).

---

### `B10-C03` *(Programa completo — Cálculo Salarial com INSS e IRRF)*
Escreva um programa completo em C que calcule o salário líquido a partir do salário bruto e número de dependentes (`double salario_bruto; int dependentes;` lidos via `scanf("%lf %d", &salario_bruto, &dependentes);`).
Regras:
1. Se `salario_bruto <= 0.0` ou `dependentes < 0`: imprima `Entrada Invalida\n`.
2. Se os dados forem válidos:
   - **Desconto do INSS:**
     - até `R$ 1412.00`: `7.5%` do salário bruto (`salario_bruto * 0.075`)
     - acima de `1412.00` até `2666.00`: `9.0%` do salário bruto (`salario_bruto * 0.09`)
     - acima de `2666.00` até `4000.00`: `12.0%` do salário bruto (`salario_bruto * 0.12`)
     - acima de `4000.00`: teto fixo de `R$ 550.00`
   - **Base de Cálculo do IRRF:**
     - $\text{base} = \text{salario\_bruto} - \text{inss} - (\text{dependentes} \times 189.59)$
     - Se $\text{base} < 0.0$, ajuste $\text{base} = 0.0$.
   - **Desconto do IRRF:**
     - $\text{base} \le 2259.20$: `R$ 0.00` (isento)
     - acima de `2259.20` até `2826.65`: `7.5%` sobre a base (`base * 0.075`)
     - acima de `2826.65` até `3751.05`: `15.0%` sobre a base (`base * 0.15`)
     - acima de `3751.05`: `22.5%` sobre a base (`base * 0.225`)
   - **Salário Líquido:**
     - $\text{salario\_liquido} = \text{salario\_bruto} - \text{inss} - \text{irrf}$
   - Imprima exatamente 3 linhas:
     ```text
     INSS: R$ %.2f
     IRRF: R$ %.2f
     Liquido: R$ %.2f
     ```

Arquivo correspondente: [B10_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B10_C03.c).

---

## 5. Orientação de Avanço ou Recuperação (Conclusão do Estágio B)

- **Avançar para o Estágio C (`Estruturas de Repetição - while`):** somente após autocorreção dos exercícios `B10-E01..E06` **e** **100% (3/3)** na Checagem Independente `B10-C01..C03` sem consulta ao gabarito.
- **Recuperação Geral:** se o aluno falhar na checagem independente, analisar qual módulo falhou:
  - Falha em Bhaskara / Heron $\rightarrow$ revisar **`B01`** e **`B02`** (expressões e parênteses).
  - Falha em Bissexto / Triângulos $\rightarrow$ revisar **`B06`** (`&&`/`||`) e **`B07`** (aninhamento).
  - Falha em Faturas / Menus $\rightarrow$ revisar **`B05`** (`else if`) e **`B08`** (`switch`).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 1–2 (itens 5 e 6).
- `[DOC]` `Aula_05` a `Aula_08_v2` (tópicos integrais de expressões, condicionais e seleção múltipla).
- `[DOC]` `Lista1_Algoritmos.pdf` p. 1–2 (Bhaskara).
- `[DOC]` `Lista2_Algoritmos.pdf` p. 2–4 (Triângulos, calendário e validações complexas).
- `[DOC]` `Lista3_Algoritmos.pdf` p. 1–2 (Menus de faturas e opções).
- `[DOC]` `Lista8_Algoritmos_Revisao.pdf` p. 1 (Ex. 2 — integração condicional).
- Casos de teste e soluções verificáveis: [B10_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/gabaritos/B10_gabarito.md) e [B10_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/B10_testes.md).
