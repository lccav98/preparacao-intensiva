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

    int num = 1;
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%3d", num++);
        }
        printf("\n");
    }

    return 0;
}
