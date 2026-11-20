# Gabarito Comentado — Bloco `B10` (Revisão e Consolidação do Estágio B)

> **Bloco de referência:** [B10_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/blocos/B10_bloco.md)  
> **Nota de Consolidação:** Este bloco consolida todas as micro-habilidades dos blocos `B01` a `B09` sem nenhum conteúdo novo. Todas as soluções devem ser estritamente compiláveis em `-std=c99 -Wall -Wextra` (com `-lm` nos exercícios que utilizam `sqrt`).

---

## 1. Gabarito dos Exercícios (`B10-E01` a `B10-E06`)

### `B10-E01` *(Teste de Mesa Integrador)*
Variáveis: `x = 15, y = 4, z = 2`.
1. **Avaliação de `cond1 = (x / y == 3) && (x % y != 0)`:**
   - `x / y` $\rightarrow$ `15 / 4` é `3` (divisão inteira). `3 == 3` é `1` (verdadeiro).
   - `x % y` $\rightarrow$ `15 % 4` é `3`. `3 != 0` é `1` (verdadeiro).
   - `1 && 1` $\rightarrow$ **`cond1 = 1`**.
2. **Avaliação de `cond2 = !(z > y) || (x + y * z > 25)`:**
   - `z > y` $\rightarrow$ `2 > 4` é `0`. `!(0)` resulta em `1`.
   - Por **curto-circuito** no `||`, o termo `(x + y * z > 25)` nem precisa ser avaliado!
   - Resultado: **`cond2 = 1`**.
3. **Execução condicional:**
   - `if (cond1)` entra no bloco interno.
   - `if (cond2)` avalia para verdadeiro e executa `printf("A-%d\n", x % z);`.
   - `x % z` $\rightarrow$ `15 % 2` é `1`.
   - Linha impressa: **`A-1\n`**.

---

### `B10-E02` *(Caça ao Bug — Precisão de Fronteiras e Lacunas)*
1. **Problemas do código original:**
   - **Precisão de `float`:** O tipo `float` possui apenas 24 bits de mantissa (~6-7 dígitos de precisão decimal), acumulando erros de arredondamento em limites como `10000.0f` e `25000.0f`. Deve-se utilizar `double` com `%lf`.
   - **Lacuna de fronteira:** A condição `lucro <= 24999.99` deixa de fora qualquer valor entre `24999.99` e `25000.00` (ex.: `lucro = 24999.995`), que cairia erroneamente no ramo de 15% em vez de 10%. A forma correta e sem lacunas é `lucro <= 25000.0`.
2. **Solução corrigida completa:** [B10_E02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B10_E02_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    double lucro, imposto;

    if (scanf("%lf", &lucro) != 1) {
        return 1;
    }

    if (lucro < 10000.0) {
        imposto = 0.0;
    } else if (lucro <= 25000.0) {
        imposto = lucro * 0.10;
    } else {
        imposto = lucro * 0.15;
    }

    printf("Imposto: R$ %.2f\n", imposto);
    return 0;
}
```

---

### `B10-E03` *(Teste de Mesa — Switch com Fall-Through e Aritmética Modular)*
Trecho analisado:
```c
int chave = (num % 5);
switch (chave) {
    case 1: printf("Um "); break;
    case 2: printf("Dois "); /* Sem break */
    case 3: printf("Tres "); break;
    case 4: printf("Quatro "); break;
    default: printf("Outro "); break;
}
```
1. **Para `num = 17`:**
   - `17 % 5` $\rightarrow$ resto `2`.
   - Entra no `case 2:`, imprime `Dois `. Como não há `break`, sofre *fall-through* para o `case 3:` e imprime `Tres `. Encontra o `break` e sai.
   - Saída: **`Dois Tres \n`**.
2. **Para `num = 20`:**
   - `20 % 5` $\rightarrow$ resto `0`.
   - Não casa com `1..4`, cai no `default:`.
   - Saída: **`Outro \n`**.
3. **Para `num = 14`:**
   - `14 % 5` $\rightarrow$ resto `4`.
   - Casa com `case 4:`, imprime `Quatro `.
   - Saída: **`Quatro \n`**.

---

### `B10-E04` *(Programa completo — Bhaskara com Validações)*
Arquivo: [B10_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B10_E04.c)
```c
#include <stdio.h>
#include <math.h>

int main(void) {
    double a, b, c;

    if (scanf("%lf %lf %lf", &a, &b, &c) != 3) {
        return 1;
    }

    if (a == 0.0) {
        printf("Nao e equacao de segundo grau\n");
    } else {
        double delta = b * b - 4.0 * a * c;
        if (delta < 0.0) {
            printf("Sem raizes reais\n");
        } else if (delta == 0.0) {
            double x = -b / (2.0 * a);
            printf("Raiz unica: %.2f\n", x);
        } else {
            double x1 = (-b + sqrt(delta)) / (2.0 * a);
            double x2 = (-b - sqrt(delta)) / (2.0 * a);
            printf("Raizes: %.2f e %.2f\n", x1, x2);
        }
    }

    return 0;
}
```

---

### `B10-E05` *(Programa completo — Calendário e Ano Bissexto)*
Arquivo: [B10_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B10_E05.c)
```c
#include <stdio.h>

