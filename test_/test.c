int fun(int a, int b, int c, int d, int e, int f, int g, int h) {
    return a + h;
   }
   int caller(int arg) {
    int a;
    int b;
    int c;
    int d;
    return arg + fun(a, b, c, d, 5, 6, 7, 8);
   }