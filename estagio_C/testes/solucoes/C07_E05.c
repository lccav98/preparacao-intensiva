#include <stdio.h>

int main(void) {
    long long num;
    int total_primos = 0;

    while (1) {
        if (scanf("%lld", &num) != 1 || num == 0) {
            break;
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
            total_primos++;
        }
    }

    printf("Total Primos: %d\n", total_primos);
    return 0;
}
