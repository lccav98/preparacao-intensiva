# Bloco `E01` — Equações da Reta no `\mathbb{R}^3` e Pertinência

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio E — A Reta, O Plano e Distâncias no `\mathbb{R}^3` / **`E01`** |
| **Micro-habilidade foco** | Escrever as equações vetorial, paramétricas, simétricas e reduzidas em `x` de uma reta no espaço, a partir de dois pontos ou de um ponto e vetor diretor, e verificar pertinência de ponto. |
| **Pré-requisitos** | `D02`, `D03` |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`E01-E01`–`E01-E05`, 22 min):** `14 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`E01-C01`–`E01-C03`, 14 min):** `10 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** equação vetorial `r: P + t\vec{v}`, paramétricas `(x(t), y(t), z(t))`, simétricas `\frac{x-x_0}{a} = \frac{y-y_0}{b} = \frac{z-z_0}{c}`, reduzidas em `x` (`y = mx + n`, `z = px + q`), vetor diretor de coordenadas constantes (`x = k, z = h`), pertinência. **Proibido:** produto vetorial para reta (`E02`), ângulo entre retas (`E02`), coplanaridade (`E03`), planos (`E04`). |

---

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`E01-E01`–`E01-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`E01-C01`–`E01-C03`):** `___ / 3` | **Tempo:** `___ min (`[ ] Aprovado (100%)  [ ] Recuperação)`

---

## 1. Instruções Curtas

1. **Equação vetorial:** dado ponto `P(x_0, y_0, z_0)` e vetor diretor `\vec{v} = (a, b, c)`, a reta é `\vec{r}(t) = \vec{p} + t\vec{v}`, `t \in \mathbb{R}`.
2. **Equações paramétricas:** `x = x_0 + at`, `y = y_0 + bt`, `z = z_0 + ct`.
3. **Equações simétricas:** `\frac{x-x_0}{a} = \frac{y-y_0}{b} = \frac{z-z_0}{c}` (quando `a, b, c` todos não nulos).
4. **Reduzidas em `x`:** isolar `t` na equação de `x` e substituir em `y` e `z`, obtendo `y = m_x x + n` e `z = p_x x + q`. Sempre em função de `x`.
5. **Vetor diretor de coordenadas constantes:** se a reta tem `x = k` e `z = h`, o vetor diretor é `(0, 1, 0)` (paralela ao eixo `y`); as reduzidas são `x = k`, `z = h`.
6. **Pertinência:** um ponto `Q` pertence à reta se existir o mesmo `t` nas três equações paramétricas.
7. **Dois pontos `A` e `B`:** vetor diretor `\vec{v} = \overrightarrow{AB} = B - A` (regra "extremidade menos origem").
8. **Aritmética exata:** frações irredutíveis e radicais exatos; sem arredondamento decimal.

---

## 2. Exemplos Guiados

### Exemplo 1 — Reta por dois pontos (reduzidas em `x`)
Dados `A(1, 2, -1)` e `B(3, 0, 2)`:
- `\vec{v} = \overrightarrow{AB} = (3-1, 0-2, 2-(-1)) = (2, -2, 3)`
- Vetorial: `r: (1, 2, -1) + t(2, -2, 3)`
- Paramétricas: `x = 1 + 2t`, `y = 2 - 2t`, `z = -1 + 3t`
- Simétricas: `\frac{x-1}{2} = \frac{y-2}{-2} = \frac{z+1}{3}`
- Reduzidas em `x`: `t = \frac{x-1}{2}` → `y = 2 - 2(\frac{x-1}{2}) = 3 - x`; `z = -1 + 3(\frac{x-1}{2}) = \frac{3}{2}x - \frac{5}{2}`

### Exemplo 2 — Pertinência de ponto
Reta `r: x = 2 + t, y = 1 - 2t, z = 3t`. Verificar se `P(5, -7, 9)` pertence:
- `x: 5 = 2 + t → t = 3`
- `y: -7 = 1 - 2t → t = 4`
- `z: 9 = 3t → t = 3`
Como `t` não é o mesmo em todas (3, 4, 3), **`P` não pertence a `r`**.

---

## 3. Exercícios (`E01-E01` a `E01-E05`)

### `E01-E01` *(Vetorial e paramétricas por dois pontos)*
Dados `A(-1, 3, 2)` e `B(2, -1, 5)`:
**(a)** Escreva a equação vetorial `r: P + t\vec{v}`.  
**(b)** Escreva as equações paramétricas.

**Formato de resposta:** `(a) vetor_ponto + t(vetor_diretor) (b) x=..., y=..., z=...`.

---

### `E01-E02` *(Simétricas e reduzidas em `x`)*
Dados `P(1, -2, 4)` e vetor diretor `\vec{v} = (2, 3, -1)`:
**(a)** Escreva as equações simétricas.  
**(b)** Escreva as equações reduzidas em `x`.

**Formato de resposta:** `(a) (x-1)/2 = (y+2)/3 = (z-4)/(-1) (b) y=..., z=...`.

---

### `E01-E03` *(Vetor diretor de coordenadas constantes)*
Uma reta passa por `C(3, 1, -2)` e é paralela ao eixo `y`:
**(a)** Qual é o vetor diretor?  
**(b)** Escreva as equações reduzidas (x e z constantes).

**Formato de resposta:** `(a) (a, b, c) (b) x = ..., z = ...`.

---

### `E01-E04` *(Pertinência de ponto)*
Considere a reta `r: x = 3 - 2t, y = 1 + t, z = -2 + 4t`.  
Verifique se o ponto `Q(1, 3, 6)` pertence a `r`. Se pertencer, informe o valor de `t`.

**Formato de resposta:** `(pertence_ou_nao) t=valor` (ex.: `sim t=1` ou `nao`).

---

### `E01-E05` *(Conversão simétricas → paramétricas)*
Dadas as equações simétricas `\frac{x-2}{-1} = \frac{y+3}{2} = \frac{z-5}{3}`:
**(a)** Escreva as equações paramétricas.  
**(b)** Um ponto da reta (para `t = 0`).

**Formato de resposta:** `(a) x=..., y=..., z=... (b) (x, y, z)`.

---

## 4. Checagem Independente (`E01-C01` a `E01-C03`)

### `E01-C01` *(Reta completa por dois pontos)*
Dados `M(0, 4, -3)` e `N(4, 0, 1)`:
**(a)** Equação vetorial.  
**(b)** Equações reduzidas em `x`.

**Formato de resposta:** `(a) P + t(a, b, c) (b) y=..., z=...`.

---

### `E01-C02` *(Pertinência com frações)*
Reta `r: x = 1 + 3t, y = -2 - t, z = 4 + 2t`. Verifique se `R(7, -5, 10)` pertence a `r`.

**Formato de resposta:** `sim t=valor` ou `nao`.

---

### `E01-C03` *(Reduzidas a partir de simétricas)*
Dados `\frac{x-5}{3} = \frac{y-1}{-2} = \frac{z+2}{4}`:
Escreva as equações reduzidas em `x`.

**Formato de resposta:** `y=..., z=...`.

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `E02`:** somente após autocorreção de `E01-E01`–`E01-E05` e **100% (3/3)** na Checagem Independente `E01-C01`–`E01-C03` sem consulta.
- **Recuperação direcionada (1ª falha):**
  - Se errou vetor diretor → refaça `D02` (`\overrightarrow{AB} = B - A`).
  - Se errou reduzidas → refaça a substituição de `t` mantendo frações exatas.
- **Após 2 tentativas malsucedidas:** interrompa e revise `D02`/`D03` com o orientador antes de nova variante.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Parte_4.pdf` p. 3–9 (reta: vetorial, paramétricas, simétricas, reduzidas em `x`).
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 124–135 (Cap. 4: Reta).
- Gabarito e casos: [E01_gabarito.md](../gabaritos/E01_gabarito.md) e [casos_E01.json](../testes/casos_E01.json).
