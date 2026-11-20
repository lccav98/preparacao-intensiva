#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int maior = v[0], pos_maior = 0;
    int menor = v[0], pos_menor = 0;
    for (int i = 1; i < n; i++) {
        if (v[i] > maior) {
            maior = v[i];
            pos_maior = i;
        }
        if (v[i] <= menor) {
            menor = v[i];
            pos_menor = i;
        }
    }

    printf("Maior: %d (indice %d)\nMenor: %d (indice %d)\n",
           maior, pos_maior, menor, pos_menor);
    return 0;
}
