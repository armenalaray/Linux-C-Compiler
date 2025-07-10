struct other
{
    int b;
};

struct large_struct
{
    char array[2];
    struct other a;
};

struct large_struct return_a_struct(struct large_struct i)
{
    return i;
}


int main(void)
{
    struct large_struct callee_result;

    struct large_struct caller_result = return_a_struct(callee_result);
}