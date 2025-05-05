/* Variable initializers aren't permitted in parameter lists */
int a(void) {
    for(int i;;)
    {

    }
}

int main(void) {
    int a(int a);
}