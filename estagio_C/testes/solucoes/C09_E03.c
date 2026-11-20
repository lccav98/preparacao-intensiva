#include <stdio.h>

int main(void) {
    int linhas, cols;
    if (scanf("%d %d", &linhas, &cols) != 2) {
        return 1;
    }

    if (linhas <= 0 || cols <= 0) {
        printf("Entrada Invalida\n");
        return 0;
    }

    for (int i = 1; i <= linhas; i++) {
        for (int j = 1; j <= cols; j++) {
            printf("%4d", i * j);
        }
        printf("\n");
    }

    return 0;
}
