# Gabarito Comentado — Bloco `A08` (Bits, Bytes, Sistema Binário e Capacidade)

> **Bloco de referência:** [A08_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/blocos/A08_bloco.md)  
> **Natureza do bloco:** 100% exercícios no papel e rastreio manual (sem arquivos `.c`).

---

## 1. Gabarito dos Exercícios (`A08-E01` a `A08-E06`)

### `A08-E01` *(Conversão posicional guiada)*
- **(a) `1001_2`:** $1 \cdot 2^3 + 0 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0 = 8 + 0 + 0 + 1 = \mathbf{9_{10}}$
- **(b) `11101_2`:** $1 \cdot 2^4 + 1 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0 = 16 + 8 + 4 + 0 + 1 = \mathbf{29_{10}}$
- **(c) `01000001_2`:** $0 \cdot 2^7 + 1 \cdot 2^6 + 0 \cdot 2^5 + 0 \cdot 2^4 + 0 \cdot 2^3 + 0 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0 = 64 + 1 = \mathbf{65_{10}}$ *(código ASCII de `'A'`)*

### `A08-E02` *(Completar lacunas)*
- **(a)** $19_{10} = 16 + \mathbf{2} + \mathbf{1} = \mathbf{10011}_2$
- **(b)** `1 byte =` **`8`** `bits`, representando $2^{\mathbf{8}} = \mathbf{256}$ valores distintos (inteiros não negativos de `0` até **`255`**).
- **(c)** $2^3 = \mathbf{8} < 12 \le 2^4 = \mathbf{16}$, logo o mínimo necessário é **`4`** bits.

### `A08-E03` *(Caça ao Erro Conceitual)*
1. **Erros na afirmação 1:**
   - $2^8 = 256$ já contabiliza **todos** os padrões possíveis (incluindo o zero, ou seja, de `0` a `255` = `256` valores, **não** `257`).
   - Em $\lceil \log_2 T \rceil$ arredonda-se **para cima** (função teto), nunca para baixo; `8` bits não comportam `300` valores porque $2^8 = 256 < 300$.
   - **Resposta correta:** $2^8 = 256 < 300 \le 512 = 2^9 \implies$ são necessários pelo menos **`9` bits**.
2. **Erros na afirmação 2:**
   - As posições da direita para a esquerda são $2^3, 2^2, 2^1, 2^0$. Em `1010_2`, os bits `1` estão nas posições $2^3$ e $2^1$ (e **não** $2^2$).
   - **Resposta correta:** $1010_2 = 1 \cdot 8 + 0 \cdot 4 + 1 \cdot 2 + 0 \cdot 1 = \mathbf{10_{10}}$.

### `A08-E04` *(Capacidade $2^n$ e bytes)*
- **(a)** `5 bits`: $T(5) = 2^5 = \mathbf{32}$ valores distintos; maior inteiro não negativo = $32 - 1 = \mathbf{31}$ (`0` a `31`).
- **(b)** `2 bytes` = $2 \times 8 = 16$ bits: $T(16) = 2^{16} = \mathbf{65\,536}$ valores distintos.
- **(c)** `4 bytes` = $4 \times 8 = \mathbf{32\text{ bits}}$; capacidade = $\mathbf{2^{32}} = 4\,294\,967\,296 \approx \mathbf{4{,}3 \times 10^9}$ valores distintos.

### `A08-E05` *(Problema inverso $\lceil \log_2 T \rceil$)*
- **(a)** `7` valores: $2^2 = 4 < 7 \le 8 = 2^3 \implies \mathbf{3\text{ bits}}$.
- **(b)** `64` valores: $2^6 = 64 \ge 64 \implies \mathbf{6\text{ bits}}$ *(potência exata de 2)*.
- **(c)** `1 000 000` valores: $2^{19} = 524\,288 < 1\,000\,000 \le 1\,048\,576 = 2^{20} \implies \mathbf{20\text{ bits}}$.

### `A08-E06` *(Conversões e hexadecimal)*
- **(a)** `110110_2` = $1 \cdot 32 + 1 \cdot 16 + 0 \cdot 8 + 1 \cdot 4 + 1 \cdot 2 + 0 \cdot 1 = \mathbf{54_{10}}$.
- **(b)** `75_10`: $75 = 64 + 8 + 2 + 1$ (divisões por 2: restos $1, 1, 0, 1, 0, 0, 1$ de baixo para cima) = **`1001011_2`**.
- **(c)** `11_10` = $8 + 2 + 1 = \mathbf{1011_2} = \mathbf{B_{16}}$ (pois `A=10`, `B=11`).

---

## 2. Gabarito da Checagem Independente (`A08-C01` a `A08-C04`)

### `A08-C01` *(Binário → Decimal)*
- **`1011011_2`:** $1\cdot 2^6 + 0\cdot 2^5 + 1\cdot 2^4 + 1\cdot 2^3 + 0\cdot 2^2 + 1\cdot 2^1 + 1\cdot 2^0 = 64 + 0 + 16 + 8 + 0 + 2 + 1 = \mathbf{91_{10}}$.

### `A08-C02` *(Decimal → Binário)*
- **`106_10`:**
  - $106 \div 2 = 53$ (r `0`)
  - $53 \div 2 = 26$ (r `1`)
  - $26 \div 2 = 13$ (r `0`)
  - $13 \div 2 = 6$ (r `1`)
  - $6 \div 2 = 3$ (r `0`)
  - $3 \div 2 = 1$ (r `1`)
  - $1 \div 2 = 0$ (r `1`)
  - Resultado: **`1101010_2`** (conferência: $64 + 32 + 8 + 2 = 106$).

### `A08-C03` *(Capacidade Direta $2^n$)*
1. **`10 bits`:** $2^{10} = \mathbf{1024}$ valores distintos.
2. **`7 bits`:** $2^7 = 128$ valores distintos, no intervalo **`[0, 127]`** (`0` até `127`).

### `A08-C04` *(Problema Inverso $\lceil \log_2 T \rceil$)*
1. **`500` valores:** $2^8 = 256 < 500 \le 512 = 2^9 \implies \mathbf{9\text{ bits}}$.
2. **`16` valores:** $2^4 = 16 \implies \mathbf{4\text{ bits}}$.
