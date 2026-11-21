# Gabarito Comentado — Bloco `G02` (Simulado Integrador P2 — Parte 1: Sistemas Lineares e Parâmetros)

> **Bloco de referência:** [G02_bloco.md](../blocos/G02_bloco.md)

---

## 1. Exercícios

### `G02-E01` *(Sistema sobredeterminado $4 \times 3$, forma de escada e posto)*
- **Passo a passo:**
  - Matriz ampliada:
    $$A = \left[\begin{array}{ccc|c} 1 & 1 & 1 & 4 \\ 2 & -1 & 1 & 8 \\ 1 & 2 & -1 & -3 \\ 3 & 0 & 2 & 12 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 - 2L_1 \\ L_3' = L_3 - L_1 \\ L_4' = L_4 - 3L_1}} \left[\begin{array}{ccc|c} 1 & 1 & 1 & 4 \\ 0 & -3 & -1 & 0 \\ 0 & 1 & -2 & -7 \\ 0 & -3 & -1 & 0 \end{array}\right]$$
    $$\xrightarrow{L_4' = L_4 - L_2} \left[\begin{array}{ccc|c} 1 & 1 & 1 & 4 \\ 0 & -3 & -1 & 0 \\ 0 & 1 & -2 & -7 \\ 0 & 0 & 0 & 0 \end{array}\right] \xrightarrow{L_2 \leftrightarrow L_3} \left[\begin{array}{ccc|c} 1 & 1 & 1 & 4 \\ 0 & 1 & -2 & -7 \\ 0 & -3 & -1 & 0 \\ 0 & 0 & 0 & 0 \end{array}\right]$$
    $$\xrightarrow{L_3' = L_3 + 3L_2} \left[\begin{array}{ccc|c} 1 & 1 & 1 & 4 \\ 0 & 1 & -2 & -7 \\ 0 & 0 & -7 & -21 \\ 0 & 0 & 0 & 0 \end{array}\right] \xrightarrow{L_3(-1/7)} \left[\begin{array}{ccc|c} 1 & 1 & 1 & 4 \\ 0 & 1 & -2 & -7 \\ 0 & 0 & 1 & 3 \\ 0 & 0 & 0 & 0 \end{array}\right] = B.$$
  - Contagem: $C_A = 3$, $C_V = 3$, $n = 3 \implies g = 3 - 3 = 0$ (`SPD`).
  - Substituição regressiva: $z = 3$; $y = -7 + 2(3) = -1$; $x = 4 - (-1) - 3 = 2$.
- **Resposta Final:** `ca: 3; cv: 3; g: 0; classificacao: SPD; solucao: (2, -1, 3)`
- **Alerta pedagógico:** Um sistema com $4$ equações e $3$ incógnitas não é necessariamente `SI`; se a 4ª linha anula completamente, conta apenas como $3$ linhas não nulas.

---

### `G02-E02` *(Sistema subdeterminado $3 \times 4$ com $g = 2$ e valores arbitrários)*
- **Passo a passo:**
  - Escalonamento:
    $$\left[\begin{array}{cccc|c} 1 & 2 & -1 & 1 & 3 \\ 2 & 5 & 1 & -1 & 8 \\ 3 & 7 & 0 & 0 & 11 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 - 2L_1 \\ L_3' = L_3 - 3L_1}} \left[\begin{array}{cccc|c} 1 & 2 & -1 & 1 & 3 \\ 0 & 1 & 3 & -3 & 2 \\ 0 & 1 & 3 & -3 & 2 \end{array}\right] \xrightarrow{L_3' = L_3 - L_2} \left[\begin{array}{cccc|c} 1 & 2 & -1 & 1 & 3 \\ 0 & 1 & 3 & -3 & 2 \\ 0 & 0 & 0 & 0 & 0 \end{array}\right] = B.$$
  - $C_A = 2$, $C_V = 2 \implies C = 2$. Com $n = 4$, temos $g = 4 - 2 = 2$ (`SPI`).
  - Da 2ª linha: $y = 2 - 3z + 3w$. Para $z = 2$ e $w = -1$:
    $$y = 2 - 3(2) + 3(-1) = 2 - 6 - 3 = -7.$$
  - Da 1ª linha: $x = 3 - 2y + z - w = 3 - 2(-7) + 2 - (-1) = 3 + 14 + 2 + 1 = 20$.
- **Resposta Final:** `ca: 2; cv: 2; g: 2; classificacao: SPI; solucao: (20, -7, 2, -1)`
- **Alerta pedagógico:** Não esqueça de contar todas as $n = 4$ incógnitas ($x, y, z, w$) ao calcular $g = n - C$.

---

### `G02-E03` *(Sistema homogêneo com parâmetro quadrático — sem perder raízes)*
- **Passo a passo:**
  - Um sistema homogêneo $3\times 3$ admite solução não-trivial quando $\det(A) = 0$. Desenvolvendo pela 1ª linha (sem Sarrus):
    $$\det\begin{bmatrix} 1 & 1 & -1 \\ 2 & k & 1 \\ k & 2 & 1 \end{bmatrix} = 1(k - 2) - 1(2 - k) - 1(4 - k^2) = k - 2 - 2 + k - 4 + k^2 = k^2 + 2k - 8.$$
  - Fatorando: $k^2 + 2k - 8 = (k + 4)(k - 2) = 0 \implies k = -4$ ou $k = 2$.
- **Resposta Final:** `-4, 2`
- **Alerta pedagógico:** Confira os sinais xadrez $(+,\; -,\; +)$ da 1ª linha ao expandir $\det(A)$.

---

### `G02-E04` *(Discussão paramétrica e solução particular compatível)*
- **Passo a passo:**
  - Escalonando a matriz ampliada:
    $$\left[\begin{array}{ccc|c} 1 & 2 & -1 & 2 \\ 2 & 5 & 1 & a \\ 1 & 3 & 2 & 5 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 - 2L_1 \\ L_3' = L_3 - L_1}} \left[\begin{array}{ccc|c} 1 & 2 & -1 & 2 \\ 0 & 1 & 3 & a - 4 \\ 0 & 1 & 3 & 3 \end{array}\right] \xrightarrow{L_3' = L_3 - L_2} \left[\begin{array}{ccc|c} 1 & 2 & -1 & 2 \\ 0 & 1 & 3 & a - 4 \\ 0 & 0 & 0 & 7 - a \end{array}\right].$$
  - **(a)** Para compatibilidade ($C_A = C_V = 2$), é necessário $7 - a = 0 \implies a = 7$.
  - **(b)** Com $a = 7$, a 2ª linha fica $y + 3z = 3$. Para $z = 1$: $y = 3 - 3(1) = 0$.
    Da 1ª linha: $x = 2 - 2y + z = 2 - 0 + 1 = 3$. Logo $(x, y, z) = (3, 0, 1)$.
- **Resposta Final:** `(a) 7 (b) (3, 0, 1)`
- **Alerta pedagógico:** Acompanhe o parâmetro $a$ em todas as operações elementares sobre a coluna da direita.

---

### `G02-E05` *(Resolução pelo Método da Matriz Inversa $X = A^{-1}B$)*
- **Passo a passo:**
  - **(a)** Calculando $A^{-1}$ via $[A \mid I_3]$:
    $$\left[\begin{array}{ccc|ccc} 1 & 1 & 1 & 1 & 0 & 0 \\ 0 & 2 & 1 & 0 & 1 & 0 \\ 1 & 0 & 2 & 0 & 0 & 1 \end{array}\right] \xrightarrow{L_3' = L_3 - L_1} \left[\begin{array}{ccc|ccc} 1 & 1 & 1 & 1 & 0 & 0 \\ 0 & 2 & 1 & 0 & 1 & 0 \\ 0 & -1 & 1 & -1 & 0 & 1 \end{array}\right] \xrightarrow{L_2 \leftrightarrow L_3,\, L_2(-1)}$$
    $$\left[\begin{array}{ccc|ccc} 1 & 1 & 1 & 1 & 0 & 0 \\ 0 & 1 & -1 & 1 & 0 & -1 \\ 0 & 2 & 1 & 0 & 1 & 0 \end{array}\right] \xrightarrow{L_3' = L_3 - 2L_2} \left[\begin{array}{ccc|ccc} 1 & 1 & 1 & 1 & 0 & 0 \\ 0 & 1 & -1 & 1 & 0 & -1 \\ 0 & 0 & 3 & -2 & 1 & 2 \end{array}\right] \xrightarrow{L_3(1/3)}$$
    $$\left[\begin{array}{ccc|ccc} 1 & 1 & 1 & 1 & 0 & 0 \\ 0 & 1 & -1 & 1 & 0 & -1 \\ 0 & 0 & 1 & -2/3 & 1/3 & 2/3 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_3 \\ L_1' = L_1 - L_3}} \left[\begin{array}{ccc|ccc} 1 & 1 & 0 & 5/3 & -1/3 & -2/3 \\ 0 & 1 & 0 & 1/3 & 1/3 & -1/3 \\ 0 & 0 & 1 & -2/3 & 1/3 & 2/3 \end{array}\right]$$
    $$\xrightarrow{L_1' = L_1 - L_2} \left[\begin{array}{ccc|ccc} 1 & 0 & 0 & 4/3 & -2/3 & -1/3 \\ 0 & 1 & 0 & 1/3 & 1/3 & -1/3 \\ 0 & 0 & 1 & -2/3 & 1/3 & 2/3 \end{array}\right].$$
    Assim, $A^{-1} = \begin{bmatrix} 4/3 & -2/3 & -1/3 \\ 1/3 & 1/3 & -1/3 \\ -2/3 & 1/3 & 2/3 \end{bmatrix}$.
  - **(b)** Calculando $X = A^{-1}B$:
    $$X = \begin{bmatrix} 4/3 & -2/3 & -1/3 \\ 1/3 & 1/3 & -1/3 \\ -2/3 & 1/3 & 2/3 \end{bmatrix}\begin{bmatrix} 4 \\ 3 \\ 5 \end{bmatrix} = \begin{bmatrix} (16 - 6 - 5)/3 \\ (4 + 3 - 5)/3 \\ (-8 + 3 + 10)/3 \end{bmatrix} = \begin{bmatrix} 5/3 \\ 2/3 \\ 5/3 \end{bmatrix}.$$
- **Resposta Final:** `(a) [[4/3, -2/3, -1/3], [1/3, 1/3, -1/3], [-2/3, 1/3, 2/3]] (b) (5/3, 2/3, 5/3)`
- **Alerta pedagógico:** Confira a solução substituindo na 1ª equação: $\frac{5}{3} + \frac{2}{3} + \frac{5}{3} = \frac{12}{3} = 4$.

---

## 2. Checagem Independente

### `G02-C01` *(Classificação por posto $C_A > C_V$)*
- **Passo a passo:**
  $$\left[\begin{array}{ccc|c} 1 & -1 & 2 & 1 \\ 2 & 1 & -1 & 3 \\ 3 & 0 & 1 & 7 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 - 2L_1 \\ L_3' = L_3 - 3L_1}} \left[\begin{array}{ccc|c} 1 & -1 & 2 & 1 \\ 0 & 3 & -5 & 1 \\ 0 & 3 & -5 & 4 \end{array}\right] \xrightarrow{L_3' = L_3 - L_2} \left[\begin{array}{ccc|c} 1 & -1 & 2 & 1 \\ 0 & 3 & -5 & 1 \\ 0 & 0 & 0 & 3 \end{array}\right].$$
  - Na forma de escada $B$, $V$ tem 2 linhas não nulas ($C_V = 2$) e $B$ tem 3 linhas não nulas ($C_A = 3$).
  - Como $C_A > C_V$, o sistema é **incompatível (`SI`)**.
- **Resposta Final:** `ca: 3; cv: 2; classificacao: SI`
- **Alerta pedagógico:** A última linha $[0 \;\; 0 \;\; 0 \mid 3]$ zera em $V$, mas permanece não nula em $B$, produzindo $C_A = 3 > C_V = 2$.

---

### `G02-C02` *(Homogêneo com parâmetro sem consulta)*
- **Passo a passo:**
  - Desenvolvendo $\det(A) = 0$ pela 1ª linha:
    $$\det\begin{bmatrix} 1 & 1 & 1 \\ 2 & k & 2 \\ 1 & 2 & k \end{bmatrix} = 1(k^2 - 4) - 1(2k - 2) + 1(4 - k) = k^2 - 3k + 2 = (k - 1)(k - 2) = 0.$$
  - Portanto, $k = 1$ ou $k = 2$.
- **Resposta Final:** `1, 2`
- **Alerta pedagógico:** Substituindo $k=1$ (1ª e 3ª colunas idênticas) ou $k=2$ (2ª linha $= 2 \times$ 1ª linha), confirma-se imediatamente a dependência entre equações.

---

### `G02-C03` *(Método da matriz inversa $X = A^{-1}B$ sem consulta)*
- **Passo a passo:**
  - **(a)** Redução $[A \mid I_3]$:
    $$\left[\begin{array}{ccc|ccc} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 2 & 1 & 0 & 1 & 0 \\ 1 & 0 & 1 & 0 & 0 & 1 \end{array}\right] \xrightarrow{L_3' = L_3 - L_1} \left[\begin{array}{ccc|ccc} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 2 & 1 & 0 & 1 & 0 \\ 0 & -1 & 1 & -1 & 0 & 1 \end{array}\right] \xrightarrow{L_2 \leftrightarrow L_3,\, L_2(-1)}$$
    $$\left[\begin{array}{ccc|ccc} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 1 & -1 & 1 & 0 & -1 \\ 0 & 2 & 1 & 0 & 1 & 0 \end{array}\right] \xrightarrow{L_3' = L_3 - 2L_2} \left[\begin{array}{ccc|ccc} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 1 & -1 & 1 & 0 & -1 \\ 0 & 0 & 3 & -2 & 1 & 2 \end{array}\right] \xrightarrow{L_3(1/3)}$$
    $$\left[\begin{array}{ccc|ccc} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 1 & -1 & 1 & 0 & -1 \\ 0 & 0 & 1 & -2/3 & 1/3 & 2/3 \end{array}\right] \xrightarrow{L_2' = L_2 + L_3} \left[\begin{array}{ccc|ccc} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 1/3 & 1/3 & -1/3 \\ 0 & 0 & 1 & -2/3 & 1/3 & 2/3 \end{array}\right]$$
    $$\xrightarrow{L_1' = L_1 - L_2} \left[\begin{array}{ccc|ccc} 1 & 0 & 0 & 2/3 & -1/3 & 1/3 \\ 0 & 1 & 0 & 1/3 & 1/3 & -1/3 \\ 0 & 0 & 1 & -2/3 & 1/3 & 2/3 \end{array}\right].$$
    Logo, $A^{-1} = \begin{bmatrix} 2/3 & -1/3 & 1/3 \\ 1/3 & 1/3 & -1/3 \\ -2/3 & 1/3 & 2/3 \end{bmatrix}$.
  - **(b)** Multiplicando $X = A^{-1}B$:
    $$X = \begin{bmatrix} 2/3 & -1/3 & 1/3 \\ 1/3 & 1/3 & -1/3 \\ -2/3 & 1/3 & 2/3 \end{bmatrix}\begin{bmatrix} 3 \\ 5 \\ 4 \end{bmatrix} = \begin{bmatrix} (6 - 5 + 4)/3 \\ (3 + 5 - 4)/3 \\ (-6 + 5 + 8)/3 \end{bmatrix} = \begin{bmatrix} 5/3 \\ 4/3 \\ 7/3 \end{bmatrix}.$$
- **Resposta Final:** `(a) [[2/3, -1/3, 1/3], [1/3, 1/3, -1/3], [-2/3, 1/3, 2/3]] (b) (5/3, 4/3, 7/3)`
- **Alerta pedagógico:** Conferência: $x + y = \frac{5}{3} + \frac{4}{3} = 3$, $2y + z = \frac{8}{3} + \frac{7}{3} = 5$, $x + z = \frac{5}{3} + \frac{7}{3} = 4$.
