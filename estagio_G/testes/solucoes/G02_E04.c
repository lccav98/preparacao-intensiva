#include <stdio.h>

void sequencia_ab(int n);

int main(void) {
    int n;
    scanf("%d", &n);
    sequencia_ab(n);
    printf("\n");
    return 0;
}

void sequencia_ab(int n) {
    if (n <= 0) {
        return;
    }
    printf("A%d ", n);
    sequencia_ab(n - 1);
    if (n > 1) {
        printf(" ");
    }
    printf("B%d", n);
}
