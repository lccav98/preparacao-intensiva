#include <stdio.h>
#define MAX 100

int main(void) {
    int n, m, v[MAX], p[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &m);
    for (int k = 0; k < m; k++) {
        scanf("%d", &p[k]);
    }

    int ocorrencias = 0;
    for (int i = 0; i <= n - m; i++) {
        int casou = 1;
        for (int k = 0; k < m; k++) {
            if (v[i + k] != p[k]) {
                casou = 0;
                break;
            }
        }
        if (casou) {
            ocorrencias++;
        }
    }

    printf("Ocorrencias: %d\n", ocorrencias);
    return 0;
}
