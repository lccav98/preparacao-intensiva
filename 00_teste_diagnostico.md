# Teste Diagnóstico de Posicionamento — Algoritmos e Programação em C

> **Finalidade:** Identificar os pré-requisitos já dominados pelo estudante e posicioná-lo com segurança no bloco inicial adequado da trilha de `CC61A - Algoritmos` (Estágios `A` a `H`).  
> **Princípio de Avaliação:** O posicionamento baseia-se **nos pré-requisitos demonstrados** (e não apenas na soma total de pontos).

---

## Instruções Gerais de Aplicação

1. **Modalidade:** Aplicação **sem consulta** e **sem computador/compilador** (caneta e papel para rascunho/teste de mesa). *(Se necessário confirmar fluência prática após entrada direta em estágio intermediário, o orientador aplicará checagem adicional no bloco sugerido.)*
2. **Tempos-alvo *(estimativas iniciais sujeitas à calibração)*:**
   - **Etapa 1 (Triagem Inicial Curta):** ~15 minutos.
   - **Etapa 2 (Sondagem Específica):** ~10 a 15 minutos por sondagem aplicada (máximo de 2 sondagens na mesma sessão).
3. **Regra contra chute:** Caso não reconheça um conceito ou sintaxe, **marque `[ ] Não sei / Não estudei`** em vez de tentar adivinhar. Isso evita posicionamento acima do domínio real.
4. **Convenção de código nos itens:** Todos os trechos em C pressupõem o cabeçalho padrão necessário (`#include <stdio.h>`, e `<stdbool.h>` / `<string.h>` quando indicado) e padrão **C99**. Saídas ignoram acentuação, conforme convenção das listas da disciplina.

---

## Regras Obrigatórias de Interrupção (Preenchimento pelo Orientador)

Siga rigorosamente estas 5 regras durante a aplicação para evitar fadiga e exposição a conteúdos muito além do nível atual do estudante:

| Regra | Condição de Disparo | Ação Imediata |
|---|---|---|
| **`I1` — Dois erros seguidos na Triagem** | O estudante erra ou marca *"Não sei"* em **2 itens consecutivos** da Triagem (`T_k` e `T_{k+1}`). | **Interromper imediatamente a Etapa 1** (não aplicar `T_{k+2}..T8`). Seguir apenas para a Sondagem do estágio correspondente ao **primeiro item falho** (`T_k`). |
| **`I2` — Iniciante absoluto ou falha em `T1`** | O estudante declara nunca ter programado em C **ou** erra / marca *"Não sei"* em **`T1`**. | **Interromper imediatamente a Etapa 1** (não aplicar `T2`–`T8`). Se declarou nunca ter tido contato com C, posicionar diretamente em **`A01`**; se teve algum contato, aplicar apenas a Sondagem **`S-A`**. |
| **`I3` — Travamento prolongado por item** | O estudante permanece travado por **mais de 3 minutos** em um único item da Triagem sem avançar. | Solicitar que pule e registre como *"Não demonstrado / tempo excedido"*, prosseguindo apenas se `I1` e `I2` ainda não tiverem disparado. |
| **`I4` — Falha no item-âncora da Sondagem** | Na Etapa 2, o estudante erra ou marca *"Não sei"* no **item 1 (`*-01`, item-âncora)** da Sondagem `S-X`. | **Interromper imediatamente a Sondagem `S-X`** (não aplicar `*-02` e `*-03`) e posicionar no bloco inicial do estágio `X` (ou no pré-requisito anterior se aplicável). |
| **`I5` — Limite de Sondagens e menor pré-requisito** | O estudante apresenta lacunas em múltiplos estágios. | Aplicar **no máximo 2 sondagens** na mesma sessão e posicionar sempre no **menor pré-requisito ainda não demonstrado** (ver Matriz de Decisão no gabarito). |

---

## Etapa 1 — Triagem Inicial Curta (`T1` a `T8`)

> **Orientação ao aluno:** Execute passo a passo no papel. Pare imediatamente se o orientador indicar uma regra de interrupção.

### `T1` — Estágio A: Memória, Atribuição e Entrada/Saída
Analise o programa completo abaixo:

