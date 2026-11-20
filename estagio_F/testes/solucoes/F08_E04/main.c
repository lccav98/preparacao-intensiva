#include <stdio.h>
#include "vetor.h"

int main(void) {
    int n, v[50];
    scanf("%d", &n);
    ler_vetor(v, n);
    printf("Soma: %d\n", soma_vetor(v, n));
    printf("Maior: %d\n", maior_vetor(v, n));
    return 0;
}
