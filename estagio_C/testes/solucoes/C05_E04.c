#include <stdio.h>

int main(void) {
    int inicio, passo;
    int qtd = 0;

    scanf("%d %d", &inicio, &passo);

    for (int i = inicio; i >= 1; i -= passo) {
        printf("%d\n", i);
        qtd++;
    }

    printf("Contagem: %d\n", qtd);
    return 0;
}
