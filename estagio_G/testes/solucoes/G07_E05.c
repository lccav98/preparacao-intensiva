#include <stdio.h>

int comprimento(const char s[], int i);
void inverter(char s[], int i, int j);

int main(void) {
    char s[100];
    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }

    int len = comprimento(s, 0);
    inverter(s, 0, len - 1);
    printf("Invertida: %s\n", s);
    return 0;
}

int comprimento(const char s[], int i) {
    if (s[i] == '\0') {
        return 0;
    }
    return 1 + comprimento(s, i + 1);
}

void inverter(char s[], int i, int j) {
    if (i >= j) {
        return;
    }
    char aux = s[i];
    s[i] = s[j];
    s[j] = aux;
    inverter(s, i + 1, j - 1);
}
