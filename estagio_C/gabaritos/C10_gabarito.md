# Gabarito Comentado — Bloco `C10` (Revisão e Consolidação do Estágio C)

> **Bloco de referência:** [C10_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/blocos/C10_bloco.md)  
> **Nota de Consolidação:** Este bloco integra todas as micro-habilidades de `C01` a `C09` sem nenhum conteúdo novo. Todas as soluções compilam em `-std=c99 -Wall -Wextra` sem vetores e sem funções auxiliares além de `int main(void)`.

---

## 1. Gabarito dos Exercícios (`C10-E01` a `C10-E06`)

### `C10-E01` *(Teste de Mesa Integrado — `for`, `continue` e Laços Aninhados)*
1. **Na iteração `i = 2`:** A condição `i == 2` é verdadeira, acionando `continue`. Todo o restante do corpo do laço externo (incluindo o laço interno de `j` e o `printf("\n");`) é saltado; a execução passa diretamente para `i++` (`i = 3`).
2. **Rastreamento:**
   - `i = 1`: `j = 1` $\rightarrow$ `i+j = 2` (`total = 2`), imprime ` 2\n`.
   - `i = 2`: `continue` (nada impresso, `total` permanece `2`).
   - `i = 3`: `j = 1, 2, 3` $\rightarrow$ `4, 5, 6` (`total = 2 + 4 + 5 + 6 = 17`), imprime ` 4 5 6\n`.
   - `i = 4`: `j = 1, 2, 3, 4` $\rightarrow$ `5, 6, 7, 8` (`total = 17 + 5 + 6 + 7 + 8 = 43`), imprime ` 5 6 7 8\n`.

**Saída Exata:**
```text
 2
 4 5 6
 5 6 7 8
Total = 43
```

---

### `C10-E02` *(Caça ao Bug 1 — Sentinela, `continue` em `while` e Máximo com Negativos)*
1. **Os 3 bugs do código original:**
   - **Bug 1 (Variável `num` não inicializada no teste `while (num != -1)`):** Como não há *priming read* antes do laço, o primeiro teste lê lixo de memória (comportamento indefinido).
   - **Bug 2 (Sentinela `-1` é processada):** Ao digitar `-1`, o `scanf` lê `-1`, ele não é múltiplo de `5`, logo `-1` é somado em `soma` antes do laço testar `num != -1` na volta seguinte! Em entrada vazia (`-1`), o programa imprime `Soma = -1` e `Maior = 0` em vez de `Nenhum valor valido`.
   - **Bug 3 (`maior = 0` falha com números negativos):** Na entrada `-10 -3 -5 -1`, `-10` e `-5` são ignorados e `-3` é o único válido, mas `-3 > 0` é falso, imprimindo `Maior = 0` em vez de `Maior = -3`.
2. **Solução completa corrigida:** [C10_E02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C10_E02_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int num;
    int soma = 0;
    int maior = 0;
    int tem_valido = 0;

    while (1) {
        if (scanf("%d", &num) != 1 || num == -1) {
            break;
        }
        if (num % 5 == 0) {
            continue;
        }
        soma += num;
        if (!tem_valido || num > maior) {
            maior = num;
            tem_valido = 1;
        }
    }

    if (!tem_valido) {
        printf("Nenhum valor valido\n");
    } else {
        printf("Soma = %d\n", soma);
        printf("Maior = %d\n", maior);
    }

    return 0;
}
```

---

### `C10-E03` *(Caça ao Bug 2 — Divisão Inteira e Divisão por Zero em Série Alternada)*
1. **Explicação dos 2 bugs:**
   - **Bug 1 (Divisão por zero por *off-by-one* `k <= n`):** Quando `k` atinge `n`, o denominador `(n - k) * (n - k)` torna-se `0`, causando falha fatal por divisão inteira por zero. O limite correto é `k < n`.
   - **Bug 2 (Divisão inteira truncada):** Tanto `sinal` quanto `(n - k) * (n - k)` são `int`. Para todo `k < n - 1`, o denominador é maior que `1`, truncando `sinal / den` para **`0`**.
2. **Solução completa corrigida:** [C10_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C10_E03_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int n;
    if (scanf("%d", &n) != 1) {
        return 1;
    }

    if (n <= 0) {
        printf("Entrada Invalida\n");
        return 0;
    }

    double soma = 0.0;
    double sinal = 1.0;

    for (int k = 0; k < n; k++) {
        double den = (double)(n - k) * (n - k);
        soma += sinal / den;
        sinal = -sinal;
    }

    printf("S = %.6f\n", soma);
    return 0;
}
```

---

