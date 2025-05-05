int foo(int a, int b);

int main(void)
{
    int c = foo(1,2);

    c = 2;
}

int foo(int a, int b)
{
    return a + b;
}