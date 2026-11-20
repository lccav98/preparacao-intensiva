# Gabarito, Mapa de Pré-Requisitos e Matriz de Posicionamento — Diagnóstico

> **Referência:** Gabarito oficial do instrumento [00_teste_diagnostico.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/00_teste_diagnostico.md).  
> **Regra Central:** O posicionamento ocorre **pelos pré-requisitos demonstrados**, nunca pela soma bruta de acertos.

---

## 1. Gabarito Comentado — Etapa 1: Triagem Inicial Curta (`T1` a `T8`)

| Item | Estágio / Blocos | Resposta Esperada (Exata) | Erros Típicos e Pré-Requisito Sinalizado | Fontes (`[DOC]` / `[INF]`) |
|---|---|---|---|---|
| **`T1`** | `A` (`A04`–`A07`) | **(a)** `5 14` (`p=14, q=5` → `p=9` → `q=14` → `p=5`).<br>**(b)** Falta o operador de endereço `&` em `scanf("%lf", &nota);`. | Errar (a) por não atualizar passo a passo → revisar **`A07`**.<br>Não detectar falta de `&` → revisar **`A06`**.<br>Desconhecer estrutura C → **`A01`/`A02`**. | `[DOC]` `Aula_03` p. 4–22 |
| **`T2`** | `B` (`B01`–`B02`) | `3.0 11 1`<br>• `a / b`: `7 / 2 = 3` (divisão inteira antes de converter para `double`).<br>• `expr`: `2 + (6 / 2) * 3 = 2 + 3 * 3 = 11`.<br>• `a % b`: `7 % 2 = 1`. | Responder `3.5` (não reconhecer divisão inteira em `double r = a / b`) → **`B01`**.<br>Responder `12` (`(2+6)/2*3`) ou `3` (`2+6/(2*3)`) → **`B02`**. | `[DOC]` `Aula_05` p. 7–19; `Lista1` Ex. 1–2 |
| **`T3`** | `B` (`B05`–`B09`) | **(a)** `P` (`&&` precede `\|\|`: `y<5 && x==10` dá `1 && 0 = 0`; em seguida `x>15 \|\| 0` dá `1 \|\| 0 = 1`, entra no 1º ramo e encerra a cadeia).<br>**(b)** `BC` (entra no `case 2:`, imprime `B`, faz *fall-through* no `case 3:`, imprime `C` e para no `break`). | Responder `Q` em (a) avaliando `\|\|` antes de `&&` (`(1 \|\| 1) && 0 = 0`) → **`B06`**.<br>Imprimir `PQR` em (a) → **`B05`**.<br>Responder `B` em (b) (ignorar *fall-through*) → **`B08`**. | `[DOC]` `ementa` item 5–6; `Aula_07` p. 11–15; `Aula_08_v2` p. 7–8; `Lista3` Ex. 1 |
| **`T4`** | `C` (`C01`, `C05`–`C06`) | **(a)** `F:12` (condição `12 < 10` falsa no pré-teste: executa 0 vezes).<br>**(b)** `12 10` (`i = 1, 4, 7`, `soma = 1+4+7 = 12`; após `i += 3`, `i = 10` falha em `10 <= 7`). | Executar o `while` uma vez (`12 F:14`) → **`C01`**.<br>Imprimir `i = 7` no final de (b) ou errar acumulação → **`C05`–`C06`**. | `[DOC]` `Aula_09` p. 6–10; `Aula_10` p. 5–12; `Lista4` Ex. 1 |
| **`T5`** | `D` (`D01`–`D02`, `D06`) | `-2 1 ALGO`<br>• `maior = -2`, `pos = 1` (`>` mantém a 1ª ocorrência no índice `1`, ignorando índice `3`).<br>• `texto[4] = '\0'` encerra a string após 4 caracteres (`ALGO`). | Inicializar mentalmente em `0` → **`D02`**.<br>Responder `pos = 3` (desempate errando `>` vs `>=`) → **`D02`**.<br>Ignorar efeito de `'\0'` em `texto[4]` → **`D06`**. | `[DOC]` `Aula_12` p. 5–11; `Aula_13` p. 5–8; `Lista6` Ex. 1 |
| **`T6`** | `E` (`E01`–`E05`) | `11 \| 2 5 7 `<br>• `soma_sec = m[0][2] + m[1][1] + m[2][0] = 1 + 3 + 7 = 11`.<br>• Segundo laço imprime a coluna `0`: `m[0][0]=2`, `m[1][0]=5`, `m[2][0]=7`. | Inverter linha/coluna em `m[j][0]` (imprimindo linha `0`: `2 4 1`) → **`E01`/`E03`**.<br>Errar diagonal secundária `m[i][2-i]` → **`E04`**. | `[DOC]` `Aula_15` p. 6–8, 13–14; `Lista9` Ex. 1, 4 |
| **`T7`** | `F` (`F03`–`F05`, `F08`) | **(a)** `3 14` (`x` recebe cópia por valor, logo `a` segue `3`; `y` recebe `&b`, logo `*y += 10` altera `b` para `14`).<br>**(b)** Erro de ligação **`undefined reference`** (às funções de `calc.c`), porque `calc.c` não foi passado no comando `gcc main.c calc.c -o app`. | Responder `13 14` → **`F03`/`F05`**.<br>Achar que `#include "calc.h"` dispensa listar `calc.c` no `gcc` → **`F08`**. | `[DOC]` `Aula_18` p. 4–8; `Aula_19` p. 10–13 |
| **`T8`** | `G` (`G01`–`G02`) | **(a)** `if (n == 0)` (retorna quando `n == 0`).<br>**(b)** `I3 I2 I1 V1 V2 V3 ` (`I*` executa na ida/empilhamento; `V*` executa na volta/desempilhamento). | Imprimir `I3 I2 I1 V3 V2 V1` (não entender ordem LIFO do retorno da pilha) ou `I3 V3 I2 V2 I1 V1` → **`G01`–`G02`**. | `[DOC]` `Aula_21` p. 18, 21–24; `Lista11` Ex. 1 |

