# Bloco `A01` — Problemas Computacionais, Algoritmos e Abstração

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio A — Fundamentos de Algoritmos, Ambiente C, Variáveis e Representação de Dados / **`A01`** |
| **Micro-habilidade foco** | Decompor um enunciado em entradas, processamento passo a passo finito e saídas, distinguindo problema computacional, abstração, algoritmo e programa. |
| **Pré-requisitos** | `—` *(Nenhum pré-requisito de programação)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`A01-E01`–`A01-E06`, 20 min):** `12 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`A01-C01`–`A01-C03`, 12 min):** `8 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **100% conceitual e no papel (português estruturado). Zero código C:** não utilize `#include`, `main`, `printf`, `scanf`, tipos de dados ou sintaxe de linguagem de programação neste bloco. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`A01-E01`–`A01-E06`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 6` | **Após autocorreção:** `___ / 6`
- **Checagem independente (sem gabarito) (`A01-C01`–`A01-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Problema computacional:** é um enunciado geral que relaciona uma condição inicial (**entrada**) à resposta esperada (**saída**).
2. **Algoritmo:** é uma sequência **finita**, **ordenada** e composta por **instruções elementares** (claras e executáveis sem ambiguidade) para resolver um problema, independente de computador ou linguagem.
3. **Três propriedades obrigatórias de um algoritmo:**
   - **Sequência:** a ordem dos passos altera o resultado (ex.: não se pode calcular antes de ler a entrada).
   - **Finitude:** deve terminar após um número limitado de passos (processos infinitos não resolvem problemas computacionais).
   - **Instruções elementares:** cada passo deve descrever uma ação objetiva e executável (nunca instruções vagas como *"descubra o valor ideal"*).
4. **Abstração em níveis:** técnica para remover detalhes irrelevantes e manter apenas o que importa ao contexto (como o mapa do metrô simplificado para o passageiro vs. o mapa georreferenciado detalhado para o engenheiro).
5. **Do algoritmo ao computador:**
   - **Linguagem de programação de alto nível:** aproxima-se do vocabulário humano e abstrai a complexidade física do processador.
   - **Programa (código-fonte):** é a implementação do algoritmo em uma linguagem de programação (ex.: C).
   - **Linguagem de máquina:** instruções numéricas (`0` e `1`) executadas diretamente pelo processador.
   - **Compilador:** programa tradutor que converte o **código-fonte** de alto nível em um **programa executável** (em linguagem de máquina).

---

## 2. Exemplos Guiados

### Exemplo 1 — Decomposição Entrada/Saída e Abstração *(Trecho ilustrativo — decomposição parcial em português estruturado, sem código C)*
Problema: calcular o troco ao pagar uma compra em dinheiro.
- **Entradas:** valor pago (`VP`) e preço do produto (`PP`).
- **Saída:** valor do troco (`VP - PP`).
- **Abstração no caixa:** interessam apenas `VP`, `PP` e a operação de subtração; abstraem-se detalhes irrelevantes como a cor do produto, o nome da loja ou o número de série da cédula.

### Exemplo 2 — Fluxo finito completo em português estruturado *(Algoritmo completo em português estruturado, sem código C)*
Problema: receber a média semestral (`MS`) de um estudante e informar se obteve aprovação direta (critério `MS >= 6.0`).

```text
1. Leia a media semestral (MS).
2. Se MS >= 6.0, exiba "Aprovado".
3. Senao, exiba "Em reavaliacao".
4. Encerre o algoritmo.
```
**Por que está correto?**
- **Sequência:** lê `MS` antes de comparar no passo 2.
- **Instruções elementares:** leitura, comparação objetiva (`>= 6.0`), exibição e encerramento.
- **Finitude:** executa no máximo 4 passos e sempre termina no passo 4.

---

## 3. Exercícios (`A01-E01` a `A01-E06`)

