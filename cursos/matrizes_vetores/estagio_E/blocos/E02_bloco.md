# Bloco `E02` — Ângulo, Paralelismo, Ortogonalidade e Reta Ortogonal a Duas

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio E — A Reta, O Plano e Distâncias no `\mathbb{R}^3` / **`E02`** |
| **Micro-habilidade foco** | Calcular o ângulo entre duas retas (sempre agudo, `\le 90^\circ`), reconhecer paralelismo e ortogonalidade de vetores diretores, e construir a reta ortogonal a duas retas dadas (vetor diretor = produto vetorial dos diretores). |
| **Pré-requisitos** | `E01`, `D05`, `D07` |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`E02-E01`–`E02-E05`, 22 min):** `14 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`E02-C01`–`E02-C03`, 14 min):** `10 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** `\cos\theta = \frac{|\vec{v}_1\cdot\vec{v}_2|}{|\vec{v}_1||\vec{v}_2|}` (ângulo agudo), paralelismo `\vec{v}_1 \parallel \vec{v}_2`, ortogonalidade `\vec{v}_1 \perp \vec{v}_2`, `\vec{v}_r = \vec{v}_1\times\vec{v}_2`. **Proibido:** coplanaridade de retas (`E03`), planos (`E04`). |

---

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`E02-E01`–`E02-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`E02-C01`–`E02-C03`):** `___ / 3` | **Tempo:** `___ min (`[ ] Aprovado (100%)  [ ] Recuperação)`

---

## 1. Instruções Curtas

1. **Ângulo entre retas:** sempre o ângulo agudo (ou reto), `\cos\theta = \frac{|\vec{v}_1\cdot\vec{v}_2|}{|\vec{v}_1||\vec{v}_2|}`, com `\theta \in [0, \pi/2]`. Use valor absoluto no produto escalar.
2. **Paralelismo:** `\vec{v}_1 = k\vec{v}_2` (proporcionalidade de componentes).
3. **Ortogonalidade:** `\vec{v}_1\cdot\vec{v}_2 = 0`.
4. **Reta ortogonal a duas retas:** se `r_1` tem diretor `\vec{v}_1` e `r_2` tem diretor `\vec{v}_2`, a reta ortogonal a ambas tem diretor `\vec{v}_r = \vec{v}_1\times\vec{v}_2` (produto vetorial, mão direita).
5. **Produto vetorial:** `\vec{u}\times\vec{v} = (u_2v_3 - u_3v_2,\; u_3v_1 - u_1v_3,\; u_1v_2 - u_2v_1)`.
6. **Módulo:** `|\vec{v}| = \sqrt{v_1^2 + v_2^2 + v_3^2}`.
7. **Aritmética exata:** frações irredutíveis e radicais exatos.

---

## 2. Exemplos Guiados

### Exemplo 1 — Ângulo entre duas retas
`r_1` com `\vec{v}_1 = (1, 2, 2)` e `r_2` com `\vec{v}_2 = (2, -1, 2)`:
- `\vec{v}_1\cdot\vec{v}_2 = 2 - 2 + 4 = 4`
- `|\vec{v}_1| = \sqrt{1+4+4} = 3`, `|\vec{v}_2| = \sqrt{4+1+4} = 3`
- `\cos\theta = \frac{|4|}{3\cdot 3} = \frac{4}{9}` → `\theta = \arccos(4/9)` (ângulo agudo).

### Exemplo 2 — Reta ortogonal a duas
`\vec{v}_1 = (1, 0, 1)`, `\vec{v}_2 = (0, 1, 1)`:
- `\vec{v}_r = \vec{v}_1\times\vec{v}_2 = (0\cdot1 - 1\cdot1,\; 1\cdot0 - 1\cdot1,\; 1\cdot1 - 0\cdot0) = (-1, -1, 1)`.
- A reta ortogonal a ambas tem diretor `(-1, -1, 1)` (ou `(1, 1, -1)`).

---

## 3. Exercícios (`E02-E01` a `E02-E05`)

### `E02-E01` *(Ângulo entre duas retas)*
Dados `\vec{v}_1 = (1, 2, 2)` e `\vec{v}_2 = (2, 1, -2)`:
Calcule o ângulo agudo entre as retas. Informe `\cos\theta` como fração exata.

**Formato de resposta:** `cos = fração`.

---

### `E02-E02` *(Paralelismo de vetores diretores)*
Determine se `\vec{u} = (2, 4, -6)` e `\vec{v} = (-1, -2, 3)` são paralelos. Se sim, informe o fator `k` tal que `\vec{u} = k\vec{v}`.

**Formato de resposta:** `sim k = valor` ou `nao`.

---

### `E02-E03` *(Ortogonalidade)*
Dados `\vec{a} = (1, 2, -1)` e `\vec{b} = (2, -1, 0)`:
Verifique se são ortogonais (produto escalar nulo).

**Formato de resposta:** `sim` ou `nao`.

---

### `E02-E04` *(Reta ortogonal a duas retas)*
Dados `\vec{v}_1 = (1, 2, 3)` e `\vec{v}_2 = (2, -1, 1)`:
Calcule um vetor diretor da reta ortogonal a ambas via produto vetorial.

**Formato de resposta:** `(a, b, c)`.

---

### `E02-E05` *(Integração: ângulo + ortogonalidade)*
Dados `\vec{p} = (1, 1, 1)` e `\vec{q} = (1, -1, 2)`:
**(a)** São ortogonais?  
**(b)** Qual é `\cos\theta` do ângulo agudo entre elas?

**Formato de resposta:** `(a) sim/nao (b) cos = fração`.

---

## 4. Checagem Independente (`E02-C01` a `E02-C03`)

### `E02-C01` *(Ângulo agudo com frações)*
Dados `\vec{r} = (3, 4, 0)` e `\vec{s} = (1, 0, 2)`:
Calcule `\cos\theta` do ângulo agudo.

**Formato de resposta:** `cos = fração`.

---

### `E02-C02` *(Reta ortogonal a duas retas coordenadas)*
Dados `\vec{v}_1 = (1, 0, 0)` e `\vec{v}_2 = (0, 1, 0)`:
Calcule o vetor diretor da reta ortogonal a ambas.

**Formato de resposta:** `(a, b, c)`.

---

### `E02-C03` *(Paralelismo com frações)*
Dados `\vec{m} = (1/2, 1, -3/2)` e `\vec{n} = (1, 2, -3)`:
São paralelos? Informe o fator `k`.

**Formato de resposta:** `sim k = valor` ou `nao`.

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `E03`:** somente após autocorreção de `E02-E01`–`E02-E05` e **100% (3/3)** na Checagem Independente `E02-C01`–`E02-C03` sem consulta.
- **Recuperação direcionada (1ª falha):**
  - Se errou o ângulo → refaça `D05` (produto escalar e cossenos) e `D07` (módulo).
  - Se errou o produto vetorial → refaça `D07`.
- **Após 2 tentativas malsucedidas:** interrompa e revise `D05`/`D07` com o orientador.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Parte_4.pdf` p. 10–11, 14–17 (ângulo, paralelismo, reta ortogonal a duas).
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 124–135 (Cap. 4: Reta).
- Gabarito e casos: [E02_gabarito.md](../gabaritos/E02_gabarito.md) e [casos_E02.json](../testes/casos_E02.json).
