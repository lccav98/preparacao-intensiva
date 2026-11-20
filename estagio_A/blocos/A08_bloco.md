# Bloco `A08` — Bits, Bytes, Sistema Binário e Capacidade de Representação

| Campo | Especificação |
|---|---|
| **Estágio / Bloco** | Estágio A — Fundamentos, Ambiente C, Variáveis e Representação / **`A08`** |
| **Micro-habilidade foco** | Converter inteiros não negativos entre base 10 e base 2 e calcular capacidade de representação ($T(n)=2^n$) e quantidade mínima de bits ($n=\lceil \log_2 T \rceil$). |
| **Pré-requisitos** | `A04` *(Identificadores, palavras reservadas e tipos básicos)*. *(Pré-requisito matemático `[INF]`: potências inteiras de 2 de $2^0$ a $2^{16}$ e definição operacional de $\lceil \log_2 T \rceil$ como menor $n$ tal que $2^n \ge T$.)* |
| **Tempo estimado** *(sujeito à calibração)* | **1 sessão de prática (22 min) + checagem (14 min)** — **Sessão (`E01`–`E06`, 22 min):** `13 min` resol. \| `5 min` corr. \| `4 min` recup.; **Checagem (`C01`–`C04`, 14 min):** `10 min` resol. \| `4 min` conf. |
| **Restrição de escopo** | **100% papel e rastreio manual.** **Zero código C** neste bloco; **não utilize** compilador, operadores bit a bit (`&`, `\|`, `^`, `<<`, `>>`), complemento de 2 (negativos) ou ponto flutuante (tópicos de `A09`). |

### Registro da Sessão (Preenchido na Prática)
- **Sessão (`E01`–`E06`) — Data:** `____/____/______` | **Aluno:** `____________________` | **Variante:** `[ ] V1  [ ] V2` | **Tentativa:** `___` | **Tempo:** `___ min` | **1ª tent.:** `___ / 6` | **Após corr.:** `___ / 6`
- **Checagem Independente (`C01`–`C04`, sem gabarito):** `___ / 4` \| **Tempo:** `___ min` (`[ ] Aprovado (100%)  [ ] Recuperação`)

---

## 1. Instruções Curtas

1. **Bit e Byte (`Aula_04` p. 4):**
   - **Bit** (*binary digit*): menor unidade de informação; assume apenas `0` ou `1`.
   - **Byte:** grupo de **8 bits** (`1 byte = 8 bits`), unidade básica de endereçamento da memória.
2. **Capacidade direta ($T(n) = 2^n$):** Com $n$ bits, existem exatamente **$2^n$ padrões distintos** (por exemplo, os inteiros não negativos de $0$ até $2^n - 1$). Tabela de referência essencial ($2^0$ a $2^{16}$, mais $2^{20}$):
   - $2^0 = 1$, $2^1 = 2$, $2^2 = 4$, $2^3 = 8$, $2^4 = 16$, $2^5 = 32$, $2^6 = 64$, $2^7 = 128$, $2^8 = 256$
   - $2^9 = 512$, $2^{10} = 1024$, $2^{11} = 2048$, $2^{12} = 4096$, $2^{16} = 65\,536$, $2^{20} = 1\,048\,576$
3. **Problema inverso ($n = \lceil \log_2 T \rceil$):** Para representar **$T$ valores distintos**, encontre o **menor inteiro $n$** tal que **$2^n \ge T$** (`Aula_04` p. 7). Se $T$ não for potência exata de 2, sempre escolha a **próxima potência maior ou igual** (nunca arredonde para baixo!).
4. **Sistema binário posicional (`Aula_04` p. 9):** Da direita para a esquerda, cada posição $k$ ($k = 0, 1, 2, \dots$) tem peso $2^k$. Para converter **binário → decimal**, some os pesos $2^k$ das posições que contêm bit `1`.
5. **Decimal → Binário e menção ao Hexadecimal (`Aula_04` p. 8):** Para converter inteiro não negativo da base 10 para a base 2, divida sucessivamente por $2$ lendo os restos **do último para o primeiro** (ou subtraia a maior potência de 2 $\le N$). O sistema **hexadecimal** (base 16: dígitos `0–9` e `A=10..F=15`) representa exatamente **4 bits** por dígito (ex.: $13_{10} = 1101_2 = D_{16}$).

