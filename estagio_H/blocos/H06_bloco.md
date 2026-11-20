# Bloco `H06` — Verificação Sistemática, Teste de Mesa Integrado e Preparação para Arguição/Reavaliação *(Inclui Desafios Opcionais)*

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio H — Integração Geral e Projeto Modularizado (PGM) / **`H06`** |
| **Micro-habilidade foco** | *(Integração e Síntese Final)* Validar o sistema de 5 arquivos contra casos de borda calculados à mão, executar pequenas modificações sob restrições (simulando arguição oral ao vivo) e revisar integralmente os Estágios A–H para avaliação global. |
| **Pré-requisitos** | `H05` *(Menu interativo `do-while` + `switch` e validação de entradas)*, `G09` *(Consolidação de recursividade e pilha de execução)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 24 min):** `15 min` resol. \| `5 min` corr. \| `4 min` recup.; **Sessão 2 (`E04`–`E06`, 24 min):** `15 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. *(Desafios `[OPCIONAIS]` fora do tempo obrigatório.)* |
| **Restrição de escopo** | **Conteúdo novo: NENHUM.** Núcleo obrigatório em 5 arquivos (`main.c`, `imagem.h`, `imagem.c`, `funcoes.h`, `funcoes.c`); funções recursivas em `E02`, `C01` e `OP1` proibidas de usar laços no eixo recursivo. **Não utilize** `struct`, alocação dinâmica (`malloc`/`free`), VLAs, aritmética de ponteiros ou `gets(`. Saídas estritamente em ASCII puro. Desafios `[OPCIONAIS]` **não bloqueiam** a conclusão. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente Obrigatória (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%) — Curso Concluido  [ ] Recuperacao`)
- **Desafios `[OPCIONAIS]` (Não bloqueantes):** `[ ] H06-OP1   [ ] H06-OP2`

---

## 1. Instruções Curtas (Checklist de Verificação e Arguição)

1. **Checklist sistemático em matrizes pequenas conferidas à mão:**
   - **Brilho (`H02`):** testar `b > 0` ultrapassando `255` (satura em `255`), `b < 0` ficando abaixo de `0` (satura em `0`) e `b == 0`.
   - **Blur (`H03`):** testar `t = 3, 5, 7`, garantindo divisão inteira e **preservação exata das `r = t / 2` bordas** sem contaminação cruzada (`static int aux`).
   - **Mediana (`H04`):** testar ruído extremo (`0` e `255`), reinício de `k = 0` por pixel, `ordenar(v, 9)`, seleção de `v[4]` e preservação das bordas.
   - **Menu (`H05`):** testar leitura única pré-menu (e falha na leitura), rejeição de `t` fora de `{3, 5, 7}`, opção inválida, encadeamento de 2+ operações e gravação correta ao escolher `0`.
2. **Preparação para arguição individual e modificações ao vivo (`Trabalho` Seção 7):**
   - Saber explicar **sem ler o código pronto**: o papel de cada um dos 5 arquivos, por que `#ifndef` protege contra inclusão múltipla, por que `aux` usa `static`, por que `brilho`/`limiar` não precisam de `aux` mas `blur`/`mediana` precisam, e por que funções `const` impedem alteração acidental.
   - Saber executar **modificações pontuais rápidas** mantendo a separação `.h`/`.c`/`main.c` (adicionar filtro no módulo `funcoes`, atualizar protótipo em `funcoes.h`, adicionar `case` + `break;` em `main.c`).
3. **Política dos Desafios `[OPCIONAIS]`:**
   - Os itens `H06-OP1 [OPCIONAL]` e `H06-OP2 [OPCIONAL]` permanecem dentro da ementa (recursão e modularização `.h`/`.c`), servem para aprofundamento adicional e **jamais bloqueiam a aprovação** caso não sejam resolvidos.

---

## 2. Exemplos Guiados