```c
#include <stdio.h>

int main(void) {
    int p = 14, q = 5;
    double nota;

    p = p - q;
    q = p + q;
    p = q - p;

    scanf("%lf", nota);
    printf("%d %d\n", p, q);
    return 0;
}
```

**(a)** Qual seria a saída do `printf` caso a linha do `scanf` não tivesse erro?  
**(b)** Qual erro existe na chamada `scanf("%lf", nota);`?  
`[ ] Não sei / Não estudei`

---

### `T2` — Estágio B (Parte 1): Divisão Inteira, Resto e Precedência
Preveja exatamente o que será impresso pelo programa abaixo:

```c
#include <stdio.h>

int main(void) {
    int a = 7, b = 2;
    double r = a / b;
    int expr = 2 + 6 / 2 * 3;
    int resto = a % b;

    printf("%.1f %d %d\n", r, expr, resto);
    return 0;
}
```

**Saída prevista:** `_______________________________`  
`[ ] Não sei / Não estudei`

---

### `T3` — Estágio B (Parte 2): `else if`, Operadores Lógicos e `switch`
Preveja exatamente o que será impresso em cada parte:

**Parte (a):**
```c
int x = 16, y = 4;
if (x > 15 || y < 5 && x == 10) {
    printf("P");
} else if (x >= 10) {
    printf("Q");
} else if (y == 4) {
    printf("R");
} else {
    printf("S");
}
```

**Parte (b):**
```c
int cod = 2;
switch (cod) {
    case 1: printf("A");
    case 2: printf("B");
    case 3: printf("C"); break;
    default: printf("D");
}
```

**Saída (a):** `________` | **Saída (b):** `________`  
`[ ] Não sei / Não estudei`

---

### `T4` — Estágio C: Rastreamento de Repetição (`while` e `for`)
Sem compilar, faça o teste de mesa dos dois trechos abaixo:

**Trecho (a):**
```c
int k = 12;
while (k < 10) {
    printf("%d ", k);
    k += 2;
}
printf("F:%d\n", k);
```

**Trecho (b):**
```c
int i, soma = 0;
for (i = 1; i <= 7; i += 3) {
    soma += i;
}
printf("%d %d\n", soma, i);
```

**Saída (a):** `________________` | **Saída (b):** `________________`  
`[ ] Não sei / Não estudei`

---

### `T5` — Estágio D: Vetores 1D e Strings (`'\0'`)
Preveja exatamente a saída do programa abaixo:

```c
#include <stdio.h>

int main(void) {
    int v[5] = {-7, -2, -9, -2, -5};
    int maior = v[0], pos = 0;
    for (int i = 1; i < 5; i++) {
        if (v[i] > maior) {
            maior = v[i];
            pos = i;
        }
    }

    char texto[12] = "ALGORITMO";
    texto[4] = '\0';

    printf("%d %d %s\n", maior, pos, texto);
    return 0;
}
```

**Saída prevista:** `_______________________________`  
`[ ] Não sei / Não estudei`

---

### `T6` — Estágio E: Matrizes 2D e Índices
Considere a matriz abaixo e o trecho de código que a percorre:

```c
int m[3][3] = {
    {2, 4, 1},
    {5, 3, 6},
    {7, 8, 9}
};
int soma_sec = 0;
for (int i = 0; i < 3; i++) {
    soma_sec += m[i][2 - i];
}
printf("%d | ", soma_sec);
for (int j = 0; j < 3; j++) {
    printf("%d ", m[j][0]);
}
```

**Saída prevista:** `_______________________________`  
`[ ] Não sei / Não estudei`

---

### `T7` — Estágio F: Funções, Passagem de Valor/Endereço e Multi-Arquivo
Analise o programa abaixo e responda às duas perguntas:

```c
#include <stdio.h>

void ajustar(int x, int *y) {
    x = x + 10;
    *y = *y + 10;
}

int main(void) {
    int a = 3, b = 4;
    ajustar(a, &b);
    printf("%d %d\n", a, b);
    return 0;
}
```

**(a)** Qual a saída impressa pelo programa?  
**(b)** Ao compilar um projeto dividido em `main.c`, `calc.h` e `calc.c` usando apenas `gcc main.c -o app`, qual erro típico de ligação ocorre (e por quê)?  
`[ ] Não sei / Não estudei`

