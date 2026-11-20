# Bloco `G04` — Recursão Linear em Vetores 1D: Redução por Tamanho (`n - 1`)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio G — Recursividade e Pilha de Execução / **`G04`** |
| **Micro-habilidade foco** | Implementar funções recursivas lineares sobre vetores `const int v[]` mantendo `v` fixo, reduzindo o tamanho lógico (`n - 1`) até `n == 0` e combinando `v[n - 1]` no retorno, sem laços. |
| **Pré-requisitos** | `G03` *(Recursão Linear sobre Inteiros e Decomposição Decimal)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem (24 min):** `14 min` resol. \| `6 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C03`, 16 min):** `11 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Proibição estrita de `for`, `while` e `do-while` em funções recursivas** (laços são permitidos apenas em `main` para ler os dados de teste do vetor). Use capacidade fixa (`int v[50]`), `const int v[]` e redução `n - 1`. **Não utilize** aritmética de ponteiros (`v + 1`), parada antecipada (`contem`), máximo com variável local única ou média recursiva (`G05`), strings (`G06`), `struct`, `malloc`/`free` ou VLAs. Saídas estritamente em ASCII puro. |

### Registro da Sessão (Preenchido na Prática)
- **Sessão (`E01`–`E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 5` | **Após corr.:** `___ / 5`
- **Checagem Independente (`C01`–`C03`, sem gabarito):** `___ / 3` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Redução pelo tamanho (`n - 1`) sem copiar o vetor:** Em C, ao chamar `func(v, n - 1)`, o vetor **não é copiado**: todas as ativações recebem o mesmo endereço inicial `&v[0]` e apenas o tamanho lógico `n` diminui (`n`, `n - 1`, `...`, `0`).
2. **Decomposição em `v[0..n-1]`:** Para resolver o problema nos `n` primeiros elementos, combine o **último elemento válido `v[n - 1]`** com o resultado recursivo do subvetor `v[0..n-2]` de tamanho `n - 1`:
   - **Caso base:** `if (n <= 0) return 0;` (vetor vazio tem soma `0` e contagem `0`).
   - **Passo recursivo:** `return v[n - 1] + soma(v, n - 1);`
3. **Regra obrigatória de segurança (`n == 0` ANTES de `v[n - 1]`):** Sempre verifique `if (n <= 0)` (ou `if (n == 0)`) **antes** de ler `v[n - 1]`. Acessar `v[n]` (fora do intervalo `0..n-1`) ou ler `v[n - 1]` antes de testar `n <= 0` (gerando `v[-1]`) provoca **comportamento indefinido**.
4. **Contagem filtrada no retorno:** Para contar elementos que satisfazem uma condição `C(v[n - 1])`:
   ```c
   if (n <= 0) return 0;
   if (C(v[n - 1])) return 1 + contar(v, n - 1);
   return contar(v, n - 1);
   ```

---

## 2. Exemplos Guiados

### Exemplo 1 — Soma recursiva de vetor e rastreamento para `v = {4, 7, 2}`, `n = 3` *(Trecho ilustrativo)*
```c
int soma_vetor(const int v[], int n) {
    if (n <= 0) {
        return 0;
    }
    return v[n - 1] + soma_vetor(v, n - 1);
}
```
- **Descida:**
  - `soma_vetor(v, 3)` → `v[2]` (`2`) `+ soma_vetor(v, 2)`
  - `soma_vetor(v, 2)` → `v[1]` (`7`) `+ soma_vetor(v, 1)`
  - `soma_vetor(v, 1)` → `v[0]` (`4`) `+ soma_vetor(v, 0)`
  - `soma_vetor(v, 0)` → atinge `n <= 0` e retorna `0`
- **Subida:** `0` → `4 + 0 = 4` → `7 + 4 = 11` → `2 + 11 = 13`.

### Exemplo 2 — Contagem condicional com `const int v[]` *(Programa completo)*
```c
#include <stdio.h>

int contar_pares(const int v[], int n);

int main(void) {
    int n, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    printf("Pares: %d\n", contar_pares(v, n));
    return 0;
}

int contar_pares(const int v[], int n) {
    if (n <= 0) {
        return 0;
    }
    if (v[n - 1] % 2 == 0) {
        return 1 + contar_pares(v, n - 1);
    }
    return contar_pares(v, n - 1);
}
```
Observe: o `for` aparece **somente em `main`** para carregar a entrada; `contar_pares` é 100% recursiva, usa `const int v[]` e testa `n <= 0` antes de acessar `v[n - 1]`.

---

## 3. Exercícios (`G04-E01` a `G04-E05`)

### `G04-E01` *(Teste de mesa — Reprodução do modelo — Papel)*
Sem utilizar computador, acompanhe `calcular(v, 3)` para `int v[3] = {5, 2, 7};`:
```c
int calcular(const int v[], int n) {
    if (n <= 0) {
        return 0;
    }
    if (v[n - 1] % 2 != 0) {
        return v[n - 1] + calcular(v, n - 1);
    }
    return calcular(v, n - 1);
}
```
**(a)** Liste cada chamada empilhada na descida, indicando qual elemento `v[n - 1]` é inspecionado em cada quadro.  
**(b)** Mostre todos os valores devolvidos na subida da pilha até o resultado final.

---

### `G04-E02` *(Completar lacunas — Contagem condicional em vetor — Papel)*
Complete as lacunas `/* A */`, `/* B */` e `/* C */` na função recursiva abaixo para contar quantos elementos estritamente negativos existem em `v[0..n-1]`:
```c
int contar_negativos( /* A */ , int n) {
    if ( /* B */ ) {
        return 0;
    }
    if ( /* C */ ) {
        return 1 + contar_negativos(v, n - 1);
    }
    return contar_negativos(v, n - 1);
}
```

---

### `G04-E03` *(Caça ao Bug — Programa completo `.c`)*
O programa abaixo deveria ler `n` (`0 <= n <= 50`) e `n` inteiros, e imprimir a soma apenas dos elementos positivos (`> 0`). Identifique os **2 bugs** em `soma_positivos`, explique-os em comentários `//` diretamente no código e escreva a versão corrigida completa sem laços na função recursiva:

