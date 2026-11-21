# Gabarito Comentado e Matriz de Posicionamento — Diagnóstico `MAT121`

> **Referência:** [00_teste_diagnostico.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/00_teste_diagnostico.md).  
> **Regra Central:** Posicione sempre pelo **menor pré-requisito não demonstrado**.

---

## 1. Gabarito Comentado — Etapa 1: Triagem (`T1` a `T6`)

| Item | Estágio | Resposta Exata | Erro Típico / Sinal |
|---|---|---|---|
| **`T1`** | `A` | **(a)** $A\cdot B = \begin{bmatrix} 4 & 7 \\ -6 & 3 \end{bmatrix} \Rightarrow (AB)^T = \begin{bmatrix} 4 & -6 \\ 7 & 3 \end{bmatrix}$.<br>**(b)** $D = \begin{bmatrix} 4 & -1 \\ -1 & 6 \end{bmatrix}$; como $D^T = D$, $D$ é **simétrica**. | Errar produto linha-por-coluna → **`A04`**; errar transposta → **`A06`**; errar simetria → **`A07`**. |
| **`T2`** | `B` | **(a)** Desenvolvendo pela 1ª linha: $\det(M) = 1(3k - 0) - 2(-k - 2) = 5k + 4$. Singular $\Leftrightarrow 5k+4=0 \Rightarrow \mathbf{k = -4/5}$.<br>**(b)** Para $k=1$: $\det(M) = \mathbf{9}$. | Errar matriz de sinais no termo $-2$ → **`B01`/`B02`**; não associar singularidade a $\det = 0$ → **`B05`/`B06`**. |
| **`T3`** | `C` | **(a)** Escalonamento produz $\begin{bmatrix} 1 & 1 & 1 & \mid & 6 \\ 0 & -2 & 0 & \mid & -4 \\ 0 & 0 & 0 & \mid & 0 \end{bmatrix} \sim \begin{bmatrix} 1 & 0 & 1 & \mid & 4 \\ 0 & 1 & 0 & \mid & 2 \\ 0 & 0 & 0 & \mid & 0 \end{bmatrix}$. Assim **$C_A = C_V = C = 2$**, **$g = 3 - 2 = 1$**, **Compatível e Indeterminado (`SPI`)**.<br>**(b)** **$(4 - z,\, 2,\, z)$**, $z \in \mathbb{R}$. | Confundir $C_A$ e $C_V$ ou errar grau de liberdade → **`C05`/`C06`**; errar redução da ampliada → **`C03`**. |
| **`T4`** | `D` | **(a)** $\vec{u}\cdot\vec{v} = 2 - 2 - 4 = \mathbf{-4} \neq 0 \Rightarrow$ **não são ortogonais** (ângulo obtuso).<br>**(b)** $\vec{u}\times\vec{v} = \mathbf{(-2,\, 6,\, 5)}$; área $= |\vec{u}\times\vec{v}| = \mathbf{\sqrt{65}}$. | Errar sinal do componente $\hat{\jmath}$ no produto vetorial → **`D07`**; errar ortogonalidade → **`D05`**. |
| **`T5`** | `E` | **(a)** $\vec{n} = \mathbf{(2, -1, 2)}$ (qualquer múltiplo não nulo). $2(1)-3+2(-1)-6 = -9 \neq 0 \Rightarrow \mathbf{P_0 \notin \pi}$.<br>**(b)** $d(P_0, \pi) = \frac{|-9|}{\sqrt{4+1+4}} = \frac{9}{3} = \mathbf{3}$. | Esquecer valor absoluto no numerador ou errar módulo de $\vec{n}$ → **`E04`/`E09`**. |
| **`T6`** | `F` | $9(x-3)^2 - 4(y-1)^2 = -36 \Rightarrow \mathbf{\frac{(y-1)^2}{9} - \frac{(x-3)^2}{4} = 1}$. **Hipérbole** de eixo real vertical, centro **$C(3, 1)$**, $a=3, b=2, c=\sqrt{13}$, excentricidade **$e = \frac{\sqrt{13}}{3}$**. | Errar sinal negativo ao fatorar $-4(y^2-2y)$ ou esquecer de inverter o eixo ao dividir por $-36$ → **`F05`/`F06`**. |

---

## 2. Gabarito Comentado — Etapa 2: Sondagens (`S-A` a `S-F`)

