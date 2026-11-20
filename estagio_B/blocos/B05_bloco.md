# Bloco `B05` — Múltiplas Alternativas com `else if` e Ordem das Condições

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio B — Expressões, Operadores e Estruturas Condicionais / **`B05`** |
| **Micro-habilidade foco** | Construir cadeias `if / else if / else` ordenando condições sobrepostas da mais restritiva para a mais geral, sem lacunas em fronteiras contínuas. |
| **Pré-requisitos** | `B04` *(Desvio condicional composto `if / else` vs. `if`s independentes)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 20 min):** `12 min` resol. \| `5 min` corr. \| `3 min` recup.; **Sessão 2 (`E04`–`E06`, 22 min):** `14 min` resol. \| `5 min` corr. \| `3 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Não utilize** operadores lógicos (`&&`, `\|\|`, `!`), `switch`, laços ou vetores neste bloco. Resolva apenas ordenando comparações relacionais simples (`<`, `<=`, `>`, `>=`) em `if / else if / else`. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. Quando há **3 ou mais alternativas mutuamente exclusivas** para a mesma variável, encadeie `if (...) { ... } else if (...) { ... } else { ... }`.
2. A avaliação é **de cima para baixo (*top-down*)**: **apenas o primeiro bloco cuja condição for verdadeira é executado**; todas as condições abaixo são ignoradas.
3. **Ordem crítica:** Quando as condições se sobrepõem, teste **do extremo mais restritivo para o mais amplo** (ou em ordem estritamente crescente com `<` / `<=`, ou estritamente decrescente com `>` / `>=`).
4. **Sem lacunas em valores reais (`double`):** Evite escrever `<= 99.99` antes de `>= 100.00` (o valor `99.995` ficaria sem cobertura ou cairia no `else` errado). Prefira `< 100.0` seguido de `< 200.0`.
5. Use **`double`** (com `%lf` no `scanf`) para evitar erros de arredondamento de `float` exatamente sobre os limites das faixas.

---

## 2. Exemplos Guiados

### Exemplo 1 — Por que a ordem altera o resultado *(Trecho ilustrativo)*
Considere classificar uma `double nota` (`>= 8.0` Excelente; `>= 6.0` e `< 8.0` Aprovado; `< 6.0` Reprovado):

```c
/* FORMA ERRADA: >= 6.0 captura notas >= 8.0 */
if (nota >= 6.0) {
    printf("Aprovado\n");
} else if (nota >= 8.0) {
    printf("Excelente\n");   /* INATINGIVEL! */
} else {
    printf("Reprovado\n");
}
```
Se `nota = 9.2`, o primeiro teste (`9.2 >= 6.0`) já é verdadeiro e imprime `Aprovado`, ignorando `else if (nota >= 8.0)`.  
**Correção:** Testar o limite mais restritivo primeiro (`if (nota >= 8.0)` → `else if (nota >= 6.0)` → `else`).

### Exemplo 2 — Faixas contínuas crescentes sem usar `&&` *(Programa completo)*
Regra de taxa de serviço sobre `double valor`: até `50.00` → `R$ 5.00`; acima de `50.00` até `150.00` → `R$ 9.00`; acima de `150.00` → `R$ 14.00`.

```c
#include <stdio.h>

