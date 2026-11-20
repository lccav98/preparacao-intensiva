#ifndef FUNCOES_H
#define FUNCOES_H

#include "imagem.h"

void ajustarBrilho(int img[ALTURA][LARGURA], int b);
void aplicarBlur(int img[ALTURA][LARGURA], int t);
void ordenar(int v[], int n);
void aplicarMediana(int img[ALTURA][LARGURA]);
void limiarizar(int img[ALTURA][LARGURA], int limiar);
void resumoImagem(const int img[ALTURA][LARGURA], int *min, int *max, double *media);

#endif
