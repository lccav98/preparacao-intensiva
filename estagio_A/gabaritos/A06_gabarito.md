# Gabarito Comentado — Bloco `A06` (Entrada de Dados com `scanf` e Operador `&`)

> **Bloco de referência:** [A06_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/blocos/A06_bloco.md)  
> **Nota para Caça ao Bug:** Os códigos em `A06-E03` e `A06-C01` no bloco do aluno contêm **erros intencionais** detalhados abaixo. Apenas as versões corrigidas devem ser compiladas.

---

## 1. Gabarito dos Exercícios (`A06-E01` a `A06-E05`)

### `A06-E01` *(Leitura e Diagnóstico de Código)*
1. **`scanf("%d", alunos);`** — Falta o operador de endereço `&`. Correção: `scanf("%d", &alunos);`.
2. **`scanf("%f", &nota_corte);`** — Especificador `%f` incompatível com `double` no `scanf` (causa leitura incorreta na memória e warning em `-Wall`). Correção: `scanf("%lf", &nota_corte);`.
3. **`scanf("%c", &turma);`** — Falta espaço antes de `%c`; após ler o número anterior, `%c` capturaria `'\n'` ou `' '` residual do teclado. Correção: `scanf(" %c", &turma);`.

### `A06-E02` *(Completar solução)*
- **`/* A */`:** `%d %d`
- **`/* B */`:** `&codigo, &lote`
- **`/* C */`:** `%lf %c` *(com espaço antes de `%c` para descartar whitespace entre `peso` e `categoria`)*

### `A06-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `scanf("%d", item);` omite o operador `&` antes de `item`.
  2. `scanf("%f", &preco);` usa `%f` em vez de `%lf` para variável `double`.
  3. `scanf("%c", &setor);` omite o espaço inicial `" %c"`, podendo ler `'\n'` deixado pela entrada de `preco`.
- **Solução corrigida completa:** [A06_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A06_E03_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int item;
    double preco;
    char setor;

    scanf("%d", &item);
    scanf("%lf", &preco);
    scanf(" %c", &setor);

    printf("Item: %d\n", item);
    printf("Preco: R$ %.2f\n", preco);
    printf("Setor: %c\n", setor);
    return 0;
}
```

### `A06-E04` *(Programa completo — Leitura dupla de inteiros e reais)*
Arquivo: [A06_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A06_E04.c)
```c
#include <stdio.h>

int main(void) {
    int id_a, id_b;
    double min_val, max_val;

    scanf("%d %d", &id_a, &id_b);
    scanf("%lf %lf", &min_val, &max_val);

    printf("IDs: %d e %d\n", id_a, id_b);
    printf("Limites: %.2f a %.2f\n", min_val, max_val);
    return 0;
}
```

### `A06-E05` *(Programa completo — Leitura de `int`, `double` e `char`)*
Arquivo: [A06_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A06_E05.c)
```c
#include <stdio.h>

int main(void) {
    int codigo;
    double temperatura;
    char escala;

    scanf("%d %lf %c", &codigo, &temperatura, &escala);

    printf("Sensor %d: %.1f %c\n", codigo, temperatura, escala);
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`A06-C01` a `A06-C03`)

### `A06-C01` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `scanf("%d", sala);` não fornece o endereço `&sala`.
  2. `scanf("%f", &area);` usa `%f` em vez de `%lf` para `double area;`.
- **Solução corrigida completa:** [A06_C01_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A06_C01_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    int sala;
    double area;

    scanf("%d", &sala);
    scanf("%lf", &area);

    printf("Sala: %d\n", sala);
    printf("Area: %.2f m2\n", area);
    return 0;
}
```

### `A06-C02` *(Completar leitura múltipla no papel)*
1. `scanf("%d %d %d", &dia, &mes, &ano);`
2. `scanf("%lf %c", &indice, &classe);`

### `A06-C03` *(Programa completo — Entrada e eco formatado)*
Arquivo: [A06_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A06_C03.c)
```c
#include <stdio.h>

int main(void) {
    int id;
    double valor;
    char situacao;

    scanf("%d %lf %c", &id, &valor, &situacao);

    printf("ID: %d\n", id);
    printf("Valor: R$ %.2f\n", valor);
    printf("Situacao: %c\n", situacao);
    return 0;
}
```
