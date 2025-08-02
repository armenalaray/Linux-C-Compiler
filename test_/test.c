/* Test case in a program with a mix of integer and floating-point
 * pseudoregisters; make sure we can allocate all of them.
 * Test script validates that there are no spills.
 */


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


int target(int one, int two, double one_d, double two_d, int three,
           double three_d) {
    // Define ints 4-8 (all callee-saved) and doubles 10-23 and validate them
    long four = two * two;
    long five = three + two_d;

    double ten_d = three * two_d + four;
    double eleven_d = ten_d + one;

    long six = three * two_d;
    long seven = four + 3;

    double twelve_d = six * two_d;
    double thirteen_d = 14.0 - one_d;
    double fourteen_d = seven * two;
    double fifteen_d = twelve_d + three;
    double sixteen_d = four * four;
    double seventeen_d = ten_d + seven;
    double eighteen_d = three_d * six;

    unsigned long eight = four * two;

    double nineteen_d = 20 - one;
    double twenty_d = four * five;
    double twenty_one_d = three * 7;
    double twenty_two_d = eleven_d * 2;
    double twenty_three_d = ten_d + thirteen_d;

    check_14_doubles(ten_d, eleven_d, twelve_d, thirteen_d, fourteen_d,
                     fifteen_d, sixteen_d, seventeen_d, eighteen_d, nineteen_d,
                     twenty_d, twenty_one_d, twenty_two_d, twenty_three_d,
                     10.0);
    check_5_ints(four, five, six, seven, eight, 4);
    return 0;
}