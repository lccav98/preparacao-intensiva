#include <stdio.h>

int main(void) {
    long long n;
    if (scanf("%lld", &n) != 1) {
        return 1;
    }

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
        printf("Primo\n");
    } else {
        printf("Nao Primo\n");
    }

    return 0;
}
