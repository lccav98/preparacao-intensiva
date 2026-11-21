# Gabarito Comentado — Bloco `G03` (Simulado Integrador P2 — Parte 2: Vetores e Produtos)

> **Bloco de referência:** [G03_bloco.md](../blocos/G03_bloco.md)

---

## 1. Exercícios

### `G03-E01` *(Combinação linear e colinearidade de três pontos)*
- **Passo a passo:**
  - **(a)** De $a_1(1, 0, 1) + a_2(0, 1, 1) + a_3(1, -1, 1) = (5, -1, 7)$:
    $$\begin{cases} a_1 + a_3 = 5 \\ a_2 - a_3 = -1 \\ a_1 + a_2 + a_3 = 7 \end{cases}$$
    Subtraindo a 1ª equação da 3ª: $a_2 = 7 - 5 = 2$.
    Da 2ª: $2 - a_3 = -1 \implies a_3 = 3$.
    Da 1ª: $a_1 = 5 - 3 = 2$. Logo $(a_1, a_2, a_3) = (2, 2, 3)$.
  - **(b)** $\overrightarrow{AB} = B - A = (2, -2, 2)$ e $\overrightarrow{AC} = C - A = (4, m - 2, n + 1)$.
    Para colinearidade, $\overrightarrow{AC} = k\,\overrightarrow{AB}$. Pela 1ª coordenada, $4 = 2k \implies k = 2$.
    Logo, $m - 2 = 2(-2) = -4 \implies m = -2$, e $n + 1 = 2(2) = 4 \implies n = 3$.
- **Resposta Final:** `(a) (2, 2, 3) (b) (-2, 3)`
- **Alerta pedagógico:** Na colinearidade, use sempre dois vetores com um vértice comum ($\overrightarrow{AB}$ e $\overrightarrow{AC}$) e garanta o mesmo escalar $k$ em todas as coordenadas.

---

### `G03-E02` *(Ângulo interno de triângulo e projeção ortogonal)*
- **Passo a passo:**
  - Vetores saindo do vértice $A$:
    $$\overrightarrow{AB} = B - A = (2, 0, 2), \qquad \overrightarrow{AC} = C - A = (2, 2, 0).$$
  - **(a)** Produto escalar e módulos:
    $$\overrightarrow{AB}\cdot\overrightarrow{AC} = 2(2) + 0(2) + 2(0) = 4, \quad |\overrightarrow{AB}| = \sqrt{8} = 2\sqrt{2}, \quad |\overrightarrow{AC}| = \sqrt{8} = 2\sqrt{2}.$$
    $$\cos\hat{A} = \frac{4}{2\sqrt{2}\cdot 2\sqrt{2}} = \frac{4}{8} = \frac{1}{2} \implies \hat{A} = 60^\circ.$$
  - **(b)** Projeção ortogonal:
    $$\operatorname{proj}_{\overrightarrow{AC}}\overrightarrow{AB} = \left(\frac{\overrightarrow{AB}\cdot\overrightarrow{AC}}{|\overrightarrow{AC}|^2}\right)\overrightarrow{AC} = \frac{4}{8}(2, 2, 0) = \frac{1}{2}(2, 2, 0) = (1, 1, 0).$$
- **Resposta Final:** `(a) 60° (b) (1, 1, 0)`
- **Alerta pedagógico:** Se tivesse tomado $\overrightarrow{BA}$ em vez de $\overrightarrow{AB}$, o ângulo calculado seria $120^\circ$ (suplementar).

---

