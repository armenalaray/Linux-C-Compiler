#ifdef SUPPRESS_WARNINGS
#ifndef __clang__
#pragma GCC diagnostic ignored "-Wparentheses"
#endif
#endif
int main(void) {
    return ((2+1) > (1 - 2) ) || (2 != 3);
}