---

## 2. Gabarito Comentado — Etapa 2: Sondagens Específicas (`S-A` a `S-G`)

### Sondagem `S-A`
- **`SA-01` (Item-âncora):** **Não compila.** Três erros: (1) `Int` com inicial maiúscula (C é *case-sensitive*; deve ser `int`); (2) falta `;` após `printf("Ola UTFPR\n")`; (3) falta `;` após `return 0`.
  - *Se falhar:* posicionar em **`A02`** (ou **`A01`** se o aluno também não compreende o conceito de algoritmo/fluxo de programa). `[DOC]` `Aula_02` p. 6, 8, 13.
- **`SA-02`:** (1) Válidos: **`nota_1`** e **`_contador`**. Inválidos: `2aluno` (inicia com dígito), `total$` (`$` não permitido), `float` (palavra reservada). (2) `int aux = x; x = y; y = aux;` (ou `int aux;` seguido das 3 atribuições).
  - *Se falhar parte (1):* **`A04`** | *Se falhar parte (2):* **`A07`**. `[DOC]` `Aula_02` p. 8–9; `Aula_03` p. 21.
- **`SA-03`:** (1) 6 bits representam $2^6 = 64$ valores distintos; 500 estados exigem $\lceil \log_2 500 \rceil = 9$ bits ($2^8 = 256 < 500 \le 512 = 2^9$). (2) `0,1` decimal não possui representação binária exata finita, sendo armazenado como aproximação binária; **`double`** oferece maior precisão (~15–16 dígitos em 8 bytes vs. ~6–7 em 4 bytes do `float`).
  - *Se falhar:* **`A08`** (binário/bits) ou **`A09`** (precisão `float` vs `double`). `[DOC]` `Aula_04` p. 5–7, 14–18.

### Sondagem `S-B`
- **`SB-01` (Item-âncora):** `double media = (double)a / b;` (ou `a / (double)b;`); expressão `9 / 4 * 4 + 9 % 4` = `2 * 4 + 1` = **`9`**.
  - *Se falhar:* parar `S-B` (`I4`) e posicionar em **`B01`** (se errou `/` ou `%`) ou **`B02`** (se errou *cast* ou precedência). `[DOC]` `Aula_05` p. 7–19.
- **`SB-02`:** A condição mais ampla (`nota >= 6.0`) aparece antes da mais restritiva (`nota >= 9.0`), fazendo notas $\ge 9{,}0$ entrarem no primeiro ramo e tornando o segundo inatingível. Correção:
```c
if (nota >= 9.0) {
    printf("Otimo\n");
} else if (nota >= 6.0) {
    printf("Aprovado\n");
} else {
    printf("Reprovado\n");
}
```
  - *Se falhar:* **`B05`** (ou **`B04`** se confundir `else if` com `if`s independentes). `[DOC]` `Aula_07` p. 13.