### `G03-E03` *(Área do triângulo `1/2` e altura relativa à base)*
- **Passo a passo:**
  - $\overrightarrow{PQ} = Q - P = (2, 2, -1)$ e $\overrightarrow{PR} = R - P = (1, -1, 2)$.
  - Desenvolvendo pela 1ª linha:
    $$\overrightarrow{PQ}\times\overrightarrow{PR} = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ 2 & 2 & -1 \\ 1 & -1 & 2 \end{vmatrix} = (4 - 1)\hat{\imath} - (4 + 1)\hat{\jmath} + (-2 - 2)\hat{k} = (3, -5, -4).$$
  - Módulo: $|\overrightarrow{PQ}\times\overrightarrow{PR}| = \sqrt{3^2 + (-5)^2 + (-4)^2} = \sqrt{9 + 25 + 16} = \sqrt{50} = 5\sqrt{2}$.
  - **(a)** Área do triângulo $PQR$:
    $$A_{\triangle} = \frac{1}{2}|\overrightarrow{PQ}\times\overrightarrow{PR}| = \frac{5\sqrt{2}}{2}.$$
  - **(b)** Como $|\overrightarrow{PQ}| = \sqrt{4 + 4 + 1} = 3$, a altura sobre $PQ$ é:
    $$h = \frac{|\overrightarrow{PQ}\times\overrightarrow{PR}|}{|\overrightarrow{PQ}|} = \frac{5\sqrt{2}}{3}.$$
- **Resposta Final:** `(a) 5*sqrt(2)/2 (b) 5*sqrt(2)/3`
- **Alerta pedagógico:** A altura do triângulo é $h = \frac{2 A_{\triangle}}{\text{base}} = \frac{|\overrightarrow{PQ}\times\overrightarrow{PR}|}{|\overrightarrow{PQ}|}$, e não $\frac{A_{\triangle}}{\text{base}}$.

---

### `G03-E04` *(Volume do tetraedro `1/6` e teste de coplanaridade de 4 pontos)*
- **Passo a passo:**
  - Vetores partindo de $A(1, 0, 1)$:
    $$\overrightarrow{AB} = (1, 1, -1), \qquad \overrightarrow{AC} = (-1, 2, 0), \qquad \overrightarrow{AD} = (2, 3, 1).$$
  - Produto misto pela 1ª linha:
    $$(\overrightarrow{AB}, \overrightarrow{AC}, \overrightarrow{AD}) = \begin{vmatrix} 1 & 1 & -1 \\ -1 & 2 & 0 \\ 2 & 3 & 1 \end{vmatrix} = 1(2 - 0) - 1(-1 - 0) - 1(-3 - 4) = 2 + 1 + 7 = 10.$$
  - **(a)** Volume do tetraedro:
    $$V_{\text{tetra}} = \frac{1}{6}|10| = \frac{5}{3}.$$
  - **(b)** Como o produto misto é diferente de zero ($10 \neq 0$), os 4 pontos **não são coplanares**.
- **Resposta Final:** `(a) 5/3 (b) nao coplanares`
- **Alerta pedagógico:** Nunca esqueça o fator $\frac{1}{6}$ no volume do tetraedro (o paralelepípedo tem volume $10$, o tetraedro tem $\frac{1}{6}$ disso).

---

### `G03-E05` *(Parâmetro em volume de tetraedro — duas soluções)*
- **Passo a passo:**
  - Vetores partindo de $A(0,0,0)$: $\overrightarrow{AB} = (2, 1, 0)$, $\overrightarrow{AC} = (1, 3, 1)$, $\overrightarrow{AD} = (1, 2, k)$.
  - Produto misto pela 1ª linha:
    $$(\overrightarrow{AB}, \overrightarrow{AC}, \overrightarrow{AD}) = \begin{vmatrix} 2 & 1 & 0 \\ 1 & 3 & 1 \\ 1 & 2 & k \end{vmatrix} = 2(3k - 2) - 1(k - 1) + 0 = 5k - 3.$$
  - Igualando ao volume $2$:
    $$\frac{1}{6}|5k - 3| = 2 \iff |5k - 3| = 12.$$
    - Caso 1: $5k - 3 = 12 \implies 5k = 15 \implies k = 3$.
    - Caso 2: $5k - 3 = -12 \implies 5k = -9 \implies k = -\frac{9}{5}$.
- **Resposta Final:** `-9/5, 3`
- **Alerta pedagógico:** O valor absoluto no volume gera sempre duas soluções lineares; descartar o caso $-12$ elimina metade da resposta.

