# Bloco `F04` — Elipse Transladada e Completamento de Quadrados

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio F — Seções Cônicas e Superfícies Quádricas / **`F04`** |
| **Micro-habilidade foco** | Escrever a equação reduzida de uma elipse transladada `((x-h)²/a² + (y-k)²/b² = 1)` via completamento de quadrados, identificar centro `C(h, k)`, vértices, focos e excentricidade. |
| **Pré-requisitos** | `F03`, `F02` |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`F04-E01`–`F04-E05`, 22 min):** `16 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`F04-C01`–`F04-C03`, 15 min):** `11 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** fatoração `A(x² + bx) + B(y² + dy)`, centro `C(h, k)`, vértices, focos, excentricidade. **Proibido:** hipérbole transladada (`F06`), termo misto `xy`. |

---

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`F04-E01`–`F04-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`F04-C01`–`F04-C03`):** `___ / 3` | **Tempo:** `___ min (`[ ] Aprovado (100%)  [ ] Recuperação)`

---

## 1. Instruções Curtas

1. **Completamento de quadrados:** agrupe termos em `x` e em `y`, fatore o coeficiente do quadrado, complete o quadrado dentro dos parênteses, mova constantes para o lado direito.
2. **Equação reduzida transladada:** `(x-h)²/a² + (y-k)²/b² = 1` com centro `C(h, k)`.
3. **Centro:** `C(h, k)` vem dos termos `(x-h)` e `(y-k)`.
4. **Vértices:** `(h ± a, k)` (eixo horizontal) ou `(h, k ± a)` (eixo vertical).
5. **Focos:** `(h ± c, k)` ou `(h, k ± c)` com `c = √(a² - b²)`.
6. **Excentricidade:** `e = c/a < 1`.
7. **Aritmética exata:** mantenha frações irredutíveis e radicais exatos em todas as etapas.

---

## 2. Exemplos Guiados

### Exemplo 1 — Elipse transladada
`4x² + 9y² - 16x + 18y - 11 = 0`:
- `4(x² - 4x) + 9(y² + 2y) = 11`
- `4(x² - 4x + 4) + 9(y² + 2y + 1) = 11 + 16 + 9 = 36`
- `4(x-2)² + 9(y+1)² = 36`
- `(x-2)²/9 + (y+1)²/4 = 1`
- Centro `C(2, -1)`, `a² = 9 → a = 3`, `b² = 4 → b = 2`.
- `c = √(9 - 4) = √5`. Focos `(2 ± √5, -1)`. `e = √5/3`.

---

## 3. Exercícios (`F04-E01` a `F04-E05`)

### `F04-E01` *(Completamento de quadrados simples)*
`x² + 4y² - 4x + 8y + 4 = 0`:
Escreva a equação reduzida e informe o centro.

**Formato de resposta:** `(x-h)²/a² + (y-k)²/b² = 1, centro (h, k)`.

---

### `F04-E02` *(Elipse transladada com coeficientes)*
`9x² + 4y² - 54x - 16y + 61 = 0`:
**(a)** Equação reduzida.  
**(b)** Centro `C(h, k)`.

**Formato de resposta:** `(a) (x-h)²/... + (y-k)²/... = 1 (b) (h, k)`.

---

### `F04-E03` *(Vértices e focos de elipse transladada)*
`(x-3)²/25 + (y+2)²/9 = 1`:
**(a)** Vértices.  
**(b)** Focos.

**Formato de resposta:** `(a) (h+-a, k) (b) (h+-c, k)`.

---

### `F04-E04` *(Excentricidade de elipse transladada)*
`(x+1)²/16 + (y-4)²/7 = 1`:
Calcule `c` e `e`.

**Formato de resposta:** `c = radical, e = fração`.

---

### `F04-E05` *(Reconhecer elipse vs. circunferência transladada)*
`(x-2)² + (y+3)² = 16`:
**(a)** É elipse ou circunferência?  
**(b)** Centro e raio.

**Formato de resposta:** `(a) circunferencia/elipse (b) centro=(h,k), r=valor`.

---

## 4. Checagem Independente (`F04-C01` a `F04-C03`)

### `F04-C01` *(Completamento de quadrados)*
`x² + y² - 6x + 4y - 12 = 0`:
**(a)** É circunferência?  
**(b)** Centro e raio.

**Formato de resposta:** `(a) sim/nao (b) centro=(h,k), r=valor`.

---

### `F04-C02` *(Elipse transladada, eixo vertical)*
`4(x-1)² + 9(y+2)² = 36`:
**(a)** Equação reduzida.  
**(b)** `a`, `b`, `c`.

**Formato de resposta:** `(a) (x-h)²/... + (y-k)²/... = 1 (b) a=..., b=..., c=...`.

---

### `F04-C03` *(Focos de elipse transladada)*
`(x+2)²/49 + (y-3)²/36 = 1`:
Focos.

**Formato de resposta:** `(h+-c, k)` com valores.

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `F05`:** somente após autocorreção de `F04-E01`–`F04-E05` e **100% (3/3)** na Checagem Independente `F04-C01`–`F04-C03` sem consulta.
- **Recuperação direcionada (1ª falha):**
  - Se errou o sinal ao completar o quadrado → confira a expansão de `(x-h)²`.
  - Se confundiu eixo maior → confira qual denominador é maior.
- **Após 2 tentativas malsucedidas:** interrompa e revise `F03`/`F02` com o orientador.

---

## 6. Referências do Orientador
- `[DOC]` `P3` p. 176–177; `L11` Ex. 9–10.
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 172–177 (Cap. 7: Elipse transladada).
- Gabarito e casos: [F04_gabarito.md](../gabaritos/F04_gabarito.md) e [casos_F04.json](../testes/casos_F04.json).
