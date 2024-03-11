#include<iostream>
#include<thread>
#include<unistd.h>
#include<mutex>

using namespace std;


int count = 0;
mutex Mutex;


void task(){
    Mutex.lock();
    extern int count;
    for(int i=0;i<100000;i++){
        count=count+1;
        fflush(stdout);
    }
    Mutex.unlock();
}

int main(){
    extern int count;
    thread t1(task);
    thread t2(task);

    t1.join();
    t2.join();

    cout<<count<<endl;
    return 0;
}