#include <stdio.h>

int main(void) {
    double a, b;
    char op;

    if (scanf("%lf %lf %c", &a, &b, &op) != 3) {
        return 1;
    }

    switch (op) {
        case '+':
            printf("Resultado: %.2f\n", a + b);
            break;
        case '-':
            printf("Resultado: %.2f\n", a - b);
            break;
        case '*':
            printf("Resultado: %.2f\n", a * b);
            break;
        case '/':
            if (b == 0.0) {
                printf("Erro: Divisao por Zero\n");
            } else {
                printf("Resultado: %.2f\n", a / b);
            }
            break;
        default:
            printf("Operador Invalido\n");
            break;
    }

    return 0;
}
