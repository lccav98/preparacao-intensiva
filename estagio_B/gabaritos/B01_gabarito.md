# Gabarito Comentado — Bloco `B01` (Operadores Aritméticos, Divisão Inteira e Resto `%`)

> **Bloco de referência:** [B01_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/blocos/B01_bloco.md)  
> **Nota para Caça ao Bug:** O código em `B01-C02` no bloco do aluno contém erro intencional de divisão inteira truncada (`10 / 100`). Apenas a versão corrigida deve ser compilada.

---

## 1. Gabarito dos Exercícios (`B01-E01` a `B01-E05`)

### `B01-E01` *(Teste de Mesa / Previsão Mental)*
- **a) `5 / 2`:** Ambos os operandos são inteiros (`int`). O operador `/` realiza **divisão inteira truncada**, descartando a parte decimal. Resultado: **`2`**.
- **b) `5.0 / 2`:** Pelo menos um operando é ponto flutuante (`double`). O operador `/` realiza **divisão real**. Resultado: **`2.5`**.
- **c) `double r = 5 / 2;`:** O lado direito da atribuição (`5 / 2`) é avaliado primeiro pelo compilador como divisão inteira, resultando em `2`. Somente depois esse `2` é promovido e armazenado em `r`. Resultado armazenado em `r`: **`2.0`**. *(Atenção: o tipo da variável receptora NÃO altera o tipo da operação no lado direito!)*
- **d) `17 % 5`:** Resto da divisão inteira de 17 por 5 (`17 = 5 * 3 + 2`). Resultado: **`2`**.
- **e) `7 % 10`:** Como 7 é menor que 10, o quociente inteiro é 0 e o resto é o próprio 7 (`7 = 10 * 0 + 7`). Resultado: **`7`**.
- **f) `4 * (10 / 3) + (10 % 3)`:** `10 / 3` vale `3`; `10 % 3` vale `1`. Logo: `4 * 3 + 1 = 12 + 1 = 13`. Resultado: **`13`**.

---

### `B01-E02` *(Completar Solução — Decomposição de Notas)*
Arquivo: [B01_E02.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B01_E02.c)
```c
#include <stdio.h>

int main(void) {
    int valor, notas20, moedas1;
    scanf("%d", &valor);

    notas20 = valor / 20;
    moedas1 = valor % 20;

    printf("Notas de 20: %d\n", notas20);
    printf("Moedas de 1: %d\n", moedas1);
    return 0;
}
```

---

### `B01-E03` *(Completar Solução — Segundos em Minutos e Segundos)*
Arquivo: [B01_E03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B01_E03.c)
```c
#include <stdio.h>

int main(void) {
    int total_seg, minutos, segundos;
    scanf("%d", &total_seg);

    minutos = total_seg / 60;
    segundos = total_seg % 60;

    printf("Minutos: %d\n", minutos);
    printf("Segundos: %d\n", segundos);
    return 0;
}
```

---

### `B01-E04` *(Resolver com Pistas — Horas, Minutos e Segundos Compacto)*
Arquivo: [B01_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B01_E04.c)
```c
#include <stdio.h>

int main(void) {
    int seg_totais, horas, resto, minutos, segundos;
    scanf("%d", &seg_totais);

    horas = seg_totais / 3600;
    resto = seg_totais % 3600;
    minutos = resto / 60;
    segundos = resto % 60;

    printf("%d h %d m %d s\n", horas, minutos, segundos);
    return 0;
}
```

---

### `B01-E05` *(Resolução Independente — Decomposição Horária Detalhada)*
Arquivo: [B01_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B01_E05.c)
```c
#include <stdio.h>

int main(void) {
    int tempo_seg, h, m, s, resto;
    scanf("%d", &tempo_seg);

    h = tempo_seg / 3600;
    resto = tempo_seg % 3600;
    m = resto / 60;
    s = resto % 60;

    printf("Horas: %d\n", h);
    printf("Minutos: %d\n", m);
    printf("Segundos: %d\n", s);
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`B01-C01` a `B01-C03`)

### `B01-C01` *(Teste de Mesa / Avaliação Mental)*
1. `14 / 4` = **`3`** (divisão inteira truncada; `14 / 4 = 3.5` → parte inteira `3`).
2. `14 % 4` = **`2`** (resto da divisão inteira: `14 = 4 * 3 + 2`).
3. `double x = 14 / 4;` = **`3.0`** (o lado direito resulta em `3`; `x` recebe `3.0`).
4. `14.0 / 4` = **`3.5`** (`14.0` é `double`, forçando divisão real).
5. `3 % 8` = **`3`** (quociente inteiro é `0`, resto é `3`).

---

### `B01-C02` *(Caça ao Bug — Correção de Desconto Percentual)*
- **Erro intencional:** Em `desconto = 10 / 100 * valor;`, os números `10` e `100` são inteiros literais. O compilador calcula `10 / 100` como divisão inteira, que resulta em **`0`**. Em seguida, `0 * valor` resulta sempre em `0`, e qualquer compra fica com `R$ 0.00` de desconto.
- **Correção:** Forçar a divisão real usando literais de ponto flutuante: `(10.0 / 100.0) * valor` ou `0.10 * valor`.
- **Solução corrigida completa:** [B01_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B01_C02_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int valor;
    double desconto;
    scanf("%d", &valor);

    desconto = (10.0 / 100.0) * valor;

    printf("Desconto: R$ %.2f\n", desconto);
    return 0;
}
```

---

### `B01-C03` *(Programa Completo — Caixa Eletrônico com 4 Cédulas)*
Arquivo: [B01_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B01_C03.c)
```c
#include <stdio.h>

int main(void) {
    int quantia, n50, n20, n10, n1, resto;
    scanf("%d", &quantia);

    n50 = quantia / 50;
    resto = quantia % 50;

    n20 = resto / 20;
    resto = resto % 20;

    n10 = resto / 10;
    n1 = resto % 10;

    printf("Cedulas de 50: %d\n", n50);
    printf("Cedulas de 20: %d\n", n20);
    printf("Cedulas de 10: %d\n", n10);
    printf("Cedulas de 1: %d\n", n1);
    return 0;
}
```
