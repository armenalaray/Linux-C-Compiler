/* Test returning a pointer from a function */
int *return_pointer(int *in) {
    return in;
}

int main(void) {
    int x = 10;
    long *x_ptr = (long*)return_pointer(&x);
    return 0;
}