### `A01-E01` *(Leitura e Análise — Reprodução do modelo)*
Analise o problema e o algoritmo em português estruturado abaixo, destinado a classificar a água ao nível do mar segundo sua temperatura `T` (em graus Celsius):

```text
1. Leia a temperatura T em graus Celsius.
2. Se T <= 0, exiba "Solido".
3. Senao, se T < 100, exiba "Liquido".
4. Senao, exiba "Gasoso".
5. Encerre o algoritmo.
```
**(a)** Identifique exatamente qual é a **entrada** e quais são as possíveis **saídas** do problema.  
**(b)** Considere agora dois contextos de mapa de uma cidade: um **mapa turístico de bolso** e uma **planta hidráulica da rede de esgoto**. Cite **1 detalhe preservado** e **1 detalhe abstraído (omitido)** no mapa turístico e explique em 1 frase por que ambos representam o mesmo espaço físico em níveis diferentes de abstração.

---

### `A01-E02` *(Completar algoritmo em português estruturado)*
Um problema pede para ler o salário atual de um trabalhador (`S`) e o percentual de reajuste (`P`), calcular e exibir o novo salário (`novo`). Complete as 3 lacunas `(___ A ___)`, `(___ B ___)` e `(___ C ___)` respeitando sequência lógica e instruções elementares:

```text
1. Leia o salario atual (S).
2. (___ A ___)
3. Calcule aumento = S * (P / 100).
4. (___ B ___)
5. (___ C ___)
6. Encerre o algoritmo.
```

---

### `A01-E03` *(Caça ao Bug conceitual — Algoritmo defeituoso)*
Um estudante escreveu o algoritmo abaixo para ler dois números positivos `A` e `B`, somá-los e avisar apenas uma vez se a soma supera `100`. Identifique **3 falhas conceituais** (violação de **sequência**, **instrução não elementar** e **violação de finitude**) e reescreva a **versão corrigida completa** em português estruturado:

```text
1. Exiba o resultado da soma.
2. Leia o primeiro numero A e pense em um numero B adequado.
3. Calcule soma = A + B.
4. Se soma > 100, exiba "Maior que 100" e volte ao passo 1 para repetir para sempre.
5. Encerre o algoritmo.
```

---

### `A01-E04` *(Variação controlada com pistas — Ordenação de passos e fluxo de compilação)*
**(a)** Reordene os 5 passos embaralhados abaixo para formar um algoritmo válido que calcule a média ponderada de duas provas (`P1` com peso `4` e `P2` com peso `6`):
- `[Passo X]` Exiba `media`.
- `[Passo Y]` Calcule `media = (P1 * 4 + P2 * 6) / 10`.
- `[Passo Z]` Leia a nota `P1`.
- `[Passo W]` Encerre o algoritmo.
- `[Passo K]` Leia a nota `P2`.

**(b)** Ordene a cadeia de transformação abaixo da concepção lógica até a execução no processador e explique em 1 frase o papel do **compilador**:
`[Programa Executável]` · `[Algoritmo]` · `[Compilador]` · `[Código-Fonte em Alto Nível]`

*Pistas:* O cálculo de `media` só pode ocorrer após todas as leituras de entrada; o compilador não cria o algoritmo — ele traduz texto legível para instruções de máquina.

---

### `A01-E05` *(Variação controlada com pistas — Abstração e Linguagem de Máquina vs. Alto Nível)*
Considere o sistema de empréstimo de livros da biblioteca da universidade:
**(a)** Compare dois níveis de abstração indicando **1 dado relevante** e **1 detalhe abstraído** em cada nível: (1) visão do **estudante** consultando se um livro está disponível; (2) visão do **programador** que modela os registros do sistema.  
**(b)** Por que os programadores escrevem programas em linguagens de **alto nível** em vez de programar diretamente em **linguagem de máquina** (`0` e `1`), considerando o desafio histórico enfrentado no ENIAC?

