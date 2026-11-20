# Gabarito Comentado — Bloco `F09` (Pré-Processamento, Etapas e Compilação vs. Interpretação)

> **Bloco de referência:** [F09_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_F/blocos/F09_bloco.md)

---

## 1. Gabarito dos Exercícios (`F09-E01` a `F09-E05`)

### `F09-E01` *(Rastreamento de expansão textual)*
**Código após o pré-processamento:**
```c
int dobrar(int x);

int main(void) {
    int r = dobrar(50);
    return r;
}
```
**Explicação:**
- Na 1ª linha `#include "calc.h"`, `CALC_H` não está definido; o pré-processador define `CALC_H`, substitui/registra `LIMITE -> 50` e cola o protótipo `int dobrar(int x);`.
- Na 2ª linha `#include "calc.h"`, `CALC_H` já está definido, logo `#ifndef CALC_H` falha e todo o conteúdo interno é ignorado (não há duplicação).
- A macro `LIMITE` é substituída textualmente por `50`, e o comentário `/* leitura omitida */` é removido antes de o texto seguir para o compilador.

### `F09-E02` *(Completar lacunas)*
- **`/* A */`:** `Pré-processamento`
- **`/* B */`:** `Compilação`
- **`/* C */`:** `Ligação` (ou *Linking*)
- **`/* D */`:** `-c`

### `F09-E03` *(Caça ao Erro Conceitual)*
1. **Erro:** O pré-processador apenas manipula texto (`#include`, `#define`, `#ifndef`), não conhece a gramática nem os tipos de C. **Correção:** A verificação de tipos e protótipos ocorre na etapa de **compilação**.
2. **Erro:** Como `#define` faz substituição textual literal, `2 * PI * r` vira `2 * 3.14; * r`, causando erro de sintaxe por causa do `;` no meio da expressão. **Correção:** `#define` não deve terminar com `;` (`#define PI 3.14`).
3. **Erro:** Com `gcc -c`, cada `.c` é compilado **separadamente** para gerar seu `.o`; basta o protótipo presente em `mod.h` para o compilador aceitar a chamada e deixá-la pendente para o ligador. **Correção:** A resolução do endereço real da função de `mod.c` acontece apenas depois, na etapa de **ligação**.

### `F09-E04` *(Compilação vs. Interpretação)*
- **(a)** O executável C contém instruções nativas específicas para o conjunto de instruções da CPU (x86-64) e chamadas do sistema operacional (Linux). Já o `.py` (código-fonte) ou o `.class` (bytecode neutro) dependem de um interpretador Python ou JVM instalada na máquina destino, que traduz em tempo de execução para o hardware local.
- **(b)** Porque em C o código já foi inteiramente traduzido previamente para instruções diretas de máquina, sem o custo de leitura, interpretação ou despacho dinâmico durante a execução do programa.

### `F09-E05` *(Cenário completo)*
- **(a)** **Gera `main.o` com sucesso** (desde que `main.c` inclua `"math_ops.h"` e respeite a sintaxe/tipos C), pois `gcc -c` apenas compila `main.c` para código-objeto sem realizar a ligação.
- **(b)** Falha a etapa de **ligação** (*linking*), emitindo erro **`undefined reference to '...'`** para as funções de `math_ops.c`.
- **(c)** Em **C**, o compilador analisa o arquivo inteiro antes de gerar o executável e rejeita o programa imediatamente por identificador não declarado (`'nao_existe' undeclared`), mesmo dentro de `if (0)`. Em **Python**, como a verificação de nomes ocorre em tempo de execução e a condição `0` é falsa, a linha nunca é executada e o script roda sem acusar o `NameError`.

---

## 2. Gabarito da Checagem Independente (`F09-C01` a `F09-C04`)

### `F09-C01` *(3 etapas de construção)*
1. **Pré-processamento:** processa diretivas `#` (`#include`, `#define`, `#ifndef`) e remove comentários, produzindo código-fonte C puro expandido.
2. **Compilação:** analisa sintaxe/tipos de cada `.c` e traduz para linguagem de máquina em arquivo-objeto (`.o`), mantendo referências externas em aberto.
3. **Ligação (*Linking*):** une todos os `.o` do projeto e bibliotecas padrão, resolvendo chamadas entre módulos e gerando o executável final.

### `F09-C02` *(Pré-processamento e `#ifndef`)*
- `#include "arq.h"` copia literalmente o texto de `arq.h` para dentro do arquivo naquele ponto.
- `#define MAX 100` instrui substituição textual de toda ocorrência do token `MAX` por `100`.
- Sem `#ifndef`, se um mesmo `.h` for incluído direta e indiretamente mais de uma vez na mesma unidade de compilação, constantes `#define` ou declarações repetidas podem ser coladas múltiplas vezes e causar erros/avisos de redefinição.

### `F09-C03` *(Compilação vs. Interpretação)*
1. **Momento da tradução:** C traduz o programa inteiro antes da execução; Python interpreta/executa dinamicamente no momento em que o programa roda.
2. **Requisito no usuário final:** o executável C roda diretamente no sistema operacional alvo sem precisar do compilador; o script Python exige o interpretador Python instalado.
3. **Detecção de erros:** C detecta erros de sintaxe e de tipo antes de executar (na compilação); Python pode executar trechos válidos e só acusar erros de nome/tipo se o fluxo passar pela linha defeituosa (erros de sintaxe, porém, são detectados ao carregar o script).

### `F09-C04` *(Portabilidade e compilação separada)*
1. O executável C é preso à arquitetura de CPU e ao sistema operacional para o qual foi compilado (alta velocidade nativa, baixa portabilidade binária). O `.class` Java contém *bytecode* independente de hardware, rodando em qualquer plataforma que possua uma JVM compatível.
2. Na compilação separada (`gcc -c a.c`), o compilador só precisa conferir a assinatura das funções externas — e isso já está no protótipo dentro de `b.h` — gerando `a.o`. Para construir o executável final, porém, o ligador precisa juntar as implementações reais presentes em `a.o` e `b.o`.
