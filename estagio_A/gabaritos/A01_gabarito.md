# Gabarito Comentado — Bloco `A01` (Problemas Computacionais, Algoritmos e Abstração)

> **Bloco de referência:** [A01_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/blocos/A01_bloco.md)  
> **Nota para Caça ao Bug:** Os algoritmos em português estruturado de `A01-E03` e `A01-C02` no bloco do aluno contêm **falhas conceituais intencionais** detalhadas abaixo. Este bloco é 100% conceitual (zero código C).

---

## 1. Gabarito dos Exercícios (`A01-E01` a `A01-E06`)

### `A01-E01` *(Leitura e Análise)*
- **(a)** **Entrada:** temperatura `T` da água (em graus Celsius). **Saída:** classificação do estado físico (`"Solido"`, `"Liquido"` ou `"Gasoso"`).
- **(b)** No **mapa turístico de bolso**, preserva-se a localização simplificada das ruas principais, pontos turísticos e conexões de transporte; **abstraem-se** (omitem-se) tubulações subterrâneas, profundidade de encanamentos ou curvas topográficas precisas, pois não interessam ao turista. Cada contexto exige um nível de abstração distinto para o mesmo espaço físico.

### `A01-E02` *(Completar algoritmo)*
- **`(___ A ___)`:** `Leia o percentual de aumento (P).`
- **`(___ B ___)`:** `Calcule novo = S + aumento.`
- **`(___ C ___)`:** `Exiba o novo salario (novo).`

### `A01-E03` *(Caça ao Bug conceitual — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. **Violação de sequência (passo 1):** tenta exibir `soma` antes de ler `A` e `B` e antes de calcular `A + B`.
  2. **Instrução não elementar / ambígua (passo 2):** *"pense em um numero B adequado"* é vago e não define uma entrada objetiva a ser lida.
  3. **Violação de finitude (passo 4):** voltar incondicionalmente para o passo 1 cria repetição infinita quando `soma > 100`.
- **Versão corrigida completa (português estruturado):**
```text
1. Leia o numero positivo A.
2. Leia o numero positivo B.
3. Calcule soma = A + B.
4. Se soma > 100, exiba "Maior que 100".
5. Exiba o resultado da soma.
6. Encerre o algoritmo.
```
*(Aceita-se também exibir `soma` antes do passo 4, desde que ocorra após o passo 3 e sem salto infinito.)*

### `A01-E04` *(Ordenação de passos e cadeia de compilação)*
- **(a)** Ordem correta: **`Passo Z` → `Passo K` → `Passo Y` → `Passo X` → `Passo W`** (ou `Passo K` antes de `Passo Z`, desde que ambas as leituras precedam `Passo Y`):
```text
1. Leia a nota P1.
2. Leia a nota P2.
3. Calcule media = (P1 * 4 + P2 * 6) / 10.
4. Exiba media.
5. Encerre o algoritmo.
```
- **(b)** Ordem da cadeia: **`[Algoritmo]` → `[Código-Fonte em Alto Nível]` → `[Compilador]` → `[Programa Executável]`**.  
  **Papel do compilador:** é o programa tradutor que converte o código-fonte escrito em linguagem de alto nível para linguagem de máquina (gerando o programa executável).

### `A01-E05` *(Abstração e Linguagem de Máquina vs. Alto Nível)*
- **(a)**
  - **Nível do estudante:** relevante → título do livro e status (`disponivel`/`emprestado`); abstraído → código interno de tabela, formato de armazenamento na memória ou endereço de servidor.
  - **Nível do programador:** relevante → identificadores de usuário e livro, datas de empréstimo/devolução e regras de controle; abstraído → cor da capa do livro ou disposição física das cadeiras na sala de leitura.
- **(b)** Porque programar diretamente em linguagem de máquina (`0` e `1`, ou sinais físicos/tensão como no ENIAC) é lento, complexo e altamente propenso a erros humanos; linguagens de alto nível usam vocabulário próximo ao humano e abstraem detalhes de hardware, cabendo ao compilador traduzir para a máquina.

### `A01-E06` *(Resolução independente — Português estruturado)*
- **(a)** **Entradas:** distância percorrida (`distancia`, em km) e quantidade de combustível gasta (`litros`, em litros). **Saídas:** valor do consumo médio (`consumo = distancia / litros`) e indicação de desempenho (`"Economico"` ou `"Nao economico"`), ou mensagem de entrada inválida quando `litros <= 0`.
- **(b)** Algoritmo completo esperado:
```text
1. Leia a distancia percorrida em km (distancia).
2. Leia o volume de combustivel em litros (litros).
3. Se litros <= 0, exiba "Entrada invalida: litros deve ser positivo" e va para o passo 7.
4. Calcule consumo = distancia / litros.
5. Exiba consumo.
6. Se consumo >= 12.0, exiba "Economico"; senao, exiba "Nao economico".
7. Encerre o algoritmo.
```

---

## 2. Gabarito da Checagem Independente (`A01-C01` a `A01-C03`)

### `A01-C01` *(E/S, Abstração e Compilação)*
- **(a)** **Entradas:** valor base do ingresso (`V`) e condição do cliente (`estudante`: sim ou não). **Saída:** valor final a pagar pelo ingresso (`V * 0.5` ou `V`).
- **(b)** Exemplos válidos de informações abstraídas: cor da poltrona, título do filme, horário da sessão, nome do atendente (qualquer par de detalhes irrelevantes ao cálculo financeiro do ingresso).
- **(c)** O programador implementa o algoritmo escrevendo um código-fonte em uma **linguagem de alto nível** (mais legível aos humanos, abstraindo o hardware); em seguida, o **compilador** traduz esse código-fonte para instruções em **linguagem de máquina**, gerando um executável que o processador do computador consegue rodar diretamente.

### `A01-C02` *(Caça ao Bug conceitual — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. **Violação de sequência (passo 1):** calcula `perimetro` antes de ler `L` e `H`.
  2. **Instrução não elementar (passo 2):** *"Descubra mentalmente valores convenientes"* não é instrução computacional objetiva de leitura.
  3. **Violação de finitude (passo 3):** voltar continuamente ao passo 1 cria um laço infinito.
- **Versão corrigida completa (português estruturado):**
```text
1. Leia o lado L positivo do retangulo.
2. Leia o lado H positivo do retangulo.
3. Calcule perimetro = 2 * (L + H).
4. Exiba o valor de perimetro.
5. Encerre o algoritmo.
```

### `A01-C03` *(Algoritmo independente em passos finitos)*
```text
1. Leia a idade da pessoa em anos inteiros (idade).
2. Se idade < 12, exiba "Crianca".
3. Senao, se idade <= 17, exiba "Adolescente".
4. Senao, exiba "Adulto".
5. Encerre o algoritmo.
```
*(Critério de aceitação: deve testar as fronteiras `12` e `17`/`18` sem lacunas, garantir saída única e terminar em número finito de passos sem código C.)*
