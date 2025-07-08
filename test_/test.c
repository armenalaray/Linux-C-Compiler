/* A non-lvalue structure that contains an array has temporary lifetime;
 * test that you can get this array's address implicitly (even though
 * you can't load it explicitly)
 * Adapted from Listing 18-27
 * */

struct s {
    char arr[3];
    long a;
    int c;
};

int main(void)
{
    struct s a;

    a.a = 0;
}