#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int positivos = 0;
    int menor = v[0], pos_menor = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] > 0) {
            positivos++;
        }
        if (v[i] < menor) {
            menor = v[i];
            pos_menor = i;
        }
    }

    printf("Positivos: %d\nMenor: %d (indice %d)\n", positivos, menor, pos_menor);
    return 0;
}
