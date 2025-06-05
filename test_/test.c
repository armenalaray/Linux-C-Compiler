/* Test out parsing a range of abstract declarators */
int main(void) {
    (int (****(***(**(*)[2])[4])[6]))other_ptr == ptr_arr;
}