*Pistas:* Pense em legibilidade, propensão a erros humanos e dependência de detalhes físicos do hardware.

---

### `A01-E06` *(Resolução independente — Português estruturado)*
Considere o problema de calcular o consumo médio de combustível (em km/l) de uma viagem e informar se o percurso foi econômico (consumo `>= 12.0` km/l). Sem escrever qualquer código em C:
**(a)** Liste exatamente quais são as **entradas** e as **saídas** do problema.  
**(b)** Escreva, em **português estruturado** (passos numerados), um algoritmo **finito**, na **sequência correta** e com **instruções elementares** que resolva o problema, incluindo proteção para o caso de a quantidade de litros informada ser menor ou igual a zero (`litros <= 0`).

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `A01-C01` *(Análise de E/S, Abstração e Compilação)*
Considere o problema de calcular o valor final de um ingresso de cinema dado seu preço inteiro `V` e a informação se o cliente é estudante (caso seja estudante, paga `50%` de `V`; caso contrário, paga `V`):
**(a)** Identifique as **entradas** e a **saída** do problema.  
**(b)** Cite **2 informações do mundo real abstraídas** nesse modelo por serem irrelevantes ao cálculo do valor.  
**(c)** Relacione os termos **linguagem de alto nível**, **compilador** e **linguagem de máquina** em 1 parágrafo curto explicando como um algoritmo escrito pelo programador chega a ser executado pelo computador.

### `A01-C02` *(Caça ao Bug conceitual — Algoritmo não finito e fora de ordem)*
O algoritmo abaixo foi proposto para calcular o perímetro de um retângulo de lados positivos `L` e `H`, mas contém **3 falhas conceituais** (sequência, instrução não elementar e finitude). Liste as 3 falhas e escreva a versão corrigida completa em português estruturado:

```text
1. Calcule perimetro = 2 * (L + H).
2. Descubra mentalmente valores convenientes para L e H.
3. Exiba perimetro e volte ao passo 1 continuamente.
```

### `A01-C03` *(Algoritmo independente em passos finitos)*
Escreva, em **português estruturado** (passos numerados, sem código C), um algoritmo completo e finito que leia a **idade** inteira de uma pessoa e apresente exatamente uma classificação:
- menor que `12` anos → `"Crianca"`
- de `12` a `17` anos → `"Adolescente"`
- `18` anos ou mais → `"Adulto"`

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `A02` (`Anatomia de um Programa em C e Compilação no GCC/Linux`):** somente após autocorreção da bateria `A01-E01..E06` **e** **100% (3/3)** na Checagem Independente `A01-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** identificar qual propriedade falhou (E/S, sequência, finitude, instrução elementar, abstração ou papel do compilador), revisar o Exemplo 1 ou 2 no papel e aplicar a variante `V2` de `A01`.
- **Após 2 tentativas malsucedidas:** parar a repetição mecânica do bloco; como `A01` não possui pré-requisitos de programação (`—`), o orientador deve conduzir leitura guiada em voz alta de 2 problemas cotidianos simples (como parada de ônibus e troco da `Aula_01`) para consolidar a identificação de entradas, passos ordenados e condição de término antes de nova tentativa.

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 1 — Introdução a algoritmos e resolução de problemas: problema, abstração, algoritmo, linguagem de programação e programa).
- `[DOC]` `Aula_01_Algoritmos.pdf` p. 2–12, 21–32 (exemplos cotidianos, sequência, finitude, instruções elementares, problema computacional, ENIAC, abstração em níveis, linguagem de máquina vs. alto nível, compilador e executável).
- `[DOC]` `Lista8_Algoritmos_Revisao.pdf` p. 1 (Ex. 1a–b — identificação de entradas/saídas e descrição de algoritmo em linguagem natural).
- Gabarito comentado e rubrica de verificação: [A01_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/gabaritos/A01_gabarito.md) e [A01_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/A01_testes.md).
