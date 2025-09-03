#include <stdio.h>

int letraNum(char c) { return c - 'A'; }
char numLetra(int x) { return (x % 26 + 26) % 26 + 'A'; }

int comprimento(char s[]) {
    int i = 0;
    while (s[i] != '\0') i++;
    return i;
}

char paraMaiuscula(char c) {
    if (c >= 'a' && c <= 'z') return c - 'a' + 'A';
    return c;
}

int eLetra(char c) {
    return (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z');
}

void multiplicar(int M[2][2], int vIn[2], int vOut[2]) {
    int i, j, soma;
    for (i = 0; i < 2; i++) {
        soma = 0;
        for (j = 0; j < 2; j++)
            soma += M[i][j] * vIn[j];
        vOut[i] = (soma % 26 + 26) % 26;
    }
}

void cifra(char txt[], char res[], int M[2][2]) {
    int tam = comprimento(txt);
    int i, j;
    for (i = 0; i < tam; i += 2) {
        int vin[2], vout[2];
        for (j = 0; j < 2; j++)
            vin[j] = letraNum(txt[i+j]);
        multiplicar(M, vin, vout);
        for (j = 0; j < 2; j++)
            res[i+j] = numLetra(vout[j]);
    }
    res[tam] = '\0';
}

int inverso(int a) {
    int x;
    a = (a % 26 + 26) % 26;
    for (x = 1; x < 26; x++)
        if ((a * x) % 26 == 1) return x;
    return -1;
}

void inversa(int M[2][2], int Minv[2][2]) {
    int det = (M[0][0]*M[1][1] - M[0][1]*M[1][0] + 26) % 26;
    int invDet = inverso(det);

    Minv[0][0] =  ( M[1][1] * invDet) % 26;
    Minv[0][1] = (-M[0][1] * invDet + 26) % 26;
    Minv[1][0] = (-M[1][0] * invDet + 26) % 26;
    Minv[1][1] =  ( M[0][0] * invDet) % 26;
}

void prepara(char entrada[], char saida[]) {
    int i, k = 0;
    for (i = 0; entrada[i] != '\0'; i++) {
        if (eLetra(entrada[i])) {
            saida[k] = paraMaiuscula(entrada[i]);
            k++;
        }
    }
    if (k % 2 != 0) {
        saida[k] = 'X';
        k++;
    }
    saida[k] = '\0';
}

int main() {
    char texto[1000];
    char puro[1000], cifrado[1000], decifrado[1000];

    int K[2][2] = { {3, 2}, {5, 7} };
    int Kinv[2][2];
    inversa(K, Kinv);

    printf("Digite o texto (uma palavra): ");
    scanf("%s", texto);  // lê até o primeiro espaço

    prepara(texto, puro);
    cifra(puro, cifrado, K);
    cifra(cifrado, decifrado, Kinv);

    printf("Cifrado:   %s\n", cifrado);
    printf("Decifrado: %s\n", decifrado);

    return 0;
}
