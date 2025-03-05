#include <iostream>

int reverseNumber(int num) {

    int ans = 0;
    int temp = num;

    while (temp > 0) {

        int lastDigit = temp % 10;

        ans = ans * 10 + lastDigit;

        temp = temp / 10;

    }

    return ans;

}

bool isProductOf(int num) {

    for (int i = 100; i < 999; i++) {

        if (num % i == 0) {

            int j = num / i;

            if (j >= 100 && j <= 999) {

                return true;

            }

        }

    }

    return false;

}

int main(int argv, char* argc[]) {

    int largestPalindrome = 0;

    for (int i = 100*100; i < 999*999; i++) {
        
        if (i == reverseNumber(i)) {

            if (isProductOf(i)) {

                if (i > largestPalindrome) {

                    largestPalindrome = i;

                }

            }
        }

    }

    std::cout << largestPalindrome;

}