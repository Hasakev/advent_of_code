#include <iostream>
#include <fstream>
#include <string>

int main () {
std::ifstream reader; reader.open("test.txt");

if (reader.is_open()) {
    char line;
    while (reader) {
        line = reader.get();
        std::cout << line;
    }
}

}