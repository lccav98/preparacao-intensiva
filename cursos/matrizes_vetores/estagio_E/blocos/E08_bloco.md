# Bloco `E08` — Distância entre Duas Retas (Concorrentes, Paralelas e Reversas)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio E — A Reta, O Plano e Distâncias no `\mathbb{R}^3` / **`E08`** |
| **Micro-habilidade foco** | Verificar se duas retas são paralelas antes de escolher a fórmula: distância ponto-reta (se paralelas) ou fórmula do paralelepípedo `d = \frac{|(\vec{u},\vec{v},\overrightarrow{P_1P_2})|}{|\vec{u}\times\vec{v}|}` (se reversas). |
| **Pré-requisitos** | `E03`, `E07`, `D09` |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`E08-E01`–`E08-E05`, 22 min):** `14 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`E08-C01`–`E08-C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** verificar `\vec{v}_1 \parallel \vec{v}_2` antes de escolher `d(P_0, s)` vs. fórmula do paralelepípedo. **Proibido:** distâncias envolvendo planos (`E09`). |

---

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`E08-E01`–`E08-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`E08-C01`–`E08-C03`):** `___ / 3` | **Tempo:** `___ min (`[ ] Aprovado (100%)  [ ] Recuperação)`

---

## 1. Instruções Curtas

1. **Primeiro passo:** verifique se `\vec{v}_1 \parallel \vec{v}_2` (diretores proporcionais).
2. **Se paralelas:** escolha um ponto `P_0` de uma reta e calcule `d(P_0, s)` (distância ponto-reta da outra reta).
3. **Se reversas (não coplanares):** use a fórmula do paralelepípedo:
   `d = \frac{|(\vec{u},\vec{v},\overrightarrow{P_1P_2})|}{|\vec{u}\times\vec{v}|}`
   onde `\vec{u}`, `\vec{v}` são os diretores e `\overrightarrow{P_1P_2}` liga um ponto de cada reta.
4. **Se concorrentes:** a distância é `0` (se intersectam).
5. **Ordem dos itens no produto misto:** o valor absoluto torna a ordem irrelevante para o módulo, mas mantenha consistência.
6. **Aritmética exata:** frações irredutíveis e radicais exatos.

---

## 2. Exemplos Guiados

### Exemplo 1 — Retas paralelas
`r_1: (0, 0, 0) + t(1, 1, 0)` e `r_2: (1, 0, 1) + t(1, 1, 0)`:
- Diretores iguais → paralelas.
- Ponto `P_0(0, 0, 0)` de `r_1`, reta `r_2: (1, 0, 1) + t(1, 1, 0)`.
- `\overrightarrow{P_1P_0}` (de `r_2` para `P_0`) = `(-1, 0, -1)`.
- `\vec{v}\times\overrightarrow{P_1P_0} = (1, 1, 0)\times(-1, 0, -1) = (-1, 1, 1)`, módulo = `\sqrt{3}`.
- `|\vec{v}| = \sqrt{2}`.
- `d = \sqrt{3}/\sqrt{2} = \sqrt{6}/2`.

### Exemplo 2 — Retas reversas
`r_1: (0, 0, 0) + t(1, 0, 0)` e `r_2: (0, 1, 0) + t(0, 0, 1)`:
- Diretores `(1, 0, 0)` e `(0, 0, 1)` não são paralelos.
- `\overrightarrow{P_1P_2} = (0, 1, 0)`.
- Produto misto: `det[(1,0,0), (0,0,1), (0,1,0)] = 1(0-0) - 0 + 0 = 0`... espere, vou recalcular.
- `\vec{u}\times\vec{v} = (1,0,0)\times(0,0,1) = (0\cdot1 - 0\cdot0,\; 0\cdot0 - 1\cdot1,\; 1\cdot0 - 0\cdot0) = (0, -1, 0)`.
- `|(0,-1,0)| = 1`.
- Produto misto `(1,0,0)\cdot(0,-1,0) = 0`. Hmm, essas retas são coplanares (no plano `y` variável?). Na verdade `(0,0,0)+t(1,0,0)` está em `z=0, y=0`; `(0,1,0)+t(0,0,1)` está em `x=0, y=1`. São reversas (não se intersectam, não paralelas).
- Vou ajustar: `\vec{u}=(1,0,0)`, `\vec{v}=(0,0,1)`, `\overrightarrow{P_1P_2}=(0,1,0)`.
- `\vec{u}\times\vec{v} = (0, -1, 0)`. `|...| = 1`.
- Produto misto: `(1,0,0)\cdot((0,0,1)\times(0,1,0))`. `(0,0,1)\times(0,1,0) = (-1, 0, 0)`. `(1,0,0)\cdot(-1,0,0) = -1`. `|−1| = 1`.
- `d = 1/1 = 1`.

---

## 3. Exercícios (`E08-E01` a `E08-E05`)

### `E08-E01` *(Verificar paralelismo primeiro)*
`r_1: (1, 2, 3) + t(2, 4, 6)` e `r_2: (0, 0, 0) + s(1, 2, 3)`:
São paralelas?

**Formato de resposta:** `sim` ou `nao`.

---

### `E08-E02` *(Distância entre retas paralelas)*
`r_1: (0, 0, 0) + t(1, 0, 0)` e `r_2: (0, 1, 0) + s(1, 0, 0)`:
Distância entre elas.

**Formato de resposta:** `valor`.

---

### `E08-E03` *(Distância entre retas reversas — paralelepípedo)*
`r_1: (0, 0, 0) + t(1, 0, 0)` e `r_2: (0, 1, 0) + s(0, 0, 1)`:
Distância entre elas.

**Formato de resposta:** `valor`.

---

### `E08-E04` *(Retas concorrentes → distância zero)*
`r_1: (0, 0, 0) + t(1, 1, 0)` e `r_2: (2, 2, 0) + s(-1, -1, 0)`:
Distância entre elas.

**Formato de resposta:** `valor`.

---

### `E08-E05` *(Integração: classificação + distância)*
`r_1: (1, 0, 0) + t(0, 1, 0)` e `r_2: (0, 0, 1) + s(0, 1, 0)`:
**(a)** São paralelas?  
**(b)** Distância entre elas.

**Formato de resposta:** `(a) sim/nao (b) valor`.

---

## 4. Checagem Independente (`E08-C01` a `E08-C03`)

### `E08-C01` *(Retas reverses com produto misto)*
`r_1: (1, 2, 3) + t(1, 0, 0)` e `r_2: (4, 5, 6) + s(0, 1, 0)`:
Distância entre elas.

**Formato de resposta:** `valor`.

---

### `E08-C02` *(Retas paralelas com frações)*
`r_1: (0, 0, 0) + t(2, 2, 0)` e `r_2: (1, 1, 1) + s(1, 1, 0)`:
Distância entre elas.

**Formato de resposta:** `valor`.

---

### `E08-C03` *(Classificação e distância)*
`r_1: (0, 0, 0) + t(1, 2, 3)` e `r_2: (3, 2, 1) + s(-1, -2, -3)`:
**(a)** Paralelas?  
**(b)** Distância.

**Formato de resposta:** `(a) sim/nao (b) valor`.

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `E09`:** somente após autocorreção de `E08-E01`–`E08-E05` e **100% (3/3)** na Checagem Independente `E08-C01`–`E08-C03` sem consulta.
- **Recuperação direcionada (1ª falha):**
  - Se esqueceu verificar paralelismo → sempre teste `\vec{v}_1 \parallel \vec{v}_2` primeiro.
  - Se errou o paralelepípedo → refaça `D09` (produto misto, `|\vec{u}\times\vec{v}|`).
- **Após 2 tentativas malsucedidas:** interrompa e revise `D09`/`E07` com o orientador.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Parte_4.pdf` p. 48–49, 53–58 (distância entre retas).
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 151–164 (Cap. 6: Distâncias).
- Gabarito e casos: [E08_gabarito.md](../gabaritos/E08_gabarito.md) e [casos_E08.json](../testes/casos_E08.json).
