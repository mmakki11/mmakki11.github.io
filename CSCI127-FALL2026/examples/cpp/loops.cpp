//Another C++ program; Demonstrates loops
// Source: index.html week 12 — "Loops example"  (was onlinegdb.com/HktpcoT1f)
#include <iostream>
using namespace std;

int main ()
{
  int i,j;
  for (i = 0; i < 4; i++)
  {
      cout << "The world turned upside down...\n";
  }

  for (j = 10; j > 0; j--)
  {
      cout << j << " ";
  }
  cout << "Blast off!!" << endl;

  return 0;
}
