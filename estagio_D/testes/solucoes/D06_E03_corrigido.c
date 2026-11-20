#include <stdio.h>
#define MAX_COD 16
#define MAX_DESC 51

int main(void) {
    char codigo[MAX_COD];
    char desc[MAX_DESC];
    int ch;

    scanf("%15s", codigo);
    while ((ch = getchar()) != '\n' && ch != EOF) {
    }

    fgets(desc, MAX_DESC, stdin);
    for (int i = 0; desc[i] != '\0'; i++) {
        if (desc[i] == '\n') {
            desc[i] = '\0';
            break;
        }
    }

    printf("Codigo: %s\nDesc: [%s]\n", codigo, desc);
    return 0;
}
