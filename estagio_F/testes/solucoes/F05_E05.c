#include <stdio.h>

void extremos_tres(int a, int b, int c, int *menor, int *maior);

int main(void) {
    int a, b, c, menor, maior;
    scanf("%d %d %d", &a, &b, &c);
    extremos_tres(a, b, c, &menor, &maior);
    printf("Menor: %d\nMaior: %d\n", menor, maior);
    return 0;
}

void extremos_tres(int a, int b, int c, int *menor, int *maior) {
    *menor = a;
    *maior = a;
    if (b < *menor) {
        *menor = b;
    }
    if (c < *menor) {
        *menor = c;
    }
    if (b > *maior) {
        *maior = b;
    }
    if (c > *maior) {
        *maior = c;
    }
}
