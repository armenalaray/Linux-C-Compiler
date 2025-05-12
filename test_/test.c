/* Verify that if variable is tentatively defined one or more times,
 * but not explicitly initialized, we'll initialize it to 0.
 */

/* This declares foo but does not define it */
extern int foo = 2;

/* A tentative definition of foo */
int foo;

/* Another tentative definition of foo */
int foo;

int main(void) {
    extern int b;
    
    for (int i = 0; i < 5; i = i + 1)
    {   
        static int a = 2 + b;
        foo = a + 1;
    }
    return foo;
}

/* Yet another tentative definition of foo */
int foo;