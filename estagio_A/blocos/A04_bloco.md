# Bloco `A04` — Identificadores, Palavras Reservadas e Declaração de Variáveis

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio A — Fundamentos de Algoritmos, Ambiente C, Variáveis e Representação de Dados / **`A04`** |
| **Micro-habilidade foco** | Validar identificadores segundo as regras da linguagem C e declarar variáveis com os tipos primitivos básicos (`char`, `int`, `float`, `double`). |
| **Pré-requisitos** | `A02` *(Anatomia mínima de programa em C e compilação no GCC/Linux)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`A04-E01`–`A04-E06`, 18 min):** `10 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`A04-C01`–`A04-C04`, 12 min):** `8 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** regras de formação de identificadores, palavras reservadas, *case-sensitivity* e declarações de `char`, `int`, `float`, `double` (além de `void` como conceito de função). **Proibido:** uso de variáveis em `printf` ou `scanf`, especificadores (`%d`, `%f`, `%c`), inicialização/atribuição com `=`, `#define`, `const` e operadores. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`A04-E01`–`A04-E06`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 6` | **Após autocorreção:** `___ / 6`
- **Checagem independente (sem gabarito) (`A04-C01`–`A04-C04`):** `___ / 4` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Conceito de variável:** é uma região nomeada da memória para guardar um dado. Em C, toda variável precisa ser **declarada antes de ser usada** e nasce com **conteúdo inicialmente indeterminado** (até receber um valor em blocos futuros).
2. **Regras obrigatórias para identificadores em C:**
   - Pode usar apenas letras (`a`–`z`, `A`–`Z`), dígitos (`0`–`9`) e sublinhado (`_`).
   - **Nunca** pode começar com dígito (`0`–`9`).
   - **Nunca** pode conter espaços, acentos, cedilha (`ç`) ou símbolos especiais (`&`, `$`, `-`, `%`, `@`, `.`).
   - **Nunca** pode coincidir com uma **palavra reservada** da linguagem C.
   - Use **nomes mnemônicos** (que indicam o significado do dado, como `idade`, `mediaFinal`).
3. **Palavras reservadas e *case-sensitivity*:** palavras como `char`, `int`, `float`, `double`, `void`, `return`, `const`, `if`, `else`, `switch`, `case`, `for`, `while`, `do`, `break` e `sizeof` têm significado fixo em C (todas em minúsculas). Como C diferencia maiúsculas de minúsculas, `Int` não é palavra reservada (mas deve ser evitada por clareza).
4. **Sintaxe de declaração:** `<tipo> <identificador>;` (ou múltiplos nomes do mesmo tipo separados por vírgula: `int dia, mes, ano;`).
5. **Os 5 tipos primitivos básicos:**
   - `char`: armazena um único caractere (ex.: `'A'`, `'7'`).
   - `int`: armazena número inteiro (ex.: `42`, `-10`, `0`).
   - `float`: armazena número real de precisão simples.
   - `double`: armazena número real de precisão dupla (preferido quando se exige maior exatidão).
   - `void`: vazio / sem tipo (usado em funções, não para declarar variáveis comuns).

---

## 2. Exemplos Guiados

### Exemplo 1 — Validação de identificadores e palavras reservadas *(Trecho ilustrativo)*
Analise os identificadores propostos abaixo:
- `mediaFinal` → **Válido** (usa apenas letras, mnemônico).
- `conta_2` → **Válido** (usa letras, `_` e dígito, sem iniciar com dígito).
- `2conta` → **Inválido** (inicia com o dígito `2`).
- `valor&total` → **Inválido** (contém o caractere especial `&`).
- `nome aluno` → **Inválido** (contém espaço em branco).
- `double` → **Inválido** (é palavra reservada de C).
- `Return` vs. `return`: `return` é palavra reservada (proibida); `Return` é tecnicamente aceita porque C é *case-sensitive*, mas deve ser evitada para não confundir quem lê.

### Exemplo 2 — Declaração de variáveis no escopo do programa *(Programa completo)*

```c
/* Exemplo de declaracao de variaveis sem inicializar valores */
#include <stdio.h>

int main(void) {
    int quantidadeItens;
    double precoUnitario;
    float descontoEstimado;
    char categoria;
    return 0;
}
```
**O que acontece na memória?** Cada linha reserva espaço para o tipo escolhido (`int`, `double`, `float`, `char`) terminado com `;`. Como ainda não foi feita inicialização nem entrada de dados (`A05` e `A06`), o conteúdo dentro de cada variável permanece indeterminado.

---

## 3. Exercícios (`A04-E01` a `A04-E06`)

### `A04-E01` *(Leitura e Classificação — Reprodução do modelo)*
Classifique cada um dos 6 identificadores abaixo como **Válido** ou **Inválido**, justificando brevemente o motivo sempre que for inválido:
1. `idadeAluno`
2. `1semestre`
3. `taxa_juros`
4. `while`
5. `saldo-atual`
6. `_indice`

---

### `A04-E02` *(Completar declarações)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` no trecho ilustrativo abaixo escolhendo apenas o **tipo primitivo** adequado (`char`, `int`, `float` ou `double`):

```c
/* A */ numeroVagas;      // quantidade inteira de vagas em uma sala
/* B */ conceito;         // letra unica da avaliacao ('A', 'B', 'C')
/* C */ massaAmostra;     // medida real em laboratorio exigindo dupla precisao
/* D */ temperatura;      // medida real em precisao simples
```

