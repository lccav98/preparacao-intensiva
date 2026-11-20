#include <stdio.h>

int main(void) {
    int n1, n2, n3;
    double media;
    scanf("%d %d %d", &n1, &n2, &n3);

    media = (double)(n1 * 2 + n2 * 3 + n3 * 5) / 10.0;

    printf("Media: %.2f\n", media);
    return 0;
}