### Exemplo 1 — Roteiro de modificação ao vivo em 3 passos *(Trecho ilustrativo)*
Para adicionar uma nova operação (ex.: **negativo**, `img[i][j] = 255 - img[i][j]`) ao sistema de 5 arquivos:
1. **`funcoes.h`:** declarar o protótipo `void aplicarNegativo(int img[ALTURA][LARGURA]);` dentro da guarda `#ifndef FUNCOES_H`.
2. **`funcoes.c`:** implementar `aplicarNegativo` percorrendo `0 <= i < ALTURA` e `0 <= j < LARGURA` (como depende apenas do próprio pixel, não precisa de matriz auxiliar `aux`).
3. **`main.c`:** acrescentar a opção no menu impresso e inserir `case 4: aplicarNegativo(img); break;` no `switch` (nunca esquecendo o `break;`).

### Exemplo 2 — Modelo de explicação oral objetiva *(Para arguição)*
- **Pergunta:** *"Por que `lerImagem` recebe `int img[ALTURA][LARGURA]`, mas `salvarImagem` recebe `const int img[ALTURA][LARGURA]`?"*
- **Resposta esperada:** *"Em C, matrizes são passadas pelo endereço do primeiro elemento, então `lerImagem` consegue preencher diretamente a matriz declarada na `main`. Já `salvarImagem` apenas lê os pixels para gravar a saída; o qualificador `const` garante em tempo de compilação que ela não alterará a imagem acidentalmente."*

---

## 3. Exercícios (`H06-E01` a `H06-E06` + Opcionais)

### Sessão 1 (`H06-E01` a `H06-E03` — Casos de Borda, Simulado Misto e Arguição)

### `H06-E01` *(Checklist de Casos de Borda Calculados à Mão)*
Sem usar computador, considere a matriz `5 x 5` abaixo:
```text
 10   20   30   40   50
 60  220  230  240   70
 80  100  255  110   90
 15  120  130  140   25
  0   35   45   55  250
```
Calcule à mão, a partir da **matriz original** em cada item:
- **(a)** O resultado de `ajustarBrilho(img, 40)` nos pixels `(0, 0)`, `(1, 1)`, `(1, 3)` e `(4, 4)`.
- **(b)** O resultado de `ajustarBrilho(img, -40)` nos pixels `(0, 0)`, `(3, 0)`, `(4, 0)` e `(4, 2)`.
- **(c)** O novo valor do pixel central `(2, 2)` após `aplicarMediana(img)` (mostre o vetor `v[9]` ordenado) e confirme se `(0, 0)` ou `(4, 4)` mudam.
- **(d)** O novo valor do pixel central `(2, 2)` após `aplicarBlur(img, 5)` (mostre a soma dos 25 pixels e a divisão inteira) e informe quantos dos 25 pixels permanecem inalterados como borda.

---

### `H06-E02` *(Simulado Misto Integrado — Rastreamento Sem Computador: Ponteiros + Matriz `const` + Recursão)*
Sem usar computador, rastreie o programa abaixo e escreva **exatamente** a saída impressa no terminal:

```c
#include <stdio.h>

void faixa_linha(const int m[][4], int lin, int *min, int *max) {
    *min = m[lin][0];
    *max = m[lin][0];
    for (int j = 1; j < 4; j++) {
        if (m[lin][j] < *min) {
            *min = m[lin][j];
        }
        if (m[lin][j] > *max) {
            *max = m[lin][j];
        }
    }
}

int contar_acima(const int v[], int n, int lim) {
    if (n == 0) {
        return 0;
    }
    return (v[n - 1] > lim) + contar_acima(v, n - 1, lim);
}

int main(void) {
    int m[2][4] = {
        {12, 5, 18, 9},
        {20, 3, 14, 7}
    };
    int mn, mx;

    faixa_linha(m, 0, &mn, &mx);
    printf("L0: %d..%d acima=%d\n", mn, mx, contar_acima(m[0], 4, mn));

    int ref = mn;
    faixa_linha(m, 1, &mn, &mx);
    printf("L1: %d..%d acima=%d\n", mn, mx, contar_acima(m[1], 4, ref));
    return 0;
}
```

