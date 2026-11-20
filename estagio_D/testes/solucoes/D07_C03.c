#include <stdio.h>
#include <ctype.h>
#define MAX 101

int main(void) {
    char orig[MAX];
    char limpa[MAX];

    fgets(orig, MAX, stdin);
    for (int i = 0; orig[i] != '\0'; i++) {
        if (orig[i] == '\n') {
            orig[i] = '\0';
            break;
        }
    }

    int j = 0, removidos = 0;
    for (int i = 0; orig[i] != '\0'; i++) {
        if (isalpha((unsigned char)orig[i]) || isdigit((unsigned char)orig[i])) {
            limpa[j++] = (char)tolower((unsigned char)orig[i]);
        } else {
            removidos++;
        }
    }
    limpa[j] = '\0';

    printf("Limpa: [%s]\nRemovidos: %d\n", limpa, removidos);
    return 0;
}
