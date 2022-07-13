#include <iostream>
#include <time.h>

using namespace std;

//? Created this for returing 2 values for single function
struct Values
{
    int MinValue;
    int MaxValue;
};

Values getMinMax(int len, int arr[])
{
    struct Values MinMax;
    if (len == 0)
    {
        MinMax.MaxValue = arr[0];
        MinMax.MinValue = arr[0];

        return MinMax;
    }

    for (int i = 0; i < len; i++)
    {
    }

    return MinMax;
}

int main()
{
    return 0;
}