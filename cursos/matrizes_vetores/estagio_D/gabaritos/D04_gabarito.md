# Gabarito Comentado — Bloco `D04` (Produto Escalar, Módulo Analítico, Distância e Versor)

> **Bloco de referência:** [D04_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/blocos/D04_bloco.md)  
> **Nota para Caça ao Erro:** Em `D04-E03`, o estudante desprezou a raiz negativa ao extrair $\sqrt{4/9}$.

---

## 1. Gabarito dos Exercícios (`D04-E01` a `D04-E06`)

### `D04-E01` *(Produto escalar, módulo e versor)*
Dados $\vec{u} = (2, -3, 6)$ e $\vec{v} = (-1, 4, 2)$:
- **(a)** $\vec{u}\cdot\vec{v} = 2(-1) + (-3)(4) + 6(2) = -2 - 12 + 12 = \mathbf{-2}$.
- **(b)** $|\vec{u}| = \sqrt{2^2 + (-3)^2 + 6^2} = \sqrt{4 + 9 + 36} = \sqrt{49} = \mathbf{7}$.
- **(c)** $\hat{u} = \frac{\vec{u}}{|\vec{u}|} = \mathbf{\left(\frac{2}{7},\, -\frac{3}{7},\, \frac{6}{7}\right)}$.

### `D04-E02` *(Distância entre pontos e versor)*
$\overrightarrow{AB} = B - A = (3 - 1,\; 0 - (-1),\; 1 - 3) = (2, 1, -2)$.
- **(a)** $d(A, B) = |\overrightarrow{AB}| = \sqrt{2^2 + 1^2 + (-2)^2} = \sqrt{9} = \mathbf{3}$.
- **(b)** $\widehat{AB} = \frac{1}{3}(2, 1, -2) = \mathbf{\left(\frac{2}{3},\, \frac{1}{3},\, -\frac{2}{3}\right)}$.

### `D04-E03` *(Caça ao Erro — Sinal $\pm$ em vetor unitário)*
- **Erro do estudante:** esqueceu que uma equação quadrática $n^2 = k$ ($k > 0$) admite **duas raízes** reais opostas.
- **Resolução correta:**
  $$|\vec{v}|^2 = 1 \implies n^2 + \left(\frac{1}{3}\right)^2 + \left(\frac{2}{3}\right)^2 = 1 \implies n^2 + \frac{5}{9} = 1 \implies n^2 = \frac{4}{9} \implies \mathbf{n = -\frac{2}{3} \text{ ou } n = \frac{2}{3}}.$$

### `D04-E04` *(Equação com produto escalar)*
1. $\vec{u}\cdot\vec{v} = 2a + a(a+1) + (1-a)(-1) = a^2 + 4a - 1$.
2. $\vec{u} + \vec{v} = (a+2,\; 2a+1,\; -a)$, logo:
   $$(\vec{u} + \vec{v})\cdot\vec{w} = (a+2)\cdot 1 + (2a+1)\cdot a + (-a)\cdot 2 = 2a^2 + 2.$$
3. Igualando: $a^2 + 4a - 1 = 2a^2 + 2 \implies a^2 - 4a + 3 = 0 \implies (a-1)(a-3) = 0$.  
Resposta: **$\mathbf{a = 1 \text{ ou } a = 3}$** (`{1, 3}`).

### `D04-E05` *(Parâmetro no módulo)*
$\overrightarrow{AC} = C - A = (1, 2, -2)$ e $\overrightarrow{BC} = C - B = (1, 0, 2)$. Então:
$$\vec{v} = m(1, 2, -2) + (1, 0, 2) = (m + 1,\; 2m,\; -2m + 2).$$
Impondo $|\vec{v}|^2 = 29$:
$$(m + 1)^2 + (2m)^2 + (-2m + 2)^2 = 29 \implies 9m^2 - 6m + 5 = 29 \implies 9m^2 - 6m - 24 = 0 \implies 3m^2 - 2m - 8 = 0.$$
Fatorando $(3m + 4)(m - 2) = 0$:  
Resposta: **$\mathbf{m = -\frac{4}{3} \text{ ou } m = 2}$**.

### `D04-E06` *(Vetor paralelo com produto escalar fixado)*
- **(a)** Como $\vec{v} \parallel \vec{u}$, existe $k \in \mathbb{R}$ tal que $\vec{v} = k\vec{u}$. Assim:
  $$\vec{v}\cdot\vec{u} = k(\vec{u}\cdot\vec{u}) = k|\vec{u}|^2 = k(4 + 1 + 4) = 9k = -27 \implies k = -3.$$
  Logo $\vec{v} = -3(2, -1, 2) = \mathbf{(-6, 3, -6)}$.
- **(b)** $|\vec{u}| = 3 \implies \hat{u} = \mathbf{\left(\frac{2}{3},\, -\frac{1}{3},\, \frac{2}{3}\right)}$.

---

## 2. Gabarito da Checagem Independente (`D04-C01` a `D04-C03`)

### `D04-C01`
- **(a)** $\vec{p}\cdot\vec{q} = 4(1) + (-4)(2) + 2(-2) = 4 - 8 - 4 = \mathbf{-8}$.
- **(b)** $|\vec{p}| = \sqrt{16 + 16 + 4} = \sqrt{36} = \mathbf{6}$.
- **(c)** $\hat{p} = \frac{1}{6}(4, -4, 2) = \mathbf{\left(\frac{2}{3},\, -\frac{2}{3},\, \frac{1}{3}\right)}$.

### `D04-C02`
$$|\vec{v}|^2 = 30 \implies (m+3)^2 + (m-1)^2 + 2^2 = 30 \implies 2m^2 + 4m + 14 = 30 \implies m^2 + 2m - 8 = 0.$$
Logo $(m+4)(m-2) = 0 \implies \mathbf{m = -4 \text{ ou } m = 2}$.

### `D04-C03`
Como $\vec{v}$ é colinear a $\vec{u} = (2, -3, 6)$, escrevemos $\vec{v} = k(2, -3, 6) = (2k, -3k, 6k)$.  
Aplicando $\vec{v}\cdot\vec{w} = -28$ com $\vec{w} = (1, 0, 2)$:
$$2k(1) + (-3k)(0) + 6k(2) = 14k = -28 \implies k = -2.$$
Portanto $\vec{v} = -2(2, -3, 6) = \mathbf{(-4, 6, -12)}$.
