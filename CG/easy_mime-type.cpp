// You are provided with a table which associates MIME types to file extensions
// You are also given a list of names of files to be transferred and for each
// one of these files, you must find the MIME type to be used.

// The extension of a file is defined as the substring which follows the last
// occurrence, if any, of the dot character within the file name. If the
// extension for a given file can be found in the association table (case
// insensitive, e.g. TXT is treated the same way as txt), then print the
// corresponding MIME type. If it is not possible to find the MIME type
// corresponding to a file, or if the file doesn’t have an extension, print
// UNKNOWN.

 
#include <iostream>
#include <string>
#include <algorithm>
#include <map>

using namespace std;


int main() {
    int N, Q; // N types, Q files
    cin >> N >> Q; cin.ignore();
    map<string, string> TABLE;
    for (int i = 0; i < N; i++) {
        string EXT, MT;
        cin >> EXT >> MT; cin.ignore();
        transform(EXT.begin(), EXT.end(), EXT.begin(), ::tolower);
        TABLE[EXT] = MT;
    }
    for (int i = 0; i < Q; i++) {
        string FNAME, FEXT;
        getline(cin, FNAME);
        unsigned int found = FNAME.rfind('.');
        FEXT = found > FNAME.size() ? "" : FNAME.substr(found+1);
        transform(FEXT.begin(), FEXT.end(), FEXT.begin(), ::tolower);
        if (TABLE[FEXT] == "") {
            cout << "UNKNOWN";
        } else {
            cout << TABLE[FEXT];
        }
        cout << endl;
    }
}