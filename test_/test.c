/* Test that we can use strings literals as function arguments/return values */

#ifdef SUPPRESS_WARNINGS
#ifdef __clang__
#pragma clang diagnostic ignored "-Wincompatible-library-redeclaration"
#else
#pragma GCC diagnostic ignored "-Wbuiltin-declaration-mismatch"
#endif
#endif

unsigned long strlen(char *s);

char *return_string(void) {
    // constant strings have static storage duration,
    // so this will persist after the function call;
    return "I'm a string!";
}

