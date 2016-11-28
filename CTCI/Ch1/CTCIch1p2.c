#include <stdio.h>

void swap(char* str, int one, int two){
    printf("debug:: entered swap() with args %s, %d, %d\n", str, one, two);
    printf("debug:: str[%d] = %c\n", one, str[one]);
    printf("debug:: str[%d] = %c\n", two, str[two]);
    char temp;
    temp = str[one];
    str[one] = str[two];
    str[two] = temp;
    printf("debug:: swapped %d and %d, str = %s\n", one, two, str);
    return;
}

void reverse(char* str){
    printf("debug:: entered reverse() with arg %s\n", str);
    int length = sizeof(str);
    int i = 0;
    int j = length - 3;
    while (i < j){
        swap(str, i, j);
        i++;
        j--;
    }
    return;
}

int main(int argc, char* argv[]){
    printf("debug:: argc = %d\n", argc);
    printf("debug:: argv[0] = %s\n", argv[0]);
    printf("debug:: argv[1] = %s\n", argv[1]);
    reverse(argv[1]);
    printf("%s\n", argv[1]);
    return 1;
}
