// Casablanca’s hippodrome is organizing a new type of horse racing: duals.
// During a dual, only two horses will participate in the race. In order for
// the race to be interesting, it is necessary to try to select two horses with
// similar strength.

// Write a program which, using a given number of strengths, identifies the two
// closest strengths and shows their difference with an integer (≥ 0).

 
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main()
{
    unsigned N;
    cin >> N; cin.ignore();
    vector<unsigned> P;
    for (int i = 0; i < N; i++) {
        unsigned Pi;
        cin >> Pi; cin.ignore();
        P.push_back(Pi);
    }
    sort(P.begin(), P.end());
    float best = 1.0/0.0;
    float last = 0;
    for (auto &i: P) {
        best = min(best, i - last);
        last = i;
    }
    cout << best << endl;
}