---

## 2. Exemplos Guiados *(100% no papel — sem código C)*

### Exemplo 1 — Capacidade ($2^n$) e mínimo de bits ($\lceil \log_2 T \rceil$) *(Exemplo resolvido no papel)*
- **(a) Quantos valores distintos cabem em `6 bits` e em `1 byte`?**
  - `6 bits`: $T(6) = 2^6 = \mathbf{64}$ valores distintos (de `0` a `63`).
  - `1 byte` = `8 bits`: $T(8) = 2^8 = \mathbf{256}$ valores distintos (de `0` a `255`).
- **(b) Quantos bits mínimos são necessários para representar `1000` valores distintos? (`Aula_04` p. 20)**
  - Testamos potências de 2 próximas: $2^9 = 512$ (insuficiente, $512 < 1000$) e $2^{10} = 1024$ (suficiente, $1024 \ge 1000$).
  - Portanto, $n = \lceil \log_2 1000 \rceil = \mathbf{10\text{ bits}}$.

### Exemplo 2 — Conversão Binário ↔ Decimal e relação com Hexadecimal *(Exemplo resolvido no papel)*
- **(a) Converter `10110_2` para base 10:**

| Bit | `1` | `0` | `1` | `1` | `0` |
|---|---|---|---|---|---|
| Posição ($2^k$) | $2^4$ | $2^3$ | $2^2$ | $2^1$ | $2^0$ |
| Peso | `16` | `8` | `4` | `2` | `1` |
| Contribuição | `16` | `0` | `4` | `2` | `0` |

  Soma: $16 + 0 + 4 + 2 + 0 = \mathbf{22_{10}}$.

- **(b) Converter `45_10` para base 2 (divisões sucessivas por 2):**
  - $45 \div 2 = 22$ (resto **`1`** — bit menos significativo)
  - $22 \div 2 = 11$ (resto **`0`**)
  - $11 \div 2 = 5$ (resto **`1`**)
  - $5 \div 2 = 2$ (resto **`1`**)
  - $2 \div 2 = 1$ (resto **`0`**)
  - $1 \div 2 = 0$ (resto **`1`** — bit mais significativo)
  - Lendo os restos de baixo para cima: $\mathbf{101101_2}$. Conferência: $32 + 8 + 4 + 1 = 45$.

---

## 3. Exercícios (`A08-E01` a `A08-E06` — Papel)

### `A08-E01` *(Conversão posicional guiada — Reprodução do modelo)*
Monte a tabela posicional (`Bit | Posição 2^k | Peso | Contribuição`) e converta para a base decimal:
- **(a)** `1001_2`
- **(b)** `11101_2`
- **(c)** `01000001_2` *(código ASCII de `'A'`, `Aula_04` p. 4)*

---

### `A08-E02` *(Completar lacunas no papel)*
Complete as lacunas abaixo:
- **(a)** $19_{10} = 16 + \text{\_\_\_} + \text{\_\_\_} = \text{\_\_\_\_\_\_\_\_}_2$
- **(b)** `1 byte = ___ bits`, o que permite representar $2^{\text{\_\_\_}} = \text{\_\_\_}$ valores distintos (inteiros não negativos de `0` até `___`).
- **(c)** Para representar `12` estados distintos, como $2^3 = \text{\_\_\_} < 12 \le 2^4 = \text{\_\_\_}$, o mínimo necessário é `___` bits.

---

### `A08-E03` *(Caça ao Erro Conceitual — Sem compilador)*
Analise as duas afirmações abaixo, identifique **todos os erros** e apresente as respostas corretas:
1. *"Para codificar `300` produtos distintos, `8 bits` bastam porque $2^8 = 256$ e o zero acrescenta mais possibilidades; além disso, $\log_2 300 \approx 8{,}23$ arredonda para `8`."*
2. *"O binário `1010_2` vale `12_10`, pois os dois bits `1` valem $2^3$ e $2^2$ ($8 + 4 = 12$)."*

---

