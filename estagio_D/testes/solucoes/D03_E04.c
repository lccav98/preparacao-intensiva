#include <stdio.h>
#include <stdlib.h>
#define MAX 100

int main(void) {
    int n, x, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &x);

    int melhor_dist = abs(v[0] - x);
    int pos_melhor = 0;
    for (int i = 1; i < n; i++) {
        int d = abs(v[i] - x);
        if (d < melhor_dist) {
            melhor_dist = d;
            pos_melhor = i;
        }
    }

    printf("Mais proximo: %d (indice %d, distancia %d)\n",
           v[pos_melhor], pos_melhor, melhor_dist);
    return 0;
}
