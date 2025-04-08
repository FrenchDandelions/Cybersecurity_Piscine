#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void no() {
    puts("Nope.");
    exit(1);
}

void ok() {
    puts("Good job.");
}

int main(void) {
    char input[24];
    char result[9] = {0}; // up to 8 chars + null terminator
    int index = 2;
    int result_index = 1;

    printf("Please enter key: ");
    if (scanf("%23s", input) != 1) {
        no();
    }

    if (input[0] != '0' || input[1] != '0') {
        no();
    }

    result[0] = 'd';

    while (strlen(result) < 8 && index + 2 < (int)strlen(input)) {
        char buffer[4] = { input[index], input[index + 1], input[index + 2], '\0' };
        int val = atoi(buffer);
        result[result_index++] = (char)val;
        index += 3;
    }

    result[result_index] = '\0';

    if (strcmp(result, "delabere") == 0) {
        ok();
    } else {
        no();
    }

    return 0;
}
