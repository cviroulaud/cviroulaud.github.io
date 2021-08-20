#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
  for (int i = 0; i < 25; i = i + 2) {
    printf("%d ", i);
  }
  return 0;
}