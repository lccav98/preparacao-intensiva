#include <stdio.h>

int main(void) {
    int nota;

    if (scanf("%d", &nota) != 1) {
        return 1;
    }

    if (nota < 0 || nota > 100) {
        printf("Nota Invalida\n");
    } else {
        switch (nota / 10) {
            case 10:
            case 9:
                printf("Conceito A\n");
                break;
            case 8:
                printf("Conceito B\n");
                break;
            case 7:
                printf("Conceito C\n");
                break;
            case 6:
                printf("Conceito D\n");
                break;
            default:
                printf("Conceito F\n");
                break;
        }
    }

    return 0;
}
