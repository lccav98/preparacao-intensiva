#include <stdio.h>

int mdc(int a, int b);
int mmc(int a, int b);

int main(void) {
    int x, y;
    scanf("%d %d", &x, &y);
    printf("MDC: %d\n", mdc(x, y));
    printf("MMC: %d\n", mmc(x, y));
    return 0;
}

int mdc(int a, int b) {
    while (b != 0) {
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int mmc(int a, int b) {
    int d = mdc(a, b);
    return (a / d) * b;
}
