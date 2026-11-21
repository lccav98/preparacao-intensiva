# Gabarito Comentado — Bloco `C03` (Método de Gauss-Jordan na Matriz Ampliada `n × n`)

> **Bloco de referência:** [C03_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_C/blocos/C03_bloco.md)  
> **Nota para Caça ao Bug (`C03-E03`):** Erro clássico de sinal ao normalizar `L_3(-1/4)` sobre `-12` (`-12 * (-1/4) = +3`, e não `-3`).

---

## 1. Gabarito dos Exercícios (`C03-E01` a `C03-E05`)

### `C03-E01` *(Lista 5 Ex. 2)*
$$A = \left[\begin{array}{ccc|c} 3 & 2 & -5 & 8 \\ 2 & -4 & -2 & -4 \\ 1 & -2 & -3 & -4 \end{array}\right] \xrightarrow{L_{13}} \left[\begin{array}{ccc|c} 1 & -2 & -3 & -4 \\ 2 & -4 & -2 & -4 \\ 3 & 2 & -5 & 8 \end{array}\right]$$
$$\xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(-3)}} \left[\begin{array}{ccc|c} 1 & -2 & -3 & -4 \\ 0 & 0 & 4 & 4 \\ 0 & 8 & 4 & 20 \end{array}\right] \xrightarrow{L_{23},\; L_2(1/8),\; L_3(1/4)} \left[\begin{array}{ccc|c} 1 & -2 & -3 & -4 \\ 0 & 1 & 1/2 & 5/2 \\ 0 & 0 & 1 & 1 \end{array}\right]$$
$$\xrightarrow{L_1' = L_1 + L_2(2)} \left[\begin{array}{ccc|c} 1 & 0 & -2 & 1 \\ 0 & 1 & 1/2 & 5/2 \\ 0 & 0 & 1 & 1 \end{array}\right] \xrightarrow{\substack{L_1' = L_1 + L_3(2) \\ L_2' = L_2 + L_3(-1/2)}} \left[\begin{array}{ccc|c} 1 & 0 & 0 & 3 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 1 & 1 \end{array}\right]$$
- **Classificação:** `SPD` *(Compatível e Determinado)*.
- **Resposta final:** `classificacao: SPD; solucao: (3, 2, 1)`.

### `C03-E02` *(Lista 5 Ex. 5)*
$$A = \left[\begin{array}{ccc|c} 1 & 0 & 3 & -8 \\ 2 & -4 & 0 & -4 \\ 3 & -2 & -5 & 26 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(-3)}} \left[\begin{array}{ccc|c} 1 & 0 & 3 & -8 \\ 0 & -4 & -6 & 12 \\ 0 & -2 & -14 & 50 \end{array}\right] \xrightarrow{L_2(-1/4)} \left[\begin{array}{ccc|c} 1 & 0 & 3 & -8 \\ 0 & 1 & 3/2 & -3 \\ 0 & -2 & -14 & 50 \end{array}\right]$$
$$\xrightarrow{L_3' = L_3 + L_2(2)} \left[\begin{array}{ccc|c} 1 & 0 & 3 & -8 \\ 0 & 1 & 3/2 & -3 \\ 0 & 0 & -11 & 44 \end{array}\right] \xrightarrow{L_3(-1/11)} \left[\begin{array}{ccc|c} 1 & 0 & 3 & -8 \\ 0 & 1 & 3/2 & -3 \\ 0 & 0 & 1 & -4 \end{array}\right] \xrightarrow{\substack{L_1' = L_1 + L_3(-3) \\ L_2' = L_2 + L_3(-3/2)}} \left[\begin{array}{ccc|c} 1 & 0 & 0 & 4 \\ 0 & 1 & 0 & 3 \\ 0 & 0 & 1 & -4 \end{array}\right]$$
- **Resposta final:** `(4, 3, -4)`.

### `C03-E03` *(Caça ao Bug)*
- **Diagnóstico:** Na linha `[0  0  -4 | -12]`, aplicar $L_3(-1/4)$ resulta em $(-12)\cdot(-1/4) = +3$, e não $-3$. Com $z = 3$, as reduções acima produzem $y = -5$ e $x = 2$. *(Conferência: $2(2) + (-5) + 3(3) = 4 - 5 + 9 = 8$.)*
- **Resposta final:** `(2, -5, 3)`.

### `C03-E04`
$$A = \left[\begin{array}{ccc|c} 1 & 2 & -1 & 3 \\ 2 & 5 & 1 & 7 \\ 3 & 7 & 0 & 12 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(-3)}} \left[\begin{array}{ccc|c} 1 & 2 & -1 & 3 \\ 0 & 1 & 3 & 1 \\ 0 & 1 & 3 & 3 \end{array}\right] \xrightarrow{\substack{L_1' = L_1 + L_2(-2) \\ L_3' = L_3 + L_2(-1)}} \left[\begin{array}{ccc|c} 1 & 0 & -7 & 1 \\ 0 & 1 & 3 & 1 \\ 0 & 0 & 0 & 2 \end{array}\right]$$
A última equação é $0x + 0y + 0z = 2$ (absurdo).
- **Resposta final:** `SI` *(Sistema Incompatível)*.

