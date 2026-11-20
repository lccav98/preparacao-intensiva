# Bloco `A07` — Atribuição (`=`), Modelo de Memória e Troca com Variável Auxiliar

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio A — Fundamentos, Ambiente C, Variáveis e Representação / **`A07`** |
| **Micro-habilidade foco** | Executar teste de mesa rastreando sobrescritas de memória com o operador de atribuição `=` e realizar troca segura entre duas ou três variáveis usando variável auxiliar `aux`. |
| **Pré-requisitos** | `A06` *(Entrada de dados com `scanf` e operador `&`)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática (20 min) + checagem (15 min)** — **Sessão (`E01`–`E06`, 20 min):** `11 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** tudo de `A06` + reatribuição `=`, troca em 3 passos com `aux`, rotação cíclica de 3 variáveis com `aux` e, apenas nos testes de mesa no papel (`E01`/`C01`), somas/subtrações elementares (`+`/`-`). Nos arquivos `.c`, concentre-se em entrada, atribuição/troca com `aux` e saída (**proibido** `/`, `%`, `<math.h>`, `if`, laços e vetores). |

### Registro da Sessão (Preenchido na Prática)
- **Sessão (`E01`–`E06`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 6` | **Após corr.:** `___ / 6`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Semântica da atribuição (`=`):** Em `variavel = expressao;`, o computador primeiro **avalia o lado direito** (constante, variável ou expressão) e depois **grava o resultado na variável à esquerda**, sobrescrevendo o valor antigo (`Aula_03` p. 10–11).
2. **Três momentos na memória (`Aula_03` p. 16–18):**
   - **Declaração** (`int a;`): reserva o espaço na memória com conteúdo indeterminado (`?`).
   - **Atribuição / Leitura** (`a = 10;` ou `scanf("%d", &a);`): armazena um novo valor no espaço reservado.
   - **Impressão** (`printf("%d", a);`): apenas lê o valor atual sem modificá-lo.
3. **Por que `a = b; b = a;` falha (`Aula_03` p. 20):** A instrução `a = b;` apaga o valor original de `a`. Quando chega em `b = a;`, ambos já possuem o mesmo valor de `b`.
4. **Troca segura em 3 passos (`aux`):**
   ```c
   aux = a;   /* 1. salva o valor original de a */
   a = b;     /* 2. copia b para a */
   b = aux;   /* 3. recupera o valor salvo em b */
   ```
   A variável auxiliar `aux` deve ter o **mesmo tipo** das variáveis trocadas (ex.: `double aux;` para trocar dois `double`).
5. **Rotação cíclica de 3 variáveis (`a`, `b`, `c`):** Guarde em `aux` a variável que será sobrescrita primeiro, mova as demais na ordem contrária à perda de dados e termine gravando `aux` na última posição do ciclo.

---

## 2. Exemplos Guiados

### Exemplo 1 — Teste de mesa em tabela de memória *(Trecho ilustrativo)*
Acompanhe a evolução da memória para:
```c
int a = 10, b = 4, aux;
aux = a;
a = b + 2;
b = aux - 1;
aux = a + b;
```
| Passo | Instrução | `a` | `b` | `aux` |
|---|---|---:|---:|---:|
| 0 | `int a = 10, b = 4, aux;` | `10` | `4` | `?` |
| 1 | `aux = a;` | `10` | `4` | `10` |
| 2 | `a = b + 2;` | `6` | `4` | `10` |
| 3 | `b = aux - 1;` | `6` | `9` | `10` |
| 4 | `aux = a + b;` | `6` | `9` | `15` |

### Exemplo 2 — Troca de dois inteiros lidos do teclado *(Programa completo)*
```c
#include <stdio.h>

int main(void) {
    int a, b, aux;
    scanf("%d %d", &a, &b);

    printf("Antes: A = %d, B = %d\n", a, b);

    aux = a;
    a = b;
    b = aux;

    printf("Depois: A = %d, B = %d\n", a, b);
    return 0;
}
```
Para entrada `10 20`, imprime `Antes: A = 10, B = 20` e depois `Depois: A = 20, B = 10`.

---

## 3. Exercícios (`A07-E01` a `A07-E06`)

### `A07-E01` *(Teste de Mesa — Reprodução do modelo)*
Sem utilizar computador, preencha a tabela de memória (`x`, `y`, `z`) após cada uma das **5 atribuições** abaixo e informe a saída exata do `printf`:

```c
int x = 8, y = 3, z;
z = x;
x = x - y;
y = z + y;
z = y - x;
x = z;
printf("%d %d %d\n", x, y, z);
```

