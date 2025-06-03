/* Test returning a pointer from a function */
int *return_pointer(int *in) {
    return in;
}

int main(void) {
    
    for (int* a = 0; a != 0;)
    {
        a = return_pointer(a);
        if (a == 0) {
            break; // Prevent infinite loop
        }
    }
}