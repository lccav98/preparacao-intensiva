#include <stdio.h>

int main(void) {
    int idade;

    if (scanf("%d", &idade) != 1) {
        return 1;
    }

    if (idade < 0 || idade > 120) {
        printf("Idade Invalida\n");
    } else {
        switch (idade / 10) {
            case 0:
                printf("Crianca\n");
                break;
            case 1:
                printf("Jovem\n");
                break;
            case 2:
            case 3:
            case 4:
            case 5:
                printf("Adulto\n");
                break;
            default:
                printf("Idoso\n");
                break;
        }
    }

    return 0;
}
