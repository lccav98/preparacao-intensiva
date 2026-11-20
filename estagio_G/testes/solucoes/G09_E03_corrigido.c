#include <stdio.h>

int soma_digitos(int n);
int maior_vetor(const int v[], int n);
int comprimento(const char s[], int i);
void inverter(char s[], int i, int j);

int main(void) {
    char s[100];
    int num, n, v[50];

    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }
    scanf("%d %d", &num, &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int len = comprimento(s, 0);
    inverter(s, 0, len - 1);

    printf("Soma digitos: %d\n", soma_digitos(num));
    printf("Maior: %d\n", maior_vetor(v, n));
    printf("Invertida: %s\n", s);
    return 0;
}

int soma_digitos(int n) {
    // Erro original 1: retornava 1 no caso base n == 0, somando 1 a mais.
    // Correcao: retornar 0 quando n == 0.
    if (n == 0) {
        return 0;
    }
    return (n % 10) + soma_digitos(n / 10);
}

int maior_vetor(const int v[], int n) {
    // Erro original 2: usava caso base n == 0 retornando 0 (falha com todos negativos) e fazia dupla chamada.
    // Correcao: caso base n == 1 retornando v[0] e chamada unica em variavel local m.
    if (n == 1) {
        return v[0];
    }
    int m = maior_vetor(v, n - 1);
    if (v[n - 1] > m) {
        return v[n - 1];
    }
    return m;
}

int comprimento(const char s[], int i) {
    if (s[i] == '\0') {
        return 0;
    }
    return 1 + comprimento(s, i + 1);
}

void inverter(char s[], int i, int j) {
    // Erro original 3: usava if (i == j), falhando para strings de tamanho par ou vazias.
    // Correcao: usar if (i >= j) return;.
    if (i >= j) {
        return;
    }
    char aux = s[i];
    s[i] = s[j];
    s[j] = aux;
    inverter(s, i + 1, j - 1);
}
