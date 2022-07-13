// C++ program to find the sum of two
// numbers using function declared in
// header file
#include "iostream"

// Including header file
#include <randint.h>
using namespace std;

// check code to run for the custom header file
// Driver Code
int main()
{

    // Given two numbers
    int a = 13, b = 22;

    // Function declared in header
    // file to find the sum
    cout << "Sum is: "
         << sumOfTwoNumbers(a, b)
         << endl;
}
