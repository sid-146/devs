#include <iostream>
#include <time.h>

using namespace std;

//? Created this for returing 2 values for single function
struct Values
{
    int MinValue;
    int MaxValue;
};

// create a struct type return type
Values getMinMax(int len, int arr[])
{
    struct Values MinMax;
    //! assigning default values to the min and max values

    MinMax.MaxValue = 0;
    MinMax.MinValue = 10000000;

    if (len == 0)
    {
        MinMax.MaxValue = arr[0];
        MinMax.MinValue = arr[0];

        return MinMax;
    }

    for (int i = 0; i < len; i++)
    {
        if (MinMax.MaxValue <= arr[i])
        {
            MinMax.MaxValue = arr[i];
        }

        if (MinMax.MinValue >= arr[i])
        {
            MinMax.MinValue = arr[i];
        }
    }

    return MinMax;
}

int main()
{
    return 0;
}