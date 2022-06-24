#include <iostream>
#include <conio.h>

using namespace std;

int main()

{
    char again = 'Y';
    while (again == 'Y' || again == 'y')

    {
    system("color 0a");

    cout << "                  ___________________________________________  " << endl;
    cout << "                 / _____           _       _          _     |  " << endl;
    cout << "                | |  _  |  _   _  | |__   (_)   ___  | | __ |  " << endl;
    cout << "                | | |_) | | | | | | '_ |  | |  / __| | |/ / |  " << endl;
    cout << "                | |  _ <  | |_| | | |_) | | | | (__  |   <  |  " << endl;
    cout << "                | |_| |_| |___,_| |_.__/  |_| |____| |_||_| |  " << endl;
    cout << "                |__________________________________________/  " << endl;
    cout << "                                             " << endl;
    cout << "                                             " << endl;
    cout << "When you are asked to add tax amount in such a manner that even if the tax is deducted you will get your desired amount" << endl;
    cout << "                      " << endl;
    cout << "                      " << endl;
    cout << "Only use numbers (no symbols, no alphabet)" << endl;
    cout << "                      " << endl;
    cout << "                      " << endl;


    float percentage;
    cout << "enter percentage (without symbol): ";
    (cin >> percentage);
    cout << "                      " << endl;

    float amount;
    cout << "enter amount: ";
    (cin >> amount);
    cout << "                      " << endl;


    float result = amount / (100 - percentage) * 100;

    cout << "                      " << endl;
    cout << "========> " << result << " should be the amount if " << percentage << "% is added in " << amount << " <======== " << endl;
    cout << "          *****************************************************" << endl;
    cout << " " << endl;
    cout << " " << endl;
    cout << " " << endl;
    cout << "would you like to make another calculation (Y/N): ";
    char response;
    cin>>response;
    switch(response)
{
    case 'y': system("cls"); break;
    case 'n': return 0;
    default: cout<<"invalid choice";
        }
    }

    return 0;
}
