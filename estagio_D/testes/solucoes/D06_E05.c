#include <stdio.h>
#define MAX 81

int main(void) {
    char texto[MAX];
    char alvo;

    fgets(texto, MAX, stdin);
    for (int i = 0; texto[i] != '\0'; i++) {
        if (texto[i] == '\n') {
            texto[i] = '\0';
            break;
        }
    }

    scanf(" %c", &alvo);
    for (int i = 0; texto[i] != '\0'; i++) {
        if (texto[i] == alvo) {
            texto[i] = '\0';
            break;
        }
    }

    printf("Resultado: [%s]\n", texto);
    return 0;
}
