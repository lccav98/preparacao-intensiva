# Gabarito Comentado — Bloco `B05` (`else if` e Ordem das Condições)

> **Bloco de referência:** [B05_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/blocos/B05_bloco.md)  
> **Nota para Caça ao Bug:** Os códigos em `B05-E03` e `B05-C02` no bloco do aluno contêm **erros intencionais** claramente identificados abaixo. Apenas as versões corrigidas devem ser compiladas.

---

## 1. Gabarito dos Exercícios (`B05-E01` a `B05-E06`)

### `B05-E01` *(Teste de Mesa)*
- **`pontos = 95`:** Avalia **1** condição (`95 >= 50` é verdadeira). Saída impressa: **`Nivel Prata`**. *(Erro lógico do trecho: não atinge `"Nivel Ouro"` porque `>= 50` já captura `>= 90`.)*
- **`pontos = 70`:** Avalia **1** condição (`70 >= 50` é verdadeira). Saída impressa: **`Nivel Prata`**.
- **`pontos = 30`:** Avalia **2** condições (`30 >= 50` falsa; `30 >= 90` falsa) e cai no `else`. Saída impressa: **`Nivel Bronze`**.
- **Análise e correção:** Nenhum inteiro atinge `"Nivel Ouro"` (ramo morto), pois todo valor `>= 90` também é `>= 50`. Correção: inverter a ordem dos dois primeiros testes (`if (pontos >= 90)` primeiro, depois `else if (pontos >= 50)`).

### `B05-E02` *(Completar solução)*
- **`/* A */`:** `temp < 10.0`
- **`/* B */`:** `temp < 25.0` *(como o primeiro teste falhou, já está garantido que `temp >= 10.0`)*

### `B05-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. **Ordem/condição ampla bloqueadora:** `else if (compra >= 100.0)` captura todos os valores `>= 100.0`, tornando `compra <= 299.99` e o `else` inatingíveis (`compra = 350.00` receberia apenas `5%` em vez de `15%`).
  2. **Lacuna em fronteira contínua:** Mesmo se estivesse na ordem certa, `compra <= 299.99` deixaria o intervalo `(299.99, 300.0)` (ex.: `299.995`) cair no `else` de `15%` quando a regra diz "menos de 300.00" (`10%`).
- **Solução corrigida completa:** [B05_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B05_E03_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    double compra, desconto, total;
    scanf("%lf", &compra);

    if (compra < 100.0) {
        desconto = 0.0;
    } else if (compra < 200.0) {
        desconto = compra * 0.05;
    } else if (compra < 300.0) {
        desconto = compra * 0.10;
    } else {
        desconto = compra * 0.15;
    }

    total = compra - desconto;
    printf("Desconto: R$ %.2f\n", desconto);
    printf("Total: R$ %.2f\n", total);
    return 0;
}
```

### `B05-E04` *(Programa completo — Energia em kWh)*
Arquivo: [B05_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B05_E04.c)
```c
#include <stdio.h>

int main(void) {
    double kwh, total;
    scanf("%lf", &kwh);

    if (kwh <= 100.0) {
        total = kwh * 0.50;
    } else if (kwh <= 250.0) {
        total = kwh * 0.65;
    } else {
        total = kwh * 0.80;
    }

    printf("Total: R$ %.2f\n", total);
    return 0;
}
```

### `B05-E05` *(Programa completo — Taxa de bagagem)*
Arquivo: [B05_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B05_E05.c)
```c
#include <stdio.h>

int main(void) {
    double peso, taxa;
    scanf("%lf", &peso);

    if (peso <= 10.0) {
        taxa = 0.00;
    } else if (peso <= 20.0) {
        taxa = 40.00;
    } else if (peso <= 30.0) {
        taxa = 75.00;
    } else {
        taxa = 75.00 + (peso - 30.0) * 8.50;
    }

    printf("Taxa: R$ %.2f\n", taxa);
    return 0;
}
```

### `B05-E06` *(Programa completo — Taxa de entrega por distância)*
Arquivo: [B05_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B05_E06.c)
```c
#include <stdio.h>

int main(void) {
    double dist, taxa;
    scanf("%lf", &dist);

    if (dist <= 5.0) {
        taxa = 10.00;
    } else if (dist <= 15.0) {
        taxa = 18.00;
    } else if (dist <= 30.0) {
        taxa = 28.00;
    } else {
        taxa = 28.00 + (dist - 30.0) * 2.25;
    }

    printf("Taxa: R$ %.2f\n", taxa);
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`B05-C01` a `B05-C03`)

### `B05-C01` *(Teste de Mesa)*
| Entrada (`nota`) | Condições avaliadas | Quantidade de avaliações | Saída impressa |
|---|---|---:|---|
| `2.9` | `2.9 < 3.0` (V) | **1** | `Insuficiente` |
| `3.0` | `3.0 < 3.0` (F), `3.0 < 6.0` (V) | **2** | `Recuperacao` |
| `6.0` | `6.0 < 3.0` (F), `6.0 < 6.0` (F), `6.0 < 9.0` (V) | **3** | `Bom` |
| `9.0` | `9.0 < 3.0` (F), `9.0 < 6.0` (F), `9.0 < 9.0` (F) → `else` | **3** | `Excelente` |

### `B05-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. Os dois blocos `if (mbps <= 100.0)` e `if (mbps <= 20.0)` são **independentes** (falta `else if` ligando-os), além de estarem em **ordem invertida** (`<= 100.0` antes de `<= 20.0`). Para `mbps = 50.0`, o 1º `if` define `109.90`, mas em seguida o 2º `if` falha e entra no `else if (mbps <= 300.0)`, sobrescrevendo `preco` para `149.90`!
- **Solução corrigida completa:** [B05_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B05_C02_corrigido.c)
```c
#include <stdio.h>

int main(void) {
    double mbps, preco;
    scanf("%lf", &mbps);

    if (mbps <= 20.0) {
        preco = 79.90;
    } else if (mbps <= 100.0) {
        preco = 109.90;
    } else if (mbps <= 300.0) {
        preco = 149.90;
    } else {
        preco = 199.90;
    }

    printf("Plano: R$ %.2f\n", preco);
    return 0;
}
```

### `B05-C03` *(Programa completo — Estacionamento)*
Arquivo: [B05_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/solucoes/B05_C03.c)
```c
#include <stdio.h>

int main(void) {
    double horas, total;
    scanf("%lf", &horas);

    if (horas <= 1.0) {
        total = 8.00;
    } else if (horas <= 3.0) {
        total = 15.00;
    } else if (horas <= 6.0) {
        total = 24.00;
    } else {
        total = 24.00 + (horas - 6.0) * 4.50;
    }

    printf("Total: R$ %.2f\n", total);
    return 0;
}
```