### `C10-E04` *(Menu `do-while` + `switch` Integrando Euclides e Primalidade)*
Solução completa: [C10_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C10_E04.c)
```c
#include <stdio.h>

int main(void) {
    int opcao;

    do {
        if (scanf("%d", &opcao) != 1) {
            break;
        }

        switch (opcao) {
            case 1: {
                long long a, b;
                if (scanf("%lld %lld", &a, &b) != 2) {
                    return 1;
                }
                if (a <= 0 || b <= 0) {
                    printf("Entrada Invalida\n");
                } else {
                    while (b != 0) {
                        long long resto = a % b;
                        a = b;
                        b = resto;
                    }
                    printf("MDC = %lld\n", a);
                }
                break;
            }
            case 2: {
                long long n;
                if (scanf("%lld", &n) != 1) {
                    return 1;
                }
                int primo = 1;
                if (n <= 1) {
                    primo = 0;
                } else if (n == 2) {
                    primo = 1;
                } else if (n % 2 == 0) {
                    primo = 0;
                } else {
                    for (long long d = 3; d * d <= n; d += 2) {
                        if (n % d == 0) {
                            primo = 0;
                            break;
                        }
                    }
                }
                if (primo) {
                    printf("Primo\n");
                } else {
                    printf("Nao Primo\n");
                }
                break;
            }
            case 0:
                printf("Encerrando\n");
                break;
            default:
                printf("Opcao Invalida\n");
                break;
        }
    } while (opcao != 0);

    return 0;
}
```

---

### `C10-E05` *(Sentinela com Estatísticas e Contagem de Primos)*
Solução completa: [C10_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C10_E05.c)
```c
#include <stdio.h>

int main(void) {
    long long num;
    int qtd = 0;
    int qtd_primos = 0;
    long long soma = 0;
    long long maior = 0;

    while (1) {
        if (scanf("%lld", &num) != 1 || num == 0) {
            break;
        }

        qtd++;
        soma += num;
        if (qtd == 1 || num > maior) {
            maior = num;
        }

        int primo = 1;
        if (num <= 1) {
            primo = 0;
        } else if (num == 2) {
            primo = 1;
        } else if (num % 2 == 0) {
            primo = 0;
        } else {
            for (long long d = 3; d * d <= num; d += 2) {
                if (num % d == 0) {
                    primo = 0;
                    break;
                }
            }
        }

        if (primo) {
            qtd_primos++;
        }
    }

    if (qtd == 0) {
        printf("Nenhum numero valido\n");
    } else {
        printf("Qtd: %d\n", qtd);
        printf("Primos: %d\n", qtd_primos);
        printf("Maior: %lld\n", maior);
        printf("Media: %.2f\n", (double)soma / qtd);
    }

    return 0;
}
```

---

### `C10-E06` *(Série Alternada de $\sin(x)$ por Tolerância $\varepsilon$)*
Solução completa: [C10_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C10_E06.c)
```c
#include <stdio.h>

int main(void) {
    double x, eps;
    if (scanf("%lf %lf", &x, &eps) != 2) {
        return 1;
    }

    if (eps <= 0.0) {
        printf("Entrada Invalida\n");
        return 0;
    }

    double soma = 0.0;
    double termo = x;
    int termos = 0;
    int k = 0;

    while (termo >= eps || termo <= -eps) {
        soma += termo;
        termos++;
        k++;
        double fator = (2.0 * k) * (2.0 * k + 1.0);
        termo = -termo * x * x / fator;
    }

    printf("sen(x) aprox: %.6f\n", soma);
    printf("Termos = %d\n", termos);
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`C10-C01` a `C10-C03`)

### `C10-C01` *(Teste de Mesa Integrador — `do-while` + `switch` com *Fall-Through*)*

| Iteração | `x` no início | `x % 3` | Ação no `switch` | `soma` pós-`switch` | `x` pós-`x++` | `x <= 4`? |
|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| **1** | `1` | `1` | `case 1`: `soma += 1`; `break` | `1` | `2` | Sim |
| **2** | `2` | `2` | `case 2`: `soma += 4` (sem `break`, *fall-through*!) $\rightarrow$ `default`: `soma += 1`; `break` | `6` | `3` | Sim |
| **3** | `3` | `0` | `default`: `soma += 1`; `break` | `7` | `4` | Sim |
| **4** | `4` | `1` | `case 1`: `soma += 4`; `break` | `11` | `5` | **Não** (encerra) |

**Saída Exata:**
```text
x = 5, soma = 11
```

---

### `C10-C02` *(Programa Completo — Contagem e Soma de Primos em Intervalo $[a, b]$)*
Solução completa: [C10_C02.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C10_C02.c)
```c
#include <stdio.h>

int main(void) {
    long long a, b;
    if (scanf("%lld %lld", &a, &b) != 2) {
        return 1;
    }

    if (b < a) {
        printf("Intervalo Invalido\n");
        return 0;
    }

    int qtd_primos = 0;
    long long soma_primos = 0;

    for (long long n = a; n <= b; n++) {
        int primo = 1;
        if (n <= 1) {
            primo = 0;
        } else if (n == 2) {
            primo = 1;
        } else if (n % 2 == 0) {
            primo = 0;
        } else {
            for (long long d = 3; d * d <= n; d += 2) {
                if (n % d == 0) {
                    primo = 0;
                    break;
                }
            }
        }

        if (primo) {
            qtd_primos++;
            soma_primos += n;
        }
    }

    printf("Qtd Primos: %d\n", qtd_primos);
    printf("Soma Primos: %lld\n", soma_primos);
    return 0;
}
```

---

### `C10-C03` *(Programa Completo — Tabela Triangular de Multiplicação com Laços Aninhados)*
Solução completa: [C10_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C10_C03.c)
```c
#include <stdio.h>

int main(void) {
    int n;
    if (scanf("%d", &n) != 1) {
        return 1;
    }

    if (n <= 0) {
        printf("Entrada Invalida\n");
        return 0;
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%4d", i * j);
        }
        printf("\n");
    }

    return 0;
}
```
