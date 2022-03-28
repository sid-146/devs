/*
    ! Exponential Search

*/

#include <iostream>
#include <bits/stdc++.h>
#define HUNDRED 100
#define FIFTEEN 15

using namespace std;

int BinarySearch(int arr[], int n, int low, int high)
{
    int index;
    return index;
}

int exponentialSearch(int arr[], int n, int value)
{

    int indexValue, low = 0, high = n - 1, exp = 1, prevExp = 0;

    while (exp <= n)
    {
        indexValue = BinarySearch(arr, n, low, high);
    }

    return indexValue;
}

int main()
{
    int arr[FIFTEEN];
    srand(time(0));

    // int value = 105;
    int value = HUNDRED;

    for (int i = 1; i < FIFTEEN; i++)
    {
        int random;

        random = rand();
        cout << random << " ";
    }

    if (int ans = exponentialSearch(arr, FIFTEEN, value) == -1)
    {
        cout << "Value not in array" << endl;
    }
    else
    {
        cout << "value at " << ans << " index" << endl;
    }
    return 0;
}