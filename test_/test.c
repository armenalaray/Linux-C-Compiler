struct two_eightbytes
{
    double d;
    char c;
};

struct two_eightbytes foo(void)
{
    struct two_eightbytes a;
    return a;
}

int main(void)
{
    return foo().d;
}