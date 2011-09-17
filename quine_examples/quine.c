#include <stdio.h>
const char* code[] = {
    "};",
    "const int code_length = 27;",
    "int main() {",
    "    printf(\"#include <stdio.h>\\n\");",
    "    printf(\"const char* code[] = {\\n\");",
    "    int i;",
    "    for (i=0; i<code_length; i++) {",
    "        int c=0;",
    "        printf(\"    \\\"\");",
    "        while (1) {",
    "            if (code[i][c] == '\\\\') {",
    "                printf(\"\\\\\\\\\");",
    "            } else if (code[i][c] == '\"') {",
    "                printf(\"\\\\\\\"\");",
    "            } else if (code[i][c] == '\\0') {",
    "                break;",
    "            } else {",
    "                printf(\"%c\", code[i][c]);",
    "            }",
    "            c++;",
    "        }",
    "        printf(\"\\\",\\n\");",
    "    }",
    "    for (i=0; i<code_length; i++) {",
    "        printf(\"%s\\n\", code[i]);",
    "    }",
    "}",
};
const int code_length = 27;
int main() {
    printf("#include <stdio.h>\n");
    printf("const char* code[] = {\n");
    int i;
    for (i=0; i<code_length; i++) {
        int c=0;
        printf("    \"");
        while (1) {
            if (code[i][c] == '\\') {
                printf("\\\\");
            } else if (code[i][c] == '"') {
                printf("\\\"");
            } else if (code[i][c] == '\0') {
                break;
            } else {
                printf("%c", code[i][c]);
            }
            c++;
        }
        printf("\",\n");
    }
    for (i=0; i<code_length; i++) {
        printf("%s\n", code[i]);
    }
}
