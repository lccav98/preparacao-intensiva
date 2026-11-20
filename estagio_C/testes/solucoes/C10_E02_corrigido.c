#include <stdio.h>

int main(void) {
    int num;
    int soma = 0;
    int maior = 0;
    int tem_valido = 0;

    while (1) {
        if (scanf("%d", &num) != 1 || num == -1) {
            break;
        }
        if (num % 5 == 0) {
            continue;
        }
        soma += num;
        if (!tem_valido || num > maior) {
            maior = num;
            tem_valido = 1;
        }
    }

    if (!tem_valido) {
        printf("Nenhum valor valido\n");
    } else {
        printf("Soma = %d\n", soma);
        printf("Maior = %d\n", maior);
    }

    return 0;
}