---

### `H06-E03` *(Arguição Oral + Caça ao Bug em Modificação ao Vivo — 5 Arquivos)*
- **(a) Perguntas de Arguição (`Trabalho` Seção 7):** Responda objetivamente no papel:
  1. Por que matrizes como `static int aux[ALTURA][LARGURA];` usam `static` em imagens grandes?
  2. Por que `ajustarBrilho` pode alterar `img[i][j]` diretamente *in-place*, enquanto `aplicarBlur` e `aplicarMediana` exigem matriz auxiliar `aux`?
  3. O que ocorre no processo de compilação se você executar `gcc main.c imagem.c funcoes.h -o processador`?
- **(b) Caça ao Bug de Modificação ao Vivo (`7 x 7`):** Um estudante tentou adicionar a opção `4 - Inverter cores` (`255 - img[i][j]`) ao sistema de 5 arquivos, mas introduziu **3 bugs** nos trechos abaixo. Identifique e corrija os 3 bugs nos 5 arquivos completos documentando-os com **comentários `//`**:

**Trecho de `funcoes.h` (com bug):**
```c
int inverterCores(int img[ALTURA][LARGURA]);
```
**Trecho de `funcoes.c` (com bug):**
```c
void inverterCores(int img[ALTURA][LARGURA]) {
    for (int i = 0; i <= ALTURA; i++) {
        for (int j = 0; j <= LARGURA; j++) {
            img[i][j] = 255 - img[i][j];
        }
    }
}
```
**Trecho de `main.c` (com bug):**
```c
case 4:
    inverterCores(img);
default:
    printf("Opcao invalida.\n");
    break;
```

---

### Sessão 2 (`H06-E04` a `H06-E06` — Modificações ao Vivo e Simulado Final)

### `H06-E04` *(Modificação ao Vivo 1 — Adicionar Limiarização como Opção `4`)*
No sistema completo de **5 arquivos** (`ALTURA 7`, `LARGURA 7`), realize a modificação ao vivo para adicionar `limiarizar(int img[ALTURA][LARGURA], int limiar)` (`< limiar -> 0`, `>= limiar -> 255`) como opção `4` do menu:
- Menu impresso a cada ciclo:
  ```text
  ===== PROCESSAMENTO DE IMAGENS =====
  1 - Ajustar brilho
  2 - Aplicar desfoque (blur)
  3 - Aplicar filtro da mediana
  4 - Aplicar limiarizacao
  0 - Salvar e sair
  Escolha uma opcao:
  ```
- Na opção `4`, leia `limiar` e valide `0 <= limiar && limiar <= 255` (caso contrário, imprima `Limiar invalido. Use 0 a 255.\n` sem alterar a imagem).
- *Pista:* Garanta que todas as operações (`1`..`4`) atuem encadeadas sobre `img` até a opção `0`.

---

### `H06-E05` *(Modificação ao Vivo 2 — Novo Filtro `espelharHorizontal`)*
Adicione ao sistema de **5 arquivos** (`ALTURA 7`, `LARGURA 7`) a função `void espelharHorizontal(int img[ALTURA][LARGURA]);` que espelha cada linha horizontalmente (trocando `img[i][j]` com `img[i][LARGURA - 1 - j]` usando variável auxiliar `temp`), como opção `4` do menu:
- Menu impresso a cada ciclo:
  ```text
  ===== PROCESSAMENTO DE IMAGENS =====
  1 - Ajustar brilho
  2 - Aplicar desfoque (blur)
  3 - Aplicar filtro da mediana
  4 - Espelhar horizontalmente
  0 - Salvar e sair
  Escolha uma opcao:
  ```
