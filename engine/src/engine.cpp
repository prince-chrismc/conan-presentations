#include <iostream>
#include "engine.h"
#include "mymath.h"

#define STRINGIFY(x) #x
#define STRINGIFYMACRO(y) STRINGIFY(y)


void engine(){
    math();
    #ifdef NDEBUG
    std::cout << "engine/" << STRINGIFYMACRO(PKG_VERSION)  << ": Hello World Release!\n";
    #else
    std::cout << "engine/" << STRINGIFYMACRO(PKG_VERSION)  << ": Hello World Debug!\n";
    #endif
}
