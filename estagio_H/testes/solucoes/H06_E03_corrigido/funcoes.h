#ifndef FUNCOES_H
#define FUNCOES_H

#include "imagem.h"

void ajustarBrilho(int img[ALTURA][LARGURA], int b);
void aplicarBlur(int img[ALTURA][LARGURA], int t);
void ordenar(int v[], int n);
void aplicarMediana(int img[ALTURA][LARGURA]);
// Bug 1 corrigido: tipo de retorno void alinhado a definicao em funcoes.c
void inverterCores(int img[ALTURA][LARGURA]);

#endif
