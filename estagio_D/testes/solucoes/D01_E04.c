#include <stdio.h>
#define N 6

int main(void) {
    int v[N];

    for (int i = 0; i < N; i++) {
        scanf("%d", &v[i]);
    }

    printf("Metade 2:");
    for (int i = N / 2; i < N; i++) {
        printf(" %d", v[i]);
    }
    printf("\nMetade 1:");
    for (int i = 0; i < N / 2; i++) {
        printf(" %d", v[i]);
    }
    printf("\n");

    return 0;
}
