# Gabarito Comentado — Bloco `F03` (Passagem por Valor em C e Limites da Cópia Local)

> **Bloco de referência:** [F03_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/blocos/F03_bloco.md)  
> **Nota para Caça ao Bug:** `F03-E03` no bloco do aluno contém **erro intencional** detalhado abaixo.

---

## 1. Gabarito dos Exercícios (`F03-E01` a `F03-E05`)

### `F03-E01` *(Teste de Mesa de Memória)*
- **(a)** Quadros de memória:
  - Durante `ajusta(x, y)`:
    - Quadro `main`: `x = 4`, `y = 7` *(inalterados)*
    - Quadro `ajusta`: recebe cópias `a = 4`, `b = 7` → `a` passa a `14`, `b` passa a `14`.
  - Após retorno de `ajusta`: o quadro `ajusta` é destruído; em `main`, `x` continua `4` e `y` continua `7`.
- **(b)** Saída exata:
  ```text
  Antes: 4 7
  Dentro: 14 14
  Depois: 4 7
  ```

### `F03-E02` *(Análise Conceitual e Lacunas)*
- **(a)** Em C, a passagem de parâmetros escalares é feita **por valor**: `x` e `y` recebem apenas **cópias** dos valores de `u` e `v` em um quadro separado na memória. A troca altera somente essas cópias locais, que são destruídas no fim de `trocar`, deixando `u` e `v` em `main` intocados.
- **(b)** Lacunas:
  - **`/* A */`:** `double`
  - **`/* B */`:** `return novo;`
  - **`/* C */`:** `p = aplicar_desconto(p, 10.0);` *(ou passando outro percentual válido `pct` com atribuição em `p`)*

### `F03-E03` *(Caça ao Bug — Erro intencional no enunciado)*
- **Erro intencional:** `reajustar` tinha tipo `void` e alterava apenas a cópia local `sal` (passagem por valor), sem devolver o novo valor para `salario` em `main`.
- **Correção:** Alterar o tipo de retorno para `double`, retornar o salário reajustado com `return` e atribuir o retorno em `main` (`salario = reajustar(salario, percentual);`).
- **Solução corrigida completa:** [F03_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F03_E03_corrigido.c)
```c
#include <stdio.h>

double reajustar(double sal, double pct);

int main(void) {
    double salario, percentual;
    scanf("%lf %lf", &salario, &percentual);
    // Erro original: reajustar era void e alterava apenas a copia local 'sal'.
    // Correcao: retornar o novo valor e atribuir a 'salario' em main.
    salario = reajustar(salario, percentual);
    printf("Novo salario: %.2f\n", salario);
    return 0;
}

double reajustar(double sal, double pct) {
    return sal * (1.0 + pct / 100.0);
}
```

### `F03-E04` *(Programa completo — Saque com retorno e original preservado)*
Arquivo: [F03_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F03_E04.c)
```c
#include <stdio.h>

int processar_saque(int saldo, int valor);

int main(void) {
    int saldo, saque, novo_saldo;
    scanf("%d %d", &saldo, &saque);
    novo_saldo = processar_saque(saldo, saque);
    printf("Original: %d\nAtualizado: %d\n", saldo, novo_saldo);
    return 0;
}

int processar_saque(int saldo, int valor) {
    if (valor > 0 && valor <= saldo) {
        saldo -= valor;
    }
    return saldo;
}
```

### `F03-E05` *(Programa completo — Conversão Celsius → Kelvin limitada)*
Arquivo: [F03_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F03_E05.c)
```c
#include <stdio.h>

double converter_celsius_para_kelvin(double c);
double limitar_intervalo(double val, double min, double max);

int main(void) {
    double t, kelvin;
    scanf("%lf", &t);
    kelvin = converter_celsius_para_kelvin(t);
    kelvin = limitar_intervalo(kelvin, 0.0, 1000.0);
    printf("Kelvin limitado: %.2f\n", kelvin);
    return 0;
}

double converter_celsius_para_kelvin(double c) {
    return c + 273.15;
}

double limitar_intervalo(double val, double min, double max) {
    if (val < min) {
        return min;
    }
    if (val > max) {
        return max;
    }
    return val;
}
```

---

## 2. Gabarito da Checagem Independente (`F03-C01` a `F03-C03`)

### `F03-C01` *(Teste de Mesa)*
Saída exata:
```text
func: a=18 b=7
main: x=6 y=2 z=25
```
*(Rastreamento: `a` recebe cópia `6` → `18`; `b` recebe cópia `2` → `7`; retorna `18 + 7 = 25` para `z`. As variáveis `x` e `y` de `main` permanecem `6` e `2`.)*

### `F03-C02` *(Análise Conceitual)*
- **(a)** Saída impressa: **`15 4`**.
- **(b)** Na chamada `ordenar_par(x, y)`, os valores `15` e `4` são copiados **por valor** para os parâmetros `a` e `b` em um quadro de memória separado. A troca `a = b; b = aux;` ocorre apenas nas cópias locais `a` e `b`, que são destruídas ao encerrar `ordenar_par`, deixando `x = 15` e `y = 4` intactos em `main`. Além disso, um comando `return` devolve **no máximo um valor** ao chamador, o que não permite atualizar simultaneamente duas variáveis distintas (`x` e `y`) de `main` sem passar seus endereços (assunto de `F04`–`F05`).

### `F03-C03` *(Programa completo — Conversão de `void` falho para `return` útil)*
Arquivo: [F03_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/testes/solucoes/F03_C03.c)
```c
#include <stdio.h>

int aplicar_multa(int pontos, int infracao);

int main(void) {
    int pontos, infracao;
    scanf("%d %d", &pontos, &infracao);
    pontos = aplicar_multa(pontos, infracao);
    printf("Total de pontos: %d\n", pontos);
    return 0;
}

int aplicar_multa(int pontos, int infracao) {
    if (infracao > 0) {
        return pontos + infracao;
    }
    return pontos;
}
```
