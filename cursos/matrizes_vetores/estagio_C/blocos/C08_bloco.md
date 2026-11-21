# Bloco `C08` — Revisão Cumulativa do Estágio C

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio C — Sistemas Lineares, Escalonamento, Posto (`C_A, C_V`) e Parâmetros / **`C08`** |
| **Micro-habilidade foco** | Integrar sem consulta todos os métodos do Estágio C: Gauss-Jordan em `[A | B]`, Método da Matriz Inversa $X = A^{-1}B$ (`[A | I]`), redução à forma de escada $B$ em sistemas $m \times n$ com $C_A, C_V, g$, sistemas homogêneos e discussão paramétrica ($k, a, b, c$). |
| **Pré-requisitos** | `C04` *(Matriz inversa $X = A^{-1}B$)* e `C07` *(Discussão com parâmetros)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Prática (`C08-E01`–`C08-E05`, 25 min):** `16 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C08-C01`–`C08-C03`, 18 min):** `12 min` resol. \| `6 min` conf. |
| **Restrição de escopo** | **Proibido:** Regra de Cramer, Regra de Sarrus, Chió, Vandermonde ou matriz adjunta. Utilize exclusivamente operações elementares $L_{ij}$, $L_i(\alpha)$ e $L_j' = L_j + L_i(\alpha)$, notação $A, B, V, C_A, C_V, C, g = n - C$ e frações irredutíveis exatas. |

