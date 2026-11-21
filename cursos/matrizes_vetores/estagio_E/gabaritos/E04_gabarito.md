# Gabarito Comentado — Bloco `E04` (Equação Geral e Paramétricas do Plano)

> **Bloco de referência:** [E04_bloco.md](../blocos/E04_bloco.md)

---

## 1. Exercícios

### `E04-E01` *(Plano por ponto e normal)*
- **Passo a passo:**
  - `1(x-2) + 2(y-(-1)) + (-2)(z-3) = 0`.
  - `x - 2 + 2y + 2 - 2z + 6 = 0`.
  - `x + 2y - 2z + 6 = 0`.
- **Resposta Final:** `x + 2y - 2z + 6 = 0`
- **Alerta pedagógico:** Confira substituindo o ponto `P(2, -1, 3)`: `2 + 2(-1) - 2(3) + 6 = 2 - 2 - 6 + 6 = 0`. Confere.

---

### `E04-E02` *(Plano por 3 pontos)*
- **Passo a passo:**
  - `\overrightarrow{AB} = (3, 3, 3)`, `\overrightarrow{AC} = (6, 6, 7)`.
  - `\vec{n} = (3, 3, 3)\times(6, 6, 7) = (3\cdot7 - 3\cdot6,\; 3\cdot6 - 3\cdot7,\; 3\cdot6 - 3\cdot6) = (21-18,\; 18-21,\; 18-18) = (3, -3, 0)`.
  - Normal `(3, -3, 0)` ou simplificada `(1, -1, 0)`.
  - Plano: `1(x-1) - 1(y-2) + 0(z-3) = 0` → `x - 1 - y + 2 = 0` → `x - y + 1 = 0`.
  - Verifique colinearidade: `\overrightarrow{AB} = (3, 3, 3)` e `\overrightarrow{AC} = (6, 6, 7)` não são proporcionais → não colineares.
- **Resposta Final:** `x - y + 1 = 0`
- **Alerta pedagógico:** Se os 3 pontos fossem colineares, o produto vetorial seria `(0, 0, 0)` e não definiria um plano único.

---

### `E04-E03` *(Mediador de um segmento)*
- **Passo a passo:**
  - Ponto médio `M = ((1+5)/2, (2+6)/2, (3+7)/2) = (3, 4, 5)`.
  - `\overrightarrow{AB} = (4, 4, 4)` ou simplificado `(1, 1, 1)`.
  - Plano: `1(x-3) + 1(y-4) + 1(z-5) = 0` → `x + y + z - 12 = 0`.
- **Resposta Final:** `x + y + z - 12 = 0`
- **Alerta pedagógico:** O mediador é ortogonal ao segmento e passa pelo ponto médio. Todo ponto do mediador está à mesma distância de `A` e `B`.

---

### `E04-E04` *(Plano contendo duas retas paralelas)*
- **Passo a passo:**
  - Diretor comum `\vec{v} = (1, 1, 0)`.
  - `\overrightarrow{A_1A_2} = (0-1, 0-0, 1-0) = (-1, 0, 1)`.
  - Normal: `\vec{v}\times\overrightarrow{A_1A_2} = (1, 1, 0)\times(-1, 0, 1) = (1\cdot1 - 0\cdot0,\; 0(-1) - 1\cdot1,\; 1\cdot0 - 1(-1)) = (1, -1, 1)`.
  - Plano: `1(x-1) - 1(y-0) + 1(z-0) = 0` → `x - y + z - 1 = 0`.
- **Resposta Final:** `x - y + z - 1 = 0`
- **Alerta pedagógico:** O plano contendo duas retas paralelas tem normal ortogonal tanto ao diretor comum quanto ao vetor ligando um ponto de cada reta.

---

### `E10-E05` *(Forma paramétrica `(h, t)`)*
- **Passo a passo:**
  - Plano `2x - y + 3z - 6 = 0`. Normal `\vec{n} = (2, -1, 3)`.
  - Precisamos de dois diretores no plano. Escolha `\vec{u} = (1, 2, 0)` (confere: `2(1) - 2 + 3(0) = 0` ✓) e `\vec{v} = (0, 3, 1)` (confere: `2(0) - 3 + 3(1) = 0` ✓).
  - Ponto no plano: ponha `y = 0, z = 0` → `2x - 6 = 0 → x = 3`. Ponto `P(3, 0, 0)`.
  - Paramétrica: `x = 3 + h + 0t = 3 + h`, `y = 0 + 2h + 3t`, `z = 0 + 0h + t = t`.
- **Resposta Final:** `x = 3 + h, y = 2h + 3t, z = t`
- **Alerta pedagógico:** Qualquer par de diretores não paralelos no plano serve. A resposta pode variar; verifique se os diretores são ortogonais à normal.

---

## 2. Checagem Independente

### `E04-C01` *(Plano por ponto e normal com frações)*
- **Passo a passo:**
  - `2(x-1/2) + 1(y-1) + 1(z-(-1)) = 0`.
  - `2x - 1 + y - 1 + z + 1 = 0`.
  - `2x + y + z - 1 = 0`.
- **Resposta Final:** `2x + y + z - 1 = 0`
- **Alerta pedagógico:** Mantenha as frações até o final; o resultado pode ter coeficientes inteiros.

---

### `E04-C02` *(Pertinência de ponto no plano)*
- **Passo a passo:**
  - Substitua `Q(2, 1, 2)`: `3(2) - 2(1) + 2 - 5 = 6 - 2 + 2 - 5 = 1 \neq 0`.
  - Não pertence.
- **Resposta Final:** `nao`
- **Alerta pedagógico:** O resultado deve ser `0` para pertencer; `1` não é zero.

---

### `E04-C03` *(Plano por 3 pontos não colineares)*
- **Passo a passo:**
  - `\overrightarrow{AB} = (1, 1, 0)`, `\overrightarrow{AC} = (0, 1, 1)`.
  - `\vec{n} = (1, 1, 0)\times(0, 1, 1) = (1\cdot1 - 0\cdot1,\; 0\cdot0 - 1\cdot1,\; 1\cdot1 - 1\cdot0) = (1, -1, 1)`.
  - Plano (usando `A(0, 0, 0)`): `1(x-0) - 1(y-0) + 1(z-0) = 0` → `x - y + z = 0`.
- **Resposta Final:** `x - y + z = 0`
- **Alerta pedagógico:** Como `A` é a origem, a equação fica sem termo independente (`d = 0`).
