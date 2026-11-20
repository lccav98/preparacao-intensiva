#include <stdio.h>

int main(void) {
    int idade;
    if (scanf("%d", &idade) != 1) {
        return 1;
    }

    if (idade >= 18 && idade <= 35) {
        printf("Apto\n");
    } else {
        printf("Inapto\n");
    }

    return 0;
}
