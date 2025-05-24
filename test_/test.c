/* Can't declare the same function with two return types: unsignd int and unsigned long */
unsigned int foo(long a);

unsigned int foo(int a) {
    return 0;
}

int main(void) {
    return 0;
}