### `C03-E05`
$$A = \left[\begin{array}{ccc|c} 2 & 4 & -2 & 3 \\ 4 & 6 & 2 & 5 \\ 2 & -2 & 4 & 1 \end{array}\right] \xrightarrow{L_1(1/2)} \left[\begin{array}{ccc|c} 1 & 2 & -1 & 3/2 \\ 4 & 6 & 2 & 5 \\ 2 & -2 & 4 & 1 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-4) \\ L_3' = L_3 + L_1(-2)}} \left[\begin{array}{ccc|c} 1 & 2 & -1 & 3/2 \\ 0 & -2 & 6 & -1 \\ 0 & -6 & 6 & -2 \end{array}\right]$$
$$\xrightarrow{L_2(-1/2)} \left[\begin{array}{ccc|c} 1 & 2 & -1 & 3/2 \\ 0 & 1 & -3 & 1/2 \\ 0 & -6 & 6 & -2 \end{array}\right] \xrightarrow{\substack{L_1' = L_1 + L_2(-2) \\ L_3' = L_3 + L_2(6)}} \left[\begin{array}{ccc|c} 1 & 0 & 5 & 1/2 \\ 0 & 1 & -3 & 1/2 \\ 0 & 0 & -12 & 1 \end{array}\right]$$
$$\xrightarrow{L_3(-1/12)} \left[\begin{array}{ccc|c} 1 & 0 & 5 & 1/2 \\ 0 & 1 & -3 & 1/2 \\ 0 & 0 & 1 & -1/12 \end{array}\right] \xrightarrow{\substack{L_1' = L_1 + L_3(-5) \\ L_2' = L_2 + L_3(3)}} \left[\begin{array}{ccc|c} 1 & 0 & 0 & 11/12 \\ 0 & 1 & 0 & 1/4 \\ 0 & 0 & 1 & -1/12 \end{array}\right]$$
- **Resposta final:** `(11/12, 1/4, -1/12)`.

---

## 2. Gabarito da Checagem Independente (`C03-C01` a `C03-C03`)

