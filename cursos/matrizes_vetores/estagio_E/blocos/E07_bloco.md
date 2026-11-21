# Bloco `E07` — Distâncias Ponto-Ponto e Ponto-Reta

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio E — A Reta, O Plano e Distâncias no `\mathbb{R}^3` / **`E07`** |
| **Micro-habilidade foco** | Calcular a distância entre dois pontos e a distância de um ponto a uma reta (`d = \frac{|\vec{v}\times\overrightarrow{P_1P_0}|}{|\vec{v}|}`), incluindo distâncias aos eixos coordenados. |
| **Pré-requisitos** | `E01`, `D08` |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`E07-E01`–`E07-E05`, 20 min):** `12 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`E07-C01`–`E07-C03`, 14 min):** `10 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** `d(P_1, P_2)`, `d(P_0, r) = \frac{|\vec{v}\times\overrightarrow{P_1P_0}|}{|\vec{v}|}`, distâncias aos eixos coordenados `x, y, z`. **Proibido:** distância ponto-plano (`E09`), distância reta-reta (`E08`). |

---

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`E07-E01`–`E07-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`E07-C01`–`E07-C03`):** `___ / 3` | **Tempo:** `___ min (`[ ] Aprovado (100%)  [ ] Recuperação)`

---

## 1. Instruções Curtas

1. **Distância ponto-ponto:** `d(P_1, P_2) = |\overrightarrow{P_1P_2}| = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2}`.
2. **Distância ponto-reta:** dado ponto `P_0` e reta `r: P_1 + t\vec{v}`, a distância é `d(P_0, r) = \frac{|\vec{v}\times\overrightarrow{P_1P_0}|}{|\vec{v}|}`. Intuição: comprimento da componente de `\overrightarrow{P_1P_0}` ortogonal a `\vec{v}`.
3. **Distância a um eixo coordenado:**
   - Ao eixo `x`: `d = \sqrt{y^2 + z^2}` (distância de `(x, y, z)` ao eixo `x`).
   - Ao eixo `y`: `d = \sqrt{x^2 + z^2}`.
   - Ao eixo `z`: `d = \sqrt{x^2 + y^2}`.
4. **Produto vetorial:** necessário para a distância ponto-reta. Use a fórmula determinante simbólica.
5. **Aritmética exata:** radicais exatos, sem arredondamento decimal.

---

## 2. Exemplos Guiados

### Exemplo 1 — Distância ponto-ponto
`P_1(1, 2, 3)` e `P_2(4, 6, 8)`:
- `\overrightarrow{P_1P_2} = (3, 4, 5)`
- `d = \sqrt{9 + 16 + 25} = \sqrt{50} = 5\sqrt{2}`.

### Exemplo 2 — Distância ponto-reta
`P_0(1, 2, 3)` e reta `r: (0, 0, 0) + t(1, 1, 1)`:
- `P_1 = (0, 0, 0)`, `\vec{v} = (1, 1, 1)`, `\overrightarrow{P_1P_0} = (1, 2, 3)`
- `\vec{v}\times\overrightarrow{P_1P_0} = (1\cdot3 - 1\cdot2,\; 1\cdot1 - 1\cdot3,\; 1\cdot2 - 1\cdot1) = (1, -2, 1)`
- `|(1, -2, 1)| = \sqrt{1+4+1} = \sqrt{6}`, `|\vec{v}| = \sqrt{3}`
- `d = \frac{\sqrt{6}}{\sqrt{3}} = \sqrt{2}`.

---

## 3. Exercícios (`E07-E01` a `E07-E05`)

### `E07-E01` *(Distância ponto-ponto)*
`P_1(1, 1, 1)` e `P_2(4, 5, 9)`:
Calcule a distância exata.

**Formato de resposta:** `valor`.

---

### `E07-E02` *(Distância ponto-reta)*
Ponto `P_0(1, 2, 3)` e reta `r: (0, 0, 0) + t(2, 1, 2)`:
Calcule `d(P_0, r)`.

**Formato de resposta:** `valor`.

---

### `E07-E03` *(Distância a um eixo coordenado)*
Ponto `P(3, 4, 12)`:
Calcule a distância de `P` ao eixo `z`.

**Formato de resposta:** `valor`.

---

### `E07-E04` *(Distância ponto-reta com frações)*
Ponto `P_0(1, 1, 1)` e reta `r: (1, 0, 0) + t(0, 1, 1)`:
Calcule `d(P_0, r)`.

**Formato de resposta:** `valor`.

---

### `E07-E05` *(Integração: ponto-reta + ponto-ponto)*
`P_1(0, 0, 0)`, `P_2(3, 4, 0)` e reta `r: (1, 1, 0) + t(1, -1, 0)`:
**(a)** Distância `d(P_1, P_2)`.  
**(b)** Distância `d(P_1, r)`.

**Formato de resposta:** `(a) valor (b) valor`.

---

## 4. Checagem Independente (`E07-C01` a `E07-C03`)

### `E07-C01` *(Distância ponto-ponto com radical)*
`P_1(-1, 2, 3)` e `P_2(2, -1, -1)`:
Distância exata.

**Formato de resposta:** `valor`.

---

### `E07-C02` *(Distância ponto-reta)*
Ponto `P_0(2, 1, -1)` e reta `r: (0, 1, 0) + t(1, 0, 1)`:
Calcule `d(P_0, r)`.

**Formato de resposta:** `valor`.

---

### `E07-C03` *(Distância ao eixo y)*
Ponto `P(5, -3, 12)`:
Distância ao eixo `y`.

**Formato de resposta:** `valor`.

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `E08`:** somente após autocorreção de `E07-E01`–`E07-E05` e **100% (3/3)** na Checagem Independente `E07-C01`–`E07-C03` sem consulta.
- **Recuperação direcionada (1ª falha):**
  - Se errou o produto vetorial → refaça `D07`.
  - Se errou a distância ponto-ponto → refaça `D04` (módulo analítico).
- **Após 2 tentativas malsucedidas:** interrompa e revise `D07`/`D04` com o orientador.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Parte_4.pdf` p. 46–47 (distâncias ponto-ponto, ponto-reta, aos eixos).
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 151–164 (Cap. 6: Distâncias).
- Gabarito e casos: [E07_gabarito.md](../gabaritos/E07_gabarito.md) e [casos_E07.json](../testes/casos_E07.json).
