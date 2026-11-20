#include <stdio.h>

int main(void) {
    int k;
    if (scanf("%d", &k) != 1 || k <= 0) {
        return 1;
    }

    int total_primos = 0;

    for (int i = 0; i < k; i++) {
        long long num;
        if (scanf("%lld", &num) != 1) {
            return 1;
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
            printf("Numero %lld: Primo\n", num);
            total_primos++;
        } else {
            printf("Numero %lld: Nao Primo\n", num);
        }
    }

    printf("Resumo: %d primos de %d numeros\n", total_primos, k);
    return 0;
}
