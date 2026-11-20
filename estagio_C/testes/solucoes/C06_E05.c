#include <stdio.h>

int main(void) {
    long long n;
    if (scanf("%lld", &n) != 1 || n <= 0) {
        printf("Entrada Invalida\n");
        return 0;
    }

    long long atual = n;
    int passos = 0;

    printf("%lld", atual);
    while (atual != 1 && passos < 200) {
        if (atual % 2 == 0) {
            atual = atual / 2;
        } else {
            atual = 3 * atual + 1;
        }
        passos++;
        printf(" %lld", atual);
    }
    printf("\n");
    printf("Passos: %d\n", passos);

    return 0;
}
