// ASCII art allows you to represent forms by using characters. To be precise,
// in our case, these forms are words. For example, the word "MANHATTAN" could
// be displayed as follows in ASCII art:
 
// # #  #  ### # #  #  ### ###  #  ###
// ### # # # # # # # #  #   #  # # # #
// ### ### # # ### ###  #   #  ### # #
// # # # # # # # # # #  #   #  # # # #
// # # # # # # # # # #  #   #  # # # #
 
// ​Your mission is to write a program that can display a line of text in ASCII
// art in a style you are given as input.


 
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int L, H;
    cin >> L >> H; cin.ignore();
    string T;
    getline(cin, T);
    for (int i = 0; i < H; i++) {
        string ROW;
        getline(cin, ROW);
        for (auto &c: T) {
            int index = isalpha(c) ? toupper(c) - 'A' : 26;
            cout << ROW.substr(index * L, L);
        }
        cout << endl;
    }
    
}


