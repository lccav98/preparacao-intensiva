#include <stdio.h>

int main(void) {
    int valor;
    int maior, menor;

    scanf("%d", &valor);

    if (valor == -1) {
        printf("Nenhum dado informado\n");
    } else {
        maior = valor;
        menor = valor;

        while (valor != -1) {
            if (valor > maior) {
                maior = valor;
            }
            if (valor < menor) {
                menor = valor;
            }
            scanf("%d", &valor);
        }

        printf("Maior: %d\n", maior);
        printf("Menor: %d\n", menor);
    }

    return 0;
}
