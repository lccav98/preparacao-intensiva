# Gabarito Comentado — Bloco `G06` (Recursão em Strings por Índice Crescente e Impressão no Retorno)

> **Bloco de referência:** [G06_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/blocos/G06_bloco.md)  
> **Nota para Caça ao Bug:** `G06-E03` e `G06-C02` no bloco do aluno contêm **erros intencionais** detalhados abaixo.

---

## 1. Gabarito dos Exercícios (`G06-E01` a `G06-E05`)

### `G06-E01` *(Teste de Mesa — Índice crescente e pós-recursão)*
- **(a)** Cadeia de chamadas e retornos de `contar("ABA", 0, 'A')`:
  - `i = 0` (`'A' == 'A'` → `1`): `1 + contar("ABA", 1, 'A')`
  - `i = 1` (`'B' == 'A'` → `0`): `0 + contar("ABA", 2, 'A')`
  - `i = 2` (`'A' == 'A'` → `1`): `1 + contar("ABA", 3, 'A')`
  - `i = 3` (`'\0'`): caso base retorna **`0`**
  - Retornos (desempilhamento): `1 + 0 = 1` → `0 + 1 = 1` → `1 + 1 = 2`.
- **(b)** Saída exata no terminal:
  ```text
  Qtd=2
  ASAC
  ```
  O primeiro caractere impresso por `imprimir_inversa("CASA", 0)` é **`'A'`** (índice `3`), exibido **no retorno da chamada `i = 3`**, logo após a chamada `i = 4` (`'\0'`) retornar.

### `G06-E02` *(Completar solução — `iguais`)*
- **`/* A */`:** `const char`
- **`/* B */`:** `a[i] != b[i]`
- **`/* C */`:** `a[i] == '\0'`
- **`/* D */`:** `iguais(a, b, i + 1)`
- **(e)** Em `"SOL"` vs. `"SOLAR"`: para `i = 0` (`'S'=='S'`), `i = 1` (`'O'=='O'`) e `i = 2` (`'L'=='L'`), a função avança. Em `i = 3`, `a[3]` é `'\0'` e `b[3]` é `'A'`. Como `'\0' != 'A'`, a condição `a[i] != b[i]` é verdadeira e retorna **`0`** imediatamente.

### `G06-E03` *(Caça ao Bug — Erros intencionais no enunciado)*
- **Erros intencionais:**
  1. Em `contar_caractere`, faltava o caso base `if (s[i] == '\0') return 0;`, causando leitura além do fim da string e recursão sem fim.
  2. Em `contar_caractere`, passava `i++` (pós-incremento envia o valor atual `i` sem somar `1`), mantendo `i = 0` em todas as chamadas e causando *stack overflow*. Deve passar `i + 1`.
  3. Em `imprimir_inversa`, `printf("%c", s[i]);` vinha antes da chamada recursiva, imprimindo na ordem direta em vez da ordem inversa no retorno.
- **Solução corrigida completa:** [G06_E03_corrigido.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G06_E03_corrigido.c)
```c
#include <stdio.h>

int contar_caractere(const char s[], int i, char c);
void imprimir_inversa(const char s[], int i);

int main(void) {
    char s[100], c;
    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }
    scanf(" %c", &c);

    printf("Ocorrencias: %d\n", contar_caractere(s, 0, c));
    printf("Inversa: ");
    imprimir_inversa(s, 0);
    printf("\n");
    return 0;
}

int contar_caractere(const char s[], int i, char c) {
    // Erro original 1: faltava o caso base para s[i] == '\0', lendo alem do fim da string.
    // Correcao: parar e retornar 0 ao encontrar o terminador '\0'.
    if (s[i] == '\0') {
        return 0;
    }
    // Erro original 2: passava i++ (pos-incremento), repetindo o mesmo indice i infinitamente.
    // Correcao: passar i + 1 para progredir ate '\0'.
    return (s[i] == c) + contar_caractere(s, i + 1, c);
}

void imprimir_inversa(const char s[], int i) {
    if (s[i] == '\0') {
        return;
    }
    // Erro original 3: imprimia s[i] antes da chamada recursiva (ordem direta).
    // Correcao: chamar recursivamente primeiro e imprimir s[i] no retorno (pos-recursao).
    imprimir_inversa(s, i + 1);
    printf("%c", s[i]);
}
```

