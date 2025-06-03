/* Test returning a pointer from a function */
int *return_pointer(int *in) {
    return in;
}

int main(void) {
    int b = 2;
    int * a = 0;
    
    a = &b;
    *a = 2;

    b = *a;
}