#include <stdio.h>
#define MAX_SIGLA 11
#define MAX_CIDADE 31

int main(void) {
    char sigla[MAX_SIGLA];
    char cidade[MAX_CIDADE];
    int ch;

    scanf("%10s", sigla);
    while ((ch = getchar()) != '\n' && ch != EOF) {
    }

    fgets(cidade, MAX_CIDADE, stdin);
    for (int i = 0; cidade[i] != '\0'; i++) {
        if (cidade[i] == '\n') {
            cidade[i] = '\0';
            break;
        }
    }

    printf("Sigla: %s | Cidade: %s\n", sigla, cidade);
    return 0;
}
