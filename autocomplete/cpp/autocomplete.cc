#include <iostream>
#include <stdio.h>
#include <cstdlib>
using namespace std;

// To compile: g++ autocomplete.cc -o autocomplete.o
// To run: ./autocomplete.o

char CTRL_C = '\003';

char get_input() {
  system("stty raw opost -echo");
  char input = getchar();
  system("stty cooked");
  return input;
}

int main() {
  cout << "Waiting for input...\n";

  char input = get_input();
  if (input != CTRL_C) {
    cout << "Got input:" << input << "\n";
  }

  return 0;
}
