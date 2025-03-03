#include <iostream>

int main(int argv, char* argc[]) {

    int x = 1;
    int y = 2;

    int sum = 0;

    while (x < 1000000) {

        int z = y;

        y += x;
        x = z;

        if (x % 2 == 0) {

            sum += x;

        }

    }

    std::cout << sum;

}