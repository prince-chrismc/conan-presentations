#include <iostream>
#include "game.h"
#include "engine.h"


void game(){
    engine();
    #ifdef NDEBUG
    std::cout << "game/1.0: Hello World Release!\n";
    #else
    std::cout << "game/1.0: Hello World Debug!\n";
    #endif

}
