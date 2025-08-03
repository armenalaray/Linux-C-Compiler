/* Test that liveness analysis for registers handles loop correctly */

//#include "../util.h"


/* Helper functions defined in tests/chapter_20/helper_libs/util.c */

/* The check_* functions return 0 on success,
 * print and exit with code -1 on failure.
 */

int check_one_int(int actual, int expected);

// Validates a == start, b == start + 1, ...e == start + 5
int check_5_ints(int a, int b, int c, int d, int e, int start);

// Validates a == start, b == start + 1, ... l == start + 11
int check_12_ints(int a, int b, int c, int d, int e, int f, int g, int h, int i,
                  int j, int k, int l, int start);

// return x; used to get constants in a way that can't be optimized away
int id(int x);


int counter = 5;
int expected_a = 2;

int update_expected_a(void);
int times_two(int x);

int target(void) {
    int z;
    int a;

    // define four callee-saved regs
    int one = counter - 4;
    int two = counter / 2;
    int three = -counter + 8;
    int four = counter - 1;

    // a and z are both callee-saved but their live ranges don't overlap;
    // we can avoid spills by placing them in the same hard register
    while (counter > 0) {
        if (counter == 5)
            z = 4; // a not yet initialized
        else
            z = times_two(a);
        // z is live, a is dead below here
        update_expected_a(); // force z to be callee-saved
        a = 1 - z; // a is live, z is dead from here to start of loop
        check_one_int(a, expected_a);
        counter = counter - 1;
    }

    // validate other callee-saved regs
    check_one_int(one, 1);
    check_one_int(two, 2);
    check_one_int(three, 3);
    check_one_int(four, 4);
    return 0;
}

// independently calculate a's value on each loop iteration so we can validate it
int update_expected_a(void) {
    expected_a = 1 - (2 * expected_a);
    return 0;
}

int times_two(int x) {
    return x * 2;
}
