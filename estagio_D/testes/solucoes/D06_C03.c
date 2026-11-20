#include <stdio.h>
#define MAX_MAT 13
#define MAX_NOME 51
#define MAX_DISC 41

int main(void) {
    char mat[MAX_MAT];
    char nome[MAX_NOME];
    char disc[MAX_DISC];
    int ch;

    scanf("%12s", mat);
    while ((ch = getchar()) != '\n' && ch != EOF) {
    }

    fgets(nome, MAX_NOME, stdin);
    for (int i = 0; nome[i] != '\0'; i++) {
        if (nome[i] == '\n') {
            nome[i] = '\0';
            break;
        }
    }

    fgets(disc, MAX_DISC, stdin);
    for (int i = 0; disc[i] != '\0'; i++) {
        if (disc[i] == '\n') {
            disc[i] = '\0';
            break;
        }
    }

    printf("Matricula: %s\nNome: %s\nDisciplina: %s\n", mat, nome, disc);
    return 0;
}
