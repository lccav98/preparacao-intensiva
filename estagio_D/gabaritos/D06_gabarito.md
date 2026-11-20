# Gabarito Comentado — Bloco `D06` (Strings em C, Terminador `'\0'` e E/S Segura)

> **Bloco de referência:** [D06_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/blocos/D06_bloco.md)  
> **Nota para Caça ao Bug:** `D06-E03` e `D06-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`D06-E01` a `D06-E05`)

### `D06-E01` *(Leitura e Teste de Mesa)*
1. **Capacidade máxima útil:** `9` caracteres úteis (pela regra `N + 1`, pois `1` posição é reservada ao `'\0'`).
2. **Diferença ASCII:** `s[2]` recebe `'\0'` cujo código numérico é **`0`** (nulo, fim de string); `s[1]` recebe `'0'` cujo código numérico é **`48`** (o dígito zero visível).
3. **Saída exata:** `U0`. O `printf("%s\n", s)` imprime `s[0]` (`'U'`), `s[1]` (`'0'`) e encerra imediatamente ao encontrar `'\0'` em `s[2]`. O caractere `'!'` em `s[5]` permanece na memória após o terminador, mas nunca é exibido por `%s`.

---

### `D06-E02` *(Completar solução)*
- **`/* A */`:** `41` *(regra `N + 1` para 40 caracteres úteis + `'\0'`)*
- **`/* B */`:** `MAX`
- **`/* C */`:** `'\0'`
- **`/* D */`:** `'\0'`

---

### `D06-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `#define MAX_COD 15` viola a regra `N + 1`: para armazenar até 15 caracteres úteis + `'\0'`, o vetor precisa de tamanho `16` (`#define MAX_COD 16`).
  2. `scanf("%s", &codigo);` usa `&` indevidamente antes do nome do vetor (tipo incompatível) e omite o limite de tamanho `%15s`, abrindo risco de estouro de buffer. Correto: `scanf("%15s", codigo);`.
  3. `desc[i] = '0';` substitui `'\n'` pelo dígito `'0'` (ASCII `48`) em vez do terminador nulo `'\0'` (ASCII `0`), imprimindo um `0` extra ao final da descrição. Correto: `desc[i] = '\0';`.
- **Solução corrigida completa:** [D06_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D06_E03_corrigido.c)
```c
#include <stdio.h>
#define MAX_COD 16
#define MAX_DESC 51

int main(void) {
    char codigo[MAX_COD];
    char desc[MAX_DESC];
    int ch;

    scanf("%15s", codigo);
    while ((ch = getchar()) != '\n' && ch != EOF) {
    }

    fgets(desc, MAX_DESC, stdin);
    for (int i = 0; desc[i] != '\0'; i++) {
        if (desc[i] == '\n') {
            desc[i] = '\0';
            break;
        }
    }

    printf("Codigo: %s\nDesc: [%s]\n", codigo, desc);
    return 0;
}
```

---

### `D06-E04` *(Programa completo — Leitura de `tag` e `titulo`)*
Arquivo: [D06_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D06_E04.c)
```c
#include <stdio.h>
#define MAX_TAG 21
#define MAX_TITULO 61

int main(void) {
    char tag[MAX_TAG];
    char titulo[MAX_TITULO];
    int ch;

    scanf("%20s", tag);
    while ((ch = getchar()) != '\n' && ch != EOF) {
    }

    fgets(titulo, MAX_TITULO, stdin);
    for (int i = 0; titulo[i] != '\0'; i++) {
        if (titulo[i] == '\n') {
            titulo[i] = '\0';
            break;
        }
    }

    printf("Tag: %s\nTitulo: [%s]\n", tag, titulo);
    return 0;
}
```

---

### `D06-E05` *(Programa completo — Truncamento na primeira ocorrência de caractere)*
Arquivo: [D06_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D06_E05.c)
```c
#include <stdio.h>
#define MAX 81

int main(void) {
    char texto[MAX];
    char alvo;

    fgets(texto, MAX, stdin);
    for (int i = 0; texto[i] != '\0'; i++) {
        if (texto[i] == '\n') {
            texto[i] = '\0';
            break;
        }
    }

    scanf(" %c", &alvo);
    for (int i = 0; texto[i] != '\0'; i++) {
        if (texto[i] == alvo) {
            texto[i] = '\0';
            break;
        }
    }

    printf("Resultado: [%s]\n", texto);
    return 0;
}
```

---

## 2. Gabarito da Checagem Independente (`D06-C01` a `D06-C03`)

### `D06-C01` *(Teste de Mesa)*
1. **Saída exata:** `AL`.
2. **Valores numéricos:** `v[2]` armazena **`0`** (`'\0'`); se fosse `'0'`, armazenaria **`48`**.
3. **Pertinência de `'X'`:** Não pertence à string impressa. A leitura de `%s` encerra no primeiro `'\0'` (no índice `2`), ignorando qualquer caractere posterior na memória (`v[3]` e `v[4]`).

---

### `D06-C02` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. `#define MAX_SIGLA 10` não reserva espaço para `'\0'` em siglas de 10 caracteres úteis. Correto: `#define MAX_SIGLA 11`.
  2. `scanf("%s", &sigla);` utiliza `&` indevidamente e não limita a leitura. Correto: `scanf("%10s", sigla);`.
  3. Falta limpar o `'\n'` deixado no buffer pelo `scanf` antes de chamar `fgets(cidade, MAX_CIDADE, stdin)`, fazendo `fgets` ler apenas uma linha vazia. Correto: inserir `while ((ch = getchar()) != '\n' && ch != EOF) {}` antes do `fgets`.
- **Solução corrigida completa:** [D06_C02_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D06_C02_corrigido.c)
```c
#include <stdio.h>
#define MAX_SIGLA 11
#define MAX_CIDADE 31

int main(void) {
    char sigla[MAX_SIGLA];
    char cidade[MAX_CIDADE];
    int ch;

    scanf("%10s", sigla);
    while ((ch = getchar()) != '\n' && ch != EOF) {
    }

    fgets(cidade, MAX_CIDADE, stdin);
    for (int i = 0; cidade[i] != '\0'; i++) {
        if (cidade[i] == '\n') {
            cidade[i] = '\0';
            break;
        }
    }

    printf("Sigla: %s | Cidade: %s\n", sigla, cidade);
    return 0;
}
```

---

### `D06-C03` *(Programa completo — Matrícula, Nome e Disciplina)*
Arquivo: [D06_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_D/testes/solucoes/D06_C03.c)
```c
#include <stdio.h>
#define MAX_MAT 13
#define MAX_NOME 51
#define MAX_DISC 41

int main(void) {
    char mat[MAX_MAT];
    char nome[MAX_NOME];
    char disc[MAX_DISC];
    int ch;

    scanf("%12s", mat);
    while ((ch = getchar()) != '\n' && ch != EOF) {
    }

    fgets(nome, MAX_NOME, stdin);
    for (int i = 0; nome[i] != '\0'; i++) {
        if (nome[i] == '\n') {
            nome[i] = '\0';
            break;
        }
    }

    fgets(disc, MAX_DISC, stdin);
    for (int i = 0; disc[i] != '\0'; i++) {
        if (disc[i] == '\n') {
            disc[i] = '\0';
            break;
        }
    }

    printf("Matricula: %s\nNome: %s\nDisciplina: %s\n", mat, nome, disc);
    return 0;
}
```
