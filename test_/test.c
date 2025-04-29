int main(void) {
    int a = 1;
    int b = 0;
    a ? b = 1 + a : (b = 2);
    return b;
}