#include <stdio.h>
#define N 5

int main(void) {
    int v[N];

    for (int i = 0; i < N; i++) {
        scanf("%d", &v[i]);
    }

    printf("Direta:");
    for (int i = 0; i < N; i++) {
        printf(" %d", v[i]);
    }
    printf("\nInversa:");
    for (int i = N - 1; i >= 0; i--) {
        printf(" %d", v[i]);
    }
    printf("\n");

    return 0;
}
