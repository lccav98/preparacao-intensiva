#include <stdio.h>
#include <string.h>
#define MAX 81

int main(void) {
    char orig[MAX];
    char inv[MAX];

    fgets(orig, MAX, stdin);
    int len = (int)strlen(orig);
    if (len > 0 && orig[len - 1] == '\n') {
        orig[len - 1] = '\0';
        len--;
    }

    for (int i = 0; i < len; i++) {
        inv[i] = orig[len - 1 - i];
    }
    inv[len] = '\0';

    printf("Original: %s\nInvertida: %s\n", orig, inv);
    if (strcmp(orig, inv) == 0) {
        printf("Identicas: Sim\n");
    } else {
        printf("Identicas: Nao\n");
    }
    return 0;
}
