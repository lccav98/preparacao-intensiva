#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int menor = v[0], pos_menor = 0;
    for (int i = 1; i < n; i++) {
        if (v[i] <= menor) {
            menor = v[i];
            pos_menor = i;
        }
    }

    printf("Menor: %d\nIndice: %d\n", menor, pos_menor);
    return 0;
}
