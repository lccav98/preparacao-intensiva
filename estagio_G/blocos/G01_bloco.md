# Bloco `G01` — Conceito de Recursividade e Pilha de Execução (Rastreamento de Chamadas e Retornos)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio G — Recursividade e Pilha de Execução / **`G01`** |
| **Micro-habilidade foco** | Identificar o tripé recursivo (caso base, passo recursivo e progresso) e rastrear manualmente o empilhamento de chamadas e desempilhamento de retornos na pilha de execução sem executar o programa. |
| **Pré-requisitos** | `F10` *(Revisão e Consolidação do Estágio F — Modularização, Funções e Ponteiros)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem (22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 15 min):** `10 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **100% leitura, identificação e teste de mesa no papel.** **Não há** escrita livre de funções recursivas (`G03`+), programas `.c` para compilar, uso de pilha como estrutura de dados explícita (`struct`/vetores de pilha), vetores (`G04`), strings (`G06`) ou recursão múltipla (`G08`). Nenhuma função recursiva utiliza laços (`for`, `while`, `do-while`). |

### Registro da Sessão (Preenchido na Prática)
- **Sessão (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **O que é recursividade em C:** Não existe comando especial para recursão em C; uma função é **recursiva** quando chama a si mesma direta ou indiretamente. Cada nova chamada cria um **novo quadro de ativação** independente na memória, com suas próprias cópias de parâmetros e variáveis locais.
2. **O tripé obrigatório de toda função recursiva correta:**
   - **Caso base:** condição de parada que devolve um resultado diretamente (ou encerra) **sem** fazer nova chamada recursiva.
   - **Passo recursivo:** chamada da função a si mesma sobre uma versão menor/mais simples do problema.
   - **Progresso estrito:** cada passo recursivo deve aproximar os argumentos do caso base.
3. **Pilha de execução (regra de ouro):** Cada chamada ativa fica empilhada aguardando a resposta da chamada que ela disparou. Vale sempre a regra: **"a chamada mais recente termina primeiro"**. Somente quando o caso base retorna é que os quadros pendentes começam a concluir e desempilhar, do topo para a base.
4. **Caso base inalcançável e *stack overflow*:** Se faltar caso base, se a condição nunca for atingida para a entrada dada (ex.: pular de `1` para `-1` quando o caso base testa `n == 0`), ou se o passo recursivo afastar o valor do caso base (ex.: `n + 1` rumo a `0`), as chamadas se acumulam até esgotar a memória reservada à pilha — erro fatal conhecido como ***stack overflow*** (estouro de pilha).

---

## 2. Exemplos Guiados *(100% no papel)*

### Exemplo 1 — Tripé e pilha de execução de `somaAte(4)` *(Trecho ilustrativo)*
```c
int somaAte(int n) {
    if (n <= 1) {               /* Caso base */
        return n;
    }
    return n + somaAte(n - 1);  /* Passo recursivo com progresso (n - 1) */
}
```
Rastreando `somaAte(4)` na pilha de execução:
```text
Descida (empilhamento de quadros pendentes):
  somaAte(4) -> aguarda 4 + somaAte(3)
    somaAte(3) -> aguarda 3 + somaAte(2)
      somaAte(2) -> aguarda 2 + somaAte(1)
        somaAte(1) -> atinge caso base (n <= 1) e retorna 1

Subida (desempilhamento — chamada mais recente termina primeiro):
        somaAte(1) retorna 1
      somaAte(2) recebe 1 -> retorna 2 + 1 = 3
    somaAte(3) recebe 3 -> retorna 3 + 3 = 6
  somaAte(4) recebe 6 -> retorna 4 + 6 = 10
```
Observe: no instante em que `somaAte(1)` executa, existem **4 quadros ativos simultaneamente** na pilha, cada um com seu próprio `n` (`4`, `3`, `2`, `1`).

### Exemplo 2 — Caso base inalcançável e *stack overflow* *(Trecho ilustrativo)*
```c
int f_quebrada(int n) {
    if (n == 0) {
        return 1;
    }
    return n * f_quebrada(n + 1); /* ERRO: afasta-se de 0! */
}
```
Ao chamar `f_quebrada(3)`: `3 -> 4 -> 5 -> 6 -> ...`. Como `n` cresce indefinidamente, `n == 0` **nunca** é alcançado e o programa sofre *stack overflow*.

---

## 3. Exercícios (`G01-E01` a `G01-E05` — Papel)

### `G01-E01` *(Identificação do tripé e teste de mesa — Reprodução do modelo)*
Considere a função recursiva abaixo (sem uso de computador):
```c
int fat(int n) {
    if (n == 0) {
        return 1;
    }
    return n * fat(n - 1);
}
```
**(a)** Identifique explicitamente qual linha representa o **caso base**, qual linha representa o **passo recursivo** e o que garante o **progresso** para `n >= 0`.  
**(b)** Desenhe o empilhamento de chamadas e os valores retornados no desempilhamento para `fat(4)`.

---

### `G01-E02` *(Completar tabela de pilha de execução)*
Analise a função abaixo e complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` para a chamada `soma_pares(6)`:
```c
int soma_pares(int n) {
    if (n <= 0) {
        return 0;
    }
    if (n % 2 == 0) {
        return n + soma_pares(n - 2);
    }
    return soma_pares(n - 1);
}
```
| Ordem da chamada | Expressão pendente na descida | Valor retornado na subida |
|---|---|---|
| 1ª | `soma_pares(6) = 6 + soma_pares(4)` | `/* D */` |
| 2ª | `/* A */` | `/* C */` |
| 3ª | `soma_pares(2) = 2 + soma_pares(0)` | `2 + 0 = 2` |
| 4ª (topo) | `/* B */` | `0` |

