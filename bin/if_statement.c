
int main(void)
{
    int a = 0;

    while (a < 5)
        if (a > 3)
        {

            break;
            do
            {
                if (a > 4)
                {
                    int a = 2 + 3;
                    
                    // int a = 12345;
                    int i;
                    
                    for (i = 5; i >= 0; i = i - 1)
                    {
                        continue;
                        a = a / 3;
                    }
                    
                    return a;
                }
                break;
            } while ((a = 1));
            return a;
        }
        else
            continue;
}




int main(void) {
    int a = 10;
    do
    {
        if(a > 4)
        {
            break;
        }
    }
    while ((a = 1));
    return a;
}










int main(void) {
    int a = 0;

    while (a < 5)
    {
        if (a > 3)
        {
            break;
        }
        
        a = a + 2;
    }

    return a;
}






int main(void) {
    int a = 0;
    a = 1 ? 2 : 3;
    
    if (a)
        a = 2;
    else
        a = 3;

    return a;
}


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

int main(void)
{
    int FocusDistance;
    int HalfWidth;
    int HalfHeight;
    int LookFrom;
    int u;
    int v;
    int w;
    int Origin = LookFrom;

    if (Origin > LookFrom)
    {
        int LowerLeftCorner = (Origin - (HalfWidth * FocusDistance * u) - (HalfHeight * FocusDistance * v) - w * FocusDistance);
    }
    else
    {
        int Horizontal = 2 * HalfWidth * FocusDistance * u;
        int Vertical = 2 * HalfHeight * FocusDistance * v;
    }
}
