# Gabarito Comentado — Bloco `C07` (Discussão de Sistemas com Parâmetros `k, a, b, c, d`)

> **Bloco de referência:** [C07_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_C/blocos/C07_bloco.md)  
> **Nota para Caça ao Bug (`C07-E03`):** Dividir por $(1 - k)$ oculta a raiz $k = 1$, na qual o sistema fica com duas equações idênticas (`SPI`).

---

## 1. Gabarito dos Exercícios (`C07-E01` a `C07-E05`)

### `C07-E01` *(Lista 5 Ex. 12)*
$$\left[\begin{array}{cc|c} 1 & 2 & a \\ -3 & 4 & b \\ 2 & -1 & c \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(3) \\ L_3' = L_3 + L_1(-2)}} \left[\begin{array}{cc|c} 1 & 2 & a \\ 0 & 10 & b + 3a \\ 0 & -5 & c - 2a \end{array}\right] \xrightarrow{\substack{L_{23},\; L_2(-1/5) \\ L_3' = L_3 + L_2(-10)}} \left[\begin{array}{cc|c} 1 & 2 & a \\ 0 & 1 & (2a - c)/5 \\ 0 & 0 & b + 3a - 4a + 2c \end{array}\right]$$
*(Alternativamente, fazendo diretamente $L_3'' = 2L_3' + L_2' \sim L_3' + L_2'(1/2)$: o termo independente da 3ª linha zera quando $\frac{b + 3a}{2} + (c - 2a) = 0 \iff b - a + 2c = 0$.)*
Logo, $C_A = C_V \iff \mathbf{a = b + 2c}$ (ou $a - b - 2c = 0$).
- **Resposta final:** `a - b - 2c = 0`.

