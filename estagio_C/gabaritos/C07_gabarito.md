# Gabarito Comentado — Bloco `C07` (Controle de Fluxo em Laços e Primalidade)

> **Bloco de referência:** [C07_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/blocos/C07_bloco.md)  
> **Nota para Caça ao Bug:** Os códigos em `C07-E02` e `C07-C02` contêm armadilhas conceituais reais (`continue` pulando decremento em `while` e `break` em `switch` sem afetar o laço externo). As versões corrigidas compiláveis encontram-se em `testes/solucoes/`.

---

## 1. Gabarito dos Exercícios (`C07-E01` a `C07-E05`)

### `C07-E01` *(Rastreamento de `break` e `continue` em `for`)*
Código:
```c
int soma = 0;
for (int i = 1; i <= 10; i++) {
    if (i % 3 == 0) {
        continue;
    }
    if (i > 7) {
        break;
    }
    printf("%d ", i);
    soma += i;
}
printf("\nSoma = %d\n", soma);
```

**Tabela de Rastreamento Passo a Passo:**

| `i` | `i % 3 == 0`? | `i > 7`? | Ação Tomada | Impressão | `soma` acumulada |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | Não | Não | Executa corpo | `1 ` | `0 + 1 = 1` |
| **2** | Não | Não | Executa corpo | `2 ` | `1 + 2 = 3` |
| **3** | **Sim** | — | `continue` acionado | — | `3` (inalterado) |
| **4** | Não | Não | Executa corpo | `4 ` | `3 + 4 = 7` |
| **5** | Não | Não | Executa corpo | `5 ` | `7 + 5 = 12` |
| **6** | **Sim** | — | `continue` acionado | — | `12` (inalterado) |
| **7** | Não | Não | Executa corpo | `7 ` | `12 + 7 = 19` |
| **8** | Não | **Sim** | `break` acionado | — | `19` (laço abortado) |

**Saída Impressa Exata:**
```text
1 2 4 5 7 
Soma = 19
```
*Observação didática:* As iterações para `i = 9` e `i = 10` jamais foram executadas devido ao `break` em `i = 8`.

---

### `C07-E02` *(Caça ao Bug — Armadilha do `continue` em `while`)*
1. **Explicação:** No laço `while`, o comando `continue` salta imediatamente para o teste da condição (`i >= 1`), ignorando todas as instruções subsequentes do corpo do laço. Como a linha de decremento `i--;` estava localizada no final do corpo, quando `i` atinge o valor `3`, o `continue` é acionado e a linha `i--;` é pulada. Na volta seguinte, `i` continua valendo `3`, acionando novamente o `continue`. Esse ciclo se repete infinitamente com `i` congelado em `3`, impedindo a terminação do programa.
2. **Solução completa corrigida:** [C07_E02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C07_E02_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int n;
    if (scanf("%d", &n) != 1) {
        return 1;
    }

    int i = n;
    while (i >= 1) {
        if (i == 3) {
            i--; // Garante o decremento antes de saltar a iteracao!
            continue;
        }
        printf("%d ", i);
        i--;
    }
    printf("\n");
    return 0;
}
```

---

### `C07-E03` *(Completar Laço `while (1)` com `break` Condicional)*
Solução completa: [C07_E03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C07_E03.c)
```c
#include <stdio.h>

int main(void) {
    int nota;
    int qtd = 0;
    double soma = 0.0;

    while (1) {
        if (scanf("%d", &nota) != 1) {
            break;
        }
        if (nota < 0) {
            break; // Sentinela de parada encontrado
        }
        soma += nota;
        qtd++;
    }

    if (qtd == 0) {
        printf("Nenhuma nota valida\n");
    } else {
        printf("Qtd: %d\n", qtd);
        printf("Media: %.2f\n", soma / qtd);
    }

    return 0;
}
```

---

### `C07-E04` *(Detector de Número Primo com Tratamento Rigoroso de Bordas)*
Solução completa: [C07_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C07_E04.c)
```c
#include <stdio.h>

