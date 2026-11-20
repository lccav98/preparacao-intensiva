#include <stdio.h>

int main(void) {
    int nota;

    do {
        scanf("%d", &nota);
        if (nota < 0 || nota > 10) {
            printf("Nota invalida\n");
        }
    } while (nota < 0 || nota > 10);

    printf("Nota registrada: %d\n", nota);
    return 0;
}
