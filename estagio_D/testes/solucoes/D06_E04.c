#include <stdio.h>
#define MAX_TAG 21
#define MAX_TITULO 61

int main(void) {
    char tag[MAX_TAG];
    char titulo[MAX_TITULO];
    int ch;

    scanf("%20s", tag);
    while ((ch = getchar()) != '\n' && ch != EOF) {
    }

    fgets(titulo, MAX_TITULO, stdin);
    for (int i = 0; titulo[i] != '\0'; i++) {
        if (titulo[i] == '\n') {
            titulo[i] = '\0';
            break;
        }
    }

    printf("Tag: %s\nTitulo: [%s]\n", tag, titulo);
    return 0;
}
