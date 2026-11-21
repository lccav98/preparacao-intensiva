# Bloco `E09` — Distâncias Envolvendo Planos (Ponto-Plano, Planos Paralelos, Reta-Plano)

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio E — A Reta, O Plano e Distâncias no `\mathbb{R}^3` / **`E09`** |
| **Micro-habilidade foco** | Calcular distância ponto-plano `d = \frac{|ax_0+by_0+cz_0+d|}{\sqrt{a^2+b^2+c^2}}`, distância entre planos paralelos (normalizando coeficientes antes de `|d_1-d_2|`), e distância reta-plano para reta paralela. |
| **Pré-requisitos** | `E05`, `E07` |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`E09-E01`–`E09-E05`, 22 min):** `14 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`E09-C01`–`E09-C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** fórmula ponto-plano, normalização de `(a,b,c)` antes de `|d_1-d_2|`, `d(r,\pi)` para reta paralela. **Proibido:** distância reta-reta (`E08`, já feito). |

---

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`E09-E01`–`E09-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`E09-C01`–`E09-C03`):** `___ / 3` | **Tempo:** `___ min (`[ ] Aprovado (100%)  [ ] Recuperação)`

---

## 1. Instruções Curtas

1. **Distância ponto-plano:** dado `P_0(x_0, y_0, z_0)` e `\pi: ax + by + cz + d = 0`,
   `d(P_0, \pi) = \frac{|ax_0 + by_0 + cz_0 + d|}{\sqrt{a^2 + b^2 + c^2}}`. Use valor absoluto no numerador.
2. **Planos paralelos:** `\pi_1: ax+by+cz+d_1=0` e `\pi_2: kax+kby+kcz+d_2=0`. **Normalize** dividindo `\pi_2` por `k` para que os coeficientes de `x, y, z` coincidam com `\pi_1`, depois calcule `d = \frac{|d_1 - d_2'|}{\sqrt{a^2+b^2+c^2}}`.
3. **Distância reta-plano (reta paralela):** se a reta é paralela ao plano (`\vec{v}\cdot\vec{n} = 0`), a distância é a distância de qualquer ponto da reta ao plano (use a fórmula ponto-plano).
4. **Erro comum:** não dividir `\pi_2` pelo fator de proporcionalidade antes de subtrair `d_1` e `d_2`.
5. **Aritmética exata:** frações irredutíveis e radicais exatos.

---

## 2. Exemplos Guiados

### Exemplo 1 — Distância ponto-plano
`P_0(1, 3, -1)` e `\pi: 2x - y + 2z - 6 = 0`:
- Numerador: `|2(1) - 3 + 2(-1) - 6| = |2 - 3 - 2 - 6| = |-9| = 9`.
- Denominador: `\sqrt{4 + 1 + 4} = 3`.
- `d = 9/3 = 3`.

### Exemplo 2 — Planos paralelos (normalização obrigatória)
`\pi_1: x - 2y + 2z - 3 = 0` e `\pi_2: 2x - 4y + 4z + 6 = 0`:
- Divida `\pi_2` por 2: `x - 2y + 2z + 3 = 0`.
- Agora `d_1 = -3`, `d_2' = 3`.
- `d = \frac{|-3 - 3|}{\sqrt{1+4+4}} = \frac{6}{3} = 2`.

---

## 3. Exercícios (`E09-E01` a `E09-E05`)

### `E09-E01` *(Distância ponto-plano)*
`P_0(2, 1, -1)` e `\pi: x + 2y + 2z - 3 = 0`:
Calcule `d(P_0, \pi)`.

**Formato de resposta:** `valor`.

---

### `E09-E02` *(Planos paralelos — normalização)*
`\pi_1: 3x - 4y + 12z - 5 = 0` e `\pi_2: 6x - 8y + 24z + 10 = 0`:
Distância entre eles.

**Formato de resposta:** `valor`.

---

### `E09-E03` *(Distância reta-plano, reta paralela)*
Reta `r: (1, 0, 0) + t(1, 1, 0)` e plano `x + y - 2 = 0`:
Verifique se `r` é paralela a `\pi`. Se sim, calcule a distância.

**Formato de resposta:** `valor` ou `nao_paralela`.

---

### `E09-E04` *(Distância ponto-plano com frações)*
`P_0(1/2, 1, -1/2)` e `\pi: 2x - y + 2z - 3 = 0`:
Calcule `d(P_0, \pi)`.

**Formato de resposta:** `valor`.

---

### `E09-E05` *(Integração: ponto-plano e planos paralelos)*
`P_0(1, 2, 3)` e `\pi: 2x - y + 2z - 6 = 0`:
**(a)** Distância `d(P_0, \pi)`.  
**(b)** Plano paralelo `\pi': 4x - 2y + 4z + 8 = 0`. Distância entre `\pi` e `\pi'`.

**Formato de resposta:** `(a) valor (b) valor`.

---

## 4. Checagem Independente (`E09-C01` a `E09-C03`)

### `E09-C01` *(Distância ponto-plano exata)*
`P_0(1, 2, 3)` e `\pi: x - 2y + 2z - 4 = 0`:
Calcule `d(P_0, \pi)`.

**Formato de resposta:** `valor`.

---

### `E09-C02` *(Planos paralelos com normalização)*
`\pi_1: x + y + z - 1 = 0` e `\pi_2: 2x + 2y + 2z + 5 = 0`:
Distância entre eles.

**Formato de resposta:** `valor`.

---

### `E09-C03` *(Distância reta-plano — ponto da reta ao plano)*
Reta `r: (2, 1, 0) + t(1, -1, 0)` e plano `x - y - 3 = 0`:
Distância (verifique paralelismo primeiro).

**Formato de resposta:** `valor` ou `nao_paralela`.

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `E10`:** somente após autocorreção de `E09-E01`–`E09-E05` e **100% (3/3)** na Checagem Independente `E09-C01`–`E09-C03` sem consulta.
- **Recuperação direcionada (1ª falha):**
  - Se esqueceu normalizar → sempre divida o segundo plano pelo fator de proporcionalidade antes de subtrair `d`.
  - Se errou o valor absoluto → lembre: `|ax_0+by_0+cz_0+d|` no numerador.
- **Após 2 tentativas malsucedidas:** interrompa e revise `E05`/`E07` com o orientador.

---

## 6. Referências do Orientador
- `[DOC]` `MAT121_Parte_4.pdf` p. 50–52, 59–61 (ponto-plano, planos paralelos, reta-plano).
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 151–164 (Cap. 6: Distâncias).
- Gabarito e casos: [E09_gabarito.md](../gabaritos/E09_gabarito.md) e [casos_E09.json](../testes/casos_E09.json).