---

### `T8` — Estágio G: Recursividade e Pilha de Execução
Faça o rastreamento da função recursiva abaixo para a chamada `eco(3);` **sem utilizar computador**:

```c
#include <stdio.h>

void eco(int n) {
    if (n == 0) {
        return;
    }
    printf("I%d ", n);
    eco(n - 1);
    printf("V%d ", n);
}
```

**(a)** Qual é a condição do **caso base**?  
**(b)** Qual é a saída exata impressa por `eco(3);`?  
`[ ] Não sei / Não estudei`

---

## Etapa 2 — Sondagens Específicas (`S-A` a `S-G`)

> **Orientação ao orientador:** Aplique apenas a(s) sondagem(ns) indicada(s) pelo resultado da Etapa 1 (no máximo 2 por sessão). Se o **item 1 (`*-01`)** de uma sondagem falhar, **pare imediatamente aquela sondagem (`I4`)**.

---

### Sondagem `S-A` — Fundamentos, C Básico e Representação de Dados

- **`SA-01` (Item-âncora | Blocos `A01`–`A02`):** Observe o programa incompleto abaixo. Ele compila no GCC do Linux? Liste **3 problemas** que impedem sua compilação ou execução correta.
```c
#include <stdio.h>
Int main(void) {
    printf("Ola UTFPR\n")
    return 0
}
```
`[ ] Não sei / Não estudei`

- **`SA-02` (Blocos `A03`–`A07`):**
  1. Quais dos identificadores a seguir são **válidos** em C: `nota_1`, `2aluno`, `total$`, `float`, `_contador`?
  2. Escreva as 3 linhas em C necessárias para trocar os valores das variáveis `int x = 10, y = 25;` usando uma variável auxiliar `aux`.  
`[ ] Não sei / Não estudei`

- **`SA-03` (Blocos `A08`–`A09`):**
  1. Quantos valores distintos podem ser representados com **6 bits**? E qual o número mínimo de bits necessários para representar **500 estados distintos**?
  2. Por que `float x = 0.1f;` exibido com `%.20f` frequentemente não imprime exatamente `0.10000000000000000000`, e qual tipo entre `float` e `double` oferece maior precisão?  
`[ ] Não sei / Não estudei`

---

### Sondagem `S-B` — Expressões e Estruturas Condicionais

- **`SB-01` (Item-âncora | Blocos `B01`–`B02`):** Leia dois inteiros `a = 9` e `b = 4`. Escreva a expressão em C que armazena em `double media` o resultado real `2.25` (sem alterar os tipos `int a, b;`), e calcule `9 / 4 * 4 + 9 % 4`.  
`[ ] Não sei / Não estudei`

- **`SB-02` (Blocos `B03`–`B05`):** Identifique o erro lógico na cadeia condicional abaixo (destinada a classificar notas: `>= 9.0` Ótimo, `>= 6.0` Aprovado, `< 6.0` Reprovado) e reescreva a ordem correta sem usar operadores lógicos `&&` ou `||`:
```c
if (nota >= 6.0) {
    printf("Aprovado\n");
} else if (nota >= 9.0) {
    printf("Otimo\n");
} else {
    printf("Reprovado\n");
}
```
`[ ] Não sei / Não estudei`

- **`SB-03` (Blocos `B06`–`B09`):**
  1. Em C, por que a condição `if (10 <= idade <= 18)` está logicamente errada para testar o intervalo $[10, 18]$? Como escrevê-la corretamente?
  2. Escreva um `switch (op)` que imprima `"Desconto"` quando `int op` for `1`, `2` ou `3`, `"Normal"` para `4`, e `"Invalido"` nos demais casos, evitando código duplicado.  
`[ ] Não sei / Não estudei`

---

### Sondagem `S-C` — Estruturas de Repetição e Rastreamento

- **`SC-01` (Item-âncora | Blocos `C01`–`C03`):** Um programa deve ler inteiros não negativos até que o usuário digite `-1` (valor de parada que **não** deve entrar na soma) e imprimir a soma dos valores válidos lidos. Explique os 2 erros no trecho abaixo e corrija-o usando `while`:
```c
int x, soma = 0;
while (x != -1) {
    scanf("%d", &x);
    soma += x;
}
```
`[ ] Não sei / Não estudei`

