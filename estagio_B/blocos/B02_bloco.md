# Bloco `B02` — Precedência Aritmética, Conversão de Tipos (*Cast*), `<math.h>` e Atribuições Compostas

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio B — Expressões, Operadores e Estruturas Condicionais / **`B02`** |
| **Micro-habilidade foco** | Aplicar precedência e associatividade aritmética, forçar divisão real por *cast* explícito `(double)` e usar funções de `<math.h>` (`sqrt`) e atribuições compostas (`+=`, `-=`, `*=`, `/=`, `%=`, `++`/`--` isolados). |
| **Pré-requisitos** | `B01` *(Operadores aritméticos, divisão inteira e resto `%`)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão única de prática + checagem (24 min):** `14 min` resol. \| `6 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Não utilize** comandos de desvio condicional (`if`, `switch`), operadores relacionais (`<`, `==`), operadores lógicos (`&&`, `||`, `!`), laços (`while`, `for`) ou vetores. Utilize apenas tipos básicos (`int`, `double`), *cast* explícito, biblioteca `<math.h>` com `-lm`, operadores compostos e E/S. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Hierarquia de Precedência:**  
   $$( \dots ) \quad > \quad \text{Cast } (tipo) \quad > \quad * \;/\; \% \quad > \quad + \;-$$  
   Operadores de mesma prioridade são avaliados da **esquerda para a direita** (associatividade à esquerda).
2. **Uso Defensivo de Parênteses:** Sempre use parênteses para agrupar numeradores e denominadores compostos. Escrever `a + b / 2.0` calcula $a + \frac{b}{2}$; para calcular a média, escreva obrigatoriamente `(a + b) / 2.0`.
3. **Conversão Explícita de Tipo (*Cast*):** Escrever `(double)a / b` converte o valor de `a` para `double` antes da divisão, promovendo `b` e forçando uma divisão real. Cuidado: `(double)(a / b)` calcula primeiro a divisão inteira truncada e só depois converte o quociente para real!
4. **Funções Matemáticas (`<math.h>` e `-lm`):** Para usar `sqrt(x)` (raiz quadrada), inclua `#include <math.h>`. No compilador GCC em ambiente Linux, é **obrigatório** passar a flag `-lm` no final do comando de ligação: `gcc -std=c99 programa.c -lm -o programa`.
5. **Atribuições Compostas e Incremento:**  
   - `x += 5;` equivale a `x = x + 5;` (igualmente para `-=`, `*=`, `/=`, `%=`).  
   - Use `x++;` e `x--;` **apenas como comandos isolados** em sua própria linha para evitar comportamentos ambíguos ou dependentes de ordem de avaliação.

---

## 2. Exemplos Guiados

### Exemplo 1 — A Armadilha do Parêntese no Denominador *(Trecho ilustrativo)*
Deseja-se calcular $y = \frac{x}{2a}$ em C com variáveis `double`:

```c
/* FORMA ERRADA: divide por 2 e multiplica o resultado por a */
y = x / 2.0 * a;

/* FORMA CORRETA: parenteses no produto do divisor */
y = x / (2.0 * a);
```
Se `x = 10.0` e `a = 5.0`, o correto é $10 / (2 \times 5) = 1.0$. A forma errada calcularia $(10 / 2) \times 5 = 25.0$.

### Exemplo 2 — Cast Explícito vs. Promoção Tardia *(Trecho ilustrativo)*
Dadas duas notas inteiras `int soma = 15, qtd = 2;`:

```c
double m1 = (double)soma / qtd;    /* m1 = 15.0 / 2 = 7.5 (CORRETO) */
double m2 = (double)(soma / qtd);  /* m2 = (double)(7) = 7.0 (TRUNCADO!) */
```

---

## 3. Exercícios (`B02-E01` a `B02-E05`)

### `B02-E01` *(Teste de Mesa / Avaliação de Precedência — Reprodução do Modelo)*
Sem usar o computador, determine o valor e o tipo de cada expressão:
1. `3 + 4 * 2 - 1`
2. `(3 + 4) * (2 - 1)`
3. `10 / 4 * 2`
4. `(double)10 / 4 * 2`
5. `(double)(10 / 4) * 2`
6. Acompanhe o valor de `x` nas instruções: `int x = 5; x += 3; x *= 2; x--;`

---

### `B02-E02` *(Caça ao Bug — Precedência na Fórmula Quadrática)*
Um estudante escreveu o trecho abaixo para calcular uma das raízes de $ax^2 + bx + c = 0$ ($x_1 = \frac{-b + \sqrt{\Delta}}{2a}$):