- **`SB-03`:** (1) Em C, `10 <= idade` produz `0` ou `1`, e em seguida `0 <= 18` ou `1 <= 18` resulta sempre em `1` (verdadeiro). Forma correta: `if (idade >= 10 && idade <= 18)`. (2)
```c
switch (op) {
    case 1:
    case 2:
    case 3:
        printf("Desconto\n");
        break;
    case 4:
        printf("Normal\n");
        break;
    default:
        printf("Invalido\n");
        break;
}
```
  - *Se falhar parte (1):* **`B06`** | *Se falhar parte (2):* **`B08`**. `[DOC]` `ementa` item 5; `Aula_08_v2` p. 9.

### Sondagem `S-C`
- **`SC-01` (Item-âncora):** (1) `x` não foi inicializada antes de `while (x != -1)` (lixo de memória; se por acaso valer `-1`, o laço nunca executa); (2) ao digitar `-1`, `soma += x;` soma o próprio sentinela (`-1`) antes de testar novamente a condição, corrompendo o resultado. Correção por *priming read*:
```c
int x, soma = 0;
scanf("%d", &x);
while (x != -1) {
    soma += x;
    scanf("%d", &x);
}
```
  - *Se falhar:* parar `S-C` (`I4`) e posicionar em **`C01`** (se não compreende pré-teste) ou **`C03`** (se o único erro foi o padrão de sentinela). `[DOC]` `Aula_09` p. 13–14, 18.
- **`SC-02`:** (1) `3` (`do-while` executa ao menos uma vez: `c = 0 + 3 = 3`, testa `3 < 3` falso e sai). (2) `4` (o `;` após `for (...)` cria corpo nulo; `i` avança `0 → 1 → 2 → 3 → 4` e então o `printf` executa uma vez).
  - *Se falhar (1):* **`C04`** | *Se falhar (2):* **`C05`/`C06`**. `[DOC]` `ementa` item 7; `Aula_10` p. 26–27.
- **`SC-03`:** (1) **`1 2 4 `** (`i=3` salta o `printf` via `continue`; `i=5` encerra via `break`). (2)
```c
for (int i = 1; i <= 4; i++) {
    for (int j = 1; j <= i; j++) {
        printf("*");
    }
    printf("\n");
}
```
  - *Se falhar (1):* **`C07`** | *Se falhar (2):* **`C09`**. `[DOC]` `Aula_10` p. 19–22; `Aula_11` p. 8–9.

### Sondagem `S-D`
- **`SD-01` (Item-âncora):** (1) Último índice válido é **`3`** (`0..3`); `v[4]` realiza acesso fora dos limites do vetor (C não verifica índices automaticamente, gerando comportamento indefinido). (2)
```c
int soma = 0;
int menor = v[0], pos_menor = 0;
for (int i = 0; i < 4; i++) {
    soma += v[i];
    if (v[i] <= menor) {
        menor = v[i];
        pos_menor = i;
    }
}
double media = (double)soma / 4;
```
  - *Se falhar (1):* **`D01`** | *Se falhar (2) (ex.: usar `<` em vez de `<=` ou `soma / 4` inteiro):* **`D02`**. `[DOC]` `Aula_11` p. 27; `Aula_12` p. 11–13; `Lista6` Ex. 1–2.
- **`SD-02`:** (1) Valor máximo de `i` é **`3`** (`M - N = 6 - 3 = 3`, acessando `a[3], a[4], a[5]`). (2) **`2`** ocorrências com sobreposição: iniciando em `i = 0` (`a[0..2]`) e em `i = 2` (`a[2..4]`).
  - *Se falhar:* **`D05`** (ou **`D03`** se houver falha prévia em busca simples). `[DOC]` `Aula_12` p. 21–24; `Lista6` Ex. 5.
- **`SD-03`:** (1) `"UTFPR"` possui 5 caracteres mais o terminador `'\0'`, exigindo ao menos **6 posições** (`N + 1`). (2) Usar `strcpy(s2, s1);` e `strcmp(s1, s2) == 0`; usar `s1 == s2` compara os endereços dos vetores, não o conteúdo textual. (3) `2 * 5 + 3 = 13`.
  - *Se falhar (1):* **`D06`** | *(2):* **`D08`** | *(3):* **`D09`**. `[DOC]` `Aula_13` p. 5, 20–22; `Aula_14` p. 4–5; `Lista7` Ex. 6.

### Sondagem `S-E`
- **`SE-01` (Item-âncora):** (1) `3 × 4 = 12` elementos; linhas `0..2` e colunas `0..3`. (2) `break;` encerra apenas o `for` interno (`j`); o `for` externo (`i`) continua executando e pode encontrar outra ocorrência e sobrescrever `(li, co)`. Correção: incluir `&& li == -1` na condição do `for` externo: `for (int i = 0; i < 3 && li == -1; i++)`.
  - *Se falhar (1):* **`E01`** | *Se falhar (2):* **`E02`**. `[DOC]` `Aula_14` p. 7–9; `Aula_15` p. 20.
