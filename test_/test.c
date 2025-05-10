/* A function parameter cannot have a storage class */
int a = 3;

static int f(int i) {
    int a = 4;
    return a;
}

int main(void) {
    return f(1);
}