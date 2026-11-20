#include <stdio.h>

int main(void) {
    int n;
    int i = 1;
    scanf("%d", &n);

    while (i <= 10) {
        printf("%d x %d = %d\n", n, i, n * i);
        i++;
    }

    return 0;
}