- **`SE-02`:** (1) `i == j` (`m[i][i]`); (2) `i + j == N - 1` (para `N=4`, `i + j == 3`, `m[i][3 - i]`); (3) `j > i`.
  - *Se falhar:* **`E04`**. `[DOC]` `Aula_15` p. 13–15.
- **`SE-03`:** (1) `T` deve ter dimensões **`5 × 3`**, com `T[j][i] = A[i][j];`. (2) `C` tem dimensões **`2 × 4`**, e cada `C[i][j]` soma **`3`** multiplicações ($k = 0, 1, 2$).
  - *Se falhar (1):* **`E05`** | *Se falhar (2):* **`E06`**. `[DOC]` `Aula_15` p. 18; `Lista9` Ex. 5, 7.

### Sondagem `S-F`
- **`SF-01` (Item-âncora):** (1) Falta o **protótipo** `int dobro(int x);` antes de `main`. (2) `a` continua valendo **`4`**, porque argumentos em C são passados **por valor** (o parâmetro `n` recebe apenas uma cópia local).
  - *Se falhar (1):* **`F02`** (ou **`F01`** se desconhecer sintaxe básica) | *Se falhar (2):* **`F03`**. `[DOC]` `Aula_17` p. 4–14.
- **`SF-02`:** (1) `int *tmp;` é um ponteiro não inicializado (endereço indeterminado); `*tmp = *a;` tenta escrever em endereço inválido, gerando comportamento indefinido. Correção: `int tmp = *a; *a = *b; *b = tmp;`. (2) Deve chamar **`trocar(p, q)`** (sem `&`), pois `p` e `q` já armazenam os endereços recebidos por `ordena`.
  - *Se falhar (1):* **`F04`**/`**F05**` | *Se falhar (2):* **`F05`**. `[DOC]` `Aula_17` p. 24, 35; `Aula_18` p. 34–35; `Lista10` Ex. 3–4.
- **`SF-03`:** (1) Como a matriz é armazenada linearmente por linhas, o compilador exige o número de colunas para localizar a linha `i` (`i * 5 + j`). Assinatura recomendada: `void exibir(const int m[][5], int linhas);`. (2) Definições ficam em `filtros.c`; guardas `#ifndef`/`#define`/`#endif` impedem redefinições se o cabeçalho for incluído mais de uma vez; compilação: `gcc main.c filtros.c -o programa` (recomendado `-std=c99 -Wall -Wextra`).
  - *Se falhar (1):* **`F07`** | *Se falhar (2):* **`F08`**. `[DOC]` `Aula_18_parte2` p. 3; `Aula_19` p. 11–13.

### Sondagem `S-G`
- **`SG-01` (Item-âncora):** Saída: **`1 2 3 `** (o `printf` ocorre após o retorno da chamada recursiva, desempilhando de `1` até `3`). Sem o caso base `if (n <= 0) return;`, as chamadas avançam indefinidamente (`0, -1, -2, ...`) até esgotar a pilha de execução (*stack overflow*).
  - *Se falhar:* parar `S-G` (`I4`) e posicionar em **`G01`** (caso base/pilha) ou **`G02`** (ordem pré/pós-recursão). `[DOC]` `Aula_21` p. 18–22.
- **`SG-02`:**
```c
int soma_pares(const int v[], int n) {
    if (n == 0) {
        return 0;
    }
    if (v[n - 1] % 2 == 0) {
        return v[n - 1] + soma_pares(v, n - 1);
    }
    return soma_pares(v, n - 1);
}
```
  - *Se falhar (usar `for`/`while`, errar `n == 0` ou `v[n - 1]`):* **`G03`** ou **`G04`**. `[DOC]` `Aula_22` p. 25–33; `Lista11` Ex. 5–6.
- **`SG-03`:** (1)
```c
int contar_letra(const char s[], int i, char alvo) {
    if (s[i] == '\0') {
        return 0;
    }
    return (s[i] == alvo) + contar_letra(s, i + 1, alvo);
}
```
  (2) Duplicar a chamada recursiva no `return` faz o algoritmo recalcular todo subproblema duas vezes a cada passo, transformando a complexidade de chamadas de logarítmica para linear ($O(n)$ em vez de $O(\log n)$).
  - *Se falhar (1):* **`G06`** | *Se falhar (2):* **`G08`**. `[DOC]` `Aula_23` p. 7–8; `Aula_24` p. 6–8, 14–17.

---

