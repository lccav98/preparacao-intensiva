# Gabarito Comentado — Bloco `A04` (Identificadores, Palavras Reservadas e Declaração de Variáveis)

> **Bloco de referência:** [A04_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/blocos/A04_bloco.md)  
> **Nota para Caça ao Bug:** O trecho em `A04-E03` no bloco do aluno contém **erros intencionais** detalhados abaixo. Este bloco foca validação e declaração sintática (sem arquivos `.c` executáveis em `solucoes/`).

---

## 1. Gabarito dos Exercícios (`A04-E01` a `A04-E06`)

### `A04-E01` *(Classificação de identificadores)*
1. `idadeAluno` → **Válido** (apenas letras, mnemônico).
2. `1semestre` → **Inválido** (inicia com o dígito numérico `1`).
3. `taxa_juros` → **Válido** (letras e sublinhado `_` são permitidos).
4. `while` → **Inválido** (é palavra reservada da linguagem C).
5. `saldo-atual` → **Inválido** (contém hífen `-`, que é caractere especial / operador, não sublinhado `_`).
6. `_indice` → **Válido** (iniciar com `_` seguido de letras é permitido em C).

### `A04-E02` *(Completar declarações)*
- **`/* A */`:** `int`
- **`/* B */`:** `char`
- **`/* C */`:** `double`
- **`/* D */`:** `float`

### `A04-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `int 3notas;` → identificador inválido porque começa com o dígito `3`.
  2. `double preco produto;` → identificador inválido porque contém espaço em branco.
  3. `char int;` → inválido porque `int` é uma palavra reservada de C.
  4. `float taxa%;` → identificador inválido porque contém o caractere especial `%`.
  5. `int valorTotal; double valorTotal;` → redeclaração do mesmo identificador (`valorTotal`) dentro do mesmo escopo, proibida em C.
- **Versão corrigida (exemplo válido com nomes mnemônicos):**
```c
int notas3;
double precoProduto;
char inicial;
float taxaPercentual;
int quantidadeTotal;
double valorTotal;
```
*(Aceitam-se outros identificadores válidos equivalentes, como `qtdNotas`, `preco_produto`, `letra`, `taxa`.)*

### `A04-E04` *(Palavras reservadas, acentos e case-sensitivity)*
- **(a)** As 3 palavras reservadas são: **`char`**, **`sizeof`** e **`return`**. *(Todas em minúsculas.)*
- **(b)** **`média`** é inválido porque contém o caractere acentuado `é` (identificadores padrão em C usam apenas letras ASCII sem acentuação).
- **(c)** Porque C é uma linguagem *case-sensitive* (diferencia maiúsculas de minúsculas), logo `media_1` e `Media_1` referem-se a endereços/variáveis completamente distintos.

### `A04-E05` *(Escolha de tipos e estado na memória)*
- **(a)** Exemplo de declarações corretas:
```c
int codigoExemplar;
double pesoKg;
char letraEstante;
```
- **(b)** O conteúdo é **indeterminado** ("lixo" de memória), pois a declaração apenas reserva o espaço para um `int` sem gravar um valor inicial.

### `A04-E06` *(Resolução independente — Programa completo de declarações)*
```c
/* Exercicio A04-E06: Declaracao de variaveis para corrida de rua */
#include <stdio.h>

int main(void) {
    // Conteudo inicial indeterminado ("lixo de memoria") ate receber atribuicao ou leitura
    int numeroInscricao, numeroLote;
    int _prioridade;
    char categoria;
    double tempoSegundos;
    float distanciaKm;
    return 0;
}
```
*(Os nomes exatos dos identificadores podem variar, desde que respeitem as regras de formação do C, sejam mnemônicos, não usem palavras reservadas, empreguem exatamente `int`, `char`, `double` e `float`, e não contenham `=` nem `printf`/`scanf`.)*

---

## 2. Gabarito da Checagem Independente (`A04-C01` a `A04-C04`)

### `A04-C01` *(Classificação de identificadores)*
- `nota2` → **Válido** (dígito após letra é permitido).
- `2nota` → **Inválido** (começa com o dígito `2`).
- `valor_final` → **Válido** (letras e `_`).
- `valor final` → **Inválido** (contém espaço em branco).
- `custo$` → **Inválido** (contém símbolo especial `$`).
- `_total` → **Válido** (sublinhado `_` e letras).

### `A04-C02` *(Palavra reservada e case-sensitivity)*
- **(a)** Palavras reservadas da lista: **`void`**, **`switch`** e **`for`**.
- **(b)** Como C é *case-sensitive*, `Void` (com `V` maiúsculo) é diferente de `void`, portanto o compilador não a reconhece como palavra reservada (embora seja má prática usá-la como variável). Já `caso` é um identificador válido em português porque a palavra reservada da linguagem C é `case` (em inglês).

### `A04-C03` *(Escolha de tipo para 3 dados reais)*
1. **Quantidade de passageiros:** **`int`** — número inteiro sem parte fracionária.
2. **Coeficiente térmico de alta precisão:** **`double`** — número real que exige precisão dupla (superior ao `float`).
3. **Código de turno (`'M'`, `'T'`, `'N'`):** **`char`** — armazena exatamente um único caractere.

### `A04-C04` *(Escrita de declarações válidas)*
```c
int anoFabricacao;
char inicialBloco;
float larguraMetros;
double saldoBancario;
```
*(Aceitam-se outros identificadores válidos e mnemônicos nos tipos `int`, `char`, `float` e `double`, obrigatoriamente finalizados com `;` e sem atribuição `=`.)*
