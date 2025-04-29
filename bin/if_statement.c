int main(void) {
    int a = 0;
    a = 1 ? 2 : 3;
    
    if (a)
        a = 2;
    else
        a = 3;

    return a;
}