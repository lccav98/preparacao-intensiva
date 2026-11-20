#include <stdio.h>

int main(void) {
    int n, achou = 0;
    scanf("%d", &n);

    if (n % 2 == 0) {
        printf("Divisivel por 2\n");
        achou = 1;
    }
    if (n % 3 == 0) {
        printf("Divisivel por 3\n");
        achou = 1;
    }
    if (n % 5 == 0) {
        printf("Divisivel por 5\n");
        achou = 1;
    }
    if (achou == 0) {
        printf("Nenhum divisor encontrado\n");
    }

    return 0;
}
