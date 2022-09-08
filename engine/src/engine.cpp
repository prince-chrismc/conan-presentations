#include <iostream>
#include "engine.h"
#include "mymath.h"

void engine(){
    math();
    #ifdef NDEBUG
    std::cout << "engine/1.0: Hello World Release!\n";
    #else
    std::cout << "engine/1.0: Hello World Debug!\n";
    #endif
}
