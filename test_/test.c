long sign_extend(int i, long expected, int j, int p, int k, int h, int l) {
    long extended = (long) i;
    return (extended == expected);
}


int main(void) {
    /* Converting a positive or negative int to a long preserves its value */
    if (!sign_extend(10, 10l, 4, 3, 4, 1, 0)) {
        return 1;
    }

    return 0;
}