#include <stdio.h>
#define ALTURA_MAX 500
#define LARGURA_MAX 500

int main(void) {
    static int img[ALTURA_MAX][LARGURA_MAX];
    int largura, altura, delta, limiar;

    scanf("%d %d", &largura, &altura);
    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            scanf("%d", &img[i][j]);
        }
    }
    scanf("%d %d", &delta, &limiar);

    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            img[i][j] += delta;
            if (img[i][j] < 0) {
                img[i][j] = 0;
            } else if (img[i][j] > 255) {
                img[i][j] = 255;
            }
        }
    }

    int min_v = img[0][0], min_i = 0, min_j = 0;
    int max_v = img[0][0], max_i = 0, max_j = 0;
    int pretos = 0, brancos = 0;

    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            if (img[i][j] < min_v) {
                min_v = img[i][j];
                min_i = i;
                min_j = j;
            }
            if (img[i][j] > max_v) {
                max_v = img[i][j];
                max_i = i;
                max_j = j;
            }
            if (img[i][j] < limiar) {
                img[i][j] = 0;
                pretos++;
            } else {
                img[i][j] = 255;
                brancos++;
            }
        }
    }

    printf("P2\n%d %d\n255\n", largura, altura);
    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", img[i][j]);
        }
        printf("\n");
    }
    printf("Minimo: %d em (%d, %d)\n", min_v, min_i, min_j);
    printf("Maximo: %d em (%d, %d)\n", max_v, max_i, max_j);
    printf("Pretos: %d Brancos: %d\n", pretos, brancos);
    return 0;
}