```c
#include <stdio.h>
#include <math.h>

int main(void) {
    double a, b, c, delta, x1;
    scanf("%lf %lf %lf", &a, &b, &c);

    delta = b * b - 4.0 * a * c;
    x1 = -b + sqrt(delta) / 2 * a;   /* LINHA COM ERROS DE PRECEDENCIA */

    printf("x1 = %.2f\n", x1);
    return 0;
}
```
Identifique os **2 erros de precedência** na linha indicada e escreva a versão corrigida completa.

---

### `B02-E03` *(Completar Solução — Bhaskara Completo)*
Complete o programa em C que lê três coeficientes `a`, `b`, `c` (`double`, com $a \neq 0$ e $\Delta \ge 0$) e calcula as duas raízes $x_1$ e $x_2$:

```c
#include <stdio.h>
#include <math.h>

int main(void) {
    double a, b, c, delta, x1, x2;
    scanf("%lf %lf %lf", &a, &b, &c);

    delta = /* A: calcular delta */;
    x1 = /* B: calcular x1 com parenteses defensivos */;
    x2 = /* C: calcular x2 com parenteses defensivos */;

    printf("x1 = %.2f\n", x1);
    printf("x2 = %.2f\n", x2);
    return 0;
}
```

---

### `B02-E04` *(Completar Solução — Operadores Compostos e Incremento)*
Complete o programa abaixo de controle financeiro simplificado usando apenas operadores de atribuição composta (`+=`, `-=`, `*=`) e operador de incremento isolado:

```c
#include <stdio.h>

int main(void) {
    int saldo, bonus, taxa;
    scanf("%d %d %d", &saldo, &bonus, &taxa);

    /* 1. Somar bonus ao saldo usando atribuicao composta */
    /* 2. Subtrair taxa do saldo usando atribuicao composta */
    /* 3. Dobrar o saldo usando atribuicao composta */
    /* 4. Incrementar o saldo em 1 usando operador isolado */

    printf("Saldo final: %d\n", saldo);
    return 0;
}
```

---

### `B02-E05` *(Resolução Independente — Distância Euclidiana)*
Escreva um programa completo em C que leia as coordenadas cartesianas de dois pontos $P_1(x_1, y_1)$ e $P_2(x_2, y_2)$ como números reais (`double`) e calcule a distância euclidiana entre eles:
$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$
Imprima o resultado formatado exatamente como: `Distancia: %.2f\n`.

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `B02-C01` *(Teste de Mesa / Avaliação Mental)*
Acompanhe no papel o valor final de cada variável:
```c
int a = 7, b = 2;
double c;
a += 3;
c = (double)a / b;
b *= 4;
a--;
```
Informe os valores exatos de `a`, `b` e `c`.

---

### `B02-C02` *(Caça ao Bug — Média Ponderada)*
O programa a seguir deveria calcular a média ponderada de três notas inteiras com pesos 2, 3 e 5:
$$\text{Média} = \frac{n_1 \times 2 + n_2 \times 3 + n_3 \times 5}{10}$$

```c
#include <stdio.h>

int main(void) {
    int n1, n2, n3;
    double media;
    scanf("%d %d %d", &n1, &n2, &n3);

    media = n1 * 2 + n2 * 3 + n3 * 5 / 10;

    printf("Media: %.2f\n", media);
    return 0;
}
```
Aponte os defeitos do cálculo e escreva o programa corrigido completo.

---

### `B02-C03` *(Programa Completo Independente — Hipotenusa com `-lm`)*
Escreva um programa completo em C que leia o comprimento de dois catetos inteiros `a` e `b` de um triângulo retângulo e calcule o comprimento da hipotenusa $h = \sqrt{a^2 + b^2}$.  
Utilize *cast* explícito `(double)` ao alimentar a função `sqrt` e imprima exatamente: `Hipotenusa: %.2f\n`.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `B03` (`Expressões Relacionais, <stdbool.h> e if Simples`):** somente após autocorreção dos exercícios `B02-E01..E05` **e** **100% (3/3)** na Checagem Independente `B02-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** revisar tabelas de precedência, parentetização de expressões algébricas e compilação de `<math.h>` com `-lm`.
- **Após 2 tentativas malsucedidas:** retornar para **`B01`** (divisão inteira vs. real) e **`A02`** (sintaxe básica do GCC e opções de compilação).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 5 — Precedência e associatividade de operadores aritméticos; conversão de tipos).
- `[DOC]` `Aula_02_Algoritmos.pdf` p. 5 (Inclusão de `<math.h>` e uso da flag de ligação `-lm`).
- `[DOC]` `Aula_05_Algoritmos.pdf` p. 14–24 (Precedência, operadores de atribuição composta e conversão explícita/cast).
- `[DOC]` `Lista1_Algoritmos.pdf` p. 1–2 (Ex. 2 — fórmulas algébricas e raízes com `<math.h>`).
- Casos de teste e soluções verificáveis: [B02_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/gabaritos/B02_gabarito.md) e [B02_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/B02_testes.md).
