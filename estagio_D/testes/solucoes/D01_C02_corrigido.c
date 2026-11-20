#include <stdio.h>
#define MAX 20

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    printf("Impares:");
    for (int i = 1; i < n; i += 2) {
        printf(" %d", v[i]);
    }
    printf("\nInverso:");
    for (int i = n - 1; i >= 0; i--) {
        printf(" %d", v[i]);
    }
    printf("\n");

    return 0;
}