- **`SC-02` (Blocos `C04`–`C06`):** Preveja exatamente a saída de cada trecho sem compilar:
  1. `int c = 0; do { c += 3; } while (c < 3); printf("%d\n", c);`
  2. `int i; for (i = 0; i < 4; i++); printf("%d\n", i);` *(atenção ao `;`)*  
`[ ] Não sei / Não estudei`

- **`SC-03` (Blocos `C07`–`C09`):**
  1. Qual será a saída de:
     ```c
     for (int i = 1; i <= 5; i++) {
         if (i == 3) continue;
         if (i == 5) break;
         printf("%d ", i);
     }
     ```
  2. Escreva os dois laços `for` aninhados que imprimem um triângulo retângulo de `*` com 4 linhas (1 `*` na linha 1, 2 na linha 2, ..., 4 na linha 4).  
`[ ] Não sei / Não estudei`

---

### Sondagem `S-D` — Vetores 1D e Strings

- **`SD-01` (Item-âncora | Blocos `D01`–`D02`):** Dado `int v[4] = {10, 20, 30, 40};`:
  1. Qual é o índice do último elemento válido e o que ocorre ao acessar `v[4]` em C?
  2. Escreva um trecho com `for` que percorra `v` (de tamanho `4`) uma única vez para calcular a média real `(double)` dos elementos e encontrar o índice da **última ocorrência** do menor elemento.  
`[ ] Não sei / Não estudei`

- **`SD-02` (Blocos `D03`–`D05`):** Dado um vetor `int a[6] = {2, 5, 2, 5, 2, 8};` e o padrão `int p[3] = {2, 5, 2};`:
  1. Qual deve ser o valor máximo do índice inicial `i` no laço externo de busca de `p` dentro de `a` para não acessar fora dos limites de `a`?
  2. Quantas ocorrências consecutivas de `p` existem em `a` quando se permite **sobreposição**?  
`[ ] Não sei / Não estudei`

- **`SD-03` (Blocos `D06`–`D09`):**
  1. Por que `char sigla[4] = "UTFPR";` está incorreto em C?
  2. Como copiar e comparar corretamente o conteúdo de `char s1[20]` e `char s2[20]` usando `<string.h>` (e por que `s1 == s2` não compara o texto)?
  3. Em uma grade de `4` linhas por `5` colunas armazenada em um único vetor linear `g`, qual índice 1D corresponde à posição `(linha = 2, coluna = 3)`?  
`[ ] Não sei / Não estudei`

---

### Sondagem `S-E` — Matrizes Bidimensionais

- **`SE-01` (Item-âncora | Blocos `E01`–`E02`):** Considere `int mat[3][4];`:
  1. Quantos elementos cabem na matriz e quais são os índices válidos de linha e coluna?
  2. No código de busca abaixo, um aluno usou `break;` no laço interno esperando sair dos dois laços assim que achasse `alvo`. Por que isso não basta e como corrigir?
     ```c
     int li = -1, co = -1;
     for (int i = 0; i < 3; i++) {
         for (int j = 0; j < 4; j++) {
             if (mat[i][j] == alvo) {
                 li = i; co = j;
                 break;
             }
         }
     }
     ```
`[ ] Não sei / Não estudei`

- **`SE-02` (Blocos `E03`–`E04`):** Em uma matriz quadrada `N × N` (`N = 4`), escreva as condições ou expressões de índice para:
  1. Elementos da diagonal principal;
  2. Elementos da diagonal secundária;
  3. Elementos **estritamente acima** da diagonal principal.  
`[ ] Não sei / Não estudei`

- **`SE-03` (Blocos `E05`–`E07`):**
  1. Se uma matriz `A` tem dimensões `3 × 5`, quais devem ser as dimensões de sua transposta `T` e qual atribuição preenche `T` a partir de `A`?
  2. Dadas $A_{2 \times 3}$ e $B_{3 \times 4}$, quais as dimensões da matriz produto $C = A \cdot B$ e quantas multiplicações escalares compõem cada elemento `C[i][j]`?  
`[ ] Não sei / Não estudei`

