#include <stdio.h>
#define MAX_P 10
#define MAX_L 10
#define MAX_C 10

int main(void) {
    static int cubo[MAX_P][MAX_L][MAX_C];
    int P, L, C, delta;

    scanf("%d %d %d", &P, &L, &C);
    for (int p = 0; p < P; p++) {
        for (int i = 0; i < L; i++) {
            for (int j = 0; j < C; j++) {
                scanf("%d", &cubo[p][i][j]);
            }
        }
    }
    scanf("%d", &delta);

    int total = 0, saturados = 0;
    for (int p = 0; p < P; p++) {
        int soma_camada = 0;
        for (int i = 0; i < L; i++) {
            for (int j = 0; j < C; j++) {
                cubo[p][i][j] += delta;
                if (cubo[p][i][j] < 0) {
                    cubo[p][i][j] = 0;
                } else if (cubo[p][i][j] > 255) {
                    cubo[p][i][j] = 255;
                }
                if (cubo[p][i][j] == 0 || cubo[p][i][j] == 255) {
                    saturados++;
                }
                soma_camada += cubo[p][i][j];
            }
        }
        total += soma_camada;
        printf("Camada %d: soma = %d\n", p, soma_camada);
    }
    printf("Total geral: %d\n", total);
    printf("Saturados (0 ou 255): %d\n", saturados);
    return 0;
}