### Sondagem `S-A`
- **`SA-01` (Âncora):** $A = \begin{bmatrix} 1 & 0 & -1 \\ 3 & 2 & 1 \end{bmatrix}$ e $A^T = \begin{bmatrix} 1 & 3 \\ 0 & 2 \\ -1 & 1 \end{bmatrix}$. *(Falha → **`A01`** ou **`A06`** se apenas errou transposta.)*
- **`SA-02`:** $m^2 = 81 \Rightarrow \mathbf{m = \pm 9}$; $n^2 = 9 \Rightarrow \mathbf{n = \pm 3}$. *(Esquecer sinal $\pm$ → **`A02`**.)*
- **`SA-03`:** $H^2 = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} = O \Rightarrow$ **nilpotente** (de índice 2). *(Falha → **`A08`**.)*

### Sondagem `S-B`
- **`SB-01` (Âncora):** Pela 2ª linha: $-0 + 4(10-3) - (-2)(4 - (-1)) = 4(7) + 2(5) = \mathbf{38}$ *(ou pela 1ª linha: $2(20-(-4)) - (-1)(0 - (-2)) + 3(0-4) = 48 + 2 - 12 = 38$)*. *(Falha → **`B01`/`B02`**.)*
- **`SB-02`:** $\det(B \cdot A^T) = \det(B)\det(A^T) = (-2)(5) = \mathbf{-10}$. Como o determinante não é operador linear, em geral $\det(A+B) \neq \det(A)+\det(B)$ (ex.: $I_2 + I_2 = 2I_2$ tem $\det=4 \neq 1+1=2$). *(Falha → **`B03`**.)*
- **`SB-03`:** $\det(P) = 6 - 5 = 1$, logo $P^{-1} = \begin{bmatrix} 2 & -5 \\ -1 & 3 \end{bmatrix}$ (via `[P|I] -> [I|P^{-1}]`). Na equação $DX^T = DC$, multiplicando à esquerda por $D^{-1}$ tem-se $X^T = C \Rightarrow \mathbf{X = C^T}$. *(Falha em $P^{-1}$ → **`B07`**; falha na equação → **`B08`**.)*

### Sondagem `S-C`
- **`SC-01` (Âncora):** Sistema escalonado dá **$x = 3,\, y = 1$** (`(3, 1)`). *(Falha → **`C01`–`C03`**.)*
- **`SC-02`:** Solução não-trivial em homogêneo $3\times 3$ exige $\det = 0$: $\det = 1(k-2) - 1(2k-3) - 1(4-3) = -k + 1 - 1 = -k \Rightarrow \mathbf{k = 0}$ *(Conferência: se $k=0$, $L_1+L_2 = (3,2,0) = L_3$! Exato.)*. *(Falha → **`C06`**.)*
- **`SC-03`:** $\begin{bmatrix} 1 & -2 & \mid & a \\ 2 & 1 & \mid & b \\ 3 & -1 & \mid & c \end{bmatrix} \xrightarrow{L_2'=L_2-2L_1,\, L_3'=L_3-3L_1} \begin{bmatrix} 1 & -2 & \mid & a \\ 0 & 5 & \mid & b-2a \\ 0 & 5 & \mid & c-3a \end{bmatrix} \xrightarrow{L_3''=L_3'-L_2'} \begin{bmatrix} 1 & -2 & \mid & a \\ 0 & 5 & \mid & b-2a \\ 0 & 0 & \mid & c-a-b \end{bmatrix}$. Compatível $\Leftrightarrow C_A = C_V \Leftrightarrow \mathbf{c - a - b = 0}$ (ou $c = a + b$). *(Falha → **`C07`**.)*

### Sondagem `S-D`
- **`SD-01` (Âncora):** $\overrightarrow{AB} = B - A = \mathbf{(2, 4, -4)}$; $|\overrightarrow{AB}| = \sqrt{4+16+16} = 6$; versor $\widehat{AB} = \mathbf{(1/3,\, 2/3,\, -2/3)}$. *(Falha → **`D02`/`D04`**.)*
- **`SD-02`:** $\vec{u}\cdot\vec{v} = 2 + 0 - 1 = 1$, $|\vec{v}|^2 = 1+0+1 = 2$, logo $\operatorname{proj}_{\vec{v}}\vec{u} = \frac{1}{2}(1, 0, -1) = \mathbf{(1/2,\, 0,\, -1/2)}$. *(Falha → **`D06`**.)*
- **`SD-03`:** $(\vec{u},\vec{v},\vec{w}) = \det\begin{bmatrix} 1 & 2 & -1 \\ 2 & -1 & 3 \\ 1 & -8 & 7 \end{bmatrix} = 1(-7+24) - 2(14-3) - 1(-16+1) = 17 - 22 + 15 = \mathbf{10} \neq 0 \Rightarrow$ **não são coplanares**. Volume do tetraedro: $V = \frac{|10|}{6} = \mathbf{5/3}$. *(Falha → **`D09`**.)*

