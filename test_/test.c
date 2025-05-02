int main(void) {
    int a = 0;

    while (a < 5)
    {
        if (a > 3)
        {
            break;
        }
        
        continue;
        a = a + 2;
    }

    return a;
}
