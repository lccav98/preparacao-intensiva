# Bloco `F06` — Hipérbole Transladada e Reconhecimento Geral de Cônicas

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio F — Seções Cônicas e Superfícies Quádricas / **`F06`** |
| **Micro-habilidade foco** | Escrever a equação reduzida de uma hipérbole transladada via completamento de quadrados, reconhecer o sinal do lado direito (armadilha: dividir por negativo inverte a cônica), e classificar cônicas gerais sem termo `xy` pelos coeficientes `A` e `C`. |
| **Pré-requisitos** | `F05`, `F04` |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática + checagem** — **Sessão única (`F06-E01`–`F06-E05`, 24 min):** `18 min` resol. \| `4 min` corr. \| `4 min` recup.; **Checagem (`F06-C01`–`F06-C03`, 16 min):** `12 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **Permitido:** hipérbole transladada, armadilha do sinal negativo, classificação geral por `A` e `C` (sem `xy`). **Proibido:** quádricas (`F07`), rotação com termo `xy`. |

---

### Registro da Sessão (Preenchido na Prática)
- **Sessão única (`F06-E01`–`F06-E05`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tentativa:** `___ / 5` | **Após autocorreção:** `___ / 5`
- **Checagem independente (sem gabarito) (`F06-C01`–`F06-C03`):** `___ / 3` | **Tempo:** `___ min (`[ ] Aprovado (100%)  [ ] Recuperação)`

---

## 1. Instruções Curtas

1. **Hipérbole transladada:** complete os quadrados para obter `(x-h)²/a² - (y-k)²/b² = 1` ou `(y-k)²/a² - (x-h)²/b² = 1`. Centro `C(h, k)`.
2. **Armadilha do sinal negativo:** se após completar o quadrados o lado direito for negativo (ex: `-36`), multiplique toda a equação por `-1` antes de dividir. Isso inverte qual termo é positivo e, portanto, qual é o eixo real.
3. **Classificação geral sem `xy`:** equação `Ax² + Cy² + Dx + Ey + F = 0`.
   - `A = C ≠ 0`: circunferência.
   - `A` e `C` same sign, `A ≠ C`: elipse.
   - `A` e `C` opposite signs: hipérbole.
   - `A = 0` ou `C = 0` (mas não ambos): parábola.
4. **Aritmética exata:** frações irredutíveis e radicais exatos.

---

## 2. Exemplos Guiados

### Exemplo 1 — Armadilha do sinal negativo
`9(x-3)² - 4(y-1)² = -36`:
- O lado direito é negativo. Multiplique por `-1`: `-9(x-3)² + 4(y-1)² = 36`.
- Divida por 36: `-(x-3)²/4 + (y-1)²/9 = 1`, ou seja, `(y-1)²/9 - (x-3)²/4 = 1`.
- É uma hipérbole com eixo real vertical (o termo positivo está sob `y`). Centro `C(3, 1)`, `a² = 9`, `b² = 4`.

---

## 3. Exercícios (`F06-E01` a `F06-E05`)

### `F06-E01` *(Hipérbole transladada, eixo horizontal)*
`(x-2)²/16 - (y+3)²/9 = 1`:
**(a)** Centro.  
**(b)** Focos.  
**(c)** Assíntotas.

**Formato de resposta:** `(a) (h, k) (b) (h+-c, k) (c) y-k = +-(b/a)(x-h)`.

---

### `F06-E02` *(Armadilha do sinal negativo)*
`4(x-1)² - 9(y-2)² = -36`:
**(a)** Qual é a cônica após correção do sinal?  
**(b)** Equação reduzida correta.

**Formato de resposta:** `(a) hipérbole/elipse (b) (y-k)²/... - (x-h)²/... = 1`.

---

### `F06-E03` *(Classificação geral por A e C)*
`4x² + 9y² - 16x + 18y - 11 = 0`:
Que cônica é esta (sem `xy`)?

**Formato de resposta:** `circunferencia/elipse/hiperbole/parabola`.

---

### `F06-E04` *(Hipérbole transladada, eixo vertical)*
`(y-4)²/25 - (x+1)²/16 = 1`:
**(a)** Centro.  
**(b)** Focos.

**Formato de resposta:** `(a) (h, k) (b) (h, k+-c)`.

---

### `F06-E05` *(Reconhecimento com completamento de quadrados)*
`x² - 4y² - 2x + 16y - 11 = 0`:
**(a)** Complete os quadrados e escreva a equação reduzida.  
**(b)** Identifique a cônica.

**Formato de resposta:** `(a) equacao_reduzida (b) nome_da_conica`.

---

## 4. Checagem Independente (`F06-C01` a `F06-C03`)

### `F06-C01` *(Classificação geral)*
`x² - y² + 4x - 6y + 5 = 0`:
Que cônica é?

**Formato de resposta:** `circunferencia/elipse/hiperbole/parabola`.

---

### `F06-C02` *(Hipérbole transladada com armadilha)*
`9(x+2)² - 4(y-3)² = -36`:
Equação reduzida correta.

**Formato de resposta:** `(y-k)²/... - (x-h)²/... = 1`.

---

### `F06-C03` *(Focos de hipérbole transladada)*
`(x-5)²/9 - (y+2)²/16 = 1`:
Focos.

**Formato de resposta:** `(h+-c, k)` com valores.

---

## 5. Critério de Domínio e Recuperação

- **Avançar para `F07`:** somente após autocorreção de `F06-E01`–`F06-E05` e **100% (3/3)** na Checagem Independente `F06-C01`–`F06-C03` sem consulta.
- **Recuperação direcionada (1ª falha):**
  - Se errou o sinal → sempre verifique o lado direito antes de dividir.
  - Se errou a classificação → confira os sinais de `A` e `C`.
- **Após 2 tentativas malsucedidas:** interrompa e revise `F05`/`F04` com o orientador.

---

## 6. Referências do Orientador
- `[DOC]` `P3` p. 181–184; `L11` Ex. 13–15.
- `[DOC]` `Matrizes_Vetores_P3.pdf` p. 181–184 (Cap. 7: Hipérbole transladada, reconhecimento de cônicas).
- Gabarito e casos: [F06_gabarito.md](../gabaritos/F06_gabarito.md) e [casos_F06.json](../testes/casos_F06.json).
