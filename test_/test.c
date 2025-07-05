// postfix operators have higher precedence than prefix
struct inner {
    char inner_arr[3];
};

struct outer {
    struct inner b;
    int a;
    int d;
    long c;
};

struct outer array = {{{2, 3, 4}}};

int main(void) {
    //int i = -array[2].b.inner_arr[1];
    //return i == -11;
}