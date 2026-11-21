# Gabarito Comentado — Bloco `D05` (Ângulo entre Vetores, Ortogonalidade e Cossenos Diretores)

> **Bloco de referência:** [D05_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/blocos/D05_bloco.md)  
> **Nota para Caça ao Erro:** Em `D05-E03`, o estudante não partiu do vértice comum $B$, medindo o suplementar ($120^\circ$) em vez do ângulo interno ($60^\circ$).

---

## 1. Gabarito dos Exercícios (`D05-E01` a `D05-E06`)

### `D05-E01` *(Cosseno e classificação do ângulo)*
- $\vec{u}\cdot\vec{v} = 1(2) + 2(-1) + (-2)(2) = 2 - 2 - 4 = -4$.
- $|\vec{u}| = \sqrt{1 + 4 + 4} = 3$ e $|\vec{v}| = \sqrt{4 + 1 + 4} = 3$.
- **(a)** $\cos\theta = \frac{-4}{3 \cdot 3} = \mathbf{-\frac{4}{9}}$.
- **(b)** Como $\cos\theta < 0$, o ângulo é **obtuso**.

### `D05-E02` *(Ortogonalidade com parâmetro)*
$$\vec{a} \perp \vec{b} \iff \vec{a}\cdot\vec{b} = 0 \implies \alpha(\alpha - 2) + 3(1) + (-3)(2) = 0.$$
$$\alpha^2 - 2\alpha - 3 = 0 \implies (\alpha + 1)(\alpha - 3) = 0 \implies \mathbf{\alpha = -1 \text{ ou } \alpha = 3}.$$

### `D05-E03` *(Caça ao Erro — Ângulo interno em triângulo)*
- **Erro do estudante:** usou $\overrightarrow{AB}$ (terminando em $B$) e $\overrightarrow{BC}$ (partindo de $B$), calculando o ângulo suplementar externo.
- **Resolução correta (vetores partindo de $B$):**
  $$\overrightarrow{BA} = A - B = (2, 2, 0), \qquad \overrightarrow{BC} = C - B = (2, 0, 2).$$
  $$\overrightarrow{BA}\cdot\overrightarrow{BC} = 4 + 0 + 0 = 4, \qquad |\overrightarrow{BA}| = \sqrt{8} = 2\sqrt{2}, \qquad |\overrightarrow{BC}| = \sqrt{8} = 2\sqrt{2}.$$
- **(a)** $\cos\hat{B} = \frac{4}{2\sqrt{2}\cdot 2\sqrt{2}} = \frac{4}{8} = \mathbf{\frac{1}{2}}$.
- **(b)** $\hat{B} = \arccos\left(\frac{1}{2}\right) = \mathbf{60^\circ}$.

### `D05-E04` *(Cossenos diretores)*
$|\vec{v}| = \sqrt{2^2 + (-1)^2 + 2^2} = \sqrt{9} = 3$.
- **(a)** $(\cos\alpha,\, \cos\beta,\, \cos\gamma) = \hat{v} = \mathbf{\left(\frac{2}{3},\, -\frac{1}{3},\, \frac{2}{3}\right)}$.
- **(b)** $\cos^2\alpha + \cos^2\beta + \cos^2\gamma = \frac{4}{9} + \frac{1}{9} + \frac{4}{9} = \mathbf{1}$.

### `D05-E05` *(Ângulo diretor faltante)*
- **(a)** $\cos^2 60^\circ + \cos^2 45^\circ + \cos^2\gamma = 1 \implies \left(\frac{1}{2}\right)^2 + \left(\frac{\sqrt{2}}{2}\right)^2 + \cos^2\gamma = 1$:
  $$\frac{1}{4} + \frac{2}{4} + \cos^2\gamma = 1 \implies \cos^2\gamma = \frac{1}{4} \implies \mathbf{\cos\gamma = -\frac{1}{2} \text{ ou } \cos\gamma = \frac{1}{2}}.$$
- **(b)** Como o enunciado pede o ângulo **agudo**, tomamos $\cos\gamma = \frac{1}{2} \implies \gamma = \mathbf{60^\circ}$.

### `D05-E06` *(Parâmetro para ângulo dado e raiz espúria)*
$\vec{u}\cdot\vec{v} = 2 - 1 + 2m = 1 + 2m$, $|\vec{u}| = \sqrt{6}$ e $|\vec{v}| = \sqrt{5 + m^2}$.  
Para $\theta = 60^\circ$, $\cos 60^\circ = \frac{1}{2} > 0$, o que **exige $1 + 2m > 0$**:
$$\frac{1 + 2m}{\sqrt{6}\sqrt{5 + m^2}} = \frac{1}{2} \implies 2(1 + 2m) = \sqrt{6(5 + m^2)}.$$
Elevando ao quadrado:
$$4(1 + 4m + 4m^2) = 30 + 6m^2 \implies 10m^2 + 16m - 26 = 0 \implies 5m^2 + 8m - 13 = 0.$$
Fatorando $(5m + 13)(m - 1) = 0$: obtemos $m = 1$ ou $m = -\frac{13}{5}$.
- Teste em $1 + 2m > 0$: para $m = -\frac{13}{5}$, $1 + 2\left(-\frac{13}{5}\right) = -\frac{21}{5} < 0$ (geraria $\cos\theta = -\frac{1}{2}$, isto é, $120^\circ$ — raiz espúria!).
- Para $m = 1$, $1 + 2(1) = 3 > 0$, conferindo $\cos\theta = \frac{3}{\sqrt{6}\sqrt{6}} = \frac{1}{2}$.  
Resposta: **$\mathbf{m = 1}$**.

---

## 2. Gabarito da Checagem Independente (`D05-C01` a `D05-C03`)

### `D05-C01`
Vetores saindo de $P$: $\overrightarrow{PQ} = Q - P = (2, 2, 0)$ e $\overrightarrow{PR} = R - P = (2, 0, 2)$.  
$\overrightarrow{PQ}\cdot\overrightarrow{PR} = 4$, $|\overrightarrow{PQ}| = 2\sqrt{2}$ e $|\overrightarrow{PR}| = 2\sqrt{2}$.
- **(a)** $\cos\hat{P} = \frac{4}{8} = \mathbf{\frac{1}{2}}$.
- **(b)** $\hat{P} = \mathbf{60^\circ}$.

### `D05-C02`
$$\vec{u}\cdot\vec{v} = k(k + 2) + 2k - 3k = k^2 + k = k(k + 1) = 0 \implies \mathbf{k = -1 \text{ ou } k = 0}.$$
*(Nunca divida por $k$ antes de fatorar, para não perder a solução $k = 0$.)*

### `D05-C03`
Pela identidade $\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$:
$$\left(\frac{2}{3}\right)^2 + \left(\frac{1}{3}\right)^2 + \cos^2\gamma = 1 \implies \frac{5}{9} + \cos^2\gamma = 1 \implies \cos^2\gamma = \frac{4}{9}.$$
Como $\gamma$ é **obtuso**, $\cos\gamma = -\frac{2}{3}$. Logo o versor é $\hat{w} = \left(\frac{2}{3}, \frac{1}{3}, -\frac{2}{3}\right)$ e:
$$\vec{w} = |\vec{w}|\,\hat{w} = 6\left(\frac{2}{3},\, \frac{1}{3},\, -\frac{2}{3}\right) = \mathbf{(4, 2, -4)}.$$
