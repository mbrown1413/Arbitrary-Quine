const char* c_code[] = {
    "#include <stdio.h>",
    "void print_py_list(const char* name, const char* list[], int size) {",
    "    int i;",
    "    printf(\"%s = [\\n\", name);",
    "    for (i=0; i<size; i++) {",
    "        int c=0;",
    "        printf(\"    \\\"\");",
    "        while (1) {",
    "            if (list[i][c] == '\\\\') {",
    "                printf(\"\\\\\\\\\");",
    "            } else if (list[i][c] == '\"') {",
    "                printf(\"\\\\\\\"\");",
    "            } else if (list[i][c] == '\\0') {",
    "                break;",
    "            } else {",
    "                printf(\"%c\", list[i][c]);",
    "            }",
    "            c++;",
    "        }",
    "        printf(\"\\\",\\n\");",
    "    }",
    "    printf(\"]\\n\");",
    "}",
    "int main() {",
    "    int i;",
    "    print_py_list(\"c_code\", c_code, sizeof(c_code)/sizeof(char*));",
    "    print_py_list(\"py_code\", py_code, sizeof(py_code)/sizeof(char*));",
    "    for (i=0; i<sizeof(py_code)/sizeof(char*); i++) {",
    "        printf(\"%s\\n\", py_code[i]);",
    "    }",
    "}",
};
const char* py_code[] = {
    "def print_c_list(name, l):",
    "    print \"const char* %s[] = {\" % name",
    "    for item in l:",
    "        print \"    \\\"\"+item.replace(\"\\\\\", r\"\\\\\").replace(\"\\\"\", \"\\\\\\\"\")+\"\\\",\"",
    "    print \"};\"",
    "print_c_list(\"c_code\", c_code)",
    "print_c_list(\"py_code\", py_code)",
    "for line in c_code:",
    "    print line",
};
#include <stdio.h>
void print_py_list(const char* name, const char* list[], int size) {
    int i;
    printf("%s = [\n", name);
    for (i=0; i<size; i++) {
        int c=0;
        printf("    \"");
        while (1) {
            if (list[i][c] == '\\') {
                printf("\\\\");
            } else if (list[i][c] == '"') {
                printf("\\\"");
            } else if (list[i][c] == '\0') {
                break;
            } else {
                printf("%c", list[i][c]);
            }
            c++;
        }
        printf("\",\n");
    }
    printf("]\n");
}
int main() {
    int i;
    print_py_list("c_code", c_code, sizeof(c_code)/sizeof(char*));
    print_py_list("py_code", py_code, sizeof(py_code)/sizeof(char*));
    for (i=0; i<sizeof(py_code)/sizeof(char*); i++) {
        printf("%s\n", py_code[i]);
    }
}
