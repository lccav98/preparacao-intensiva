#include <stdio.h>

#define COL 4

int soma_matriz(const int m[][COL], int linhas);
double media_matriz(const int m[][COL], int linhas);
int contar_acima_media(const int m[][COL], int linhas);

int main(void) {
    int linhas, m[10][COL];
    scanf("%d", &linhas);
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < COL; j++) {
            scanf("%d", &m[i][j]);
        }
    }
    printf("Soma: %d\n", soma_matriz(m, linhas));
    printf("Media: %.2f\n", media_matriz(m, linhas));
    printf("Acima da media: %d\n", contar_acima_media(m, linhas));
    return 0;
}

int soma_matriz(const int m[][COL], int linhas) {
    int soma = 0;
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < COL; j++) {
            soma += m[i][j];
        }
    }
    return soma;
}

double media_matriz(const int m[][COL], int linhas) {
    return (double)soma_matriz(m, linhas) / (linhas * COL);
}

int contar_acima_media(const int m[][COL], int linhas) {
    double med = media_matriz(m, linhas);
    int cont = 0;
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < COL; j++) {
            if (m[i][j] > med) {
                cont++;
            }
        }
    }
    return cont;
}