int main(void) {
    double valor, taxa;
    scanf("%lf", &valor);

    if (valor <= 50.0) {
        taxa = 5.00;
    } else if (valor <= 150.0) {   /* So chega aqui se valor > 50.0! */
        taxa = 9.00;
    } else {                       /* So chega aqui se valor > 150.0! */
        taxa = 14.00;
    }

    printf("Taxa: R$ %.2f\n", taxa);
    return 0;
}
```
**Por que funciona sem `&&`?** O segundo teste (`valor <= 150.0`) só é avaliado quando `valor <= 50.0` foi **falso**, portanto já está garantido que `valor > 50.0`.

---

## 3. Exercícios (`B05-E01` a `B05-E06`)

### Sessão 1 (`B05-E01` a `B05-E03` — Leitura, Lacunas e Depuração)

### `B05-E01` *(Leitura e Teste de Mesa — Reprodução do modelo)*
Sem utilizar computador, acompanhe o trecho ilustrativo abaixo (com `int pontos;`) para as entradas `pontos = 95`, `pontos = 70` e `pontos = 30`. Informe para cada caso **quantas condições são avaliadas** e **o texto impresso**:

```c
if (pontos >= 50) {
    printf("Nivel Prata\n");
} else if (pontos >= 90) {
    printf("Nivel Ouro\n");
} else {
    printf("Nivel Bronze\n");
}
```
*(Responda também: qual valor de `pontos` nunca conseguirá atingir `"Nivel Ouro"` e como corrigir o trecho?)*

---

### `B05-E02` *(Completar solução)*
O trecho ilustrativo abaixo recebe `double temp;` (em °C) e deve classificar conforme a tabela:
- abaixo de `10.0`: `Frio`
- de `10.0` até menos de `25.0`: `Agradavel`
- `25.0` ou mais: `Quente`

Complete as lacunas `/* A */` e `/* B */` usando **apenas um operador relacional por condição** e sem deixar lacunas entre `9.9` e `10.0`:

```c
if ( /* A */ ) {
    printf("Frio\n");
} else if ( /* B */ ) {
    printf("Agradavel\n");
} else {
    printf("Quente\n");
}
```

---

### `B05-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler o valor de uma compra (`double compra`) e calcular o desconto de uma livraria:
- abaixo de `100.00`: `0%`
- de `100.00` até menos de `200.00`: `5%`
- de `200.00` até menos de `300.00`: `10%`
- `300.00` ou mais: `15%`

Identifique os **2 bugs intencionais** presentes no código (anotando no papel ou em comentários `//`) e escreva a **versão corrigida completa** usando `if / else if / else` sem `&&`:

```c
#include <stdio.h>

int main(void) {
    double compra, desconto, total;
    scanf("%lf", &compra);

    if (compra < 100.0) {
        desconto = 0.0;
    } else if (compra >= 100.0) {
        desconto = compra * 0.05;
    } else if (compra <= 299.99) {
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

---

### Sessão 2 (`B05-E04` a `B05-E06` — Escrita Guiada → Independente)

### `B05-E04` *(Variação controlada com pistas)*
Escreva um **programa completo** em C que leia o consumo mensal de energia elétrica em kWh (`double kwh`, com `kwh >= 0`) e calcule o valor da conta segundo a faixa inteira de consumo:
- até `100.0` kWh: `R$ 0.50` por kWh;
- acima de `100.0` até `250.0` kWh: `R$ 0.65` por kWh (sobre todo o consumo);
- acima de `250.0` kWh: `R$ 0.80` por kWh (sobre todo o consumo).

Imprima exatamente `Total: R$ X.XX\n` (2 casas decimais).  
*Pistas:* Use `<= 100.0`, depois `<= 250.0`, e `else` para o último caso. Teste especialmente os limites exatos `100.0` e `250.0`.

---

### `B05-E05` *(Variação controlada com pistas)*
Escreva um **programa completo** em C que leia o peso de uma bagagem em kg (`double peso`, com `peso >= 0`) e calcule a taxa de despacho:
- até `10.0` kg: `R$ 0.00`;
- acima de `10.0` até `20.0` kg: `R$ 40.00` fixo;
- acima de `20.0` até `30.0` kg: `R$ 75.00` fixo;
- acima de `30.0` kg: `R$ 75.00` mais `R$ 8.50` por quilograma excedente acima de `30.0` kg.

Imprima exatamente `Taxa: R$ X.XX\n`.  
*Pista:* No último ramo (`else`), calcule o excedente subtraindo `30.0` do `peso` antes de multiplicar por `8.50`.

---

### `B05-E06` *(Resolução independente)*
Escreva um **programa completo** em C que leia a distância de entrega em quilômetros (`double dist`, com `dist >= 0`) e informe a taxa de entrega conforme as regras:
- até `5.0` km: `R$ 10.00`;
- acima de `5.0` até `15.0` km: `R$ 18.00`;
- acima de `15.0` até `30.0` km: `R$ 28.00`;
- acima de `30.0` km: `R$ 28.00` mais `R$ 2.25` por km excedente acima de `30.0` km.

Imprima exatamente `Taxa: R$ X.XX\n`.

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `B05-C01` *(Teste de Mesa)*
Considere `double nota;` e o código abaixo:
```c
if (nota < 3.0) {
    printf("Insuficiente\n");
} else if (nota < 6.0) {
    printf("Recuperacao\n");
} else if (nota < 9.0) {
    printf("Bom\n");
} else {
    printf("Excelente\n");
}
```
Para as 4 entradas `2.9`, `3.0`, `6.0` e `9.0`, indique **o texto impresso** e **quantas condições do `if`/`else if` foram avaliadas** em cada caso.

### `B05-C02` *(Caça ao Bug — Programa completo)*
Um plano de internet cobra segundo a velocidade contratada em Mbps (`double mbps`, `mbps > 0`):
- até `20.0` Mbps: `R$ 79.90`
- acima de `20.0` até `100.0` Mbps: `R$ 109.90`
- acima de `100.0` até `300.0` Mbps: `R$ 149.90`
- acima de `300.0` Mbps: `R$ 199.90`

Corrija todos os defeitos do programa completo abaixo (sem usar `&&`/`||`):
```c
#include <stdio.h>

