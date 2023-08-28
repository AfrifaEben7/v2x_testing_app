#include <iostream>
#include <string>
#include <ctime>
#include <fstream>
#include <vector>
#include <cmath>
#include <cstring>
#include <cstdlib>

// Include appropriate headers for your platform
#ifdef _WIN32
#include <Windows.h>
#else
#include <dlfcn.h>
#endif

struct SEScenarioObjectState {
    int id;
    int model_id;
    int control;
    float timestamp;
    float x, y, z;
    float h, p, r;
    int roadId, junctionId;
    float t;
    int laneId;
    float laneOffset;
    float s;
    float speed;
    float centerOffsetX, centerOffsetY, centerOffsetZ;
    float width, length, height;
    int objectType;
    int objectCategory;
    float wheelAngle, wheelRot;
};

int main() {
    // Load the shared library
    #ifdef _WIN32
    HINSTANCE se = LoadLibrary("../esmini/bin/esminiLib.dll");
    #else
    void* se = dlopen("../esmini/bin/libesminiLib.so", RTLD_LAZY);
    #endif

    if (!se) {
        std::cerr << "Failed to load the shared library." << std::endl;
        return 1;
    }

    
    SEScenarioObjectState obj_state;

    // shared library
    #ifdef _WIN32
    FreeLibrary(se);
    #else
    dlclose(se);
    #endif

    return 0;
}
