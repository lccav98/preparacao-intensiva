# Bloco `A10` — Revisão e Consolidação do Estágio A *(Bloco de Revisão)*

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio A — Fundamentos, Ambiente C, Variáveis e Representação / **`A10` *(Bloco de Revisão)*** |
| **Micro-habilidade foco** | Integrar conceitos fundamentais de algoritmos, compilação C99 no GCC, identificadores, constantes, E/S formatada, atribuição/troca em memória e representação numérica (`A01`–`A09`), sem conteúdo novo. |
| **Pré-requisitos** | `A07` *(Atribuição, memória e troca com `aux`)* e `A09` *(Tamanhos de tipos, `sizeof` e precisão `float` vs `double`)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 20 min):** `14 min` resol. \| `6 min` corr.; **Sessão 2 (`E04`–`E05`, 20 min):** `13 min` resol. \| `4 min` corr. \| `3 min` recup.; **Checagem (`C01`–`C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** todo o repertório de `A01`–`A09` + operações lineares `+`, `-`, `*` em `double` (cálculo de área/perímetro de terreno, salário fixo + comissão `0.05 * vendas` e troca com `aux`). **Não utilize** divisão `/`, resto `%`, `if`, `switch`, laços, vetores, funções além de `main` ou `<math.h>`. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E05`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 2` | **Após corr.:** `___ / 2`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

*(Bloco de revisão integrada: nenhum tópico inédito é introduzido.)*

1. **Sintaxe mínima C99 (`A02`–`A05`):** `#include <stdio.h>`, `int main(void)`, `return 0;`, `;` após comandos, diferenciação maiúsculas/minúsculas (*case-sensitive*), identificadores válidos (sem iniciar com dígito, sem espaços/especiais além de `_`, sem palavras reservadas), escapes (`\n`, `\t`, `\"`, `\\`, `%%`) e constantes (`#define NOME valor` **sem** `;` vs `const tipo NOME = valor;` **com** tipo e `;`).
2. **Entrada e Saída (`A05`–`A06`):** No `scanf`, use `&` antes da variável e especificador compatível (`%d`, `%f`, **`%lf` obrigatório para `double`**, `" %c"` para caractere); no `printf`, formate reais com `%.2f` (saídas estritamente ASCII, sem acentos e com ponto `.`).
3. **Memória e Troca (`A07`):** Em `v = expr;`, primeiro avalia-se a direita e depois sobrescreve-se `v`. Trocar duas variáveis exige variável auxiliar `aux` do mesmo tipo (`aux = a; a = b; b = aux;`).
4. **Representação Numérica (`A08`–`A09`):** $n$ bits representam $2^n$ valores; $T$ valores exigem $\lceil \log_2 T \rceil$ bits; `sizeof` usa `%zu`; prefira `double` (8 bytes) ao `float` (4 bytes) em cálculos reais.
5. **Expressões de revisão (`A10`):** Use apenas `+`, `-` e `*` sobre `double` (não use `/`, `%` nem `<math.h>`).

---

## 2. Exemplos Guiados

### Exemplo 1 — Rastreamento misto (Memória + Sistema Binário) *(Trecho ilustrativo)*
- **(a) Memória:** Para `int x = 5, y = 9, aux; aux = x; x = y - 2; y = aux + x;`:
  - Início: `x = 5, y = 9, aux = ?` → `aux = 5` → `x = 7` → `y = 5 + 7 = 12`. Saída `x y aux`: `7 12 5`.
- **(b) Binário e Bits:** `11010_2 = 16 + 8 + 2 = 26_10`; para representar `35` valores distintos: $2^5 = 32 < 35 \le 64 = 2^6 \implies \mathbf{6\text{ bits}}$.

### Exemplo 2 — Cálculo com constante e troca segura *(Programa completo)*
Lê dois preços `double` (`p1`, `p2`), aplica reajuste fixo de `+10%` via `#define FATOR 1.10`, troca os valores reajustados usando `aux` e imprime os resultados:

```c
#include <stdio.h>
#define FATOR 1.10

int main(void) {
    double p1, p2, aux;
    scanf("%lf %lf", &p1, &p2);

    p1 = p1 * FATOR;
    p2 = p2 * FATOR;

    aux = p1;
    p1 = p2;
    p2 = aux;

    printf("P1 final: R$ %.2f\nP2 final: R$ %.2f\n", p1, p2);
    return 0;
}
```

---

## 3. Exercícios (`A10-E01` a `A10-E05`)

### Sessão 1 (`A10-E01` a `A10-E03` — Rastreamento, Bits e Caça ao Bug)

### `A10-E01` *(Teste de Mesa — Memória e Atribuição)*
Sem usar computador, preencha a tabela de memória (`Passo | Instrução | m | n | aux`) para o trecho ilustrativo abaixo e informe o texto exato impresso pelo `printf`:

```c
int m = 4, n = 11, aux;
aux = m;
m = n - m;
n = aux + 5;
aux = n * 2;
m = aux - m;
printf("%d %d %d\n", m, n, aux);
```

---

### `A10-E02` *(Conversão Binário/Decimal e Capacidade em Bits — Papel)*
Sem usar calculadora:
- **(a)** Converta `101110_2` para a base 10.
- **(b)** Converta `53_10` para a base 2.
- **(c)** Quantos valores distintos cabem em `9 bits`? E qual a quantidade mínima de bits necessária para representar `200` códigos distintos?

---

### `A10-E03` *(Caça ao Bug Combinada — Programa completo)*
O programa completo abaixo deveria ler um salário base (`double`), somar o bônus simbólico `50.0` definido via `#define` e imprimir `Total: R$ <valor>`. Identifique todos os **5 defeitos intencionais** combinando sintaxe, *case-sensitivity*, identificador, `#define` e `scanf` (anote no papel ou em comentários `//`) e escreva a **versão corrigida completa**:

```c
#include <stdio.h>
#define BONUS 50.0;

Int main(void) {
    double 1nota, salario_final;
    scanf("%f", 1nota);
    salario_final = 1nota + BONUS;
    printf("Total: R$ %.2f\n", salario_final);
    return 0;
}
```

---

### Sessão 2 (`A10-E04` e `A10-E05` — Programas Completos Independentes)

### `A10-E04` *(Programa completo — Área e Perímetro de Terreno com `const`)*
Escreva um **programa completo** em C que leia a largura e o comprimento de um terreno retangular em metros (`double largura, comprimento;`), declare a constante `const double FATOR_PERIMETRO = 2.0;`, calcule a área (`largura * comprimento`) e o perímetro (`FATOR_PERIMETRO * (largura + comprimento)`), e imprima exatamente (com 2 casas decimais):
```text
Area: <area> m2
Perimetro: <perimetro> m
```
*(Não utilize divisão `/` nem `<math.h>`.)*

---

### `A10-E05` *(Programa completo — Salário Fixo + Comissão 5% e Troca de Registros)*
Inspirado na `Lista1` Ex. 6 (adaptado sem divisão), defina a macro `#define TAXA 0.05`. Escreva um **programa completo** em C que leia, para dois vendedores, o salário fixo e o total de vendas do mês (`double fixo1, vendas1, fixo2, vendas2;`):
1. Calcule as comissões `com1 = TAXA * vendas1` e `com2 = TAXA * vendas2`, e os totais `total1 = fixo1 + com1` e `total2 = fixo2 + com2`.
2. Troque os valores de `total1` e `total2` usando uma variável auxiliar `double aux;` (corrigindo uma inversão de cadastro nos totais).
3. Imprima exatamente:
```text
Comissao 1: R$ <com1 com 2 casas>
Comissao 2: R$ <com2 com 2 casas>
Total 1: R$ <total1 apos troca com 2 casas>
Total 2: R$ <total2 apos troca com 2 casas>
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `A10-C01` *(Papel — Teste de Mesa + Binário/$2^n$)*
- **(a)** Monte a tabela de memória (`a | b | c`) e informe a saída final do trecho:
```c
int a = 3, b = 10, c = 7;
c = b - a;
a = c * 2;
b = a - b;
c = b + a;
printf("%d %d %d\n", a, b, c);
```
- **(b)** Converta `11001_2` para decimal, converta `38_10` para binário, informe quantos valores cabem em `7 bits` e qual o mínimo de bits para `130` valores distintos.

### `A10-C02` *(Caça ao Bug — `#define`, escapes e `scanf` — Programa completo)*
Identifique e corrija todos os defeitos do programa completo abaixo, que lê `valor` (`double`), calcula `10%` de acréscimo e imprime exatamente `Taxa aplicada: "10%"` na 1ª linha e `Valor final: R$ <valor final>` na 2ª linha:
```c
#include <stdio.h>
#define TAXA 0.10;

int main(void) {
    double valor, acrescimo;
    scanf("%f", valor);
    acrescimo = valor * TAXA;
    printf("Taxa aplicada: "10%"\nValor final: R$ %.2f\n", valor + acrescimo);
    return 0;
}
```

### `A10-C03` *(Programa completo — Área/Comissão `double` + Troca com `aux`)*
Escreva um **programa completo** em C que leia as duas dimensões de um lote retangular (`double lado_a, lado_b;`) e o preço por metro quadrado (`double preco_m2;`), use `const double COMISSAO = 0.05;`:
1. Calcule `area = lado_a * lado_b` e `comissao = area * preco_m2 * COMISSAO`.
2. Troque `lado_a` e `lado_b` entre si usando `double aux;`.
3. Imprima exatamente:
```text
Dimensoes trocadas: <lado_a> x <lado_b>
Area: <area> m2
Comissao: R$ <comissao>
```
*(Todos os valores reais formatados com 2 casas decimais.)*

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para o Estágio B (`B01 — Operadores Aritméticos, Divisão Inteira e Resto`):** somente após autocorreção de `A10-E01`..`E05` **e** **100% (3/3)** na Checagem Independente `A10-C01`..`C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** identificar o tópico específico da falha (sintaxe/identificadores, `scanf`/`%lf`/`&`, troca `aux` ou binário/$2^n$) e aplicar variante `V2` de `A10`.
- **Regra das 2 tentativas malsucedidas:** após **2 reprovações** na revisão `A10`, suspender avanço e retornar especificamente ao bloco pré-requisito correspondente ao erro (`A02`–`A05` para sintaxe/constantes, `A06` para `scanf`, `A07` para memória/troca, `A08`–`A09` para bits/`sizeof`/`double`).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (itens 1–4 — Fundamentos, variáveis/constantes, precisão numérica, entrada/saída/atribuição).
- `[DOC]` `Aula_01_Algoritmos.pdf` a `Aula_04_Algoritmos.pdf` (visão consolidada do Estágio A).
- `[DOC]` `Aula_03_Algoritmos.pdf` p. 24 (Ex. 1 e Ex. 2 — área e constantes).
- `[DOC]` `Lista1_Algoritmos.pdf` p. 2 (Ex. 6 — comissão sobre vendas, adaptada para `0.05 * vendas` sem divisão).
- `[DOC]` `Lista8_Algoritmos_Revisao.pdf` p. 1 (Ex. 1 — revisão conceitual inicial).
- Gabarito e especificação de testes: [A10_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/gabaritos/A10_gabarito.md) e [A10_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/A10_testes.md).
