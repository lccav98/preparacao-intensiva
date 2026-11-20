# Gabarito Comentado — Bloco `B09` (Combinação de `switch` com `if` e `switch` Aninhado)

> **Bloco de referência:** [B09_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/blocos/B09_bloco.md)  
> **Nota para Caça ao Bug:** O código em `B09-E03` no bloco do aluno contém **erro clássico de escopo do `break`** em `switch` aninhado. Apenas a versão corrigida deve ser compilada.

---

## 1. Gabarito dos Exercícios (`B09-E01` a `B09-E06`)

### `B09-E01` *(Teste de Mesa — Switch Aninhado e Escopo do Break)*
Trecho analisado:
```c
switch (grupo) {
    case 1:
        printf("G1-");
        switch (subgrupo) {
            case 1: printf("S1 "); break;
            case 2: printf("S2 "); break;
        }
    case 2:
        printf("G2 ");
        break;
    default:
        printf("Outro ");
        break;
}
```
1. **Para `grupo = 1` e `subgrupo = 1`:**
   - Entra no `case 1:`, imprime `G1-`.
   - Entra no `switch (subgrupo)`, casa com `case 1:`, imprime `S1 `.
   - O `break` do `case 1:` interno encerra **apenas o `switch (subgrupo)`**.
   - Como o `case 1:` do `switch (grupo)` **não possui `break`**, o fluxo sofre *fall-through* externo para o `case 2:`, imprimindo `G2 `.
   - Encontra o `break` do `case 2:` e sai.
   - Saída: **`G1-S1 G2 \n`**.
2. **Para `grupo = 1` e `subgrupo = 2`:**
   - Entra no `case 1:`, imprime `G1-`.
   - No `switch (subgrupo)`, casa com `case 2:`, imprime `S2 `.
   - Encerra o `switch` interno, cai no `case 2:` externo, imprime `G2 `.
   - Saída: **`G1-S2 G2 \n`**.
3. **Correção:** Inserir `break;` logo após o fechamento da chave `}` do `switch (subgrupo)`, finalizando o `case 1:` do `switch (grupo)`.

---

### `B09-E02` *(Teste de Mesa — Colapso por Divisão Inteira `pontos / 10`)*
- **a) `pontos = 50`:** `50 / 10 == 5` $\rightarrow$ **`Nivel 5\n`**.
- **b) `pontos = 48`:** `48 / 10 == 4` (divisão inteira trunca) $\rightarrow$ **`Nivel 4\n`**.
- **c) `pontos = 39`:** `39 / 10 == 3` $\rightarrow$ **`Nivel 3\n`**.
- **d) `pontos = 25`:** `25 / 10 == 2` $\rightarrow$ cai no `default` $\rightarrow$ **`Nivel Inicial\n`**.
- **e) `pontos = 4`:** `4 / 10 == 0` $\rightarrow$ cai no `default` $\rightarrow$ **`Nivel Inicial\n`**.

---

### `B09-E03` *(Caça ao Bug — Break no nível incorreto)*
1. **Comportamento para `1 1`:**
   - Imprime `Prato: Peixe\n`.
   - No `switch (bebida)`, imprime `Bebida: Suco\n`.
   - O `break` encerra o `switch` da bebida, mas não havia `break` no `case 1` do prato. O programa sofre *fall-through* e imprime indevidamente `Prato: Frango\n`!
2. **Solução corrigida completa:** [B09_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B09_E03_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int prato, bebida;

    if (scanf("%d %d", &prato, &bebida) != 2) {
        return 1;
    }

    switch (prato) {
        case 1:
            printf("Prato: Peixe\n");
            switch (bebida) {
                case 1:
                    printf("Bebida: Suco\n");
                    break;
                case 2:
                    printf("Bebida: Agua\n");
                    break;
                default:
                    printf("Bebida Invalida\n");
                    break;
            }
            break;

        case 2:
            printf("Prato: Frango\n");
            switch (bebida) {
                case 1:
                    printf("Bebida: Suco\n");
                    break;
                case 2:
                    printf("Bebida: Agua\n");
                    break;
                default:
                    printf("Bebida Invalida\n");
                    break;
            }
            break;

        default:
            printf("Prato Invalido\n");
            break;
    }

    return 0;
}
```

---

### `B09-E04` *(Programa completo — Caixa Eletrônico)*
Arquivo: [B09_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B09_E04.c)
```c
#include <stdio.h>

