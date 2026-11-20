# Bloco `C03` — Leituras por Sentinela e Algoritmos Iterativos com `while` (Máximo e MDC/Euclides)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio C — Estruturas de Repetição e Rastreamento de Laços / **`C03`** |
| **Micro-habilidade foco** | Estruturar laços controlados por valor sentinela (sem processar a sentinela) e atualizar estado iterativo com algoritmo clássico de Euclides e busca de máximo/estatísticas. |
| **Pré-requisitos** | `C02` *(Contadores e Acumuladores com `while`)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 20 min):** `12 min` resol. \| `5 min` corr. \| `3 min` recup.; **Sessão 2 (`E04`–`E06`, 22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Não utilize** laços `do-while` ou `for`, comandos de salto (`break`, `continue`), vetores ou funções customizadas além de `main`. Use estritamente o laço `while`, tipos escalares (`int`, `double`), condicionais simples e saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **O Conceito de Sentinela:** Um valor especial fora do domínio dos dados válidos (por exemplo, `-1` para notas positivas, ou `0` para dados não nulos) utilizado exclusivamente para sinalizar o fim da entrada quando a quantidade de elementos é previamente desconhecida.
2. **Padrão *Priming Read* (Leitura Prévia Obrigatória):**
   - **1ª leitura:** Realizada *fora e imediatamente antes* do `while`.
   - **Teste de repetição:** `while (valor != SENTINELA)`.
   - **Processamento:** Ocorre no início/meio do corpo com o dado já validado.
   - **Próxima leitura:** Feita *no final do corpo*, logo antes do fechamento `}` do `while`.
   - Essa estrutura impede categoricamente que o valor da sentinela seja somado, contado ou computado nas estatísticas.
3. **Tratamento de Borda de Entrada Vazia:** Se o primeiro valor digitado for a própria sentinela, o corpo do laço é executado exatamente **0 vezes**. O programa deve prever essa situação (por exemplo, não dividindo por zero no cálculo de médias e imprimindo mensagem apropriada).
4. **Atualização de Extremos (Máximo e Mínimo) em Fluxo:**
   - **Regra de ouro:** **Nunca inicialize `maior` ou `menor` com zero ou valores arbitrários (`9999`)**. Se todos os números digitados forem negativos (ex.: `-5, -12, -8`), inicializar `maior = 0` resultará no valor errado `0`.
   - **Inicialização correta:** Inicialize `maior` com o **primeiro valor válido lido** antes do laço (ou use uma variável de controle de primeiro elemento).
5. **Algoritmo de Euclides para o Máximo Divisor Comum (MDC):**
   - Propriedade: $\text{MDC}(m, n) = \text{MDC}(n, m \pmod n)$.
   - Algoritmo iterativo: enquanto $n \ne 0$, calcula-se $resto = m \pmod n$, atualiza-se $m = n$ e $n = resto$. Ao final, $m$ conterá o MDC exato.
   - **Auto-inversão elegante:** Se $m < n$ na entrada (ex.: $m = 12, n = 18$), a primeira iteração calcula $resto = 12 \pmod{18} = 12$, atribui $m = 18$ e $n = 12$, invertendo as grandezas perfeitamente sem necessidade de `if` prévio!

---

## 2. Exemplos Guiados

### Exemplo 1 — Teste de mesa de Euclides com $m < n$ *(Trecho ilustrativo)*
Calcular $\text{MDC}(12, 18)$ pelo Algoritmo de Euclides:

```c
int m = 12, n = 18, resto;
while (n != 0) {
    resto = m % n;
    m = n;
    n = resto;
}
/* Pos-laco: m contem o MDC */
```

**Tabela de Teste de Mesa:**

| Iteração | `m` no início | `n` no início | `resto = m % n` | Novo `m = n` | Novo `n = resto` |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 12 | 18 | $12 \pmod{18} = 12$ | 18 | 12 *(inverteu!)* |
| 2 | 18 | 12 | $18 \pmod{12} = 6$ | 12 | 6 |
| 3 | 12 | 6 | $12 \pmod{6} = 0$ | 6 | 0 |
| Saída | 6 | 0 | *(encerra: `n == 0`)* | `m = 6` | `n = 0` |

Resultado: $\text{MDC}(12, 18) = 6$.

---

### Exemplo 2 — Média com sentinela e proteção contra divisão por zero *(Programa completo)*
O programa lê notas inteiras positivas até que seja digitado `-1`. Imprime a média com duas casas decimais ou mensagem de entrada vazia:

```c
#include <stdio.h>

int main(void) {
    int nota;
    int soma = 0;
    int conta = 0;

    scanf("%d", &nota);   /* Priming read */
    while (nota != -1) {
        soma += nota;
        conta++;
        scanf("%d", &nota);   /* Releitura no fim do corpo */
    }

    if (conta > 0) {
        double media = (double)soma / conta;
        printf("Media: %.2f\n", media);
    } else {
        printf("Nenhum dado valido\n");
    }

    return 0;
}
```

---

## 3. Exercícios (`C03-E01` a `C03-E06`)

### Sessão 1 (`E01`–`E03`)

### `C03-E01` *(Teste de Mesa / Algoritmo de Euclides)*
Sem usar o computador, preencha a tabela de rastreamento do Algoritmo de Euclides para cada um dos pares:
1. `m = 15, n = 25` (mostre a inversão na primeira iteração e o MDC final).
2. `m = 24, n = 9`.

---

### `C03-E02` *(Caça ao Bug — Sentinela Somada e Máximo com Negativos)*
Um aluno tentou escrever um programa para ler uma sequência de temperaturas inteiras até a sentinela `-999`, calculando a soma e a maior temperatura lida:

```c
#include <stdio.h>

int main(void) {
    int temp;
    int soma = 0;
    int maior = 0;    /* Bug 1: inicializado com zero */

    while (temp != -999) {   /* Bug 2: temp nao lido antes */
        scanf("%d", &temp);
        soma += temp;        /* Bug 3: soma a sentinela -999! */
        if (temp > maior) {
            maior = temp;
        }
    }

    printf("Soma: %d\n", soma);
    printf("Maior: %d\n", maior);
    return 0;
}
```
1. Explique por que a inicialização `maior = 0` falha se todas as temperaturas digitadas forem negativas (ex.: `-10, -5, -8`).
2. Explique por que fazer a leitura no início do `while` faz com que o valor `-999` seja somado à variável `soma`.
3. Escreva a versão corrigida completa e funcional do programa em C usando o padrão *priming read*. Considere que pelo menos uma temperatura válida anterior a `-999` será informada.

---

### `C03-E03` *(Completar Solução — Contagem e Soma com Sentinela 0)*
O programa a seguir lê uma sequência de números inteiros positivos até que o valor `0` seja informado (sentinela). Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */`:

```c
#include <stdio.h>

int main(void) {
    int x;
    int conta = 0;
    int soma = 0;

    scanf("%d", &x);   /* A: Leitura previa */

    while (/* B: condicao */) {
        soma += x;
        /* C: incrementa contador */;
        /* D: releitura de x */;
    }

    printf("Quantidade: %d\n", conta);
    printf("Soma: %d\n", soma);
    return 0;
}
```

---

### Sessão 2 (`E04`–`E06`)

### `C03-E04` *(Completar Solução — Média Real com Sentinela Negativa)*
Complete o programa em C que lê números reais (`double`) estritamente positivos até que um número menor ou igual a zero seja digitado. Se nenhum número positivo for lido, imprime `Nenhum positivo lido\n`. Caso contrário, imprime `Media: %.2f\n`:

```c
#include <stdio.h>

int main(void) {
    double valor;
    double soma = 0.0;
    int qtd = 0;

    scanf("%lf", &valor);

    while (/* Lacuna 1: condicao para positivos */) {
        soma += valor;
        qtd++;
        /* Lacuna 2: releitura de valor */;
    }

    if (/* Lacuna 3: teste se houve leitura */) {
        printf("Media: %.2f\n", soma / qtd);
    } else {
        printf("Nenhum positivo lido\n");
    }

    return 0;
}
```

---

### `C03-E05` *(Programa Completo Independente — MDC de Euclides Iterativo)*
Escreva um programa completo em C que leia dois inteiros positivos `a` e `b`.  
Implemente o Algoritmo de Euclides usando um laço `while` para calcular o Máximo Divisor Comum entre `a` e `b`.  
A saída deve imprimir estritamente:
```text
MDC: %d\n
```

Exemplo de entrada:
```text
48 18
```
Exemplo de saída:
```text
MDC: 6
```

---

### `C03-E06` *(Programa Completo Independente — Maior e Menor com Sentinela)*
Escreva um programa completo em C que leia uma sequência de números inteiros positivos até que a sentinela `-1` seja digitada.  
O programa deve determinar e imprimir o maior e o menor número lido.  
Se o primeiro valor for `-1`, imprima exatamente:
```text
Nenhum dado informado\n
```
Caso contrário, imprima:
```text
Maior: %d\n
Menor: %d\n
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `C03-C01` *(Teste de Mesa / Entrada Vazia no Priming Read)*
Sem usar o computador, analise o programa:

```c
#include <stdio.h>

int main(void) {
    int val, cont = 0;
    scanf("%d", &val);
    while (val != 0) {
        cont++;
        scanf("%d", &val);
    }
    printf("Contagem: %d\n", cont);
    return 0;
}
```
1. Se a entrada fornecida for `0`, quantas iterações são executadas pelo laço? O que é impresso?
2. Se a entrada for `4 7 0`, qual o valor impresso?
3. O número `0` é contado em alguma das duas situações? Justifique.

---

### `C03-C02` *(Teste de Mesa / Ordem das Atribuições em Euclides)*
Um estudante escreveu o seguinte corpo do laço de Euclides:
```c
while (n != 0) {
    m = n;           /* Linha 1 */
    n = m % n;       /* Linha 2 */
}
```
1. Explique por que esse trecho é um bug crítico e o que acontece na Linha 2 quando a Linha 1 é executada primeiro.
2. Escreva a sequência correta de 3 atribuições para atualizar `m` e `n`.

---

### `C03-C03` *(Programa Completo Independente — Estatísticas de Fluxo com Sentinela)*
Escreva um programa completo em C que leia uma sequência de inteiros positivos até que seja digitado o valor `0` (sentinela).  
Se o primeiro valor lido for `0`, imprima exatamente:
```text
Nenhum valor valido\n
```
Caso contrário, o programa deve calcular e imprimir:
1. A quantidade de números lidos (excluindo o zero).
2. A soma de todos os números lidos.
3. A média aritmética com duas casas decimais (`%.2f`).
4. O maior número lido.

Formato exato de saída:
```text
Quantidade: %d\n
Soma: %d\n
Media: %.2f\n
Maior: %d\n
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `C04` (`Repetição com Pós-Condição do-while e Menus Interativos`):** somente após autocorreção dos exercícios `C03-E01..E06` **e** **100% (3/3)** na Checagem Independente `C03-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** revisar o padrão *priming read*, a necessidade de salvar o resto em variável temporária antes de atualizar `m` e `n` em Euclides, e aplicar a variante `V2` do bloco.
- **Após 2 tentativas malsucedidas:** retornar para **`C02`** (contadores e acumuladores) e **`B04`** (proteção condicional de divisão por zero).

---

## 6. Referências do Orientador
- `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 2 (18/09 — Laços controlados por sentinela e algoritmo de Euclides).
- `[DOC]` `Aula_09_Algoritmos.pdf` p. 13–14, 19–20 (Leitura com sentinela, cálculo de maior/menor e MDC).
- `[DOC]` `Lista4_Algoritmos.pdf` p. 2–3 (Ex. 4, 5 e 6 — leitura com sentinela e algoritmo de Euclides).
- `[DOC]` `Lista8_Algoritmos_Revisao.pdf` p. 1–2 (Ex. 3 — estatísticas de fluxo sem vetores).
- Casos de teste e soluções verificáveis: [C03_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/gabaritos/C03_gabarito.md) e [C03_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/C03_testes.md).
