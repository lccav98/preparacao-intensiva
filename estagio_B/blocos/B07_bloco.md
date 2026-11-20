# Bloco `B07` — Condicionais Aninhadas, Decisões Hierárquicas e Associação do `else` (*Dangling Else*)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio B — Expressões, Operadores e Estruturas Condicionais / **`B07`** |
| **Micro-habilidade foco** | Estruturar decisões hierárquicas e dependentes com `if` aninhado, dominar a regra sintática do *dangling else* (associação ao `if` mais próximo) e aplicar prioridade estrita de validação. |
| **Pré-requisitos** | `B05` *(Múltiplas Alternativas com `else if`)*, `B06` *(Operadores Lógicos e Tabela-Verdade)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Sessão 2 (`E04`–`E06`, 20 min):** `12 min` resol. \| `5 min` corr. \| `3 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Não utilize** `switch`, laços (`while`, `for`, `do-while`), vetores/strings (`char[]`), ou funções além de `main`. Use chaves explícitas `{ }` em todas as estruturas para evitar ambiguidades. Saídas estritamente em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **`if` Aninhado vs. `else if`:**
   - Use **`else if`** quando houver alternativas mutuamente exclusivas que pertencem ao **mesmo nível lógico** (ex.: classificar uma nota em A, B, C ou D).
   - Use **`if` aninhado** (um `if` dentro do corpo de outro `if` ou `else`) quando a segunda decisão só faz sentido se a primeira tiver sido atendida (relação hierárquica ou pré-requisito).
2. **Prioridade Estrita de Validação (*Guard Clauses*):** 
   - Sempre teste primeiro a condição de existência, impedimento ou erro (ex.: lados não formam triângulo; frequência insuficiente para aprovação).
   - O refinamento ou classificação só deve ser processado após a validação prévia ter sido satisfeita.
3. **A Regra do *Dangling Else*:**
   - Em C, quando há múltiplos `if`s e não são usadas chaves `{ }`, o compilador associa o `else` ao **`if` mais próximo que ainda não tenha um `else` correspondente**, **independentemente da indentação do código**.
   - Indentação engana os olhos humanos, mas o compilador C ignora espaços em branco!
4. **Boas Práticas de Engenharia (Chaves Obrigatórias):**
   - Sempre coloque chaves `{ }` em todos os blocos `if` e `else`, mesmo quando houver apenas um comando interno. Isso elimina completamente o risco de bugs de *dangling else*.

---

## 2. Exemplos Guiados

### Exemplo 1 — A Armadilha do *Dangling Else* *(Trecho ilustrativo)*
Observe o código abaixo sem chaves:

```c
/* ATENCAO: Indentacao visual enganosa! */
if (x > 0)
    if (y > 0)
        printf("Ambos positivos\n");
else
    printf("X nao e positivo\n");  /* BUG: Este else pertence ao if (y > 0)! */
```
Se `x = 5` e `y = -1`:
- `x > 0` é verdadeiro.
- Entra no segundo teste: `y > 0` é falso.
- A CPU salta para o `else`, imprimindo `"X nao e positivo"` — o que é falso, pois `x` vale `5`!

**Forma Corrigida e Segura (com chaves explícitas):**
```c
if (x > 0) {
    if (y > 0) {
        printf("Ambos positivos\n");
    }
} else {
    printf("X nao e positivo\n");
}
```

### Exemplo 2 — Decisão Hierárquica: Existência antes da Classificação *(Programa completo)*
Para classificar um triângulo, é mandatório testar primeiro a sua condição de existência ($a < b + c$ e $b < a + c$ e $c < a + b$). Tentar classificar lados que não formam um triângulo gera absurdos lógicos (ex.: lados `1, 2, 10` não formam triângulo, mas sem teste de existência seriam chamados de "escaleno"!).

```c
#include <stdio.h>

int main(void) {
    double a, b, c;
    scanf("%lf %lf %lf", &a, &b, &c);

    /* 1º Nivel: Validacao previa de existencia */
    if (a < b + c && b < a + c && c < a + b) {
        /* 2º Nivel Hierarquico: Classificacao */
        if (a == b && b == c) {
            printf("Equilatero\n");
        } else if (a == b || a == c || b == c) {
            printf("Isosceles\n");
        } else {
            printf("Escaleno\n");
        }
    } else {
        printf("Nao Forma Triangulo\n");
    }

    return 0;
}
```

---

## 3. Exercícios (`B07-E01` a `B07-E06`)

### Sessão 1 (`B07-E01` a `B07-E03` — Rastreio de Dangling Else e Árvores)

### `B07-E01` *(Teste de Mesa — O perigo da indentação sem chaves)*
Sem usar computador, analise o trecho abaixo:

```c
int a = 2, b = -3;

