/*
    ! Exponential Search

*/

#include <iostream>
#include <bits/stdc++.h>
#include <tuple>

using namespace std;

int exponentialSearch(int arr[], int n, int value)
{

    int indexValue, low = 0, high = n - 1, exp = 1, prevExp = 0;

    if (arr[low] == low)
    {
        return low;
    }
    if (arr[exp] > value)
    {
        low =
    }

    indexValue = BinarySearch(arr, n, low, high);

    return indexValue;
}

int BinarySearch(int arr[], int n, int low, int high)
{
    int index;
    return index;
}

int main()
{
    int n = 10;
    int arr[10];

    // int value = 105;
    int value = 100;

    for (int i = 1; i < n; i++)
    {
        arr[i] = i * 15;
    }

    if (int ans = exponentialSearch(arr, n, value) == -1)
    {
        cout << "Value not in array" << endl;
    }
    else
    {
        cout << "value at " << ans << " index" << endl;
    }
    return 0;
}