#include "sparkle.h"
#include <vector>
#include <string>

int main() {
    sparkle();

    std::vector<std::string> vec;
    vec.push_back("test_package");

    sparkle_print_vector(vec);
}
