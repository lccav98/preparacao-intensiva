#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int freq[6] = {0};
    for (int i = 0; i < n; i++) {
        freq[v[i]]++;
    }

    for (int k = 0; k <= 5; k++) {
        printf("Nota %d: %d\n", k, freq[k]);
    }
    return 0;
}