### Sondagem `S-E`
- **`SE-01` (Âncora):** $\vec{v} = \overrightarrow{AB} = (2, -1, 1)$. Paramétricas: **$x = 2 + 2t,\; y = 1 - t,\; z = -3 + t$**. Reduzidas em $x$: $t = \frac{x-2}{2} \Rightarrow \mathbf{y = -\frac{1}{2}x + 2,\; z = \frac{1}{2}x - 4}$. *(Falha → **`E01`**.)*
- **`SE-02`:** $\vec{n} = \vec{v}_r = (2, -1, 3)$. Usando $A(1,0,2)$: $2(x-1) - 1(y-0) + 3(z-2) = 0 \Rightarrow \mathbf{2x - y + 3z - 8 = 0}$. *(Falha → **`E04`**.)*
- **`SE-03`:** Dividindo $\pi_2$ por 2: $\pi_2: x - 2y + 2z + 3 = 0$. Coeficientes normalizados: $d = \frac{|-3 - 3|}{\sqrt{1+4+4}} = \frac{6}{3} = \mathbf{2}$. *(Errar divisão por 2 antes da fórmula → **`E09`**.)*

### Sondagem `S-F`
- **`SF-01` (Âncora):** $(y+3)^2 - 9 = 8x - 1 \Rightarrow (y+3)^2 = 8(x-1)$, logo $2p = 8 \Rightarrow p/2 = 2$. Vértice **$V(1, -3)$**, foco **$F(3, -3)$**, diretriz **$x = -1$**. *(Falha → **`F02`**.)*
- **`SF-02`:** $c = 3$, $2a = 8 \Rightarrow a = 4$, $b^2 = a^2 - c^2 = 16 - 9 = 7$. Equação: **$\frac{x^2}{16} + \frac{y^2}{7} = 1$**; excentricidade **$e = 3/4$**. *(Falha → **`F03`**.)*
- **`SF-03`:** Traço em $z=0$ é a elipse $\frac{x^2}{4} + \frac{y^2}{9} = 1$; traço em $x=0$ é a hipérbole $\frac{y^2}{9} - \frac{z^2}{16} = 1$. Logo é um **hiperboloide de uma folha** ao longo do eixo $z$. *(Falha → **`F07`**.)*

---

## 3. Matriz de Decisão de Posicionamento

| Desempenho na Triagem (`T1`–`T6`) | Resultado da Sondagem Aplicada | Bloco de Entrada Recomendado |
|---|---|---|
| Errou `T1` ou nunca estudou Matrizes | Erra `SA-01` / Nunca estudou | **`A01`** *(Definitivo)* |
| Passou em `T1` (`A`), falhou em `T2` (`B`) | Falha `SB-01` → **`B01`**; passa `SB-01` e erra `SB-02`/`SB-03` → **`B03`/`B07`** | **`B01`**, **`B03`** ou **`B07`** |
| Passou `T1`–`T2`, falhou em `T3` (`C`) | Falha `SC-01` → **`C01`**; passa `SC-01` e erra `SC-02`/`SC-03` → **`C06`/`C07`** | **`C01`**, **`C06`** ou **`C07`** |
| Passou `T1`–`T3`, falhou em `T4` (`D`) | Falha `SD-01` → **`D01`**; erra `SD-02`/`SD-03` → **`D06`/`D09`** | **`D01`**, **`D06`** ou **`D09`** |
| Passou `T1`–`T4`, falhou em `T5` (`E`) | Falha `SE-01` → **`E01`**; erra `SE-02`/`SE-03` → **`E04`/`E09`** | **`E01`**, **`E04`** ou **`E09`** |
| Passou `T1`–`T5`, falhou em `T6` (`F`) | Falha `SF-01` → **`F01`**; erra `SF-02`/`SF-03` → **`F03`/`F07`** | **`F01`**, **`F03`** ou **`F07`** |
| Passou `T1`–`T6` integralmente (sem consulta) | Confirma fluência nos simulados | **`G01`** (revisão rápida P1→P3) |
