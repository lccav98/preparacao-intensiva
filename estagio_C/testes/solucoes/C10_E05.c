#include <stdio.h>

int main(void) {
    long long num;
    int qtd = 0;
    int qtd_primos = 0;
    long long soma = 0;
    long long maior = 0;

    while (1) {
        if (scanf("%lld", &num) != 1 || num == 0) {
            break;
        }

        qtd++;
        soma += num;
        if (qtd == 1 || num > maior) {
            maior = num;
        }

        int primo = 1;
        if (num <= 1) {
            primo = 0;
        } else if (num == 2) {
            primo = 1;
        } else if (num % 2 == 0) {
            primo = 0;
        } else {
            for (long long d = 3; d * d <= num; d += 2) {
                if (num % d == 0) {
                    primo = 0;
                    break;
                }
            }
        }

        if (primo) {
            qtd_primos++;
        }
    }

    if (qtd == 0) {
        printf("Nenhum numero valido\n");
    } else {
        printf("Qtd: %d\n", qtd);
        printf("Primos: %d\n", qtd_primos);
        printf("Maior: %lld\n", maior);
        printf("Media: %.2f\n", (double)soma / qtd);
    }

    return 0;
}
