#include <stdio.h>

int main(void) {
    int opcao;

    do {
        if (scanf("%d", &opcao) != 1) {
            break;
        }

        switch (opcao) {
            case 1: {
                long long a, b;
                if (scanf("%lld %lld", &a, &b) != 2) {
                    return 1;
                }
                if (a <= 0 || b <= 0) {
                    printf("Entrada Invalida\n");
                } else {
                    while (b != 0) {
                        long long resto = a % b;
                        a = b;
                        b = resto;
                    }
                    printf("MDC = %lld\n", a);
                }
                break;
            }
            case 2: {
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
                break;
            }
            case 0:
                printf("Encerrando\n");
                break;
            default:
                printf("Opcao Invalida\n");
                break;
        }
    } while (opcao != 0);

    return 0;
}
