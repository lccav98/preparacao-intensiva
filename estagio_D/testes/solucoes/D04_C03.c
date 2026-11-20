#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int unicos[MAX], k = 0;
    for (int i = 0; i < n; i++) {
        int repetido = 0;
        for (int j = 0; j < i; j++) {
            if (v[j] == v[i]) {
                repetido = 1;
                break;
            }
        }
        if (repetido == 0) {
            unicos[k++] = v[i];
        }
    }

    printf("Unicos (%d):", k);
    for (int i = 0; i < k; i++) {
        printf(" %d", unicos[i]);
    }
    printf("\nRepetidos removidos: %d\n", n - k);
    return 0;
}