int main(void) {
    int dia, mes, ano;

    if (scanf("%d %d %d", &dia, &mes, &ano) != 3) {
        return 1;
    }

    if (ano <= 0 || mes < 1 || mes > 12) {
        printf("Data Invalida\n");
    } else {
        int bissexto = ((ano % 4 == 0 && ano % 100 != 0) || (ano % 400 == 0));
        int limite_dias;

        if (mes == 2) {
            if (bissexto) {
                limite_dias = 29;
            } else {
                limite_dias = 28;
            }
        } else if (mes == 4 || mes == 6 || mes == 9 || mes == 11) {
            limite_dias = 30;
        } else {
            limite_dias = 31;
        }

        if (dia >= 1 && dia <= limite_dias) {
            if (bissexto) {
                printf("Data Valida: Bissexto\n");
            } else {
                printf("Data Valida: Nao Bissexto\n");
            }
        } else {
            printf("Data Invalida\n");
        }
    }

    return 0;
}
```

---

### `B10-E06` *(Programa completo — Tarifas de Energia Elétrica)*
Arquivo: [B10_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B10_E06.c)
```c
#include <stdio.h>

int main(void) {
    int tipo;
    double kwh;

    if (scanf("%d %lf", &tipo, &kwh) != 2) {
        return 1;
    }

    if (kwh < 0.0) {
        printf("Consumo Invalido\n");
    } else {
        double valor;
        switch (tipo) {
            case 1:
                if (kwh <= 100.0) {
                    valor = kwh * 0.60;
                } else {
                    valor = 60.00 + (kwh - 100.0) * 0.85;
                }
                printf("Fatura Residencial: R$ %.2f\n", valor);
                break;

            case 2:
                if (kwh <= 200.0) {
                    valor = kwh * 0.75;
                } else {
                    valor = 150.00 + (kwh - 200.0) * 0.95;
                }
                printf("Fatura Comercial: R$ %.2f\n", valor);
                break;

            case 3:
                valor = 300.00 + kwh * 0.50;
                printf("Fatura Industrial: R$ %.2f\n", valor);
                break;

            default:
                printf("Tipo Invalido\n");
                break;
        }
    }

    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`B10-C01` a `B10-C03`)

### `B10-C01` *(Teste de Mesa Integrador)*
Variáveis: `a = 10, b = 20, c = 5`.
1. `r1 = (a < b) && (b / c == 4)`:
   - `10 < 20` é `1`.
   - `20 / 5 == 4` é `1`.
   - `1 && 1` $\rightarrow$ **`r1 = 1`**.
2. `r2 = !(a + c == 15) || (b % c == 0)`:
   - `a + c` $\rightarrow$ `10 + 5 == 15` é `1`. `!(1)` é `0`.
   - Avalia o segundo termo: `b % c` $\rightarrow$ `20 % 5` é `0`. `0 == 0` é `1`.
   - `0 || 1` $\rightarrow$ **`r2 = 1`**.
3. `if (r1 && r2)` é verdadeiro.
   - Avalia `b - a > c` $\rightarrow$ `20 - 10 > 5` $\rightarrow$ `10 > 5` é verdadeiro.
   - Saída: **`Resultado Alpha\n`**.

---

### `B10-C02` *(Programa completo — Triângulo, Classificação e Heron)*
Arquivo: [B10_C02.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B10_C02.c)
```c
#include <stdio.h>
#include <math.h>

int main(void) {
    double a, b, c;

    if (scanf("%lf %lf %lf", &a, &b, &c) != 3) {
        return 1;
    }

    if (a < b + c && b < a + c && c < a + b) {
        double s = (a + b + c) / 2.0;
        double area = sqrt(s * (s - a) * (s - b) * (s - c));

        if (a == b && b == c) {
            printf("Equilatero - Area: %.2f\n", area);
        } else if (a == b || a == c || b == c) {
            printf("Isosceles - Area: %.2f\n", area);
        } else {
            printf("Escaleno - Area: %.2f\n", area);
        }
    } else {
        printf("Invalido\n");
    }

    return 0;
}
```

---

### `B10-C03` *(Programa completo — Salário Líquido com INSS e IRRF)*
Arquivo: [B10_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B10_C03.c)
```c
#include <stdio.h>

int main(void) {
    double salario_bruto;
    int dependentes;

    if (scanf("%lf %d", &salario_bruto, &dependentes) != 2) {
        return 1;
    }

    if (salario_bruto <= 0.0 || dependentes < 0) {
        printf("Entrada Invalida\n");
    } else {
        double inss;
        if (salario_bruto <= 1412.00) {
            inss = salario_bruto * 0.075;
        } else if (salario_bruto <= 2666.00) {
            inss = salario_bruto * 0.09;
        } else if (salario_bruto <= 4000.00) {
            inss = salario_bruto * 0.12;
        } else {
            inss = 550.00;
        }

        double base_irrf = salario_bruto - inss - (dependentes * 189.59);
        if (base_irrf < 0.0) {
            base_irrf = 0.0;
        }

        double irrf;
        if (base_irrf <= 2259.20) {
            irrf = 0.0;
        } else if (base_irrf <= 2826.65) {
            irrf = base_irrf * 0.075;
        } else if (base_irrf <= 3751.05) {
            irrf = base_irrf * 0.15;
        } else {
            irrf = base_irrf * 0.225;
        }

        double liquido = salario_bruto - inss - irrf;

        printf("INSS: R$ %.2f\n", inss);
        printf("IRRF: R$ %.2f\n", irrf);
        printf("Liquido: R$ %.2f\n", liquido);
    }

    return 0;
}
```
