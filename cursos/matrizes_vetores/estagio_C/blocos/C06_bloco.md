# Bloco `C06` — Grau de Liberdade (`g = n - C`) e Sistemas Homogêneos

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio C — Sistemas Lineares, Escalonamento, Posto (`C_A, C_V`) e Parâmetros / **`C06`** |
| **Micro-habilidade foco** | Determinar o grau de liberdade $g = n - C$, atribuir valores arbitrários às $g$ variáveis livres e analisar sistemas lineares homogêneos ($AX = O$), distinguindo solução trivial única ($C = n$) de soluções próprias / não-triviais ($C < n$ ou $\det(A) = 0$). |
| **Pré-requisitos** | `C05` *(Forma de escada $B$, $C_A, C_V, C$)* e `B05` *(Equações com determinantes e singularidade)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Prática (`C06-E01`–`C06-E05`, 22 min):** `14 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`C06-C01`–`C06-C03`, 16 min):** `11 min` resol. \| `5 min` conf. |
| **Restrição de escopo** | **Proibido:** Regra de Cramer, Regra de Sarrus ou matriz adjunta. Em sistemas homogêneos com parâmetro $k$, use escalonamento na forma de escada $B$ ou desenvolvimento por linha/coluna ($\det = 0$) para encontrar **todas** as raízes (atenção ao sinal $\pm$). |

### Registro da Sessão (Preenchido na Prática)
- **Protocolo:** `PREP-MV-C06-<VARIANTE>-T<TENTATIVA>-<HASH>`
- **Prática (`C06-E01`–`C06-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`C06-C01`–`C06-C03`):** `___ / 3` | **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Sistema linear homogêneo (`A.44`):** todo sistema em que os termos independentes são todos nulos ($AX = O$).
   - **Propriedade fundamental:** todo sistema homogêneo é **sempre compatível** ($C_A = C_V = C$, pois a última coluna de zeros permanece sempre nula nas operações $L$), admitindo no mínimo a **solução trivial** $x_1 = x_2 = \dots = x_n = 0$.
2. **Solução trivial vs. soluções próprias (não-triviais):**
   - Se **$C = n$** *(grau de liberdade $g = n - C = 0$)* $\Rightarrow$ `SPD`: admite **apenas a solução trivial** $(0, 0, \dots, 0)$.
   - Se **$C < n$** *(grau de liberdade $g = n - C \ge 1$)* $\Rightarrow$ `SPI`: admite **infinitas soluções próprias** (não-triviais), obtidas atribuindo valores arbitrários às $g$ variáveis livres.
   - **Caso particular $m = n$ (matriz quadrada $A$):** admite soluções próprias (não-triviais) **se e somente se** $\det(A) = 0$ *(ou seja, uma linha zera no escalonamento de $A$)*.
3. **Quando $m < n$ (menos equações que incógnitas):** como $C \le m < n$, todo sistema homogêneo com menos equações do que variáveis possui automaticamente $g = n - C \ge 1$ e, portanto, **sempre admite soluções próprias**.

---

## 2. Exemplos Guiados