---

## 2. Checagem Independente

### `G03-C01` *(Projeção ortogonal e parcela ortogonal)*
- **Passo a passo:**
  - $\vec{v}\cdot\vec{u} = 2(1) + 1(-2) + (-2)(2) = 2 - 2 - 4 = -4$, e $|\vec{u}|^2 = 1^2 + (-2)^2 + 2^2 = 9$.
  - **(a)** $\operatorname{proj}_{\vec{u}}\vec{v} = \frac{-4}{9}(1, -2, 2) = \left(-\frac{4}{9},\; \frac{8}{9},\; -\frac{8}{9}\right)$.
  - **(b)** $\vec{v}_\perp = \vec{v} - \operatorname{proj}_{\vec{u}}\vec{v} = (2, 1, -2) - \left(-\frac{4}{9}, \frac{8}{9}, -\frac{8}{9}\right) = \left(\frac{22}{9},\; \frac{1}{9},\; -\frac{10}{9}\right)$.
    *(Conferência: $\vec{v}_\perp \cdot \vec{u} = \frac{22 - 2 - 20}{9} = 0$.)*
- **Resposta Final:** `(a) (-4/9, 8/9, -8/9) (b) (22/9, 1/9, -10/9)`
- **Alerta pedagógico:** O denominador de $\operatorname{proj}_{\vec{u}}\vec{v}$ é $|\vec{u}|^2 = 9$ (e não $|\vec{u}| = 3$); confira sempre que $\vec{v}_\perp \cdot \vec{u} = 0$.

---

### `G03-C02` *(Área de triângulo e versor ortogonal)*
- **Passo a passo:**
  - $\overrightarrow{AB} = (2, 0, -2)$ e $\overrightarrow{AC} = (1, 2, 0)$.
  - Produto vetorial pela 1ª linha:
    $$\overrightarrow{AB}\times\overrightarrow{AC} = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ 2 & 0 & -2 \\ 1 & 2 & 0 \end{vmatrix} = (0 + 4)\hat{\imath} - (0 + 2)\hat{\jmath} + (4 - 0)\hat{k} = (4, -2, 4).$$
  - Módulo: $|\overrightarrow{AB}\times\overrightarrow{AC}| = \sqrt{16 + 4 + 16} = \sqrt{36} = 6$.
  - **(a)** Área do triângulo: $A_{\triangle} = \frac{1}{2}(6) = 3$.
  - **(b)** Versor de $\overrightarrow{AB}\times\overrightarrow{AC}$:
    $$\hat{n} = \frac{(4, -2, 4)}{6} = \left(\frac{2}{3},\; -\frac{1}{3},\; \frac{2}{3}\right).$$
- **Resposta Final:** `(a) 3 (b) (2/3, -1/3, 2/3)`
- **Alerta pedagógico:** O versor tem módulo unitário: $(2/3)^2 + (-1/3)^2 + (2/3)^2 = 9/9 = 1$.

---

### `G03-C03` *(Parâmetro em volume de tetraedro sem consulta)*
- **Passo a passo:**
  - Produto misto pela 1ª linha:
    $$(\vec{u}, \vec{v}, \vec{w}) = \begin{vmatrix} 1 & 1 & 0 \\ 0 & 2 & 1 \\ m & 1 & 3 \end{vmatrix} = 1(6 - 1) - 1(0 - m) + 0 = m + 5.$$
  - Igualando ao volume $\frac{5}{3}$:
    $$\frac{1}{6}|m + 5| = \frac{5}{3} \iff |m + 5| = 10.$$
    - $m + 5 = 10 \implies m = 5$.
    - $m + 5 = -10 \implies m = -15$.
- **Resposta Final:** `-15, 5`
- **Alerta pedagógico:** Não troque $\frac{1}{6}|m+5|$ por $|m+5|$ (volume do paralelepípedo) e resolva ambos os sinais de $|m+5| = 10$.
