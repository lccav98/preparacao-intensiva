# Bloco `E03` — Coplanaridade de Retas, Posições Relativas e Interseção

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio E — A Reta, O Plano e Distâncias no `\mathbb{R}^3` / **`E03`** |
| **Micro-habilidade foco** | Usar o produto misto para testar coplanaridade de duas retas, classificar posições relativas (concorrentes, paralelas, reversas) e encontrar o ponto de interseção quando existente. |
| **Pré-requisitos** | `E02`, `D09`, `C05` |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`E03-E01`–`E03-E05`, 24 min):** `16 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`E03-C01`–`E03-C03`, 16 min):** `12 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** produto misto `\vec{v}_1\cdot(\vec{v}_2\times\overrightarrow{A_1A_2})`, coplanaridade, concorrentes vs. paralelas vs. reversas, sistema com parâmetros `t_1, t_2`. **Proibido:** planos (`E04`), distâncias (`E07`–`E09`). |

---

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`E03-E01`–`E03-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`E03-C01`–`E03-C03`):** `___ / 3` | **Tempo:** `___ min (`[ ] Aprovado (100%)  [ ] Recuperação)`

---

## 1. Instruções Curtas

1. **Coplanaridade de duas retas:** dadas `r_1: A_1 + t_1\vec{v}_1` e `r_2: A_2 + t_2\vec{v}_2`, calculam-se `\vec{v}_1\times\vec{v}_2` e o produto misto `\vec{v}_1\cdot(\vec{v}_2\times\overrightarrow{A_1A_2})` (ou `det` com as três linhas). Se for `0`, são coplanares.
2. **Posições relativas:**
   - **Paralelas:** `\vec{v}_1 \parallel \vec{v}_2` (e não coincidentes, a menos que compartilhem ponto).
   - **Concorrentes:** coplanares e não paralelas → se intersectam em um ponto.
   - **Reversas:** não coplanares (não se intersectam, não são paralelas).
3. **Interseção:** resolva o sistema `A_1 + t_1\vec{v}_1 = A_2 + t_2\vec{v}_2` (3 equações, 2 incógnitas `t_1, t_2`). Se compatível, há ponto de interseção.
4. **Produto misto:** `(\vec{u},\vec{v},\vec{w}) = \vec{u}\cdot(\vec{v}\times\vec{w}) = det[\vec{u}\;\vec{v}\;\vec{w}]`.
5. **Aritmética exata:** frações irredutíveis.

---

## 2. Exemplos Guiados

### Exemplo 1 — Coplanaridade
`r_1: A_1(1, 0, 0) + t_1(1, 1, 0)` e `r_2: A_2(0, 1, 0) + t_2(0, 1, 1)`:
- `\overrightarrow{A_1A_2} = (-1, 1, 0)`
- `\vec{v}_1\times\vec{v}_2 = (1\cdot1 - 0\cdot1,\; 0\cdot0 - 1\cdot1,\; 1\cdot1 - 1\cdot0) = (1, -1, 1)`
- Produto misto: `(1, 1, 0)\cdot(1, -1, 1) = 1 - 1 + 0 = 0` → **coplanares**.

### Exemplo 2 — Interseção
`r_1: x = 1 + t_1, y = 2 + t_1` e `r_2: x = 3 - t_2, y = 1 + 2t_2` (no plano `z=0`):
- `1 + t_1 = 3 - t_2` e `2 + t_1 = 1 + 2t_2`
- Do primeiro: `t_1 + t_2 = 2`. Do segundo: `t_1 - 2t_2 = -1`.
- Subtraindo: `3t_2 = 3 → t_2 = 1`, `t_1 = 1`.
- Ponto: `(2, 3)`.

---

## 3. Exercícios (`E03-E01` a `E03-E05`)

### `E03-E01` *(Coplanaridade via produto misto)*
Dados `r_1: A_1(1, 2, 3) + t_1(1, 0, -1)` e `r_2: A_2(2, 1, 0) + t_2(2, 1, 1)`:
Calcule o produto misto e diga se são coplanares.

**Formato de resposta:** `produto_misto = valor, coplanares = sim/nao`.

---

### `E03-E02` *(Posições relativas)*
Dados `\vec{v}_1 = (1, 2, 3)` e `\vec{v}_2 = (2, 4, 6)`:
As retas com esses diretores são paralelas?

**Formato de resposta:** `sim` ou `nao`.

---

### `E03-E03` *(Interseção de duas retas)*
`r_1: x = 2 + t, y = 1 - t, z = 3 + 2t` e `r_2: x = 4 - s, y = 3 + s, z = 1 - s`:
Encontre o ponto de interseção, se existir.

**Formato de resposta:** `(x, y, z)` ou `nao_intersectam`.

---

### `E03-E04` *(Reversa vs. concorrente)*
Dados `r_1` passando por `(0, 0, 0)` com diretor `(1, 0, 0)` e `r_2` passando por `(0, 1, 0)` com diretor `(0, 1, 0)`:
Classifique: paralelas, concorrentes ou reversas.

**Formato de resposta:** `paralelas` / `concorrentes` / `reversas`.

---

### `E03-E05` *(Sistema com parâmetros)*
`r_1: x = 1 + 2t_1, y = 3 - t_1` e `r_2: x = 5 - t_2, y = 1 + 2t_2` (plano `z=0`):
Resolva o sistema e informe se intersectam.

**Formato de resposta:** `(x, y)` ou `nao_intersectam`.

---

## 4. Checagem Independente (`E03-C01` a `E03-C03`)

### `E03-C01` *(Coplanaridade e classificação)*
Dados `r_1: (1, 1, 1) + t_1(1, 1, 1)` e `r_2: (2, 2, 2) + t_2(2, 2, 2)`:
Classifique as retas.

**Formato de resposta:** `paralelas` / `concorrentes` / `reversas`.

---

### `E03-C02` *(Interseção com frações)*
`r_1: x = 1 + t_1, y = 2 + 2t_1` e `r_2: x = 3 - t_2, y = 4 - t_2`:
Encontre o ponto de interseção.

**Formato de resposta:** `(x, y)` ou `nao_intersectam`.

---

### `E03-C03` *(Produto misto não nulo → reversas)*
Dados `r_1: A_1(0, 0, 0) + t_1(1, 0, 0)` e `r_2: A_2(0, 0, 1) + t_2(0, 1, 0)`:
Calcule o produto misto e classifique.

**Formato de resposta:** `valor_misto, classificacao`.

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `E04`:** somente após autocorreção de `E03-E01`–`E03-E05` e **100% (3/3)** na Checagem Independente `E03-C01`–`E03-C03` sem consulta.
- **Recuperação direcionada (1ª falha):**
  - Se errou coplanaridade → refaça `D09` (produto misto).
  - Se errou interseção → refaça `C05` (sistemas `m x n` com parâmetros).
- **Após 2 tentativas malsucedidas:** interrompa e revise `D09`/`C05` com o orientador.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Parte_4.pdf` p. 12–13, 18–22 (coplanaridade, posições relativas, interseção).
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 124–135 (Cap. 4: Reta).
- Gabarito e casos: [E03_gabarito.md](../gabaritos/E03_gabarito.md) e [casos_E03.json](../testes/casos_E03.json).
