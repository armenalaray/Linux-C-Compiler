struct s;

int main(void) {
    extern struct s my_incomplete_struct;
    struct s *ptr = &my_incomplete_struct;   
}