# Bloco `B06` — Operadores Lógicos (`&&`, `||`, `!`), Tabela-Verdade e Precedência Completa

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio B — Expressões, Operadores e Estruturas Condicionais / **`B06`** |
| **Micro-habilidade foco** | Combinar e negar expressões booleanas usando `&&`, `||` e `!` com tabela-verdade, avaliação em curto-circuito e precedência correta (`!` > aritméticos > relacionais > `&&` > `||`). |
| **Pré-requisitos** | `B03` *(Operadores Relacionais e Expressões Booleanas)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 20 min):** `12 min` resol. \| `5 min` corr. \| `3 min` recup.; **Sessão 2 (`E04`–`E06`, 18 min):** `11 min` resol. \| `4 min` corr. \| `3 min` recup.; **Checagem (`C01`–`C04`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Não utilize** laços (`while`, `for`, `do-while`), vetores/strings (`char[]`), ou funções além de `main`. Use apenas operadores aritméticos, relacionais e lógicos dentro de estruturas condicionais `if / else`. Saídas estritamente em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C04`, sem gabarito):** `___ / 4` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Conjunção (`&&`) — E lógico:** `A && B` resulta em `1` (verdadeiro) apenas se **ambos** os operandos forem verdadeiros (`!= 0`). Se qualquer um for `0`, resulta em `0`.
2. **Disjunção (`||`) — OU lógico:** `A || B` resulta em `1` se **pelo menos um** dos operandos for verdadeiro (`!= 0`). Só resulta em `0` se ambos forem falsos.
3. **Negação unária (`!`) — NÃO lógico:** Inverte o valor lógico: `!0` resulta em `1`, e `!(qualquer valor != 0)` resulta em `0`.
4. **Avaliação em Curto-Circuito (*Short-Circuit*):** 
   - Em `A && B`, se `A` for falso (`0`), `B` **não é avaliado** (o resultado já é garantidamente `0`).
   - Em `A || B`, se `A` for verdadeiro (`!= 0`), `B` **não é avaliado** (o resultado já é garantidamente `1`).
5. **Ordem de Precedência Completa em C:**
   - 1º: Parênteses `( )` e operador unário de negação `!`
   - 2º: Aritméticos multiplicativos (`*`, `/`, `%`)
   - 3º: Aritméticos aditivos (`+`, `-`)
   - 4º: Relacionais de grandeza (`<`, `<=`, `>`, `>=`)
   - 5º: Relacionais de igualdade (`==`, `!=`)
   - 6º: Conjunção lógica `&&`
   - 7º: Disjunção lógica `||`
   - 8º: Atribuição `=`
6. **O Erro Clássico `1 <= x <= 10`:** Em matemática escreve-se $1 \le x \le 10$. Em C, isso é avaliado como `(1 <= x) <= 10`. Como `(1 <= x)` resulta em `0` ou `1`, e tanto `0` quanto `1` são menores ou iguais a `10`, a expressão resulta **sempre em `1` (verdadeiro)**, qualquer que seja o valor de `x`! A forma correta em C exige conjunção explícita: `x >= 1 && x <= 10`.
7. **Parênteses Defensivos:** Sempre que combinar `&&` e `||` na mesma expressão, use parênteses explícitos para garantir legibilidade e imunidade a erros sutis de precedência.

---

## 2. Exemplos Guiados

### Exemplo 1 — Tabela-Verdade e Avaliação Curto-Circuito *(Trecho ilustrativo)*
Dadas as variáveis `int a = 5, b = 0, c = -2;`:

| Expressão | Avaliação Passo a Passo | Resultado | Curto-Circuito? |
|---|---|---|---|
| `a > 0 && b > 0` | `(5 > 0)` é `1` → avalia `(0 > 0)` que é `0` → `1 && 0` | `0` | Não |
| `b > 0 && a > 0` | `(0 > 0)` é `0` → encerra imediatamente | `0` | **Sim** (`a > 0` nem é avaliado) |
| `a > 0 \|\| c > 0` | `(5 > 0)` é `1` → encerra imediatamente | `1` | **Sim** (`c > 0` nem é avaliado) |
| `!b && c < 0` | `!0` é `1` → `(-2 < 0)` é `1` → `1 && 1` | `1` | Não |

### Exemplo 2 — Intervalo com Conjunção e Validação Composta *(Programa completo)*
Um clube concede acesso especial a membros que tenham idade entre 18 e 60 anos (inclusive) **E** mensalidade em dia (`mensalidade == 1`):

```c
#include <stdio.h>

int main(void) {
    int idade, mensalidade;
    scanf("%d %d", &idade, &mensalidade);

    /* FORMA CORRETA: intervalos requerem && explicito */
    if (idade >= 18 && idade <= 60 && mensalidade == 1) {
        printf("Acesso Permitido\n");
    } else {
        printf("Acesso Negado\n");
    }

    return 0;
}
```
**Por que não usar `18 <= idade <= 60`?** Se `idade = 80`, `18 <= 80` avalia para `1`. Em seguida `1 <= 60` avalia para `1`. O aluno idoso de 80 anos receberia acesso indevidamente!

---

## 3. Exercícios (`B06-E01` a `B06-E06`)

### Sessão 1 (`B06-E01` a `B06-E03` — Tabela-Verdade, Precedência e Caça ao Bug)

### `B06-E01` *(Tabela-Verdade e Teste de Mesa)*
Sem usar computador, determine o valor inteiro (`0` ou `1`) resultante de cada uma das expressões lógicas abaixo, considerando as seguintes variáveis:
`int x = 4, y = 7, z = 0;`

a) `x < y && y != 7`  
b) `x + 3 == y || z > 0`  
c) `!z && (x > y || y > 0)`  
d) `!(x < y) || !z && y > x`  
e) `z != 0 && (y / z > 1)` *(atenção ao curto-circuito: ocorre divisão por zero?)*  

---

### `B06-E02` *(Precedência e Parênteses Defensivos)*
Dadas as variáveis `int a = 1, b = 0, c = 1;`:
1. Avalie a expressão sem parênteses: `a || b && c == 0`
   - Indique a ordem em que os operadores são avaliados (`==`, `&&`, `||`).
   - Qual é o resultado final (`0` ou `1`)?
2. Avalie a mesma expressão com agrupamento forçado: `(a || b) && c == 0`
   - Qual é o resultado final agora? Explique por que a adição de parênteses alterou o resultado.

---

### `B06-E03` *(Caça ao Bug — O erro clássico `min <= x <= max`)*
O programa abaixo deveria verificar se um candidato atende ao requisito de idade para uma vaga de concurso público (idade entre 18 e 35 anos inclusive). Se estiver na faixa, deve imprimir `Apto\n`; caso contrário, `Inapto\n`.

```c
#include <stdio.h>

int main(void) {
    int idade;
    scanf("%d", &idade);

    /* BUG: encadeamento matematico invalido em C */
    if (18 <= idade <= 35) {
        printf("Apto\n");
    } else {
        printf("Inapto\n");
    }

    return 0;
}
```
1. Explique passo a passo o que a CPU executa quando a entrada é `idade = 50`. Por que o programa imprime `Apto` de forma incorreta?
2. Escreva o programa completo corrigido em C (arquivo [B06_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B06_E03_corrigido.c)).

---

### Sessão 2 (`B06-E04` a `B06-E06` — Escrita Guiada → Independente)

### `B06-E04` *(Variação controlada com pistas — Parque de Diversões)*
Escreva um **programa completo** em C que leia a altura em metros (`double alt`) e a idade em anos (`int idade`) de uma pessoa para uma montanha-russa radical.
- Regra de acesso: a pessoa pode entrar se tiver **altura mínima de 1.50 m** E **idade mínima de 12 anos**, **OU** se tiver **idade maior ou igual a 16 anos** e **altura mínima de 1.40 m**.
- Se puder entrar, imprima: `Acesso Permitido\n`
- Caso contrário, imprima: `Acesso Negado\n`

*Pista:* Use parênteses defensivos agrupando as duas condições alternativas: `((alt >= 1.50 && idade >= 12) || (idade >= 16 && alt >= 1.40))`.

---

### `B06-E05` *(Variação com regras geométricas — Condição de Existência de Triângulo)*
Escreva um **programa completo** em C que leia três números reais positivos (`double a, b, c`) representando os comprimentos dos lados de um triângulo.
Para que três lados formem um triângulo válido, **cada lado deve ser estritamente menor que a soma dos outros dois**. Ou seja, as três condições a seguir devem ser simultaneamente verdadeiras:
- $a < b + c$
- $b < a + c$
- $c < a + b$

Se os três lados formarem um triângulo, imprima: `Triangulo Valido\n`  
Caso contrário, imprima: `Triangulo Invalido\n`  
*Atenção:* Use uma única expressão lógica com o operador `&&` no `if`.

---

### `B06-E06` *(Resolução independente — Sistema de Concessão de Empréstimo)*
Escreva um **programa completo** em C que leia três valores:
1. `int idade` (idade do solicitante)
2. `double renda` (renda mensal bruta em R$)
3. `int correntista` (`1` se for cliente VIP/especial do banco; `0` se for cliente comum)

A aprovação do empréstimo segue as regras:
- O empréstimo é **aprovado** se:
  - O solicitante tiver idade entre 21 e 65 anos inclusive (`idade >= 21` e `idade <= 65`) **E** renda mensal de pelo menos `2500.00` (`renda >= 2500.00`);
  - **OU** se o solicitante for cliente especial (`correntista == 1`), desde que tenha pelo menos 18 anos (`idade >= 18`) e renda de pelo menos `1500.00` (`renda >= 1500.00`).
- Caso atenda a qualquer um desses critérios, imprima exatamente: `Emprestimo Aprovado\n`
- Caso contrário, imprima: `Emprestimo Negado\n`

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `B06-C01` *(Teste de Mesa — Tabela-Verdade e Curto-Circuito)*
Para as variáveis `int p = 0, q = 3, r = -1;`, avalie as 4 expressões abaixo indicando o valor numérico final (`0` ou `1`) e informando se o último termo foi ou não avaliado devido ao curto-circuito:
1. `p != 0 && (q / p > 0)`
2. `q > 0 || (r / p == 0)`
3. `!p && (q > 0 || r > 0)`
4. `!(q > 2 && r < 0) || (p == 0)`

---

### `B06-C02` *(Caça ao Bug — Precedência e Limite Duplo)*
O programa abaixo recebe a nota (`double nota`, de 0 a 10) e a frequência (`int freq`, em %) de um aluno, e deve imprimir `Aprovado\n` se a nota estiver entre 6.0 e 10.0 inclusive **E** a frequência for de pelo menos 75%. Caso contrário, imprime `Reprovado\n`.

```c
#include <stdio.h>

int main(void) {
    double nota;
    int freq;
    scanf("%lf %d", &nota, &freq);

    if (6.0 <= nota <= 10.0 && freq >= 75) {
        printf("Aprovado\n");
    } else {
        printf("Reprovado\n");
    }

    return 0;
}
```
1. Identifique o defeito que faz um aluno com `nota = 2.0` e `freq = 80` ser considerado `Aprovado`.
2. Escreva o programa corrigido completo em C ([B06_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B06_C02_corrigido.c)).

---

### `B06-C03` *(Programa completo — Validação de Data em Ano Não-Bissexto)*
Escreva um programa completo em C que leia dois inteiros: `dia` e `mes` (`scanf("%d %d", &dia, &mes);`).
Considere um ano padrão de 365 dias (fevereiro tem 28 dias). A data é válida se:
- O mês estiver na faixa de 1 a 12 (`mes >= 1 && mes <= 12`), **E**
- O dia for compatível com o mês correspondente:
  - Mês 2 (Fevereiro): `dia >= 1 && dia <= 28`
  - Meses com 30 dias (Abril=4, Junho=6, Setembro=9, Novembro=11): `dia >= 1 && dia <= 30`
  - Meses com 31 dias (Janeiro=1, Março=3, Maio=5, Julho=7, Agosto=8, Outubro=10, Dezembro=12): `dia >= 1 && dia <= 31`

Se a data for válida, imprima: `Data Valida\n`  
Caso contrário, imprima: `Data Invalida\n`  
*Restrição:* Proibido usar laços ou vetores. Utilize combinações de `&&` e `||` em `if / else if / else`.

---

### `B06-C04` *(Programa completo — Concessão de Bolsa de Iniciação Científica)*
Escreva um programa completo em C que leia dois valores referentes a um estudante universitário:
- `double cra` (Coeficiente de Rendimento Acumulado, de 0.0 a 10.0)
- `double renda` (Renda familiar per capita em R$)

O estudante terá direito à bolsa de apoio acadêmico se atender a qualquer uma das condições:
1. `cra >= 8.5` E `renda <= 1800.00` (Critério Mérito + Renda)
2. `cra >= 9.5` independente de renda (Critério Mérito Excepcional)

Se tiver direito, imprima: `Bolsa Concedida\n`  
Caso contrário, imprima: `Bolsa Nao Concedida\n`

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `B07` (`Condicionais Aninhadas e Decisões Hierárquicas`):** somente após autocorreção dos exercícios `B06-E01..E06` **e** **100% (4/4)** na Checagem Independente `B06-C01..C04` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** revisar a regra de curto-circuito e o erro de encadeamento `min <= x <= max`, reescrevendo explicitamente com `x >= min && x <= max`.
- **Após 2 tentativas malsucedidas:** retornar a **`B03`** (comparações relacionais simples) e **`B02`** (precedência de operadores aritméticos).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 1–2 (item 5: *"Precedência de operadores lógicos e aritméticos. Lógica booleana, valores e operadores lógicos, tabela-verdade"*).
- `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 1 (Aulas de 01/09 e 08/09).
- `[DOC]` `Lista2_Algoritmos.pdf` p. 2–4 (Ex. 6, 7, 8 — regras compostas com `&&` e `||`).
- `[DOC]` `Aula_08_Algoritmos_v2.pdf` p. 20 (expressões lógicas compostas com `||`).
- Casos de teste e soluções verificáveis: [B06_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/gabaritos/B06_gabarito.md) e [B06_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/B06_testes.md).