if (a > 0)
    if (b > 0)
        printf("Caso 1\n");
    else
        printf("Caso 2\n");
```
1. Qual texto será impresso para `a = 2` e `b = -3`?
2. Qual texto será impresso para `a = -2` e `b = 3`?
3. Se o programador desejava que o `else` pertencesse ao primeiro `if (a > 0)`, reescreva o trecho utilizando chaves `{ }` para expressar essa intenção corretamente.

---

### `B07-E02` *(Completar Solução — Árvore de Decisão de Desconto em Passagem)*
Uma companhia aérea concede desconto em passagens sob as regras:
- Crianças menores de 2 anos viajam de graça no colo (`R$ 0.00`).
- Para passageiros de 2 anos ou mais, analisa-se a condição de estudante:
  - Se for estudante (`estudante == 1`), recebe 50% de desconto sobre a tarifa base (`tarifa * 0.50`).
  - Se não for estudante, paga a tarifa integral (`tarifa`).

Complete as lacunas `/* A */`, `/* B */` e `/* C */`:

```c
double tarifa, valor_final;
int idade, estudante;

scanf("%lf %d %d", &tarifa, &idade, &estudante);

if ( /* A: idade menor que 2 */ ) {
    valor_final = 0.0;
} else {
    if ( /* B: e estudante */ ) {
        valor_final = /* C: 50% da tarifa */;
    } else {
        valor_final = tarifa;
    }
}
printf("Valor: R$ %.2f\n", valor_final);
```

---

### `B07-E03` *(Caça ao Bug — Associação do else e falta de chaves)*
O programa abaixo deveria verificar o acesso a uma sala de servidores. Para entrar, o funcionário precisa ter crachá ativo (`cracha == 1`). Se tiver crachá, verifica se possui autorização biométrica (`biometria == 1`). Se não tiver biometria, imprime `Biometria Obrigatoria\n`. Se não tiver nem crachá ativo, deve imprimir `Cracha Invalido\n`.

```c
#include <stdio.h>

int main(void) {
    int cracha, biometria;
    scanf("%d %d", &cracha, &biometria);

    /* CODIGO BUGADO POR FALTA DE CHAVES */
    if (cracha == 1)
        if (biometria == 1)
            printf("Acesso Liberado\n");
    else
        printf("Cracha Invalido\n");

    return 0;
}
```
1. O que acontece quando `cracha = 1` e `biometria = 0`? O que é impresso e por que isso é um erro grave de segurança e lógica?
2. O que acontece quando `cracha = 0` e `biometria = 1`?
3. Escreva a versão corrigida completa em C com chaves explícitas e cobrindo os três desfechos: `Acesso Liberado`, `Biometria Obrigatoria` e `Cracha Invalido` ([B07_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B07_E03_corrigido.c)).

---

### Sessão 2 (`B07-E04` a `B07-E06` — Escrita Guiada → Independente)

### `B07-E04` *(Variação controlada — Classificação Completa de Triângulos)*
Escreva um **programa completo** em C que leia três números reais positivos (`double a, b, c`).
- Primeiro, valide a existência do triângulo ($a < b + c$ e $b < a + c$ e $c < a + b$).
- Se **não for triângulo**, imprima exatamente: `Nao Forma Triangulo\n`
- Se for triângulo, determine sua classificação:
  - Se todos os lados forem iguais ($a = b$ e $b = c$): imprima `Equilatero\n`
  - Se pelo menos dois lados forem iguais ($a = b$ ou $a = c$ ou $b = c$): imprima `Isosceles\n`
  - Se todos os lados forem distintos: imprima `Escaleno\n`

*Pista:* Siga a estrutura hierárquica do Exemplo 2.

---

### `B07-E05` *(Prioridade Estrita de Validação — Sistema Acadêmico UTFPR)*
Escreva um **programa completo** em C que leia a frequência percentual (`int freq`) e a nota final (`double nota`, de 0 a 10) de um aluno.
A regra universitária impõe **prioridade absoluta à frequência**:
1. Se o aluno tiver frequência inferior a 75% (`freq < 75`), ele está **imediatamente reprovado por falta**, independentemente de sua nota: imprima `Reprovado por Falta\n`.
2. Se a frequência for suficiente (`freq >= 75`), avalie o desempenho acadêmico:
   - Se `nota >= 7.0`: imprima `Aprovado\n`
   - Se `nota >= 4.0` e `nota < 7.0`: imprima `Exame Final\n`
   - Se `nota < 4.0`: imprima `Reprovado por Nota\n`

---

### `B07-E06` *(Resolução independente — Aprovação de Crédito Habitacional)*
Escreva um **programa completo** em C que leia três dados para solicitação de empréstimo habitacional:
1. `double renda_mensal` (renda mensal familiar em R$)
2. `double valor_parcela` (valor desejado da parcela mensal em R$)
3. `int restricoes_spc` (`1` se possui pendências/nome sujo no SPC/Serasa; `0` se possui cadastro limpo)

Regras hierárquicas:
1. Se houver restrições cadastrais (`restricoes_spc != 0`), o crédito é recusado imediatamente: imprima `Credito Recusado: Restricao Cadastral\n`.
2. Se não houver restrições (`restricoes_spc == 0`), a instituição financeira exige que o valor da parcela não ultrapasse **30% da renda mensal** (`valor_parcela <= renda_mensal * 0.30`):
   - Se a parcela exceder 30% da renda, imprima: `Credito Recusado: Parcela Excede Margem\n`
   - Se a parcela couber na margem de 30%, imprima: `Credito Aprovado\n`

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `B07-C01` *(Teste de Mesa — Rastreamento de Dangling Else)*
Considere o seguinte trecho em C:

```c
int x = 10, y = 5;

