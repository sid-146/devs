#include <bits/stdc++.h>
#include <iostream>

using namespace std;

// ! try to automate process for range of the array values like 10 to 10k or more
// ! calculate time taken to compute that

/*
* hint use file handling to store data CSV and generate array len

*/

struct timeTaken
{
    int startTime;
    int endTime;
    int TAT;
    int sortStartTime;
    int sortEndTime;

};



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

        for (int j = 0; j < sizeOfArray - i - 1; j++)
        {
            if (arr[j] >= arr[j + 1])
            {
                swap(arr[j], arr[j + 1]);
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