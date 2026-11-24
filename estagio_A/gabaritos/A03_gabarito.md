# Gabarito Comentado — Bloco `A03` (`printf` e Sequências de Escape)

> **Bloco de referência:** [A03_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/blocos/A03_bloco.md)  
> **Nota para Caça ao Bug:** Os códigos de `A03-E03` e `A03-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo. Apenas as versões corrigidas em `solucoes/` devem ser compiladas.

---

## 1. Gabarito dos Exercícios (`A03-E01` a `A03-E05`)

### `A03-E01` *(Teste de Mesa caractere a caractere)*
```text
Log:<TAB>"ok"
Rota:<TAB>/home\aluno
Fim
```
- **Observações:** O primeiro `printf` não tem `\n`, mas o segundo **começa** com `\n`, provocando a quebra antes de `Rota:`. Em `/home\\aluno`, `\\` imprime uma única barra `\`. A palavra `Fim` é impressa sem quebra de linha ao final.

### `A03-E02` *(Completar sequências de escape)*
- **`/* A */`:** `\"`
- **`/* B */`:** `\"`
- **`/* C */`:** `\t`
- **`/* D */`:** `\\` *(em ambas as ocorrências)*

### `A03-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. Em `C:\usuarios`, a sequência `\u` não usa barra duplicada `\\` (o compilador interpreta `\u` como escape inválido, gerando erro).
  2. Em `\aluno`, a sequência `\a` é interpretada como caractere de controle sonoro (alerta) em vez de `\a` literal; o correto é `\\aluno`.
  3. Falta `\n` ao final do primeiro `printf("Diretorio: C:\usuarios\aluno");`, o que juntaria `Mensagem:` na mesma linha.
  4. Em `"Compilado!"`, as aspas internas não estão escapadas com `\"`, encerrando a string antes da hora e gerando erro de sintaxe.
- **Solução corrigida completa:** [A03_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A03_E03_corrigido.c)
```c
/* Exercicio A03-E03: Correcao de barras e aspas */
#include <stdio.h>

int main(void) {
    printf("Diretorio: C:\\usuarios\\aluno\n");
    printf("Mensagem: \"Compilado!\"\n");
    return 0;
}
```

### `A03-E04` *(Programa completo — Único `printf` multilinhas)*
Arquivo: [A03_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A03_E04.c)
```c
/* Exercicio A03-E04: Unico printf multilinhas com aspas */
#include <stdio.h>

int main(void) {
    printf("UTFPR - Campus Ponta Grossa\nDisciplina: Algoritmos\nPadrao: \"C99\"\n");
    return 0;
}
```

### `A03-E05` *(Programa completo — Tabela com tabulação e escapes)*
Arquivo: [A03_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A03_E05.c)
```c
/* Exercicio A03-E05: Tabela com tabulacao e sequencias de escape */
#include <stdio.h>

int main(void) {
    printf("Comando\tFuncao\n\"gcc\"\tCompila C\n\\n\tNova linha\n\\\\\tBarra literal\n");
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`A03-C01` a `A03-C03`)

### `A03-C01` *(Previsão de saída no papel)*
```text
Caminho:<TAB>"src\main.c"
Status:<TAB>Pronto
```
*(Em `"\"src\\main.c\""`, cada `\"` imprime `"` e `\\` imprime uma única barra `\`; ambas as linhas terminam com `\n`.)*

### `A03-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. Falta `\n` ao final do primeiro `printf("Codigo:\t100");`, o que colaria `Rota:` na mesma linha.
  2. Em `C:\projetos`, `\p` é sequência de escape inválida (faltou `\\`).
  3. Em `\teste`, `\t` seria interpretado como tabulação horizontal antes de `este` em vez de barra invertida seguida de `teste` (faltou `\\teste`).
  4. As aspas de `"Aprovado"` não usam `\"`, fechando a string prematuramente.
- **Solução corrigida completa:** [A03_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A03_C02_corrigido.c)
```c
/* Checagem A03-C02: Correcao de escapes \n, \t, \\ e \" */
#include <stdio.h>

int main(void) {
    printf("Codigo:\t100\n");
    printf("Rota:\tC:\\projetos\\teste\n");
    printf("Nota:\t\"Aprovado\"\n");
    return 0;
}
```

### `A03-C03` *(Programa completo — Único `printf` multilinhas)*
Arquivo: [A03_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A03_C03.c)
```c
/* Checagem A03-C03: Relatorio em unico printf multilinhas */
#include <stdio.h>

int main(void) {
    printf("Relatorio\t\"Final\"\nPasta:\tD:\\aulas\\c\nSituacao:\tOK\n");
    return 0;
}
```
