double main(void) {
    sizeof(1);
    (void)10; // you can't negate void expressions, only arithmetic expressions
    1 ? (void)0 : (void)1;
}