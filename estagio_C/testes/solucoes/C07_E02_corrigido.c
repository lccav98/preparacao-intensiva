#include <stdio.h>

int main(void) {
    int n;
    if (scanf("%d", &n) != 1) {
        return 1;
    }

    int i = n;
    while (i >= 1) {
        if (i == 3) {
            i--;
            continue;
        }
        printf("%d ", i);
        i--;
    }
    printf("\n");
    return 0;
}
