
#include <stdio.h>
#include <stdlib.h>

void escape_and_print(char* str) {
    int c=0;
    while (1) {
        if (str[c] == '\\') {
            printf("\\\\");
        } else if (str[c] == '"') {
            printf("\\\"");
        } else if (str[c] == '\0') {
            break;
        } else {
            printf("%c", str[c]);
        }
        c++;
    }
}

void print_py_list(char* name, char* list[], int size) {
    int i;
    printf("%s = [\n", name);
    for (i=0; i<size; i++) {
        printf("    \"");
        escape_and_print(list[i]);
        printf("\",\n");
    }
    printf("]\n");
}

void print_c_list(char* name, char* list[], int size) {
    int i;
    printf("char* %s[] = {\n", name);
    for (i=0; i<size; i++) {
        printf("    \"");
        escape_and_print(list[i]);
        printf("\",\n");
    }
    printf("};\n");
}

void print_list(char* list[], int size) {
    int i=0;
    for (i=0; i<size; i++) {
        printf("%s\n", list[i]);
    }
}

int main() {
    int i;

    // Get list_print_func
    void (*list_print_func)(char* name, char* list[], int size);
    if (strcmp(languages[0], "python") == 0) {
        list_print_func = print_py_list;
    } else if (strcmp(languages[0], "c") == 0) {
        list_print_func = print_c_list;
    } else {
        printf("UNRECOGNIZED LANGUAGE\n");
        exit(-1);
    }

    // Print program lists
    list_print_func("python_prog", python_prog, sizeof(python_prog)/sizeof(char*));
    list_print_func("c_prog", c_prog, sizeof(c_prog)/sizeof(char*));

    // Rotate and print language array
    int num_languages = sizeof(languages)/sizeof(char*);
    char* new_languages[num_languages];
    for (i=0; i<num_languages; i++) {
        new_languages[i] = languages[(i+1)%num_languages];
    }
    list_print_func("languages", new_languages, num_languages);

    // Print the actual program
    if (strcmp(languages[0], "python") == 0) {
        print_list(python_prog, sizeof(python_prog)/sizeof(char*));
    } else if (strcmp(languages[0], "c") == 0) {
        print_list(c_prog, sizeof(c_prog)/sizeof(char*));
    } else {
        printf("UNRECOGNIZED LANGUAGE\n");
        exit(-1);
    }

}
