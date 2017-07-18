// The goal for your program is to safely land the "Mars Lander" shuttle, the
// landing ship which contains the Opportunity rover. Mars Lander is guided by
// a program, and right now the failure rate for landing on the NASA simulator
// is unacceptable.

// Note that it may look like a difficult problem, but in reality the problem
// is easy to solve. This puzzle is the first level among three, therefore, we
// need to present you some controls you won't need in order to complete this
// first level.

// For a landing to be successful, the ship must:

//     land on flat ground
//     land in a vertical position (tilt angle = 0°)
//     vertical speed must be limited ( ≤ 40m/s in absolute value)
//     horizontal speed must be limited ( ≤ 20m/s in absolute value)


#include <iostream>
#include <string>
#include <algorithm>

using namespace std;


int main()
{
    unsigned short surfaceN;
    cin >> surfaceN; cin.ignore();
    for (unsigned short i = 0; i < surfaceN; i++) {
        unsigned short landX, landY;
        cin >> landX >> landY; cin.ignore();
    }

    while (1) {
        unsigned short X, Y, fuel, power;
        short hSpeed, vSpeed, rotate;
        cin >> X >> Y >> hSpeed >> vSpeed >> fuel >> rotate >> power; cin.ignore();
        
        cout << "0 " << (vSpeed < -39 ? 4 : 0) << endl;
    }
}