/* Variable initializers aren't permitted in parameter lists */
int bad_params(int a, int b) {
    bad_params(a + b, b * a);
}

int main(void) {
    return 0;
}