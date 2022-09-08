#include <iostream>
#include "mymath.h"

#define STRINGIFY(x) #x
#define STRINGIFYMACRO(y) STRINGIFY(y)

void math(){
    #ifdef NDEBUG
    std::cout << "math/" << STRINGIFYMACRO(PKG_VERSION)  << ": Hello World Release!\n";
    #else
    std::cout << "math/" << STRINGIFYMACRO(PKG_VERSION) << ": Hello World Debug!\n";
    #endif
}
