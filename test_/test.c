/* Test returning a pointer from a function */
int *return_pointer(int *in) {
    return in;
}

int main(void) {
    int x = 10;
    long *x_ptr;
    
    //signextend
    x_ptr = 0;

    x_ptr = (long*)&x;

    //*x_ptr;
}