/* Test truncating wider to narrow types */
int ulong_to_int(unsigned long ul, int expected) {
    int result = (int) ul;
    return (result == expected);
}

int ulong_to_uint(unsigned long ul, unsigned expected) {
    return ((unsigned int) ul == expected);
}


