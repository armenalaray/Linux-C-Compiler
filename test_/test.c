struct ale
{
    int a;
};

int main(void)
{
    static struct ale a = {2};
    int y = a.a;
    int * x = &y;
    *x = 4;
    return *x;
}