### `G06-E04` *(Programa completo — Vogais e impressão inversa)*
Arquivo: [G06_E04.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G06_E04.c)
```c
#include <stdio.h>

int contar_vogais(const char s[], int i);
void imprimir_inversa(const char s[], int i);

int main(void) {
    char s[100];
    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }

    printf("Vogais: %d\n", contar_vogais(s, 0));
    printf("Inversa: ");
    imprimir_inversa(s, 0);
    printf("\n");
    return 0;
}

int contar_vogais(const char s[], int i) {
    if (s[i] == '\0') {
        return 0;
    }
    char c = s[i];
    int eh_vogal = (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
                    c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
    return eh_vogal + contar_vogais(s, i + 1);
}

void imprimir_inversa(const char s[], int i) {
    if (s[i] == '\0') {
        return;
    }
    imprimir_inversa(s, i + 1);
    printf("%c", s[i]);
}
```

### `G06-E05` *(Programa completo — Comprimento e comparação recursiva)*
Arquivo: [G06_E05.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G06_E05.c)
```c
#include <stdio.h>

int comprimento(const char s[], int i);
int iguais(const char a[], const char b[], int i);

int main(void) {
    char a[50], b[50];
    scanf("%49s %49s", a, b);

    printf("Comp A: %d\n", comprimento(a, 0));
    printf("Comp B: %d\n", comprimento(b, 0));
    if (iguais(a, b, 0)) {
        printf("Iguais: Sim\n");
    } else {
        printf("Iguais: Nao\n");
    }
    return 0;
}

int comprimento(const char s[], int i) {
    if (s[i] == '\0') {
        return 0;
    }
    return 1 + comprimento(s, i + 1);
}

int iguais(const char a[], const char b[], int i) {
    if (a[i] != b[i]) {
        return 0;
    }
    if (a[i] == '\0') {
        return 1;
    }
    return iguais(a, b, i + 1);
}
```

---

## 2. Gabarito da Checagem Independente (`G06-C01` a `G06-C03`)

### `G06-C01` *(Teste de Mesa)*
- **(a)** Saída exata: **`DC`** (em `"CODE"`, índices `0='C', 1='O', 2='D', 3='E'`; na volta da pilha, apenas `i=2` (`'D'`) e `i=0` (`'C'`) satisfazem `i % 2 == 0`).
- **(b)** Os índices são verificados na ordem inversa da pilha: `i = 3`, `i = 2`, `i = 1`, `i = 0`.

### `G06-C02` *(Diagnóstico em comparação de strings)*
- **(a)** `iguais_bug("AB", "ABC", 0)` retorna **`1`** (verdadeiro), o que está errado! Em `i = 2`, `a[2]` é `'\0'` e `b[2]` é `'C'`; como o primeiro `if` usa `||` (`a[i] == '\0' || b[i] == '\0'`), ele aceita o fim de apenas uma das strings como igualdade.
- **(b)** Versão corrigida:
```c
int iguais(const char a[], const char b[], int i) {
    if (a[i] != b[i]) {
        return 0;
    }
    if (a[i] == '\0') {
        return 1;
    }
    return iguais(a, b, i + 1);
}
```

### `G06-C03` *(Programa completo — Dígitos e busca em string)*
Arquivo: [G06_C03.c](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/solucoes/G06_C03.c)
```c
#include <stdio.h>

int contar_digitos_str(const char s[], int i);
int tem_caractere(const char s[], int i, char c);

int main(void) {
    char s[100], c;
    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }
    scanf(" %c", &c);

    printf("Digitos: %d\n", contar_digitos_str(s, 0));
    if (tem_caractere(s, 0, c)) {
        printf("Contem: Sim\n");
    } else {
        printf("Contem: Nao\n");
    }
    return 0;
}

int contar_digitos_str(const char s[], int i) {
    if (s[i] == '\0') {
        return 0;
    }
    int dig = (s[i] >= '0' && s[i] <= '9');
    return dig + contar_digitos_str(s, i + 1);
}

int tem_caractere(const char s[], int i, char c) {
    if (s[i] == '\0') {
        return 0;
    }
    if (s[i] == c) {
        return 1;
    }
    return tem_caractere(s, i + 1, c);
}
```
