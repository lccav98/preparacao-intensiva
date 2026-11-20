# Bloco `G06` — Recursão em Strings por Índice Crescente (`i + 1` até `'\0'`) e Impressão no Retorno

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio G — Recursividade e Pilha de Execução / **`G06`** |
| **Micro-habilidade foco** | Percorrer e comparar strings recursivamente avançando o índice `i + 1` até o terminador `'\0'`, aplicando acumulação booleana ou processamento no retorno das chamadas. |
| **Pré-requisitos** | `G03`, `G04` *(Recursão linear sobre inteiros e sobre vetores 1D sem laços)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão única de prática + checagem (22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **PROIBIÇÃO DE LAÇOS EM FUNÇÕES RECURSIVAS:** nenhuma função recursiva pode conter `for`, `while` ou `do-while` (laços são permitidos apenas na `main`, se necessários para leitura/limpeza de `fgets`). **Não utilize** dois índices convergentes ou modificação *in-place* (`G07`), recursão dupla (`G08`), `<string.h>`, `struct`, alocação dinâmica (`malloc`/`free`), `gets(` ou VLAs. Use `const char []` em toda função de leitura e saídas em ASCII puro. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão Única (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Índice crescente (`int i`) até `'\0'`:** Como strings em C terminam em `'\0'`, não precisamos passar o tamanho `n`. Passamos `int i` começando em `0` na chamada inicial (`func(s, 0)`) e avançamos com `i + 1` até atingir o caso base **`if (s[i] == '\0')`**.
2. **Contagem com expressão booleana:** A expressão `(s[i] == c)` vale `1` se verdadeiro e `0` se falso. Assim, uma contagem recursiva fica enxuta:
   ```c
   int contar(const char s[], int i, char c) {
       if (s[i] == '\0') return 0;
       return (s[i] == c) + contar(s, i + 1, c);
   }
   ```
3. **Impressão inversa no retorno (pós-recursão):** Para exibir a string ao contrário **sem modificá-la**, empilhe até `'\0'` chamando `imprimir_inversa(s, i + 1);` **antes** de `printf("%c", s[i]);`. Ao desempilhar, o último caractere válido é impresso primeiro.
4. **Comparação de duas strings (`iguais`):**
   - Teste primeiro `if (a[i] != b[i]) return 0;` — isso resolve automaticamente strings de tamanhos diferentes, pois `'\0'` é diferente de qualquer caractere válido!
   - Só depois teste `if (a[i] == '\0') return 1;` (se `a[i] == b[i]` e `a[i] == '\0'`, ambas terminaram juntas).
   - Caso contrário, retorne `iguais(a, b, i + 1)`.
5. **Proteção com `const char []`:** Toda função que apenas lê a string deve declarar `const char s[]`. Nunca use `i++` na chamada recursiva (`contar(s, i++, c)` repassa `i` antigo e causa *stack overflow*).

---

## 2. Exemplos Guiados

### Exemplo 1 — Comprimento e contagem por índice crescente *(Trecho ilustrativo)*
```c
int comprimento(const char s[], int i) {
    if (s[i] == '\0') {
        return 0;
    }
    return 1 + comprimento(s, i + 1);
}
```
Rastreamento de `comprimento("SOL", 0)`:
- `i = 0` (`'S'`): `1 + comprimento("SOL", 1)`
- `i = 1` (`'O'`): `1 + comprimento("SOL", 2)`
- `i = 2` (`'L'`): `1 + comprimento("SOL", 3)`
- `i = 3` (`'\0'`): retorna **`0`** → desempilha: `1 + 0 = 1` → `1 + 1 = 2` → `1 + 2 = 3`.

### Exemplo 2 — Impressão inversa no retorno e comparação segura *(Programa parcial)*
```c
void imprimir_inversa(const char s[], int i) {
    if (s[i] == '\0') {
        return;
    }
    imprimir_inversa(s, i + 1); /* desce ate '\0' */
    printf("%c", s[i]);           /* imprime somente no retorno */
}
```
Rastreamento de `imprimir_inversa("CASA", 0)`:
- Descida (empilhamento): `i=0('C') -> i=1('A') -> i=2('S') -> i=3('A') -> i=4('\0' retorna)`
- Subida (desempilhamento): imprime `'A'`, depois `'S'`, depois `'A'`, depois `'C'` → saída: **`ASAC`**.

---

## 3. Exercícios (`G06-E01` a `G06-E05`)

### `G06-E01` *(Teste de Mesa — Índice crescente e pós-recursão sem computador)*
Sem usar computador, rastreie manualmente o programa abaixo:

```c
#include <stdio.h>

int contar(const char s[], int i, char c);
void imprimir_inversa(const char s[], int i);

int main(void) {
    char p1[] = "ABA";
    char p2[] = "CASA";
    printf("Qtd=%d\n", contar(p1, 0, 'A'));
    imprimir_inversa(p2, 0);
    printf("\n");
    return 0;
}

int contar(const char s[], int i, char c) {
    if (s[i] == '\0') {
        return 0;
    }
    return (s[i] == c) + contar(s, i + 1, c);
}

void imprimir_inversa(const char s[], int i) {
    if (s[i] == '\0') {
        return;
    }
    imprimir_inversa(s, i + 1);
    printf("%c", s[i]);
}
```
**(a)** Mostre a cadeia de chamadas e retornos de `contar("ABA", 0, 'A')` (valores em `i = 0, 1, 2, 3`).  
**(b)** Qual é a saída exata impressa por `main`, linha por linha? Qual é o primeiro caractere impresso por `imprimir_inversa("CASA", 0)` e em qual momento da pilha ele é exibido?

---

### `G06-E02` *(Completar solução — Comparação de strings com comprimentos diferentes)*
Complete as lacunas `/* A */`, `/* B */`, `/* C */` e `/* D */` na função `iguais` abaixo:

```c
#include <stdio.h>

int iguais(/* A */ a[], const char b[], int i);

int main(void) {
    char a[50], b[50];
    scanf("%49s %49s", a, b);
    if (iguais(a, b, 0)) {
        printf("Iguais\n");
    } else {
        printf("Diferentes\n");
    }
    return 0;
}

int iguais(/* A */ a[], const char b[], int i) {
    if (/* B */) {
        return 0;
    }
    if (/* C */) {
        return 1;
    }
    return /* D */;
}
```
**(e)** Explique passo a passo por que a função completa retorna `0` ao comparar `"SOL"` e `"SOLAR"`.

---

### `G06-E03` *(Caça ao Bug — Programa completo)*
O programa completo abaixo deveria ler uma linha de texto `s` e um caractere `c`, e imprimir `Ocorrencias: K` e `Inversa: <texto_invertido>` **sem usar laços nas funções recursivas**. Identifique os **3 bugs intencionais** no código, corrija o programa completo e explique cada correção usando **comentários `//`**:

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
    return (s[i] == c) + contar_caractere(s, i++, c);
}

void imprimir_inversa(const char s[], int i) {
    if (s[i] == '\0') {
        return;
    }
    printf("%c", s[i]);
    imprimir_inversa(s, i + 1);
}
```

---

### `G06-E04` *(Variação controlada com pistas — Vogais e impressão inversa)*
Escreva um **programa completo** em C99 (sem laços nas funções recursivas) com protótipos antes de `main`:
- `int contar_vogais(const char s[], int i);` — conta quantas vogais (`'a','e','i','o','u'`, maiúsculas ou minúsculas) há em `s` a partir do índice `i`.
- `void imprimir_inversa(const char s[], int i);` — imprime `s` de trás para frente **sem modificar o vetor `s`**.

No `main`, leia uma linha em `char s[100]` com `fgets` (removendo `'\n'`/`'\r'`), e imprima exatamente:
```text
Vogais: V
Inversa: <texto_invertido>
```
*Pista:* Em `imprimir_inversa`, chame `imprimir_inversa(s, i + 1)` antes de `printf("%c", s[i])`.

---

### `G06-E05` *(Resolução independente — Comprimento e comparação recursiva)*
Escreva um **programa completo** em C99 (sem laços nas funções recursivas e sem `<string.h>`) usando `const char []`:
- `int comprimento(const char s[], int i);`
- `int iguais(const char a[], const char b[], int i);`

No `main`, leia duas palavras `char a[50], b[50];` com `scanf("%49s %49s", a, b);` e imprima exatamente:
```text
Comp A: LA
Comp B: LB
Iguais: Sim
```
*(ou `Iguais: Nao` quando forem diferentes).*

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `G06-C01` *(Teste de Mesa sem Compilar)*
Sem usar computador, rastreie o programa abaixo e escreva a saída exata:
```c
#include <stdio.h>

void filtrar_retorno(const char s[], int i) {
    if (s[i] == '\0') {
        return;
    }
    filtrar_retorno(s, i + 1);
    if (i % 2 == 0) {
        printf("%c", s[i]);
    }
}

int main(void) {
    filtrar_retorno("CODE", 0);
    printf("\n");
    return 0;
}
```
**(a)** Qual linha exata é impressa no terminal?  
**(b)** Em que ordem os índices `i` são verificados no `if (i % 2 == 0)`?

### `G06-C02` *(Diagnóstico em comparação de strings)*
Um aluno escreveu a função abaixo para verificar se duas strings são iguais:
```c
int iguais_bug(const char a[], const char b[], int i) {
    if (a[i] == '\0' || b[i] == '\0') {
        return 1;
    }
    if (a[i] != b[i]) {
        return 0;
    }
    return iguais_bug(a, b, i + 1);
}
```
**(a)** O que `iguais_bug("AB", "ABC", 0)` retorna e por que isso está errado?  
**(b)** Reescreva `iguais` corretamente com `const char []` tratando comprimentos diferentes.

### `G06-C03` *(Programa completo independente)*
Escreva um **programa completo** em C99 (sem laços dentro das funções recursivas) com:
- `int contar_digitos_str(const char s[], int i);` — conta quantos caracteres de `'0'` a `'9'` existem em `s`.
- `int tem_caractere(const char s[], int i, char c);` — retorna `1` se `c` aparece em `s` (com parada antecipada ao encontrar) e `0` caso contrário.

No `main`, leia uma linha em `char s[100]` com `fgets` (removendo `'\n'`/`'\r'`) e um caractere não-espaço `c` com `scanf(" %c", &c);`. Imprima exatamente:
```text
Digitos: D
Contem: Sim
```
*(ou `Contem: Nao` se ausente).*

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `G07` (`Recursão em Strings com Dois Índices i, j e Modificação In-Place Sem Laços`):** somente após autocorreção de `G06-E01..E05` e **100% (3/3)** na Checagem Independente `G06-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** revisar a diferença entre executar antes e após a chamada recursiva (`G02`), conferir que o caso base testa `s[i] == '\0'` antes de qualquer acesso e aplicar variante `V2` de `G06`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`G02`** (pré vs. pós-recursão na pilha), **`G03`** (recursão linear sem laços) e **`D06`** (terminador `'\0'` em strings).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (itens 9 e 10 — modularização e recursão).
- `[DOC]` `Aula_23_Algoritmos.pdf` p. 4–8, 15 (recursão em strings por índice crescente, impressão no retorno e `iguais`, com correção metodológica aplicando `const char []`).
- `[DOC]` `Lista12_Algoritmos.pdf` p. 1–2 (Ex. 1 — entrega, Ex. 2, Ex. 3).
- Casos de teste e soluções verificáveis: [G06_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/gabaritos/G06_gabarito.md) e [G06_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/G06_testes.md).
