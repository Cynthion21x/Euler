#include <iostream>

int main(int argv, char* argc[]) {

    int total = 0;

    for (int i = 0; i < 1000; i++) {

        if (i % 3 == 0) {
            total += i;
        }

        if (i % 5 == 0) {
            total += i;
        }

    }

    std::cout << total;

}