/* Make sure our analysis recognizes which registers are used by each function
 * call - same idea as chapter_20/int_only/no_coalescing/track_arg_registers.c.
 * The test script validates that we don't spill.
 * Liveness analysis should recognize that only XMM0-XMM2 are live right before
 * we call callee(). If we assume XMM3-XMM7 are also live, we'll conclude
 * they're live from the start of the function until the function call
 * (since they're never updated) and won't be able to allocate them, resulting
 * in spills.
 * */

//#include "../util.h"


/* Helper functions defined in tests/chapter_20/helper_libs/util.c */

/* The check_* functions return 0 on success,
 * print and exit with code -1 on failure.
 */

/* Validating ints */

int check_one_int(int actual, int expected);

// Validates a == start, b == start + 1, ...e == start + 5
int check_5_ints(int a, int b, int c, int d, int e, int start);

// Validates a == start, b == start + 1, ... l == start + 11
int check_12_ints(int a, int b, int c, int d, int e, int f, int g, int h, int i,
                  int j, int k, int l, int start);

/* Validating other types */

int check_one_uchar(unsigned char actual, unsigned char expected);
int check_one_uint(unsigned int actual, unsigned int expected);
int check_one_long(long actual, long expected);
int check_one_ulong(unsigned long actual, unsigned long expected);

int check_one_double(double actual, double expected);

int check_12_longs(long a, long b, long c, long d, long e, long f, long g,
                   long h, long i, long j, long k, long l, long start);

int check_six_chars(char a, char b, char c, char d, char e, char f, int start);

// validates a == start, b == start + 1, ... n == start + 13
// and exits early if they don't have those values
// NOTE: assumes a-n are small integral values that can be represented exactly
// as double so no rounding error
int check_14_doubles(double a, double b, double c, double d, double e, double f,
                     double g, double h, double i, double j, double k, double l,
                     double m, double n, double start);

// Used in force_spill_mixed_ints; validates a == start, b == start + 1, ...,
// *k == start + 10, *l == start + 11
int check_12_vals(int a, int b, int c, int d, int e, int f, int g, int h, int i,
                  int j, long *k, double *l, int start);

/* Identity functions that return their argument;
 * used to get constants in a way that can't be optimized away
 */
int id(int x);
double dbl_id(double x);
long long_id(long l);
unsigned unsigned_id(unsigned u);
unsigned char uchar_id(unsigned char uc);


// defined in tests/chapter_20/helper_libs/track_dbl_arg_registers_lib.c,
// exits early if a, b, c don't have expected values
int callee(double a, double b, double c);

double glob1;
double glob2;
double glob3;
double glob4;
double glob5;
double glob6;
double glob7;
double glob8;
double glob9;
double glob10;
double glob11;

// Note: we deliberately give target the same number of params as callee;
// if liveness incorrectly thought that some reg was used by callee and
// therefore live, it still wouldn't interfere with the parameter passed to
// target in that reg, so the error wouldn't necessarily force a spill. (I think
// having _fewer_ params in target than in callee would be be fine.)
int target(double one, double two, double three) {
    double four = three + one;
    double five = two + three;
    double six = three * two;
    double seven = 13. - six;
    double eight = four * two;
    double nine = three * three;
    double ten = five * two;
    double eleven = seven * two - three;
    double twelve = eight * four - 20.;
    double thirteen = (nine + ten) - six;
    double fourteen = eleven + 3;

    // copy variables into global variables to make them interfere
    glob1 = one;
    glob2 = two;
    glob3 = three;
    glob4 = four;
    glob5 = five;
    glob6 = six;
    glob7 = seven;
    glob8 = eight;
    glob9 = nine;
    glob10 = ten;
    glob11 = eleven;

    // don't need to copy in twelve through fourteen b/c we use them below

    // use ten through twelve
    callee(twelve, thirteen, fourteen);

    // validate globals
    check_14_doubles(glob1, glob2, glob3, glob4, glob5, glob6, glob7, glob8,
                     glob9, glob10, glob11, 12., 13., 14., 1);

    return 0;
}
