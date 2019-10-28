/**
* @file main.cpp
* @brief Implementation main method
* @author $Author:$ Holanda, Gabriel Bandeira
* @version $Revision:$
* @date $Date:$ 21/03/2019
*/

// System Heders
#include <chrono>
#include <thread>
#include <string>
#include <vector>
#include <time.h>
#include <ctime>
#include <iostream>
#include <dirent.h>
#include <math.h>

using namespace std;

int main(int argc, char** argv){

  float hour = 11;
  float maxTimeSec = hour*60*60;
  double elapsed_time_sec = 0;
  auto t_start = std::chrono::high_resolution_clock::now();
  bool run = true;
  while(run){

    auto t_end = std::chrono::high_resolution_clock::now();
    elapsed_time_sec = std::chrono::duration<double, std::milli>(t_end-t_start).count();
    elapsed_time_sec = elapsed_time_sec/1000;

    if(elapsed_time_sec>maxTimeSec){
      string command = "pkill -9 darknet";
      printf("%s\n",command.c_str());
      system(command.c_str());
      run = false;
    }
    std::this_thread::sleep_for(std::chrono::milliseconds(1000)); // wait 60 seconds..
    printf("%f\n",elapsed_time_sec);
  }
  // rodar o comando para subir as coisas no drive
  string command = "python /content/darknet/uploadDriver.py";
  printf("%s\n",command.c_str());
  system(command.c_str());

  return 0;
}
