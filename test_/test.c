struct first
{
    char d[21];
};

struct two_eightbytes
{
    char d[21];
    struct first a;
};

int main(void)
{
    struct two_eightbytes b;
    struct first a;
    b.a = a;
}