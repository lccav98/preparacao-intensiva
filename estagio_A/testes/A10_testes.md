# Especificação de Testes — Bloco `A10`

- **Ambiente alvo:** Linux (`x86-64`), compilador GCC, padrão **C99**.
- **Comando de compilação padrão:**
  ```bash
  gcc -std=c99 -Wall -Wextra solucoes/<arquivo>.c -o programa
  ```
- **Restrições verificadas nos arquivos `.c`:** uso exclusivo de `#include <stdio.h>`, `int main(void)`, `return 0;`, `#define`, `const`, `scanf`/`printf`, atribuição/troca `aux` e operações `+`, `-`, `*` em `double`; **ausência** de `/`, `%`, `if`, `switch`, laços, vetores, funções auxiliares e `<math.h>`.
- **Critério de comparação e tolerância:**
  - Comparação textual exata linha a linha após normalização `\r\n` → `\n`.
  - Valores formatados com `%.2f`: entradas escolhidas para evitar empates de arredondamento `.xx5`; tolerância numérica de **`1e-2`**.
- **Status de execução no ambiente atual (`19/11/2026`):**
  - **Executado:** verificação estática C99 + checagem de não-antecipação + sincronia literal com [A10_gabarito.md](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/gabaritos/A10_gabarito.md) + **oráculo matemático em Python** (conferindo ausência de empates `.xx5` e igualdade IEEE-754 × decimal exato) sobre todos os **22 casos** de [casos_A10.json](file:///C:/Users/d7opa/Documents/Algoritmos/Curso_Preparacao_Intensiva_Algoritmos/estagio_A/testes/casos_A10.json).
  - **Pendente:** compilação e execução binária em GCC (`gcc` ausente no ambiente local).

---

## Casos de Teste por Programa (mínimo 4 casos por arquivo: normais, `0.0` e bordas)

### 1. `A10_E03_corrigido.c` (Salário base + `#define BONUS 50.0`)
- `A10-E03-T1` (normal): `1200.00\n` → `Total: R$ 1250.00`
- `A10-E03-T2` (borda zero): `0.0\n` → `Total: R$ 50.00`
- `A10-E03-T3` (centavos): `2345.67\n` → `Total: R$ 2395.67`
- `A10-E03-T4` (borda saldo negativo zerando): `-50.0\n` → `Total: R$ 0.00`

### 2. `A10_E04.c` (Área e perímetro de terreno com `const double FATOR_PERIMETRO = 2.0`)
- `A10-E04-T1` (normal): `10.0 25.0\n` → `Area: 250.00 m2` / `Perimetro: 70.00 m`
- `A10-E04-T2` (borda uma dimensão zero): `0.0 15.0\n` → `Area: 0.00 m2` / `Perimetro: 30.00 m`
- `A10-E04-T3` (borda duplo zero): `0.0 0.0\n` → `Area: 0.00 m2` / `Perimetro: 0.00 m`
- `A10-E04-T4` (decimais exatos): `12.5 8.2\n` → `Area: 102.50 m2` / `Perimetro: 41.40 m`
- `A10-E04-T5` (sub-unitário): `0.4 0.6\n` → `Area: 0.24 m2` / `Perimetro: 2.00 m`

### 3. `A10_E05.c` (Salário fixo + comissão 5% e troca com `aux`)
- `A10-E05-T1` (normal): `2000.00 5000.00\n1800.00 4000.00\n` → `Comissao 1: R$ 250.00` / `Comissao 2: R$ 200.00` / `Total 1: R$ 2000.00` / `Total 2: R$ 2250.00`
- `A10-E05-T2` (vendas zero): `1500.00 0.0\n2200.00 0.0\n` → `Comissao 1: R$ 0.00` / `Comissao 2: R$ 0.00` / `Total 1: R$ 2200.00` / `Total 2: R$ 1500.00`
- `A10-E05-T3` (tudo zero): `0.0 0.0\n0.0 0.0\n` → todos `R$ 0.00`
- `A10-E05-T4` (centavos distintos): `1200.40 3000.00\n1500.60 2400.00\n` → `Comissao 1: R$ 150.00` / `Comissao 2: R$ 120.00` / `Total 1: R$ 1620.60` / `Total 2: R$ 1350.40`
- `A10-E05-T5` (valores iguais): `1000.00 1240.00\n1000.00 1240.00\n` → `Comissao 1: R$ 62.00` / `Comissao 2: R$ 62.00` / `Total 1: R$ 1062.00` / `Total 2: R$ 1062.00`

### 4. `A10_C02_corrigido.c` (Acréscimo 10% + aspas/percentual escapados)
- `A10-C02-T1` (normal): `200.00\n` → `Taxa aplicada: "10%"` / `Valor final: R$ 220.00`
- `A10-C02-T2` (borda zero): `0.0\n` → `Taxa aplicada: "10%"` / `Valor final: R$ 0.00`
- `A10-C02-T3` (decimal sem empate): `154.20\n` → `Taxa aplicada: "10%"` / `Valor final: R$ 169.62`
- `A10-C02-T4` (valor pequeno): `12.00\n` → `Taxa aplicada: "10%"` / `Valor final: R$ 13.20`

### 5. `A10_C03.c` (Dimensões trocadas, área e comissão 5%)
- `A10-C03-T1` (normal): `10.0 20.0 500.00\n` → `Dimensoes trocadas: 20.00 x 10.00` / `Area: 200.00 m2` / `Comissao: R$ 5000.00`
- `A10-C03-T2` (preço zero): `15.0 30.0 0.0\n` → `Dimensoes trocadas: 30.00 x 15.00` / `Area: 450.00 m2` / `Comissao: R$ 0.00`
- `A10-C03-T3` (tudo zero): `0.0 0.0 0.0\n` → `Dimensoes trocadas: 0.00 x 0.00` / `Area: 0.00 m2` / `Comissao: R$ 0.00`
- `A10-C03-T4` (decimal exato): `12.0 15.0 250.40\n` → `Dimensoes trocadas: 15.00 x 12.00` / `Area: 180.00 m2` / `Comissao: R$ 2253.60`
