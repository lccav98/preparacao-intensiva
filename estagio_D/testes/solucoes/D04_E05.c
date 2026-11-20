#include <stdio.h>
#define MAX 100

int main(void) {
    int n, a[MAX], b[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    for (int i = 0; i < n; i++) {
        scanf("%d", &b[i]);
    }

    int fa[10] = {0}, fb[10] = {0};
    for (int i = 0; i < n; i++) {
        fa[a[i]]++;
        fb[b[i]]++;
    }

    int iguais = 1;
    for (int d = 0; d < 10; d++) {
        if (fa[d] != fb[d]) {
            iguais = 0;
            break;
        }
    }

    int melhor = 0;
    int maior_total = fa[0] + fb[0];
    for (int d = 1; d < 10; d++) {
        int total = fa[d] + fb[d];
        if (total > maior_total) {
            maior_total = total;
            melhor = d;
        }
    }

    if (iguais) {
        printf("Mesmo histograma\n");
    } else {
        printf("Histogramas diferentes\n");
    }
    printf("Mais frequente: %d (total %d)\n", melhor, maior_total);
    return 0;
}
