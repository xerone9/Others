#include <iostream>

using namespace std;

int main()
{
    char again = 'y';
    while (again == 'y')

    {
    system("color FC");
    cout << ".___            .___              ____ ___      .__                          .__  __          " << endl;
    cout << "|   | ____    __| _/_ __  ______ |    |   \\____ |__|__  __ ___________  _____|__|/  |_ ___.__." << endl;
    cout << "|   |/    \\  / __ |  |  \\/  ___/ |    |   /    \\|  \\  \\/ // __ \\_  __ \\/  ___/  \\   __<   |  |" << endl;
    cout << "|   |   |  \\/ /_/ |  |  /\\___ \\  |    |  /   |  \\  |\\   /\\  ___/|  | \\/\\___ \\|  ||  |  \\___  |" << endl;
    cout << "|___|___|  /\\____ |____//____  > |______/|___|  /__| \\_/  \\___  >__|  /____  >__||__|  / ____|" << endl;
    cout << "         \\/      \\/          \\/               \\/              \\/           \\/          \\/     " << endl;
    cout << "" << endl;
    cout << "===============================================================================================" << endl;
    cout << "" << endl;
    cout << "" << endl;
    cout << "" << endl;


    float Salary;
    cout << "   Salary: ";
    cin >> Salary;

    cout << "" << endl;
    float DeductiveHours;
    cout << "   Deductive Hours; ";
    cin >> DeductiveHours;

    cout << "" << endl;
    float OvertimeExtra;
    cout << "   Over Time + Extra: ";
    cin >> OvertimeExtra;

    cout << "" << endl;
    float Loan;
    cout << "   Any Loan Deductions; ";
    cin >> Loan;

    cout << "" << endl;
    float Absent;
    cout << "   Any Absent Days: ";
    cin >> Absent;

    float SalaryC1;
    SalaryC1 = Salary*12/365*OvertimeExtra;

    float SalaryC2;
    SalaryC2 = Salary*12/3650*DeductiveHours;

    float SalaryC3;
    SalaryC3 = Salary*12/365*Absent;

    float SalaryF;
    SalaryF = SalaryC1-SalaryC2+Salary-Loan-SalaryC3;


    cout << "" << endl;
    cout << "" << endl;
    cout << "" << endl;
    cout << "   -------> Your Salary would be: " << SalaryF << " <-------" << endl;
    cout << "            `````````````````````````````";


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
