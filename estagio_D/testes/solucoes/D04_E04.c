#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int freq[10] = {0};
    for (int i = 0; i < n; i++) {
        freq[v[i]]++;
    }

    for (int d = 0; d < 10; d++) {
        if (freq[d] > 0) {
            printf("%d: ", d);
            for (int c = 0; c < freq[d]; c++) {
                printf("*");
            }
            printf("\n");
        }
    }
    return 0;
}
