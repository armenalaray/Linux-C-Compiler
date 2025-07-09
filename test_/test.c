struct c_struct
{
    int a;
    long j;
};


struct b_struct
{
    char c[5];
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
    
    struct a_struct a[4] = 
    {
        {1, {"ale", 2, {3}}},
        {1, {"ale", 2, {3}}}
    };
    

    //char ale[4][4] = {"123"};


    //int b[3] = {1};
}