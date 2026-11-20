#include <stdio.h>

int main(void) {
    int idade, jejum_horas;
    double peso;

    if (scanf("%d %lf %d", &idade, &peso, &jejum_horas) != 3) {
        return 1;
    }

    if (idade < 16 || idade > 69) {
        printf("Impedimento: Idade Fora da Faixa\n");
    } else {
        if (peso < 50.0) {
            printf("Impedimento: Peso Insuficiente\n");
        } else {
            if (jejum_horas < 2 || jejum_horas > 12) {
                printf("Impedimento: Jejum Inadequado\n");
            } else {
                printf("Apto para Doacao\n");
            }
        }
    }

    return 0;
}
