struct s
{
    int member;
    int arr[3];
};

struct s f(void);

int main(void)
{
    int *arr_pointer = f().arr;
    return arr_pointer[0];
}