### `C03-C01`
$$A = \left[\begin{array}{ccc|c} 2 & 2 & -2 & 1 \\ 2 & -2 & 2 & 5 \\ 3 & 1 & 2 & 5 \end{array}\right] \xrightarrow{L_1(1/2)} \left[\begin{array}{ccc|c} 1 & 1 & -1 & 1/2 \\ 2 & -2 & 2 & 5 \\ 3 & 1 & 2 & 5 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(-3)}} \left[\begin{array}{ccc|c} 1 & 1 & -1 & 1/2 \\ 0 & -4 & 4 & 4 \\ 0 & -2 & 5 & 7/2 \end{array}\right]$$
$$\xrightarrow{L_2(-1/4)} \left[\begin{array}{ccc|c} 1 & 1 & -1 & 1/2 \\ 0 & 1 & -1 & -1 \\ 0 & -2 & 5 & 7/2 \end{array}\right] \xrightarrow{\substack{L_1' = L_1 + L_2(-1) \\ L_3' = L_3 + L_2(2)}} \left[\begin{array}{ccc|c} 1 & 0 & 0 & 3/2 \\ 0 & 1 & -1 & -1 \\ 0 & 0 & 3 & 3/2 \end{array}\right]$$
$$\xrightarrow{L_3(1/3)} \left[\begin{array}{ccc|c} 1 & 0 & 0 & 3/2 \\ 0 & 1 & -1 & -1 \\ 0 & 0 & 1 & 1/2 \end{array}\right] \xrightarrow{L_2' = L_2 + L_3(1)} \left[\begin{array}{ccc|c} 1 & 0 & 0 & 3/2 \\ 0 & 1 & 0 & -1/2 \\ 0 & 0 & 1 & 1/2 \end{array}\right]$$
- **Resposta final:** `classificacao: SPD; solucao: (3/2, -1/2, 1/2)`.

### `C03-C02` *(Lista 5 Ex. 3)*
$$A = \left[\begin{array}{ccc|c} 2 & 4 & 6 & -6 \\ 3 & -2 & -4 & -38 \\ 1 & 2 & 3 & -3 \end{array}\right] \xrightarrow{L_{13}} \left[\begin{array}{ccc|c} 1 & 2 & 3 & -3 \\ 3 & -2 & -4 & -38 \\ 2 & 4 & 6 & -6 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-3) \\ L_3' = L_3 + L_1(-2)}} \left[\begin{array}{ccc|c} 1 & 2 & 3 & -3 \\ 0 & -8 & -13 & -29 \\ 0 & 0 & 0 & 0 \end{array}\right]$$
$$\xrightarrow{L_2(-1/8)} \left[\begin{array}{ccc|c} 1 & 2 & 3 & -3 \\ 0 & 1 & 13/8 & 29/8 \\ 0 & 0 & 0 & 0 \end{array}\right] \xrightarrow{L_1' = L_1 + L_2(-2)} \left[\begin{array}{ccc|c} 1 & 0 & -1/4 & -41/4 \\ 0 & 1 & 13/8 & 29/8 \\ 0 & 0 & 0 & 0 \end{array}\right]$$
- **(a)** Linha nula inteira sem absurdo e $2$ pivôs para $3$ variáveis $\Rightarrow$ **`SPI`** *(Compatível e Indeterminado)*.
- **(b)** Solução geral: $x = \frac{-41 + z}{4}$, $y = \frac{29 - 13z}{8}$, $z \in \mathbb{R}$. Para $z = 1$: $x = \frac{-40}{4} = -10$, $y = \frac{16}{8} = 2$.
- **Resposta final:** `classificacao: SPI; solucao_z1: (-10, 2, 1)`.

### `C03-C03`
$$A = \left[\begin{array}{ccc|c} 1 & -2 & 1 & 4 \\ 2 & -3 & 4 & 7 \\ 3 & -5 & 5 & 9 \end{array}\right] \xrightarrow{\substack{L_2' = L_2 + L_1(-2) \\ L_3' = L_3 + L_1(-3)}} \left[\begin{array}{ccc|c} 1 & -2 & 1 & 4 \\ 0 & 1 & 2 & -1 \\ 0 & 1 & 2 & -3 \end{array}\right] \xrightarrow{\substack{L_1' = L_1 + L_2(2) \\ L_3' = L_3 + L_2(-1)}} \left[\begin{array}{ccc|c} 1 & 0 & 5 & 2 \\ 0 & 1 & 2 & -1 \\ 0 & 0 & 0 & -2 \end{array}\right]$$
Última linha: $0 = -2$ (absurdo).
- **Resposta final:** `SI`.
