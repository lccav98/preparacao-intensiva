#include <stdio.h>

int main(void) {
    int temp;
    int soma = 0;
    int maior;

    scanf("%d", &temp);
    if (temp != -999) {
        maior = temp;
        while (temp != -999) {
            soma += temp;
            if (temp > maior) {
                maior = temp;
            }
            scanf("%d", &temp);
        }
        printf("Soma: %d\n", soma);
        printf("Maior: %d\n", maior);
    }

    return 0;
}
