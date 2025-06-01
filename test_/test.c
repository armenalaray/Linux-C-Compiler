/* Test returning a pointer from a function */
int *return_pointer(int *in) {
    static double ale = 2.0;
    return &ale;
}

int main(void) {

    int x = 10UL;

    double *x_ptr = return_pointer(&x);

    if (*x_ptr != 10)
        return 1;

    x = 100;
    if (*x_ptr != 100)
        return 2;

    if (x_ptr != &x)
        return 3;

    return 0;
}