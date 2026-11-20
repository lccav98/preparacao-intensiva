# Gabarito Comentado — Bloco `B07` (Condicionais Aninhadas e Dangling Else)

> **Bloco de referência:** [B07_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/blocos/B07_bloco.md)  
> **Nota para Caça ao Bug:** Os códigos em `B07-E03` e `B07-C02` no bloco do aluno contêm **erros conceituais de associação sintática e falta de validação prévia**. Apenas as versões corrigidas devem ser compiladas.

---

## 1. Gabarito dos Exercícios (`B07-E01` a `B07-E06`)

### `B07-E01` *(Teste de Mesa — Dangling Else)*
Trecho analisado:
```c
if (a > 0)
    if (b > 0)
        printf("Caso 1\n");
    else
        printf("Caso 2\n");
```
1. **Para `a = 2` e `b = -3`:**
   - `a > 0` $\rightarrow$ `2 > 0` é verdadeiro.
   - Entra no segundo `if`: `b > 0` $\rightarrow$ `-3 > 0` é falso.
   - A CPU executa o `else` (que pertence a `if (b > 0)`).
   - Saída: **`Caso 2\n`**.
2. **Para `a = -2` e `b = 3`:**
   - `a > 0` $\rightarrow$ `-2 > 0` é falso.
   - Como o `if` externo falhou e não possui `else`, o comando inteiro é ignorado.
   - Saída: **nenhuma saída é impressa** (em branco).
3. **Reescrita com chaves para associar o `else` ao `if (a > 0)`:**
```c
if (a > 0) {
    if (b > 0) {
        printf("Caso 1\n");
    }
} else {
    printf("Caso 2\n");
}
```

---

### `B07-E02` *(Completar Solução — Desconto em Passagem)*
- `/* A */`: `idade < 2`
- `/* B */`: `estudante == 1`
- `/* C */`: `tarifa * 0.50`

---

### `B07-E03` *(Caça ao Bug — Associação Incorreta de Else)*
1. **Para `cracha = 1` e `biometria = 0`:**
   - `cracha == 1` é verdadeiro. A CPU avalia `biometria == 1`, que é falso.
   - Como o `else` está sintaticamente associado ao `if (biometria == 1)` mais próximo, o programa imprime: `Cracha Invalido\n`!
   - Erro de lógica/segurança: a mensagem diz que o crachá é inválido, quando na verdade o crachá é válido e o problema foi a biometria ausente.
2. **Para `cracha = 0` e `biometria = 1`:**
   - `cracha == 1` é falso. O programa não entra no bloco e nenhuma mensagem é impressa (o invasor sem crachá não recebe sequer mensagem de recusa!).
3. **Versão corrigida completa:** [B07_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B07_E03_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int cracha, biometria;

    if (scanf("%d %d", &cracha, &biometria) != 2) {
        return 1;
    }

    if (cracha == 1) {
        if (biometria == 1) {
            printf("Acesso Liberado\n");
        } else {
            printf("Biometria Obrigatoria\n");
        }
    } else {
        printf("Cracha Invalido\n");
    }

    return 0;
}
```

---

### `B07-E04` *(Programa completo — Classificação de Triângulos)*
Arquivo: [B07_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B07_E04.c)
```c
#include <stdio.h>

int main(void) {
    double a, b, c;

    if (scanf("%lf %lf %lf", &a, &b, &c) != 3) {
        return 1;
    }

    if (a < b + c && b < a + c && c < a + b) {
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

### `B07-E05` *(Programa completo — Sistema Acadêmico UTFPR)*
Arquivo: [B07_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B07_E05.c)
```c
#include <stdio.h>

int main(void) {
    int freq;
    double nota;

    if (scanf("%d %lf", &freq, &nota) != 2) {
        return 1;
    }

    if (freq < 75) {
        printf("Reprovado por Falta\n");
    } else {
        if (nota >= 7.0) {
            printf("Aprovado\n");
        } else if (nota >= 4.0) {
            printf("Exame Final\n");
        } else {
            printf("Reprovado por Nota\n");
        }
    }

    return 0;
}
```

---

### `B07-E06` *(Programa completo — Crédito Habitacional)*
Arquivo: [B07_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B07_E06.c)
```c
#include <stdio.h>

int main(void) {
    double renda_mensal, valor_parcela;
    int restricoes_spc;

    if (scanf("%lf %lf %d", &renda_mensal, &valor_parcela, &restricoes_spc) != 3) {
        return 1;
    }

    if (restricoes_spc != 0) {
        printf("Credito Recusado: Restricao Cadastral\n");
    } else {
        if (valor_parcela <= renda_mensal * 0.30) {
            printf("Credito Aprovado\n");
        } else {
            printf("Credito Recusado: Parcela Excede Margem\n");
        }
    }

    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`B07-C01` a `B07-C03`)

### `B07-C01` *(Teste de Mesa — Rastreamento de Dangling Else)*
1. `x = 10, y = 5`: `x > 5` é verdadeiro. `y > 10` é falso $\rightarrow$ salta para o `else` interno $\rightarrow$ imprime **`Beta\n`**.
2. `x = 3, y = 20`: `x > 5` é falso $\rightarrow$ salta para o `else` externo $\rightarrow$ imprime **`Gama\n`**.
3. `x = 8, y = 12`: `x > 5` é verdadeiro. `y > 10` é verdadeiro $\rightarrow$ imprime **`Alpha\n`**.

---

### `B07-C02` *(Caça ao Bug — Triângulo sem validação prévia)*
1. **Exemplo de falha:** Os lados `1.0, 2.0, 10.0`. Como $1.0 + 2.0 = 3.0 < 10.0$, eles não podem fechar um polígono e não formam triângulo. No entanto, como nenhum lado é igual ao outro, o código ingênuo cai no último `else` e imprime absurdamente `Escaleno`!
2. **Solução corrigida completa:** [B07_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B07_C02_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    double a, b, c;

    if (scanf("%lf %lf %lf", &a, &b, &c) != 3) {
        return 1;
    }

    if (a < b + c && b < a + c && c < a + b) {
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

### `B07-C03` *(Programa completo — Triagem de Doação de Sangue)*
Arquivo: [B07_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B07_C03.c)
```c
#include <stdio.h>

int main(void) {
    int idade, jejum_horas;
    double peso;

    if (scanf("%d %lf %d", &idade, &peso, &jejum_horas) != 3) {
        return 1;
    }

    if (idade < 16 || idade > 69) {
        printf("Impedimento: Idade Fora da Faixa\n");
    } else {
        if (peso < 50.0) {
            printf("Impedimento: Peso Insuficiente\n");
        } else {
            if (jejum_horas < 2 || jejum_horas > 12) {
                printf("Impedimento: Jejum Inadequado\n");
            } else {
                printf("Apto para Doacao\n");
            }
        }
    }

    return 0;
}
```
