# Gabarito Comentado — Bloco `A02` (Anatomia de um Programa em C e Compilação no GCC/Linux)

> **Bloco de referência:** [A02_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/blocos/A02_bloco.md)  
> **Nota para Caça ao Bug:** Os códigos de `A02-E03` e `A02-C02` no bloco do aluno contêm **erros intencionais** listados abaixo. Apenas as versões corrigidas salvas em `solucoes/` devem ser compiladas.

---

## 1. Gabarito dos Exercícios (`A02-E01` a `A02-E05`)

### `A02-E01` *(Leitura e Diagnóstico no papel)*
- **(a)** `printf("Curso de C);` → **Inválido:** faltou fechar as aspas duplas `"` antes de `)`.
- **(b)** `Printf("Teste\n");` → **Inválido:** `P` maiúsculo; C é *case-sensitive* e a função chama-se `printf`.
- **(c)** `printf "Algoritmos\n";` → **Inválido:** faltaram os parênteses `(...)` envolvendo o argumento da chamada de função.
- **(d)** `print("Ola\n");` → **Inválido:** a função `print` não existe na biblioteca padrão `<stdio.h>` (o nome correto em C é `printf`).
- **(e)** Em sistemas Linux, por segurança o terminal não procura executáveis na pasta atual sem indicação explícita de caminho; `./meu_prog` informa ao shell para executar o arquivo `meu_prog` localizado no diretório corrente (`.`).

### `A02-E02` *(Completar esqueleto + comando GCC)*
- **`/* A */`:** `#include <stdio.h>`
- **`/* B */`:** `printf("Linguagem C ativa\n");`
- **`/* C */`:** `return 0;`
- **Comandos no terminal Linux:**
  1. `cd pratica_a02`
  2. `gcc -std=c99 -Wall -Wextra saudacao.c -o saudacao`
  3. `./saudacao`

### `A02-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. Comentário de bloco `/*` no topo não foi fechado com `*/`, fazendo o compilador ignorar `#include <stdio.h>` e todo o resto do código.
  2. `Int main(void)` escreve `Int` com inicial maiúscula; a palavra reservada correta em C é `int` (*case-sensitive*).
  3. Falta ponto-e-vírgula `;` ao final de `printf("UTFPR Ponta Grossa\n")`.
  4. `Printf("Laboratorio GCC\n");` usa `P` maiúsculo; o identificador da função é `printf`.
- **Solução corrigida completa:** [A02_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A02_E03_corrigido.c)
```c
/*
   Exercicio A02-E03
   Objetivo: Exibir instituicao e laboratorio
*/
#include <stdio.h>

int main(void) {
    printf("UTFPR Ponta Grossa\n");
    printf("Laboratorio GCC\n");
    return 0;
}
```

### `A02-E04` *(Programa completo — Etapas de desenvolvimento)*
Arquivo: [A02_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A02_E04.c)
```c
// Exercicio A02-E04: Etapas basicas de desenvolvimento em C
#include <stdio.h>

int main(void) {
    printf("Passo 1: Editar codigo\n");
    printf("Passo 2: Compilar com gcc\n");
    printf("Passo 3: Executar no Linux\n");
    return 0;
}
```

### `A02-E05` *(Programa completo e reflexão)*
- **(a)** Arquivo: [A02_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A02_E05.c)
```c
/* Programa: Informacoes do ambiente da disciplina */
#include <stdio.h>

int main(void) {
    printf("Curso: Algoritmos CC61A\n");
    printf("Padrao: C99\n");
    printf("Compilador: GCC Linux\n");
    return 0;
}
```
- **(b)** O **algoritmo** em linguagem natural descreve os passos lógicos independentemente de máquina ou regras de sintaxe específicas (basta que um humano entenda sem ambiguidade). Já o **programa em C** é a implementação desse algoritmo em uma linguagem formal, exigindo biblioteca (`#include <stdio.h>`), função de entrada (`int main(void)`), pontuação exata (`;`, `{ }`), diferenciação de maiúsculas/minúsculas e compilação no GCC para gerar código executável.

---

## 2. Gabarito da Checagem Independente (`A02-C01` a `A02-C03`)

### `A02-C01` *(Diagnóstico de erros de sintaxe no papel)*
1. **Falta `;` após `printf("Linha 1\n")`:** toda instrução de chamada em C deve terminar com ponto-e-vírgula.
2. **`print("Linha 2\n");` inválido:** a função `print` não existe em `<stdio.h>`; a função correta é `printf`.
3. **`Return 0;` inválido:** `R` maiúsculo viola o *case-sensitive* da palavra reservada `return`.

### `A02-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. Comentário `/* Inicio do programa` não foi fechado com `*/`, engolindo `#include <stdio.h>` e todo o programa.
  2. `int Main(void)` escreve `Main` com `M` maiúsculo; em C (*case-sensitive*), o ponto de entrada exigido pelo ligador é `main`.
  3. `// printf("Status: OK\n");` está comentada com `//`, sendo ignorada pelo compilador e omitindo a segunda linha da saída.
  4. Falta `;` após `return 0`.
- **Solução corrigida completa:** [A02_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A02_C02_corrigido.c)
```c
/* Inicio do programa */
#include <stdio.h>

int main(void) {
    printf("Sistema pronto\n");
    printf("Status: OK\n");
    return 0;
}
```

### `A02-C03` *(Programa mínimo compilável do zero)*
Arquivo: [A02_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/solucoes/A02_C03.c)
```c
/* Checagem A02-C03: Programa minimo compilavel em C99 */
#include <stdio.h>

int main(void) {
    printf("Compilacao limpa\n");
    printf("Execucao concluida\n");
    return 0;
}
```
- **Comandos de compilação e execução no Linux:**
  ```bash
  gcc -std=c99 -Wall -Wextra A02_C03.c -o app
  ./app
  ```
