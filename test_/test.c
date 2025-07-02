int main(void)
{
    struct shadow
    {
        int x;
    };

    struct shadow outer;
    outer.x = 2;
    {
        struct shadow
        {
            int y;
        };
        struct shadow inner;
        inner.y = 3;
        return outer->x + inner.y;
    }
}