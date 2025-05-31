int main(void)
{
    //this is an array of pointers
    //int *(arr[3]);

    //this is a pointer to an array
    //int (*arr)[3];


    int *null_ptr = 0;
    int *ptr2 = &*null_ptr;


    int *ptr = &var;
    int *ptr2 = &*ptr;


    double negative_zero = -0.0;
    double *d = &negative_zero;
    unsigned long *l = (unsigned long *)d;

    int x = 0;
    int *ptr = x;

    //int *ptr2 = (int *)0x7ffeee67b938;

    int *null = -1;

    double b = *null;

    int x = 0;

    // 0x7ffeee67b938
    // 0x7ffeee67b938
    int *ptr = &x;

    *ptr = 4;

    return *ptr;
}