# Especificação e Rubrica de Verificação — Bloco `A01`

- **Natureza do bloco:** **100% conceitual e em papel** (português estruturado). Não possui código C, não possui arquivos `.c` em `solucoes/`, não possui arquivo `casos_A01.json` e não exige compilação em GCC.
- **Critério de validação estática:** ausência integral de sintaxe C (`#include`, `main`, `printf`, `scanf`, operadores de C) nos enunciados e gabaritos, e alinhamento integral com [A01_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/blocos/A01_bloco.md) e [A01_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/gabaritos/A01_gabarito.md).
- **Status de execução:**
  - **Executado:** auditoria estrutural e verificação da rubrica objetiva de todos os 9 itens (`A01-E01`–`A01-E06`, `A01-C01`–`A01-C03`).
  - **Compilação binária GCC:** não aplicável a `A01` (zero código C); note-se também que `gcc` está ausente no ambiente local para os demais blocos.

---

## Rubrica Objetiva de Correção (`A01-E01` a `A01-E06` e `A01-C01` a `A01-C03`)

| Item | Critérios Obrigatórios para Acerto Integral (`1/1`) | Erro Típico que Reprova o Item |
|---|---|---|
| **`A01-E01`** | **(a)** Identifica `T` como entrada e os 3 estados (`Solido`, `Liquido`, `Gasoso`) como saídas; **(b)** cita 1 detalhe mantido e 1 omitido no mapa turístico explicando o papel do contexto. | Confundir `0` ou `100` (constantes da regra) com entradas fornecidas pelo usuário. |
| **`A01-E02`** | Preenche leitura de `P` antes do passo 3, cálculo de `novo = S + aumento` no passo 4 e exibição de `novo` no passo 5. | Exibir `aumento` no lugar de `novo` ou ler `P` após o cálculo. |
| **`A01-E03`** | Identifica as **3 falhas** (sequência no passo 1, instrução vaga no passo 2, ciclo infinito no passo 4) e reescreve o algoritmo na ordem `ler → somar → comparar/exibir → encerrar`. | Apontar apenas o ciclo infinito ignorando a leitura vaga ou a inversão do passo 1. |
| **`A01-E04`** | **(a)** Ambas as leituras (`P1`, `P2`) precedem `media`, seguida de exibição e fim; **(b)** cadeia `Algoritmo → Código-fonte → Compilador → Executável` com definição correta do compilador. | Colocar `Compilador` antes de `Código-Fonte` ou calcular `media` antes de ler `P2`. |
| **`A01-E05`** | **(a)** Distingue corretamente dado relevante vs. abstraído para usuário e programador; **(b)** explica legibilidade, redução de erros e tradução via compilador vs. linguagem de máquina. | Responder apenas que "alto nível é mais rápido para o computador". |
| **`A01-E06`** | **(a)** Lista `distancia` e `litros` como entradas e consumo/classificação como saídas; **(b)** inclui guarda `litros <= 0` antes da divisão, compara `>= 12.0` e encerra de forma finita. | Dividir `distancia / litros` sem verificar `litros <= 0` ou usar sintaxe C. |
| **`A01-C01`** | **(a)** Identifica `V` e condição de estudante como entradas e preço final como saída; **(b)** cita 2 abstrações válidas; **(c)** explica corretamente alto nível → compilador → linguagem de máquina. | Omitir a entrada booleana ("é estudante?") e listar apenas `V`. |
| **`A01-C02`** | Lista as **3 falhas** (cálculo antes da leitura, "descubra mentalmente" não elementar, retorno contínuo sem fim) e corrige em sequência finita. | Manter a instrução vaga no passo 2 ou deixar salto infinito. |
| **`A01-C03`** | Lê `idade`, cobre sem lacunas `< 12`, `12..17` e `>= 18` com saída única (`Crianca`, `Adolescente`, `Adulto`) e termina em passo finito sem código C. | Deixar a idade `12` ou `18` sem cobertura (ex.: `< 12` seguido de `> 12 e < 18`) ou imprimir duas classificações para `10`. |
