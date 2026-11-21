# Bloco `C03` — Método de Gauss-Jordan na Matriz Ampliada (`n × n`)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio C — Sistemas Lineares, Escalonamento, Posto (`C_A, C_V`) e Parâmetros / **`C03`** |
| **Micro-habilidade foco** | Aplicar redução completa de Gauss-Jordan na matriz ampliada `[A | B]` de sistemas quadrados $n \times n$ até obter `[I | X]` (ou detectar linhas nulas / incompatíveis), classificando em `SPD`, `SPI` ou `SI`. |
| **Pré-requisitos** | `C02` *(Eliminação de Gauss e substituição regressiva)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Prática (`C03-E01`–`C03-E05`, 24 min):** `15 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C03-C01`–`C03-C03`, 16 min):** `11 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Proibido:** Regra de Cramer, Regra de Sarrus ou matriz adjunta. Reduza a matriz ampliada usando exclusivamente $L_{ij}$, $L_i(\alpha)$ ($\alpha \neq 0$) e $L_j' = L_j + L_i(\alpha)$, mantendo frações irredutíveis exatas. |

### Registro da Sessão (Preenchido na Prática)
- **Protocolo:** `PREP-MV-C03-<VARIANTE>-T<TENTATIVA>-<HASH>`
- **Prática (`C03-E01`–`C03-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`C03-C01`–`C03-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Diferença para a Eliminação de Gauss:** no **Método de Gauss-Jordan**, além de zerar **abaixo** de cada pivô, normalizamos o pivô para **$1$** ($L_i(1/a_{ii})$) e zeramos também **acima** dele ($L_j' = L_j + L_i(-a_{ji})$).
2. **Leitura direta da solução em sistemas $n \times n$:**
   - Se a submatriz à esquerda do traço vertical atingir a identidade $I_n$ ($\left[I_n \mid X\right]$), não há substituição regressiva: o vetor-coluna à direita já fornece diretamente a solução única (`SPD`).
   - Se surgir uma linha do tipo `[0  0  ...  0 | c]` com $c \neq 0$, o sistema é **incompatível (`SI`)** (não admite solução).
   - Se surgir uma linha inteiramente nula `[0  0  ...  0 | 0]` sem linha absurda, o sistema é **compatível e indeterminado (`SPI`)** (infinitas soluções).
3. **Estratégia contra frações precoces:** antes de dividir uma linha, verifique se há uma linha abaixo com pivô `1` ou `-1` para aplicar $L_{ij}$.

---

## 2. Exemplos Guiados

### Exemplo 1 — Modelo da Apostila (`MAT121_Sistemas` p. 17–21)
Resolver por Gauss-Jordan na matriz ampliada:
$$\begin{cases} 2x + y + 3z = 8 \\ 4x + 2y + 2z = 4 \\ 2x + 5y + 3z = -12 \end{cases}$$
1. **Matriz ampliada inicial e pivô $1$ na 1ª linha:**
   $$\left[\begin{array}{ccc|c} 2 & 1 & 3 & 8 \\ 4 & 2 & 2 & 4 \\ 2 & 5 & 3 & -12 \end{array}\right] \xrightarrow{L_1(1/2)} \left[\begin{array}{ccc|c} 1 & 1/2 & 3/2 & 4 \\ 4 & 2 & 2 & 4 \\ 2 & 5 & 3 & -12 \end{array}\right]$$
2. **Zerando a 1ª coluna e trocando $L_{23}$ (pois surgiu $0$ na posição $(2,2)$):**
   $$\xrightarrow{\substack{L_2' = L_2 + L_1(-4) \\ L_3' = L_3 + L_1(-2)}} \left[\begin{array}{ccc|c} 1 & 1/2 & 3/2 & 4 \\ 0 & 0 & -4 & -12 \\ 0 & 4 & 0 & -20 \end{array}\right] \xrightarrow{L_{23}} \left[\begin{array}{ccc|c} 1 & 1/2 & 3/2 & 4 \\ 0 & 4 & 0 & -20 \\ 0 & 0 & -4 & -12 \end{array}\right]$$
3. **Pivôs $1$ em $L_2$ e $L_3$, e redução acima da diagonal:**
   $$\xrightarrow{\substack{L_2(1/4) \\ L_3(-1/4)}} \left[\begin{array}{ccc|c} 1 & 1/2 & 3/2 & 4 \\ 0 & 1 & 0 & -5 \\ 0 & 0 & 1 & 3 \end{array}\right] \xrightarrow{L_1' = L_1 + L_2(-1/2)} \left[\begin{array}{ccc|c} 1 & 0 & 3/2 & 13/2 \\ 0 & 1 & 0 & -5 \\ 0 & 0 & 1 & 3 \end{array}\right]$$
   $$\xrightarrow{L_1' = L_1 + L_3(-3/2)} \left[\begin{array}{ccc|c} 1 & 0 & 0 & 2 \\ 0 & 1 & 0 & -5 \\ 0 & 0 & 1 & 3 \end{array}\right]$$
   **Classificação:** `SPD` (compatível e determinado). **Solução:** $(2, -5, 3)$.

### Exemplo 2 — Sistema $2 \times 2$ (`MAT121_Sistemas` p. 14–16)
$$\begin{cases} 2x + 4y = 22 \\ 5x - 15y = -20 \end{cases} \Rightarrow \left[\begin{array}{cc|c} 2 & 4 & 22 \\ 5 & -15 & -20 \end{array}\right] \xrightarrow{L_1(1/2)} \left[\begin{array}{cc|c} 1 & 2 & 11 \\ 5 & -15 & -20 \end{array}\right]$$
$$\xrightarrow{L_2' = L_2 + L_1(-5)} \left[\begin{array}{cc|c} 1 & 2 & 11 \\ 0 & -25 & -75 \end{array}\right] \xrightarrow{L_2(-1/25)} \left[\begin{array}{cc|c} 1 & 2 & 11 \\ 0 & 1 & 3 \end{array}\right] \xrightarrow{L_1' = L_1 + L_2(-2)} \left[\begin{array}{cc|c} 1 & 0 & 5 \\ 0 & 1 & 3 \end{array}\right]$$
Solução única: $(5, 3)$.

---

## 3. Exercícios (`C03-E01` a `C03-E05`)

### `C03-E01` *(Reprodução guiada — Lista 5 Ex. 2)*
Utilizando o Método de Gauss-Jordan na matriz ampliada, classifique e resolva o sistema:
$$\begin{cases} 3x + 2y - 5z = 8 \\ 2x - 4y - 2z = -4 \\ x - 2y - 3z = -4 \end{cases}$$
*Formato na caixa de resposta:* `classificacao: SPD (ou SPI ou SI); solucao: (x, y, z)`.

---

### `C03-E02` *(Gauss-Jordan com zeros iniciais — Lista 5 Ex. 5)*
Resolva por Gauss-Jordan na matriz ampliada o sistema:
$$\begin{cases} x + 3z = -8 \\ 2x - 4y = -4 \\ 3x - 2y - 5z = 26 \end{cases}$$
*Formato na caixa de resposta:* terna ordenada `(x, y, z)`.

---

### `C03-E03` *(Caça ao Bug na redução por Gauss-Jordan)*
Ao resolver o sistema do Exemplo 1 ($\begin{cases} 2x + y + 3z = 8 \\ 4x + 2y + 2z = 4 \\ 2x + 5y + 3z = -12 \end{cases}$), um estudante escreveu a última linha escalonada como `[0  0  -4 | -12]` e aplicou erradamente $L_3(1/4)$ apenas ao lado esquerdo (ou trocou o sinal do termo independente), obtendo `z = -3` e solução final `(2, -5, -3)` (note que isso ocorre se substituir `z = -3` errado ou inverter o sinal em `L_3(-1/4)`). Confira todas as etapas e informe a solução exata `(x, y, z)` obtida pela redução correta até `[I | X]`.  
*Formato na caixa de resposta:* terna ordenada `(x, y, z)`.

---

### `C03-E04` *(Sistema quadrado $3 \times 3$ incompatível)*
Aplique Gauss-Jordan na matriz ampliada do sistema abaixo e classifique-o (`SPD`, `SPI` ou `SI`):
$$\begin{cases} x + 2y - z = 3 \\ 2x + 5y + z = 7 \\ 3x + 7y = 12 \end{cases}$$
*Formato na caixa de resposta:* escreva a sigla da classificação (`SPD`, `SPI` ou `SI`).

---

### `C03-E05` *(Gauss-Jordan com solução em frações irredutíveis)*
Resolva o sistema pelo método de Gauss-Jordan até atingir `[I | X]`, mantendo frações exatas:
$$\begin{cases} 2x + 4y - 2z = 3 \\ 4x + 6y + 2z = 5 \\ 2x - 2y + 4z = 1 \end{cases}$$
*Formato na caixa de resposta:* terna ordenada `(x, y, z)` em frações irredutíveis.

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `C03-C01` *(Classificação e solução fracionária por Gauss-Jordan)*
Classifique e resolva por Gauss-Jordan na matriz ampliada:
$$\begin{cases} 2x + 2y - 2z = 1 \\ 2x - 2y + 2z = 5 \\ 3x + y + 2z = 5 \end{cases}$$
*Formato na caixa de resposta:* `classificacao: <SPD/SPI/SI>; solucao: (x, y, z)`.

---

### `C03-C02` *(Sistema quadrado indeterminado — Lista 5 Ex. 3)*
Reduza pelo método de Gauss-Jordan até a forma mais simplificada possível o sistema:
$$\begin{cases} 2x + 4y + 6z = -6 \\ 3x - 2y - 4z = -38 \\ x + 2y + 3z = -3 \end{cases}$$
**(a)** Classifique o sistema (`SPD`, `SPI` ou `SI`).  
**(b)** Expresse $x$ e $y$ em função da variável arbitrária $z$ e dê a solução particular para **$z = 1$** no formato `(x, y, 1)`.  
*Formato na caixa de resposta:* `classificacao: <SPD/SPI/SI>; solucao_z1: (x, y, 1)`.

---

### `C03-C03` *(Detecção independente de incompatibilidade)*
Aplique Gauss-Jordan na matriz ampliada do sistema abaixo e informe sua classificação (`SPD`, `SPI` ou `SI`):
$$\begin{cases} x - 2y + z = 4 \\ 2x - 3y + 4z = 7 \\ 3x - 5y + 5z = 9 \end{cases}$$
*Formato na caixa de resposta:* escreva `SPD`, `SPI` ou `SI`.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `C04` (`Método da Matriz Inversa X = A^{-1}B`) e `C05` (`Forma de Escada e Posto C_A, C_V`):** somente após autocorreção de `C03-E01..E05` **e** **100% (3/3)** na Checagem Independente `C03-C01..C03`.
- **Recuperação direcionada (1ª falha):** confira se você reduziu **acima** de todos os pivôs, se manteve frações exatas sem arredondar e se verificou toda a última linha `[0 0 0 | c]` antes de classificar; aplique a variante `V2` de `C03`.
- **Após 2 tentativas malsucedidas:** recuar no DAG para **`C02`** *(escalonamento descendente controlado e conferência aritmética linha a linha)*.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Sistemas.pdf` p. 14–21 (`A.45.1`: método de Gauss-Jordan em sistemas $n \times n$ via matriz ampliada).
- `[DOC]` `Mat_Vet_L5.pdf` p. 2 (Ex. 2, Ex. 3, Ex. 5).
- Gabarito comentado e casos de verificação: [C03_gabarito.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_C/gabaritos/C03_gabarito.md) e [casos_C03.json](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_C/testes/casos_C03.json).
