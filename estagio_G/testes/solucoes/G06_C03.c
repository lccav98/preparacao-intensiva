#include <stdio.h>

int contar_digitos_str(const char s[], int i);
int tem_caractere(const char s[], int i, char c);

int main(void) {
    char s[100], c;
    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }
    scanf(" %c", &c);

    printf("Digitos: %d\n", contar_digitos_str(s, 0));
    if (tem_caractere(s, 0, c)) {
        printf("Contem: Sim\n");
    } else {
        printf("Contem: Nao\n");
    }
    return 0;
}

int contar_digitos_str(const char s[], int i) {
    if (s[i] == '\0') {
        return 0;
    }
    int dig = (s[i] >= '0' && s[i] <= '9');
    return dig + contar_digitos_str(s, i + 1);
}

int tem_caractere(const char s[], int i, char c) {
    if (s[i] == '\0') {
        return 0;
    }
    if (s[i] == c) {
        return 1;
    }
    return tem_caractere(s, i + 1, c);
}
