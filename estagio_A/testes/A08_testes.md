# Rubrica e Gabarito Verificável — Bloco `A08`

- **Natureza do bloco:** 100% exercícios no papel e rastreio manual (bits, bytes, sistema binário e $2^n$ / $\lceil \log_2 T \rceil$). **Não há código C nem arquivo JSON neste bloco.**
- **Status de verificação no ambiente atual (`19/11/2026`):**
  - **Executado:** conferência aritmética independente em Python sobre todas as conversões binário ↔ decimal, potências $2^n$ e funções teto $\lceil \log_2 T \rceil$ de [A08_bloco.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/blocos/A08_bloco.md) e [A08_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/gabaritos/A08_gabarito.md).
  - **Pendente:** não aplicável para GCC (`A08` não possui programas em C).

---

## Rubrica de Correção e Chaves Verificáveis

### Exercícios (`A08-E01` a `A08-E06`)
| Item | Critério de Acerto Integral (100% no item) | Resposta Verificada |
|---|---|---|
| **`A08-E01`** | Monta pesos corretos $2^k$ da direita para a esquerda e acerta as 3 somas. | (a) `9` (`1001_2`); (b) `29` (`11101_2`); (c) `65` (`01000001_2`). |
| **`A08-E02`** | Preenche todas as lacunas sem erro de expoente ou de limite (`2^n - 1`). | (a) `2`, `1`, `10011`; (b) `8`, `8`, `256`, `255`; (c) `8`, `16`, `4`. |
| **`A08-E03`** | Identifica os dois erros (inclusão do 0 dentro dos 256 / teto vs piso; posições $2^3$ e $2^1$ em `1010_2`). | (1) `9` bits ($2^8=256 < 300 \le 512$); (2) `10` (`8 + 2`). |
| **`A08-E04`** | Calcula $2^n$ e converte bytes em bits ($1\text{ byte} = 8\text{ bits}$). | (a) `32` valores, maior `31`; (b) `65536`; (c) `32` bits, $2^{32} = 4294967296 \approx 4{,}3 \times 10^9$. |
| **`A08-E05`** | Encontra menor $n$ com $2^n \ge T$, incluindo potência exata (`64`). | (a) `3` bits; (b) `6` bits; (c) `20` bits ($2^{19}=524288 < 10^6 \le 2^{20}=1048576$). |
| **`A08-E06`** | Converte corretamente nos dois sentidos e associa 4 bits ao dígito hexadecimal. | (a) `54`; (b) `1001011_2`; (c) `1011_2` = `B_16`. |

### Checagem Independente (`A08-C01` a `A08-C04` — Exige 4/4)
| Item | Habilidade Avaliada | Critério de Correção e Valor Exato |
|---|---|---|
| **`A08-C01`** | Binário → Decimal | Mostra $64 + 16 + 8 + 2 + 1 = \mathbf{91_{10}}$ para `1011011_2`. |
| **`A08-C02`** | Decimal → Binário | Mostra divisões por 2 ou potências ($64+32+8+2$) chegando a **`1101010_2`** para `106_10`. |
| **`A08-C03`** | Capacidade direta $2^n$ | (1) `10` bits = **`1024`** valores; (2) `7` bits = intervalo **`[0, 127]`** (`128` valores). |
| **`A08-C04`** | Problema inverso $\lceil \log_2 T \rceil$ | (1) `500` → **`9` bits** ($256 < 500 \le 512$); (2) `16` → **`4` bits** ($2^4 = 16$). |