## 3. Matriz de Decisão de Posicionamento (Pré-Requisitos Demonstrados)

> **Princípio Inviolável:** Um acerto na Etapa 1 (`T_k`) **não libera** o estágio se houver pré-requisito anterior falho não superado na sondagem correspondente. O ponto de entrada é **sempre o menor bloco com pré-requisito ausente**.

| Perfil Observado na Triagem (Etapa 1) | Sondagem Aplicada (Etapa 2) | Resultado na Sondagem | Bloco Inicial Recomendado | Status do Posicionamento e Ação de Confirmação |
|---|---|---|---|---|
| Sem contato prévio com C (`I2`) | Nenhuma | — | **`A01`** | **DEFINITIVO** (início integral da trilha). |
| Falhou `T1` com algum contato prévio (`I2`) | `S-A` | Falhou `SA-01` (`I4`)<br>Acertou `SA-01`, falhou `SA-02`<br>Acertou `SA-01..02`, falhou `SA-03` | **`A01`/`A02`**<br>**`A04`** ou **`A07`**<br>**`A08`** | **DEFINITIVO** (início em `A01`–`A02`; ou **`PROVISÓRIO`** se entrou em `A04`–`A08` — confirmar no bloco seguinte). |
| Acertou `T1`; falhou `T2` ou `T3` | `S-A` (se houve dúvida em `T1`) e `S-B` | `SA-01..03` ok; falhou `SB-01` (`I4`)<br>Falhou `SB-02`<br>Falhou `SB-03` | **`B01`**<br>**`B04`** ou **`B05`**<br>**`B06`** ou **`B08`** | **PROVISÓRIO** se pular todo o Estágio A sem evidência de escrita compilável; confirmar via checagem de `A10` se houver hesitação. |
| Acertou `T1`–`T3`; falhou `T4` | `S-C` (e `S-B` se `T2`/`T3` parcial) | Falhou `SC-01` (`I4`)<br>Falhou `SC-02`<br>Falhou `SC-03` | **`C01`** ou **`C03`**<br>**`C04`** ou **`C05`**<br>**`C07`** ou **`C09`** | **PROVISÓRIO** (entrada direta $\ge$ Estágio C exige confirmação prática nas 2 primeiras sessões). |
| Acertou `T1`–`T4`; falhou `T5` | `S-D` | Falhou `SD-01` (`I4`)<br>Falhou `SD-02`<br>Falhou `SD-03` | **`D01`** ou **`D02`**<br>**`D03`** ou **`D05`**<br>**`D06`** ou **`D08`** | **PROVISÓRIO** (confirmar nas 2 primeiras sessões com compilação em GCC/Linux). |
| Acertou `T1`–`T5`; falhou `T6` | `S-E` | Falhou `SE-01` (`I4`)<br>Falhou `SE-02`<br>Falhou `SE-03` | **`E01`** ou **`E02`**<br>**`E03`** ou **`E04`**<br>**`E05`** ou **`E06`** | **PROVISÓRIO** (verificar habilidade real de escrita de matrizes 2D no bloco inicial). |
| Acertou `T1`–`T6`; falhou `T7` | `S-F` | Falhou `SF-01` (`I4`)<br>Falhou `SF-02`<br>Falhou `SF-03` | **`F01`/`F02`**<br>**`F04`** ou **`F05`**<br>**`F07`** ou **`F08`** | **PROVISÓRIO** (verificar fluência em ponteiros e ligação multi-arquivo). |
| Acertou `T1`–`T7`; falhou `T8` | `S-G` | Falhou `SG-01` (`I4`)<br>Falhou `SG-02`<br>Falhou `SG-03` | **`G01`**<br>**`G03`** ou **`G04`**<br>**`G06`** ou **`G08`** | **PROVISÓRIO** (confirmar capacidade de escrever recursão sem laços). |
| Acertou `T1`–`T8` integralmente | `S-F` (`SF-03`) + `S-G` (`SG-02`–`03`) para confirmar | Todas corretas com boa fluência | **`H01`** (Projeto Integrador) | **PROVISÓRIO** até concluir `H01` (compilação dos 5 arquivos `.h`/`.c` no GCC). |
| Perfil "dente de serra" (ex.: acertou `T5`, mas errou `T2` ou `T4`) | Sondar o **menor estágio falho** (`S-B` ou `S-C`) | Conforme item falho na menor sondagem | **Menor bloco pré-requisito falho** (ex.: `B01` ou `C01`) | **PROVISÓRIO**; após dominar o pré-requisito falho, pode acelerar os blocos seguintes já dominados mediante checagem independente direta. |