### Registro da Sessão (Preenchido na Prática)
- **Protocolo:** `PREP-MV-C08-<VARIANTE>-T<TENTATIVA>-<HASH>`
- **Prática (`C08-E01`–`C08-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`C08-C01`–`C08-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas (Mapa de Decisão do Estágio C)

| Situação do Sistema | Método Recomendado | Critério de Classificação / Conclusão |
|---|---|---|
| Sistema $n \times n$ com único vetor $B$ | Eliminação de Gauss (`C02`) ou Gauss-Jordan (`C03`) | `[I | X]` $\Rightarrow$ `SPD`; linha `[0 ... 0 | c]` ($c \neq 0$) $\Rightarrow$ `SI`; linha toda nula sem absurdo $\Rightarrow$ `SPI`. |
| Mesmo $A$ ($n \times n$) com vários vetores $B^{(1)}, B^{(2)}, \dots$ | Matriz Inversa (`C04`): `[A | I] -> [I | A^{-1}]` e $X = A^{-1}B$ | Multiplicar **sempre à esquerda** ($A^{-1}B$); se zerar linha no bloco esquerdo de `[A | I]`, $A$ é singular. |
| Sistema retangular $m \times n$ ($m > n$ ou $m < n$) | Forma de escada $B$ e submatriz $V$ (`C05`) | $C_A > C_V \Rightarrow$ `SI`; $C_A = C_V = C = n \Rightarrow$ `SPD`; $C_A = C_V = C < n \Rightarrow$ `SPI` com $g = n - C$. |
| Sistema homogêneo $AX = O$ | Forma de escada $B$ ou $\det(A) = 0$ (para $n \times n$) (`C06`) | Sempre compatível; $C = n \Rightarrow$ apenas trivial; $C < n \Rightarrow$ soluções próprias ($g = n - C \ge 1$). |
| Sistema com parâmetros ($k, a, b, c, d$) | Escalonamento carregando símbolos em `[A | B]` (`C07`) | Compatível $\iff C_A = C_V$; nunca dividir por expressão em $k$ que possa zerar sem abrir os casos. |

---

## 2. Exemplos Guiados

### Exemplo 1 — Síntese de Classificação e Grau de Liberdade (`Sondagem T3`)
Para $\begin{cases} x + y + z = 6 \\ 2x + 2y + 2z = 12 \\ x - y + z = 2 \end{cases}$:
$$A = \left[\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 2 & 2 & 2 & 12 \\ 1 & -1 & 1 & 2 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(-1)}} \left[\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 0 & 0 & 0 & 0 \\ 0 & -2 & 0 & -4 \end{array}\right] \xrightarrow{\substack{L_{23},\; L_2(-1/2) \\ L_1' = L_1 + L_2(-1)}} \left[\begin{array}{ccc|c} 1 & 0 & 1 & 4 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 0 & 0 \end{array}\right] = B$$
- $C_A = C_V = C = 2 < n = 3 \Rightarrow g = 3 - 2 = 1$, **`SPI`**, $(x, y, z) = (4 - z, 2, z)$.

### Exemplo 2 — Alerta de prova para parâmetros em homogêneo
Em $\begin{cases} x + y - z = 0 \\ 2x + y + z = 0 \\ 3x + 2y + kz = 0 \end{cases}$, $L_1 + L_2$ já gera $3x + 2y + 0z = 0$: o escalonamento mostra imediatamente $[0\;\;0\;\;k \mid 0]$, logo há solução própria $\iff k = 0$.

---

## 3. Exercícios (`C08-E01` a `C08-E05`)

### `C08-E01` *(Gauss-Jordan $3 \times 3$ com frações exatas)*
Resolva por Gauss-Jordan na matriz ampliada até `[I | X]`:
$$\begin{cases} 2x - 2y + 4z = 5 \\ x + 3y - z = 2 \\ 3x + y + 2z = 4 \end{cases}$$
*Formato na caixa de resposta:* terna ordenada `(x, y, z)` em frações irredutíveis.

---

### `C08-E02` *(Método da Matriz Inversa com dois vetores $B$)*
Para $A = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 2 \end{bmatrix}$:  
**(a)** Calcule $A^{-1}$ via `[A | I] -> [I | A^{-1}]`.  
**(b)** Resolva $AX = B^{(1)}$ para $B^{(1)} = \begin{bmatrix} 3 \\ 5 \\ 7 \end{bmatrix}$.  
**(c)** Resolva $AX = B^{(2)}$ para $B^{(2)} = \begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix}$.  
*Formato na caixa de resposta:* `inversa: [[...], [...], [...]]; solucao1: (x1, y1, z1); solucao2: (x2, y2, z2)`.

---

### `C08-E03` *(Sistema sobredeterminado $4 \times 3$ — Posto $C_A, C_V, g$)*
Reduza à forma de escada $B$, informe $C_A$, $C_V$, $g$, a classificação e a solução do sistema:
$$\begin{cases} x + 2y - z = 3 \\ 2x + 5y + z = 8 \\ x + 3y + 2z = 5 \\ 3x + 8y = 11 \end{cases}$$
*Formato na caixa de resposta:* `ca: <int>; cv: <int>; g: <int>; classificacao: <SPD/SPI/SI>; solucao: (x, y, z)`.

---

### `C08-E04` *(Homogêneo simétrico $3 \times 3$ com parâmetro $k$)*
Determine **todos** os valores reais de $k$ para os quais o sistema homogêneo abaixo admite soluções próprias (não-triviais):
$$\begin{cases} kx + y + z = 0 \\ x + ky + z = 0 \\ x + y + kz = 0 \end{cases}$$
*(Dica: some todas as equações ou escalone / desenvolva $\det(A) = 0$ pela 1ª linha, **sem Sarrus**.)*  
*Formato na caixa de resposta:* `k = <valor1> ou k = <valor2>`.

---

### `C08-E05` *(Condição de compatibilidade sobre $a, b, c$)*
Determine a condição algébrica sobre $a, b, c$ para que o sistema abaixo seja compatível:
$$\begin{cases} x + y - 2z = a \\ 2x - y + z = b \\ 4x + y - 3z = c \end{cases}$$
*Formato na caixa de resposta:* equação em `a, b, c` (ex.: `... = 0`).

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `C08-C01` *(Escalonamento completo, posto, $g$ e solução particular)*
Para o sistema $\begin{cases} x - y + 2z = 4 \\ 2x - 2y + 4z = 8 \\ 3x - y + z = 7 \end{cases}$, obtenha a forma de escada $B$, informe $C_A$, $C_V$, $g$, a classificação e a solução particular para **$z = 1$**.  
*Formato na caixa de resposta:* `ca: <int>; cv: <int>; g: <int>; classificacao: <SPD/SPI/SI>; solucao: (x, y, 1)`.

---

### `C08-C02` *(Inversa $3 \times 3$ e resolução $X = A^{-1}B$)*
Considere $A = \begin{bmatrix} 2 & 1 & 0 \\ 1 & 1 & 1 \\ 0 & 1 & 3 \end{bmatrix}$ e $B = \begin{bmatrix} 4 \\ 3 \\ 2 \end{bmatrix}$. Determine $A^{-1}$ por `[A | I] -> [I | A^{-1}]` e calcule $X = A^{-1}B$.  
*Formato na caixa de resposta:* `inversa: [[...], [...], [...]]; solucao: (x, y, z)`.

---

### `C08-C03` *(Discussão completa do parâmetro $k$)*
Para o sistema $\begin{cases} x + y + z = 1 \\ x + 2y + kz = 2 \\ 2x + 3y + (k^2 - 1)z = k + 1 \end{cases}$, escalone carregando $k$ e informe:  
**(a)** o valor de $k$ que torna o sistema **`SPI`**;  
**(b)** o valor de $k$ que torna o sistema **`SI`**.  
*Formato na caixa de resposta:* `spi: <valor de k>; si: <valor de k>`.

---

## 5. Orientação de Avanço ou Recuperação

- **Concluir Estágio C e avançar para `D01` (ou `G02` — Simulado P2 Parte 1):** somente após autocorreção de `C08-E01..E05` **e** **100% (3/3)** na Checagem Independente `C08-C01..C03`.
- **Recuperação direcionada (1ª falha):** identifique exatamente qual sub-habilidade falhou (`[A | I]` $\rightarrow$ `C04`; posto/escada $\rightarrow$ `C05`; homogêneos $\rightarrow$ `C06`; parâmetros $\rightarrow$ `C07`), refaça 1 exemplo do bloco correspondente e aplique a variante `V2` de `C08`.
- **Após 2 tentativas malsucedidas:** recuar no DAG para **`C04`** *(matriz inversa)* ou **`C07`** *(discussão paramétrica)* antes de tentar `C08` novamente.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Sistemas.pdf` p. 1–60 (conteúdo integral de Sistemas de Equações Lineares).
- `[DOC]` `Matrizes_Vetores_P2.pdf` p. 49–77 (caderno completo de sistemas lineares).
- `[DOC]` `Mat_Vet_L5.pdf` p. 1–5 (Lista 5 completa, Ex. 1–23).
- Gabarito comentado e casos de verificação: [C08_gabarito.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_C/gabaritos/C08_gabarito.md) e [casos_C08.json](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_C/testes/casos_C08.json).
