# Bloco `C02` — Eliminação de Gauss e Substituição Regressiva

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio C — Sistemas Lineares, Escalonamento, Posto (`C_A, C_V`) e Parâmetros / **`C02`** |
| **Micro-habilidade foco** | Triangularizar a matriz ampliada $A$ de um sistema $n \times n$ apenas abaixo dos pivôs (Eliminação de Gauss) usando $L_{ij}$, $L_i(\alpha)$ e $L_j' = L_j + L_i(\alpha)$, e obter a solução exata por substituição regressiva. |
| **Pré-requisitos** | `C01` *(Equação linear, matriz ampliada e operações elementares $L$)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Prática (`C02-E01`–`C02-E05`, 22 min):** `14 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`C02-C01`–`C02-C03`, 14 min):** `10 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Proibido:** Regra de Cramer, Regra de Sarrus ou matriz adjunta. Na Eliminação de Gauss, zere **apenas abaixo** dos pivôs (sem reduzir acima da diagonal principal), finalize por **substituição regressiva** e mantenha frações irredutíveis exatas. |

### Registro da Sessão (Preenchido na Prática)
- **Protocolo:** `PREP-MV-C02-<VARIANTE>-T<TENTATIVA>-<HASH>`
- **Prática (`C02-E01`–`C02-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`C02-C01`–`C02-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Objetivo da Eliminação de Gauss:** transformar o sistema $n \times n$ em um sistema equivalente **triangular superior** (zeros abaixo da diagonal principal), sem a necessidade de zerar acima dos pivôs nem forçar pivôs iguais a $1$ na última etapa.
2. **Roteiro em 2 fases:**
   - **Fase 1 (Escalonamento descendente):** para cada coluna $j = 1, \dots, n-1$:
     1. Se o pivô $a_{jj} = 0$, aplique $L_{jk}$ com alguma linha $k > j$ que tenha elemento não nulo na coluna $j$.
     2. *(Opcional, quando facilita a aritmética)* Aplique $L_j(1/a_{jj})$ para tornar o pivô igual a $1$.
     3. Para cada linha $i > j$, zere $a_{ij}$ via $L_i' = L_i + L_j(-a_{ij}/a_{jj})$.
   - **Fase 2 (Substituição regressiva / retro-substituição):**
     1. Resolva a última equação para $x_n$.
     2. Substitua $x_n$ na penúltima equação para encontrar $x_{n-1}$, subindo até $x_1$.
3. **Conferência obrigatória:** substitua a terna/quadra encontrada em uma equação do sistema original que não tenha sido usada por último no isolamento.

---

## 2. Exemplos Guiados

### Exemplo 1 — Modelo da Apostila (`MAT121_Sistemas` p. 9–12)
Resolver por Eliminação de Gauss:
$$\begin{cases} 2x + 4y - 6z = 10 \\ 4x + 2y + 2z = 16 \\ 2x + 8y - 4z = 24 \end{cases}$$
1. **Matriz ampliada e troca estratégica:**
   $$A = \left[\begin{array}{ccc|c} 2 & 4 & -6 & 10 \\ 4 & 2 & 2 & 16 \\ 2 & 8 & -4 & 24 \end{array}\right] \xrightarrow{L_{23},\; L_1(1/2)} \left[\begin{array}{ccc|c} 1 & 2 & -3 & 5 \\ 2 & 8 & -4 & 24 \\ 4 & 2 & 2 & 16 \end{array}\right]$$
2. **Zerando a 1ª coluna abaixo do pivô:**
   $$\xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(-4)}} \left[\begin{array}{ccc|c} 1 & 2 & -3 & 5 \\ 0 & 4 & 2 & 14 \\ 0 & -6 & 14 & -4 \end{array}\right]$$
