# Gabarito Comentado — Bloco `A05` (Saída de Variáveis, Casas Decimais e Constantes)

> **Bloco de referência:** [A05_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/blocos/A05_bloco.md)  
> **Nota para Caça ao Bug:** Os códigos de `A05-E03` e `A05-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo. Apenas as versões corrigidas salvas em `solucoes/` devem ser compiladas.

---

## 1. Gabarito dos Exercícios (`A05-E01` a `A05-E05`)

### `A05-E01` *(Previsão de saída no papel)*
```text
Cod=7 Nivel=S
V1=12.3 V2=12.35
Sci=1.500000e+02
```
- **Justificativa:** `%d` e `%c` imprimem `7` e `'S'`; `%.1f` arredonda `12.346` para `12.3` e `%.2f` arredonda para `12.35`; `%e` no padrão Linux/glibc exibe `150.0` em notação científica com 6 casas na mantissa (`1.500000e+02`).

### `A05-E02` *(Completar especificadores e constantes)*
- **`/* A */`:** `#define MAX_ITENS 50`
- **`/* B */`:** `const double TAXA_BASE = 4.5;`
- **`/* C */`:** `%d` *(ou `%i`)*
- **`/* D */`:** `%.2f`

### `A05-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `#define LIMITE 100;` inclui ponto-e-vírgula `;` indevido no final da macro (o pré-processador substitui `LIMITE` por `100;` dentro dos parênteses de `printf`, causando erro de sintaxe).
  2. `Limite: %f` usa o especificador de ponto flutuante `%f` para `LIMITE` (que é o inteiro `100`), incompatível com o tipo esperado pelo `printf` (`-Wformat` / saída incorreta). O correto é `%d`.
  3. `Classe: %d` usa `%d` para um `char` (`'A'`), imprimindo o código numérico ASCII `65` em vez do caractere; o correto é `%c`.
- **Solução corrigida completa:** [A05_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A05_E03_corrigido.c)
```c
/* Exercicio A05-E03: Correcao de #define e especificadores */
#include <stdio.h>
#define LIMITE 100

int main(void) {
    double peso = 72.453;
    char classe = 'A';

    printf("Limite: %d | Peso: %.2f kg | Classe: %c\n", LIMITE, peso, classe);
    return 0;
}
```

### `A05-E04` *(Programa completo — Parâmetros constantes sem expressões)*
Arquivo: [A05_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A05_E04.c)
```c
/* Exercicio A05-E04: Exibicao de constantes #define e const sem expressoes */
#include <stdio.h>
#define PI 3.14159

int main(void) {
    const int ESCALA = 2;
    double raio = 4.5;
    char unidade = 'm';

    printf("PI aproximado: %.4f\n", PI);
    printf("Escala: %i\n", ESCALA);
    printf("Raio: %.2f %c\n", raio, unidade);
    return 0;
}
```

### `A05-E05` *(Programa completo — Ficha de dados formatada)*
Arquivo: [A05_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A05_E05.c)
```c
/* Exercicio A05-E05: Ficha formatada de produto */
#include <stdio.h>

int main(void) {
    const int ANO_BASE = 2026;
    int codigo = 308;
    double valorUnitario = 49.876;
    double peso = 7.2;
    char setor = 'E';

    printf("Ficha %d - Setor %c\n", ANO_BASE, setor);
    printf("Codigo: %d\n", codigo);
    printf("Valor: R$ %.2f\n", valorUnitario);
    printf("Peso: %.1f kg\n", peso);
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`A05-C01` a `A05-C03`)

### `A05-C01` *(Previsão de `%.2f` e `%c` no papel)*
```text
Fator 10 | Grau B | Nota 8.75
```
*(Com quebra de linha `\n` ao final; `8.749` arredonda para `8.75` com `%.2f`.)*

### `A05-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `#define MAX 40;` possui ponto-e-vírgula `;` no final da macro, quebrando a chamada `printf(..., MAX, TAXA);`.
  2. `TAXA = 12.50;` tenta reatribuir um valor a uma variável declarada com `const double TAXA`, o que o compilador proíbe com erro de atribuição a variável somente-leitura.
- **Solução corrigida completa:** [A05_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A05_C02_corrigido.c)
```c
/* Checagem A05-C02: Correcao de #define e const */
#include <stdio.h>
#define MAX 40

int main(void) {
    const double TAXA = 12.50;

    printf("Max: %d | Taxa: %.2f\n", MAX, TAXA);
    return 0;
}
```

### `A05-C03` *(Programa completo independente)*
Arquivo: [A05_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A05_C03.c)
```c
/* Checagem A05-C03: Programa completo com constante e especificadores */
#include <stdio.h>
#define VERSAO 3

int main(void) {
    const double TARIFA = 6.258;
    int sala = 102;
    char bloco = 'C';

    printf("Sistema v%d\n", VERSAO);
    printf("Sala %d - Bloco %c\n", sala, bloco);
    printf("Tarifa: R$ %.2f\n", TARIFA);
    return 0;
}
```