int main(void) {
    double saldo = 1000.00;
    int op;
    double valor;

    if (scanf("%d", &op) != 1) {
        return 1;
    }

    switch (op) {
        case 1:
            if (scanf("%lf", &valor) != 1) {
                return 1;
            }
            if (valor <= 0.0) {
                printf("Valor Invalido\n");
            } else if (valor > saldo) {
                printf("Saldo Insuficiente\n");
            } else {
                saldo = saldo - valor;
                printf("Saldo Atual: R$ %.2f\n", saldo);
            }
            break;

        case 2:
            if (scanf("%lf", &valor) != 1) {
                return 1;
            }
            if (valor <= 0.0) {
                printf("Valor Invalido\n");
            } else {
                saldo = saldo + valor;
                printf("Saldo Atual: R$ %.2f\n", saldo);
            }
            break;

        case 3:
            printf("Saldo Atual: R$ %.2f\n", saldo);
            break;

        default:
            printf("Operacao Invalida\n");
            break;
    }

    return 0;
}
```

---

### `B09-E05` *(Programa completo — Conceitos A-F com `nota / 10`)*
Arquivo: [B09_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B09_E05.c)
```c
#include <stdio.h>

int main(void) {
    int nota;

    if (scanf("%d", &nota) != 1) {
        return 1;
    }

    if (nota < 0 || nota > 100) {
        printf("Nota Invalida\n");
    } else {
        switch (nota / 10) {
            case 10:
            case 9:
                printf("Conceito A\n");
                break;
            case 8:
                printf("Conceito B\n");
                break;
            case 7:
                printf("Conceito C\n");
                break;
            case 6:
                printf("Conceito D\n");
                break;
            default:
                printf("Conceito F\n");
                break;
        }
    }

    return 0;
}
```

---

### `B09-E06` *(Programa completo — Totem com Switch Aninhado)*
Arquivo: [B09_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B09_E06.c)
```c
#include <stdio.h>

int main(void) {
    int categoria, item;

    if (scanf("%d %d", &categoria, &item) != 2) {
        return 1;
    }

    switch (categoria) {
        case 1:
            switch (item) {
                case 1:
                    printf("Suco Natural: R$ 7.00\n");
                    break;
                case 2:
                    printf("Refrigerante: R$ 5.00\n");
                    break;
                default:
                    printf("Item Invalido\n");
                    break;
            }
            break;

        case 2:
            switch (item) {
                case 1:
                    printf("Sanduiche: R$ 12.00\n");
                    break;
                case 2:
                    printf("Hamburguer: R$ 18.00\n");
                    break;
                default:
                    printf("Item Invalido\n");
                    break;
            }
            break;

        default:
            printf("Categoria Invalida\n");
            break;
    }

    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`B09-C01` a `B09-C03`)

### `B09-C01` *(Teste de Mesa — Rastreamento de Switch Aninhado com Fall-Through)*
1. **Para `a = 1` e `b = 2`:**
   - `switch (a)` entra em `case 1:`, imprime `A1 `.
   - `switch (b)` entra em `case 2:`, imprime `B2 `. Como não tem `break`, sofre *fall-through* para `case 3:`, imprimindo `B3 `.
   - Encontra o `break` do `case 3:` interno.
   - Encontra o `break` do `case 1:` externo.
   - Saída: **`A1 B2 B3 \n`**.
2. **Para `a = 1` e `b = 4`:**
   - Entra em `case 1:`, imprime `A1 `.
   - No `switch (b)` não casa com `1, 2, 3`, cai no `default`, imprime `BX `.
   - Saída: **`A1 BX \n`**.
3. **Para `a = 2` e `b = 1`:**
   - `switch (a)` casa com `case 2:`, imprime `A2 `. O `switch (b)` sequer é executado!
   - Saída: **`A2 \n`**.

---

### `B09-C02` *(Programa completo — Faixas Etárias Decimais)*
Arquivo: [B09_C02.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B09_C02.c)
```c
#include <stdio.h>

int main(void) {
    int idade;

    if (scanf("%d", &idade) != 1) {
        return 1;
    }

    if (idade < 0 || idade > 120) {
        printf("Idade Invalida\n");
    } else {
        switch (idade / 10) {
            case 0:
                printf("Crianca\n");
                break;
            case 1:
                printf("Jovem\n");
                break;
            case 2:
            case 3:
            case 4:
            case 5:
                printf("Adulto\n");
                break;
            default:
                printf("Idoso\n");
                break;
        }
    }

    return 0;
}
```

---

### `B09-C03` *(Programa completo — Central Telefônica)*
Arquivo: [B09_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B09_C03.c)
```c
#include <stdio.h>

int main(void) {
    int setor, ramal;

    if (scanf("%d %d", &setor, &ramal) != 2) {
        return 1;
    }

    switch (setor) {
        case 1:
            switch (ramal) {
                case 1:
                    printf("Hardware\n");
                    break;
                case 2:
                    printf("Software\n");
                    break;
                default:
                    printf("Ramal Invalido\n");
                    break;
            }
            break;

        case 2:
            switch (ramal) {
                case 1:
                    printf("Contas a Pagar\n");
                    break;
                case 2:
                    printf("Contas a Receber\n");
                    break;
                default:
                    printf("Ramal Invalido\n");
                    break;
            }
            break;

        default:
            printf("Setor Invalido\n");
            break;
    }

    return 0;
}
```