- *Pista:* O laço de colunas `j` deve ir apenas até `j < LARGURA / 2`! Se percorrer até `LARGURA`, cada pixel será trocado duas vezes e voltará ao lugar original.

---

### `H06-E06` *(Simulado Final Integrado — Sistema 5 Arquivos + Resumo Estatístico por Ponteiros)*
Construa do zero o sistema integrado em **5 arquivos** (`ALTURA 7`, `LARGURA 7`) unindo Estágios E, F e H:
- Em `funcoes.h` / `funcoes.c`: `ajustarBrilho`, `aplicarBlur`, `ordenar`, `aplicarMediana`, `limiarizar` e **`void resumoImagem(const int img[ALTURA][LARGURA], int *min, int *max, double *media);`** (calcula mínimo, máximo e média real `double` via ponteiros de saída).
- Em `main.c`: leitura única pré-menu, menu com opções `1` (Brilho), `2` (Blur `3/5/7`), `3` (Mediana), `4` (Limiarização `0..255`), `0` (Salvar e sair). Ao escolher `0`, chame `resumoImagem(img, &min, &max, &media);`, imprima exatamente:
  ```text
  Minimo: MN
  Maximo: MX
  Media: MED.MM
  ```
  e depois chame `salvarImagem(img);`.

---

### Desafios `[OPCIONAIS]` *(Dentro da Ementa — Não Bloqueiam a Conclusão)*

### `H06-OP1 [OPCIONAL]` *(Filtro de Brilho Recursivo por Linhas — Integração `G04` + `H02`)*
Em um projeto de **5 arquivos** (`ALTURA 7`, `LARGURA 7`), implemente `void ajustarBrilhoLinhaRec(int img[ALTURA][LARGURA], int lin, int b);` que processa a linha `lin` (com saturação `[0, 255]`) e chama recursivamente `ajustarBrilhoLinhaRec(img, lin + 1, b);` com caso base `lin == ALTURA` (**sem** laço `for`/`while` para percorrer as linhas). No `main.c`, leia a imagem via `lerImagem(img)`, leia `int b`, chame `ajustarBrilhoLinhaRec(img, 0, b);` e salve com `salvarImagem(img);`.

### `H06-OP2 [OPCIONAL]` *(Novo Módulo `estatisticas.h/.c` — Arquitetura 7 Arquivos)*
Separe as estatísticas em um módulo dedicado (`estatisticas.h` com guardas `ESTATISTICAS_H` e `#include "imagem.h"`, e `estatisticas.c` implementando `int minimoImagem(const int img[ALTURA][LARGURA]);`, `int maximoImagem(const int img[ALTURA][LARGURA]);`, `double mediaImagem(const int img[ALTURA][LARGURA]);`), mantendo `main.c`, `imagem.h/.c`, `funcoes.h/.c` (total de **7 arquivos**). O menu terá opções `1` Brilho, `2` Blur, `3` Mediana, `4` Exibir estatisticas (`Minimo: MN\nMaximo: MX\nMedia: MED.MM\n`) e `0` Salvar e sair. Compilar com `gcc -std=c99 -Wall -Wextra main.c imagem.c funcoes.c estatisticas.c -o processador`.

---

## 4. Checagem Independente de Domínio *(Núcleo Obrigatório — Sem Consulta ao Gabarito — Exige 100%)*

### `H06-C01` *(Arguição Escrita + Teste de Mesa Combinado)*
1. Explique objetivamente no papel:
   - **(a)** Qual problema ocorre se `imagem.h` não possuir `#ifndef IMAGEM_H` quando incluído por `main.c`, `imagem.c` e `funcoes.h`?
   - **(b)** Por que `aplicarBlur` e `aplicarMediana` precisam copiar `img` para uma matriz auxiliar `aux` antes de calcular os pixels internos?
   - **(c)** Qual a diferença entre passar `int b` e passar `int img[ALTURA][LARGURA]` para uma função em C?
