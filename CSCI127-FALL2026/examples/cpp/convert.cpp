//Another C++ program, demonstrating I/O & arithmetic
// Source: index.html week 12 — "Convert example"  (was onlinegdb.com/BkT2_jT1z)
#include <iostream>
using namespace std;

int main ()
{
  float kg, lbs;
  cout << "Enter kg: ";
  cin >> kg;
  lbs = kg * 2.2;
  cout << endl << "Lbs: " << lbs << "\n\n";
  return 0;
}
