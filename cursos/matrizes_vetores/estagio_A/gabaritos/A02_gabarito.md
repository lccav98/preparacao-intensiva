# Gabarito Comentado — Bloco `A02` (Igualdade de Matrizes e Equações por Elementos)

> **Bloco de referência:** [A02_bloco.md](../blocos/A02_bloco.md)

---

## 1. Exercícios

### `A02-E01` *(Igualdade linear direta)*
- **Passo a passo:**
  - Igualando os elementos correspondentes:
    - Posição $(1,1)$: $2x - 1 = 7 \implies 2x = 8 \implies x = 4$.
    - Posição $(2,2)$: $y + 4 = -2 \implies y = -6$.
  - Elementos fixos $(1,2)$ e $(2,1)$: $5 = 5$ e $3 = 3$ (consistente).
- **Resposta Final:** `(4, -6)`
- **Alerta pedagógico:** Sempre confira se os elementos fixos das demais posições coincidem; caso contrário, não existiria igualdade.

---

### `A02-E02` *(Equações quadráticas puras — atenção ao sinal `\pm`)*
- **Passo a passo:**
  - **(a)** Posição $(1,1)$: $m^2 - 15 = 10 \implies m^2 = 25 \implies m = \pm 5$ (isto é, $m = -5$ ou $m = 5$).
  - **(b)** Posição $(1,2)$: $n^2 + 3 = 19 \implies n^2 = 16 \implies n = \pm 4$ (isto é, $n = -4$ ou $n = 4$).
- **Resposta Final:** `(a) m = +-5 (b) n = +-4`
- **Alerta pedagógico:** Erro mais comum neste tópico: escrever apenas o valor positivo ($m = 5, n = 4$). Como $(-5)^2 = 25$ e $(-4)^2 = 16$, ambas as raízes satisfazem a igualdade.

---

### `A02-E03` *(Equação do 2º grau completa e raiz dupla vs. raízes distintas)*
- **Passo a passo:**
  - **(a)** Posição $(1,2)$:
    $$k^2 = 12k - 36 \implies k^2 - 12k + 36 = 0 \implies (k - 6)^2 = 0 \implies k = 6.$$
  - **(b)** Posição $(2,2)$:
    $$p^2 - 6p = -5 \implies p^2 - 6p + 5 = 0 \implies (p - 1)(p - 5) = 0 \implies p = 1 \text{ ou } p = 5.$$
- **Resposta Final:** `(a) 6 (b) 1, 5`
- **Alerta pedagógico:** Nunca divida uma equação por $k$ ou $p$; passe todos os termos para o mesmo lado e fatore ou aplique Bhaskara.

---

### `A02-E04` *(Posições acopladas em sistema `2x2`)*
- **Passo a passo:**
  - Das posições $(1,1)$ e $(2,1)$:
    $$\begin{cases} x + y = 5 \\ 2x - y = 7 \end{cases}$$
  - Somando as duas equações: $3x = 12 \implies x = 4$.
  - Substituindo na primeira: $4 + y = 5 \implies y = 1$.
  - Conferência: $2(4) - 1 = 7$.
- **Resposta Final:** `(4, 1)`
- **Alerta pedagógico:** Em igualdades acopladas, não tente adivinhar valores isolados; monte o sistema $2\times 2$ explicitamente.

---

### `A02-E05` *(Integração com lei de formação e frações exatas)*
- **Passo a passo:**
  - Construindo $M_{(2,2)}$ com $m_{ij} = \frac{2i - j}{3}$:
    - $m_{11} = \frac{2(1)-1}{3} = \frac{1}{3}$
    - $m_{12} = \frac{2(1)-2}{3} = 0$
    - $m_{21} = \frac{2(2)-1}{3} = \frac{3}{3} = 1$
    - $m_{22} = \frac{2(2)-2}{3} = \frac{2}{3}$
  - Igualando $M = N$:
    - Posição $(1,1)$: $a = \frac{1}{3}$.
    - Posição $(1,2)$: $0 = 0$ (consistente).
    - Posição $(2,1)$: $b + \frac{1}{3} = 1 \implies b = 1 - \frac{1}{3} = \frac{2}{3}$.
    - Posição $(2,2)$: $3c = \frac{2}{3} \implies c = \frac{2}{9}$.
- **Resposta Final:** `(1/3, 2/3, 2/9)`
- **Alerta pedagógico:** Mantenha `1/3`, `2/3` e `2/9` em frações exatas. Dividir `2/3` por `3` multiplica o denominador: `2/(3*3) = 2/9`.

---

## 2. Checagem Independente

### `A02-C01` *(Quadráticas puras inéditas)*
- **Passo a passo:**
  - **(a)** Posição $(1,1)$: $p^2 - 20 = 29 \implies p^2 = 49 \implies p = \pm 7$.
  - **(b)** Posição $(2,2)$: $q^2 + 7 = 16 \implies q^2 = 9 \implies q = \pm 3$.
- **Resposta Final:** `(a) p = +-7 (b) q = +-3`
- **Alerta pedagógico:** Verifique o sinal da raiz negativa antes de entregar a folha.

---

### `A02-C02` *(Acoplamento e raiz dupla)*
- **Passo a passo:**
  - **(a)** Sistema pelas posições $(1,1)$ e $(2,1)$:
    $$\begin{cases} 2a - b = 1 \implies b = 2a - 1 \\ a + 3b = 11 \end{cases}$$
    Substituindo: $a + 3(2a - 1) = 11 \implies 7a - 3 = 11 \implies 7a = 14 \implies a = 2$.
    Logo $b = 2(2) - 1 = 3$. Par $(a, b) = (2, 3)$.
  - **(b)** Posição $(2,2)$:
    $$r^2 = 8r - 16 \implies r^2 - 8r + 16 = 0 \implies (r - 4)^2 = 0 \implies r = 4.$$
- **Resposta Final:** `(a) (2, 3) (b) 4`
- **Alerta pedagógico:** Confira $(a,b)=(2,3)$ nas duas posições: $2(2)-3=1$ e $2+3(3)=11$.

---

### `A02-C03` *(Igualdade com matriz identidade `I_2` e frações)*
- **Passo a passo:**
  - Lembrando que $I_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$:
  - **(a)** Posição $(1,1)$: $3x - \frac{1}{2} = 1 \implies 3x = \frac{3}{2} \implies x = \frac{1}{2}$.
  - **(b)** Posição $(1,2)$: $y^2 - \frac{9}{4} = 0 \implies y^2 = \frac{9}{4} \implies y = \pm\frac{3}{2}$.
  - **(c)** Posição $(2,2)$: $\frac{z}{3} + 1 = 1 \implies \frac{z}{3} = 0 \implies z = 0$.
- **Resposta Final:** `(a) 1/2 (b) y = +-3/2 (c) 0`
- **Alerta pedagógico:** Cuidado com $I_2$: os elementos fora da diagonal valem $0$, enquanto os da diagonal principal valem $1$ (não confunda $I_2$ com matriz nula).