int main(void) {
    long long n;
    if (scanf("%lld", &n) != 1) {
        return 1;
    }

    int primo = 1;

    if (n <= 1) {
        primo = 0; // 0, 1 e negativos nao sao primos
    } else if (n == 2) {
        primo = 1; // 2 e primo
    } else if (n % 2 == 0) {
        primo = 0; // pares > 2 sao compostos
    } else {
        for (long long d = 3; d * d <= n; d += 2) {
            if (n % d == 0) {
                primo = 0;
                break; // Achou divisor, encerra antecipadamente
            }
        }
    }

    if (primo) {
        printf("Primo\n");
    } else {
        printf("Nao Primo\n");
    }

    return 0;
}
```

---

### `C07-E05` *(Programa Completo — Contagem de Primos em Sequência com Sentinela)*
Solução completa: [C07_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C07_E05.c)
```c
#include <stdio.h>

int main(void) {
    long long num;
    int total_primos = 0;

    while (1) {
        if (scanf("%lld", &num) != 1 || num == 0) {
            break;
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
            total_primos++;
        }
    }

    printf("Total Primos: %d\n", total_primos);
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`C07-C01` a `C07-C03`)

### `C07-C01` *(Teste de Mesa — `continue` vs `break` em Laços)*
1. **Trecho A (`continue` quando `i == 3`):**
   - O laço itera para `i = 1, 2, 3, 4, 5`.
   - Quando `i = 3`, o `continue` salta a adição `a += i`.
   - Valores somados em `a`: $1 + 2 + 4 + 5 = 12$.
   - Saída: `A = 12\n`.
2. **Trecho B (`break` quando `i == 3`):**
   - O laço itera para `i = 1, 2`.
   - Quando `i = 3`, o `break` aborta imediatamente todo o laço. As iterações 3, 4 e 5 nunca ocorrem.
   - Valores somados em `b`: $1 + 2 = 3$.
   - Saída: `B = 3\n`.

---

### `C07-C02` *(Caça ao Bug — `break` em Laço Contendo `switch`)*
1. **Explicação:** Pelo padrão da linguagem C, o comando `break` dentro de uma ramificação `case` associa-se exclusivamente à estrutura `switch`, servindo para evitar o transbordamento (*fall-through*) para o próximo `case`. Ele **não possui** o poder de interromper laços (`while` ou `for`) mais externos. Por isso, ao digitar 0, o `break` apenas finalizou o `switch`, e a próxima volta do `while (1)` continuou ativa.
2. **Solução completa corrigida:** [C07_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C07_C02_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int opcao;
    int rodando = 1; // Variavel de sinalizacao (flag)

    while (rodando) {
        if (scanf("%d", &opcao) != 1) {
            break;
        }
        switch (opcao) {
            case 1:
                printf("Opcao 1 Executada\n");
                break;
            case 0:
                printf("Saindo\n");
                rodando = 0; // Sinaliza saida do laco
                break;
            default:
                printf("Opcao Invalida\n");
                break;
        }
    }

    printf("Fim do Programa\n");
    return 0;
}
```

---

### `C07-C03` *(Programa Completo — Classificador e Estatísticas de Primalidade)*
Solução completa: [C07_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C07_C03.c)
```c
#include <stdio.h>

int main(void) {
    int k;
    if (scanf("%d", &k) != 1 || k <= 0) {
        return 1;
    }

    int total_primos = 0;

    for (int i = 0; i < k; i++) {
        long long num;
        if (scanf("%lld", &num) != 1) {
            return 1;
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
            printf("Numero %lld: Primo\n", num);
            total_primos++;
        } else {
            printf("Numero %lld: Nao Primo\n", num);
        }
    }

    printf("Resumo: %d primos de %d numeros\n", total_primos, k);
    return 0;
}
```