---

### `A07-E02` *(Análise Conceitual — Falha sem variável auxiliar)*
Considere `double p = 12.5, q = 4.0;` e a tentativa incorreta de troca:
```c
p = q;
q = p;
```
1. Indique os valores finais de `p` e `q` após executar essas duas linhas e explique **qual valor foi perdido e em qual linha**.
2. Escreva as 3 instruções corretas usando `double aux;` para trocar `p` e `q`.

---

### `A07-E03` *(Completar solução — Rotação cíclica de 3 variáveis — Trecho ilustrativo)*
Suponha que `int a, b, c, aux;` já tenham valores lidos. Complete as lacunas `/* A */` a `/* D */` para que, ao final, `a` receba o valor original de `b`, `b` receba o original de `c`, e `c` receba o original de `a`:

```c
aux = /* A */;
a = /* B */;
/* C */ = c;
c = /* D */;
```

---

### `A07-E04` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler dois inteiros `x` e `y`, trocar seus valores e imprimir `x = <novo x>, y = <novo y>`. Identifique o **bug intencional** na troca (no papel ou em comentário `//`) e escreva a **versão corrigida completa**:

```c
#include <stdio.h>

int main(void) {
    int x, y, aux;
    scanf("%d %d", &x, &y);

    x = y;
    aux = x;
    y = aux;

    printf("x = %d, y = %d\n", x, y);
    return 0;
}
```

---

### `A07-E05` *(Variação controlada com pistas — Programa completo)*
Escreva um **programa completo** em C que leia dois números reais `double` (`a` e `b`), exiba seus valores antes da troca, faça a troca usando `double aux` e exiba os valores após a troca exatamente no formato:
```text
Antes: a = <valor>, b = <valor>
Depois: a = <valor>, b = <valor>
```
*(Com 2 casas decimais em todos os valores).*  
*Pistas:* Use `%lf` no `scanf`, `%.2f` no `printf` e declare `aux` também como `double` (não `int`, pois perderia a parte fracionária).

---

### `A07-E06` *(Resolução independente — Programa completo)*
Escreva um **programa completo** em C que leia três inteiros (`a`, `b`, `c`), imprima-os antes da troca, realize a rotação cíclica à direita usando `int aux`:
- `a` recebe o valor original de `c`;
- `b` recebe o valor original de `a`;
- `c` recebe o valor original de `b`;

e imprima exatamente:
```text
Antes: <a> <b> <c>
Depois: <novo a> <novo b> <novo c>
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `A07-C01` *(Teste de Mesa com Tabela de Memória)*
Sem computador, rastreie as **5 atribuições** abaixo montando a tabela de memória (`Instrução | a | b | c`) e informe a saída final exata:
```c
int a = 5, b = 12, c = 2;
c = b - a;
a = a + c;
b = a - 3;
c = b + c;
a = c - b;
printf("%d %d %d\n", a, b, c);
```

### `A07-C02` *(Previsão da falha sem `aux`)*
Para `int u = -4, v = 9;`, preveja os valores finais de `u` e `v` após executar `u = v; v = u;`, explique qual valor foi sobrescrito e escreva a correção com `int aux;`.

### `A07-C03` *(Programa completo — Rotação cíclica de 3 variáveis)*
Escreva um **programa completo** em C que leia três inteiros (`p`, `q`, `r`) e execute uma rotação cíclica à esquerda usando `int aux` (`p` recebe original `q`; `q` recebe original `r`; `r` recebe original `p`), imprimindo exatamente:
```text
Resultado: <p> <q> <r>
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `A08` (`Bits, Bytes e Sistema Binário`) / `A10`:** somente após autocorreção de `A07-E01`..`E06` **e** **100% (3/3)** na Checagem Independente `A07-C01`..`C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** refazer o desenho de caixas de memória passo a passo (`Aula_03` p. 16–21) antes de tocar no teclado e aplicar a variante `V2` de `A07`.
- **Regra das 2 tentativas malsucedidas:** após **2 reprovações** neste bloco, parar repetições e investigar o pré-requisito **`A06`** (`scanf` e endereços `&`) e **`A04`** (declaração e conteúdo inicialmente indeterminado).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 4 — Instruções de entrada, saída e atribuição).
- `[DOC]` `Aula_03_Algoritmos.pdf` p. 9–12 (comando de atribuição `=`, tipos e inicialização) e p. 15–23 (modelo de memória declaração/atribuição/impressão e troca com variável auxiliar `aux`).
- Gabarito e especificação de testes: [A07_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/gabaritos/A07_gabarito.md) e [A07_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/A07_testes.md).
