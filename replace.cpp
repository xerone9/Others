// C++ program to print all permutations with
// duplicates allowed using rotate() in STL

#include <bits/stdc++.h>
#include <fstream>
#include <windows.h>



using namespace std;

// Function to print permutations of string str,
// out is used to store permutations one by one
void permute(string str, string out)
{
    // When size of str becomes 0, out has a
    // permutation (length of out is n)
    if (str.size() == 0)
    {
        cout << out << endl;
        return;
    }

    // One be one move all characters at
    // the beginning of out (or result)
    for (int i = 0; i < str.size(); i++)
    {
        // Remove first character from str and
        // add it to out
        permute(str.substr(1), out + str[0]);

        // Rotate string in a way second character
        // moves to the beginning.
        rotate(str.begin(), str.begin() + 1, str.end());
    }
}

// Driver code
int main()

{
CONSOLE_FONT_INFOEX cfi;
cfi.cbSize = sizeof(cfi);
cfi.nFont = 0;
cfi.dwFontSize.X = 0;                   // Width of each character in the font
cfi.dwFontSize.Y = 24;                  // Height
cfi.FontFamily = FF_DONTCARE;
cfi.FontWeight = FW_NORMAL;
std::wcscpy(cfi.FaceName, L"monotype"); // Choose your font
SetCurrentConsoleFontEx(GetStdHandle(STD_OUTPUT_HANDLE), FALSE, &cfi);

    char again = 'y';
    while (again == 'y')

    {
    system("color zz");
    string str;
    cout << " " << endl;
    cout << "Enter Word to see possible combinations: ";
    cin >> str;
    transform(str.begin(), str.end(), str.begin(), ::tolower);

    cout << " " << endl;

    ofstream fw;
    fw.open("File1.txt");


    std::streambuf *oldbuf = std::cout.rdbuf(); //save
    std::cout.rdbuf(fw.rdbuf());

    permute(str, ""); // Contents to cout will be written to text.txt

    //reset back to standard input
    std::cout.rdbuf(oldbuf);

    ifstream File1;
    ifstream File2;
    ofstream File3;
    string line,line2;


    File1.open("File1.txt");
    File2.open("File2.txt");
    File3.open("File3.txt");
    if(File1.fail()){ cerr<<"Error opening file !!"<<endl;exit(1);}
    if(File2.fail()){ cerr<<"Error opening file !!"<<endl;exit(1);}

    std::string lineA;
    std::string lineB;
    while (std::getline(File1, lineA))
{
    bool found(false);
    // read File2 until match is found
    while (std::getline(File2, lineB))
    {
        if (lineA == lineB)
        {
            found = true;
            File3 << lineA << " " << std::endl;
            break;
        }
    }

       // clear the state of File2 stream
    File2.clear();
    File2.seekg(0, ios::beg);
}

  cout << " " << endl;
  cout << " " << endl;
  cout << " " << endl;
  cout << "Possible Words " << endl;

  ifstream myfile ("File3.txt");
  if (myfile.is_open())
  {
    while ( myfile.good() )
    {
      getline (myfile,line);
      cout << line << endl;
    }
    myfile.close();
  }

    cout<<"Would You Like to see all combinations (Y/N)";
    char response;
    cin>>response;
    switch (response)

    {
    case 'y': permute(str, "");
    break;
    case 'n':
    break;
    default: cout<<"invalid choice";
    break;
}

    cout << " " << endl;
    cout << " " << endl;
    cout << "Would You Like to try again (Y/N)";
    char response2;
    cin>>response2;
    switch (response2)

{
    case 'y': system("cls"); break;
    case 'n': cout << " " << endl; cout << "SEE YOU LATER" << endl;
    return 0;
    default: cout<<"invalid choice";
    break;
}

   }


    return 0;  //open your out file and enjoy

}
