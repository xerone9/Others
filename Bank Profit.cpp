#include <iostream>

using namespace std;

int main()
{
    char again = 'y';
    while (again == 'y')

    {
    system("color FC");
    cout << ".___            .___              " << endl;
    cout << "|   | ____    __| _/_ __  ______ " << endl;
    cout << "|   |/    \\  / __ |  |  \\/  ___/ " << endl;
    cout << "|   |   |  \\/ /_/ |  |  /\\___ \\  " << endl;
    cout << "|___|___|  /\\____ |____//____  > " << endl;
    cout << "         \\/      \\/          \\/" << endl;
    cout << "" << endl;
    cout << " ____ ___      .__                          .__  __          " << endl;
    cout << "|    |   \\____ |__|__  __ ___________  _____|__|/  |_ ___.__." << endl;
    cout << "|    |   /    \\|  \\  \\/ // __ \\_  __ \\/  ___/  \\   __<   |  |" << endl;
    cout << "|    |  /   |  \\  |\\   /\\  ___/|  | \\/\\___ \\|  ||  |  \\___  |" << endl;
    cout << "|______/|___|  /__| \\_/  \\___  >__|  /____  >__||__|  / ____|" << endl;
    cout << "             \\/              \\/           \\/          \\/     " << endl;
    cout << "" << endl;
    cout << "===================================================================" << endl;
    cout << "" << endl;
    cout << "" << endl;



    float TDR;
    cout << "   TDR Amount: ";
    cin >> TDR;

    cout << "" << endl;
    float Profit;
    cout << "   Enter Profit Percentage; ";
    cin >> Profit;

    cout << "" << endl;
    float Month;
    cout << "   Enter Value for How Many Months The TDR is Booked: ";
    cin >> Month;
    float Months = Month*30.41666666666667;

    cout << "" << endl;
    float Year;
    cout << "   Enter Value for How Many Years The TDR is Booked: ";
    cin >> Year;
    float Years = Year*365;

    float Calculation;
    Calculation = TDR*Profit/365/100;


    cout << "" << endl;
    cout << "" << endl;
    cout << "" << endl;
    cout << "  Months" << endl;
    cout << "''''''''" << endl;
    cout << "   -------> For " << Month << " Months Profit Will be: " << Calculation*Months << " <-------" << endl;
    cout << "            `````````````````````````````````" << endl;
    cout << "" << endl;
    cout << "" << endl;
    cout << "  Years" << endl;
    cout << "''''''''" << endl;
    cout << "   -------> For " << Year << " Years Profit Will be: " << Calculation*Years << " <-------" << endl;
    cout << "            `````````````````````````````````" << endl;
    cout << "" << endl;
    cout << "" << endl;
    cout << "" << endl;
    cout << "" << endl;
    cout << "   -------> Per day Profit Will be: " << Calculation << " <-------" << endl;
    cout << "            `````````````````````````````````" << endl;
    cout << "   -------> Per Month Profit Will be: " << Calculation*30 << " <-------" << endl;
    cout << "            ``````````````````````````````````" << endl;
    cout << "   -------> Per Year Profit Will be: " << Calculation*365 << " <-------" << endl;
    cout << "            ``````````````````````````````````" << endl;




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
   return 0;
}
