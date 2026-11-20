#include <stdio.h>
#include "estatistica.h"

int main(void) {
    int n, v[50], min, max;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d %d", &min, &max);
    printf("Media: %.2f\n", media_vetor(v, n));
    printf("No intervalo: %d\n", contar_no_intervalo(v, n, min, max));
    return 0;
}
