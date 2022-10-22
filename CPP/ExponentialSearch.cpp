/*
    ! Exponential Search
    ? example
*/

#include <iostream>
#include <bits/stdc++.h>
#define VALUE 100
#define FIFTEEN 15

using namespace std;

int BinarySearch(int arr[], int n, int low, int high)
{
    int index;
    
    return index;
}

int exponentialSearch(int arr[], int n, int value)
{
    int sizeOfArray = sizeof(arr) / sizeof(arr[0]);
    int indexValue, low = 0, high = n - 1, exp = 1, prevExp = 0;

    while (exp <= n)
    {
        exp *= 2;
        indexValue = BinarySearch(arr, n, exp/2, exp);
    }

    return indexValue;
}

int main()
{
    int arr[FIFTEEN];
    srand(time(0));

    // int value = 105;
    int value = VALUE;

    for (int i = 1; i < FIFTEEN; i++)
    {
        int random;
        random = rand();
        arr[i] = random;
    }

    for (int i = 0; i < FIFTEEN; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;

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