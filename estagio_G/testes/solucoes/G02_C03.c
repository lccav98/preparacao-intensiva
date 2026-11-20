#include <stdio.h>

void pulso(int n);

int main(void) {
    int n;
    scanf("%d", &n);
    pulso(n);
    printf("\n");
    return 0;
}

void pulso(int n) {
    if (n <= 0) {
        printf("0");
        return;
    }
    printf("%d ", n);
    pulso(n - 1);
    printf(" %d", n);
}
