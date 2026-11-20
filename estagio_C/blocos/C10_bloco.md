# Bloco `C10` — Revisão e Consolidação do Estágio C *(Bloco de Revisão)*

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio C — Estruturas de Repetição e Rastreamento de Laços / **`C10`** |
| **Micro-habilidade foco** | *(Revisão integrada de `C01` a `C09`)* Escolher adequadamente entre `while`, `do-while` e `for`, aplicar sentinelas, controle de fluxo (`break`/`continue`), primalidade, séries numéricas incrementais/por tolerância e laços aninhados sem erros *off-by-one*. |
| **Pré-requisitos** | `C04` *(Pós-condição `do-while`)*, `C07` *(Controle de Fluxo e Primalidade)*, `C08` *(Séries Numéricas)*, `C09` *(Laços Aninhados)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 22 min):** `14 min` resol. \| `5 min` corr. \| `3 min` recup.; **Sessão 2 (`E04`–`E06`, 23 min):** `14 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Conteúdo novo: NENHUM.** **É terminantemente proibido** o uso de vetores ou strings (`char[]`, `int[]` ou qualquer array `v[i]`), funções customizadas além de `int main(void)`, `struct` ou alocação dinâmica. Use estritamente C99 com saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Apto para Estágio D`)

---

## 1. Instruções Curtas (Matriz de Decisão do Estágio C)

1. **Escolha da Estrutura de Repetição Adequada:**
   - **`for` (`C05`, `C09`):** Quando o número de repetições ou intervalo de contagem (`0..n-1`, `1..n`, passo fixo) é conhecido antes da entrada no laço, e na construção de grades/triângulos com laços aninhados.
   - **`while` (`C01`–`C03`, `C08`):** Quando o laço depende de uma pré-condição dinâmica que pode impedir até a 1ª execução (sentinela com *priming read* ou `while (1)` + `break`, algoritmo de Euclides, séries por tolerância `termo >= eps`).
   - **`do-while` (`C04`):** Exclusivamente quando o corpo deve executar **ao menos uma vez** antes do teste final (menus interativos combinados com `switch` e validação repetida).

2. **Checklist Anti-Armadilhas do Estágio C:**
   - **Comando nulo (`C06`):** Nunca coloque `;` após `for (...)` ou `while (...)`.
   - **`continue` em `while` (`C07`):** Garanta que a leitura ou atualização ocorra antes do `continue` (ou use `while (1)` com leitura no topo).
   - **`break` em `switch` dentro de laço (`C07`):** O `break` do `case` sai apenas do `switch`, nunca do laço externo.
   - **Séries numéricas (`C08`):** Use `double` e literais `1.0` para evitar divisão inteira e *overflow*; avalie `termo >= eps` antes de somar; mantenha `k < n` para não zerar denominadores `(n - k)`.
   - **Laços aninhados (`C09`):** Posicione `printf("\n");` após o laço interno `j` e use largura fixa (`%3d`, `%4d`) para tabelas alinhadas.

---

## 2. Exemplos Guiados

### Exemplo 1 — Seleção Integrada: `while` + Sentinela + Atualização de Extremos
Lembrando o padrão seguro contra entrada vazia e números todos negativos:

```c
#include <stdio.h>

int main(void) {
    int val, soma = 0, maior = 0, qtd = 0;

    while (1) {
        if (scanf("%d", &val) != 1 || val == 0) {
            break;
        }
        soma += val;
        qtd++;
        if (qtd == 1 || val > maior) {
            maior = val; // Inicializado com o 1o valor valido, nunca com 0
        }
    }

    if (qtd == 0) {
        printf("Vazio\n");
    } else {
        printf("Soma = %d | Maior = %d\n", soma, maior);
    }
    return 0;
}
```

---

### Exemplo 2 — Integração `for` Contado + Série Incremental
Para $H_n = \sum_{k=1}^{n} \frac{1}{k}$ sem divisão inteira:

```c
double h = 0.0;
for (int k = 1; k <= n; k++) {
    h += 1.0 / k; // 1.0 forca divisao em double
}
```

---

## 3. Exercícios (`C10-E01` a `C10-E06`)

### Sessão 1 (`C10-E01` a `C10-E03` — Rastreamento e Caça aos Bugs Integrados)

### `C10-E01` *(Teste de Mesa Integrado — `for`, `continue` e Laços Aninhados)*
Sem usar computador, analise o trecho abaixo e faça o rastreamento completo:

```c
int total = 0;
for (int i = 1; i <= 4; i++) {
    if (i == 2) {
        continue;
    }
    for (int j = 1; j <= i; j++) {
        total += i + j;
        printf("%2d", i + j);
    }
    printf("\n");
}
printf("Total = %d\n", total);
```

1. Indique o que acontece na iteração `i = 2`.
2. Desenhe linha por linha a saída exata impressa no terminal (incluindo espaços de `%2d` e a linha final `Total = ...`).