```c
#include <stdio.h>

int soma_positivos(const int v[], int n);

int main(void) {
    int n, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    printf("Soma positivos: %d\n", soma_positivos(v, n));
    return 0;
}

int soma_positivos(const int v[], int n) {
    if (n == 1) {
        return v[0];
    }
    if (v[n] > 0) {
        return v[n] + soma_positivos(v, n - 1);
    }
    return soma_positivos(v, n - 1);
}
```

---

### `G04-E04` *(Variação controlada com pistas — Programa completo `.c`)*
Escreva um **programa completo** em C com protótipos antes de `main` e funções recursivas **sem laços** para:
- `int contar_positivos(const int v[], int n)` — conta quantos elementos em `v[0..n-1]` são estritamente maiores que `0`.
- `int soma_pares(const int v[], int n)` — soma os elementos pares em `v[0..n-1]` (incluindo pares negativos; note que `0` é par e soma `0`).

No `main`, leia `n` (`0 <= n <= 50`) e os `n` inteiros em `int v[50]`, e imprima exatamente:
```text
Positivos: P
Soma pares: S
```
*Pista:* Ambas as funções usam `if (n <= 0) return 0;` antes de acessar `v[n - 1]`.

---

### `G04-E05` *(Resolução independente — Contagem de ocorrências sem laços `.c`)*
Escreva um **programa completo** em C contendo o protótipo e a implementação recursiva (sem laços) da função:
```c
int contar_ocorrencias(const int v[], int n, int x);
```
que retorna quantas vezes o valor `x` aparece em `v[0..n-1]`. No `main`, leia `n` (`0 <= n <= 50`), leia os `n` inteiros para `v`, leia `x` e imprima exatamente:
```text
Ocorrencias: K
```

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `G04-C01` *(Rastreamento de vetor de 4 elementos — Papel)*
Sem usar computador, rastreie `soma_multiplos(v, 4, 3)` para `int v[4] = {3, 10, 6, 5};`, mostrando todas as chamadas empilhadas, o elemento testado em cada passo e cada valor devolvido na subida:
```c
int soma_multiplos(const int v[], int n, int k) {
    if (n <= 0) {
        return 0;
    }
    if (v[n - 1] % k == 0) {
        return v[n - 1] + soma_multiplos(v, n - 1, k);
    }
    return soma_multiplos(v, n - 1, k);
}
```

### `G04-C02` *(Caça ao Bug `v[n]` e ordem do caso base — Programa completo `.c`)*
O programa abaixo lê `n` (`0 <= n <= 50`), `n` inteiros e `lim`, e deveria contar quantos elementos são estritamente maiores que `lim`. Identifique e corrija os erros de acesso fora dos limites e de ordem do caso base em `contar_acima`:
```c
#include <stdio.h>

int contar_acima(const int v[], int n, int lim);

int main(void) {
    int n, lim, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &lim);
    printf("Acima: %d\n", contar_acima(v, n, lim));
    return 0;
}

int contar_acima(const int v[], int n, int lim) {
    int ult = v[n];
    if (n <= 0) {
        return 0;
    }
    if (ult > lim) {
        return 1 + contar_acima(v, n - 1, lim);
    }
    return contar_acima(v, n - 1, lim);
}
```

### `G04-C03` *(Função recursiva em vetor compilada sem laços — Programa completo `.c`)*
Escreva um **programa completo** em C com protótipo antes de `main` e implementação recursiva (sem laços) para:
```c
int soma_intervalo_vetor(const int v[], int n, int min_val, int max_val);
```
que retorna a soma de todos os elementos `v[i]` (`0 <= i < n`) que satisfazem `min_val <= v[i] && v[i] <= max_val`. No `main`, leia `n` (`0 <= n <= 50`), os `n` inteiros, `min_val` e `max_val`, e imprima exatamente:
```text
Soma no intervalo: S
```

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `G05` (`Recursão em Vetores: Parada Antecipada, Máximo e Média`):** somente após autocorreção de `G04-E01..E05` e **100% (3/3)** na Checagem Independente `G04-C01..C03` sem gabarito.
- **Recuperação direcionada (1ª falha):** desenhar o vetor `v[0..n-1]` destacando a posição `v[n - 1]` e o subvetor `v[0..n-2]`, conferir que `if (n <= 0)` aparece **sempre na 1ª linha** da função e aplicar variante `V2` de `G04`.
- **Após 2 tentativas malsucedidas:** parar repetição e investigar os pré-requisitos **`G03`** (recursão linear sem laços) e **`F06`** (parâmetro `const int v[]` e limites `0..n-1`).

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 10 — recursão: definições e exemplos).
- `[DOC]` `Aula_22_Algoritmos.pdf` p. 23–28, 33–34 (recursão em vetores por redução `n - 1`, `soma`, `contar`).
- `[DOC]` `Lista11_Algoritmos.pdf` p. 1–2 (Ex. 2 — teste de mesa `calcular(v, 3)`; Ex. 5 — `contar_positivos`; Ex. 6 — entrega `contar_ocorrencias`).
- Casos de teste e soluções verificáveis: [G04_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/gabaritos/G04_gabarito.md) e [G04_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_G/testes/G04_testes.md).
