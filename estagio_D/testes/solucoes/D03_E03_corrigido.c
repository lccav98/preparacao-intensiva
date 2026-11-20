#include <stdio.h>
#define MAX 100

int main(void) {
    int n, x, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &x);

    int pos = -1;
    for (int i = 0; i < n; i++) {
        if (v[i] == x) {
            pos = i;
            break;
        }
    }

    for (int i = 0; i < n / 2; i++) {
        int aux = v[i];
        v[i] = v[n - 1 - i];
        v[n - 1 - i] = aux;
    }

    printf("Indice: %d\nInvertido:", pos);
    for (int i = 0; i < n; i++) {
        printf(" %d", v[i]);
    }
    printf("\n");
    return 0;
}
