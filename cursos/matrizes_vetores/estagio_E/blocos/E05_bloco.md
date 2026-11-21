# Bloco `E05` — Ângulos e Posições Relativas Plano-Plano e Reta-Plano

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio E — A Reta, O Plano e Distâncias no `\mathbb{R}^3` / **`E05`** |
| **Micro-habilidade foco** | Calcular o ângulo entre dois planos (via normais) e o ângulo reta-plano (via seno), distinguir cosseno (plano-plano) de seno (reta-plano), e verificar paralelismo estrito reta-plano. |
| **Pré-requisitos** | `E04`, `E02` |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`E05-E01`–`E05-E05`, 22 min):** `14 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`E05-C01`–`E05-C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** ângulo entre planos `\cos\theta = \frac{|\vec{n}_1\cdot\vec{n}_2|}{|\vec{n}_1||\vec{n}_2|}`, ângulo reta-plano `\sin\phi = \frac{|\vec{v}\cdot\vec{n}|}{|\vec{v}||\vec{n}|}`, verificação de ponto fora para paralelismo estrito `r \parallel \pi`. **Proibido:** interseções (`E06`), distâncias (`E07`–`E09`). |

---

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`E05-E01`–`E05-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`E05-C01`–`E05-C03`):** `___ / 3` | **Tempo:** `___ min (`[ ] Aprovado (100%)  [ ] Recuperação)`

---

## 1. Instruções Curtas

1. **Ângulo entre planos:** igual ao ângulo entre suas normais `\vec{n}_1` e `\vec{n}_2`: `\cos\theta = \frac{|\vec{n}_1\cdot\vec{n}_2|}{|\vec{n}_1||\vec{n}_2|}` (ângulo agudo).
2. **Ângulo reta-plano:** complementar ao ângulo entre o vetor diretor `\vec{v}` e a normal `\vec{n}`: `\sin\phi = \frac{|\vec{v}\cdot\vec{n}|}{|\vec{v}||\vec{n}|}`, onde `\phi` é o ângulo entre a reta e o plano.
3. **Planos paralelos:** normais proporcionais `\vec{n}_1 = k\vec{n}_2`.
4. **Paralelismo estrito reta-plano:** `\vec{v}\perp\vec{n}` (ou seja, `\vec{v}\cdot\vec{n} = 0`) E um ponto da reta não pertence ao plano.
5. **Cosseno (plano-plano) vs. Seno (reta-plano):** não confundir. Plano-plano usa cosseno das normais; reta-plano usa seno do diretor com a normal.
6. **Aritmética exata:** frações irredutíveis e radicais exatos.

---

## 2. Exemplos Guiados

### Exemplo 1 — Ângulo entre planos
`\pi_1: x + 2y + 2z - 3 = 0` (`\vec{n}_1 = (1, 2, 2)`) e `\pi_2: 2x - y + 2z + 1 = 0` (`\vec{n}_2 = (2, -1, 2)`):
- `\vec{n}_1\cdot\vec{n}_2 = 2 - 2 + 4 = 4`
- `|\vec{n}_1| = 3`, `|\vec{n}_2| = 3`
- `\cos\theta = 4/9` → `\theta = \arccos(4/9)`.

### Exemplo 2 — Ângulo reta-plano
Reta com `\vec{v} = (1, 2, 2)` e plano com `\vec{n} = (2, -1, 2)`:
- `\vec{v}\cdot\vec{n} = 2 - 2 + 4 = 4`
- `|\vec{v}| = 3`, `|\vec{n}| = 3`
- `\sin\phi = 4/9` → `\phi = \arcsin(4/9)`.

---

## 3. Exercícios (`E05-E01` a `E05-E05`)

### `E05-E01` *(Ângulo entre dois planos)*
`\pi_1: x + y + z - 1 = 0` e `\pi_2: x - y + z - 1 = 0`:
Calcule `\cos\theta` do ângulo agudo entre os planos.

**Formato de resposta:** `cos = fração`.

---

### `E05-E02` *(Ângulo reta-plano)*
Reta com diretor `\vec{v} = (1, 1, 1)` e plano `x + y + z - 3 = 0`:
Calcule `\sin\phi` do ângulo reta-plano.

**Formato de resposta:** `sen = fração`.

---

### `E05-E03` *(Paralelismo estrito reta-plano)*
Reta passando por `P(1, 2, 3)` com diretor `\vec{v} = (1, -1, 0)` e plano `x - y + 2z - 5 = 0`:
A reta é paralela estritamente ao plano?

**Formato de resposta:** `sim` ou `nao`.

---

### `E05-E04` *(Planos paralelos)*
`\pi_1: 2x - 4y + 4z - 3 = 0` e `\pi_2: x - 2y + 2z + 1 = 0`:
São paralelos?

**Formato de resposta:** `sim` ou `nao`.

---

### `E05-E05` *(Cosseno vs. Seno — não confundir)*
Planos com normais `\vec{n}_1 = (1, 0, 0)` e `\vec{n}_2 = (0, 1, 0)`:
**(a)** Ângulo entre os planos (cosseno).  
**(b)** Se uma reta tem diretor `(1, 0, 0)` e o plano tem normal `(0, 1, 0)`, qual é o seno do ângulo reta-plano?

**Formato de resposta:** `(a) cos = valor (b) sen = valor`.

---

## 4. Checagem Independente (`E05-C01` a `E05-C03`)

### `E05-C01` *(Ângulo entre planos com frações)*
`\pi_1: 2x - y + 2z - 3 = 0` e `\pi_2: x + 2y - 2z + 1 = 0`:
Calcule `\cos\theta`.

**Formato de resposta:** `cos = fração`.

---

### `E05-C02` *(Ângulo reta-plano com seno)*
Reta `\vec{v} = (3, 4, 0)` e plano `3x + 4y - 5 = 0`:
Calcule `\sin\phi`.

**Formato de resposta:** `sen = fração`.

---

### `E05-C03` *(Paralelismo estrito reta-plano — ponto fora)*
Reta passando por `P(0, 0, 1)` com diretor `(1, 1, 0)` e plano `x + y - 2 = 0`:
A reta é paralelamente estrita ao plano?

**Formato de resposta:** `sim` ou `nao`.

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `E06`:** somente após autocorreção de `E05-E01`–`E05-E05` e **100% (3/3)** na Checagem Independente `E05-C01`–`E05-C03` sem consulta.
- **Recuperação direcionada (1ª falha):**
  - Se trocou cosseno por seno → refaça a distinção plano-plano (cosseno das normais) vs reta-plano (seno diretor-normal).
  - Se errou paralelismo → verifique `\vec{v}\cdot\vec{n} = 0` e ponto fora do plano.
- **Após 2 tentativas malsucedidas:** interrompa e revise `E02`/`E04` com o orientador.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Parte_4.pdf` p. 33–34 (ângulo plano-plano e reta-plano).
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 136–150 (Cap. 5: Plano).
- Gabarito e casos: [E05_gabarito.md](../gabaritos/E05_gabarito.md) e [casos_E05.json](../testes/casos_E05.json).
