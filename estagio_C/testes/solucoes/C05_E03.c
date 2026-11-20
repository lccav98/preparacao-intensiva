#include <stdio.h>

int main(void) {
    int n;
    long long fat = 1;

    scanf("%d", &n);

    for (int i = 1; i <= n; i++) {
        fat *= i;
    }

    printf("%d! = %lld\n", n, fat);
    return 0;
}
