#include <stdio.h>
#include <string.h>
#define MAX 31
#define MAX_RES 65

int main(void) {
    char a[MAX], b[MAX];
    char res[MAX_RES], inv[MAX_RES];

    scanf("%30s %30s", a, b);

    if (strcmp(a, b) == 0) {
        printf("Iguais: Sim\n");
    } else {
        printf("Iguais: Nao\n");
    }

    strcpy(res, a);
    strcat(res, "-");
    strcat(res, b);

    int len = (int)strlen(res);
    for (int i = 0; i < len; i++) {
        inv[i] = res[len - 1 - i];
    }
    inv[len] = '\0';

    printf("Uniao: %s\nInvertida: %s\n", res, inv);
    return 0;
}
