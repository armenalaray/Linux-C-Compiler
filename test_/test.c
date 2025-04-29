int main(void) {
    int x = 2;
    int y = 7;
    int radius = 0;

    int leng_sq = x*x + y*y;

    if (leng_sq > 0)
        radius = 10;
    else if(leng_sq < 0)
        radius = -10;   
    else if(leng_sq == 0)
        radius = 0;
    else 
        radius = 50;

    int channel = 4;
    int case = 2;
    
    if (channel || case)
        return radius > 10 ? 4 : 5;
    else 
        return case > 2 ? 4 : 5;
}