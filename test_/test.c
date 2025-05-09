/* A variable with internal linkage may be tentatively defined
 * and declared multiple times, but defined only once
 */

/* A tentative definition */
extern int foo(void);

int main(void) {
    
    extern int a(void);

    for(int extern a(void){};;)
    {

    }

    return foo;
}

/* A declaration */
extern int foo;

/* A non-tentative definition */
static int foo = 4;