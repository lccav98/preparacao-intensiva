#include <stdio.h>

double converter_celsius_para_kelvin(double c);
double limitar_intervalo(double val, double min, double max);

int main(void) {
    double t, kelvin;
    scanf("%lf", &t);
    kelvin = converter_celsius_para_kelvin(t);
    kelvin = limitar_intervalo(kelvin, 0.0, 1000.0);
    printf("Kelvin limitado: %.2f\n", kelvin);
    return 0;
}

double converter_celsius_para_kelvin(double c) {
    return c + 273.15;
}

double limitar_intervalo(double val, double min, double max) {
    if (val < min) {
        return min;
    }
    if (val > max) {
        return max;
    }
    return val;
}
