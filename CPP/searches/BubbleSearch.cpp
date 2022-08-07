#include <bits/stdc++.h>
#include <iostream>

using namespace std;

// ! under trial trying to return exection time and sorted array

void showArray(int arr[], int sizeOfArray)
{

    cout << "Run showArray " << sizeOfArray << endl;

    for (int i = 0; i < sizeOfArray; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void bubble(int arr[], int sizeOfArray)
{
    cout << "Run bubble " << sizeOfArray << endl;

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

    showArray(arr, sizeOfArray);
}

int main()
{
    int arr[10] = {12, 41, 53, 6, 73, 8, 56, 66, 11, 34};

    int sizeOfArray = sizeof(arr) / sizeof(arr[1]);

    cout << "Run main " << sizeOfArray << endl;

    showArray(arr, sizeOfArray);

    bubble(arr, sizeOfArray);

    return 0;
}