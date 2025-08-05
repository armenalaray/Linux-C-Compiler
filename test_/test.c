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


int glob = 3;
double glob2 = 4.0;

int target(void) {
    /* force spill by creating lots of conflicting pseudos
     * validate that we spill the variable should_spill, which is used least
     * and has highest degree
     * Note: this isn't a good test of spill metric calculation;
     * due to optimistic coloring, we could end up spilling just should_spill
     * even if we end up choosing other nodes as spill candidates first
     */
    double should_spill = (double)glob;
    // all these registers conflict with should_spill and each other
    double one = 4.0 - glob;
    double two = one + one;
    double three = (double)glob;
    double four = two * two;
    double five = glob2 + 1;
    double six = glob * 2;
    double seven = one * one + 6.0;
    double eight = two * 4;
    double nine = three * three;
    double ten = four + six;
    double eleven = 16 - five;
    double twelve = six + six;
    double thirteen = five + eight;
    double fourteen = 21 - seven;

    // validate them
    check_14_doubles(one, two, three, four, five, six, seven, eight, nine, ten,
                     eleven, twelve, thirteen, fourteen, 1.0);

    // make another fourteen pseudos that conflict w/ should_spill and each
    // other
    double fifteen = glob2 * 4.0 - 1;
    double sixteen = glob2 * 4.0;
    double seventeen = fifteen + 2.0;
    double eighteen = 35.0 - seventeen;
    double nineteen = sixteen + glob;
    double twenty = glob2 * 5.0;
    double twenty_one = glob * 7.0;
    double twenty_two = 4.0 + eighteen;
    double twenty_three = nineteen + glob + 1;
    double twenty_four = glob2 + twenty;
    double twenty_five = twenty_one + glob2;
    double twenty_six = twenty_five - nineteen + twenty;
    double twenty_seven = glob * 9.0;
    double twenty_eight = twenty_two + 6;
    check_14_doubles(fifteen, sixteen, seventeen, eighteen, nineteen, twenty,
                     twenty_one, twenty_two, twenty_three, twenty_four,
                     twenty_five, twenty_six, twenty_seven, twenty_eight, 15.0);

    if (should_spill != 3.0) {
        return -1;
    }

    return 0;
}
