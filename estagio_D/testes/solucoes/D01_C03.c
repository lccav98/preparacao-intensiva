#include <stdio.h>
#define MAX 50

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    printf("Primeiro: %d | Ultimo: %d\n", v[0], v[n - 1]);
    printf("Inverso:");
    for (int i = n - 1; i >= 0; i--) {
        printf(" %d", v[i]);
    }
    printf("\n");

    return 0;
}
