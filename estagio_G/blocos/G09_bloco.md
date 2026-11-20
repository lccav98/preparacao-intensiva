# Bloco `G09` — Revisão e Consolidação do Estágio G *(Bloco de Revisão)*

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio G — Recursividade e Pilha de Execução / **`G09`** |
| **Micro-habilidade foco** | *(Revisão integrada de `G01` a `G08`)* Consolidar rastreamento de pilha pré/pós-chamada e árvore de chamadas, recursão linear sobre inteiros, vetores (`n - 1` com chamada única) e strings (`i + 1` e `i, j` *in-place*) sem laços, além de divisão pela metade (`n / 2`). |
| **Pré-requisitos** | `G05`, `G07`, `G08` *(Recursão em vetores com máximo/média, strings in-place e recursão múltipla vs. `n / 2`)* |
| **Tempo estimado** *(sujeito à calibração)* | **2 sessões de prática + checagem** — **Sessão 1 (`E01`–`E03`, 22 min):** `14 min` resol. \| `5 min` corr. \| `3 min` recup.; **Sessão 2 (`E04`–`E06`, 23 min):** `14 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 18 min):** `13 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Conteúdo novo: NENHUM.** **PROIBIÇÃO DE LAÇOS EM FUNÇÕES RECURSIVAS:** nenhuma função recursiva pode conter `for`, `while` ou `do-while` (laços são permitidos apenas na `main` para leitura ou limpeza de `fgets`). **Não utilize** `struct`, alocação dinâmica (`malloc`/`free`), `gets(` ou VLAs. Use `const` em funções de leitura, evite chamadas recursivas duplicadas em `maior`/`potencia_rapida` e mantenha saídas em ASCII puro. |

