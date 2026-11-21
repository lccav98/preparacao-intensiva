# Gabarito Comentado — Bloco `D01` (Segmento Orientado, Vetor, Módulo, Versor e Ângulos Geométricos)

> **Bloco de referência:** [D01_bloco.md](file:///C:/Users/d7opa/Documents/Matrizes%20e%20Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores/estagio_D/blocos/D01_bloco.md)  
> **Nota para Caça ao Erro:** Em `D01-E03`, o estudante mediu o ângulo entre $\overrightarrow{AB}$ e $\overrightarrow{BC}$ sem colocá-los com origem comum.

---

## 1. Gabarito dos Exercícios (`D01-E01` a `D01-E06`)

### `D01-E01` *(Ângulos por inversão e escala)*
Dado $\text{ang}(\vec{u}, \vec{v}) = 50^\circ$:
- **(a)** $\vec{u}$ mantém sentido e $-\vec{v}$ inverte o sentido $\Rightarrow 180^\circ - 50^\circ = \mathbf{130^\circ}$.
- **(b)** $-\vec{u}$ inverte o sentido e $\vec{v}$ mantém $\Rightarrow 180^\circ - 50^\circ = \mathbf{130^\circ}$.
- **(c)** Ambos $-\vec{u}$ e $-\vec{v}$ invertem de sentido $\Rightarrow \mathbf{50^\circ}$.
- **(d)** Escalares positivos $3 > 0$ e $5 > 0$ preservam os sentidos originais $\Rightarrow \mathbf{50^\circ}$.

### `D01-E02` *(Módulo de múltiplos e do versor)*
Dado $|\vec{v}| = 6$:
- **(a)** $|-4\vec{v}| = |-4|\cdot|\vec{v}| = 4 \cdot 6 = \mathbf{24}$.
- **(b)** $\left|\frac{1}{2}\vec{v}\right| = \left|\frac{1}{2}\right|\cdot|\vec{v}| = \frac{1}{2}\cdot 6 = \mathbf{3}$.
- **(c)** Todo versor é unitário: $|\hat{v}| = \left|\frac{\vec{v}}{|\vec{v}|}\right| = \frac{6}{6} = \mathbf{1}$.
- **(d)** $|5\hat{v}| = |5|\cdot|\hat{v}| = 5 \cdot 1 = \mathbf{5}$.

### `D01-E03` *(Caça ao Erro — Origem comum)*
- **Erro do estudante:** $\overrightarrow{AB}$ termina em $B$, enquanto $\overrightarrow{BC}$ começa em $B$. Para medir o ângulo entre dois vetores, é obrigatório transladar $\overrightarrow{AB}$ até partir de $B$ (isto é, observar o prolongamento de $AB$ além de $B$).
- **(a)** O ângulo entre $\overrightarrow{AB}$ e $\overrightarrow{BC}$ é o suplementar do ângulo interno em $B$: $180^\circ - 40^\circ = \mathbf{140^\circ}$.
- **(b)** Os vetores $\overrightarrow{BA}$ e $\overrightarrow{BC}$ partem ambos do vértice comum $B$, portanto o ângulo entre eles é o próprio ângulo interno: $\mathbf{40^\circ}$.

### `D01-E04` *(Regra do paralelogramo ortogonal)*
Com $\vec{u} \perp \vec{v}$, o paralelogramo construído na origem comum é um retângulo de lados $5$ e $12$:
- **(a)** $|\vec{u} + \vec{v}| = \sqrt{5^2 + 12^2} = \sqrt{25 + 144} = \sqrt{169} = \mathbf{13}$.
- **(b)** As duas diagonais de um retângulo têm o mesmo comprimento: $|\vec{u} - \vec{v}| = \sqrt{5^2 + 12^2} = \mathbf{13}$.

### `D01-E05` *(Simplificação vetorial e sentido)*
Expandindo e agrupando termos:
$$\vec{w} = 2\vec{a} - 2\vec{b} - 3\vec{a} + 4\vec{b} + \vec{a} = (2 - 3 + 1)\vec{a} + (-2 + 4)\vec{b} = 2\vec{b}.$$
- **(a)** O coeficiente escalar de $\vec{b}$ é $k = \mathbf{2}$.
- **(b)** $|\vec{w}| = |2\vec{b}| = 2\cdot|\vec{b}| = 2 \cdot 7 = \mathbf{14}$.
- **(c)** Como $\vec{w} = 2\vec{b}$ ($2 > 0$) tem o mesmo sentido de $\vec{b}$, ele possui sentido exatamente oposto ao de $-\vec{b}$ $\Rightarrow \mathbf{180^\circ}$.

### `D01-E06` *(Geometria do losango)*
Como $|\vec{a}| = |\vec{b}| = 8$, o paralelogramo de lados $\vec{a}$ e $\vec{b}$ é um **losango**:
- **(a)** Em todo losango, as diagonais são perpendiculares entre si $\Rightarrow \text{ang}(\vec{a}+\vec{b},\, \vec{a}-\vec{b}) = \mathbf{90^\circ}$.
- **(b)** O triângulo formado por $\vec{a}$, $\vec{b}$ e $\vec{a}-\vec{b}$ possui dois lados iguais a $8$ e ângulo compreendido de $60^\circ$; logo é um triângulo equilátero de lado $8$, donde $|\vec{a} - \vec{b}| = \mathbf{8}$.

---

## 2. Gabarito da Checagem Independente (`D01-C01` a `D01-C03`)

### `D01-C01`
Dado $\text{ang}(\vec{p}, \vec{q}) = 115^\circ$:
- **(a)** $\vec{p}$ e $-\vec{q}$: $180^\circ - 115^\circ = \mathbf{65^\circ}$.
- **(b)** $-2\vec{p}$ (inverte) e $3\vec{q}$ (mantém): $180^\circ - 115^\circ = \mathbf{65^\circ}$.
- **(c)** $-4\vec{p}$ (inverte) e $-\vec{q}$ (inverte): $\mathbf{115^\circ}$.

### `D01-C02`
Dado $|\vec{u}| = 9$:
- **(a)** $\left|-\frac{2}{3}\vec{u}\right| = \frac{2}{3} \cdot 9 = \mathbf{6}$.
- **(b)** $|\hat{u}| = \mathbf{1}$.
- **(c)** $|k\vec{u}| = 3 \Rightarrow |k|\cdot 9 = 3 \Rightarrow |k| = \frac{1}{3} \Rightarrow \mathbf{k = -\frac{1}{3} \text{ ou } k = \frac{1}{3}}$.

### `D01-C03`
No triângulo equilátero $ABC$ de lado $6$ (ângulos internos de $60^\circ$):
- **(a)** Pela regra do triângulo, $\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}$, portanto $|\overrightarrow{AB} + \overrightarrow{BC}| = |\overrightarrow{AC}| = \mathbf{6}$.
- **(b)** Transladando $\overrightarrow{AB}$ para partir de $B$, o ângulo entre $\overrightarrow{AB}$ e $\overrightarrow{BC}$ é o ângulo externo em $B$: $180^\circ - 60^\circ = \mathbf{120^\circ}$.
- **(c)** Pela diferença geométrica com origem comum em $A$, $\overrightarrow{AB} - \overrightarrow{AC} = \overrightarrow{CB}$, logo $|\overrightarrow{AB} - \overrightarrow{AC}| = |\overrightarrow{CB}| = \mathbf{6}$.