---

### Sondagem `S-F` — Modularização, Funções, Ponteiros e Multi-Arquivo

- **`SF-01` (Item-âncora | Blocos `F01`–`F03`):** Observe o código abaixo:
```c
#include <stdio.h>

int main(void) {
    printf("%d\n", dobro(5));
    return 0;
}

int dobro(int x) {
    return 2 * x;
}
```
  1. O que falta antes de `main` para o programa compilar corretamente sem erro/aviso de declaração implícita?
  2. Se criarmos `void triplicar(int n) { n = 3 * n; }` e chamarmos `triplicar(a);` com `a = 4`, quanto valerá `a` após a chamada e por quê?  
`[ ] Não sei / Não estudei`

- **`SF-02` (Blocos `F04`–`F05`):**
  1. Na função `void trocar(int *a, int *b)`, explique o bug fatal do código `int *tmp; *tmp = *a; *a = *b; *b = *tmp;` e escreva a correção.
  2. Se outra função `void ordena(int *p, int *q)` precisa chamar `trocar`, ela deve chamar `trocar(&p, &q)` ou `trocar(p, q)`? Justifique.  
`[ ] Não sei / Não estudei`

- **`SF-03` (Blocos `F06`–`F09`):**
  1. Na assinatura de uma função que apenas lê uma matriz `4 × 5` sem alterá-la, por que `void exibir(int m[][])` é inválido em C e qual é a assinatura recomendada com `const`?
  2. Em um projeto com `main.c`, `filtros.h` e `filtros.c`, onde devem ficar as **definições** das funções, para que servem `#ifndef FILTROS_H / #define FILTROS_H / #endif`, e qual comando `gcc` compila o projeto?  
`[ ] Não sei / Não estudei`

---

### Sondagem `S-G` — Recursividade e Pilha de Execução

- **`SG-01` (Item-âncora | Blocos `G01`–`G02`):** Preveja a saída exata de `contar_rec(3);` e explique o que acontece se a linha `if (n <= 0) return;` for removida:
```c
void contar_rec(int n) {
    if (n <= 0) return;
    contar_rec(n - 1);
    printf("%d ", n);
}
```
`[ ] Não sei / Não estudei`

- **`SG-02` (Blocos `G03`–`G05`):** Implemente a função `int soma_pares(const int v[], int n)` **sem usar `for`, `while` ou `do-while`**, retornando a soma apenas dos elementos pares do vetor `v` de tamanho `n >= 0`.  
`[ ] Não sei / Não estudei`

- **`SG-03` (Blocos `G06`–`G08`):**
  1. Escreva uma função recursiva `int contar_letra(const char s[], int i, char alvo)` (sem laços) que conte quantas vezes `alvo` aparece em `s` a partir do índice `i`.
  2. Qual o problema de implementar `potencia_rapida(x, n)` calculando `potencia_rapida(x, n/2) * potencia_rapida(x, n/2)` diretamente no `return` em vez de guardar o resultado em uma variável local `int p`?  
`[ ] Não sei / Não estudei`

---

## Resumo do Registro de Posicionamento (Uso do Orientador)

- **Aluno:** `_________________________________________` | **Data:** `____/____/______`
- **Etapa 1 (Triagem):** Itens acertados: `_________________` | Regra de interrupção disparada: `[ ] Nenhuma  [ ] I1  [ ] I2  [ ] I3`
- **Etapa 2 (Sondagem(ns) aplicada(s)):** `_____________` | Regra `I4`/`I5`: `_____________`
- **Bloco Inicial Definido:** `_______` | **Status:** `[ ] DEFINITIVO` `[ ] PROVISÓRIO`
- **Critério do Posicionamento Provisório:** Marque `PROVISÓRIO` sempre que ocorrer pelo menos 1 das 4 condições:
  1. Acertos em "dente de serra" (acertou estágio avançado mas falhou item de estágio anterior);
  2. Fluência muito lenta (acertou no limite de tempo com hesitação ou autocorreções múltiplas);
  3. Domínio apenas teórico/leitura sem evidência de escrita compilável em C;
  4. Entrada direta no **Estágio C ou superior** (exige confirmação prática nas 2 primeiras sessões).
