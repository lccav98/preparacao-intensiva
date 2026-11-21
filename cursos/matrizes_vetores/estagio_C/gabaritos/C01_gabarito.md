# Gabarito Comentado — Bloco `C01` (Equação Linear, Forma Matricial, Matriz Ampliada e Operações Elementares `L`)

> **Bloco de referência:** [C01_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_C/blocos/C01_bloco.md)  
> **Nota para Caça ao Bug (`C01-E03`):** O erro intencional consiste em aplicar a operação elementar apenas na parte dos coeficientes, esquecendo a coluna dos termos independentes.

---

## 1. Gabarito dos Exercícios (`C01-E01` a `C01-E05`)

### `C01-E01`
- **(a)** A equação $3x - 2xy + z = 7$ contém o termo misto $-2xy$ (produto de duas variáveis, grau $2$). Portanto, é **não linear** (`nao linear`).
- **(b)** Substituindo $(2, -1, k)$ em $3x - 2y + 4z = 20$:
  $$3(2) - 2(-1) + 4k = 20 \Rightarrow 6 + 2 + 4k = 20 \Rightarrow 4k = 12 \Rightarrow \mathbf{k = 3}.$$
- **Resposta final:** `a: nao linear; b: 3`.

### `C01-E02`
Alinhando na ordem $(x, y, z)$ e preenchendo com `0` o coeficiente de $y$ na 2ª equação:
$$\begin{cases} 2x - 1y + 3z = 7 \\ 4x + 0y + 5z = -2 \\ -1x + 3y - 2z = 9 \end{cases} \Rightarrow A = \left[\begin{array}{ccc|c} 2 & -1 & 3 & 7 \\ 4 & 0 & 5 & -2 \\ -1 & 3 & -2 & 9 \end{array}\right]$$
- **Resposta final:** `[[2, -1, 3, 7], [4, 0, 5, -2], [-1, 3, -2, 9]]`.

### `C01-E03` *(Caça ao Bug)*
- **Diagnóstico da falha:** O estudante multiplicou apenas os coeficientes de $L_1$ por $1/2$ e manteve o termo independente $10$ sem dividir por $2$, propagando o erro para $L_2'$.
- **Resolução correta:**
  $$A = \left[\begin{array}{cc|c} 2 & 4 & 10 \\ 4 & -2 & 6 \end{array}\right] \xrightarrow{L_1(1/2)} \left[\begin{array}{cc|c} 1 & 2 & 5 \\ 4 & -2 & 6 \end{array}\right] \xrightarrow{L_2' = L_2 + L_1(-4)} \left[\begin{array}{cc|c} 1 & 2 & 5 \\ 0 & -10 & -14 \end{array}\right]$$
  *(Conferência da 2ª linha: $4 + (-4)(1) = 0$; $-2 + (-4)(2) = -10$; $6 + (-4)(5) = -14$.)*
- **Resposta final:** `[[1, 2, 5], [0, -10, -14]]`.

### `C01-E04`
1. $L_{12}$:
   $$\left[\begin{array}{ccc|c} 2 & -4 & 6 & 8 \\ 0 & 3 & -6 & 9 \\ -2 & 1 & 5 & -3 \end{array}\right]$$
2. $L_1(1/2)$:
   $$\left[\begin{array}{ccc|c} 1 & -2 & 3 & 4 \\ 0 & 3 & -6 & 9 \\ -2 & 1 & 5 & -3 \end{array}\right]$$
3. $L_3' = L_3 + L_1(2)$ *(cálculos: $-2+2(1)=0$; $1+2(-2)=-3$; $5+2(3)=11$; $-3+2(4)=5$)*:
   $$\left[\begin{array}{ccc|c} 1 & -2 & 3 & 4 \\ 0 & 3 & -6 & 9 \\ 0 & -3 & 11 & 5 \end{array}\right]$$
- **Resposta final:** `[[1, -2, 3, 4], [0, 3, -6, 9], [0, -3, 11, 5]]`.

### `C01-E05`
1. $L_2' = L_2 + L_1(-2)$:
   $$\left[\begin{array}{ccc|c} 1 & -2 & 3 & 4 \\ 0 & 5 & -7 & -5 \end{array}\right]$$
   *(Cálculos na 2ª linha: $2-2(1)=0$; $1-2(-2)=5$; $-1-2(3)=-7$; $3-2(4)=-5$.)*
2. $L_2(1/5)$:
   $$\left[\begin{array}{ccc|c} 1 & -2 & 3 & 4 \\ 0 & 1 & -7/5 & -1 \end{array}\right]$$
- **Resposta final:** `[[1, -2, 3, 4], [0, 1, -7/5, -1]]`.

---

## 2. Gabarito da Checagem Independente (`C01-C01` a `C01-C03`)

### `C01-C01`
Reordenando os termos em $(x, y, z)$:
$$\begin{cases} -1x + 3y + 2z = 4 \\ 2x + 0y + 1z = -5 \\ 0x + 1y - 4z = 1 \end{cases} \Rightarrow A = \left[\begin{array}{ccc|c} -1 & 3 & 2 & 4 \\ 2 & 0 & 1 & -5 \\ 0 & 1 & -4 & 1 \end{array}\right]$$
- **Resposta final:** `[[-1, 3, 2, 4], [2, 0, 1, -5], [0, 1, -4, 1]]`.

### `C01-C02`
1. $L_1(1/3)$:
   $$\left[\begin{array}{ccc|c} 1 & -2 & 3 & 4 \\ 6 & -10 & 15 & 20 \\ -3 & 8 & -5 & -7 \end{array}\right]$$
2. $L_2' = L_2 + L_1(-6)$ *(linha 2: $6-6=0$; $-10+12=2$; $15-18=-3$; $20-24=-4$)*:
   $$\left[\begin{array}{ccc|c} 1 & -2 & 3 & 4 \\ 0 & 2 & -3 & -4 \\ -3 & 8 & -5 & -7 \end{array}\right]$$
3. $L_3' = L_3 + L_1(3)$ *(linha 3: $-3+3=0$; $8-6=2$; $-5+9=4$; $-7+12=5$)*:
   $$\left[\begin{array}{ccc|c} 1 & -2 & 3 & 4 \\ 0 & 2 & -3 & -4 \\ 0 & 2 & 4 & 5 \end{array}\right]$$
- **Resposta final:** `[[1, -2, 3, 4], [0, 2, -3, -4], [0, 2, 4, 5]]`.

### `C01-C03`
- **(a)** $m(2) + 4(-1) - 3 = 5 \Rightarrow 2m - 7 = 5 \Rightarrow 2m = 12 \Rightarrow \mathbf{m = 6}$.
- **(b)** Testando na 2ª equação: $1(2) - 2(-1) + 1(3) = 2 + 2 + 3 = 7$. A igualdade é verdadeira (**`sim`**).
- **Resposta final:** `a: 6; b: sim`.
