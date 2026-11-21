# Bloco `F03` — Elipse na Origem e Circunferência

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio F — Seções Cônicas e Superfícies Quádricas / **`F03`** |
| **Micro-habilidade foco** | Escrever a equação reduzida da elipse centrada na origem (`x²/a² + y²/b² = 1` com `a > b`), identificar semi-eixos, focos, excentricidade `e = c/a < 1`, e reconhecer circunferência como caso particular (`a = b, e = 0`). |
| **Pré-requisitos** | `D04` |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`F03-E01`–`F03-E05`, 20 min):** `14 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`F03-C01`–`F03-C03`, 14 min):** `10 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** elipse na origem com `a² = b² + c²`, focos, excentricidade `e = c/a < 1`, circunferência (`a = b, e = 0`). **Proibido:** elipse transladada (`F04`), hipérbole (`F05`), rotação com termo `xy`. |

---

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`F03-E01`–`F03-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`F03-C01`–`F03-C03`):** `___ / 3` | **Tempo:** `___ min (`[ ] Aprovado (100%)  [ ] Recuperação)`

---

## 1. Instruções Curtas

1. **Elipse na origem:** `x²/a² + y²/b² = 1` com `a > b > 0`. Eixo real horizontal se `a` está sob `x²`.
2. **Semi-eixos:** `a` (eixo maior), `b` (eixo menor). Vértices em `(±a, 0)` e co-vértices em `(0, ±b)`.
3. **Focos:** em `(±c, 0)` com `c = √(a² - b²)` (ou seja, `a² = b² + c²`).
4. **Excentricidade:** `e = c/a`, com `0 < e < 1` para elipse.
5. **Circunferência:** caso particular `a = b = r`. Equação `x² + y² = r²` (ou `x²/a² + y²/a² = 1`). Excentricidade `e = 0`. Foco coincide com o centro `(0, 0)`.
6. **Eixo vertical:** se `b > a`, a equação é `x²/b² + y²/a² = 1` com `a` sob `y²` (eixo real vertical). Neste curso, mantenha `a` sempre sob o termo do eixo maior.
7. **Aritmética exata:** radicais exatos para `c`; frações irredutíveis para `e`.

---

## 2. Exemplos Guiados

### Exemplo 1 — Elipse na origem, eixo horizontal
`x²/25 + y²/16 = 1`:
- `a² = 25 → a = 5`, `b² = 16 → b = 4`. Eixo maior horizontal.
- `c = √(25 - 16) = √9 = 3`. Focos `(±3, 0)`.
- `e = c/a = 3/5`.

### Exemplo 2 — Circunferência
`x² + y² = 9`:
- `a = b = 3`. Circunferência de raio 3 centrada na origem.
- `c = √(9 - 9) = 0`. Foco em `(0, 0)`. `e = 0/3 = 0`.

---

## 3. Exercícios (`F03-E01` a `F03-E05`)

### `F03-E01` *(Elipse na origem, eixo horizontal)*
`x²/16 + y²/9 = 1`:
**(a)** Semi-eixos `a` e `b`.  
**(b)** Focos.  
**(c)** Excentricidade `e`.

**Formato de resposta:** `(a) a=valor, b=valor (b) (+-c, 0) (c) e = fração`.

---

### `F03-E02` *(Elipse na origem, eixo vertical)*
`x²/9 + y²/25 = 1`:
**(a)** Semi-eixos `a` e `b`.  
**(b)** Focos.  
**(c)** Excentricidade `e`.

**Formato de resposta:** `(a) a=valor, b=valor (b) (0, +-c) (c) e = fração`.

---

### `F03-E03` *(Dados a e c, encontrar b e equação)*
Elipse com `a = 5` e foco em `(3, 0)`:
**(a)** Encontre `b`.  
**(b)** Escreva a equação reduzida.

**Formato de resposta:** `(a) b=valor (b) x²/... + y²/... = 1`.

---

### `F03-E04` *(Circunferência como caso particular)*
`x² + y² = 16`:
**(a)** É circunferência?  
**(b)** Raio, centro, excentricidade.

**Formato de resposta:** `(a) sim/nao (b) r=valor, centro=(0,0), e=0`.

---

### `F03-E05` *(Integração: elipse com dados mistos)*
Elipse com vértice em `(4, 0)` e foco em `(2, 0)`:
**(a)** Equação reduzida.  
**(b)** Excentricidade.

**Formato de resposta:** `(a) x²/... + y²/... = 1 (b) e = fração`.

---

## 4. Checagem Independente (`F03-C01` a `F03-C03`)

### `F03-C01` *(Elipse, eixo horizontal)*
`x²/36 + y²/20 = 1`:
**(a)** `c`.  
**(b)** `e`.

**Formato de resposta:** `(a) c=valor (b) e = fração`.

---

### `F03-C02` *(Elipse, eixo vertical)*
`x²/4 + y²/9 = 1`:
**(a)** Semi-eixo maior `a`.  
**(b)** Focos.

**Formato de resposta:** `(a) a=valor (b) (0, +-c)`.

---

### `F03-C03` *(Circunferência)*
`x² + y² = 25`:
Raio e excentricidade.

**Formato de resposta:** `r=valor, e=0`.

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `F04`:** somente após autocorreção de `F03-E01`–`F03-E05` e **100% (3/3)** na Checagem Independente `F03-C01`–`F03-C03` sem consulta.
- **Recuperação direcionada (1ª falha):**
  - Se confundiu `a` e `b` → refaça o esquema gráfico de `a, b, c` em cada cônica.
  - Se errou `e = c/a` → refaça a definição de excentricidade para elipse (`e < 1`).
- **Após 2 tentativas malsucedidas:** interrompa e revise `D04`/`F01` com o orientador.

---

## 6. Referências do Orientador
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 172–177 (Cap. 7: Elipse e circunferência).
- `[DOC]` `P3` p. 172–177; `L11` Ex. 7–8.
- Gabarito e casos: [F03_gabarito.md](../gabaritos/F03_gabarito.md) e [casos_F03.json](../testes/casos_F03.json).
