#include <iostream>
#include <conio.h>
#include <stdio.h>

using namespace std;

int main()
{
    char again = 'Y';

    while (again == 'Y' || again == 'y')



    {
     system("color f3");
    cout << "                      __    _    __     _    _  __   ___" << endl;
    cout << "                    ,'_/  ,' !  /  !  ,' !  / |/ / ,' _/" << endl;
    cout << "                   / /_  / o | / o | / o | / || / _\ `." << endl;
    cout << "                   |__/  |_,' /__,'  |_,' /_/|_/ /___,' " << endl;
    cout << "                 ______________________________________" << endl;
    cout << "                 ======================================" << endl;
    cout << " " << endl;
    cout << " " << endl;

        cout << "" << endl;
    string CharacterName;
    cout << "Make sure you only enter 3 characters (using letters U A G C)" << endl;
    cout << " " << endl;
    cout << " " << endl;
    cout << "Enter Codon Arrangement: ";
    cin >> CharacterName;

    int NameLength = CharacterName.length();



    cout << "                        " << endl;


    if(NameLength==3) {

if	(CharacterName	==	"GCU")
cout	<<	"Alanine (ALA)"	<<	endl;
else if	(CharacterName	==	"GCC")
cout	<<	"Alanine (ALA)"	<<	endl;
else if	(CharacterName	==	"GCA")
cout	<<	"Alanine (ALA)"	<<	endl;
else if	(CharacterName	==	"GCG")
cout	<<	"Alanine (ALA)"	<<	endl;
else if	(CharacterName	==	"CGU")
cout	<<	"Arginine (ARG)"	<<	endl;
else if	(CharacterName	==	"CGC")
cout	<<	"Arginine (ARG)"	<<	endl;
else if	(CharacterName	==	"CGA")
cout	<<	"Arginine (ARG)"	<<	endl;
else if	(CharacterName	==	"CGG")
cout	<<	"Arginine (ARG)"	<<	endl;
else if	(CharacterName	==	"AGA")
cout	<<	"Arginine (ARG)"	<<	endl;
else if	(CharacterName	==	"AGG")
cout	<<	"Arginine (ARG)"	<<	endl;
else if	(CharacterName	==	"AAU")
cout	<<	"Asparagine (ASN)"	<<	endl;
else if	(CharacterName	==	"AAC")
cout	<<	"Asparagine (ASN)"	<<	endl;
else if	(CharacterName	==	"GAU")
cout	<<	"Aspartic Acid (ASP)"	<<	endl;
else if	(CharacterName	==	"GAC")
cout	<<	"Aspartic Acid (ASP)"	<<	endl;
else if	(CharacterName	==	"UGU")
cout	<<	"Cysteine (CYS)"	<<	endl;
else if	(CharacterName	==	"UGC")
cout	<<	"Cysteine (CYS)"	<<	endl;
else if	(CharacterName	==	"CAA")
cout	<<	"Glutamine (GLN)"	<<	endl;
else if	(CharacterName	==	"CAG")
cout	<<	"Glutamine (GLN)"	<<	endl;
else if	(CharacterName	==	"GAA")
cout	<<	"Glutamic Acid (GLU)"	<<	endl;
else if	(CharacterName	==	"GAG")
cout	<<	"Glutamic Acid (GLU)"	<<	endl;
else if	(CharacterName	==	"GGU")
cout	<<	"Glycine Acid (GLY)"	<<	endl;
else if	(CharacterName	==	"GGC")
cout	<<	"Glycine Acid (GLY)"	<<	endl;
else if	(CharacterName	==	"GGA")
cout	<<	"Glycine Acid (GLY)"	<<	endl;
else if	(CharacterName	==	"GGG")
cout	<<	"Glycine Acid (GLY)"	<<	endl;
else if	(CharacterName	==	"CAU")
cout	<<	"Histidine (HIS)"	<<	endl;
else if	(CharacterName	==	"CAC")
cout	<<	"Histidine (HIS)"	<<	endl;
else if	(CharacterName	==	"UUA")
cout	<<	"Leucine (Leu)"	<<	endl;
else if	(CharacterName	==	"UUG")
cout	<<	"Leucine (Leu)"	<<	endl;
else if	(CharacterName	==	"CUU")
cout	<<	"Leucine (Leu)"	<<	endl;
else if	(CharacterName	==	"CUC")
cout	<<	"Leucine (Leu)"	<<	endl;
else if	(CharacterName	==	"CUA")
cout	<<	"Leucine (Leu)"	<<	endl;
else if	(CharacterName	==	"CUG")
cout	<<	"Leucine (Leu)"	<<	endl;
else if	(CharacterName	==	"AUU")
cout	<<	"Leucine (Leu)"	<<	endl;
else if	(CharacterName	==	"AUC")
cout	<<	"Leucine (Leu)"	<<	endl;
else if	(CharacterName	==	"AUA")
cout	<<	"Leucine (Leu)"	<<	endl;
else if	(CharacterName	==	"AAA")
cout	<<	"Lysine (Lys)"	<<	endl;
else if	(CharacterName	==	"AAG")
cout	<<	"Lysine (Lys)"	<<	endl;
else if	(CharacterName	==	"AUG")
cout	<<	"Methionine (Met)"	<<	endl;
else if	(CharacterName	==	"UUU")
cout	<<	"Phenylalanine (Phe)"	<<	endl;
else if	(CharacterName	==	"UUC")
cout	<<	"Phenylalanine (Phe)"	<<	endl;
else if	(CharacterName	==	"CCU")
cout	<<	"Proline (Pro)"	<<	endl;
else if	(CharacterName	==	"CCC")
cout	<<	"Proline (Pro)"	<<	endl;
else if	(CharacterName	==	"CCA")
cout	<<	"Proline (Pro)"	<<	endl;
else if	(CharacterName	==	"CCG")
cout	<<	"Proline (Pro)"	<<	endl;
else if	(CharacterName	==	"UCU")
cout	<<	"Serine (ser)"	<<	endl;
else if	(CharacterName	==	"UCC")
cout	<<	"Serine (ser)"	<<	endl;
else if	(CharacterName	==	"UCA")
cout	<<	"Serine (ser)"	<<	endl;
else if	(CharacterName	==	"UCG")
cout	<<	"Serine (ser)"	<<	endl;
else if	(CharacterName	==	"AGU")
cout	<<	"Serine (ser)"	<<	endl;
else if	(CharacterName	==	"AGC")
cout	<<	"Serine (ser)"	<<	endl;
else if	(CharacterName	==	"UAA")
cout	<<	"STOP"	<<	endl;
else if	(CharacterName	==	"UAG")
cout	<<	"STOP"	<<	endl;
else if	(CharacterName	==	"UGA")
cout	<<	"STOP"	<<	endl;
else if	(CharacterName	==	"ACU")
cout	<<	"Threonine (thr)"	<<	endl;
else if	(CharacterName	==	"ACC")
cout	<<	"Threonine (thr)"	<<	endl;
else if	(CharacterName	==	"ACA")
cout	<<	"Threonine (thr)"	<<	endl;
else if	(CharacterName	==	"ACG")
cout	<<	"Threonine (thr)"	<<	endl;
else if	(CharacterName	==	"UGG")
cout	<<	"Tryptophan (Trp)"	<<	endl;
else if	(CharacterName	==	"UAU")
cout	<<	"Tyrosine (Tyr)"	<<	endl;
else if	(CharacterName	==	"UAC")
cout	<<	"Tyrosine (Tyr)"	<<	endl;
else if	(CharacterName	==	"GUU")
cout	<<	"Valine (Val)"	<<	endl;
else if	(CharacterName	==	"GUC")
cout	<<	"Valine (Val)"	<<	endl;
else if	(CharacterName	==	"GUA")
cout	<<	"Valine (Val)"	<<	endl;
else if	(CharacterName	==	"GUG")
cout	<<	"Valine (Val)"	<<	endl;

else if	(CharacterName	==	"gcu")
cout	<<	"Alanine (ALA)"	<<	endl;
else if	(CharacterName	==	"gcc")
cout	<<	"Alanine (ALA)"	<<	endl;
else if	(CharacterName	==	"gca")
cout	<<	"Alanine (ALA)"	<<	endl;
else if	(CharacterName	==	"gcg")
cout	<<	"Alanine (ALA)"	<<	endl;
else if	(CharacterName	==	"cgu")
cout	<<	"Arginine (ARG)"	<<	endl;
else if	(CharacterName	==	"cgc")
cout	<<	"Arginine (ARG)"	<<	endl;
else if	(CharacterName	==	"cga")
cout	<<	"Arginine (ARG)"	<<	endl;
else if	(CharacterName	==	"cgg")
cout	<<	"Arginine (ARG)"	<<	endl;
else if	(CharacterName	==	"aga")
cout	<<	"Arginine (ARG)"	<<	endl;
else if	(CharacterName	==	"agg")
cout	<<	"Arginine (ARG)"	<<	endl;
else if	(CharacterName	==	"aau")
cout	<<	"Asparagine (ASN)"	<<	endl;
else if	(CharacterName	==	"aac")
cout	<<	"Asparagine (ASN)"	<<	endl;
else if	(CharacterName	==	"gau")
cout	<<	"Aspartic Acid (ASP)"	<<	endl;
else if	(CharacterName	==	"gac")
cout	<<	"Aspartic Acid (ASP)"	<<	endl;
else if	(CharacterName	==	"ugu")
cout	<<	"Cysteine (CYS)"	<<	endl;
else if	(CharacterName	==	"ugc")
cout	<<	"Cysteine (CYS)"	<<	endl;
else if	(CharacterName	==	"caa")
cout	<<	"Glutamine (GLN)"	<<	endl;
else if	(CharacterName	==	"cag")
cout	<<	"Glutamine (GLN)"	<<	endl;
else if	(CharacterName	==	"gaa")
cout	<<	"Glutamic Acid (GLU)"	<<	endl;
else if	(CharacterName	==	"gag")
cout	<<	"Glutamic Acid (GLU)"	<<	endl;
else if	(CharacterName	==	"ggu")
cout	<<	"Glycine Acid (GLY)"	<<	endl;
else if	(CharacterName	==	"ggc")
cout	<<	"Glycine Acid (GLY)"	<<	endl;
else if	(CharacterName	==	"gga")
cout	<<	"Glycine Acid (GLY)"	<<	endl;
else if	(CharacterName	==	"ggg")
cout	<<	"Glycine Acid (GLY)"	<<	endl;
else if	(CharacterName	==	"cau")
cout	<<	"Histidine (HIS)"	<<	endl;
else if	(CharacterName	==	"cac")
cout	<<	"Histidine (HIS)"	<<	endl;
else if	(CharacterName	==	"uua")
cout	<<	"Leucine (Leu)"	<<	endl;
else if	(CharacterName	==	"uug")
cout	<<	"Leucine (Leu)"	<<	endl;
else if	(CharacterName	==	"cuu")
cout	<<	"Leucine (Leu)"	<<	endl;
else if	(CharacterName	==	"cuc")
cout	<<	"Leucine (Leu)"	<<	endl;
else if	(CharacterName	==	"cua")
cout	<<	"Leucine (Leu)"	<<	endl;
else if	(CharacterName	==	"cug")
cout	<<	"Leucine (Leu)"	<<	endl;
else if	(CharacterName	==	"auu")
cout	<<	"Leucine (Leu)"	<<	endl;
else if	(CharacterName	==	"auc")
cout	<<	"Leucine (Leu)"	<<	endl;
else if	(CharacterName	==	"aua")
cout	<<	"Leucine (Leu)"	<<	endl;
else if	(CharacterName	==	"aaa")
cout	<<	"Lysine (Lys)"	<<	endl;
else if	(CharacterName	==	"aag")
cout	<<	"Lysine (Lys)"	<<	endl;
else if	(CharacterName	==	"aug")
cout	<<	"Methionine (Met)"	<<	endl;
else if	(CharacterName	==	"uuu")
cout	<<	"Phenylalanine (Phe)"	<<	endl;
else if	(CharacterName	==	"uuc")
cout	<<	"Phenylalanine (Phe)"	<<	endl;
else if	(CharacterName	==	"ccu")
cout	<<	"Proline (Pro)"	<<	endl;
else if	(CharacterName	==	"ccc")
cout	<<	"Proline (Pro)"	<<	endl;
else if	(CharacterName	==	"cca")
cout	<<	"Proline (Pro)"	<<	endl;
else if	(CharacterName	==	"ccg")
cout	<<	"Proline (Pro)"	<<	endl;
else if	(CharacterName	==	"ucu")
cout	<<	"Serine (ser)"	<<	endl;
else if	(CharacterName	==	"ucc")
cout	<<	"Serine (ser)"	<<	endl;
else if	(CharacterName	==	"uca")
cout	<<	"Serine (ser)"	<<	endl;
else if	(CharacterName	==	"ucg")
cout	<<	"Serine (ser)"	<<	endl;
else if	(CharacterName	==	"agu")
cout	<<	"Serine (ser)"	<<	endl;
else if	(CharacterName	==	"agc")
cout	<<	"Serine (ser)"	<<	endl;
else if	(CharacterName	==	"uaa")
cout	<<	"STOP"	<<	endl;
else if	(CharacterName	==	"uag")
cout	<<	"STOP"	<<	endl;
else if	(CharacterName	==	"uga")
cout	<<	"STOP"	<<	endl;
else if	(CharacterName	==	"acu")
cout	<<	"Threonine (thr)"	<<	endl;
else if	(CharacterName	==	"acc")
cout	<<	"Threonine (thr)"	<<	endl;
else if	(CharacterName	==	"aca")
cout	<<	"Threonine (thr)"	<<	endl;
else if	(CharacterName	==	"acg")
cout	<<	"Threonine (thr)"	<<	endl;
else if	(CharacterName	==	"ugg")
cout	<<	"Tryptophan (Trp)"	<<	endl;
else if	(CharacterName	==	"uau")
cout	<<	"Tyrosine (Tyr)"	<<	endl;
else if	(CharacterName	==	"uac")
cout	<<	"Tyrosine (Tyr)"	<<	endl;
else if	(CharacterName	==	"guu")
cout	<<	"Valine (Val)"	<<	endl;
else if	(CharacterName	==	"guc")
cout	<<	"Valine (Val)"	<<	endl;
else if	(CharacterName	==	"gua")
cout	<<	"valine (val)"	<<	endl;
else if	(CharacterName	==	"gug")
cout	<<	"Valine (Val)"	<<	endl;

else cout << "You had made incorrect combination, Make sure you use only Letter U A G C (case sensitive either all capital or all small not mix)" << endl;}

        else cout << "Letters are less then or more then 3" << endl;


    cout << " " << endl;
    cout << " " << endl;
    cout << " " << endl;
    cout <<"Do you wish to search for another combination (Y/N)";

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
