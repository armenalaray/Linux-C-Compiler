// postfix operators have higher precedence than prefix
struct inner {
    int inner_arr[3];
};

struct outer {
    int a;
    struct inner b;
};

int main(void) {
    struct outer * array;
    array->ale;
}