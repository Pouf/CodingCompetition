// At the start of each game turn, you are given the height of the 8 mountains
// from left to right.
// By the end of the game turn, you must fire on the highest mountain by
// outputting its index (from 0 to 7).

// Firing on a mountain will only destroy part of it, reducing its height. Your
// ship descends after each pass.  

 
#include <iostream>

using namespace std;

int main()
{
    while (1)
    {
        unsigned short highest = 0, max_h = 0, h = 0;
        for (unsigned short i = 0; i < 8; i++)
        {
            cin >> h;
            if (h > max_h) {
                max_h = h;
                highest = i;
            }
        }
        cout << highest << endl;
    }
}