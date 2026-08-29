//Demonstrates loops (input checking with while)
// Source: index.html week 13 — "Input Checking (C++)"  (was onlinegdb.com/rJttLSLgG)
#include <iostream>
using namespace std;

int main ()
{
  int num;
  cout << "Enter an even number: ";
  cin >> num;
  while (num % 2 != 0)
  {
      cout << "\nThat's odd!\n";
      cout << "Enter an even number: ";
      cin >> num;
  }
  cout << "You entered: "
       << num << ".\n";
  return 0;
}