3. **Zerando a 2ª coluna abaixo do pivô:**
   $$\xrightarrow{L_3' = L_3 + L_2(3/2)} \left[\begin{array}{ccc|c} 1 & 2 & -3 & 5 \\ 0 & 4 & 2 & 14 \\ 0 & 0 & 17 & 17 \end{array}\right]$$
4. **Substituição regressiva:**
   - $17z = 17 \Rightarrow z = 1$
   - $4y + 2(1) = 14 \Rightarrow 4y = 12 \Rightarrow y = 3$
   - $x + 2(3) - 3(1) = 5 \Rightarrow x + 3 = 5 \Rightarrow x = 2$
   - **Solução:** $(2, 3, 1)$.

### Exemplo 2 — Pivô inicial nulo exigindo $L_{12}$
Considere $\begin{cases} 0x + 2y - z = 1 \\ 2x - 2y + 4z = 6 \\ 4x + y + z = 9 \end{cases}$:
1. $A = \left[\begin{array}{ccc|c} 0 & 2 & -1 & 1 \\ 2 & -2 & 4 & 6 \\ 4 & 1 & 1 & 9 \end{array}\right] \xrightarrow{L_{12},\; L_1(1/2)} \left[\begin{array}{ccc|c} 1 & -1 & 2 & 3 \\ 0 & 2 & -1 & 1 \\ 4 & 1 & 1 & 9 \end{array}\right]$
2. $\xrightarrow{L_3' = L_3 + L_1(-4)} \left[\begin{array}{ccc|c} 1 & -1 & 2 & 3 \\ 0 & 2 & -1 & 1 \\ 0 & 5 & -7 & -3 \end{array}\right] \xrightarrow{L_3' = L_3 + L_2(-5/2)} \left[\begin{array}{ccc|c} 1 & -1 & 2 & 3 \\ 0 & 2 & -1 & 1 \\ 0 & 0 & -9/2 & -11/2 \end{array}\right]$
3. Substituição regressiva: $z = 11/9$; $2y = 1 + 11/9 = 20/9 \Rightarrow y = 10/9$; $x = 3 + 10/9 - 22/9 = 15/9 = 5/3$.

---

## 3. Exercícios (`C02-E01` a `C02-E05`)

### `C02-E01` *(Reprodução do modelo — Sistema com pivô inteiro)*
Resolva por Eliminação de Gauss e substituição regressiva o sistema do Exemplo 1 modificado apenas nos termos independentes:
$$\begin{cases} 2x + 4y - 6z = 4 \\ 4x + 2y + 2z = 10 \\ 2x + 8y - 4z = 14 \end{cases}$$
*Formato na caixa de resposta:* terna ordenada `(x, y, z)`.

---

### `C02-E02` *(Eliminação de Gauss com solução fracionária)*
Resolva o sistema por Eliminação de Gauss e substituição regressiva, mantendo frações irredutíveis:
$$\begin{cases} 2x - y + 3z = 9 \\ x + 2y - z = 0 \\ 3x + y + z = 9 \end{cases}$$
*Formato na caixa de resposta:* terna ordenada `(x, y, z)`.

---

### `C02-E03` *(Caça ao Bug na substituição regressiva)*
Após triangularizar corretamente um sistema $3 \times 3$, um estudante chegou ao sistema equivalente:
$$\begin{cases} x - 2y + z = 3 \\ 3y - 6z = -9 \\ 4z = 8 \end{cases}$$
Ao fazer a substituição regressiva, o estudante escreveu `(3, -1, 2)` alegando $3y + 6(2) = -9$ por erro de sinal. Corrija a substituição regressiva e informe a solução exata `(x, y, z)`.  
*Formato na caixa de resposta:* terna ordenada `(x, y, z)`.

---

### `C02-E04` *(Pivô nulo na 1ª equação — Uso obrigatório de $L_{12}$)*
Aplique a Eliminação de Gauss (com permutação de linhas) e a substituição regressiva para resolver:
$$\begin{cases} 2y + 3z = 7 \\ 3x - 6y + 3z = 3 \\ 2x + 4y - z = 5 \end{cases}$$
*Formato na caixa de resposta:* terna ordenada `(x, y, z)`.

---

### `C02-E05` *(Sistema $4 \times 4$ triangularizado por Gauss)*
Resolva o sistema $4 \times 4$ nas variáveis $(x, y, z, w)$ utilizando Eliminação de Gauss e substituição regressiva:
$$\begin{cases} x + y + z + w = 3 \\ 2x - y + z + 2w = 1 \\ x + 2y - 2z + w = 8 \\ 3x + y + 2z - w = 2 \end{cases}$$
*Formato na caixa de resposta:* quádrupla ordenada `(x, y, z, w)`.

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `C02-C01` *(Pivô nulo + solução fracionária)*
Resolva por Eliminação de Gauss e substituição regressiva:
$$\begin{cases} 3y - z = 5 \\ 2x - y + 4z = 7 \\ x + 2y - 3z = -4 \end{cases}$$
*Formato na caixa de resposta:* terna ordenada `(x, y, z)`.

---

### `C02-C02` *(Sistema denso com frações em cascata)*
Resolva por Eliminação de Gauss mantendo frações irredutíveis exatas:
$$\begin{cases} 2x + 3y - z = 2 \\ 4x - y + 2z = 3 \\ x + 2y + z = 3 \end{cases}$$
*Formato na caixa de resposta:* terna ordenada `(x, y, z)`.

---

### `C02-C03` *(Conferência e substituição regressiva)*
Resolva por Eliminação de Gauss e substituição regressiva:
$$\begin{cases} x - 2y + 3z = 11 \\ 2x + y - z = 1 \\ 3x - y + z = 8 \end{cases}$$
*Formato na caixa de resposta:* terna ordenada `(x, y, z)`.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `C03` (`Método de Gauss-Jordan na Matriz Ampliada`):** somente após autocorreção de `C02-E01..E05` **e** **100% (3/3)** na Checagem Independente `C02-C01..C03`.
- **Recuperação direcionada (1ª falha):** verifique se houve arredondamento prematuro de frações, troca de sinal na substituição regressiva ou esquecimento de usar $L_{ij}$ quando $a_{jj} = 0$; aplique a variante `V2` de `C02`.
- **Após 2 tentativas malsucedidas:** recuar no DAG para **`C01`** *(prática isolada das operações elementares $L_{ij}$, $L_i(\alpha)$ e $L_j' = L_j + L_i(\alpha)$ em matrizes ampliadas)*.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Sistemas.pdf` p. 9–12 (Eliminação de Gauss e substituição regressiva).
- `[DOC]` `Matrizes_Vetores_P2.pdf` p. 53–56 (escalonamento triangular e retro-substituição).
- Gabarito comentado e casos de verificação: [C02_gabarito.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_C/gabaritos/C02_gabarito.md) e [casos_C02.json](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_C/testes/casos_C02.json).
