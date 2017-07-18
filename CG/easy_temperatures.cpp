// Write a program that prints the temperature closest to 0 among input data.
// If two numbers are equally close to zero, positive integer has to be
// considered closest to zero (for instance, if the temperatures are -5 and 5,
// then display 5).


#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int n, temp;
    cin >> n; cin.ignore();
    double result = n ? 1.0/0.0 : 0;
    while (n--)
    {
        cin >> temp;
        if (abs(temp) < abs(result) || (abs(temp) == abs(result) && temp > result))
        {
            result = temp;
        }
    }
    cout << result << endl;
}
