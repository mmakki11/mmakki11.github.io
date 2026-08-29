//Demonstrates do-while loops (input checking)
// Source: index.html week 13 — "Input Checking, II (C++)"  (was onlinegdb.com/Bkn8DB8eG)
#include <iostream>
using namespace std;

int main ()
{
  int num;
  do
  {
      cout << "Enter an even number: ";
      cin >> num;
  } while (num % 2 != 0);

  cout << "You entered: "
       << num << ".\n";
  return 0;
}
