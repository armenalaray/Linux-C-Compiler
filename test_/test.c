struct two_eightbytes
{
    char d[21];
};

struct two_eightbytes foo(struct two_eightbytes a)
{
    return a;
}

int main(void)
{
    struct two_eightbytes * b;
    struct two_eightbytes a = foo(*b);


}