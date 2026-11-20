#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    if (n % 2 == 0) {
        printf("O numero %d eh par\n", n);
    }

    printf("Fim do programa\n");
    return 0;
}