### Registro das Sessões (Preenchido na Prática)
- **Sessão 1 (`E01`–`E03`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Sessão 2 (`E04`–`E06`) — Data:** `____/____/______` | **Tempo:** `___ min` | **1ª tent.:** `___ / 3` | **Após corr.:** `___ / 3`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Apto para Estágio H`)

---

## 1. Instruções Curtas (Matriz de Consolidação do Estágio G)

1. **Pilha de execução e ordem pré vs. pós-recursão (`G01`–`G02`):**
   - Toda função recursiva precisa de **caso base**, **passo recursivo** e **progresso estrito** até o caso base.
   - Instruções **antes** da chamada recursiva executam na descida (ida); instruções **após** a chamada executam na subida (retorno/desempilhamento).
2. **Recursão linear sobre inteiros (`G03`):**
   - Decomposição decimal usa `n % 10` e `n / 10`. Atenção ao caso base para entrada `0`: `contar_digitos(0)` retorna **`1`** (`if (n < 10) return 1;`), enquanto `soma_digitos(0)` retorna **`0`** (`if (n == 0) return 0;`).
3. **Recursão em vetores 1D `n - 1` (`G04`–`G05`):**
   - Teste `if (n == 0)` **antes** de acessar `v[n - 1]` (evita acesso inválido a `v[-1]`).
   - Em `maior` e `media`, use caso base `n == 1` (`v[0]`). Em `maior`, **guarde** `int m = maior(v, n - 1);` em variável local para nunca duplicar a chamada!
4. **Recursão em strings `i + 1` e `i, j` *in-place* (`G06`–`G07`):**
   - Leitura usa `const char s[]` e para em `s[i] == '\0'`.
   - Dois índices convergentes (`i`, `j`) exigem **`if (i >= j)`** (cobre tamanhos pares, ímpares e vazios).
   - Remoção *in-place* com leitura `i` e escrita `j` trata ocorrências adjacentes e grava `s[j] = '\0';` no caso base, sem laços nem vetor auxiliar.
5. **Recursão múltipla vs. divisão `n / 2` (`G08`):**
   - `fibonacci` exige dois casos base (`n == 0` e `n == 1`) e gera árvore exponencial com recomputações.
   - `potencia_rapida` usa `double p = potencia_rapida(x, n / 2);` (1 chamada por nível → custo logarítmico).

---

## 2. Exemplos Guiados

### Exemplo 1 — Pré/pós-recursão e `maior` com chamada única *(Trecho ilustrativo)*
```c
void pulso(int n) {
    if (n == 0) {
        return;
    }
    printf("<%d ", n);   /* pre-recursao (ida) */
    pulso(n - 1);
    printf("%d> ", n);   /* pos-recursao (retorno) */
}
/* pulso(3) imprime: <3 <2 <1 1> 2> 3> */

int maior_vetor(const int v[], int n) {
    if (n == 1) {
        return v[0];
    }
    int m = maior_vetor(v, n - 1); /* chamada unica evita O(2^n) */
    return (v[n - 1] > m) ? v[n - 1] : m;
}
```

### Exemplo 2 — Remoção *in-place* em string + divisão pela metade *(Trecho ilustrativo)*
```c
void remover_char(char s[], int i, int j, char c) {
    if (s[i] == '\0') {
        s[j] = '\0';
        return;
    }
    if (s[i] != c) {
        s[j] = s[i];
        remover_char(s, i + 1, j + 1, c);
    } else {
        remover_char(s, i + 1, j, c);
    }
}

double potencia_rapida(double x, int n) {
    if (n == 0) return 1.0;
    if (n == 1) return x;
    double p = potencia_rapida(x, n / 2);
    return (n % 2 == 0) ? (p * p) : (x * p * p);
}
```

---

## 3. Exercícios (`G09-E01` a `G09-E06`)

### Sessão 1 (`G09-E01` a `G09-E03` — Rastreamento e Diagnóstico de Bugs)

### `G09-E01` *(Teste de Mesa Integrado — Pilha pré/pós + Árvore curta)*
Sem usar computador, rastreie os dois trechos abaixo:
- **(a)** Qual é a saída exata impressa por `eco(3)`?
  ```c
  void eco(int n) {
      if (n <= 0) {
          printf("0\n");
          return;
      }
      printf("%d ", n);
      eco(n - 1);
      printf("%d ", n);
  }
  ```
- **(b)** Para a função abaixo, desenhe a árvore de chamadas de `f(4)`, informe o valor retornado e quantas chamadas à função `f` ocorrem no total:
  ```c
  int f(int n) {
      if (n == 0) return 1;
      if (n == 1) return 2;
      return f(n - 1) + f(n - 2);
  }
  ```

---

### `G09-E02` *(Diagnóstico de Armadilhas Recursivas — Sem Compilar)*
Identifique o erro específico em cada código e escreva a correção exata:
1. ```c
   int maior(const int v[], int n) {
       if (n == 1) return v[0];
       if (v[n - 1] > maior(v, n - 1)) return v[n - 1];
       return maior(v, n - 1);
   }
   ```
2. ```c
   int soma_positivos(const int v[], int n) {
       int parcela = (v[n - 1] > 0) ? v[n - 1] : 0;
       if (n == 0) return 0;
       return parcela + soma_positivos(v, n - 1);
   }
   ```
3. ```c
   int contar_letra(const char s[], int i, char c) {
       int cont = 0;
       for (int k = i; s[k] != '\0'; k++) {
           if (s[k] == c) cont++;
       }
       return cont;
   }
   ```

---

### `G09-E03` *(Caça ao Bug Integrada — Programa completo)*
O programa completo abaixo deveria ler uma linha `s`, um inteiro `num >= 0`, um tamanho `n` (`1 <= n <= 50`) e `n` inteiros em `v`, e imprimir `Soma digitos: S`, `Maior: M` e `Invertida: <s_invertida>`. Identifique os **3 bugs intencionais**, corrija o programa completo (sem laços nas funções recursivas) e documente cada correção com **comentários `//`**:

```c
#include <stdio.h>

int soma_digitos(int n);
int maior_vetor(const int v[], int n);
int comprimento(const char s[], int i);
void inverter(char s[], int i, int j);

int main(void) {
    char s[100];
    int num, n, v[50];

    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }
    scanf("%d %d", &num, &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int len = comprimento(s, 0);
    inverter(s, 0, len - 1);

    printf("Soma digitos: %d\n", soma_digitos(num));
    printf("Maior: %d\n", maior_vetor(v, n));
    printf("Invertida: %s\n", s);
    return 0;
}

int soma_digitos(int n) {
    if (n == 0) {
        return 1;
    }
    return (n % 10) + soma_digitos(n / 10);
}

int maior_vetor(const int v[], int n) {
    if (n == 0) {
        return 0;
    }
    if (v[n - 1] > maior_vetor(v, n - 1)) {
        return v[n - 1];
    }
    return maior_vetor(v, n - 1);
}

int comprimento(const char s[], int i) {
    if (s[i] == '\0') {
        return 0;
    }
    return 1 + comprimento(s, i + 1);
}

void inverter(char s[], int i, int j) {
    if (i == j) {
        return;
    }
    char aux = s[i];
    s[i] = s[j];
    s[j] = aux;
    inverter(s, i + 1, j - 1);
}
```

---

### Sessão 2 (`G09-E04` a `G09-E06` — Implementação Integrada Pura)

### `G09-E04` *(Integração 1 — Vetores `const`, chamada única e média recursiva)*
Escreva um **programa completo** em C99 (sem laços nas funções recursivas) com:
- `int maior_vetor(const int v[], int n);` *(chamada única em variável local)*
- `double media_vetor(const int v[], int n);` *(recursiva, caso base `n == 1`)*
- `int contar_acima(const int v[], int n, double lim);` *(conta elementos estritamente maiores que `lim`)*

No `main`, leia `n` (`1 <= n <= 50`) e `n` inteiros em `v`, e imprima exatamente:
```text
Maior: M
Media: MED.MM
Acima da media: K
```

---

### `G09-E05` *(Integração 2 — Strings *in-place* e palíndromo sem laços)*
Escreva um **programa completo** em C99 (sem laços nas funções recursivas e sem vetor auxiliar) com:
- `void remover_char(char s[], int i, int j, char c);` *(remove `c` in-place e grava `'\0'`)*
- `int comprimento(const char s[], int i);`
- `int eh_palindromo(const char s[], int i, int j);`

No `main`, leia uma linha em `char s[100]` com `fgets` (removendo `'\n'`/`'\r'`) e um caractere `c` com `scanf(" %c", &c);`. Remova todas as ocorrências de `c` e verifique se a string resultante é palíndromo, imprimindo exatamente:
```text
Limpa: <string_limpa>
Comprimento: L
Palindromo: Sim
```
*(ou `Palindromo: Nao`).*

---

### `G09-E06` *(Integração 3 — Decomposição decimal e potenciação rápida `n / 2`)*
Escreva um **programa completo** em C99 (sem laços nas funções recursivas) com:
- `int contar_digitos(int n);` *(para `n >= 0`, `0` possui `1` dígito)*
- `int soma_digitos(int n);` *(para `n >= 0`)*
- `double potencia_rapida(double x, int n);` *(para `n >= 0`, com variável local `p`)*

No `main`, leia `int num` (`num >= 0`), `double x` e `int exp` (`exp >= 0`), e imprima exatamente:
```text
Digitos: D
Soma digitos: S
Potencia: P.PP
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `G09-C01` *(Teste de Mesa Integrado — Pilha pré/pós + Diagnóstico `n / 2`)*
1. Sem usar computador, escreva a saída exata impressa pela chamada `traco(4)`:
   ```c
   void traco(int n) {
       if (n == 0) {
           printf("|\n");
           return;
       }
       printf("[%d ", n);
       traco(n - 1);
       printf("%d] ", n);
   }
   ```
2. Explique o erro conceitual em escrever `return potencia_rapida(x, n / 2) * potencia_rapida(x, n / 2);` e mostre a forma correta com variável local.

### `G09-C02` *(Implementação Integrada — Vetor `const` sem laços)*
Escreva um **programa completo** em C99 (sem laços nas funções recursivas) com:
- `int soma_pares(const int v[], int n);` *(soma apenas os elementos pares de `v`)*
- `int contem(const int v[], int n, int x);` *(retorna `1` ou `0` com parada antecipada)*
- `double media_vetor(const int v[], int n);` *(recursiva)*

No `main`, leia `n` (`1 <= n <= 50`), `n` inteiros de `v` e um inteiro `x`. Imprima exatamente:
```text
Soma pares: SP
Media: MED.MM
Contem: Sim
```
*(ou `Contem: Nao`).*

### `G09-C03` *(Implementação Integrada — String *in-place* + impressão no retorno)*
Escreva um **programa completo** em C99 (sem laços nas funções recursivas e sem vetor auxiliar) com:
- `void remover_vogais(char s[], int i, int j);` *(remove `'a','e','i','o','u'` maiúsculas e minúsculas in-place)*
- `void imprimir_inversa(const char s[], int i);` *(imprime no retorno das chamadas)*

No `main`, leia uma linha em `char s[100]` com `fgets` (removendo `'\n'`/`'\r'`), remova as vogais e imprima exatamente:
```text
Sem vogais: <string_sem_vogais>
Inversa: <string_invertida>
```

---

## 5. Orientação de Avanço ou Recuperação (Conclusão do Estágio G)

- **Avançar para o Estágio H (`H01 — Arquitetura em 5 Arquivos PGM`):** somente após autocorreção de `G09-E01..E06` **e** **100% de acerto (3/3)** na Checagem Independente `G09-C01..C03` sem consulta ao gabarito.
- **Recuperação direcionada por sub-habilidade (1ª falha):**
  - Falha em rastreamento de pilha pré/pós-recursão $\rightarrow$ revisar **`G01`–`G02`**.
  - Falha em decomposição decimal ou uso proibido de laço $\rightarrow$ revisar **`G03`**.
  - Falha em `v[n - 1]`, caso base `n == 0`/`n == 1` ou dupla chamada em `maior` $\rightarrow$ revisar **`G04`–`G05`**.
  - Falha em `i + 1`, `i >= j` ou remoção *in-place* em strings $\rightarrow$ revisar **`G06`–`G07`**.
  - Falha em árvore de Fibonacci ou divisão `n / 2` em `potencia_rapida` $\rightarrow$ revisar **`G08`**.
- **Após 2 tentativas malsucedidas:** interromper novas tentativas em `G09`, diagnosticar qual pré-requisito (`G01`–`G08`) falhou e reabilitá-lo integralmente antes de refazer a checagem de conclusão do Estágio G.

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (itens 9 e 10 — pilha de execução e recursão).
- `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 5 (17/11 e 23/11).
- `[DOC]` `Aula_21`–`Aula_24` e `Lista11`–`Lista12` completas.
- Casos de teste e soluções verificáveis: [G09_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/gabaritos/G09_gabarito.md) e [G09_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/G09_testes.md).
