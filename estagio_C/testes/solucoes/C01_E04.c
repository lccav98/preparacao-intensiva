#include <stdio.h>

int main(void) {
    int n, atual;
    scanf("%d", &n);

    if (n % 2 != 0) {
        atual = n - 1;
    } else {
        atual = n;
    }

    while (atual >= 0) {
        printf("%d\n", atual);
        atual -= 2;
    }

    return 0;
}
