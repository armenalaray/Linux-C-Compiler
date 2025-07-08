struct c_struct
{
    int ale;
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

int main(void)
{
    struct a_struct a;
    a.member2.a.ale;
}