---

### `C10-E02` *(Caça ao Bug 1 — Sentinela, `continue` em `while` e Máximo com Negativos)*
O programa abaixo deveria ler números inteiros até a sentinela `-1`, ignorar os múltiplos de `5` (`num % 5 == 0`), e imprimir a soma e o maior valor entre os números válidos restantes (ou `Nenhum valor valido\n` se nenhum for computado):

```c
#include <stdio.h>

int main(void) {
    int num;
    int soma = 0;
    int maior = 0;

    while (num != -1) {             // Bug 1: num nao lido antes e -1 entra no corpo
        scanf("%d", &num);
        if (num % 5 == 0) {
            continue;               // Funciona aqui apenas porque scanf esta no topo
        }
        soma += num;                // Bug 2: soma a sentinela -1 quando digitada!
        if (num > maior) {          // Bug 3: maior = 0 falha se todos forem negativos
            maior = num;
        }
    }

    printf("Soma = %d\nMaior = %d\n", soma, maior);
    return 0;
}
```

1. Liste os **3 bugs** presentes no código (incluindo o comportamento com entrada `-10 -3 -5 -1` e com entrada vazia `-1`).
2. Escreva o programa corrigido completo em C99 ([C10_E02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C10_E02_corrigido.c)).

---

### `C10-E03` *(Caça ao Bug 2 — Divisão Inteira e Divisão por Zero em Série Alternada)*
Um aluno tentou calcular o somatório $S = \sum_{k=0}^{n-1} \frac{(-1)^k}{(n - k)^2}$ para um inteiro positivo `n`:

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    if (n <= 0) {
        printf("Entrada Invalida\n");
        return 0;
    }

    double soma = 0.0;
    int sinal = 1;
    for (int k = 0; k <= n; k++) { // Bug 1: limite <= n zera o denominador
        soma += sinal / ((n - k) * (n - k)); // Bug 2: divisao inteira
        sinal = -sinal;
    }

    printf("S = %.6f\n", soma);
    return 0;
}
```

1. Explique os dois bugs graves no laço `for`.
2. Escreva a versão corrigida completa em C99 ([C10_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C10_E03_corrigido.c)) prevenindo também *overflow* no cálculo de $(n - k)^2$.

---

### Sessão 2 (`C10-E04` a `C10-E06` — Programas Completos Integradores)

### `C10-E04` *(Menu `do-while` + `switch` Integrando Euclides e Primalidade)*
Escreva um programa completo em C99 ([C10_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C10_E04.c)) que mantenha um menu repetido via `do-while` com `switch (opcao)` até que `opcao == 0`:
- **Opção `1`:** Leia dois inteiros (`long long a, b`). Se `a <= 0 || b <= 0`, imprima `Entrada Invalida\n`. Caso contrário, calcule o MDC pelo Algoritmo de Euclides e imprima `MDC = %lld\n`.
- **Opção `2`:** Leia um inteiro (`long long n`), verifique se é primo (tratando $n \le 1$, $n = 2$, pares e ímpares até $\sqrt{n}$) e imprima `Primo\n` ou `Nao Primo\n`.
- **Opção `0`:** Imprima `Encerrando\n` e termine o laço.
- **Qualquer outra opção (`default`):** Imprima `Opcao Invalida\n`.

*Exemplo de entrada:* `1 12 18 2 17 0`  
*Saída esperada:*
```text
MDC = 6
Primo
Encerrando
```

---

### `C10-E05` *(Sentinela com Estatísticas e Contagem de Primos)*
Escreva um programa completo em C99 ([C10_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C10_E05.c)) que leia uma sequência de números inteiros (`long long`) até que a sentinela `0` seja digitada.
- Se `0` for digitado logo na primeira leitura, imprima apenas: `Nenhum numero valido\n`.
- Para os números válidos lidos antes do `0`, calcule e imprima ao final:
  ```text
  Qtd: %d
  Primos: %d
  Maior: %lld
  Media: %.2f
  ```
*(Lembre-se: inteiros negativos e `1` não são primos; `maior` deve funcionar corretamente mesmo se todos os números forem negativos).*

*Exemplo de entrada:* `7 4 13 1 2 0`  
*Saída esperada:*
```text
Qtd: 5
Primos: 3
Maior: 13
Media: 5.40
```

---

### `C10-E06` *(Série Alternada de $\sin(x)$ por Tolerância $\varepsilon$)*
A série de Taylor para $\sin(x)$ é dada por:
$$\sin(x) = \sum_{k=0}^{\infty} (-1)^k \frac{x^{2k+1}}{(2k+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots$$

Escreva um programa completo em C99 ([C10_E06.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C10_E06.c)) que leia `double x` e `double eps`:
1. Se `eps <= 0.0`, imprima `Entrada Invalida\n` e encerre.
2. Inicie com `termo = x` ($k = 0$) e atualize incrementalmente o próximo termo a cada passo por:
   $$\text{termo}_k = -\text{termo}_{k-1} \cdot \frac{x^2}{(2k)(2k+1)}$$
3. Some os termos **apenas enquanto** $|\text{termo}| \ge \varepsilon$ (ou seja, `termo >= eps || termo <= -eps`, sem usar `<math.h>`).
4. Imprima:
   ```text
   sen(x) aprox: %.6f
   Termos = %d
   ```

*Exemplo de entrada:* `1.0 0.001`  
*Saída esperada:*
```text
sen(x) aprox: 0.841667
Termos = 3
```

---

## 4. Checagem Independente de Domínio (`C10-C01` a `C10-C03`)

> **Instruções:** Resolva estas 3 questões sem consulta a materiais ou gabaritos. Tempo limite: 18 minutos. Exige **100% de acerto (3/3)** para concluir o Estágio C.

### `C10-C01` *(Teste de Mesa Integrador — `do-while` + `switch` com *Fall-Through*)*
Sem usar computador, determine os valores finais de `x` e `soma` e a saída exata do programa:

```c
int x = 1, soma = 0;
do {
    switch (x % 3) {
        case 1:
            soma += x;
            break;
        case 2:
            soma += x * 2;
        default:
            soma += 1;
            break;
    }
    x++;
} while (x <= 4);
printf("x = %d, soma = %d\n", x, soma);
```

Apresente o rastreamento completo para cada iteração (`x = 1, 2, 3, 4`) e a linha impressa.

---

### `C10-C02` *(Programa Completo — Contagem e Soma de Primos em Intervalo $[a, b]$)*
Escreva um programa completo em C99 ([C10_C02.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C10_C02.c)) que leia dois inteiros `long long a, b`.
- Se `b < a`, imprima `Intervalo Invalido\n` e encerre.
- Caso contrário, percorra todos os inteiros $n$ no intervalo fechado $[a, b]$ utilizando um laço externo e verifique a primalidade de cada $n$ com laço interno (com `break` antecipado ao achar divisor), contabilizando a quantidade e a soma dos números primos encontrados.
- Imprima:
  ```text
  Qtd Primos: %d
  Soma Primos: %lld
  ```

*Exemplo de entrada:* `1 10`  
*Saída esperada:*
```text
Qtd Primos: 4
Soma Primos: 17
```

---

### `C10-C03` *(Programa Completo — Tabela Triangular de Multiplicação com Laços Aninhados)*
Escreva um programa completo em C99 ([C10_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/solucoes/C10_C03.c)) que leia um inteiro `n`.
- Se `n <= 0`, imprima `Entrada Invalida\n`.
- Caso contrário, imprima uma tabela triangular inferior de multiplicação com `n` linhas, na qual cada linha `i` ($1 \le i \le n$) exibe `i` colunas `j` ($1 \le j \le i$) contendo o produto `i * j` formatado com `%4d`, seguido de `\n` ao fim de cada linha.

*Exemplo de entrada:* `4`  
*Saída esperada:*
```text
   1
   2   4
   3   6   9
   4   8  12  16
