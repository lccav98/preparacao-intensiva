# Bloco `E06` — Interseções: Dois Planos, Reta-Plano e Eixos/Planos Coordenados

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio E — A Reta, O Plano e Distâncias no `\mathbb{R}^3` / **`E06`** |
| **Micro-habilidade foco** | Encontrar a reta interseção de dois planos, o ponto interseção de uma reta com um plano (via escalonamento), e os interceptos nos eixos coordenados com área/volume do tetraedro formado. |
| **Pré-requisitos** | `E04`, `C05` |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`E06-E01`–`E06-E05`, 24 min):** `16 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`E06-C01`–`E06-C03`, 16 min):** `12 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** reta interseção de `\pi_1\cap\pi_2`, ponto `r\cap\pi` via escalonamento, interceptos nos eixos + área/volume de tetraedro. **Proibido:** distâncias ponto-plano (`E09`), distância reta-reta (`E08`). |

---

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`E06-E01`–`E06-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`E06-C01`–`E06-C03`):** `___ / 3` | **Tempo:** `___ min (`[ ] Aprovado (100%)  [ ] Recuperação)`

---

## 1. Instruções Curtas

1. **Reta interseção de dois planos:** resolva o sistema `ax+by+cz+d=0` e `a'x+b'y+c'z+d'=0` (3 incógnitas, 2 equações → 1 parâmetro). O diretor da reta é `\vec{n}_1\times\vec{n}_2`.
2. **Ponto `r\cap\pi`:** substitua as paramétricas da reta na equação do plano, resolva para `t`, depois substitua de volta para obter o ponto.
3. **Interceptos nos eixos:** para o eixo `x`, ponha `y=0, z=0` e resolva `x`; análogo para `y` e `z`.
4. **Tetraedro nos interceptos:** se os interceptos são `A(a,0,0)`, `B(0,b,0)`, `C(0,0,c)` e a origem `O(0,0,0)`, o volume é `V = \frac{1}{6}|abc|`.
5. **Área do triângulo nos interceptos:** `A = \frac{1}{2}|\overrightarrow{AB}\times\overrightarrow{AC}|`.
6. **Aritmética exata:** frações irredutíveis.

---

## 2. Exemplos Guiados

### Exemplo 1 — Reta interseção de dois planos
`\pi_1: x + y + z = 3` e `\pi_2: x - y + z = 1`:
- Subtraindo: `2y = 2 → y = 1`.
- Substituindo em `\pi_1`: `x + 1 + z = 3 → x + z = 2`.
- Seja `z = t`: `x = 2 - t`, `y = 1`, `z = t`.
- Reta: `(2, 1, 0) + t(-1, 0, 1)`.

### Exemplo 2 — Ponto reta-plano
`r: x = 1 + t, y = 2 - t, z = 3t` e `\pi: x + y + z = 6`:
- `(1+t) + (2-t) + 3t = 6 → 3 + 3t = 6 → t = 1`.
- Ponto: `(2, 1, 3)`.

---

## 3. Exercícios (`E06-E01` a `E06-E05`)

### `E06-E01` *(Reta interseção de dois planos)*
`\pi_1: x + y + z = 6` e `\pi_2: x - y + z = 2`:
Encontre as equações paramétricas da reta interseção.

**Formato de resposta:** `x = ..., y = ..., z = ...`.

---

### `E06-E02` *(Ponto reta-plano)*
`r: x = 2 + t, y = 1 - t, z = 3 + 2t` e `\pi: 2x + y - z = 4`:
Encontre o ponto de interseção.

**Formato de resposta:** `(x, y, z)` ou `nao_intersectam`.

---

### `E06-E03` *(Interceptos nos eixos)*
Plano `2x + 3y + 6z = 12`:
Encontre os interceptos nos eixos `x`, `y` e `z`.

**Formato de resposta:** `(x_int, y_int, z_int)`.

---

### `E06-E04` *(Volume do tetraedro nos interceptos)*
Plano `x + 2y + 3z = 6`:
Calcule o volume do tetraedro formado pelos interceptos e a origem.

**Formato de resposta:** `valor`.

---

### `E06-E05` *(Área do triângulo nos interceptos)*
Plano `x/3 + y/4 + z/5 = 1` (ou `20x + 15y + 12z = 60`):
Calcule a área do triângulo formado pelos três interceptos nos eixos.

**Formato de resposta:** `valor`.

---

## 4. Checagem Independente (`E06-C01` a `E06-C03`)

### `E06-C01` *(Reta interseção com frações)*
`\pi_1: 2x - y + z = 3` e `\pi_2: x + y - z = 1`:
Equações paramétricas da interseção.

**Formato de resposta:** `x = ..., y = ..., z = ...`.

---

### `E06-C02` *(Ponto reta-plano com parâmetro)*
`r: x = 1 - t, y = 2 + 2t, z = 3t` e `\pi: x + 2y + 3z = 12`:
Ponto de interseção.

**Formato de resposta:** `(x, y, z)` ou `nao_intersectam`.

---

### `E06-C03` *(Volume tetraedro + interceptos)*
Plano `3x + 4y + 12z = 12`:
Volume do tetraedro formado pelos interceptos e a origem.

**Formato de resposta:** `valor`.

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `E07`:** somente após autocorreção de `E06-E01`–`E06-E05` e **100% (3/3)** na Checagem Independente `E06-C01`–`E06-C03` sem consulta.
- **Recuperação direcionada (1ª falha):**
  - Se errou a interseção de planos → refaça `C05` (sistemas `m x n`, 2 equações 3 incógnitas).
  - Se errou o volume do tetraedro → refaça `D09` (produto misto, `V = |det|/6`).
- **Após 2 tentativas malsucedidas:** interrompa e revise `C05`/`D09` com o orientador.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Parte_4.pdf` p. 35–44 (interseções de planos, reta-plano, interceptos, tetraedro).
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 136–164 (Caps. 5 e 6: Plano e Distâncias).
- Gabarito e casos: [E06_gabarito.md](../gabaritos/E06_gabarito.md) e [casos_E06.json](../testes/casos_E06.json).