2. Sem usar computador, escreva o valor retornado por `contar_pares_rec(v, 5)` para `int v[5] = {4, 11, 7, 15, 2};` e desenhe a cadeia de chamadas e retornos:
   ```c
   int contar_pares_rec(const int v[], int n) {
       if (n == 0) return 0;
       return (v[n - 1] % 2 == 0) + contar_pares_rec(v, n - 1);
   }
   ```

### `H06-C02` *(Modificação ao Vivo no Papel — Limiarização + Validação)*
Escreva no papel, exatamente como ficariam nos 3 arquivos do projeto (`ALTURA 7`, `LARGURA 7`):
1. O protótipo a acrescentar em `funcoes.h`.
2. A implementação completa de `void limiarizar(int img[ALTURA][LARGURA], int limiar)` em `funcoes.c`.
3. O trecho `case 4:` completo do `switch` em `main.c` validando `0 <= limiar <= 255`.

### `H06-C03` *(Projeto Integrado Verificado — 5 Arquivos Completo)*
Implemente do zero os **5 arquivos** (`imagem.h`, `imagem.c`, `funcoes.h`, `funcoes.c`, `main.c`) com `ALTURA 7` e `LARGURA 7`, incluindo as operações `1` (Ajustar brilho), `2` (Aplicar blur `3/5/7`), `3` (Aplicar mediana `3 x 3`), `4` (Aplicar negativo `255 - img[i][j]`) e `0` (Salvar e sair). Compile limpo com `gcc -std=c99 -Wall -Wextra main.c imagem.c funcoes.c -o processador` e verifique operações encadeadas + casos de borda.

---

## 5. Orientação de Avanço ou Recuperação (Conclusão do Curso)

- **Conclusão do Estágio H e do Curso (`CC61A — Algoritmos`):** liberada somente após autocorreção de `H06-E01..E06` e **100% de acerto (3/3)** na Checagem Independente Obrigatória `H06-C01..C03` sem consulta ao gabarito. *(Os desafios `H06-OP1` e `H06-OP2` são `[OPCIONAIS]` e **não bloqueiam** a conclusão.)*
- **Recuperação direcionada por eixo de falha (1ª tentativa):**
  - Errou caso de borda calculado à mão (`brilho`, `blur`, `mediana`) $\rightarrow$ revisar **`H02`**, **`H03`** ou **`H04`** no ponto específico.
  - Errou rastreamento de ponteiros ou recursão sem laços $\rightarrow$ revisar **`F05`** e **`G04`**–**`G05`**.
  - Errou modificação ao vivo (`.h`/`.c`, `break` no `switch`, limites de laço) $\rightarrow$ revisar **`F08`** e **`H05`** e aplicar variante equivalente `V2`.
- **Após 2 tentativas malsucedidas:** interromper novas tentativas em `H06`, mapear qual pré-requisito (`H01`–`H05`, `F08`, `G09`) originou a falha e reabilitá-lo integralmente antes da nova checagem de conclusão.

---

## 6. Referências do Orientador
- `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 5–6 (23/11, 24/11, 08/12, 11/12 — apresentação/arguição do trabalho e avaliação).
- `[DOC]` `Trabalho_Algoritmos.pdf` p. 4–5 (Seções 6 e 7 — Testes recomendados em matrizes pequenas, critérios de avaliação e explicação individual com modificações no código).
- `[DOC]` `Apresentacao_Trabalho_Algoritmos.pdf` p. 14, 16–17 (Roteiro de testes e preparação para explicação individual).
- `[DOC]` [00_mapa_curricular.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/00_mapa_curricular.md) (linhas 817–826 — Bloco `H06`).
- Casos de teste e soluções verificáveis: [H06_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/gabaritos/H06_gabarito.md) e [H06_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_H/testes/H06_testes.md).