```

---

## 5. Orientação de Avanço ou Recuperação (Conclusão do Estágio C)

- **Avançar para o Estágio D (`D01 — Vetores 1D: Declaração, Índices Base 0 e Limites`):** somente após autocorreção dos exercícios `C10-E01..E06` **e** **100% de acerto (3/3)** na Checagem Independente `C10-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada por sub-habilidade (1ª falha):**
  - Falha em escolha de laços, sentinela ou extremos negativos $\rightarrow$ revisar **`C03`** e **`C04`**.
  - Falha em rastreamento, `continue`/`break` ou primalidade $\rightarrow$ revisar **`C06`** e **`C07`**.
  - Falha em séries numéricas ou precisão/divisão $\rightarrow$ revisar **`C08`**.
  - Falha em laços aninhados ou alinhamento tabular $\rightarrow$ revisar **`C09`**.
- **Após 2 tentativas malsucedidas:** interromper novas tentativas em `C10`, diagnosticar qual pré-requisito (`C04`, `C07`, `C08` ou `C09`) falhou e reabilitá-lo integralmente antes de refazer a checagem de conclusão do Estágio C.

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 7 — estruturas de repetição).
- `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 2 (18/09 a 25/09 — repetição e consolidação).
- `[DOC]` `Aula_09` a `Aula_11` (pré-condição, `for`, controle de fluxo, laços aninhados).
- `[DOC]` `Lista4_Algoritmos.pdf`, `Lista5_Algoritmos.pdf` e `Lista8_Algoritmos_Revisao.pdf` p. 1–2 (Ex. 3–5).
- Casos de teste e soluções verificáveis: [C10_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/gabaritos/C10_gabarito.md) e [C10_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_C/testes/C10_testes.md).
