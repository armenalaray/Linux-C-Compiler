int get_input(void);

int process_input(int input);

int main(void)
{
    int done = 0;
    do
    {
        /* code */
        int input = get_input();
        if(input == 0)
        {
            return -1;
        }

        int done = process_input(input);

    } while (done);
    
}