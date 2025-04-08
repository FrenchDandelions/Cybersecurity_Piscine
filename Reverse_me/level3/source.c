#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void fail() {
    puts("Nope.");
    exit(1);
}

void success() {
    puts("Good job.");
}

int main(void) {
    char input[31];
    char result[9] = {0};  // Will build up to 8 characters plus null terminator
    int input_index = 2;
    int result_index = 1;

    printf("Please enter key: ");
    if (scanf("%30s", input) != 1) {
        fail();
    }

    if (input[0] != '4' || input[1] != '2') {
        fail();
    }

    result[0] = '*';  // Result string must start with '*'

    // Extract groups of 3 digits and convert them to characters
    while (strlen(result) < 8 && input_index + 2 < (int)strlen(input)) {
        char buffer[4] = {
            input[input_index],
            input[input_index + 1],
            input[input_index + 2],
            '\0'
        };

        int val = atoi(buffer);
        result[result_index++] = (char)val;
        input_index += 3;
    }

    result[result_index] = '\0';

    // Check if the result matches "********"
    if (strcmp(result, "********") == 0) {
        success();
    } else {
        fail();
    }

    return 0;
}