---

### `G01-E03` *(Caça ao Caso Base Inalcançável — Detecção de Stack Overflow)*
Cada função abaixo provoca *stack overflow* para a chamada indicada. Para cada caso, trace as primeiras 4 chamadas da pilha, explique o motivo da falha e escreva a correção mínima:

**(1)** Chamada `f(3)`:
```c
int f(int n) {
    if (n == 0) {
        return 1;
    }
    return n * f(n + 1);
}
```
**(2)** Chamada `g(4)`:
```c
int g(int n) {
    if (n == 1) {
        return 1;
    }
    return n + g(n - 2);
}
```

---

### `G01-E04` *(Variação controlada com pistas — Pilha com dois parâmetros)*
Rastreie no papel a chamada `misterio(4, 3)` para a função abaixo:
```c
int misterio(int a, int b) {
    if (b == 0) {
        return 0;
    }
    return a + misterio(a, b - 1);
}
```
**(a)** Liste todos os quadros empilhados com seus respectivos valores de `(a, b)` e o valor retornado por cada quadro na volta.  
**(b)** Qual operação aritmética `misterio(a, b)` calcula para `b >= 0`?  
*Pista:* Observe qual parâmetro permanece constante e qual parâmetro controla o progresso até o caso base.

---

### `G01-E05` *(Resolução independente — Variáveis locais independentes por quadro)*
Rastreie no papel a chamada `calc(4)` sem usar computador:
```c
int calc(int n) {
    int k = n * 2;
    if (n <= 1) {
        return 1;
    }
    return k + calc(n - 1);
}
```
**(a)** Monte a tabela ou diagrama de pilha indicando, para cada quadro ativo, os valores de `n`, `k` e o valor devolvido no retorno.  
**(b)** Por que o valor `k = 2` calculado dentro de `calc(1)` **não** sobrescreve o valor `k = 8` pertencente ao quadro de `calc(4)`?

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `G01-C01` *(Rastreamento completo de pilha)*
Sem usar computador, rastreie `pot2(4)` indicando:
1. A sequência exata de chamadas empilhadas (da base até o topo da pilha);
2. Quantos quadros de `pot2` chegam a existir simultaneamente no pico da pilha;
3. A ordem exata e os valores retornados no desempilhamento.
```c
int pot2(int n) {
    if (n == 0) {
        return 1;
    }
    return 2 * pot2(n - 1);
}
```

### `G01-C02` *(Rastreamento completo com salto de 2 em 2)*
Sem usar computador, rastreie `seq(6)`:
```c
int seq(int n) {
    if (n <= 1) {
        return 2;
    }
    return 3 + seq(n - 2);
}
```
Apresente todos os quadros da descida, o argumento que ativa o caso base e todos os valores retornados até o resultado final.

### `G01-C03` *(Identificação de caso base inalcançável / Stack Overflow)*
Analise a chamada `contar(5)` na função abaixo:
```c
int contar(int n) {
    if (n == 0) {
        return 0;
    }
    return 1 + contar(n - 2);
}
```
**(a)** Mostre a sequência de argumentos empilhados e explique por que ocorre *stack overflow*.  
**(b)** Qual ajuste na condição do caso base evita o problema mantendo o retorno `0` quando `n` chega ao fim da contagem?

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `G02` (`Ordem de Execução na Pilha: Pré-Recursão vs. Pós-Recursão`):** somente após autocorreção de `G01-E01..E05` e **100% (3/3)** na Checagem Independente `G01-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** redesenhar os quadros como fichas empilhadas (uma ficha por chamada com sua cópia própria de `n` e `k`, removendo a ficha do topo apenas quando ela executa `return`) e aplicar variante `V2` de `G01`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`F02`** (escopo local de parâmetros/variáveis) e **`F01`** (retorno de funções tipadas ao chamador).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (itens 9 e 10 — desvio de chamada, pilha de execução e recursão).
- `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 4–5 (13/11 e 16/11).
- `[DOC]` `Aula_21_Algoritmos.pdf` p. 3–20 (tripé recursivo, `somaAte`, `fat`, pilha de execução informal e *stack overflow*).
- `[DOC]` `Aula_22_Algoritmos.pdf` p. 3–14 (revisão visual da pilha de chamadas e retornos).
- Rubrica e gabarito verificável: [G01_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/gabaritos/G01_gabarito.md) e [G01_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/G01_testes.md).
