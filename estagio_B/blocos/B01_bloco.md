# Bloco `B01` — Operadores Aritméticos, Divisão Inteira e Resto (`%`)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio B — Expressões, Operadores e Estruturas Condicionais / **`B01`** |
| **Micro-habilidade foco** | Avaliar expressões com `+`, `-`, `*`, `/` e `%`, prevendo com exatidão quando `/` trunca como divisão inteira vs. quando produz resultado real e decompondo quantidades com `/` e `%`. |
| **Pré-requisitos** | `A10` *(Consolidação do Estágio A — Tipos, E/S e Atribuição)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão única de prática + checagem (22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Não utilize** comandos de desvio condicional (`if`, `switch`), operadores relacionais (`<`, `==`), operadores lógicos (`&&`, `||`, `!`), laços (`while`, `for`) ou vetores. Utilize apenas tipos básicos (`int`, `double`), operadores aritméticos (`+`, `-`, `*`, `/`, `%`) e E/S (`scanf`, `printf`). |

### Registro das Sessões (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Divisão Inteira (`int / int`):** Quando ambos os operandos são inteiros, o operador `/` descarta toda a parte fracionária (**trunca em direção a zero**, não arredonda). Exemplo: `7 / 2` resulta em `3`, e `1 / 4` resulta em `0`.
2. **Divisão Real:** Para obter casas decimais, ao menos um dos operandos deve ser de ponto flutuante (`float` ou `double`). Exemplo: `7.0 / 2` ou `7 / 2.0` resulta em `3.5`.
3. **A Armadilha da Variável Receptora:** Em `double r = 5 / 2;`, a variável `r` recebe `2.0`! O compilador avalia primeiro a expressão à direita (`5 / 2`, que dá `2` inteiro) e só então armazena em `r`, promovendo para real. Declarar a variável como `double` não impede a divisão inteira no lado direito.
4. **Operador Resto (`%`):** O operador `%` calcula o resto da divisão inteira entre dois inteiros. É **estritamente proibido** aplicar `%` a números reais (`float` ou `double`) em C.
5. **Relação da Decomposição Euclidiana:** Para quaisquer inteiros positivos `a` e `b`:  
   $$\text{Dividendo} = \text{Divisor} \times \text{Quociente} + \text{Resto} \iff a = b \times (a / b) + (a \% b)$$  
   Use `/` para obter a quantidade do grupo maior e `%` para extrair o que sobrou.

---

## 2. Exemplos Guiados

### Exemplo 1 — Divisão inteira vs. real e a armadilha do `double` *(Trecho ilustrativo)*
Considere o cálculo da metade de uma quantia inteira `int n = 7;`:

```c
/* FORMA ERRADA: 7 / 2 trunca antes de salvar em r */
double r1 = n / 2;        /* r1 recebe 3.0 */

/* FORMA CORRETA: forcar ao menos um operando real */
double r2 = n / 2.0;      /* r2 recebe 3.5 */
```

### Exemplo 2 — Decomposição de tempo em minutos e segundos *(Programa completo)*
Dada uma quantidade total de segundos inteiros (ex.: `135`), decompor em minutos completos e segundos restantes:

```c
#include <stdio.h>

int main(void) {
    int total_seg, minutos, segundos;
    scanf("%d", &total_seg);

    minutos = total_seg / 60;   /* Quociente: grupos de 60 segundos */
    segundos = total_seg % 60;  /* Resto: segundos que sobraram */

    printf("Minutos: %d\n", minutos);
    printf("Segundos: %d\n", segundos);
    return 0;
}
```
Se a entrada for `135`: `135 / 60` resulta em `2` minutos; `135 % 60` resulta em `15` segundos. Prova: `60 * 2 + 15 = 135`.

---

## 3. Exercícios (`B01-E01` a `B01-E05`)

### `B01-E01` *(Teste de Mesa / Previsão Mental — Reprodução do Modelo)*
Sem usar o computador, calcule o resultado de cada expressão aritmética em C e indique o seu tipo resultante (`int` ou `double`):
1. `5 / 2`
2. `5.0 / 2`
3. `double r = 5 / 2;` *(qual valor fica armazenado em `r`?)*
4. `17 % 5`
5. `7 % 10`
6. `4 * (10 / 3) + (10 % 3)`

---

### `B01-E02` *(Completar Solução — Decomposição de Cédulas)*
O programa abaixo deve ler uma quantia inteira em reais (`valor`) e calcular quantas cédulas de R$ 20 e quantas moedas de R$ 1 são necessárias para compor o valor. Complete as lacunas `/* A */` e `/* B */`:

```c
#include <stdio.h>

int main(void) {
    int valor, notas20, moedas1;
    scanf("%d", &valor);

    notas20 = /* A */;
    moedas1 = /* B */;

    printf("Notas de 20: %d\n", notas20);
    printf("Moedas de 1: %d\n", moedas1);
    return 0;
}
```

---

### `B01-E03` *(Completar Solução — Minutos e Segundos)*
Complete o programa em C que lê uma quantidade inteira de segundos (`total_seg`) e imprime quantos minutos inteiros e quantos segundos excedentes ela representa:

```c
#include <stdio.h>

int main(void) {
    int total_seg, minutos, segundos;
    scanf("%d", &total_seg);

    minutos = total_seg / 60;
    segundos = /* Lacuna */;

    printf("Minutos: %d\n", minutos);
    printf("Segundos: %d\n", segundos);
    return 0;
}
```

---

### `B01-E04` *(Resolver com Pistas — Horas, Minutos e Segundos Compacto)*
Escreva um programa completo em C que leia uma quantidade inteira de segundos (`int seg_totais`) e decomponha em horas, minutos e segundos.  
Imprima exatamente no formato: `%d h %d m %d s\n`.  
*Pistas:*
1. Uma hora possui 3600 segundos (`horas = seg_totais / 3600;`).
2. O que sobra das horas é obtido com `resto = seg_totais % 3600;`.
3. A partir desse `resto`, calcule os minutos dividindo por 60 e os segundos restantes usando `% 60`.

---

### `B01-E05` *(Resolução Independente — Decomposição Horária Detalhada)*
Escreva um programa completo em C que leia uma quantidade inteira de segundos (`int tempo_seg`, com `tempo_seg >= 0`) e calcule a decomposição em horas, minutos e segundos.  
Imprima estritamente em linhas separadas:
```text
Horas: %d\n
Minutos: %d\n
Segundos: %d\n
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `B01-C01` *(Teste de Mesa / Avaliação Mental)*
Calcule mentalmente (sem compilador) o valor exato das seguintes expressões em C:
1. `14 / 4`
2. `14 % 4`
3. `double x = 14 / 4;` *(qual o valor numérico armazenado em `x`?)*
4. `14.0 / 4`
5. `3 % 8`

---

### `B01-C02` *(Caça ao Bug — Correção de Desconto Percentual)*
Um estudante escreveu o seguinte programa para calcular um desconto de 10% sobre uma compra inteira em reais (`valor`), mas o programa sempre imprime `Desconto: R$ 0.00` para qualquer entrada:

```c
#include <stdio.h>

int main(void) {
    int valor;
    double desconto;
    scanf("%d", &valor);

    desconto = 10 / 100 * valor;

    printf("Desconto: R$ %.2f\n", desconto);
    return 0;
}
```
Explique por que o erro ocorre e escreva o programa corrigido completo.

---

### `B01-C03` *(Programa Completo Independente — Caixa Eletrônico com 4 Cédulas)*
Escreva um programa completo em C que leia um valor monetário inteiro (`int quantia`, `quantia >= 0`) e determine a menor quantidade de cédulas de R$ 50, R$ 20, R$ 10 e moedas de R$ 1 para pagá-lo.  
A saída deve imprimir exatamente:
```text
Cedulas de 50: %d\n
Cedulas de 20: %d\n
Cedulas de 10: %d\n
Cedulas de 1: %d\n
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `B02` (`Precedência Aritmética, Cast, <math.h> e Atribuições Compostas`):** somente após autocorreção dos exercícios `B01-E01..E05` **e** **100% (3/3)** na Checagem Independente `B01-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** revisar a distinção entre divisão inteira e real, reforçar a fórmula euclidiana (`dividendo = divisor * quociente + resto`) e aplicar a variante `V2` do bloco.
- **Após 2 tentativas malsucedidas:** retornar para **`A08`** (tipos numéricos em C) e **`A09`** (atribuição e ponto flutuante).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 5 — Operadores aritméticos: adição, subtração, multiplicação, divisão e resto).
- `[DOC]` `Aula_03_Algoritmos.pdf` p. 24 (Ex. 3 — Decomposição posicional de números inteiros).
- `[DOC]` `Aula_05_Algoritmos.pdf` p. 4–13 (Operadores aritméticos, truncamento da divisão inteira, operador `%`).
- `[DOC]` `Lista1_Algoritmos.pdf` p. 1 (Ex. 1 — conversão de segundos para horas, minutos e segundos).
- Casos de teste e soluções verificáveis: [B01_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/gabaritos/B01_gabarito.md) e [B01_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/B01_testes.md).
