# Bloco `F07` — Superfícies Quádricas Canônicas e Traços `[INF/AUS]`

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio F — Seções Cônicas e Superfícies Quádricas / **`F07`** |
| **Micro-habilidade foco** | Identificar as 6 superfícies quádricas centradas/não-centradas (elipsoide, hiperboloide de 1 folha, hiperboloide de 2 folhas, paraboloide elíptico, paraboloide hiperbólico, cone e cilindros) por sinais dos coeficientes e traços nos planos coordenados (`z = k`, `y = k`, `x = k`), sem termo misto (`xy`, `xz`, `yz`). |
| **Pré-requisitos** | `F03`, `F05`, `E06` |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`F07-E01`–`F07-E05`, 22 min):** `16 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`F07-C01`–`F07-C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** classificação das 6 quádricas por sinais e traços coordenados, sem termo misto. **Proibido:** quádricas com termo misto (rotação), provas teóricas. |

---

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`F07-E01`–`F07-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`F07-C01`–`F07-C03`):** `___ / 3` | **Tempo:** `___ min (`[ ] Aprovado (100%)  [ ] Recuperação)`

---

## 1. Instruções Curtas

1. **Quádricas centradas:** equação `Ax² + By² + Cz² + D = 0` (ou `= 1`). Classifique por sinais de `A, B, C` e do termo independente.
2. **Traços coordenados:** corte a superfície pelos planos `x = k`, `y = k`, `z = k`. Cada traço é uma cônica (elipse, hipérbole, parábola, retas, ponto, vazio).
3. **Elipsoide:** `x²/a² + y²/b² + z²/c² = 1`. Todos os traços são elipses.
4. **Hiperboloide de 1 folha:** `x²/a² + y²/b² - z²/c² = 1`. Traços horizontais são elipses, verticais são hipérboles.
5. **Hiperboloide de 2 folhas:** `x²/a² + y²/b² - z²/c² = -1`. Traços verticais são hipérboles, horimontal acima de certo `z` é elipse.
6. **Paraboloide elíptico:** `z = x²/a² + y²/b²`. Traços horizontais são elipses, verticais são parábolas.
7. **Paraboloide hiperbólico:** `z = x²/a² - y²/b²`. Traços horizontais são hipérboles, verticais são parábolas.
8. **Cone:** `x²/a² + y²/b² - z²/c² = 0`. Traços horizontais são elipses (ou ponto), verticais são pares de retas.
9. **Cilindro:** equação em apenas 2 variáveis (ex: `x²/a² + y²/b² = 1` → cilindro elíptico sobre o eixo `z`).
10. **Aritmética exata:** não há cálculos numéricos complexos; é classificação qualitativa por sinais.

---

## 2. Exemplos Guiados

### Exemplo 1 — Hiperboloide de 1 folha
`x²/4 + y²/9 - z²/16 = 1`:
- Sinais: `+ + -`. Termo independente `= 1` (positivo).
- Traço em `z = 0`: `x²/4 + y²/9 = 1` → elipse.
- Traço em `x = 0`: `y²/9 - z²/16 = 1` → hipérbole.
- Classificação: **hiperboloide de 1 folha** ao longo do eixo `z`.

### Exemplo 2 — Paraboloide hiperbólico
`z = x² - y²`:
- Sinais: `+ -`. Traço em `z = k` (constante): `x² - y² = k` → hipérbole (para `k ≠ 0`).
- Traço em `y = 0`: `z = x²` → parábola.
- Classificação: **paraboloide hiperbólico** (selim).

---

## 3. Exercícios (`F07-E01` a `F07-E05`)

### `F07-E01` *(Elipsoide)*
`x²/4 + y²/9 + z²/16 = 1`:
Identifique a superfície.

**Formato de resposta:** `elipsoide`.

---

### `F07-E02` *(Hiperboloide de 1 folha)*
`x² + y² - z² = 1`:
Identifique a superfície e o eixo de simetria.

**Formato de resposta:** `hiperboloide de 1 folha, eixo z`.

---

### `F07-E03` *(Hiperboloide de 2 folhas)*
`x² + y² - z² = -1`:
Identifique a superfície.

**Formato de resposta:** `hiperboloide de 2 folhas`.

---

### `F07-E04` *(Paraboloide elíptico vs. hiperbólico)*
`z = x² + y²`:
Identifique a superfície.

**Formato de resposta:** `paraboloide eliptico`.

---

### `F07-E05` *(Cone e cilindro)*
`x² + y² - z² = 0`:
Identifique a superfície.

**Formato de resposta:** `cone`.

---

## 4. Checagem Independente (`F07-C01` a `F07-C03`)

### `F07-C01` *(Traços coordenados)*
`x²/4 + y²/9 - z² = 1`:
Qual é o traço em `z = 0`?

**Formato de resposta:** `elipse`.

---

### `F07-C02` *(Paraboloide hiperbólico)*
`z = x²/4 - y²/9`:
Identifique a superfície.

**Formato de resposta:** `paraboloide hiperbolico`.

---

### `F07-C03` *(Cilindro)*
`x²/4 + y²/9 = 1`:
Identifique a superfície (qual eixo é o eixo do cilindro?).

**Formato de resposta:** `cilindro eliptico sobre o eixo z`.

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `F08`:** somente após autocorreção de `F07-E01`–`F07-E05` e **100% (3/3)** na Checagem Independente `F07-C01`–`F07-C03` sem consulta.
- **Recuperação direcionada (1ª falha):**
  - Se confundiu hiperboloide de 1 e 2 folhas → confira o sinal do termo independente (`= 1` vs `= -1`).
  - Se confundiu paraboloides → confira se há subtração entre `x²` e `y²` (hiperbólico) ou soma (elíptico).
- **Após 2 tentativas malsucedidas:** interrompa e revise `F03`/`F05` com o orientador.

---

## 6. Referências do Orientador
- `[INF/AUS]` `Planejamento` Sem. 13–14 (quádricas não constam nos 19 PDFs; bloco `F07` marcado como `[INF/AUS]`).
- `[DOC]` `L11` (cônicas como base para traços).
- Gabarito e casos: [F07_gabarito.md](../gabaritos/F07_gabarito.md) e [casos_F07.json](../testes/casos_F07.json).
