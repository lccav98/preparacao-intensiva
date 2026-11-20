#include <stdio.h>
#define MAX 100

int main(void) {
    int n;
    int v[MAX], aprov[MAX];
    int freq[10] = {0};

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int k = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] >= 0 && v[i] <= 9) {
            freq[v[i]]++;
        }
        if (v[i] >= 6) {
            aprov[k] = v[i];
            k++;
        }
    }

    printf("Aprovadas:");
    if (k == 0) {
        printf(" Nenhuma\n");
    } else {
        for (int i = 0; i < k; i++) {
            printf(" %d", aprov[i]);
        }
        printf("\n");
    }

    for (int d = 0; d < 10; d++) {
        if (freq[d] > 0) {
            printf("Nota %d: %d\n", d, freq[d]);
        }
    }
    return 0;
}