### `A08-E04` *(Variação controlada com pistas — Capacidade $2^n$ e bytes)*
Calcule passo a passo:
- **(a)** Quantos valores distintos podem ser representados com `5 bits`? E qual é o maior inteiro não negativo representável?
- **(b)** Quantos valores distintos cabem em **`2 bytes`** (`16 bits`, `Aula_04` p. 5 e 20)?
- **(c)** Quantos bits correspondem a **`4 bytes`** e qual a potência de 2 que expressa sua capacidade total?
*Pista:* Multiplique bytes por `8` para achar `n` bits e aplique $2^n$ (em `4 bytes`, indique a potência exata e a ordem aproximada $\approx 4{,}3 \times 10^9$).

---

### `A08-E05` *(Variação controlada com pistas — Problema inverso $\lceil \log_2 T \rceil$)*
Determine a quantidade mínima de bits necessária para representar exatamente:
- **(a)** `7` dias da semana;
- **(b)** `64` posições em uma tabela;
- **(c)** `1 000 000` (1 milhão) de valores distintos (`Aula_04` p. 20).
*Pista:* Em (c), lembre que $2^{10} = 1024$ e $2^{20} = (2^{10})^2 = 1024 \times 1024$.

---

### `A08-E06` *(Resolução independente — Conversões e hexadecimal)*
Sem usar calculadora:
- **(a)** Converta `110110_2` para base 10.
- **(b)** Converta `75_10` para base 2 (mostrando divisões por 2 ou decomposição em potências de 2).
- **(c)** Qual é o binário de 4 bits correspondente a `11_10` e qual seu dígito na base hexadecimal (base 16)?

---

## 4. Checagem Independente de Domínio *(Sem Consulta ao Gabarito — Exige 100%)*

### `A08-C01` *(Conversão Binário → Decimal)*
Converta `1011011_2` para a base 10 mostrando cada potência de 2 somada.

### `A08-C02` *(Conversão Decimal → Binário)*
Converta `106_10` para a base 2 apresentando o desenvolvimento completo.

### `A08-C03` *(Capacidade Direta $2^n$)*
1. Quantos valores distintos podem ser representados com `10 bits`?
2. Qual é o intervalo de inteiros não negativos representáveis com `7 bits`?

### `A08-C04` *(Problema Inverso $\lceil \log_2 T \rceil$)*
1. Qual o número mínimo de bits necessários para representar `500` valores distintos?
2. Qual o número mínimo de bits necessários para representar `16` valores distintos?

---

## 5. Orientação de Avanço ou Recuperação

- **Avançar para `A09` (`Tamanhos de Tipos, sizeof e Precisão float vs double`):** somente após autocorreção de `A08-E01`..`E06` **e** **100% (4/4)** na Checagem Independente `A08-C01`..`C04` sem consulta ao gabarito.
- **Recuperação direcionada (1ª falha):** reescrever a tabela de potências de 2 ($2^0..2^{10}$), repetir 2 conversões guiadas com pesos explícitos em cima de cada dígito e aplicar variante `V2` de `A08`.
- **Regra das 2 tentativas malsucedidas:** após **2 reprovações** neste bloco, parar repetições e revisar o pré-requisito matemático de potências de 2 ($2^0$ a $2^{16}$) e a noção básica de representação de dados em `A04`.

---

## 6. Referências do Orientador
- `[DOC]` `ementa_algoritmos.pdf` p. 2 (item 3 — Precisão numérica: bits e bytes; capacidade de representação e quantificação de bits).
- `[DOC]` `Planejamento_de_Aula_Algoritmos.pdf` p. 1 (31/08 — Representação de dados e precisão numérica).
- `[DOC]` `Aula_04_Algoritmos.pdf` p. 4–9 (bit, byte, $T(n)=2^n$, $n=\lceil \log_2 T\rceil$, bases decimal/binária/hexadecimal) e p. 19–20 (resumo e exercícios propostos).
- `[INF]` Pré-requisito matemático explícito: tabela de potências inteiras de 2 ($2^0$ a $2^{16}$) e função teto $\lceil \log_2 T \rceil$.
- Gabarito e rubrica verificável: [A08_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/gabaritos/A08_gabarito.md) e [A08_testes.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/A08_testes.md).
