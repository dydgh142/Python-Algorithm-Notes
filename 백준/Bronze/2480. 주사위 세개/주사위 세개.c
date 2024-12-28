#include <stdio.h>

int main(void) {
    
    int a = 0, b=0, c=0, m=0;
    
    scanf ("%d %d %d", &a, &b, &c);
    if (a==b && b==c){
        m = 10000+a*1000;
    }
    else if (a==b || b==c || a==c){
        if(a==b){
            m = 1000+a*100;
        }
        else if(b==c){
            m = 1000+b*100;
        }
         else if(c==a){
            m = 1000+c*100;
        }
    }
    else{
        if(a>b && a>c){
            m = 100*a;
        }
        else if (b>a && b>c){
            m = 100*b;
        }
        else{
            m = 100*c;
        }
        
    }

    
    printf("%d", m);

    return 0;
}