---

### `A04-E03` *(Caça ao Bug em declarações — Trecho ilustrativo)*
O trecho ilustrativo abaixo contém **4 erros de declaração** (entre regras de formação de identificadores e palavras reservadas). Liste os **4 erros** e reescreva as 4 declarações corrigidas com nomes válidos e mnemônicos:

```c
int 3notas;
double preco produto;
char int;
float taxa%;
```

---

### `A04-E04` *(Variação controlada com pistas — Palavras reservadas, acentos e case-sensitivity)*
Considere os 8 nomes listados a seguir:
`char` · `Char` · `sizeof` · `media_1` · `Media_1` · `média` · `return` · `Return`

**(a)** Quais **3** nomes da lista são **palavras reservadas** de C (proibidos como identificadores)?  
**(b)** Qual nome é **inválido** por conter caractere acentuado?  
**(c)** Por que `media_1` e `Media_1`, se declaradas juntas, representam **duas variáveis distintas** para o compilador?

*Pistas:* Todas as palavras reservadas em C são escritas em letras minúsculas; identificadores válidos utilizam apenas letras ASCII sem acento.

---

### `A04-E05` *(Variação controlada com pistas — Escolha de tipos e estado na memória)*
Um sistema de biblioteca precisa armazenar três informações sobre cada livro:
1. código numérico inteiro do exemplar;
2. peso do exemplar em quilogramas (com dupla precisão);
3. letra da estante (`'A'`, `'B'`, `'C'`).

**(a)** Escreva as **3 declarações em C** usando identificadores mnemônicos válidos (sem atribuir valores).  
**(b)** Logo após executar `int codigoExemplar;` (antes de qualquer leitura ou atribuição), qual é o conteúdo dessa variável na memória?

*Pistas:* Use um tipo por linha terminado em `;`; lembre do modelo de memória em 3 etapas antes da atribuição.

---

### `A04-E06` *(Resolução independente)*
Escreva um **programa completo** mínimo em C (`#include <stdio.h>`, `int main(void)`, `return 0;`) que apenas **declare** (sem inicializar, sem `printf` e sem `scanf`) 4 variáveis para registrar dados de uma corrida de rua:
- número de inscrição do atleta (inteiro);
- categoria representada por uma única letra;
- tempo oficial em segundos com dupla precisão;
- distância percorrida em km com precisão simples.

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `A04-C01` *(Classificação de identificadores)*
Classifique cada identificador abaixo em **Válido** ou **Inválido**, justificando os inválidos:
`nota2` · `2nota` · `valor_final` · `valor final` · `custo$` · `_total`

### `A04-C02` *(Palavra reservada e case-sensitivity)*
Analise os 6 nomes abaixo:
`void` · `Void` · `switch` · `for` · `For` · `caso`

**(a)** Quais são **palavras reservadas** da linguagem C (logo proibidas como variáveis)?  
**(b)** Explique por que o compilador trata `Void` diferentemente de `void`, e por que `caso` é válido enquanto `case` seria proibido.

### `A04-C03` *(Escolha de tipo para 3 dados reais)*
Indique o tipo primitivo mais adequado em C (`char`, `int`, `float`, `double`, `void`) para representar cada um dos 3 dados reais abaixo, justificando em 1 linha cada escolha:
1. Quantidade de passageiros embarcados em um ônibus;
2. Coeficiente físico de dilatação térmica que exige alta precisão decimal;
3. Código de turno de trabalho representado por um único caractere (`'M'`, `'T'` ou `'N'`).

### `A04-C04` *(Escrita de declarações válidas)*
Escreva **4 declarações válidas e independentes** em C (com `;` e nomes mnemônicos distintos, sem atribuir valores) para armazenar:
1. ano de fabricação de um veículo (inteiro);
2. letra inicial do bloco de salas (caractere único);
3. largura de uma peça em metros (precisão simples);
4. saldo bancário em reais (dupla precisão).

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `A05` (`Saída de Variáveis, Casas Decimais e Constantes`):** somente após autocorreção de `A04-E01..E06` **e** **100% (4/4)** na Checagem Independente `A04-C01..C04` sem consulta ao gabarito *(exige também domínio prévio de `A03`)*.
- **Recuperação direcionada (1ª falha):** revisar as 4 regras de formação de identificadores (dígito inicial, espaços/acentos, símbolos especiais, palavras reservadas) ou a tabela dos 5 tipos primitivos (`char`, `int`, `float`, `double`, `void`) e aplicar a variante `V2` de `A04`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar o pré-requisito **`A02`** (em especial pontuação `;`, *case-sensitivity* e estrutura mínima `int main(void)`) antes de retomar `A04`.

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 2 — Variáveis e constantes; tipos primitivos; identificador: regras de formação e palavras reservadas; conteúdo e sintaxe de declaração).
- `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 1 (28/08 — regras de formação de identificadores e palavras reservadas; tipos de dados e sintaxe de declaração).
- `[DOC]` `Aula_02_Algoritmos.pdf` p. 8–9, 16–18 (palavras reservadas, *case-sensitive*, regras de nomeação de identificadores, conceito e declaração de variáveis e os 5 tipos primitivos em C).
- Gabarito comentado e rubrica de verificação: [A04_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/gabaritos/A04_gabarito.md) e [A04_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/A04_testes.md).
