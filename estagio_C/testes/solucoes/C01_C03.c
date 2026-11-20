#include <stdio.h>

int main(void) {
    int inicio, fim, passo;
    scanf("%d %d %d", &inicio, &fim, &passo);

    while (inicio <= fim) {
        printf("%d\n", inicio);
        inicio += passo;
    }

    return 0;
}
