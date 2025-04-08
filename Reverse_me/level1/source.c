#include <stdio.h>
#include <string.h>

int main()
{
    int var1;
    const char s1[] = "__stack_check";
    char s2[100];
    printf("Please enter key: ");
    scanf("%s", s2);
    var1 = strcmp(s1, s2);
    if (var1 == 0){
        printf("Good job.\n");
    }
    else{
        printf("Nope.\n");
    }
    return 0;
}