if (x > 5)
    if (y > 10)
        printf("Alpha\n");
    else
        printf("Beta\n");
else
    printf("Gama\n");
```
1. Qual será a saída para `x = 10` e `y = 5`?
2. Qual será a saída para `x = 3` e `y = 20`?
3. Qual será a saída para `x = 8` e `y = 12`?

---

### `B07-C02` *(Caça ao Bug — Triângulo sem validação prévia)*
Um aluno escreveu o código abaixo para classificar triângulos:

```c
#include <stdio.h>

int main(void) {
    double a, b, c;
    scanf("%lf %lf %lf", &a, &b, &c);

    if (a == b && b == c) {
        printf("Equilatero\n");
    } else if (a == b || a == c || b == c) {
        printf("Isosceles\n");
    } else {
        printf("Escaleno\n");
    }

    return 0;
}
```
1. Mostre um exemplo de entrada com três valores positivos que **não podem formar um triângulo**, mas que o programa classifica erroneamente como `Escaleno` ou `Isosceles`.
2. Escreva o programa completo corrigido em C que realiza primeiro a validação de existência e, somente se válido, classifica o triângulo ([B07_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B07_C02_corrigido.c)).

---

### `B07-C03` *(Programa completo — Sistema de Triagem de Doação de Sangue)*
Escreva um programa completo em C para um hemocentro que leia:
- `int idade`
- `double peso`
- `int jejum_horas` (número de horas em jejum alimentar)

A triagem deve seguir **estritamente a hierarquia de barreiras** (cada barreira só é verificada se a anterior tiver sido superada):
1. **Idade:** deve estar entre 16 e 69 anos inclusive (`idade >= 16 && idade <= 69`). Se fora da faixa, imprima: `Impedimento: Idade Fora da Faixa\n`
2. **Peso:** deve ter no mínimo 50.0 kg (`peso >= 50.0`). Se inferior, imprima: `Impedimento: Peso Insuficiente\n`
3. **Jejum:** não pode estar em jejum prolongado nem ter acabado de comer: o jejum deve ser de pelo menos 2 horas e no máximo 12 horas (`jejum_horas >= 2 && jejum_horas <= 12`). Se fora desse intervalo, imprima: `Impedimento: Jejum Inadequado\n`
4. Se passar por todos os três filtros hierárquicos, imprima: `Apto para Doacao\n`

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `B08` (`Múltipla Escolha com switch/case`):** somente após autocorreção dos exercícios `B07-E01..E06` **e** **100% (3/3)** na Checagem Independente `B07-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** revisar o uso obrigatório de chaves `{ }` desenhando a árvore de decisão no papel antes de codificar.
- **Após 2 tentativas malsucedidas:** retornar a **`B05`** (estruturas `else if`) e **`B06`** (composição lógica com `&&`).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 6 — Estruturas condicionais aninhadas).
- `[DOC]` `Aula_07_Algoritmos.pdf` p. 16–23 (`if` aninhado, problema do *dangling else* e árvore de decisões).
- `[DOC]` `Lista2_Algoritmos.pdf` p. 2–4 (Ex. 4, 6, 7, 8 — entrega e prioridade estrita de validação).
- Casos de teste e soluções verificáveis: [B07_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/gabaritos/B07_gabarito.md) e [B07_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/B07_testes.md).
