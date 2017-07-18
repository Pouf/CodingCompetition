// Thor moves on a map which is 40 wide by 18 high. Note that the coordinates
// (X and Y) start at the top left! This means the most top left cell has the
// coordinates "X=0,Y=0" and the most bottom right one has the coordinates
// "X=39,Y=17".

// Once the program starts you are given:

// - lightX: the X position of the light of power that Thor must reach.
// - lightY: the Y position of the light of power that Thor must reach.
// - initialTX: the starting X position of Thor.
// - initialTY: the starting Y position of Thor.

 
#include <iostream>
using namespace std;

int main()
{
    int lightX, lightY, ThorX, ThorY;
    cin >> lightX >> lightY >> ThorX >> ThorY; cin.ignore();

    while (1) {
        if (lightY > ThorY) {
            cout << 'S';
            ThorY++;
        } else if (lightY < ThorY) {
            cout << 'N';
            ThorY--;
        }
        if (lightX > ThorX) {
            cout << 'E';
            ThorX++;
        } else if (lightX < ThorX) {
            cout << 'W';
            ThorX--;
        }
        cout << endl;
    }
}