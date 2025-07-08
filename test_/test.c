struct c_struct
{
    int a;
    long j;
};


struct b_struct
{
    char c;
    int i;
    struct c_struct a;
};

struct a_struct
{
    int member1;
    struct b_struct member2;
};

struct a_struct foo(void)
{
    struct a_struct a;
    return a;
}

int main(void)
{
    struct a_struct * a;
    (*a).member1;
}