### Exemplo 1 — Homogêneo com soluções próprias (`MAT121_Sistemas` p. 52–54)
$$\begin{cases} 3x + 6y - 9z = 0 \\ 2x + 4y - 6z = 0 \end{cases}$$
1. $A = \left[\begin{array}{ccc|c} 3 & 6 & -9 & 0 \\ 2 & 4 & -6 & 0 \end{array}\right] \xrightarrow{L_1(1/3)} \left[\begin{array}{ccc|c} 1 & 2 & -3 & 0 \\ 2 & 4 & -6 & 0 \end{array}\right] \xrightarrow{L_2' = L_2 + L_1(-2)} \left[\begin{array}{ccc|c} 1 & 2 & -3 & 0 \\ 0 & 0 & 0 & 0 \end{array}\right] = B$.
2. $C_A = 1$, $C_V = 1 \Rightarrow C = 1$. Como $n = 3$, temos $g = 3 - 1 = 2$ (`SPI`).
3. Da equação $x + 2y - 3z = 0 \Rightarrow x = -2y + 3z$, com $y, z$ arbitrários. Atribuindo $(y, z) = (1, 0)$, obtemos a solução própria $(-2, 1, 0)$.

### Exemplo 2 — Homogêneo $3 \times 3$ com solução apenas trivial (`MAT121_Sistemas` p. 55–57)
$$\begin{cases} x - 3y - 4z = 0 \\ x - y - z = 0 \\ x - y + 3z = 0 \end{cases} \Rightarrow \left[\begin{array}{ccc|c} 1 & -3 & -4 & 0 \\ 0 & 2 & 3 & 0 \\ 0 & 2 & 7 & 0 \end{array}\right] \sim \dots \sim \left[\begin{array}{ccc|c} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{array}\right] = B$$
Como $C_A = C_V = C = 3 = n$, $g = 0$ (`SPD`): admite **apenas a solução trivial** $(0, 0, 0)$.

---

## 3. Exercícios (`C06-E01` a `C06-E05`)

### `C06-E01` *(Homogêneo $3 \times 3$ determinado — Lista 5 Ex. 4)*
Escalone o sistema homogêneo abaixo até a forma de escada $B$, informe $C_A$, $C_V$, $g$, a classificação e a solução:
$$\begin{cases} x + y - z = 0 \\ 2x - 3y + z = 0 \\ 4x - 4y - 2z = 0 \end{cases}$$
*Formato na caixa de resposta:* `ca: <int>; cv: <int>; g: <int>; classificacao: <SPD/SPI>; solucao: (x, y, z)`.

---

### `C06-E02` *(Grau de liberdade $g = 2$ — Lista 5 Ex. 7)*
Para o sistema $\begin{cases} 6x + 2y + 4z = 0 \\ -9x - 3y - 6z = 0 \end{cases}$, obtenha a forma de escada $B$, informe $C_A$, $C_V$, $g$, a classificação e a solução particular obtida ao escolher os valores arbitrários **$y = 3$** e **$z = 0$**.  
*Formato na caixa de resposta:* `ca: <int>; cv: <int>; g: <int>; classificacao: <SPD/SPI>; solucao: (x, 3, 0)`.

---

### `C06-E03` *(Homogêneo $4 \times 2$ com frações — Lista 5 Ex. 8)*
Escalone o sistema:
$$\begin{cases} 3x + 6y = 0 \\ 12x + 24y = 0 \\ \frac{3}{2}x + 3y = 0 \\ \frac{3}{4}x + \frac{3}{2}y = 0 \end{cases}$$
Informe $C_A$, $C_V$, $g$, a classificação e **uma solução própria não nula** $(x, y)$ qualquer (ex.: com $y = 1$).  
*Formato na caixa de resposta:* `ca: <int>; cv: <int>; g: <int>; classificacao: <SPD/SPI>; solucao: (x, y)`.

---

### `C06-E04` *(Parâmetro $k$ para solução não-trivial — Lista 5 Ex. 19)*
Determine o valor real de $k$ para que o sistema homogêneo abaixo admita **solução não-trivial** (própria):
$$\begin{cases} x - y - z = 0 \\ x - 2y - 2z = 0 \\ 2x + ky + z = 0 \end{cases}$$
*Formato na caixa de resposta:* `k = <valor>`.

---

### `C06-E05` *(Caça ao Bug / Armadilha quadrática no parâmetro $k$)*
Um estudante resolveu o sistema $\begin{cases} x + 2z = 0 \\ ky + 2z = 0 \\ 2y + kz = 0 \end{cases}$ tentando dividir por $k$, descartou o sinal negativo e respondeu apenas `k = 2`.
Sem perder nenhuma raiz (por escalonamento com análise de casos ou desenvolvimento de $\det(A) = 0$ pela 1ª linha, **sem Sarrus**), encontre **todos** os valores reais de $k$ para os quais o sistema admite soluções próprias.  
*Formato na caixa de resposta:* `k = <valor1> ou k = <valor2>`.

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `C06-C01` *(Classificação de sistema homogêneo — Lista 5 Ex. 6)*
Escalone até a forma de escada $B$, determine $C_A$, $C_V$, $g$, a classificação e o conjunto solução de:
$$\begin{cases} x - z = 0 \\ 3x + y + 2z = 0 \\ 4x + 2y + 2z = 0 \end{cases}$$
*Formato na caixa de resposta:* `ca: <int>; cv: <int>; g: <int>; classificacao: <SPD/SPI>; solucao: (x, y, z)`.

---

### `C06-C02` *(Posto $C = 2$ e solução própria em $3 \times 3$)*
Escalone até $B$ o sistema $\begin{cases} x - 2y + z = 0 \\ 2x - y + 5z = 0 \\ 3x - 3y + 6z = 0 \end{cases}$. Informe $C_A$, $C_V$, $g$, a classificação e **uma solução própria não nula** $(x, y, z)$.  
*Formato na caixa de resposta:* `ca: <int>; cv: <int>; g: <int>; classificacao: <SPD/SPI>; solucao: (x, y, z)`.

---

### `C06-C03` *(Parâmetro $k$ para solução própria sem consulta)*
Determine o valor real de $k$ para que o sistema homogêneo $\begin{cases} x + 2y - z = 0 \\ 2x + y + z = 0 \\ 3x + ky = 0 \end{cases}$ admita solução não-trivial.  
*Formato na caixa de resposta:* `k = <valor>`.

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `C07` (`Discussão de Sistemas com Parâmetros k, a, b, c, d`):** somente após autocorreção de `C06-E01..E05` **e** **100% (3/3)** na Checagem Independente `C06-C01..C03`.
- **Recuperação direcionada (1ª falha):** lembre que sistemas homogêneos nunca são `SI` ($C_A = C_V$ sempre) e que $C < n$ gera infinitas soluções não-triviais; confira se não perdeu raízes $\pm$ em equações quadráticas de $k$; aplique a variante `V2` de `C06`.
- **Após 2 tentativas malsucedidas:** recuar no DAG para **`C05`** *(contagem de $C_A, C_V, C$)* ou **`B05`** *(equações $\det(A) = 0$ sem perder raízes)*.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Sistemas.pdf` p. 13, 49, 52–60 (`A.44` e `A.45.2.4`: grau de liberdade $g = n - C$ e sistemas homogêneos).
- `[DOC]` `Mat_Vet_L5.pdf` p. 2–3 (Ex. 4, 6, 7, 8, 19).
- Gabarito comentado e casos de verificação: [C06_gabarito.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_C/gabaritos/C06_gabarito.md) e [casos_C06.json](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_C/testes/casos_C06.json).
