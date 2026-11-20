# Gabarito Comentado — Bloco `B02` (Precedência Aritmética, Cast, `<math.h>` e Atribuições Compostas)

> **Bloco de referência:** [B02_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/blocos/B02_bloco.md)  
> **Nota para Caça ao Bug:** Os códigos em `B02-E02` e `B02-C02` contêm **erros intencionais** de precedência e ausência de cast. Apenas as versões corrigidas devem ser compiladas.

---

## 1. Gabarito dos Exercícios (`B02-E01` a `B02-E05`)

### `B02-E01` *(Teste de Mesa / Avaliação de Precedência)*
- **a) `3 + 4 * 2 - 1`:** A multiplicação `*` tem maior precedência que `+` e `-`. Logo: `3 + 8 - 1 = 11 - 1 = 10`. Resultado: **`10`**.
- **b) `(3 + 4) * (2 - 1)`:** Parênteses têm prioridade máxima. Logo: `7 * 1 = 7`. Resultado: **`7`**.
- **c) `10 / 4 * 2`:** `/` e `*` têm a mesma precedência e associatividade da esquerda para a direita. Primeiro é calculado `10 / 4` (divisão inteira truncada = `2`), e depois `2 * 2 = 4`. Resultado: **`4`**.
- **d) `(double)10 / 4 * 2`:** O *cast* `(double)` aplica-se imediatamente ao `10`, tornando-o `10.0`. Em seguida, `10.0 / 4` produz `2.5` (divisão real). Por fim, `2.5 * 2 = 5.0`. Resultado: **`5.0`**.
- **e) `(double)(10 / 4) * 2`:** O parêntese interno é avaliado primeiro: `10 / 4` é divisão inteira que trunca para `2`. O *cast* converte esse `2` para `2.0`. Por fim, `2.0 * 2 = 4.0`. Resultado: **`4.0`**.
- **f) `int x = 5; x += 3; x *= 2; x--;`:**  
  1. `x += 3` equivale a `x = x + 3` $\to x = 8$.  
  2. `x *= 2` equivale a `x = x * 2` $\to x = 16$.  
  3. `x--` decrementa 1 $\to x = 15$.  
  Valor final de `x`: **`15`**.

---

### `B02-E02` *(Caça ao Bug — Precedência em Bhaskara)*
- **Erros intencionais:**
  1. **Falta de parênteses no numerador:** Em `-b + sqrt(delta) / 2 * a`, a divisão `/` tem precedência sobre a adição `+`. O compilador calcula `sqrt(delta) / 2` antes de somar `-b`.
  2. **Falta de parênteses no denominador:** Pela associatividade esquerda-direita, `/ 2 * a` divide por 2 e em seguida multiplica todo o resultado por `a`, quando deveria dividir pelo produto `(2.0 * a)`.
- **Solução corrigida completa:** [B02_E02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B02_E02_corrigido.c)
```c
#include <stdio.h>
#include <math.h>

int main(void) {
    double a, b, c, delta, x1;
    scanf("%lf %lf %lf", &a, &b, &c);

    delta = b * b - 4.0 * a * c;
    x1 = (-b + sqrt(delta)) / (2.0 * a);

    printf("x1 = %.2f\n", x1);
    return 0;
}
```

---

### `B02-E03` *(Completar Solução — Bhaskara Completo)*
Arquivo: [B02_E03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B02_E03.c)
```c
#include <stdio.h>
#include <math.h>

int main(void) {
    double a, b, c, delta, x1, x2;
    scanf("%lf %lf %lf", &a, &b, &c);

    delta = b * b - 4.0 * a * c;
    x1 = (-b + sqrt(delta)) / (2.0 * a);
    x2 = (-b - sqrt(delta)) / (2.0 * a);

    printf("x1 = %.2f\n", x1);
    printf("x2 = %.2f\n", x2);
    return 0;
}
```

---

### `B02-E04` *(Completar Solução — Operadores Compostos e Incremento)*
Arquivo: [B02_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B02_E04.c)
```c
#include <stdio.h>

int main(void) {
    int saldo, bonus, taxa;
    scanf("%d %d %d", &saldo, &bonus, &taxa);

    saldo += bonus;
    saldo -= taxa;
    saldo *= 2;
    saldo++;

    printf("Saldo final: %d\n", saldo);
    return 0;
}
```

---

### `B02-E05` *(Resolução Independente — Distância Euclidiana)*
Arquivo: [B02_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B02_E05.c)
```c
#include <stdio.h>
#include <math.h>

int main(void) {
    double x1, y1, x2, y2, dist;
    scanf("%lf %lf %lf %lf", &x1, &y1, &x2, &y2);

    dist = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));

    printf("Distancia: %.2f\n", dist);
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`B02-C01` a `B02-C03`)

### `B02-C01` *(Teste de Mesa — Cast e Atribuições Compostas)*
Considere as instruções:
```c
int a = 7, b = 2;
double c;
a += 3;              /* a = 10 */
c = (double)a / b;   /* c = 10.0 / 2 = 5.0 */
b *= 4;              /* b = 2 * 4 = 8 */
a--;                 /* a = 10 - 1 = 9 */
```
Valores finais:
- `a` = **`9`**
- `b` = **`8`**
- `c` = **`5.0`**

---

### `B02-C02` *(Caça ao Bug — Média Ponderada)*
- **Erros intencionais:**
  1. Em `n1 * 2 + n2 * 3 + n3 * 5 / 10`, a divisão `n3 * 5 / 10` é realizada antes das adições devido à precedência de `/` sobre `+`.
  2. Como `n1`, `n2` e `n3` são inteiros, a divisão por `10` trunca o resultado antes de atribuir à variável `media`.
- **Correção:** Isolar todo o numerador com parênteses e realizar *cast* ou dividir por `10.0`: `(double)(n1 * 2 + n2 * 3 + n3 * 5) / 10.0`.
- **Solução corrigida completa:** [B02_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B02_C02_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int n1, n2, n3;
    double media;
    scanf("%d %d %d", &n1, &n2, &n3);

    media = (double)(n1 * 2 + n2 * 3 + n3 * 5) / 10.0;

    printf("Media: %.2f\n", media);
    return 0;
}
```

---

### `B02-C03` *(Programa Completo Independente — Hipotenusa com `-lm`)*
Arquivo: [B02_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B02_C03.c)
```c
#include <stdio.h>
#include <math.h>

int main(void) {
    int a, b;
    double hipotenusa;
    scanf("%d %d", &a, &b);

    hipotenusa = sqrt((double)(a * a + b * b));

    printf("Hipotenusa: %.2f\n", hipotenusa);
    return 0;
}
```
*(Lembrete de compilação GCC: obrigatório incluir a flag `-lm` ao final da linha de comando para ligar a biblioteca matemática).*
