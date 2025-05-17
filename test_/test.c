// int static sign_extend(int i, long expected);

int a;
int a;

long static sign_extend(int i, long expected)
{

    long extended = (long)i;
    extended = i > 4 ? 3 : 2;
    return (extended && expected);
}

// tentatives
extern long r;
extern int q;

// se cambia este
extern int i = 2147483648L;
extern long j = 2147483648L;

extern int k = 2147483647;
extern long p = 2147483647;

int main(void)
{
    static long r;
    static int q;

    static int i = 2147483648;
    static long j = 2147483648;

    static int k = 2147483647;
    static long p = 2147483647;

    while (1)
    {
        break;
    }

    do
    {
        continue;
        /* code */
    } while (1);

    for (;;)
    {
        /* Converting a positive or negative int to a long preserves its value */
        if (!sign_extend(10, 10l))
        {
            return 1;
        }

        if (!sign_extend(-10, a > 4 ? 3 : 2))
        {
            return 2;
        }

        /* sign-extend a constant to make sure we've implemented rewrite rule for movsx correctly */
        long l = (long)100;
        if (l != 100l)
        {
            return 3;
        }
    }

    return 0;
}