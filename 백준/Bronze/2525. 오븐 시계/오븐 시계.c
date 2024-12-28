#include <stdio.h>

int main(void) {
    
    int h = 0, m = 0, n = 0, a = 0;

    scanf("%d %d", &h, &m);
    scanf("%d", &n);
    m+=n;
    if (m>59){
        h+=m/60;
        m= m%60;
        if(h>23){
            h = h % 24;
        }
    }
    
    printf("%d %d", h, m);

    return 0;
}