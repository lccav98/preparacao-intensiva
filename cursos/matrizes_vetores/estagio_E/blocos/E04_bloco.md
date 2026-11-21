# Bloco `E04` — Equação Geral e Paramétricas do Plano

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio E — A Reta, O Plano e Distâncias no `\mathbb{R}^3` / **`E04`** |
| **Micro-habilidade foco** | Escrever a equação geral `ax + by + cz + d = 0` de um plano a partir de um ponto e vetor normal, de 3 pontos, ou como mediador de um segmento; escrever a forma paramétrica `(h, t)`; verificar pertinência de ponto. |
| **Pré-requisitos** | `D07`, `D09`, `E01` |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`E04-E01`–`E04-E05`, 24 min):** `16 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`E04-C01`–`E04-C03`, 16 min):** `12 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** `ax+by+cz+d=0` via `\vec{n}\cdot\overrightarrow{AP}=0`, plano por 3 pontos, mediador, via produto misto, contendo 2 retas (concorrentes e paralelas), forma paramétrica `(h,t)`, pertinência. **Proibido:** ângulo plano-plano/reta-plano (`E05`), interseções (`E06`), distâncias (`E07`–`E09`). |

---

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`E04-E01`–`E04-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`E04-C01`–`E04-C03`):** `___ / 3` | **Tempo:** `___ min (`[ ] Aprovado (100%)  [ ] Recuperação)`

---

## 1. Instruções Curtas

1. **Equação geral do plano:** `ax + by + cz + d = 0` com normal `\vec{n} = (a, b, c)`. Dado ponto `P(x_0, y_0, z_0)` e normal `\vec{n}`: `a(x-x_0) + b(y-y_0) + c(z-z_0) = 0`.
2. **Plano por 3 pontos não colineares `A, B, C`:** `\vec{n} = \overrightarrow{AB}\times\overrightarrow{AC}`, depois usa um dos pontos.
3. **Mediador do segmento `AB`:** plano ortogonal a `\overrightarrow{AB}` passando pelo ponto médio `M = (A+B)/2`. Equação: `\overrightarrow{AB}\cdot(\vec{r} - M) = 0`.
4. **Plano contendo duas retas concorrentes:** diretor = produto vetorial dos diretores, ponto = ponto de concorrência.
5. **Plano contendo duas retas paralelas:** diretor = produto vetorial do diretor comum com `\overrightarrow{A_1A_2}` (vetor ligando um ponto de cada reta).
6. **Forma paramétrica `(h, t)`:** `\vec{r} = \vec{p} + h\vec{u} + t\vec{v}`, com `\vec{u}, \vec{v}` diretores não paralelos no plano.
7. **Pertinência:** substitua as coordenadas do ponto na equação; se `0 = 0`, pertence.
8. **Aritmética exata:** frações irredutíveis.

---

## 2. Exemplos Guiados

### Exemplo 1 — Plano por ponto e normal
Ponto `P(1, 2, 3)` e normal `\vec{n} = (2, -1, 2)`:
- `2(x-1) - 1(y-2) + 2(z-3) = 0`
- `2x - 2 - y + 2 + 2z - 6 = 0`
- `2x - y + 2z - 6 = 0`

### Exemplo 2 — Plano por 3 pontos
`A(1, 0, 0)`, `B(0, 1, 0)`, `C(0, 0, 1)`:
- `\overrightarrow{AB} = (-1, 1, 0)`, `\overrightarrow{AC} = (-1, 0, 1)`
- `\vec{n} = (-1, 1, 0)\times(-1, 0, 1) = (1, 1, 1)`
- Plano: `1(x-1) + 1(y-0) + 1(z-0) = 0` → `x + y + z - 1 = 0`.

---

## 3. Exercícios (`E04-E01` a `E04-E05`)

### `E04-E01` *(Plano por ponto e normal)*
Ponto `P(2, -1, 3)` e normal `\vec{n} = (1, 2, -2)`:
Escreva a equação geral do plano.

**Formato de resposta:** `ax + by + cz + d = 0`.

---

### `E04-E02` *(Plano por 3 pontos)*
Dados `A(1, 2, 3)`, `B(4, 5, 6)`, `C(7, 8, 10)`:
Verifique se são colineares. Se não, escreva a equação do plano.

**Formato de resposta:** `equacao_do_plano` ou `colineares`.

---

### `E04-E03` *(Mediador de um segmento)*
Dados `A(1, 2, 3)` e `B(5, 6, 7)`:
Escreva a equação do plano mediador do segmento `AB`.

**Formato de resposta:** `ax + by + cz + d = 0`.

---

### `E04-E04` *(Plano contendo duas retas paralelas)*
`r_1: A_1(1, 0, 0) + t(1, 1, 0)` e `r_2: A_2(0, 0, 1) + t(1, 1, 0)`:
Escreva a equação do plano que contém ambas.

**Formato de resposta:** `ax + by + cz + d = 0`.

---

### `E04-E05` *(Forma paramétrica `(h, t)`)*
Plano `2x - y + 3z - 6 = 0`:
Escreva uma forma paramétrica válida `(h, t)`.

**Formato de resposta:** `x = ..., y = ..., z = ...` (em termos de h e t).

---

## 4. Checagem Independente (`E04-C01` a `E04-C03`)

### `E04-C01` *(Plano por ponto e normal com frações)*
Ponto `P(1/2, 1, -1)` e normal `\vec{n} = (2, 1, 1)`:
Equação geral do plano.

**Formato de resposta:** `ax + by + cz + d = 0`.

---

### `E04-C02` *(Pertinência de ponto no plano)*
Plano `3x - 2y + z - 5 = 0` e ponto `Q(2, 1, 2)`:
`Q` pertence ao plano?

**Formato de resposta:** `sim` ou `nao`.

---

### `E04-C03` *(Plano por 3 pontos não colineares)*
`A(0, 0, 0)`, `B(1, 1, 0)`, `C(0, 1, 1)`:
Equação do plano.

**Formato de resposta:** `ax + by + cz + d = 0`.

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `E05`:** somente após autocorreção de `E04-E01`–`E04-E05` e **100% (3/3)** na Checagem Independente `E04-C01`–`E04-C03` sem consulta.
- **Recuperação direcionada (1ª falha):**
  - Se errou o produto vetorial para normal → refaça `D07`.
  - Se errou o mediador → refaça `D02` (ponto médio) e `D07` (produto vetorial).
- **Após 2 tentativas malsucedidas:** interrompa e revise `D07`/`D02` com o orientador.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Parte_4.pdf` p. 24–32 (plano: geral, por 3 pontos, mediador, paramétrica).
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 136–150 (Cap. 5: Plano).
- Gabarito e casos: [E04_gabarito.md](../gabaritos/E04_gabarito.md) e [casos_E04.json](../testes/casos_E04.json).
