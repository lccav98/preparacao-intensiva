#include <stdio.h>

int main(void) {
    int n;
    if (scanf("%d", &n) != 1) {
        return 1;
    }

    if (n <= 0) {
        printf("Entrada Invalida\n");
        return 0;
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%3d", j);
        }
        printf("\n");
    }

    return 0;
}
