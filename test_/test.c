
int main(void) {
    extern int arr[6];
    extern int arr[5];

    return arr[0];
}

// it's illegal to redeclare arr as a different type