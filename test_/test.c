

static int o(int a, int b);


int a;


int main(void)
{
    extern int c;

    static int f = 4;
    static int e;
    static int d = c + 4;

    int b = a + 4;
}
