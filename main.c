#include <stdio.h>
#include <stdlib.h>

int f(int u){
    if(u == 0){
        return 1;
    }else{
        return u * f(u - 1);
    }

}

int main()
{
    int x;
    printf("escolha um numero: ");
    scanf("%i", &x);
    printf("\nvalor: %i", f(x));
    return 0;
}
