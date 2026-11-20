#include <stdio.h>

int main(void) {
    long long a, b;
    if (scanf("%lld %lld", &a, &b) != 2) {
        return 1;
    }

    if (b < a) {
        printf("Intervalo Invalido\n");
        return 0;
    }

    int qtd_primos = 0;
    long long soma_primos = 0;

    for (long long n = a; n <= b; n++) {
        int primo = 1;
        if (n <= 1) {
            primo = 0;
        } else if (n == 2) {
            primo = 1;
        } else if (n % 2 == 0) {
            primo = 0;
        } else {
            for (long long d = 3; d * d <= n; d += 2) {
                if (n % d == 0) {
                    primo = 0;
                    break;
                }
            }
        }

        if (primo) {
            qtd_primos++;
            soma_primos += n;
        }
    }

    printf("Qtd Primos: %d\n", qtd_primos);
    printf("Soma Primos: %lld\n", soma_primos);
    return 0;
}
