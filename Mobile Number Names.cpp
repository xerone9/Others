#include <iostream>
#include <string>
#include <algorithm>


using namespace std;

void findAndReplaceAll(std::string & data, std::string toSearch, std::string replaceStr)
{
	// Get the first occurrence
	size_t pos = data.find(toSearch);

	// Repeat till end is reached
	while( pos != std::string::npos)
	{
		// Replace this occurrence of Sub String
		data.replace(pos, toSearch.size(), replaceStr);
		// Get the next occurrence from the current position
		pos =data.find(toSearch, pos + replaceStr.size());
	}
}

void findAndReplaceNo(std::string & data1, std::string toSearch, std::string replaceStr)
{
	// Get the first occurrence
	size_t pos = data1.find(toSearch);

	// Repeat till end is reached
	while( pos != std::string::npos)
	{
		// Replace this occurrence of Sub String
		data1.replace(pos, toSearch.size(), replaceStr);
		// Get the next occurrence from the current position
		pos =data1.find(toSearch, pos + replaceStr.size());
	}
}




int main()

{

    char again = 'y';
    while (again == 'y')



{
    cout << "1: Word To Mobile Number" << endl;
    cout << "2: Mobile Number To Word" << endl;
    cout << " " << endl;
    cout << "Choice: ";
    int choice;
    cin >> choice;

    if (choice == 1)
{

    cout << " " << endl;
    std::string data;
    cout << "Enter Word: ";
    cin >> data;
    transform(data.begin(), data.end(), data.begin(), ::tolower);



	findAndReplaceAll(data, "a", "2");
	findAndReplaceAll(data, "b", "2");
	findAndReplaceAll(data, "c", "2");
	findAndReplaceAll(data, "d", "3");
	findAndReplaceAll(data, "e", "3");
	findAndReplaceAll(data, "f", "3");
	findAndReplaceAll(data, "g", "4");
	findAndReplaceAll(data, "h", "4");
	findAndReplaceAll(data, "i", "4");
	findAndReplaceAll(data, "j", "5");
	findAndReplaceAll(data, "k", "5");
	findAndReplaceAll(data, "l", "5");
	findAndReplaceAll(data, "m", "6");
	findAndReplaceAll(data, "n", "6");
	findAndReplaceAll(data, "o", "6");
	findAndReplaceAll(data, "p", "7");
	findAndReplaceAll(data, "q", "7");
	findAndReplaceAll(data, "r", "7");
	findAndReplaceAll(data, "s", "7");
	findAndReplaceAll(data, "t", "8");
	findAndReplaceAll(data, "u", "8");
	findAndReplaceAll(data, "v", "8");
	findAndReplaceAll(data, "w", "9");
	findAndReplaceAll(data, "x", "9");
	findAndReplaceAll(data, "y", "9");
	findAndReplaceAll(data, "z", "9");
	findAndReplaceAll(data, " ", "0");
	findAndReplaceAll(data, ".", "1");

    cout << " " << endl;
	std::cout<< ">>>> Mobile Number Should Contain these numbers: "<<data << " <<<<" << std::endl;
	cout << "" << endl;
	cout << "========================================================================" << endl;
	cout << "" << endl;
    cout << "" << endl;
    cout << "" << endl;

 }
else if (choice == 2)
{
    cout << " " << endl;
    std::string data1;
    cout << "Enter Number: ";
    cin >> data1;

	findAndReplaceNo(data1, "2", "a");
	findAndReplaceNo(data1, "2", "b");
	findAndReplaceNo(data1, "2", "c");
	findAndReplaceNo(data1, "3", "d");
	findAndReplaceNo(data1, "3", "e");
	findAndReplaceNo(data1, "3", "f");
	findAndReplaceNo(data1, "4", "g");
	findAndReplaceNo(data1, "4", "h");
	findAndReplaceNo(data1, "4", "i");
	findAndReplaceNo(data1, "5", "j");
	findAndReplaceNo(data1, "5", "k");
	findAndReplaceNo(data1, "5", "l");
	findAndReplaceNo(data1, "6", "m");
	findAndReplaceNo(data1, "6", "n");
	findAndReplaceNo(data1, "6", "o");
	findAndReplaceNo(data1, "7", "p");
	findAndReplaceNo(data1, "7", "q");
	findAndReplaceNo(data1, "7", "r");
	findAndReplaceNo(data1, "7", "s");
	findAndReplaceNo(data1, "8", "t");
	findAndReplaceNo(data1, "8", "u");
	findAndReplaceNo(data1, "8", "v");
	findAndReplaceNo(data1, "9", "w");
	findAndReplaceNo(data1, "9", "x");
	findAndReplaceNo(data1, "9", "y");
	findAndReplaceNo(data1, "9", "z");
	findAndReplaceNo(data1, "0", " ");

    cout << " " << endl;
	std::cout<< ">>>> Mobile Number Should Contain these numbers: "<<data1<< " <<<<" << std::endl;
	cout << "" << endl;
	cout << "========================================================================" << endl;
	cout << "" << endl;
    cout << "" << endl;
    cout << "" << endl;

}

else {
    cout << "XXXXX Invalid Choice XXXXX" << endl;
    cout << "========================================================================" << endl;
    cout << "" << endl;
    cout << "" << endl;
    cout << "" << endl;
}

        }
	return 0;
}