### `C07-E02` *(Lista 5 Ex. 18)*
$$\left[\begin{array}{ccc|c} 1 & -2 & -1 & a \\ 2 & 1 & 3 & b \\ 4 & -3 & 1 & c \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(-4)}} \left[\begin{array}{ccc|c} 1 & -2 & -1 & a \\ 0 & 5 & 5 & b - 2a \\ 0 & 5 & 5 & c - 4a \end{array}\right] \xrightarrow{L_3' = L_3 + L_2(-1)} \left[\begin{array}{ccc|c} 1 & -2 & -1 & a \\ 0 & 5 & 5 & b - 2a \\ 0 & 0 & 0 & c - 2a - b \end{array}\right]$$
Compatível $\iff C_A = C_V \iff c - 2a - b = 0 \iff \mathbf{2a + b - c = 0}$.
- **Resposta final:** `2a + b - c = 0`.

### `C07-E03` *(Caça ao Bug)*
$$\left[\begin{array}{cc|c} 1 & k & 2 \\ k & 1 & 2 \end{array}\right] \xrightarrow{L_2' = L_2 + L_1(-k)} \left[\begin{array}{cc|c} 1 & k & 2 \\ 0 & 1 - k^2 & 2(1 - k) \end{array}\right]$$
Fatorando $1 - k^2 = (1 - k)(1 + k)$:
- **(a)** Se **$k = 1$**, a 2ª linha torna-se `[0  0 | 0]` ($C_A = C_V = 1 < 2$) $\Rightarrow$ **`SPI`**.
- **(b)** Se **$k = -1$**, a 2ª linha torna-se `[0  0 | 4]` ($C_A = 2 > C_V = 1$) $\Rightarrow$ **`SI`**.
- *(Para $k \neq \pm 1$, o sistema é `SPD`.)*
- **Resposta final:** `spi: 1; si: -1`.

### `C07-E04` *(Lista 5 Ex. 14)*
$$\left[\begin{array}{cc|c} -1 & 3 & a \\ 2 & -1 & b \\ -2 & 1 & c \\ 3 & 1 & d \end{array}\right] \xrightarrow{L_1(-1)} \left[\begin{array}{cc|c} 1 & -3 & -a \\ 2 & -1 & b \\ -2 & 1 & c \\ 3 & 1 & d \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(2) \\ L_4' = L_4 + L_1(-3)}} \left[\begin{array}{cc|c} 1 & -3 & -a \\ 0 & 5 & b + 2a \\ 0 & -5 & c - 2a \\ 0 & 10 & d + 3a \end{array}\right]$$
$$\xrightarrow{\substack{L_3'' = L_3' + L_2' \\ L_4'' = L_4' + L_3'(2)}} \left[\begin{array}{cc|c} 1 & -3 & -a \\ 0 & 5 & b + 2a \\ 0 & 0 & b + c \\ 0 & 0 & 2c + d - a \end{array}\right]$$
Para que $C_A = C_V = 2$, ambas as linhas nulas em $V$ devem ter termo independente nulo:
- **`cond1`:** $b + c = 0$ *(ou $b = -c$)*
- **`cond2`:** $a - 2c - d = 0$ *(ou $a = 2c + d$)*
- **Resposta final:** `cond1: b + c = 0; cond2: a = 2c + d`.

### `C07-E05` *(Lista 5 Ex. 16)*
$$\left[\begin{array}{cc|c} 3 & 5 & a \\ 1 & 2 & b \end{array}\right] \xrightarrow{L_{12}} \left[\begin{array}{cc|c} 1 & 2 & b \\ 3 & 5 & a \end{array}\right] \xrightarrow{L_2' = L_2 + L_1(-3)} \left[\begin{array}{cc|c} 1 & 2 & b \\ 0 & -1 & a - 3b \end{array}\right] \xrightarrow{\substack{L_2(-1) \\ L_1' = L_1 + L_2(-2)}} \left[\begin{array}{cc|c} 1 & 0 & 2a - 5b \\ 0 & 1 & -a + 3b \end{array}\right]$$
- **Resposta final:** `x: x = 2a - 5b; y: y = -a + 3b`.

---

## 2. Gabarito da Checagem Independente (`C07-C01` a `C07-C03`)

### `C07-C01` *(Lista 5 Ex. 13)*
$$\left[\begin{array}{cc|c} 1 & 2 & a \\ -2 & 1 & b \\ -1 & 1 & c \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(2) \\ L_3' = L_3 + L_1(1)}} \left[\begin{array}{cc|c} 1 & 2 & a \\ 0 & 5 & b + 2a \\ 0 & 3 & c + a \end{array}\right] \xrightarrow{L_2(1/5)} \left[\begin{array}{cc|c} 1 & 2 & a \\ 0 & 1 & (b + 2a)/5 \\ 0 & 3 & c + a \end{array}\right]$$
$$\xrightarrow{L_3' = L_3 + L_2(-3)} \left[\begin{array}{cc|c} 1 & 2 & a \\ 0 & 1 & (b + 2a)/5 \\ 0 & 0 & c + a - \frac{3b + 6a}{5} \end{array}\right]$$
Igualando o termo da 3ª linha a zero: $5c + 5a - 3b - 6a = 0 \Rightarrow -a - 3b + 5c = 0 \iff \mathbf{a + 3b - 5c = 0}$ *(ou $a = -3b + 5c$)*.
- **Resposta final:** `a + 3b - 5c = 0`.

### `C07-C02` *(Lista 5 Ex. 15)*
Usando a mesma estrutura de `C07-E01` (ou escalonando diretamente com $-1, k, -7$):
$$\left[\begin{array}{cc|c} 1 & 2 & -1 \\ -3 & 4 & k \\ 2 & -1 & -7 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(3) \\ L_3' = L_3 + L_1(-2)}} \left[\begin{array}{cc|c} 1 & 2 & -1 \\ 0 & 10 & k - 3 \\ 0 & -5 & -5 \end{array}\right] \xrightarrow{L_3(-1/5)} \left[\begin{array}{cc|c} 1 & 2 & -1 \\ 0 & 10 & k - 3 \\ 0 & 1 & 1 \end{array}\right] \xrightarrow{L_2' = L_2 + L_3(-10)} \left[\begin{array}{cc|c} 1 & 2 & -1 \\ 0 & 0 & k - 13 \\ 0 & 1 & 1 \end{array}\right]$$
Compatível $\iff k - 13 = 0 \Rightarrow \mathbf{k = 13}$.
- **Resposta final:** `k = 13`.

### `C07-C03`
$$\left[\begin{array}{ccc|c} 1 & 1 & 1 & 2 \\ 2 & 3 & 2 & 5 \\ 1 & 1 & k^2 - 3 & k \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(-1)}} \left[\begin{array}{ccc|c} 1 & 1 & 1 & 2 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & k^2 - 4 & k - 2 \end{array}\right]$$
As raízes de $k^2 - 4 = 0$ são $k = 2$ e $k = -2$:
- **(a)** Para **$k = 2$**, a 3ª linha vira `[0  0  0 | 0]` ($C_A = C_V = 2 < 3$) $\Rightarrow$ **`SPI`**.
- **(b)** Para **$k = -2$**, a 3ª linha vira `[0  0  0 | -4]` ($C_A = 3 > C_V = 2$) $\Rightarrow$ **`SI`**.
- **Resposta final:** `spi: 2; si: -2`.
