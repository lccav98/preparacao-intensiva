#include "calc.h"

int soma_intervalo(int a, int b) {
    if (a > b) {
        int aux = a;
        a = b;
        b = aux;
    }
    int soma = 0;
    for (int i = a; i <= b; i++) {
        soma += i;
    }
    return soma;
}

int contar_pares(int a, int b) {
    if (a > b) {
        int aux = a;
        a = b;
        b = aux;
    }
    int cont = 0;
    for (int i = a; i <= b; i++) {
        if (i % 2 == 0) {
            cont++;
        }
    }
    return cont;
}