int main(void) {
    double mbps, preco;
    scanf("%lf", &mbps);

    if (mbps <= 100.0) {
        preco = 109.90;
    }
    if (mbps <= 20.0) {
        preco = 79.90;
    } else if (mbps <= 300.0) {
        preco = 149.90;
    } else {
        preco = 199.90;
    }

    printf("Plano: R$ %.2f\n", preco);
    return 0;
}
```

### `B05-C03` *(Programa completo independente)*
Escreva um programa completo em C que leia o tempo de permanência em um estacionamento em horas (`double horas`, `horas >= 0`) e calcule o valor a pagar:
- até `1.0` hora: `R$ 8.00`;
- acima de `1.0` até `3.0` horas: `R$ 15.00`;
- acima de `3.0` até `6.0` horas: `R$ 24.00`;
- acima de `6.0` horas: `R$ 24.00` mais `R$ 4.50` por hora excedente acima de `6.0` horas.

Imprima exatamente `Total: R$ X.XX\n`.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `B06` (`Operadores Lógicos e Tabela-Verdade`):** somente após autocorreção da bateria `B05-E01..E06` **e** **100% (3/3)** na Checagem Independente `B05-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** revisar a direção das faixas (`<`/`<=` crescente ou `>`/`>=` decrescente) com rastreio nas fronteiras exatas e aplicar a variante `V2` de `B05`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar o pré-requisito **`B04`** (diferença entre `if`s independentes e cadeia `else if`) e **`A09`** (precisão de `double` em fronteiras).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 6 — Estruturas condicionais: simples e composta).
- `[DOC]` `Aula_07_Algoritmos.pdf` p. 10–15 (`else if`, ordem das condições).
- `[DOC]` `Lista2_Algoritmos.pdf` p. 1 (Ex. 1 — faixas contínuas de desconto).
- `[DOC]` `Lista8_Algoritmos_Revisao.pdf` p. 1 (Ex. 2 — cálculo de frete por faixas e excedente) e `Como_Estruturar_Condicionais_no_Cálculo_de_Frete.mp4`.
- Casos de teste e soluções verificáveis: [B05_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/gabaritos/B05_gabarito.md) e [B05_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_B/testes/B05_testes.md).
