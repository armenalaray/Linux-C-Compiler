/* Test truncating wider to narrow types */
int ulong_to_int(unsigned long ul, int expected) {
    unsigned long result = ul + 4UL;
    return (result == expected);
}

int ulong_to_uint(unsigned long ul, unsigned expected) {
    return (ul == expected);
}

int long_to_uint(long l, unsigned int expected) {
    return l == expected;
}

