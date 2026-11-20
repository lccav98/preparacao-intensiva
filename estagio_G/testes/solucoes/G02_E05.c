#include <stdio.h>

void contar_regressivo(int n);
void contar_progressivo(int n);

int main(void) {
    int n;
    scanf("%d", &n);

    printf("Regressivo:");
    if (n > 0) {
        printf(" ");
        contar_regressivo(n);
    }
    printf("\n");

    printf("Progressivo:");
    if (n > 0) {
        printf(" ");
        contar_progressivo(n);
    }
    printf("\n");
    return 0;
}

void contar_regressivo(int n) {
    if (n <= 0) {
        return;
    }
    printf("%d", n);
    if (n > 1) {
        printf(" ");
    }
    contar_regressivo(n - 1);
}

void contar_progressivo(int n) {
    if (n <= 0) {
        return;
    }
    contar_progressivo(n - 1);
    if (n > 1) {
        printf(" ");
    }
    printf("%d", n);
}
