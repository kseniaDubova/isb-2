
#include <iostream>
#include <ctime>
#include <cstdlib>

int main()
{
    srand(time(0));
    for (int i = 0; i < 128; i++)
    {
        unsigned long long num = std::rand() % 5000;
        if (num % 2 == 0)
            std::cout << 0;
        else std::cout << 1;
    }
    return 0;
}
//00011101110111100010101000010101000110010011011001010101110000010110100110101000101111011110000001001100101101101010011111111001
