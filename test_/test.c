struct other
{
    char a[20];
};

struct large_struct
{
    char a[20];
    //struct other b;
};


struct large_struct return_a_struct(void)
{
    struct large_struct callee_result;
    return callee_result;
}



int main(void)
{
    struct large_struct caller_result = return_a_struct();
}