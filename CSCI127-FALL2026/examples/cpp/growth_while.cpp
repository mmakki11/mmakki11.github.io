//While Growth example
// Source: index.html week 13 — "Growth Example (C++)"  (was onlinegdb.com/rk86urUlf)
#include <iostream>
using namespace std;

int main ()
{
  int population = 100;
  int year = 0;
  cout << "Year\tPopulation\n";
  while (population < 1000)
  {
      cout << year << "\t" << population << "\n";
      population = population * 2;
  }
  return 0;
}
