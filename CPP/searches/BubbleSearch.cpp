#include <bits/stdc++.h>
#include <iostream>

using namespace std;

// ! under trial trying to return exection time and sorted array

// struct ANSWER
// {
//     int time;
//     int arr;
// };



int bubble(int arr[])
{
    int sizeOfArray = sizeof(arr) / sizeof(arr[0]);

    for (int i = 0; i < sizeOfArray; i++)
    {
        for (int j = 0; j = sizeOfArray - i - 1; j++)
        {
            if (arr[j] >= arr[j + 1])
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    return arr;
}

int main()
{
    int arr[10] = {12, 41, 53, 6, 73, 8, 56, 66, 11, 34};

    int *SortedArr = bubble(arr);

    int sizeOfArray = sizeof(arr) / sizeof(arr[0]);
    cout << sizeOfArray << endl;

    for (int i = 0; i < sizeOfArray; i++)
    {
        cout << SortedArr[i] << " ";
    }

    return 0;
}
